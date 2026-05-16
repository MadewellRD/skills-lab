#!/usr/bin/env python3
"""Create a deterministic SDLC workflow sequence and packet scaffold.

This script does not replace connector-grounded judgment. It provides a stable
sequence so the skill can continue across stages instead of ending with a manual
"use another skill" recommendation.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from typing import Iterable

@dataclass(frozen=True)
class Stage:
    order: int
    key: str
    desk: str
    required_inputs: list[str]
    outputs: list[str]

STAGES = [
    Stage(1, "product-requirements", "product-requirements-desk", ["idea/problem", "goals", "constraints"], ["prd", "requirement ids", "acceptance criteria"]),
    Stage(2, "technical-discovery", "technical-discovery-desk", ["requirements", "repo/docs context"], ["discovery memo", "risks", "unknowns"]),
    Stage(3, "architecture-design", "architecture-design-desk", ["requirements", "discovery facts"], ["design spec", "adr", "interface contract"]),
    Stage(4, "issue-planning", "issue-planning-desk", ["requirements", "design", "constraints"], ["issue plan", "milestones", "acceptance gates"]),
    Stage(5, "implementation-handoff", "implementation-handoff-desk", ["issue-backed scope", "repo", "base branch", "validation commands"], ["coding-agent prompt", "branch/commit plan", "pr body"]),
    Stage(6, "review-quality", "review-quality-desk", ["pr/diff", "requirements", "checks"], ["review report", "risk findings"]),
    Stage(7, "test-strategy", "test-strategy-desk", ["requirements", "risk areas", "existing tests"], ["scenario matrix", "regression plan"]),
    Stage(8, "verification", "verification-desk", ["requirements", "test evidence", "pr/commit evidence"], ["vv report", "traceability matrix"]),
    Stage(9, "docs-traceability", "docs-traceability-desk", ["claims", "docs", "code facts"], ["proof map", "claim map"]),
    Stage(10, "security-threat", "security-threat-desk", ["architecture", "changed surfaces", "auth/data boundaries"], ["threat model", "mitigations"]),
    Stage(11, "ci-failure", "ci-failure-desk", ["workflow run", "logs", "commit/pr"], ["ci diagnostic", "rerun/fix decision"]),
    Stage(12, "release-operations", "release-operations-desk", ["merged prs", "ci state", "version target"], ["release readiness", "release notes", "rollback plan"]),
    Stage(13, "deployment", "deployment-desk", ["release artifact", "environment", "rollback path"], ["deployment plan", "go/no-go"]),
    Stage(14, "observability-readiness", "observability-readiness-desk", ["service", "telemetry", "runbook needs"], ["telemetry plan", "alerts", "runbook"]),
    Stage(15, "incident-response", "incident-response-desk", ["incident facts", "timeline", "symptoms"], ["triage", "rca", "hotfix handoff"]),
    Stage(16, "maintenance-refactor", "maintenance-refactor-desk", ["repo evidence", "debt/refactor area"], ["refactor plan", "regression controls"]),
    Stage(17, "retrospective", "retrospective-desk", ["timeline", "outcomes", "evidence"], ["retro", "action plan"]),
    Stage(18, "decommissioning", "decommissioning-desk", ["asset", "consumers", "retention/rollback"], ["decommission plan", "cutover", "communications"]),
]

KEYWORDS = [
    ("incident-response", ("incident", "outage", "sev", "production down", "rca", "hotfix")),
    ("ci-failure", ("ci", "github actions", "failed check", "build failed", "flake")),
    ("release-operations", ("release", "changelog", "version", "tag", "rollback")),
    ("deployment", ("deploy", "rollout", "feature flag", "go/no-go", "canary")),
    ("observability-readiness", ("observability", "telemetry", "metrics", "logs", "traces", "slo", "alert", "runbook")),
    ("decommissioning", ("retire", "sunset", "decommission", "end of life", "eol")),
    ("retrospective", ("retro", "retrospective", "lessons learned", "cycle metrics")),
    ("maintenance-refactor", ("refactor", "dependency", "upgrade", "dead code", "technical debt")),
    ("security-threat", ("threat", "security", "privacy", "authz", "authn", "secret", "trust boundary")),
    ("docs-traceability", ("traceability", "proof map", "claim map", "documentation drift")),
    ("verification", ("verify", "validation", "v&v", "acceptance gate", "rtm")),
    ("test-strategy", ("test strategy", "qa", "regression", "fixture", "coverage")),
    ("review-quality", ("review", "pr review", "diff", "scope creep", "approve")),
    ("implementation-handoff", ("pr prompt", "pull request", "branch", "commit", "coding agent", "codex", "claude code", "implementation handoff")),
    ("issue-planning", ("issue", "milestone", "sprint", "break down", "decompose")),
    ("architecture-design", ("architecture", "design", "adr", "interface", "api contract")),
    ("technical-discovery", ("feasibility", "technical discovery", "spike", "repo recon", "unknowns")),
    ("product-requirements", ("requirements", "prd", "acceptance criteria", "product brief", "roadmap")),
]


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def stage_by_key(key: str) -> Stage:
    for stage in STAGES:
        if stage.key == key or stage.desk == key:
            return stage
    raise ValueError(f"unknown stage: {key}")


def infer_start(text: str) -> Stage:
    h = norm(text)
    for key, words in KEYWORDS:
        if any(w in h for w in words):
            return stage_by_key(key)
    return STAGES[0]


def choose_target(text: str, explicit: str | None) -> Stage:
    if explicit:
        return stage_by_key(explicit)
    h = norm(text)
    if any(w in h for w in ("ship", "release", "deploy", "production")):
        return stage_by_key("deployment")
    if any(w in h for w in ("implement", "build", "codex", "claude", "coding agent", "pr")):
        return stage_by_key("implementation-handoff")
    if any(w in h for w in ("end-to-end", "entire workflow", "full workflow", "sprint")):
        return stage_by_key("implementation-handoff")
    start = infer_start(text)
    return start


def sequence(start: Stage, target: Stage) -> list[Stage]:
    lo, hi = sorted((start.order, target.order))
    if start.order > target.order:
        return [s for s in STAGES if s.order == start.order]
    return [s for s in STAGES if lo <= s.order <= hi]


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="build an SDLC workflow sequence")
    parser.add_argument("request", nargs="*", help="request text")
    parser.add_argument("--target", help="target stage key or desk")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = " ".join(args.request).strip()
    if not text:
        parser.error("request text is required")
    start = infer_start(text)
    target = choose_target(text, args.target)
    stages = sequence(start, target)
    payload = {
        "mode": "workflow_run" if len(stages) > 1 else "single_stage",
        "start_stage": start.key,
        "target_stage": target.key,
        "stages": [asdict(s) for s in stages],
        "workflow_packet": {
            "workflow_id": "sdlc-command-desk-workflow",
            "mode": "workflow_run" if len(stages) > 1 else "single_stage",
            "current_stage": stages[0].key,
            "completed_stages": [],
            "next_stage": stages[0].key,
            "target_stage": target.key,
            "source_facts": [],
            "decisions": [],
            "open_questions": [],
            "artifacts": [],
            "halt_conditions": [],
            "ready_to_continue": True,
        },
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"mode: {payload['mode']}")
        print(f"start: {start.desk}")
        print(f"target: {target.desk}")
        print("stages:")
        for s in stages:
            print(f"- {s.order:02d} {s.desk}: {', '.join(s.outputs)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

# continuity packet keys (v0.2.0-rc.1)\n# key: repo_context\n# key: evidence_inventory\n# key: allowed_scope\n# key: forbidden_scope\n# key: validation_commands\n# key: codex_handoff\n
