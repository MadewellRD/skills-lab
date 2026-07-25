# Web Development Command Desk v1.1.0

Status: published
Date: 2026-07-25

## Summary

Web Development Command Desk rebuilt on the `frontier-2026-07` capability profile. Every skill in this
suite is generated from a single source cascade and carries the same capability
baseline, so the assumptions it makes about the executing model are explicit and
versioned rather than implied.

This release is vendor-neutral by construction. The packaged artifacts here name no
model vendor; per-vendor builds are generated from the same source under
`dist/vendor/<vendor>/`.

## What changed

- Scaffolding written for weaker models replaced with outcome, constraints, and an
  acceptance bar. Ordering kept only where it is externally mandated and getting it
  wrong is unsafe.
- Halt conditions retargeted from uncertainty to six consequence classes. Absent
  evidence is a soft gap; unreachable evidence is a hard halt.
- Token conservation replaced by handoff density. At current context sizes the
  constraint is ambiguity, not volume.
- Stages operating over independent items declare a parallel surface.
- Output contracts state the artifact set a complete run delivers rather than a menu.
  This never licenses inventing an artifact that has no source basis.

## Authoring standard

Authored using the most capable frontier model available at the time, run at its
highest reasoning effort, recorded per release in `authoring_standard` in
`profiles/frontier-2026-07.yaml`. Authoring happens once per release and execution
happens on every invocation, so the effort asymmetry is decisive: prose written at
a reduced tier looks correct and leaves the ambiguity in place, which is the defect
this repository exists to remove.

Effort is attested by the maintainer rather than self-reported by the authoring
run, because a session reporting its own effort tier is not evidence of it.

## Governance

Governance invariants were held fixed: never invent facts, separate fact from
assumption, preserve source hierarchy and conflicts, respect approval and
destructive-action gates. A more capable model is a reason to remove scaffolding,
never a reason to remove governance.

## Included skills (14)

- `web-development-command-desk`
- `accessibility-seo-desk`
- `backend-integration-desk`
- `cms-content-operations-desk`
- `frontend-engineering-desk`
- `information-architecture-desk`
- `site-product-requirements-desk`
- `ux-ui-design-system-desk`
- `web-maintenance-growth-desk`
- `web-observability-desk`
- `web-performance-desk`
- `web-release-deployment-desk`
- `web-security-secops-desk`
- `web-testing-qa-desk`

## Breaking changes

Compatibility shims are RETIRED as of v1.1.0. The pre-v1.0.0 names no longer
ship, so anything still reading them must move to the current names.

| Was | Now |
|---|---|
| `references/codex-conservation-policy.md` | `references/handoff-density-policy.md` |
| `references/low-token-policy.md` | `references/handoff-density-policy.md` |
| `references/*-low-token-policy.md` | `references/*-handoff-density-policy.md` |
| `agents/openai.yaml` | `agents/<vendor>.yaml` |
| `continuity_packet.codex_handoff` | `continuity_packet.implementation_handoff` |
| `max_context_policy` | `context_policy` |

## Artifacts

- Packaged skills: `dist/packages/web-development-command-desk/`
- Checksums: `dist/manifests/web-development-command-desk-CHECKSUMS.txt`
- JSON manifest: `dist/manifests/web-development-command-desk-v1.1.0.json`
- Root checksums: `CHECKSUMS.txt`

## Verify

```bash
python3 tools/audit_skills.py
python3 tools/validate_release_assets.py
```

Archives are deterministic: the same source produces byte-identical zips, so a
checksum mismatch means the content actually changed.
