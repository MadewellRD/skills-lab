#!/usr/bin/env python3
"""Deterministic first-pass SDLC route helper.

This script is intentionally conservative. It provides a starting route from
keywords, then the skill must apply connector evidence and judgment.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from typing import Iterable


@dataclass(frozen=True)
class Route:
    stage: int
    stage_name: str
    desk: str
    confidence: str
    reason: str
    required_context: list[str]


ROUTES: list[tuple[tuple[str, ...], Route]] = [
    (("incident", "outage", "sev", "production down", "rca", "hotfix"), Route(20, "incident response and production support", "incident-response-desk", "medium", "production support or incident language detected", ["incident facts", "recent deploys", "logs or symptoms"])),
    (("ci", "github actions", "workflow", "failed check", "build failed", "flake", "failing test"), Route(16, "ci/cd, build, and pipeline health", "ci-failure-desk", "medium", "ci or build failure language detected", ["repo", "commit or PR", "workflow run or logs"])),
    (("release", "changelog", "version", "tag", "rollback", "release notes"), Route(17, "release planning and release operations", "release-operations-desk", "medium", "release readiness language detected", ["merged PRs", "ci status", "release target"])),
    (("deploy", "rollout", "feature flag", "go/no-go", "canary", "change management"), Route(18, "deployment, rollout, and change management", "deployment-desk", "medium", "deployment or rollout language detected", ["deployment target", "release artifact", "monitoring checkpoints"])),
    (("observability", "telemetry", "metrics", "logs", "traces", "slo", "alert", "runbook"), Route(19, "observability and operational readiness", "observability-readiness-desk", "medium", "observability readiness language detected", ["service/component", "available telemetry", "operational goals"])),
    (("retire", "sunset", "decommission", "end of life", "eol", "archive"), Route(25, "decommissioning and end-of-life", "decommissioning-desk", "medium", "retirement or decommissioning language detected", ["system or feature", "consumers", "retention policy"])),
    (("retro", "retrospective", "lessons learned", "cycle metrics", "process improvement"), Route(24, "retrospective and continuous improvement", "retrospective-desk", "medium", "retrospective language detected", ["cycle scope", "timeline", "outcomes"])),
    (("refactor", "dependency", "upgrade", "dead code", "migration cleanup", "technical debt"), Route(21, "maintenance, refactoring, dependency management", "maintenance-refactor-desk", "medium", "maintenance or refactor language detected", ["repo", "affected areas", "regression constraints"])),
    (("threat", "security", "privacy", "authz", "authn", "secret", "dependency risk", "trust boundary"), Route(9, "security, privacy, and threat modeling", "security-threat-desk", "medium", "security or threat modeling language detected", ["architecture or code context", "data/auth boundaries"])),
    (("traceability", "proof map", "claim map", "doc-code", "documentation drift"), Route(22, "documentation and proof maps", "docs-traceability-desk", "medium", "documentation traceability language detected", ["docs", "repo files", "claims to verify"])),
    (("verify", "validation", "v&v", "acceptance gate", "rtm", "traceability matrix"), Route(15, "verification, validation, and traceability", "verification-desk", "medium", "verification language detected", ["requirements", "test evidence", "PRs or commits"])),
    (("test strategy", "qa", "regression", "fixture", "coverage gap", "scenario"), Route(14, "test planning and qa strategy", "test-strategy-desk", "medium", "test planning language detected", ["requirements", "existing tests", "risk areas"])),
    (("review", "pr review", "diff", "request changes", "scope creep", "approve"), Route(13, "code review and change quality", "review-quality-desk", "medium", "review language detected", ["PR or diff", "checks", "test expectations"])),
    (("pr prompt", "pull request", "branch", "commit", "coding agent", "codex", "claude code", "halt resume", "merge train", "implementation handoff"), Route(12, "implementation handoff, branch, and pr operations", "implementation-handoff-desk", "medium", "implementation handoff language detected", ["repo", "scope", "base branch", "validation commands"])),
    (("issue", "milestone", "dependency graph", "sprint", "break down", "decompose", "labels"), Route(10, "planning, decomposition, issue generation", "issue-planning-desk", "medium", "planning or issue decomposition language detected", ["requirements", "design context", "target tracker"])),
    (("architecture", "design", "adr", "interface", "api contract", "migration plan", "component"), Route(6, "architecture and solution design", "architecture-design-desk", "medium", "architecture or design language detected", ["requirements", "technical constraints", "repo topology"])),
    (("feasibility", "technical discovery", "spike", "repo recon", "unknowns", "dependency research"), Route(5, "technical discovery and feasibility", "technical-discovery-desk", "medium", "technical discovery language detected", ["problem statement", "repo/docs", "unknowns"])),
    (("requirements", "prd", "acceptance criteria", "non-goals", "product brief", "roadmap"), Route(3, "product requirements", "product-requirements-desk", "medium", "requirements language detected", ["idea or problem", "stakeholder context", "source facts"])),
]

DEFAULT_ROUTE = Route(3, "product requirements", "product-requirements-desk", "low", "default to earliest product requirements stage when intent is ambiguous", ["problem statement", "goals", "known constraints"])


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def choose_route(text: str) -> Route:
    haystack = normalize(text)
    for keywords, route in ROUTES:
        if any(k in haystack for k in keywords):
            return route
    return DEFAULT_ROUTE


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="route an SDLC request to a desk skill")
    parser.add_argument("request", nargs="*", help="request text to route")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args(list(argv) if argv is not None else None)
    text = " ".join(args.request).strip()
    if not text:
        parser.error("request text is required")
    route = choose_route(text)
    if args.json:
        print(json.dumps(asdict(route), indent=2))
    else:
        print(f"selected desk: {route.desk}")
        print(f"stage: {route.stage} - {route.stage_name}")
        print(f"confidence: {route.confidence}")
        print(f"reason: {route.reason}")
        print("required context:")
        for item in route.required_context:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
