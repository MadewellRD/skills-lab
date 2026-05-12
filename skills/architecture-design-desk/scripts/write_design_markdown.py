#!/usr/bin/env python3
"""Wrap architecture/design content in the Architecture Design Desk artifact format."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_markdown(title: str, artifact: str, source_facts: list[str], assumptions: list[str]) -> str:
    facts = source_facts or ["None provided"]
    assumed = assumptions or ["None"]
    fact_lines = "\n".join(f"- {fact}" for fact in facts)
    assumption_lines = "\n".join(f"- {item}" for item in assumed)
    return f"""# {title}

## How to use this file

Use this architecture artifact as source material for planning, security review, verification, and implementation handoff. Resolve blocking assumptions and open questions before implementation.

## Artifact

{artifact.rstrip()}

## Source facts used

{fact_lines}

## Unverified assumptions

{assumption_lines}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a wrapped architecture/design Markdown artifact.")
    parser.add_argument("--title", required=True, help="Artifact title")
    parser.add_argument("--artifact-file", required=True, help="Path to file containing artifact body")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    parser.add_argument("--source-fact", action="append", default=[], help="Source fact used; repeatable")
    parser.add_argument("--assumption", action="append", default=[], help="Unverified assumption; repeatable")
    args = parser.parse_args()

    artifact_path = Path(args.artifact_file)
    if not artifact_path.exists():
        raise SystemExit(f"artifact file not found: {artifact_path}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        build_markdown(args.title, artifact_path.read_text(encoding="utf-8"), args.source_fact, args.assumption),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
