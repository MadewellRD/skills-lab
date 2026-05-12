#!/usr/bin/env python3
"""Wrap review content in the Review Quality Desk Markdown artifact format."""

from __future__ import annotations

import argparse
from pathlib import Path


def build(title: str, body: str) -> str:
    return f"""# {title}

## How to use this file

Use this review artifact to decide whether to approve, comment, request changes, or route follow-up work through `implementation-handoff-desk`. Preserve source facts and unresolved evidence gaps.

## Review Artifact

{body.rstrip()}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a Review Quality Desk Markdown artifact.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    body_path = Path(args.body_file)
    out_path = Path(args.out)

    if not body_path.exists():
        raise SystemExit(f"body file not found: {body_path}")

    body = body_path.read_text(encoding="utf-8")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build(args.title, body), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
