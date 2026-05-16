#!/usr/bin/env python3
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"
EXPECTED = [
"sdlc-command-desk","product-requirements-desk","technical-discovery-desk","architecture-design-desk","issue-planning-desk","implementation-handoff-desk","review-quality-desk","test-strategy-desk","verification-desk","docs-traceability-desk","security-threat-desk","ci-failure-desk","release-operations-desk","deployment-desk","observability-readiness-desk","incident-response-desk","maintenance-refactor-desk","retrospective-desk","decommissioning-desk"
]
REQ_REFS = ["continuity-kernel.md","readiness-gates.md","halt-taxonomy.md","preflight-cache.md","codex-conservation-policy.md","suite-workflow-contract.md"]

def fail(msg):
    print(f"FAIL: {msg}")
    return 1

def ok(msg):
    print(f"OK: {msg}")

rc = 0
for name in EXPECTED:
    d = SKILLS / name
    if not d.exists(): rc |= fail(f"missing skill dir {name}")
    if not (d / "SKILL.md").exists(): rc |= fail(f"missing SKILL.md {name}")
    if not (d / "agents" / "openai.yaml").exists(): rc |= fail(f"missing agents/openai.yaml {name}")
    s = (d / "SKILL.md").read_text(encoding="utf-8") if (d / "SKILL.md").exists() else ""
    if "Suite workflow mode" not in s: rc |= fail(f"missing suite workflow mode text {name}")
    if "Continuity Kernel Adoption" not in s: rc |= fail(f"missing continuity section {name}")
    for rf in REQ_REFS:
        if not (d / "references" / rf).exists(): rc |= fail(f"missing {rf} in {name}")

runner = REPO / "skills" / "sdlc-command-desk" / "scripts" / "run_sdlc_workflow.py"
if runner.exists():
    rt = runner.read_text(encoding="utf-8")
    for key in ["repo_context", "evidence_inventory", "allowed_scope", "forbidden_scope", "validation_commands", "codex_handoff"]:
        if key not in rt:
            rc |= fail(f"runner missing key {key}")
else:
    rc |= fail("missing run_sdlc_workflow.py")

manifest = (REPO / "MANIFEST.md")
if manifest.exists() and "v0.2.0-rc.1" not in manifest.read_text(encoding="utf-8"):
    rc |= fail("MANIFEST.md does not reference v0.2.0-rc.1")

rels = REPO / "releases"
if not (rels / "v0.2.0-rc.1.md").exists(): rc |= fail("missing releases/v0.2.0-rc.1.md")
if not (rels / "RELEASE_BODY-v0.2.0-rc.1.md").exists(): rc |= fail("missing releases/RELEASE_BODY-v0.2.0-rc.1.md")
if not (rels / "publish-v0.2.0-rc.1.ps1").exists(): rc |= fail("missing releases/publish-v0.2.0-rc.1.ps1")


if rc == 0:
    ok("suite validation passed")
sys.exit(rc)

