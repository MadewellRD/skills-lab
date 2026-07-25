#!/usr/bin/env python3
"""Wrap an SDLC command artifact in a consistent Markdown file."""
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="write an SDLC command desk markdown artifact")
    parser.add_argument("--title", required=True)
    parser.add_argument("--mode", required=True, choices=["route-decision", "lifecycle-plan", "handoff", "connector-diagnostic"])
    parser.add_argument("--prompt-file", required=True, help="file containing body content")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    body = Path(args.prompt_file).read_text(encoding="utf-8").strip()
    content = f"""# {args.title}

## How to use this file

Use this {args.mode} artifact as the controlling SDLC route note. Preserve selected desks, connector requirements, source facts, missing facts, and halt conditions when handing work to downstream skills or coding agents.

## Artifact mode

{args.mode}

## Content

{body}
"""
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
