#!/usr/bin/env python3
"""Build dist/ skill packages from the 3-tier source cascade + capability profile.

  kernel/references/                          tier 1  shared default
  skills/<Desk>/references/                   tier 2  suite override
  skills/<Desk>/_skills/<slug>/references/    tier 3  skill override

Resolution is most-specific-wins. Only transitively-cited references ship,
which is what removes the orphaned copies. Vendor tokens resolve from
profiles/vendors/<vendor>.yaml so one skill body builds for every vendor.
"""
import os, re, glob, shutil, argparse, yaml, sys

CITE = re.compile(r'`(references/[^`]+?\.md)`')
TOKEN = re.compile(r'\{\{([A-Z_]+)(?::([a-z0-9-]+))?\}\}')
SENT_START = re.compile(r'(^|[.!?]\s+|\n[-*]\s+|\n#+\s+)$')

def load(p): return yaml.safe_load(open(p, encoding='utf-8'))

def slug_of(desk): return desk.lower().replace(' ', '-')

def resolve_ref(desk, slug, ref):
    for cand in (f'skills/{desk}/_skills/{slug}/references/{ref}',
                 f'skills/{desk}/references/{ref}',
                 f'kernel/references/{ref}'):
        if os.path.exists(cand): return cand
    return None

def subst(text, tokens):
    """Replace {{TOKEN}} with vendor value, capitalising at sentence start."""
    out = []; last = 0
    for m in TOKEN.finditer(text):
        key, arg = m.group(1), m.group(2)
        val = tokens.get(key, m.group(0))
        if key == 'INVOKE' and arg:
            val = tokens.get('INVOKE', '{}').replace('<skill-name>', arg)
        if SENT_START.search(text[max(0, m.start()-80):m.start()]) and val[:1].islower():
            val = val[0].upper() + val[1:]
        out.append(text[last:m.start()]); out.append(val); last = m.end()
    out.append(text[last:])
    return ''.join(out)



# Reference files renamed in v1.0.0. The build emits the OLD name as a pointer for one
# release cycle so forks and vendored copies keep resolving. Remove in v1.1.0.
# Retired in v1.1.0 at the maintainer's direction. The old names no longer ship.
# Anything still reading codex-conservation-policy.md, low-token-policy.md, or the
# platform low-token variants must move to *-handoff-density-policy.md.
COMPAT_SHIMS = {}
# Schema keys renamed in v1.0.0. These are not files, so a pointer file cannot shim them.
# The continuity packet is produced and consumed by the model, so the shim is an
# instruction: accept the old key on read, always emit the new one on write.
# Injected into continuity-kernel.md at build time. Emptying this dict removes the
# section, with no dangling citation left behind.
# Retired in v1.1.0. A packet using codex_handoff or max_context_policy now reads as
# missing those fields rather than as an error.
KEY_ALIASES = {}
# Retirement is a DATE, not a version. A version number can arrive the week after the one
# that introduced the shims, which gives forks no real adaptation window: the calendar is
# what actually lets downstream consumers catch up, so the calendar is what we commit to.
# tools/audit_skills.py reports when this date is near or past.
# Shims retired in v1.1.0. Kept as a marker of when, and so the audit can state that
# nothing is being carried rather than leaving the reader to infer it from a zero.
SHIM_RETIRE_AFTER = 'retired in v1.1.0'


def alias_section():
    if not KEY_ALIASES:
        return ''
    rows = '\n'.join(f'| `{o}` | `{n}` |' for o, n in sorted(KEY_ALIASES.items()))
    return (
        '\n## Deprecated keys\n\n'
        'A packet written before v1.0.0 may carry the older key names below. Accept them on '
        'read and treat them as equivalent. Always write the current name.\n\n'
        '| Accepted on read | Write this |\n|---|---|\n' + rows + '\n\n'
        'Do not carry both spellings in the same packet, and do not rewrite a prior stage\'s '
        'packet solely to rename a key: migrate it when you next write the packet, so a\n'
        'resumed workflow is never blocked by a naming difference.\n\n'
        f'These aliases are removed after {SHIM_RETIRE_AFTER}. Past that date a packet using '
        'the old names is read as missing those fields rather than as an error, so migrate '
        'before then.\n')

def shim_body(old, new):
    return (f"# Moved: `{old}`\n\n"
            f"This file was renamed in v1.0.0. The current version is **`{new}`** in this "
            f"same `references/` directory. Read that instead; it is the authoritative copy.\n\n"
            f"The rename went with a change of premise, not just a name. Context is no longer "
            f"scarce, so the rule is no longer 'send less'. It is 'send the right thing': a "
            f"handoff is judged on whether it removes ambiguity, not on how short it is.\n\n"
            f"This pointer exists so forks and vendored copies keep resolving while they "
            f"catch up. It is removed after {SHIM_RETIRE_AFTER}; update any reference to the "
            f"old name before then.\n")

def render_capability_baseline(prof):
    """Render kernel/references/capability-baseline.md FROM the profile.

    This file is what every skill reads to learn what it may assume. If it were
    hand-authored, a profile bump would stamp a new version into metadata while the
    skills kept reading the old numbers: upgraded by label, stale in substance.
    Generating it is what makes a profile bump actually propagate.
    """
    P = prof['profile']; caps = prof.get('capabilities', {})
    ar = prof.get('authoring_rules', {}); inv = prof.get('invariants', [])
    L = []
    L.append('# Capability Baseline\n')
    L.append(f"Generated by `tools/build_skills.py` from `profiles/{P['id']}.yaml` "
             f"(established {P['established']}). Do not edit by hand; edit the profile "
             "and rebuild, or the next build overwrites your changes.\n")
    L.append('This file tells a desk what it may assume about the model executing it. It '
             'exists so capability assumptions live in exactly one place instead of being '
             're-litigated inside every skill body.\n')
    a = prof.get('authoring_standard') or {}
    if a:
        L.append('## How this skill was authored\n')
        L.append(' '.join(str(a.get('policy', '')).split()) + '\n')
        rec = a.get('record') or []
        if rec:
            last = rec[-1]
            eff = f", {last['effort']} effort" if last.get('effort') else ''
            L.append(f"Most recent authoring pass: **{last.get('model')}**{eff}, "
                     f"{last.get('version')}, {last.get('date')}.\n")
        sched = a.get('scheduled') or []
        if sched:
            names = ', '.join(f"{x.get('model')} ({x.get('effort')})" for x in sched)
            L.append(f"Scheduled next passes: {names}, {sched[0].get('date')}. Authoring "
                     "across more than one vendor's frontier model tests whether this corpus "
                     "encodes a single vendor's house style in its structure, which token "
                     "substitution alone cannot reveal.\n")
        L.append('This is the build bench, not a runtime requirement. The capabilities '
                 'below are what the *executing* model may assume, and they are a floor '
                 'held across vendors rather than any single vendor ceiling.\n')
    L.append('## What you may assume\n')
    L.append('| Capability | Value | What it unlocks |')
    L.append('|---|---|---|')
    ctx = caps.get('context_class', {})
    if ctx:
        i, o = ctx.get('input_tokens'), ctx.get('output_tokens')
        fmt = lambda n: f"{n//1000000}M" if n and n >= 1000000 else (f"{n//1000}k" if n else '?')
        L.append(f"| Context | ~{fmt(i)} input / {fmt(o)} output | "
                 f"{' '.join(str(ctx.get('implication','')).split())} |")
    for k, v in caps.items():
        if k == 'context_class' or not isinstance(v, dict): continue
        val = str(v.get('value', ''))
        if v.get('degrade'): val += ', optional'
        L.append(f"| {k.replace('_',' ').capitalize()} | {val} | "
                 f"{' '.join(str(v.get('implication','')).split())} |")
    L.append('')
    L.append('## How this changes authoring\n')
    for k, v in ar.items():
        if not isinstance(v, dict): continue
        L.append(f"**{k.replace('_',' ').capitalize()}.** {' '.join(str(v.get('rule','')).split())}")
        for extra in ('keep_numbered_when', 'depth_rule', 'guard'):
            if v.get(extra):
                L.append(f"\n{' '.join(str(v[extra]).split())}")
        if v.get('was'):
            L.append(f"\nSupersedes: `{v['was']}`.")
        L.append('')
    L.append('## What does NOT change\n')
    L.append('These are governance boundaries, not model scaffolding. They do not relax as '
             'models improve, because capability raises the fluency of a wrong answer as '
             'fast as it raises the accuracy of a right one:\n')
    for i in inv:
        L.append(f"- **{i['id']}** {i['rule']}")
    L.append('')
    L.append('A more capable model is a reason to remove *scaffolding*, never a reason to '
             'remove *governance*.')
    return '\n'.join(L) + '\n'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vendor', default='generic')
    ap.add_argument('--profile', default='profiles/frontier-2026-07.yaml')
    ap.add_argument('--out', default=None)
    a = ap.parse_args()

    prof = load(a.profile)
    vend = load(f'profiles/vendors/{a.vendor}.yaml')
    tokens = vend['tokens']
    out_root = a.out or ('dist/skills' if a.vendor == 'generic' else f'dist/vendor/{a.vendor}')

    # regenerate the baseline from the profile BEFORE resolving references,
    # so every skill in this build reads the profile actually being built
    os.makedirs('kernel/references', exist_ok=True)
    open('kernel/references/capability-baseline.md', 'w', encoding='utf-8',
         newline='').write(render_capability_baseline(prof))

    if os.path.isdir(out_root): shutil.rmtree(out_root)
    n_sk = n_ref = n_orph = n_shim = 0
    unresolved = []

    for desk in sorted(os.listdir('skills')):
        if not os.path.isdir(f'skills/{desk}'): continue
        if os.path.exists(f'skills/{desk}/DEPRECATED.yaml'):
            print(f'  skipped (deprecated): {desk}'); continue
        # A suite mid-authoring would otherwise ship as a partial package. Compare the
        # bodies on disk against the roster the suite declares in its stage contracts.
        sc = f'skills/{desk}/references/stage-contracts.md'
        if os.path.exists(sc):
            roster = set(re.findall(r'([a-z0-9][a-z0-9-]*-desk)\b',
                                    open(sc, encoding='utf-8').read()))
            have = len([f for f in glob.glob(f'skills/{desk}/*.md')
                        if os.path.basename(f) != 'README.md'])
            if roster and have < len(roster):
                print(f'  skipped (incomplete {have}/{len(roster)}): {desk}'); continue
        bodies = [f for f in glob.glob(f'skills/{desk}/*.md')
                  if os.path.basename(f) != 'README.md']
        if not bodies: continue
        for body_path in sorted(bodies):
            slug = os.path.basename(body_path)[:-3]
            slug = re.sub(r'^\d+-', '', slug)                 # 000-foo-desk -> foo-desk
            src = f'skills/{desk}/_skills/{slug}'
            dst = f'{out_root}/{slug_of(desk)}/{slug}'
            os.makedirs(dst, exist_ok=True)

            body = subst(open(body_path, encoding='utf-8').read(), tokens)
            # every skill adopts the capability profile, automatically.
            # a future profile bump therefore reaches 100% of skills with no manual edit.
            if 'references/capability-baseline.md' not in body:
                body = body.rstrip() + (
                    "\n\n## Capability baseline\n\n"
                    "Use `references/capability-baseline.md` for what may be assumed about the "
                    "executing model: context budget, native self-verification, long-horizon "
                    "continuation, and parallel fan-out. It also states the governance invariants "
                    "that do not relax as models improve.\n")
            open(f'{dst}/SKILL.md', 'w', encoding='utf-8', newline='').write(body)
            n_sk += 1

            # transitive citation closure -> only ship what is reachable
            want, seen = set(CITE.findall(body)), set()
            while want:
                ref = want.pop()
                if ref in seen: continue
                seen.add(ref)
                rel = ref[len('references/'):]
                p = resolve_ref(desk, slug, rel)
                if not p:
                    unresolved.append((slug, ref)); continue
                txt = subst(open(p, encoding='utf-8').read(), tokens)
                if rel == 'continuity-kernel.md' and KEY_ALIASES:
                    txt = txt.rstrip() + '\n' + alias_section()
                    n_shim += 1
                o = f'{dst}/references/{rel}'
                os.makedirs(os.path.dirname(o), exist_ok=True)
                open(o, 'w', encoding='utf-8', newline='').write(txt)
                n_ref += 1
                for old, new in COMPAT_SHIMS.items():
                    if new == rel:
                        so = f'{dst}/references/{old}'
                        os.makedirs(os.path.dirname(so), exist_ok=True)
                        open(so, 'w', encoding='utf-8', newline='').write(shim_body(old, new))
                        n_shim += 1
                want |= set(CITE.findall(txt)) - seen

            for kind in ('scripts', 'assets'):
                for f in glob.glob(f'{src}/{kind}/**/*', recursive=True):
                    if os.path.isfile(f):
                        o = f'{dst}/{kind}/{os.path.relpath(f, f"{src}/{kind}")}'
                        os.makedirs(os.path.dirname(o), exist_ok=True); shutil.copy2(f, o)

            sy = f'{src}/skill.yaml'
            if os.path.exists(sy):
                y = load(sy)
                itf = y.get('interface', {})
                for k in ('display_name', 'short_description', 'default_prompt'):
                    if itf.get(k): itf[k] = subst(str(itf[k]), tokens)
                y['policy'] = y.get('policy', {})
                y['policy']['products'] = vend.get('products', [vend['vendor']])
                y['_generated'] = {'profile': prof['profile']['id'], 'vendor': vend['vendor']}
                os.makedirs(f'{dst}/agents', exist_ok=True)
                yaml.safe_dump(y, open(f'{dst}/agents/{vend["vendor"]}.yaml', 'w', encoding='utf-8'),
                               sort_keys=False, allow_unicode=True)
                # pre-v1.0.0 consumers looked for agents/openai.yaml unconditionally
                if False:  # legacy agents/openai.yaml retired in v1.1.0
                    y2 = dict(y); y2['_deprecated'] = (
                        f'Legacy path. Use agents/{vend["vendor"]}.yaml. '
                        f'Removed after {SHIM_RETIRE_AFTER}.')
                    yaml.safe_dump(y2, open(f'{dst}/agents/openai.yaml', 'w', encoding='utf-8'),
                                   sort_keys=False, allow_unicode=True)

    print(f"vendor={a.vendor}  profile={prof['profile']['id']}  ->  {out_root}")
    print(f"  skills built     : {n_sk}")
    print(f"  references shipped: {n_ref}")
    print(f"  compat shims      : {n_shim}  ({SHIM_RETIRE_AFTER})")
    print(f"  unresolved refs  : {len(unresolved)}")
    for s, r in unresolved[:10]: print(f"      {s} -> {r}")
    return 1 if unresolved else 0

sys.exit(main())
