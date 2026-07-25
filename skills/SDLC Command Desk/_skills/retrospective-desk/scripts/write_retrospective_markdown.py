#!/usr/bin/env python3
"""Wrap retrospective content in a standard Markdown artifact."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_document(title: str, content: str) -> str:
    return f"""# {title}

## How to use this file

Use this retrospective to review delivery outcomes, assign improvement actions, and continue follow-up work through the appropriate SDLC stage.

## Report

{content.strip()}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Write a retrospective Markdown artifact")
    parser.add_argument("--title", required=True, help="Artifact title")
    parser.add_argument("--content-file", required=True, help="Path to a UTF-8 Markdown content file")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    args = parser.parse_args()

    content_path = Path(args.content_file)
    output_path = Path(args.output)

    if not content_path.exists():
        raise SystemExit(f"content file not found: {content_path}")

    content = content_path.read_text(encoding="utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_document(args.title, content), encoding="utf-8")


if __name__ == "__main__":
    main()
