#!/usr/bin/env python3
"""Wrap a technical discovery artifact in the required Markdown file structure."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_document(title: str, body: str, usage: str) -> str:
    return f"# {title}\n\n## How to use this file\n\n{usage.strip()}\n\n## Artifact\n\n{body.strip()}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a wrapped technical discovery Markdown artifact.")
    parser.add_argument("--title", required=True, help="Artifact title without leading #")
    parser.add_argument("--body-file", required=True, help="Path to a Markdown file containing the artifact body")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    parser.add_argument(
        "--usage",
        default="Use this artifact as technical discovery input. Keep source facts, assumptions, risks, open questions, and downstream routing intact.",
        help="How-to-use text",
    )
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.is_file():
        raise SystemExit(f"body file not found: {body_path}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_document(args.title, body_path.read_text(encoding="utf-8"), args.usage), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
