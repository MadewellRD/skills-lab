#!/usr/bin/env python3
"""Write a wrapped observability artifact Markdown file."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_document(title: str, content: str, usage: str) -> str:
    return f"# {title}\n\n## How to use this file\n\n{usage.strip()}\n\n## Artifact\n\n{content.strip()}\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Write a wrapped observability Markdown artifact.")
    parser.add_argument("--title", required=True, help="Artifact title")
    parser.add_argument("--input", required=True, help="Path to raw Markdown content")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    parser.add_argument(
        "--usage",
        default="Use this artifact for observability readiness review, operational planning, or downstream implementation handoff.",
        help="How to use this file text",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"input file not found: {input_path}")

    content = input_path.read_text(encoding="utf-8")
    if not content.strip():
        raise ValueError("input file is empty")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_document(args.title, content, args.usage), encoding="utf-8")


if __name__ == "__main__":
    main()
