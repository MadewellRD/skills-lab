# Product Command Desk v1.0.0

Status: published
Date: 2026-07-25

## Summary

Product Command Desk rebuilt on the `frontier-2026-07` capability profile. Every skill in this
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

## Included skills (16)

- `product-command-desk`
- `churn-retention-analysis-desk`
- `competitive-analysis-desk`
- `experiment-design-desk`
- `feature-prioritization-desk`
- `feedback-synthesis-desk`
- `gtm-brief-desk`
- `launch-readiness-desk`
- `market-discovery-desk`
- `opportunity-sizing-desk`
- `persona-segmentation-desk`
- `prd-desk`
- `pricing-packaging-desk`
- `product-retrospective-desk`
- `roadmap-planning-desk`
- `user-research-desk`

## Breaking changes

Compatibility shims ship for one release cycle and are removed in v1.1.0.

| Was | Now | Shim |
|---|---|---|
| `references/codex-conservation-policy.md` | `references/handoff-density-policy.md` | yes |
| `references/low-token-policy.md` | `references/handoff-density-policy.md` | yes |
| `references/*-low-token-policy.md` | `references/*-handoff-density-policy.md` | yes |
| `agents/openai.yaml` | `agents/<vendor>.yaml` | yes |
| `continuity_packet.codex_handoff` | `continuity_packet.implementation_handoff` | no, rename in place |
| `max_context_policy: execution_packet_only` | `context_policy: relevance_density` | no, rename in place |

## Artifacts

- Packaged skills: `dist/packages/product-command-desk/`
- Checksums: `dist/manifests/product-command-desk-CHECKSUMS.txt`
- JSON manifest: `dist/manifests/product-command-desk-v1.0.0.json`
- Root checksums: `CHECKSUMS.txt`

## Verify

```bash
python3 tools/audit_skills.py
python3 tools/validate_release_assets.py
```

Archives are deterministic: the same source produces byte-identical zips, so a
checksum mismatch means the content actually changed.
