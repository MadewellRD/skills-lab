#!/usr/bin/env python3
"""Write a wrapped release operations Markdown artifact."""

import argparse
from pathlib import Path


def build_markdown(title: str, artifact: str, source_facts: list[str]) -> str:
    lines = [
        f"# {title}",
        "",
        "## How to use this file",
        "",
        "Use this release operations artifact for review, go/no-go decisions, downstream handoff, or execution planning. Preserve source facts, unknowns, and halt conditions when copying into another agent.",
        "",
        "## Artifact",
        "",
        artifact.rstrip(),
        "",
    ]
    if source_facts:
        lines.extend(["## Source facts", ""])
        lines.extend(f"- {fact}" for fact in source_facts)
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Write a release operations Markdown artifact.")
    parser.add_argument("--title", required=True, help="Artifact title")
    parser.add_argument("--body-file", required=True, help="Path to a UTF-8 Markdown body file")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    parser.add_argument("--source-fact", action="append", default=[], help="Source fact to append; may be repeated")
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.exists():
        raise SystemExit(f"body file not found: {body_path}")

    body = body_path.read_text(encoding="utf-8")
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_markdown(args.title, body, args.source_fact), encoding="utf-8")
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
