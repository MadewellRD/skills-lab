#!/usr/bin/env python3
"""Cut a release: package every suite, write checksums, manifests, and release notes.

Replaces the per-suite generate_*_release.py scripts with one command, matching the
same principle as the build: a release should be a version argument, not five scripts
that drift apart.

    python3 tools/cut_release.py --version 1.0.0

Zips are deterministic. Entry order is sorted and every timestamp is fixed, so the same
source produces byte-identical archives and therefore stable checksums. Without this a
rebuild changes every hash and checksum verification becomes meaningless.
"""
from __future__ import annotations
import argparse, hashlib, json, os, shutil, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist' / 'skills'
PKG = ROOT / 'dist' / 'packages'
MAN = ROOT / 'dist' / 'manifests'
REL = ROOT / 'releases'
FIXED_TS = (2026, 1, 1, 0, 0, 0)          # deterministic archive timestamps

SUITE_TITLES = {
    'sdlc-command-desk': 'SDLC Command Desk',
    'web-development-command-desk': 'Web Development Command Desk',
    'ai-engineering-command-desk': 'AI Engineering Command Desk',
    'product-command-desk': 'Product Command Desk',
    'sales-command-desk': 'Sales Command Desk',
    'android-command-desk': 'Android Command Desk',
    'ios-command-desk': 'iOS Command Desk',
}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def zip_skill(skill_dir: Path, out: Path) -> None:
    """Deterministic zip of one skill directory."""
    files = sorted(p for p in skill_dir.rglob('*') if p.is_file())
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in files:
            arc = f'{skill_dir.name}/{f.relative_to(skill_dir).as_posix()}'
            zi = zipfile.ZipInfo(arc, date_time=FIXED_TS)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, f.read_bytes())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--version', required=True, help='e.g. 1.0.0')
    ap.add_argument('--date', required=True, help='ISO date, e.g. 2026-07-25')
    ap.add_argument('--suite', action='append', help='limit to suite slug(s)')
    a = ap.parse_args()
    ver = a.version.lstrip('v')

    suites = sorted(a.suite or [d.name for d in DIST.iterdir() if d.is_dir()])
    root_lines: list[str] = []
    summary: list[tuple[str, int, int]] = []

    for slug in suites:
        sdir = DIST / slug
        skills = sorted(d for d in sdir.iterdir() if d.is_dir())
        # orchestrator first, then alphabetical: the 000 slot is the suite entry point
        skills.sort(key=lambda p: (p.name != slug, p.name))

        outdir = PKG / slug
        if outdir.exists():
            shutil.rmtree(outdir)
        outdir.mkdir(parents=True)

        entries = []
        for i, sk in enumerate(skills):
            z = outdir / f'{i:03d}-{sk.name}-skill.zip'
            zip_skill(sk, z)
            digest = sha256(z)
            entries.append({'order': i, 'skill': sk.name,
                            'archive': z.name, 'sha256': digest,
                            'bytes': z.stat().st_size})
            rel = z.relative_to(ROOT).as_posix()
            root_lines.append(f'{digest}  {rel}')

        MAN.mkdir(parents=True, exist_ok=True)
        (MAN / f'{slug}-CHECKSUMS.txt').write_text(
            ''.join(f'{e["sha256"]}  dist/packages/{slug}/{e["archive"]}\n' for e in entries),
            encoding='utf-8', newline='')
        (MAN / f'{slug}-v{ver}.json').write_text(json.dumps(
            {'suite': slug, 'title': SUITE_TITLES.get(slug, slug), 'version': f'v{ver}',
             'date': a.date, 'skill_count': len(entries), 'artifacts': entries},
            indent=2) + '\n', encoding='utf-8', newline='')

        write_notes(slug, ver, a.date, entries)
        summary.append((slug, len(entries), sum(e['bytes'] for e in entries)))

    (ROOT / 'CHECKSUMS.txt').write_text('\n'.join(sorted(root_lines)) + '\n',
                                        encoding='utf-8', newline='')
    write_manifest(ver, a.date, suites)

    print(f'release v{ver}  ({a.date})')
    total = 0
    for slug, n, b in summary:
        print(f'  {slug:<32} {n:>3} skills  {b/1024:>8.0f} KB')
        total += n
    print(f'  {"TOTAL":<32} {total:>3} skills')
    print(f'  root CHECKSUMS.txt: {len(root_lines)} entries')
    return 0


def write_notes(slug: str, ver: str, date: str, entries: list[dict]) -> None:
    title = SUITE_TITLES.get(slug, slug)
    REL.mkdir(exist_ok=True)
    p = REL / f'{slug}-v{ver}.md'
    lines = [
        f'# {title} v{ver}', '',
        'Status: published', f'Date: {date}', '',
        '## Summary', '',
        f'{title} rebuilt on the `frontier-2026-07` capability profile. Every skill in this',
        'suite is generated from a single source cascade and carries the same capability',
        'baseline, so the assumptions it makes about the executing model are explicit and',
        'versioned rather than implied.', '',
        'This release is vendor-neutral by construction. The packaged artifacts here name no',
        'model vendor; per-vendor builds are generated from the same source under',
        '`dist/vendor/<vendor>/`.', '',
        '## What changed', '',
        '- Scaffolding written for weaker models replaced with outcome, constraints, and an',
        '  acceptance bar. Ordering kept only where it is externally mandated and getting it',
        '  wrong is unsafe.',
        '- Halt conditions retargeted from uncertainty to six consequence classes. Absent',
        '  evidence is a soft gap; unreachable evidence is a hard halt.',
        '- Token conservation replaced by handoff density. At current context sizes the',
        '  constraint is ambiguity, not volume.',
        '- Stages operating over independent items declare a parallel surface.',
        '- Output contracts state the artifact set a complete run delivers rather than a menu.',
        '  This never licenses inventing an artifact that has no source basis.', '',
        '## Governance', '',
        'Governance invariants were held fixed: never invent facts, separate fact from',
        'assumption, preserve source hierarchy and conflicts, respect approval and',
        'destructive-action gates. A more capable model is a reason to remove scaffolding,',
        'never a reason to remove governance.', '',
        f'## Included skills ({len(entries)})', '',
    ]
    lines += [f'- `{e["skill"]}`' for e in entries]
    lines += ['', '## Breaking changes', '',
              'Compatibility shims ship for one release cycle and are removed in v1.1.0.', '',
              '| Was | Now | Shim |', '|---|---|---|',
              '| `references/codex-conservation-policy.md` | `references/handoff-density-policy.md` | yes |',
              '| `references/low-token-policy.md` | `references/handoff-density-policy.md` | yes |',
              '| `references/*-low-token-policy.md` | `references/*-handoff-density-policy.md` | yes |',
              '| `agents/openai.yaml` | `agents/<vendor>.yaml` | yes |',
              '| `continuity_packet.codex_handoff` | `continuity_packet.implementation_handoff` | no, rename in place |',
              '| `max_context_policy: execution_packet_only` | `context_policy: relevance_density` | no, rename in place |',
              '', '## Artifacts', '',
              f'- Packaged skills: `dist/packages/{slug}/`',
              f'- Checksums: `dist/manifests/{slug}-CHECKSUMS.txt`',
              f'- JSON manifest: `dist/manifests/{slug}-v{ver}.json`',
              '- Root checksums: `CHECKSUMS.txt`', '',
              '## Verify', '', '```bash',
              'python3 tools/audit_skills.py',
              'python3 tools/validate_release_assets.py', '```', '',
              'Archives are deterministic: the same source produces byte-identical zips, so a',
              'checksum mismatch means the content actually changed.', '']
    p.write_text('\n'.join(lines), encoding='utf-8', newline='')


def write_manifest(ver: str, date: str, suites: list[str]) -> None:
    """Generate MANIFEST.md from actual dist state so it cannot drift from reality."""
    rows, sections = [], []
    for slug in suites:
        skills = sorted(d.name for d in (DIST / slug).iterdir() if d.is_dir())
        skills.sort(key=lambda n: (n != slug, n))
        title = SUITE_TITLES.get(slug, slug)
        rows.append(f'| {title} | v{ver} | {len(skills)} | `skills/{title}/` | '
                    f'`dist/packages/{slug}/` | `{slug}-v{ver}` |')
        body = [f'### {title} v{ver}', '',
                f'{len(skills)} skills. Built from `profiles/frontier-2026-07.yaml`.', '',
                '| Order | Skill | Archive |', '|---:|---|---|']
        body += [f'| {i:03d} | `{n}` | `{i:03d}-{n}-skill.zip` |' for i, n in enumerate(skills)]
        sections.append('\n'.join(body))

    out = ['# Skills-Lab Manifest', '',
           'Generated by `tools/cut_release.py`. Do not edit by hand.', '',
           '## Repository identity', '',
           '- Repository: https://github.com/MadewellRD/skills-lab',
           '- Audience: vibe coders, solo builders, and AI-native engineering teams',
           '- Purpose: reduce workflow ambiguity so coding agents spend tokens on code, tests,',
           '  and validation instead of rediscovering process.',
           f'- Capability profile: `frontier-2026-07`',
           '- Vendor targets: generic (default), anthropic, openai, google', '',
           '## Suite registry', '',
           '| Suite | Version | Skills | Source | Packages | Release tag |',
           '|---|---|---:|---|---|---|'] + rows + ['',
           '## Package naming', '', '```text',
           '000-<suite-slug>-skill.zip        suite orchestrator, always order 000',
           '001-<desk-slug>-skill.zip         member desks, alphabetical', '```', '',
           'Archives are deterministic: fixed timestamps and sorted entries, so identical',
           'source produces identical checksums.', '',
           '## Deprecated', '',
           '- `skills/Sales Revenue Command Desk/` is a byte-identical duplicate of Sales',
           '  Command Desk. Marked with `DEPRECATED.yaml`, excluded from the build, source',
           '  preserved.', '',
           '## Suite inventory', '']
    for sec in sections:
        out += sec.split('\n') + ['']
    (ROOT / 'MANIFEST.md').write_text('\n'.join(out) + '\n',
                                      encoding='utf-8', newline='')


sys.exit(main())
