#!/usr/bin/env python3
"""Generate Android Command Desk release artifacts.

Packages skills/Android Command Desk/ into:
  dist/skills/android-command-desk/<desk>/
  dist/packages/android-command-desk/<ordered-desk>-skill.zip
  dist/packages/android-command-desk/android-command-desk-v0.1.0-skill-bundles.zip
  dist/packages/android-command-desk/android-command-desk-v0.1.0-source.zip
  dist/manifests/android-command-desk-v0.1.0.json
  dist/manifests/android-command-desk-CHECKSUMS.txt
  CHECKSUMS-android-command-desk-v0.1.0.txt
  releases/android-command-desk-v0.1.0.md
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
SUITE_SLUG = "android-command-desk"
SUITE_TITLE = "Android Command Desk"
SUITE_DIR = ROOT / "skills" / "Android Command Desk"
DIST_ROOT = ROOT / "dist" / "skills" / SUITE_SLUG
PACKAGE_DIR = ROOT / "dist" / "packages" / SUITE_SLUG
MANIFEST_DIR = ROOT / "dist" / "manifests"
RELEASES_DIR = ROOT / "releases"
TODAY = date.today().isoformat()

DESKS = [
    ("000", "android-command-desk", "000-android-command-desk.md", "Android Command Desk", "Orchestrates complete Android app and game development workflows."),
    ("001", "android-product-requirements-desk", "001-android-product-requirements-desk.md", "Android Product Requirements Desk", "Defines Android app/game requirements and acceptance gates."),
    ("002", "android-technical-discovery-desk", "002-android-technical-discovery-desk.md", "Android Technical Discovery Desk", "Inspects repo, Gradle, SDK, engine, CI, and feasibility facts."),
    ("003", "android-architecture-design-desk", "003-android-architecture-design-desk.md", "Android Architecture Design Desk", "Designs architecture, modules, data flow, engine boundaries, and ADR decisions."),
    ("004", "android-ui-ux-desk", "004-android-ui-ux-desk.md", "Android UI UX Desk", "Plans Android UI/UX, navigation, accessibility, localization, and input states."),
    ("005", "android-app-engineering-desk", "005-android-app-engineering-desk.md", "Android App Engineering Desk", "Prepares native Android app implementation handoffs."),
    ("006", "android-game-engineering-desk", "006-android-game-engineering-desk.md", "Android Game Engineering Desk", "Prepares Android game, engine, AGDK/NDK, and runtime handoffs."),
    ("007", "android-backend-integration-desk", "007-android-backend-integration-desk.md", "Android Backend Integration Desk", "Defines APIs, auth, sync, push, payments, multiplayer, and cloud saves."),
    ("008", "android-security-privacy-desk", "008-android-security-privacy-desk.md", "Android Security Privacy Desk", "Reviews security, privacy, permissions, data safety, policy, and abuse risks."),
    ("009", "android-performance-optimization-desk", "009-android-performance-optimization-desk.md", "Android Performance Optimization Desk", "Plans app/game performance, benchmarks, profiling, and device-tier budgets."),
    ("010", "android-testing-qa-desk", "010-android-testing-qa-desk.md", "Android Testing QA Desk", "Defines Android app/game QA, test matrix, device coverage, and release gates."),
    ("011", "android-release-store-ops-desk", "011-android-release-store-ops-desk.md", "Android Release Store Ops Desk", "Plans builds, signing, Play tracks, staged rollout, rollback, and store readiness."),
    ("012", "android-observability-liveops-desk", "012-android-observability-liveops-desk.md", "Android Observability Liveops Desk", "Defines crash/ANR monitoring, analytics, remote config, alerts, and live ops."),
    ("013", "android-maintenance-growth-desk", "013-android-maintenance-growth-desk.md", "Android Maintenance Growth Desk", "Plans SDK updates, policy changes, experiments, monetization, and technical debt."),
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8")


def copy_tree(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    for item in sorted(src.rglob("*")):
        if item.is_file():
            rel = item.relative_to(src)
            target = dst / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)


def zip_dir(src: Path, dest: Path) -> None:
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


def openai_yaml(title: str, short: str) -> str:
    return f"""interface:
  display_name: {title}
  short_description: {short}
  icon: 🤖
  primary_color: '#22c55e'
policy:
  products:
    - chatgpt
"""


def main() -> None:
    if not SUITE_DIR.exists():
        raise SystemExit(f"Missing suite source directory: {SUITE_DIR}")

    if DIST_ROOT.exists():
        shutil.rmtree(DIST_ROOT)
    DIST_ROOT.mkdir(parents=True, exist_ok=True)
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    RELEASES_DIR.mkdir(parents=True, exist_ok=True)

    skill_zip_paths: list[Path] = []

    for order, slug, source_file, title, short in DESKS:
        src_md = SUITE_DIR / source_file
        if not src_md.exists():
            raise SystemExit(f"Missing source file: {src_md.relative_to(ROOT)}")

        skill_dir = DIST_ROOT / slug
        (skill_dir / "agents").mkdir(parents=True, exist_ok=True)
        (skill_dir / "assets").mkdir(exist_ok=True)
        (skill_dir / "references").mkdir(exist_ok=True)

        shutil.copy2(src_md, skill_dir / "SKILL.md")
        write(skill_dir / "agents" / "openai.yaml", openai_yaml(title, short))
        write(skill_dir / "assets" / ".gitkeep", "")
        copy_tree(SUITE_DIR / "references", skill_dir / "references")

        zip_path = PACKAGE_DIR / f"{order}-{slug}-skill.zip"
        zip_dir(skill_dir, zip_path)
        skill_zip_paths.append(zip_path)
        print(f"packaged: {order}-{slug}")

    bundles_zip = PACKAGE_DIR / f"{SUITE_SLUG}-v{VERSION}-skill-bundles.zip"
    with zipfile.ZipFile(bundles_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in skill_zip_paths:
            zf.write(p, p.name)

    source_zip = PACKAGE_DIR / f"{SUITE_SLUG}-v{VERSION}-source.zip"
    zip_dir(SUITE_DIR, source_zip)

    manifest = {
        "suite": SUITE_SLUG,
        "title": SUITE_TITLE,
        "version": VERSION,
        "generated_on": TODAY,
        "source_dir": "skills/Android Command Desk",
        "dist_dir": f"dist/skills/{SUITE_SLUG}",
        "package_dir": f"dist/packages/{SUITE_SLUG}",
        "skills": [
            {"order": order, "slug": slug, "source": source_file, "title": title}
            for order, slug, source_file, title, _ in DESKS
        ],
        "packages": [str(p.relative_to(ROOT)).replace("\\", "/") for p in skill_zip_paths + [bundles_zip, source_zip]],
    }
    manifest_path = MANIFEST_DIR / f"{SUITE_SLUG}-v{VERSION}.json"
    write(manifest_path, json.dumps(manifest, indent=2) + "\n")

    checksum_files = sorted(set(list(SUITE_DIR.rglob("*.md")) + list(DIST_ROOT.rglob("*")) + list(PACKAGE_DIR.glob("*.zip")) + [manifest_path]))
    lines = [f"{sha256(p)}  {p.relative_to(ROOT).as_posix()}" for p in checksum_files if p.is_file()]
    checksum_text = "\n".join(lines) + "\n"
    write(ROOT / f"CHECKSUMS-{SUITE_SLUG}-v{VERSION}.txt", checksum_text)
    write(MANIFEST_DIR / f"{SUITE_SLUG}-CHECKSUMS.txt", checksum_text)
    write(PACKAGE_DIR / f"{SUITE_SLUG}-v{VERSION}-CHECKSUMS.txt", checksum_text)

    release = f"""# Android Command Desk v{VERSION}

Date: {TODAY}

## Summary

Packages the Android Command Desk source suite into ChatGPT-compatible skill directories and ZIP archives. The suite covers Android app development and Android game development from requirements, technical discovery, architecture, UI/UX, app/game engineering, backend integration, security/privacy, performance, testing, release/store operations, observability/live ops, and maintenance/growth.

## Artifacts

- Source specs: `skills/Android Command Desk/`
- Packaged skill directories: `dist/skills/{SUITE_SLUG}/`
- Skill zip bundles: `dist/packages/{SUITE_SLUG}/`
- Manifest: `dist/manifests/{SUITE_SLUG}-v{VERSION}.json`
- Checksums: `CHECKSUMS-{SUITE_SLUG}-v{VERSION}.txt`

## Desks

{chr(10).join(f"- `{order}-{slug}` — {title}" for order, slug, _, title, _ in DESKS)}

## Validation

- Every packaged skill includes `SKILL.md` sourced from `skills/Android Command Desk/`.
- Every packaged skill includes `agents/openai.yaml`.
- Shared Android references are copied into each packaged skill for progressive disclosure.
- Checksums generated after packaging.
"""
    write(RELEASES_DIR / f"{SUITE_SLUG}-v{VERSION}.md", release)

    summary = {"version": VERSION, "skill_count": len(DESKS), "zip_count": len(list(PACKAGE_DIR.glob("*.zip")))}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
