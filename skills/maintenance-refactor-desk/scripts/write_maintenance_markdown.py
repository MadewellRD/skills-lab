#!/usr/bin/env python3
"""Wrap a maintenance artifact in a standard markdown file."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write a maintenance/refactor markdown artifact.")
    parser.add_argument("--title", required=True, help="Artifact title")
    parser.add_argument("--body-file", required=True, help="Path to markdown body content")
    parser.add_argument("--output", required=True, help="Output markdown path")
    parser.add_argument("--source-fact", action="append", default=[], help="Source fact to include")
    parser.add_argument("--assumption", action="append", default=[], help="Unverified assumption to include")
    return parser.parse_args()


def bullet_list(items: list[str], empty: str) -> str:
    if not items:
        return f"- {empty}\n"
    return "".join(f"- {item}\n" for item in items)


def main() -> None:
    args = parse_args()
    body_path = Path(args.body_file)
    output_path = Path(args.output)

    if not body_path.exists():
        raise SystemExit(f"body file not found: {body_path}")

    body = body_path.read_text(encoding="utf-8").strip()
    if not body:
        raise SystemExit("body file is empty")

    content = f"""# {args.title}

## How to use this file

Use this artifact to bound maintenance, refactor, dependency-upgrade, migration, or cleanup work before implementation. If implementation is needed, pass the handoff notes to `implementation-handoff-desk` and preserve the halt conditions.

## Source facts used

{bullet_list(args.source_fact, 'No source facts provided.')}
## Unverified assumptions

{bullet_list(args.assumption, 'No unverified assumptions recorded.')}
## Artifact

{body}
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(output_path)


if __name__ == "__main__":
    main()
