#!/usr/bin/env python3
"""Audit the skills corpus against the active capability profile.

Run this after every profile bump. Non-zero exit = something needs attention.
Checks structural integrity first (things that BREAK), then capability debt
(things that are merely STALE), then governance (things that must NOT have been lost).
"""
import glob, os, re, sys, yaml, hashlib
from collections import Counter, defaultdict

prof = yaml.safe_load(open('profiles/frontier-2026-07.yaml', encoding='utf-8'))
CITE = re.compile(r'`(references/[^`]+?\.md|scripts/[^`]+?\.py)`')
fail = 0
def head(t): print(f"\n{'='*62}\n{t}\n{'='*62}")

head("1. STRUCTURAL INTEGRITY  (these break the build)")
broken = unresolved_tok = 0
for sk in glob.glob('dist/skills/*/*/SKILL.md'):
    d = os.path.dirname(sk); t = open(sk, encoding='utf-8').read()
    for c in CITE.findall(t):
        if not os.path.exists(os.path.join(d, c)):
            broken += 1; print(f"  BROKEN  {d.split('/')[-1]} -> {c}")
    unresolved_tok += len(re.findall(r'\{\{[A-Z_]+', t))
print(f"  broken citations        : {broken}")
print(f"  unresolved {{{{TOKENS}}}}     : {unresolved_tok}")
fail += (broken > 0) + (unresolved_tok > 0)

head("2. VENDOR NEUTRALITY  (the frontier-agnostic claim)")
BIB = re.compile(r'(source-inventory|standards-source-map|source-analysis)\.md$')
leak = []
for f in glob.glob('dist/skills/**/*.md', recursive=True):
    if BIB.search(f): continue
    for m in re.findall(r'\b(ChatGPT|Codex|Claude Code)\b', open(f, encoding='utf-8').read()):
        leak.append((os.path.basename(f), m))
print(f"  vendor mentions in generic build: {len(leak)}   (bibliography files exempt)")
for f, m in leak[:8]: print(f"    {f}: {m}")
fail += len(leak) > 0

head("3. CAPABILITY DEBT  (stale assumptions vs active profile)")
# Documented exceptions. Each needs a reason, so this list stays short and honest.
ACCEPTED = {
 'skills/SDLC Command Desk/implementation-handoff-desk.md':
   'frontmatter description is a TRIGGER surface; users still phrase it "low-token". '
   'Changing it would cost skill recall without changing model behavior.',
 'kernel/references/handoff-density-policy.md':
   'deliberately documents the superseded premise so the reason for the change survives.',
}
DEBT = {
 'token-conservation premise': r'\b(low.token|conserve tokens|token conservation|minimi[sz]e tokens)\b',
 'agent self-verification scaffolding': r'(use a (?:subagent|sub-agent) to verify|include a final verification step|double.check your (?:work|output))',
 'halt-on-mere-uncertainty': r'halt (?:when|if)[^.\n]{0,50}\b(?:unclear|uncertain|ambiguous)\b',
}
fail_debt = []
for name, p in DEBT.items():
    rx = re.compile(p, re.I); hits = []
    for f in glob.glob('skills/**/*.md', recursive=True) + glob.glob('kernel/**/*.md', recursive=True):
        if f.replace(os.sep, '/') in ACCEPTED: continue
        n = len(rx.findall(open(f, encoding='utf-8').read()))
        if n: hits.append((f, n))
    tot = sum(n for _, n in hits)
    print(f"  {name:<38} {tot:>4} hits / {len(hits)} files")
    for f, n in hits[:4]: print(f"       {f}")
    if tot: fail_debt.append(name)

print(f"  accepted exceptions     : {len(ACCEPTED)} (documented in tools/audit_skills.py)")
fail += len(fail_debt) > 0

head("4. GOVERNANCE INVARIANTS  (must survive every upgrade)")
INV = {'never-invent rule': r'\b(never invent|do not invent|must not invent)\b',
       'fact vs assumption separation': r'\b(assumption|assumptions)\b',
       'halt taxonomy adoption': r'HARD_HALT_|halt-taxonomy'}
bodies = [f for f in glob.glob('skills/*/*.md') if os.path.basename(f) != 'README.md']
for name, p in INV.items():
    rx = re.compile(p, re.I)
    n = sum(1 for f in bodies if rx.search(open(f, encoding='utf-8').read()))
    print(f"  {name:<38} {n:>4} / {len(bodies)} skill bodies")

head("5. PROFILE ADOPTION")
tot = len(glob.glob('dist/skills/*/*/SKILL.md'))
adopt = len([f for f in glob.glob('dist/skills/*/*/SKILL.md')
             if 'capability-baseline.md' in open(f, encoding='utf-8').read()])
print(f"  active profile : {prof['profile']['id']}  (established {prof['profile']['established']})")
print(f"  adoption       : {adopt}/{tot} skills")
fail += adopt != tot

head("6. DUPLICATION")
h = defaultdict(list)
for f in bodies: h[hashlib.md5(open(f, 'rb').read()).hexdigest()].append(f)
d = {k: v for k, v in h.items() if len(v) > 1}
print(f"  duplicate skill bodies in source: {sum(len(v)-1 for v in d.values())}")
for k, v in list(d.items())[:5]: print(f"    {[x.split('/')[1] for x in v]}")

print(f"\n{'='*62}\nRESULT: {'PASS' if not fail else str(fail)+' CHECK(S) FAILED'}\n{'='*62}")
sys.exit(1 if fail else 0)
