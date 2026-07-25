#!/usr/bin/env python3
"""Wrap a raw implementation-agent prompt in the required downloadable markdown format.

Usage:
  write_prompt_markdown.py --title "Prompt title" --input prompt.txt --output pr-prompt-title.md
  cat prompt.txt | write_prompt_markdown.py --title "Prompt title" --output pr-prompt-title.md

Optional source metadata:
  write_prompt_markdown.py --title "Prompt" --output prompt.md \
    --mode connector-grounded --source-fact "GitHub repo: owner/repo" \
    --unverified-assumption "CI status unavailable"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

USAGE_TEXT = (
    "Paste everything under `## Prompt` into Claude Code, Codex, or the target "
    "implementation agent. Keep the guardrails, halt conditions, commit instructions, "
    "PR title, PR body requirements, and final stop line intact."
)

VALID_MODES = {"connector-grounded", "mixed", "user-facts-only", "diagnostic"}


def read_prompt(input_path: str | None) -> str:
    if input_path:
        return Path(input_path).read_text(encoding="utf-8").strip()
    return sys.stdin.read().strip()


def source_facts_block(mode: str | None, source_facts: list[str], assumptions: list[str]) -> str:
    if not mode and not source_facts and not assumptions:
        return ""
    mode_value = mode or "user-facts-only"
    if mode_value not in VALID_MODES:
        raise ValueError(f"mode must be one of: {', '.join(sorted(VALID_MODES))}")
    lines = ["", "## Source facts used", "", f"- Mode: {mode_value}"]
    for fact in source_facts:
        fact = fact.strip()
        if fact:
            lines.append(f"- {fact}")
    if assumptions:
        lines.append(f"- Unverified assumptions: {'; '.join(item.strip() for item in assumptions if item.strip())}")
    elif source_facts or mode:
        lines.append("- Unverified assumptions: none")
    return "\n".join(lines) + "\n"


def build_markdown(title: str, prompt: str, mode: str | None = None, source_facts: list[str] | None = None, assumptions: list[str] | None = None) -> str:
    if not title.strip():
        raise ValueError("title must not be empty")
    if not prompt.strip():
        raise ValueError("prompt must not be empty")
    facts = source_facts_block(mode, source_facts or [], assumptions or [])
    return f"""# {title.strip()}

## How to use this file

{USAGE_TEXT}

## Prompt

{prompt.strip()}
{facts}"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Markdown title for the prompt file")
    parser.add_argument("--input", help="Path to a raw prompt text file. Reads stdin when omitted.")
    parser.add_argument("--output", required=True, help="Path to write the markdown file")
    parser.add_argument("--mode", choices=sorted(VALID_MODES), help="Grounding mode to include in Source facts used")
    parser.add_argument("--source-fact", action="append", default=[], help="Source fact to include. May be repeated.")
    parser.add_argument("--unverified-assumption", action="append", default=[], help="Unverified assumption to include. May be repeated.")
    args = parser.parse_args()

    try:
        prompt = read_prompt(args.input)
        output = build_markdown(args.title, prompt, args.mode, args.source_fact, args.unverified_assumption)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
