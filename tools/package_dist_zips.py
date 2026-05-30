"""
package_dist_zips.py

Creates dist/packages/<suite>/ ZIP archives from existing dist/skills/<suite>/ directories.
Handles: sdlc-command-desk, ai-engineering-command-desk

Usage: python tools/package_dist_zips.py
"""

from __future__ import annotations
import hashlib
import json
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today().isoformat()

SUITES = [
    {
        "slug": "sdlc-command-desk",
        "version": "0.2.0-rc.1",
        "name_prefix": lambda slug, i: f"{i:03d}-{slug}-skill",
    },
    {
        "slug": "ai-engineering-command-desk",
        "version": "0.1.0",
        "name_prefix": lambda slug, i: f"{i:03d}-{slug}-skill",
    },
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def zip_skill(skill_dir: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(skill_dir.rglob("*")):
            if p.is_file():
                zf.write(p, p.relative_to(skill_dir.parent).as_posix())


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8")


def package_suite(suite: dict):
    slug = suite["slug"]
    version = suite["version"]
    dist_skills = ROOT / "dist" / "skills" / slug
    pkg_dir = ROOT / "dist" / "packages" / slug
    pkg_dir.mkdir(parents=True, exist_ok=True)

    skill_dirs = sorted([d for d in dist_skills.iterdir() if d.is_dir()])
    print(f"\n{slug}: {len(skill_dirs)} skill dirs found")

    zip_paths = []
    for i, skill_dir in enumerate(skill_dirs):
        zip_name = f"{i:03d}-{skill_dir.name}-skill.zip"
        zip_path = pkg_dir / zip_name
        zip_skill(skill_dir, zip_path)
        zip_paths.append(zip_path)
        print(f"  {zip_name}")

    # CHECKSUMS for this suite
    lines = [f"{sha256(p)}  {p.relative_to(ROOT).as_posix()}" for p in sorted(zip_paths)]
    checksums_path = pkg_dir / f"{slug}-v{version}-CHECKSUMS.txt"
    write(checksums_path, "\n".join(lines) + "\n")
    print(f"  checksums: {checksums_path.name} ({len(lines)} entries)")

    # Also update dist/manifests checksums file for this suite
    manifest_checksums = ROOT / "dist" / "manifests" / f"{slug}-CHECKSUMS.txt"
    all_lines = [f"{sha256(p)}  {p.relative_to(ROOT).as_posix()}"
                 for p in sorted(list((ROOT / "dist" / "skills" / slug).rglob("*")) + zip_paths)
                 if p.is_file()]
    write(manifest_checksums, "\n".join(all_lines) + "\n")

    return zip_paths


def main():
    all_zips = []
    for suite in SUITES:
        zips = package_suite(suite)
        all_zips.extend(zips)

    print(f"\nTotal archives created: {len(all_zips)}")


if __name__ == "__main__":
    main()
