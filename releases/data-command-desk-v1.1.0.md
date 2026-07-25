# Data Command Desk v1.1.0

Status: published
Date: 2026-07-25

## Summary

Data Command Desk rebuilt on the `frontier-2026-07` capability profile. Every skill in this
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

## Governance

Governance invariants were held fixed: never invent facts, separate fact from
assumption, preserve source hierarchy and conflicts, respect approval and
destructive-action gates. A more capable model is a reason to remove scaffolding,
never a reason to remove governance.

## Included skills (20)

- `data-command-desk`
- `analytics-enablement-desk`
- `batch-orchestration-desk`
- `data-contract-desk`
- `data-governance-access-desk`
- `data-incident-response-desk`
- `data-migration-desk`
- `data-modeling-desk`
- `data-observability-desk`
- `data-platform-cost-desk`
- `data-product-definition-desk`
- `data-quality-desk`
- `data-retention-lifecycle-desk`
- `ingestion-pipeline-desk`
- `lineage-catalog-desk`
- `metric-semantic-layer-desk`
- `source-system-profiling-desk`
- `streaming-pipeline-desk`
- `transformation-layer-desk`
- `warehouse-lakehouse-architecture-desk`

## Breaking changes

Compatibility shims are retired by DATE, not by version number: they are
removed after 2026-11-01. A version can arrive the week after the one that
introduced them, which would leave forks no real window, so the commitment is
to the calendar instead.
Renamed files ship under their old names as pointers. Renamed schema keys cannot
be shimmed with a file, so the continuity kernel declares them as read aliases:
a pre-v1.0.0 packet still resolves, and the current name is always written back.

| Was | Now | Shim |
|---|---|---|
| `references/codex-conservation-policy.md` | `references/handoff-density-policy.md` | yes |
| `references/low-token-policy.md` | `references/handoff-density-policy.md` | yes |
| `references/*-low-token-policy.md` | `references/*-handoff-density-policy.md` | yes |
| `agents/openai.yaml` | `agents/<vendor>.yaml` | yes |
| `continuity_packet.codex_handoff` | `continuity_packet.implementation_handoff` | yes, read alias |
| `max_context_policy` | `context_policy` | yes, read alias |

## Artifacts

- Packaged skills: `dist/packages/data-command-desk/`
- Checksums: `dist/manifests/data-command-desk-CHECKSUMS.txt`
- JSON manifest: `dist/manifests/data-command-desk-v1.1.0.json`
- Root checksums: `CHECKSUMS.txt`

## Verify

```bash
python3 tools/audit_skills.py
python3 tools/validate_release_assets.py
```

Archives are deterministic: the same source produces byte-identical zips, so a
checksum mismatch means the content actually changed.
