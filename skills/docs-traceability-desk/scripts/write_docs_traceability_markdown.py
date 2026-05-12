#!/usr/bin/env python3
"""Write a docs traceability markdown artifact with a standard wrapper."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_document(title: str, how_to_use: str, source_facts: list[str], artifact: str) -> str:
    facts = "\n".join(f"- {fact}" for fact in source_facts) if source_facts else "- No source facts supplied."
    return f"# {title}\n\n## How to use this file\n\n{how_to_use}\n\n## Source facts\n\n{facts}\n\n## Artifact\n\n{artifact.rstrip()}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a docs traceability markdown artifact.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--how-to-use", required=True)
    parser.add_argument("--artifact-file", required=True, help="Path to a markdown file containing the artifact body.")
    parser.add_argument("--out", required=True, help="Output markdown path.")
    parser.add_argument("--source-fact", action="append", default=[])
    args = parser.parse_args()

    artifact_path = Path(args.artifact_file)
    if not artifact_path.exists():
        raise SystemExit(f"artifact file not found: {artifact_path}")

    artifact = artifact_path.read_text(encoding="utf-8")
    output = build_document(args.title, args.how_to_use, args.source_fact, artifact)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
