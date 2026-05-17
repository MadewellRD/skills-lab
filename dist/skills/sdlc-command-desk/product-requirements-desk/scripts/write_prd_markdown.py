#!/usr/bin/env python3
"""Write a wrapped Product Requirements Desk Markdown artifact."""
from __future__ import annotations

import argparse
from pathlib import Path

VALID_MODES = {
    "prd": "product-requirements-document.md",
    "acceptance": "acceptance-criteria.md",
    "review": "requirements-review.md",
    "sources": "requirements-source-facts.md",
    "diagnostic": "connector-diagnostic.md",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a Product Requirements Desk markdown artifact.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--mode", choices=sorted(VALID_MODES), default="prd")
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.exists():
        raise FileNotFoundError(f"body file not found: {body_path}")

    body = body_path.read_text(encoding="utf-8").strip()
    out = Path(args.out)
    wrapper = (
        f"# {args.title}\n\n"
        "## How to use this file\n\n"
        "Use this artifact as a product requirements source for the next SDLC stage. Preserve source facts, open questions, and non-goals when handing off downstream.\n\n"
        f"## Artifact mode\n\n{args.mode}\n\n"
        f"{body}\n"
    )
    out.write_text(wrapper, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
