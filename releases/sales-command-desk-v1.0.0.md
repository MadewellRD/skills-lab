# Sales Command Desk v1.0.0

Status: published
Date: 2026-07-25

## Summary

Sales Command Desk rebuilt on the `frontier-2026-07` capability profile. Every skill in this
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

## Included skills (13)

- `sales-command-desk`
- `account-discovery-desk`
- `crm-update-desk`
- `customer-handoff-desk`
- `deal-review-desk`
- `lead-research-desk`
- `objection-handling-desk`
- `outbound-sequence-desk`
- `pipeline-forecast-desk`
- `proposal-desk`
- `qualification-desk`
- `renewal-expansion-desk`
- `sales-call-prep-desk`

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

- Packaged skills: `dist/packages/sales-command-desk/`
- Checksums: `dist/manifests/sales-command-desk-CHECKSUMS.txt`
- JSON manifest: `dist/manifests/sales-command-desk-v1.0.0.json`
- Root checksums: `CHECKSUMS.txt`

## Verify

```bash
python3 tools/audit_skills.py
python3 tools/validate_release_assets.py
```

Archives are deterministic: the same source produces byte-identical zips, so a
checksum mismatch means the content actually changed.
