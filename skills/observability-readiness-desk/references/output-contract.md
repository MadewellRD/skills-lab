# Output Contract

## Artifact types

Choose the smallest artifact that satisfies the request:

- `observability-readiness-report.md`
- `telemetry-design-plan.md`
- `runbook-readiness-check.md`
- `slo-alerting-plan.md`
- `deployment-monitoring-checkpoints.md`
- `observability-gap-report.md`
- `connector-diagnostic.md`

## Required sections

Every artifact must include:

- Scope
- Source facts used
- Findings or proposed design
- Risks and gaps
- Validation or follow-up checks
- Downstream handoff notes

## Evidence handling

Use citations when connector/file citations are available. If citations are not available, list source names and mark assumptions as unverified.

## Downloadable files

When creating a file for the user, wrap the artifact with:

```markdown
# [artifact title]

## How to use this file

Use this as the source of truth for observability readiness review, operational planning, or downstream implementation handoff.

## Artifact

[content]
```
