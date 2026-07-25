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

    if os.path.isdir(out_root): shutil.rmtree(out_root)
    n_sk = n_ref = n_orph = 0
    unresolved = []

    for desk in sorted(os.listdir('skills')):
        if not os.path.isdir(f'skills/{desk}'): continue
        if os.path.exists(f'skills/{desk}/DEPRECATED.yaml'):
            print(f'  skipped (deprecated): {desk}'); continue
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
                o = f'{dst}/references/{rel}'
                os.makedirs(os.path.dirname(o), exist_ok=True)
                open(o, 'w', encoding='utf-8', newline='').write(txt)
                n_ref += 1
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

    print(f"vendor={a.vendor}  profile={prof['profile']['id']}  ->  {out_root}")
    print(f"  skills built     : {n_sk}")
    print(f"  references shipped: {n_ref}")
    print(f"  unresolved refs  : {len(unresolved)}")
    for s, r in unresolved[:10]: print(f"      {s} -> {r}")
    return 1 if unresolved else 0

sys.exit(main())
