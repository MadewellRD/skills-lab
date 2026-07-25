#!/usr/bin/env python3
"""Emit tracker.json for the v1.1.0 suite build, to the goliveprompt tracker contract.

    python3 tools/track_suites.py [--out docs/engineering-spec/tracker.json]

The file is the state; the HTML artifact is only a view. Status is DERIVED from what is
on disk and from the audit gates, never asserted, so this cannot drift from repo truth.

The contract's done/in_progress split is the whole point of the status field, so it is
honoured strictly here: a suite with every desk written is still `in_progress` until it
passes its acceptance gate. Files existing is not the gate. Clean gates are.
"""
from __future__ import annotations
import argparse, glob, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

SUITES = [
    ('SL-01', 'Security Command Desk'),
    ('SL-02', 'Platform Engineering Command Desk'),
    ('SL-03', 'SRE Reliability Command Desk'),
    ('SL-04', 'Cloud Infrastructure Command Desk'),
    ('SL-05', 'Data Command Desk'),
    ('SL-06', 'GRC Command Desk'),
    ('SL-07', 'Privacy Data Protection Command Desk'),
    ('SL-08', 'Legal Contracts Command Desk'),
    ('SL-09', 'FinOps Command Desk'),
    ('SL-10', 'Customer Success Command Desk'),
    ('SL-11', 'Customer Support Command Desk'),
    ('SL-12', 'Finance Accounting Command Desk'),
    ('SL-13', 'People Talent Command Desk'),
    ('SL-14', 'Procurement Vendor Management Command Desk'),
]

VENDOR = re.compile(r'\b(chatgpt|codex|claude code|gemini|openai|anthropic)\b', re.I)
CITE = re.compile(r'`(references/[^`]+?\.md)`')
ALLOWED_CITES = {
    'references/suite-workflow-contract.md', 'references/halt-taxonomy.md',
    'references/capability-baseline.md', 'references/stage-contracts.md',
}


def planned(desk_dir: str) -> int:
    p = Path('skills') / desk_dir / 'references' / 'stage-contracts.md'
    if not p.exists():
        return 0
    return len(set(re.findall(r'([a-z0-9][a-z0-9-]*-desk)\b', p.read_text(encoding='utf-8'))))


def scan(desk_dir: str) -> dict:
    base = Path('skills') / desk_dir
    bodies = [f for f in base.glob('*.md') if f.name != 'README.md']
    yamls = list(base.glob('_skills/*/skill.yaml'))
    scaffolded = (base / 'references' / 'suite-workflow-contract.md').exists()

    em = vend = badcite = 0
    for f in bodies:
        t = f.read_text(encoding='utf-8')
        em += t.count('—')
        vend += len(VENDOR.findall(t))
        badcite += sum(1 for c in CITE.findall(t) if c not in ALLOWED_CITES)

    n = len(bodies)
    want = planned(desk_dir)
    packaged = len(glob.glob(f'dist/skills/{desk_dir.lower().replace(" ", "-")}/*/SKILL.md'))
    return {'bodies': n, 'planned': want, 'yamls': len(yamls), 'scaffolded': scaffolded,
            'em': em, 'vendor': vend, 'badcite': badcite, 'packaged': packaged}


def suite_task(tid: str, desk_dir: str) -> dict:
    s = scan(desk_dir)
    gates_clean = s['em'] == 0 and s['vendor'] == 0 and s['badcite'] == 0
    complete = s['planned'] > 0 and s['bodies'] >= s['planned'] and s['yamls'] >= s['planned']

    if not s['scaffolded']:
        status, blocked = 'todo', None
    elif not complete:
        status, blocked = 'in_progress', None
    elif not gates_clean:
        # authored but failing its gate: not done, and the reason is stated
        status, blocked = 'in_progress', None
    elif s['packaged'] < s['planned']:
        status, blocked = 'in_progress', None
    else:
        status, blocked = 'done', None

    ev = [f"{s['bodies']}/{s['planned'] or '?'} desks",
          f"{s['yamls']} skill.yaml",
          f"packaged {s['packaged']}"]
    if gates_clean:
        ev.append('gates clean')
    else:
        ev.append(f"GATE FAIL: em={s['em']} vendor={s['vendor']} badcite={s['badcite']}")

    return {
        'id': tid,
        'title': desk_dir,
        'milestone': 'M2',
        'sprint': 1,
        'status': status,
        'acceptance': ('every planned desk has a body and a skill.yaml, the suite passes the '
                       'audit gates with zero em dashes, zero vendor names and zero '
                       'unresolvable citations, and every desk is packaged into dist'),
        'depends_on': [],
        'source': 'recon',
        'blocked_on': blocked,
        'pr': None,
        'evidence': '; '.join(ev),
        'metrics': s,
    }


def gate_task(tid: str, title: str, milestone: str, acceptance: str,
              cmd: list[str] | None, depends: list[str]) -> dict:
    status, ev = 'todo', 'not run'
    if cmd:
        try:
            r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, timeout=300)
            status = 'done' if r.returncode == 0 else 'in_progress'
            tail = [l for l in (r.stdout or '').strip().splitlines() if l.strip()]
            ev = tail[-1][:200] if tail else f'exit {r.returncode}'
        except Exception as e:
            status, ev = 'blocked', f'{type(e).__name__}: {e}'[:200]
    return {'id': tid, 'title': title, 'milestone': milestone, 'sprint': 1,
            'status': status, 'acceptance': acceptance, 'depends_on': depends,
            'source': 'recon', 'blocked_on': None, 'pr': None, 'evidence': ev}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='docs/engineering-spec/tracker.json')
    ap.add_argument('--stamp', help='ISO timestamp; defaults to git HEAD commit time')
    a = ap.parse_args()

    tasks = [suite_task(tid, d) for tid, d in SUITES]
    authored = sum(t['metrics']['bodies'] for t in tasks)
    plan = sum(t['metrics']['planned'] for t in tasks)
    all_authored = all(t['metrics']['planned'] and
                       t['metrics']['bodies'] >= t['metrics']['planned'] for t in tasks)

    ids = [t['id'] for t in tasks]
    tasks.append(gate_task('SL-15', 'Audit gates across the whole corpus', 'M3',
                           'tools/audit_skills.py exits 0 with all 21 suites present',
                           ['tools/audit_skills.py'] if all_authored else None, ids))
    tasks.append(gate_task('SL-16', 'SDLC suite structural validation', 'M3',
                           'tools/validate_sdlc_suite.py exits 0',
                           ['tools/validate_sdlc_suite.py'], []))
    tasks.append(gate_task('SL-17', 'Package and checksum every suite', 'M4',
                           'tools/cut_release.py writes 21 suite package sets and '
                           'validate_release_assets.py exits 0', None, ['SL-15']))
    tasks.append(gate_task('SL-18', 'Publish v1.1.0', 'M4',
                           '21 suite releases plus repo-level v1.1.0 tagged, assets uploaded, '
                           'README, MANIFEST and About reflect 21 suites', None, ['SL-17']))

    # Wall-clock generation time, NOT the git commit time. The view uses this both as its
    # staleness indicator and as the key that decides whether to re-render, so anchoring it
    # to a commit means the tracker silently stops updating between commits, which is the
    # one behaviour a live tracker must not have.
    from datetime import datetime, timezone
    stamp = a.stamp or datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    head = ''
    try:
        head = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                              capture_output=True, text=True).stdout.strip()
    except Exception:
        pass

    doc = {
        'project': 'Skills-Lab v1.1.0',
        'generated_at': stamp,
        'head': head,
        'summary': {'desks_authored': authored, 'desks_planned': plan,
                    'suites_done': sum(1 for t in tasks[:14] if t['status'] == 'done'),
                    'suites_total': len(SUITES)},
        'milestones': [
            {'id': 'M1', 'name': 'Suite design and scaffolding', 'sprint': 1},
            {'id': 'M2', 'name': 'Desk authoring', 'sprint': 1},
            {'id': 'M3', 'name': 'Verification', 'sprint': 1},
            {'id': 'M4', 'name': 'Release', 'sprint': 1},
        ],
        'tasks': tasks,
        'commits': [],
    }
    try:
        raw = subprocess.run(['git', 'log', '-12', '--format=%h%x1f%s%x1f%cI'],
                             capture_output=True, text=True).stdout.strip().splitlines()
        doc['commits'] = [dict(zip(('sha', 'message', 'date'), l.split('\x1f'))) | {'task': None}
                          for l in raw if l.count('\x1f') == 2]
    except Exception:
        pass

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    # Atomic write. write_text truncates in place, so a poller reading on the wrong tick
    # sees a missing or half-written file. os.replace is atomic on POSIX and Windows, so a
    # reader always gets either the previous complete file or the new complete file.
    tmp = out.with_suffix(out.suffix + '.tmp')
    tmp.write_text(json.dumps(doc, indent=2) + '\n', encoding='utf-8', newline='')
    os.replace(tmp, out)
    print(f"{out}: {authored}/{plan} desks, "
          f"{doc['summary']['suites_done']}/{len(SUITES)} suites done")
    return 0


sys.exit(main())
