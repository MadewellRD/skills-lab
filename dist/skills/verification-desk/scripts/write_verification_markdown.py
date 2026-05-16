#!/usr/bin/env python3
"""Write a wrapped verification artifact Markdown file."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_document(title: str, report: str, usage: str) -> str:
    return f"# {title}\n\n## How to use this file\n\n{usage.strip()}\n\n## Report\n\n{report.strip()}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a wrapped verification Markdown artifact.")
    parser.add_argument("--title", required=True, help="Artifact title")
    parser.add_argument("--report-file", required=True, help="Path to a Markdown file containing report body")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    parser.add_argument(
        "--usage",
        default=(
            "Use this report to decide whether scoped work is verified, blocked, "
            "or needs follow-up. Preserve source facts, evidence mapping, gaps, "
            "and downstream handoff notes."
        ),
        help="How-to-use text",
    )
    args = parser.parse_args()

    report_path = Path(args.report_file)
    if not report_path.exists():
        raise SystemExit(f"report file not found: {report_path}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_document(args.title, report_path.read_text(), args.usage), encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
