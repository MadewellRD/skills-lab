from __future__ import annotations

import importlib.util
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = ROOT / "tools" / "generate_sales_command_desk_release.py"
CORRECT_SUITE_DIR = ROOT / "skills" / "Sales Command Desk"
WRONG_SUITE_DIR = ROOT / "skills" / "Sales Revenue Command Desk"
VERSION = "0.1.0"

spec = importlib.util.spec_from_file_location("sales_generator", GENERATOR_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)

DESKS = module.DESKS

CORRECT_SUITE_DIR.mkdir(parents=True, exist_ok=True)
(CORRECT_SUITE_DIR / "references").mkdir(parents=True, exist_ok=True)
(CORRECT_SUITE_DIR / "references" / "stage-contracts").mkdir(parents=True, exist_ok=True)
(CORRECT_SUITE_DIR / "references" / "desk-workflows").mkdir(parents=True, exist_ok=True)

readme = """# Sales Command Desk

Status: v0.1.0 packaged suite source.

This folder contains the authoring source for the Sales Command Desk suite. Each desk has a top-level Markdown source spec and a related reference artifact under `references/stage-contracts/` and `references/desk-workflows/`.

Generated ChatGPT skill folders remain under `dist/skills/sales-command-desk/`. Zip bundles, manifests, and checksums remain generated under `dist/packages/sales-command-desk/`, `dist/manifests/`, and the repository root.

## Included desks

"""
readme += "\n".join(f"- `{d['slug']}.md` - {d['title']}" for d in DESKS)
readme += "\n\n## Shared references\n\n- `references/suite-workflow-contract.md`\n- `references/workflow-packet-schema.md`\n- `references/source-inventory.md`\n- `references/stage-contracts/<desk>.md`\n- `references/desk-workflows/<desk>.md`\n"
(CORRECT_SUITE_DIR / "README.md").write_text(readme, encoding="utf-8")

for d in DESKS:
    (CORRECT_SUITE_DIR / f"{d['slug']}.md").write_text(module.source_md(d), encoding="utf-8")
    (CORRECT_SUITE_DIR / "references" / "stage-contracts" / f"{d['slug']}.md").write_text(module.stage_contract(d), encoding="utf-8")
    workflow = f"""# {d['title']} Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `{d['slug']}.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
{module.bullets(d['evidence'])}

## Outputs
{module.bullets(d['outputs'])}

## Halt conditions
{module.bullets(d['halt'])}

## Downstream handoffs
{module.bullets(d['downstream'])}
"""
    (CORRECT_SUITE_DIR / "references" / "desk-workflows" / f"{d['slug']}.md").write_text(workflow, encoding="utf-8")

(CORRECT_SUITE_DIR / "references" / "suite-workflow-contract.md").write_text(module.SHARED_CONTRACT, encoding="utf-8")
(CORRECT_SUITE_DIR / "references" / "workflow-packet-schema.md").write_text(module.PACKET_SCHEMA, encoding="utf-8")
(CORRECT_SUITE_DIR / "references" / "source-inventory.md").write_text(module.SOURCE_INVENTORY, encoding="utf-8")

# Update generator so future runs keep the expected source layout.
text = GENERATOR_PATH.read_text(encoding="utf-8")
text = text.replace('SUITE_DIR = ROOT / "skills" / "Sales Revenue Command Desk"', 'SUITE_DIR = ROOT / "skills" / "Sales Command Desk"')
# Add source-reference authoring if this generator has not already been upgraded.
needle = '    readme = "# Sales Revenue Command Desk\\n\\nStatus: v0.1.0 packaged suite generated.\\n\\nThis folder contains source Markdown specs for the Sales Command Desk suite. Packaged ChatGPT skill folders are generated under `dist/skills/sales-command-desk/`; zip bundles and manifests are generated under `dist/packages/sales-command-desk/`, `dist/manifests/`, and `releases/`.\\n\\n## Included desks\\n\\n" + "\\n".join(f"- `{d[\'slug\']}.md` - {d[\'title\']}" for d in DESKS) + "\\n"\n    write(SUITE_DIR / "README.md", readme)'
replacement = '    (SUITE_DIR / "references" / "stage-contracts").mkdir(parents=True, exist_ok=True)\n    (SUITE_DIR / "references" / "desk-workflows").mkdir(parents=True, exist_ok=True)\n    readme = "# Sales Command Desk\\n\\nStatus: v0.1.0 packaged suite generated.\\n\\nThis folder contains source Markdown specs and reference artifacts for the Sales Command Desk suite. Packaged ChatGPT skill folders are generated under `dist/skills/sales-command-desk/`; zip bundles and manifests are generated under `dist/packages/sales-command-desk/`, `dist/manifests/`, and `releases/`.\\n\\n## Included desks\\n\\n" + "\\n".join(f"- `{d[\'slug\']}.md` - {d[\'title\']}" for d in DESKS) + "\\n\\n## Shared references\\n\\n- `references/suite-workflow-contract.md`\\n- `references/workflow-packet-schema.md`\\n- `references/source-inventory.md`\\n- `references/stage-contracts/<desk>.md`\\n- `references/desk-workflows/<desk>.md`\\n"\n    write(SUITE_DIR / "README.md", readme)\n    write(SUITE_DIR / "references" / "suite-workflow-contract.md", SHARED_CONTRACT)\n    write(SUITE_DIR / "references" / "workflow-packet-schema.md", PACKET_SCHEMA)\n    write(SUITE_DIR / "references" / "source-inventory.md", SOURCE_INVENTORY)'
if needle in text:
    text = text.replace(needle, replacement)
loop_needle = '        write(SUITE_DIR / f"{d[\"slug\"]}.md", source_md(d))\n        skill_dir = DIST_ROOT / d["slug"]'
loop_replacement = '        write(SUITE_DIR / f"{d[\"slug\"]}.md", source_md(d))\n        write(SUITE_DIR / "references" / "stage-contracts" / f"{d[\"slug\"]}.md", stage_contract(d))\n        write(SUITE_DIR / "references" / "desk-workflows" / f"{d[\"slug\"]}.md", f"# {d[\"title\"]} Desk Workflow Reference\\n\\n## Workflow mode\\nUse this reference when authoring or reviewing `{d[\"slug\"]}.md` or its packaged `SKILL.md`.\\n\\n## Stage execution\\n1. Resolve the requested outcome and workflow mode.\\n2. Resolve account, contact, opportunity, source facts, and approval state.\\n3. Produce the stage output using only grounded facts plus labeled assumptions.\\n4. Preserve the sales workflow packet.\\n5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.\\n\\n## Required evidence\\n{bullets(d[\"evidence\"])}\\n\\n## Outputs\\n{bullets(d[\"outputs\"])}\\n\\n## Halt conditions\\n{bullets(d[\"halt\"])}\\n\\n## Downstream handoffs\\n{bullets(d[\"downstream\"])}\\n")\n        skill_dir = DIST_ROOT / d["slug"]'
if loop_needle in text and 'references" / "stage-contracts" / f"{d["slug"]}.md"' not in text:
    text = text.replace(loop_needle, loop_replacement)
GENERATOR_PATH.write_text(text, encoding="utf-8")

# Clean only the wrongly generated desk markdown files from the old stub folder and restore its original scaffold README.
if WRONG_SUITE_DIR.exists():
    for d in DESKS:
        p = WRONG_SUITE_DIR / f"{d['slug']}.md"
        if p.exists():
            p.unlink()
    old_readme = """# Sales Revenue Command Desk

Status: planned suite scaffold.

This folder is reserved for `.md` source specs belonging to the Sales Revenue Command Desk suite.

Authoring convention:

- Suite folders are human-readable product taxonomy.
- Desk files are kebab-case and end in `.md`.
- Packaged ChatGPT skill folders are generated artifacts, not the primary authoring structure.

"""
    (WRONG_SUITE_DIR / "README.md").write_text(old_readme, encoding="utf-8")

manifest_path = ROOT / "dist" / "manifests" / f"sales-command-desk-v{VERSION}.json"
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["source_dir"] = "skills/Sales Command Desk"
    manifest["source_references"] = [
        "skills/Sales Command Desk/references/suite-workflow-contract.md",
        "skills/Sales Command Desk/references/workflow-packet-schema.md",
        "skills/Sales Command Desk/references/source-inventory.md",
        "skills/Sales Command Desk/references/stage-contracts/<desk>.md",
        "skills/Sales Command Desk/references/desk-workflows/<desk>.md",
    ]
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "correct_source_dir": str(CORRECT_SUITE_DIR),
    "desk_md_count": len(list(CORRECT_SUITE_DIR.glob("*-desk.md"))),
    "stage_contract_count": len(list((CORRECT_SUITE_DIR / "references" / "stage-contracts").glob("*.md"))),
    "desk_workflow_count": len(list((CORRECT_SUITE_DIR / "references" / "desk-workflows").glob("*.md"))),
    "shared_reference_count": len(list((CORRECT_SUITE_DIR / "references").glob("*.md"))),
}, indent=2))
