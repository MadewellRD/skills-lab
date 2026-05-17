#!/usr/bin/env python3
"""Write an issue-planning Markdown artifact with a standard wrapper."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_markdown(title: str, body: str, usage: str) -> str:
    title = title.strip() or "Issue Plan"
    body = body.strip()
    usage = usage.strip() or (
        "Use this file as the source of truth for issue creation, sprint planning, "
        "or downstream implementation-handoff-desk handoff."
    )
    return f"# {title}\n\n## How to use this file\n\n{usage}\n\n## Content\n\n{body}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Artifact title")
    parser.add_argument("--body-file", required=True, help="Path to body Markdown")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    parser.add_argument("--usage", default="", help="Optional usage instructions")
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.exists():
        raise SystemExit(f"body file not found: {body_path}")

    body = body_path.read_text(encoding="utf-8")
    markdown = build_markdown(args.title, body, args.usage)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
