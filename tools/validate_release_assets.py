#!/usr/bin/env python3
"""Validate release checksum files against package roots."""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[1]
CHECKSUM_RE = re.compile(r"^([0-9a-fA-F]{64})\s+(.+)$")


@dataclass(frozen=True)
class ArtifactSet:
    name: str
    checksum_file: Path
    package_root: Path
    minimum_entries: int


ARTIFACT_SETS = [
    ArtifactSet(
        "SDLC Command Desk",
        REPO / "dist" / "manifests" / "sdlc-command-desk-CHECKSUMS.txt",
        REPO / "dist" / "packages" / "sdlc-command-desk",
        19,
    ),
    ArtifactSet(
        "Web Development Command Desk",
        REPO / "dist" / "manifests" / "web-development-command-desk-CHECKSUMS.txt",
        REPO / "dist" / "packages" / "web-development-command-desk",
        14,
    ),
    ArtifactSet(
        "AI Engineering Command Desk",
        REPO / "dist" / "manifests" / "ai-engineering-command-desk-CHECKSUMS.txt",
        REPO / "dist" / "packages" / "ai-engineering-command-desk",
        18,
    ),
    ArtifactSet(
        "Sales Command Desk",
        REPO / "CHECKSUMS-sales-command-desk-v0.1.0.txt",
        REPO / "dist" / "packages" / "sales-command-desk",
        13,
    ),
    ArtifactSet(
        "Product Command Desk",
        REPO / "CHECKSUMS-product-command-desk-v0.1.0.txt",
        REPO / "dist" / "packages" / "product-command-desk",
        16,
    ),
    ArtifactSet(
        "Android Command Desk",
        REPO / "CHECKSUMS-android-command-desk-v0.1.0.txt",
        REPO / "dist" / "packages" / "android-command-desk",
        14,
    ),
    ArtifactSet(
        "iOS Command Desk",
        REPO / "CHECKSUMS-ios-command-desk-v0.1.0.txt",
        REPO / "dist" / "packages" / "ios-command-desk",
        14,
    ),
]


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def candidate_paths(package_root: Path, recorded_path: str) -> list[Path]:
    raw = recorded_path.strip().replace("\\", "/")
    path = Path(raw)
    candidates = []
    if path.is_absolute():
        candidates.append(path)
    else:
        candidates.append(REPO / path)
        candidates.append(package_root / path)
        candidates.append(package_root / path.name)
    seen: set[Path] = set()
    unique: list[Path] = []
    for candidate in candidates:
        normalized = candidate.resolve() if candidate.exists() else candidate
        if normalized not in seen:
            unique.append(candidate)
            seen.add(normalized)
    return unique


def validate_artifact_set(artifact_set: ArtifactSet) -> list[str]:
    errors: list[str] = []
    entries = 0
    print(f"Checking {artifact_set.name}")

    if not artifact_set.checksum_file.exists():
        return [f"missing checksum file: {artifact_set.checksum_file.relative_to(REPO)}"]
    if not artifact_set.package_root.exists():
        return [f"missing package root: {artifact_set.package_root.relative_to(REPO)}"]

    for line_no, line in enumerate(artifact_set.checksum_file.read_text(encoding="utf-8").splitlines(), start=1):
        match = CHECKSUM_RE.match(line.strip())
        if not match:
            continue
        entries += 1
        expected, recorded_path = match.groups()
        expected = expected.lower()
        resolved = next((p for p in candidate_paths(artifact_set.package_root, recorded_path) if p.exists()), None)
        if resolved is None:
            errors.append(f"{artifact_set.checksum_file.relative_to(REPO)}:{line_no}: missing artifact {recorded_path}")
            continue
        actual = file_sha256(resolved)
        if actual != expected:
            errors.append(
                f"{artifact_set.checksum_file.relative_to(REPO)}:{line_no}: hash mismatch for {recorded_path}; expected {expected}; actual {actual}"
            )

    if entries < artifact_set.minimum_entries:
        errors.append(
            f"{artifact_set.checksum_file.relative_to(REPO)}: expected at least {artifact_set.minimum_entries} checksum entries; found {entries}"
        )

    if errors:
        print(f"FAIL: {artifact_set.name} ({len(errors)} issue(s))")
    else:
        print(f"OK: {artifact_set.name} ({entries} entries)")
    return errors


def main() -> int:
    errors: list[str] = []
    for artifact_set in ARTIFACT_SETS:
        errors.extend(validate_artifact_set(artifact_set))

    if errors:
        print("\nRelease artifact validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nRelease artifact validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
