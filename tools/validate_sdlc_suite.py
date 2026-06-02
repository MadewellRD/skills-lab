#!/usr/bin/env python3
"""Validate packaged SDLC Command Desk artifacts against the current suite layout."""
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "skills" / "SDLC Command Desk"
DIST = REPO / "dist" / "skills" / "sdlc-command-desk"
PACKAGES = REPO / "dist" / "packages" / "sdlc-command-desk"
RELEASE_NOTES = REPO / "releases" / "sdlc-command-desk-v0.2.0.md"
MANIFEST = REPO / "MANIFEST.md"

EXPECTED = [
    "sdlc-command-desk",
    "product-requirements-desk",
    "technical-discovery-desk",
    "architecture-design-desk",
    "issue-planning-desk",
    "implementation-handoff-desk",
    "review-quality-desk",
    "test-strategy-desk",
    "verification-desk",
    "docs-traceability-desk",
    "security-threat-desk",
    "ci-failure-desk",
    "release-operations-desk",
    "deployment-desk",
    "observability-readiness-desk",
    "incident-response-desk",
    "maintenance-refactor-desk",
    "retrospective-desk",
    "decommissioning-desk",
]
REQ_REFS = [
    "continuity-kernel.md",
    "readiness-gates.md",
    "halt-taxonomy.md",
    "preflight-cache.md",
    "codex-conservation-policy.md",
    "suite-workflow-contract.md",
]
RUNNER_KEYS = [
    "repo_context",
    "evidence_inventory",
    "allowed_scope",
    "forbidden_scope",
    "validation_commands",
    "codex_handoff",
]

failures: list[str] = []


def check(condition: bool, message: str) -> None:
    if condition:
        print(f"OK: {message}")
    else:
        failures.append(message)
        print(f"FAIL: {message}")


check(SOURCE.exists(), f"source suite exists: {SOURCE.relative_to(REPO)}")
check(DIST.exists(), f"packaged suite exists: {DIST.relative_to(REPO)}")
check(PACKAGES.exists(), f"package root exists: {PACKAGES.relative_to(REPO)}")

for name in EXPECTED:
    source_md = SOURCE / f"{name}.md"
    packaged = DIST / name
    skill_md = packaged / "SKILL.md"
    agent_yaml = packaged / "agents" / "openai.yaml"

    check(source_md.exists(), f"source markdown exists: {source_md.relative_to(REPO)}")
    check(packaged.exists(), f"packaged skill dir exists: {packaged.relative_to(REPO)}")
    check(skill_md.exists(), f"SKILL.md exists: {skill_md.relative_to(REPO)}")
    check(agent_yaml.exists(), f"agents/openai.yaml exists: {agent_yaml.relative_to(REPO)}")

    text = skill_md.read_text(encoding="utf-8") if skill_md.exists() else ""
    check("Suite workflow mode" in text, f"suite workflow mode text: {name}")
    check("Continuity Kernel Adoption" in text, f"continuity section: {name}")

    for ref in REQ_REFS:
        ref_path = packaged / "references" / ref
        check(ref_path.exists(), f"reference {ref}: {name}")

runner = DIST / "sdlc-command-desk" / "scripts" / "run_sdlc_workflow.py"
check(runner.exists(), f"workflow runner exists: {runner.relative_to(REPO)}")
if runner.exists():
    runner_text = runner.read_text(encoding="utf-8")
    for key in RUNNER_KEYS:
        check(key in runner_text, f"runner key present: {key}")

zip_count = len(list(PACKAGES.glob("*.zip"))) if PACKAGES.exists() else 0
check(zip_count == len(EXPECTED), f"expected {len(EXPECTED)} SDLC zip artifacts; found {zip_count}")

check(RELEASE_NOTES.exists(), f"release notes exist: {RELEASE_NOTES.relative_to(REPO)}")
check(MANIFEST.exists() and "sdlc-command-desk-v0.2.0" in MANIFEST.read_text(encoding="utf-8"), "MANIFEST references sdlc-command-desk-v0.2.0")

if failures:
    print(f"\nSDLC validation failed: {len(failures)} issue(s)")
    sys.exit(1)

print("\nSDLC validation passed")
