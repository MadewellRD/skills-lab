#!/usr/bin/env python3
"""Wrap decommissioning content in the standard downloadable Markdown artifact format."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_document(title: str, body: str, source_fact: list[str], assumption: list[str]) -> str:
    lines: list[str] = [
        f"# {title}",
        "",
        "## How to use this file",
        "",
        "Use this artifact as the decommissioning control document. Preserve the source facts, assumptions, halt conditions, verification gates, rollback criteria, and downstream handoff notes when converting it into PR, deployment, release, verification, or documentation work.",
        "",
    ]
    if source_fact:
        lines.extend(["## Source facts", ""])
        lines.extend(f"- {fact}" for fact in source_fact)
        lines.append("")
    if assumption:
        lines.extend(["## Unverified assumptions", ""])
        lines.extend(f"- {item}" for item in assumption)
        lines.append("")
    lines.extend(["## Plan", "", body.rstrip(), ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="artifact title")
    parser.add_argument("--body-file", required=True, help="markdown file containing plan body")
    parser.add_argument("--output", required=True, help="output markdown path")
    parser.add_argument("--source-fact", action="append", default=[], help="confirmed source fact; repeatable")
    parser.add_argument("--assumption", action="append", default=[], help="unverified assumption; repeatable")
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.exists():
        raise SystemExit(f"body file not found: {body_path}")

    document = build_document(
        title=args.title,
        body=body_path.read_text(encoding="utf-8"),
        source_fact=args.source_fact,
        assumption=args.assumption,
    )
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(document, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
