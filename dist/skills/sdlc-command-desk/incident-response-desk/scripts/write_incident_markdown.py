#!/usr/bin/env python3
"""Wrap incident-response content in the standard Markdown artifact format."""

from __future__ import annotations

import argparse
from pathlib import Path


def build(title: str, body: str, usage: str | None = None) -> str:
    usage_text = usage or (
        "Use this artifact as the source of truth for triage, response coordination, RCA, "
        "or downstream SDLC handoff. Preserve severity, evidence, unknowns, halt conditions, "
        "and verification gates."
    )
    return f"# {title}\n\n## How to use this file\n\n{usage_text}\n\n## Artifact\n\n{body.rstrip()}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Write an incident-response Markdown artifact")
    parser.add_argument("--title", required=True)
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--usage", default=None)
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.exists():
        raise SystemExit(f"body file not found: {body_path}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build(args.title, body_path.read_text(encoding="utf-8"), args.usage), encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
