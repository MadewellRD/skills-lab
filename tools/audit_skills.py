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
 'kernel/references/capability-baseline.md':
   'generated from the profile and necessarily QUOTES the banned verification phrasing '
   'in order to prohibit it. The detector cannot distinguish instructing from forbidding.',
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

head("3b. OUTPUT AMBITION  (regression check)")
bodies_oa = [f for f in glob.glob('skills/*/*.md')
             if os.path.basename(f) != 'README.md' and 'Sales Revenue' not in f]
# Detect REGRESSION, not compliance.
# A semantic sweep confirmed 109/109 state a complete-run set and carry an
# anti-fabrication guard. Both are worded differently in every file on purpose -
# identical boilerplate is exactly what the output_ambition rule exists to prevent.
# Matching good prose by regex failed twice here: it flagged well-written guards
# like "an unmeasured metric stays unmeasured in writing" as missing.
# Detecting the OLD menu phrasing is reliable, so that is what is gated.
MENU = re.compile(r'(smallest (?:complete )?artifact|one of the following|pick one|'
                  r'produce (?:only )?the artifact needed|whichever artifact)', re.I)
# Negations are the CORRECT construction ("delivers a set rather than the smallest
# artifact", "do not silently pick one"), so exclude them or the check fires on
# exactly the prose it is meant to reward.
NEG = re.compile(r'(rather than|instead of|not |never|do not|avoid|no longer)', re.I)
regressed = []
for f in bodies_oa:
    txt = open(f, encoding='utf-8').read()
    for m in MENU.finditer(txt):
        if NEG.search(txt[max(0, m.start()-24):m.start()]): continue
        regressed.append((f, m.group(0)))
print(f"  menu-phrasing regressions  : {len(regressed)} (0 expected)")
for f, m in regressed[:6]: print(f"      {os.path.basename(f)}: \"{m}\"")
print("  set-per-run + guard        : verified semantically, not regex-gated")
print("                               (see docs/model-upgrade-playbook.md)")
fail += len(regressed) > 0

head("3c. HOUSE STYLE")
# Mechanically decidable, unlike the prose checks above, so this one is gated.
em = []
for f in (glob.glob('skills/**/*.md', recursive=True) + glob.glob('kernel/**/*.md', recursive=True)
          + glob.glob('docs/*.md') + glob.glob('profiles/**/*.yaml', recursive=True)
          + glob.glob('dist/**/*.md', recursive=True)):
    n = open(f, encoding='utf-8').read().count('\u2014')
    if n: em.append((f, n))
print(f"  em dashes                  : {sum(n for _, n in em)} (0 required)")
for f, n in em[:6]: print(f"      {n:>3}  {f}")
fail += len(em) > 0

head("3d. COMPATIBILITY SHIMS")
import importlib.util as _ilu
_sp = _ilu.spec_from_file_location('bs', 'tools/build_skills.py')
try:
    _src = open('tools/build_skills.py', encoding='utf-8').read()
    _ns = {}
    exec(_src.split('def main(')[0], {'re': re, 'os': os, 'glob': glob}, _ns)
    _files, _keys = _ns.get('COMPAT_SHIMS', {}), _ns.get('KEY_ALIASES', {})
    _target = _ns.get('SHIM_RETIRE_AFTER', '?')
except Exception:
    _files, _keys, _target = {}, {}, '?'
_shipped = len(glob.glob('dist/skills/*/*/references/**/*.md', recursive=True))
_ptr = sum(1 for f in glob.glob('dist/skills/*/*/references/**/*.md', recursive=True)
           if open(f, encoding='utf-8').read().startswith('# Moved: '))
_alias = sum(1 for f in glob.glob('dist/skills/*/*/references/continuity-kernel.md')
             if 'Deprecated keys' in open(f, encoding='utf-8').read())
print(f"  file renames shimmed  : {len(_files)}  -> {_ptr} pointer files shipped")
print(f"  schema keys aliased   : {len(_keys)}  -> {_alias} kernels carrying the alias table")
print(f"  legacy agents/openai  : {len(glob.glob('dist/skills/*/*/agents/openai.yaml'))}")
print(f"  retire after          : {_target}")
# A date only helps if something checks it, otherwise it is a string nobody reads.
if _target != '?' and (_files or _keys):
    from datetime import date as _d
    try:
        _y, _m, _dd = (int(x) for x in _target.split('-'))
        _left = (_d(_y, _m, _dd) - _d.today()).days
        if _left < 0:
            print(f"  ACTION: retirement date passed {abs(_left)} days ago. Empty COMPAT_SHIMS")
            print( "          and KEY_ALIASES in tools/build_skills.py, rebuild, and update")
            print( "          the breaking-changes table in tools/cut_release.py.")
        elif _left <= 30:
            print(f"  due in {_left} days")
        else:
            print(f"  {_left} days remaining")
    except ValueError:
        print("  WARNING: retirement date is unparseable")
if not _files and not _keys:
    print("  none active. Confirm the release notes no longer promise them.")

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
