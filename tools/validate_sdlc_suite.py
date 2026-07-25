#!/usr/bin/env python3
"""Validate packaged SDLC Command Desk artifacts against the current suite layout.

Reference and key names track the active capability profile
(profiles/frontier-2026-07.yaml). If a profile bump renames a kernel reference,
update REQ_REFS here in the same commit or this validator will report false failures.
The generic (vendor-neutral) build is the validation target; vendor builds live
under dist/vendor/<vendor>/ and carry agents/<vendor>.yaml instead.
"""
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "skills" / "SDLC Command Desk"
DIST = REPO / "dist" / "skills" / "sdlc-command-desk"
PACKAGES = REPO / "dist" / "packages" / "sdlc-command-desk"
# Version is read from MANIFEST.md rather than hardcoded, so cutting a release does not
# require editing this file. Hardcoding it is what made this validator fail on v1.0.0.
def _active_version() -> str:
    import re as _re
    m = _re.search(r"sdlc-command-desk-v(\d+\.\d+\.\d+)", MANIFEST_TEXT)
    return m.group(1) if m else "0.0.0"
MANIFEST = REPO / "MANIFEST.md"
MANIFEST_TEXT = MANIFEST.read_text(encoding="utf-8") if MANIFEST.exists() else ""

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
    "goliveprompt",
]
# Skills that are protocol runners rather than lifecycle stages. They carry their own
# state (goliveprompt uses tracker.json and a fixed six-phase sequence), so requiring the
# suite workflow packet on top would duplicate state and create two sources of truth for
# where a run is. They still must adopt the halt taxonomy and the capability baseline.
STAGE_EXEMPT = {"goliveprompt"}
EXEMPT_REQ_REFS = ["halt-taxonomy.md", "capability-baseline.md"]

REQ_REFS = [
    "continuity-kernel.md",
    "readiness-gates.md",
    "halt-taxonomy.md",
    "preflight-cache.md",
    "handoff-density-policy.md",
    "capability-baseline.md",
    "suite-workflow-contract.md",
]
RUNNER_KEYS = [
    "repo_context",
    "evidence_inventory",
    "allowed_scope",
    "forbidden_scope",
    "validation_commands",
    "implementation_handoff",
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
    agent_yaml = packaged / "agents" / "generic.yaml"

    check(source_md.exists(), f"source markdown exists: {source_md.relative_to(REPO)}")
    check(packaged.exists(), f"packaged skill dir exists: {packaged.relative_to(REPO)}")
    check(skill_md.exists(), f"SKILL.md exists: {skill_md.relative_to(REPO)}")
    check(agent_yaml.exists(), f"agents/generic.yaml exists: {agent_yaml.relative_to(REPO)}")

    text = skill_md.read_text(encoding="utf-8") if skill_md.exists() else ""
    if name in STAGE_EXEMPT:
        for ref in EXEMPT_REQ_REFS:
            ref_path = packaged / "references" / ref
            check(ref_path.exists(), f"reference {ref}: {name} (protocol runner)")
    else:
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

VERSION = _active_version()
RELEASE_NOTES = REPO / "releases" / f"sdlc-command-desk-v{VERSION}.md"
check(RELEASE_NOTES.exists(), f"release notes exist: {RELEASE_NOTES.relative_to(REPO)}")
check(f"sdlc-command-desk-v{VERSION}" in MANIFEST_TEXT, f"MANIFEST references sdlc-command-desk-v{VERSION}")

if failures:
    print(f"\nSDLC validation failed: {len(failures)} issue(s)")
    sys.exit(1)

print("\nSDLC validation passed")
