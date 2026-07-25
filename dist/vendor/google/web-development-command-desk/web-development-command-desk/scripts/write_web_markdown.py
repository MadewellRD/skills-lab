#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) < 3:
    raise SystemExit("usage: write_web_markdown.py <output.md> <title>")
out = Path(sys.argv[1])
title = sys.argv[2]
out.write_text(f"# {title}

## How to use this file

Use this artifact as a Web Development Command Desk workflow output.
", encoding="utf-8")
print(out)
