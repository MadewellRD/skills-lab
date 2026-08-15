#!/usr/bin/env python3
"""Fail when a goliveprompt preset declares a REPO that is not an absolute path.

    python tools/validate_presets.py

An unpinned REPO is not a stylistic problem. `list_roots` returns overlapping roots, and
more than one of them can contain a directory with the project's name, so an instruction
to resolve the root by search is re-decided every session and can land on a dormant clone.
That defect shipped and was found in the field. This check exists so it cannot come back
quietly.

A project may be left unpinned deliberately, but only out loud: it needs an entry in the
UNPINNED_ALLOWANCES block inside presets.md naming the project and the reason. An
allowance with no reason is not an allowance, because the whole point is that the next
session can see why the value is missing rather than assuming nobody got to it.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PRESETS = REPO_ROOT / "skills" / "SDLC Command Desk" / "_skills" / "goliveprompt" / "references" / "presets.md"

# A pinned value is a Windows drive path, a UNC path, or a POSIX absolute path. Anything
# else, including "resolve root via ...", is unpinned.
ABSOLUTE = re.compile(r"^(?:[A-Za-z]:[\\/]|\\\\|/)")

PROJECT_LINE = re.compile(r"^PROJECT\s*=\s*(\S.*?)\s*$")
REPO_LINE = re.compile(r"^REPO\s*=\s*(\S.*?)\s*$")

# Format inside presets.md:
#   <!-- UNPINNED_ALLOWANCE: PROJECT_NAME -- reason text -->
#
# The separator must be a SPACED " -- ". An earlier version matched the project as
# [^-]*, which silently failed on any project name containing a hyphen: the hyphen ate
# the delimiter, so the allowance was recorded, looked correct, and did nothing.
# Requiring surrounding whitespace lets a project name contain hyphens.
ALLOWANCE = re.compile(
    r"<!--\s*UNPINNED_ALLOWANCE:\s*(?P<project>\S+)\s+--\s+(?P<reason>.+?)\s*-->",
    re.DOTALL,
)


def parse_blocks(text: str) -> list[tuple[str, str, int]]:
    """Return (project, repo_value, line_no) for each preset block, in file order."""
    blocks: list[tuple[str, str, int]] = []
    current: str | None = None
    for line_no, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        m = PROJECT_LINE.match(line)
        if m:
            current = m.group(1).strip()
            continue
        m = REPO_LINE.match(line)
        if m and current:
            blocks.append((current, m.group(1).strip(), line_no))
            current = None
    return blocks


def strip_fences(text: str) -> str:
    """Blank out fenced code blocks, preserving line count.

    presets.md documents its own allowance syntax inside a fence. That example is a
    template, not a declaration, and grading it made the file fail its own check by
    reporting an allowance for the placeholder project name.
    """
    out, fenced = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append("")
            continue
        out.append("" if fenced else line)
    return "\n".join(out)


def parse_allowances(text: str) -> dict[str, str]:
    """Project name -> reason, for deliberately unpinned projects.

    Read from prose only. An allowance shown inside a fence is documentation.
    """
    out: dict[str, str] = {}
    for m in ALLOWANCE.finditer(strip_fences(text)):
        reason = " ".join(m.group("reason").split())
        if reason:
            out[m.group("project").strip().upper()] = reason
    return out


def main() -> int:
    if not PRESETS.exists():
        print(f"FAIL: presets file not found: {PRESETS}")
        return 1

    text = PRESETS.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    allowances = parse_allowances(text)

    if not blocks:
        print("FAIL: no preset blocks parsed; the format changed and this check went blind")
        return 1

    errors: list[str] = []
    rel = PRESETS.relative_to(REPO_ROOT).as_posix()
    print(f"Checking {rel}")

    for project, value, line_no in blocks:
        # An angle-bracket value is a documentation placeholder in the shape template, not
        # a declared preset. Grading it would make the file's own instructions fail.
        if value.startswith("<") and value.endswith(">"):
            continue
        # Strip a trailing parenthetical note such as "(remote example.invalid/...)".
        path_part = value.split("  (")[0].strip()
        if ABSOLUTE.match(path_part):
            print(f"OK: {project} pinned to {path_part}")
            continue
        reason = allowances.get(project.upper())
        if reason:
            print(f"OK: {project} unpinned by allowance: {reason}")
            continue
        errors.append(
            f"{rel}:{line_no}: {project} has a non-absolute REPO value {value!r}. "
            f"Pin it to an absolute path, or record "
            f"<!-- UNPINNED_ALLOWANCE: {project} -- why it cannot be pinned --> in this file."
        )

    orphans = {p.upper() for p, _, _ in blocks}
    for project in allowances:
        if project not in orphans:
            errors.append(
                f"{rel}: allowance recorded for {project}, which has no preset block. "
                f"Remove the allowance or add the block."
            )

    if errors:
        print("\nPreset validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    print(f"\nPreset validation passed ({len(blocks)} blocks, {len(allowances)} allowed unpinned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
