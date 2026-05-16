#!/usr/bin/env python3
"""Wrap a test-strategy artifact in a standard Markdown file."""

from __future__ import annotations

import argparse
from pathlib import Path


def read_text_or_literal(value: str) -> str:
    path = Path(value)
    if path.exists() and path.is_file():
        return path.read_text(encoding="utf-8")
    return value


def build_markdown(title: str, artifact: str, source_facts: list[str], assumptions: list[str]) -> str:
    source_lines = "\n".join(f"- {fact}" for fact in source_facts) if source_facts else "- none provided"
    assumption_lines = "\n".join(f"- {item}" for item in assumptions) if assumptions else "- none"
    return f"""# {title}

## How to use this file

Paste or attach this file to the target SDLC skill or implementation agent. Preserve source facts, assumptions, halt conditions, and downstream handoff instructions.

## Source facts

{source_lines}

## Unverified assumptions

{assumption_lines}

## Artifact

{artifact.rstrip()}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a wrapped test strategy Markdown artifact.")
    parser.add_argument("--title", required=True, help="artifact title")
    parser.add_argument("--artifact", required=True, help="artifact text or path to a markdown file")
    parser.add_argument("--output", required=True, help="output markdown path")
    parser.add_argument("--source-fact", action="append", default=[], help="verified source fact; repeatable")
    parser.add_argument("--assumption", action="append", default=[], help="unverified assumption; repeatable")
    args = parser.parse_args()

    artifact = read_text_or_literal(args.artifact)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_markdown(args.title, artifact, args.source_fact, args.assumption), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
