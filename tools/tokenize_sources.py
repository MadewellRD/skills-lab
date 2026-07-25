#!/usr/bin/env python3
"""Replace hardcoded vendor names in source with neutral tokens.

Three protections, each learned from a failed dry run:
  1. Code spans containing paths are frozen (`codex-conservation-policy.md` stays intact).
  2. Bibliography files are skipped entirely - they cite real vendor products as
     external standards, and tokenizing a citation destroys its attribution.
  3. Vendor enumerations collapse to ONE token instead of repeating it
     ("Codex, Claude Code, or other agents" -> "{{CODING_AGENT}} or other agents").
"""
import re, glob, os, argparse

# 2. files whose whole purpose is citing external vendor work
BIBLIOGRAPHY = re.compile(r'(source-inventory|standards-source-map|source-analysis)\.md$')

# 3. collapse enumerations first - order matters
ENUMS = [
    (re.compile(r'\b(?:Codex|Claude Code)\b(?:\s*,\s*(?:Codex|Claude Code)\b)*\s*,?\s*(?:or|and)\s+(?:the\s+)?other coding agents?', re.I),
     '{{CODING_AGENT}} or other coding agents'),
    (re.compile(r'\b(?:Codex|Claude Code)\b\s*,\s*(?:Codex|Claude Code)\b\s*,?\s*(?:or|and)\s+the target implementation agent', re.I),
     '{{CODING_AGENT}} or the target implementation agent'),
    (re.compile(r'\b(?:Codex|Claude Code)\b(?:\s*,\s*(?:Codex|Claude Code)\b)*\s+(?:or|and)\s+(?:Codex|Claude Code)\b', re.I),
     '{{CODING_AGENT}}'),
]
TOKENS = [
    (re.compile(r'\bCODEX_BLOCKER\b'),     '{{BLOCKER_TAG}}'),
    (re.compile(r'\bClaude Code\b', re.I), '{{CODING_AGENT}}'),
    (re.compile(r'\bCodex\b', re.I),       '{{CODING_AGENT}}'),
    (re.compile(r'\bChatGPT\b', re.I),     '{{AGENT}}'),
]
PATHISH = re.compile(r'`[^`]*?(?:/|\.md|\.py|\.yaml|\.json)[^`]*?`')

def convert(text):
    frozen = []
    def stash(m):
        frozen.append(m.group(0)); return f'\x00{len(frozen)-1}\x00'
    body = PATHISH.sub(stash, text)                       # 1. freeze paths
    n = 0
    for rx, rep in ENUMS + TOKENS:
        body, k = rx.subn(rep, body); n += k
    body = re.sub(r'\x00(\d+)\x00', lambda m: frozen[int(m.group(1))], body)
    return body, n

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()
    files = sorted(glob.glob('skills/**/*.md', recursive=True) +
                   glob.glob('kernel/**/*.md', recursive=True))
    tot = touched = skipped = 0
    for f in files:
        if BIBLIOGRAPHY.search(f):
            skipped += 1; continue                        # 2. never touch citations
        orig = open(f, encoding='utf-8').read()
        new, n = convert(orig)
        if n:
            tot += n; touched += 1
            if a.apply:
                open(f, 'w', encoding='utf-8', newline='').write(new)
    print(f"{'APPLIED' if a.apply else 'DRY RUN'}: {tot} replacements / {touched} files "
          f"({skipped} bibliography files protected)")
    if a.apply:
        res = []
        for f in files:
            if BIBLIOGRAPHY.search(f): continue
            body = PATHISH.sub('', open(f, encoding='utf-8').read())
            for rx, _ in TOKENS:
                for m in rx.findall(body): res.append((f, m))
        print(f"residual vendor mentions: {len(res)}")
        for f, m in res[:10]: print(f"   {os.path.basename(f)}: {m}")

main()
