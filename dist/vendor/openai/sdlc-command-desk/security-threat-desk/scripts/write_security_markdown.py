#!/usr/bin/env python3
"""Write a Security Threat Desk markdown artifact with a standard wrapper."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_document(title: str, usage: str, body: str) -> str:
    return f"# {title}\n\n## How to use this file\n\n{usage.strip()}\n\n## Artifact\n\n{body.strip()}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a security/threat-model markdown artifact.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--usage", required=True)
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    body_path = Path(args.body_file)
    if not body_path.exists():
        raise SystemExit(f"body file not found: {body_path}")

    body = body_path.read_text(encoding="utf-8")
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_document(args.title, args.usage, body), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
