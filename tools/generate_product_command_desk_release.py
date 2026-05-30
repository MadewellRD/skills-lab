"""
generate_product_command_desk_release.py

Packages skills/Product Command Desk/ into:
  dist/skills/product-command-desk/<desk>/
  dist/packages/product-command-desk/<desk>-v0.1.0.zip
  dist/manifests/product-command-desk-v0.1.0.json
  CHECKSUMS-product-command-desk-v0.1.0.txt
  releases/product-command-desk-v0.1.0.md
"""

from __future__ import annotations
import hashlib
import json
import shutil
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0"
SUITE_DIR = ROOT / "skills" / "Product Command Desk"
DIST_ROOT = ROOT / "dist" / "skills" / "product-command-desk"
PACKAGE_DIR = ROOT / "dist" / "packages" / "product-command-desk"
MANIFEST_DIR = ROOT / "dist" / "manifests"
RELEASES_DIR = ROOT / "releases"
TODAY = date.today().isoformat()

DESKS = [
    ("product-command-desk", "Product Command Desk", "Orchestrate product workflows from idea through discovery, requirements, prioritization, roadmap, launch, experimentation, feedback, retention, and retrospective."),
    ("market-discovery-desk", "Market Discovery Desk", "Analyze market context, category dynamics, customer segments, and opportunity framing from primary and secondary evidence."),
    ("user-research-desk", "User Research Desk", "Plan, conduct, and synthesize user interviews, research plans, and findings into evidence-backed product insights."),
    ("persona-segmentation-desk", "Persona & Segmentation Desk", "Define personas, segments, ICP, use-cases, and customer journeys from behavioral and contextual evidence."),
    ("opportunity-sizing-desk", "Opportunity Sizing Desk", "Estimate TAM, SAM, SOM, revenue potential, adoption constraints, and confidence levels for product opportunities."),
    ("competitive-analysis-desk", "Competitive Analysis Desk", "Analyze competitors, alternatives, substitutes, positioning, and differentiation opportunities."),
    ("prd-desk", "PRD Desk", "Write product requirements, acceptance criteria, non-goals, risks, and downstream handoffs."),
    ("roadmap-planning-desk", "Roadmap Planning Desk", "Plan roadmap themes, sequencing, dependencies, milestones, and tradeoffs."),
    ("feature-prioritization-desk", "Feature Prioritization Desk", "Rank, score, and document feature prioritization decisions with impact/effort tradeoffs and decision records."),
    ("pricing-packaging-desk", "Pricing & Packaging Desk", "Develop pricing hypotheses, packages, entitlements, monetization risk assessments, and pricing experiments."),
    ("gtm-brief-desk", "GTM Brief Desk", "Write go-to-market briefs covering audiences, messaging, channels, sales/support enablement, and launch handoff."),
    ("launch-readiness-desk", "Launch Readiness Desk", "Gate product launches against release scope, comms, support, docs, metrics, and rollback readiness."),
    ("experiment-design-desk", "Experiment Design Desk", "Design product experiments with hypotheses, metrics, cohorts, guardrails, and decision rules."),
    ("feedback-synthesis-desk", "Feedback Synthesis Desk", "Intake, cluster, and weight product feedback from multiple sources and map to product actions."),
    ("churn-retention-analysis-desk", "Churn & Retention Analysis Desk", "Analyze churn drivers, retention opportunities, cohorts, lifecycle gaps, and intervention plans."),
    ("product-retrospective-desk", "Product Retrospective Desk", "Run post-launch or cycle retrospectives, capture lessons, metric outcomes, and improvement actions."),
]


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8")


def zip_dir(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(src.rglob("*")):
            if p.is_file():
                zf.write(p, p.relative_to(src.parent).as_posix())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def openai_yaml(slug: str, title: str, short: str) -> str:
    return f"""interface:
  display_name: {title}
  short_description: {short}
  icon: 📦
  primary_color: '#7c3aed'
policy:
  products:
    - chatgpt
"""


def main():
    DIST_ROOT.mkdir(parents=True, exist_ok=True)
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    RELEASES_DIR.mkdir(parents=True, exist_ok=True)

    skill_zip_paths = []

    for slug, title, short in DESKS:
        src_md = SUITE_DIR / f"{slug}.md"
        if not src_md.exists():
            print(f"WARNING: source not found: {src_md}")
            continue

        skill_dir = DIST_ROOT / slug
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "agents").mkdir(exist_ok=True)
        (skill_dir / "assets").mkdir(exist_ok=True)

        # SKILL.md = source file content (already has proper frontmatter)
        shutil.copy2(src_md, skill_dir / "SKILL.md")

        # agents/openai.yaml
        write(skill_dir / "agents" / "openai.yaml", openai_yaml(slug, title, short))

        # assets placeholder
        (skill_dir / "assets" / ".gitkeep").write_text("", encoding="utf-8")

        # zip
        zip_path = PACKAGE_DIR / f"{slug}-v{VERSION}.zip"
        zip_dir(skill_dir, zip_path)
        skill_zip_paths.append(zip_path)
        print(f"  packaged: {slug}")

    # bundle zips
    bundles_zip = PACKAGE_DIR / f"product-command-desk-v{VERSION}-skill-bundles.zip"
    with zipfile.ZipFile(bundles_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in skill_zip_paths:
            zf.write(p, p.name)

    # source zip
    source_zip = PACKAGE_DIR / f"product-command-desk-v{VERSION}-source.zip"
    zip_dir(SUITE_DIR, source_zip)

    # manifest
    manifest = {
        "suite": "product-command-desk",
        "version": VERSION,
        "generated_on": TODAY,
        "source_dir": "skills/Product Command Desk",
        "dist_dir": "dist/skills/product-command-desk",
        "skills": [{"slug": slug, "title": title} for slug, title, _ in DESKS],
        "packages": [str(p.relative_to(ROOT)).replace("\\", "/") for p in skill_zip_paths + [bundles_zip, source_zip]],
    }
    write(MANIFEST_DIR / f"product-command-desk-v{VERSION}.json", json.dumps(manifest, indent=2) + "\n")

    # checksums
    checksum_files = sorted(set(
        list(SUITE_DIR.rglob("*.md")) +
        list(DIST_ROOT.rglob("*")) +
        list(PACKAGE_DIR.glob("*.zip")) +
        [MANIFEST_DIR / f"product-command-desk-v{VERSION}.json"]
    ))
    lines = [f"{sha256(p)}  {p.relative_to(ROOT).as_posix()}" for p in checksum_files if p.is_file()]
    write(ROOT / f"CHECKSUMS-product-command-desk-v{VERSION}.txt", "\n".join(lines) + "\n")
    write(PACKAGE_DIR / f"product-command-desk-v{VERSION}-CHECKSUMS.txt", "\n".join(lines) + "\n")

    # release notes
    release = f"""# Product Command Desk v{VERSION}

Date: {TODAY}

## Summary

Packages the Product Command Desk source suite into ChatGPT-compatible skill directories and ZIP archives. The suite covers the full product lifecycle: market discovery, user research, persona and segmentation, opportunity sizing, competitive analysis, product requirements, roadmap planning, feature prioritization, pricing and packaging, GTM, launch readiness, experiment design, feedback synthesis, churn and retention analysis, and product retrospectives.

## Artifacts

- Source specs: `skills/Product Command Desk/`
- Packaged skill directories: `dist/skills/product-command-desk/`
- Skill zip bundles: `dist/packages/product-command-desk/`
- Manifest: `dist/manifests/product-command-desk-v{VERSION}.json`
- Checksums: `CHECKSUMS-product-command-desk-v{VERSION}.txt`

## Desks

{chr(10).join(f"- `{slug}` — {title}" for slug, title, _ in DESKS)}

## Validation

- Every packaged skill includes `SKILL.md` sourced from `skills/Product Command Desk/`.
- Every packaged skill includes `agents/openai.yaml`.
- Checksums generated after packaging.
"""
    write(RELEASES_DIR / f"product-command-desk-v{VERSION}.md", release)

    summary = {"version": VERSION, "skill_count": len(DESKS), "zip_count": len(list(PACKAGE_DIR.glob("*.zip")))}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
