#!/usr/bin/env python3
"""Wrap deployment-desk content in a standard markdown artifact."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_markdown(title: str, artifact: str, source_fact: list[str], assumption: list[str]) -> str:
    source_lines = "\n".join(f"- {item}" for item in source_fact) if source_fact else "- none recorded"
    assumption_lines = "\n".join(f"- {item}" for item in assumption) if assumption else "- none"
    return f"""# {title}

## How to use this file

Use this file as the deployment, rollout, change-management, or go/no-go source of truth. Preserve source facts, assumptions, validation gates, rollback triggers, and halt conditions.

## Artifact

{artifact.strip()}

## Source facts

{source_lines}

## Unverified assumptions

{assumption_lines}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a deployment-desk markdown artifact.")
    parser.add_argument("--title", required=True, help="artifact title")
    parser.add_argument("--content-file", required=True, help="path to artifact body text")
    parser.add_argument("--output", required=True, help="output markdown path")
    parser.add_argument("--source-fact", action="append", default=[], help="verified source fact")
    parser.add_argument("--assumption", action="append", default=[], help="unverified assumption")
    args = parser.parse_args()

    content_path = Path(args.content_file)
    if not content_path.exists():
        raise SystemExit(f"content file does not exist: {content_path}")

    artifact = content_path.read_text(encoding="utf-8")
    markdown = build_markdown(args.title, artifact, args.source_fact, args.assumption)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
