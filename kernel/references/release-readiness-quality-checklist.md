# Release Readiness Quality Checklist

Use this checklist before emitting `go`, `go_with_warnings`, or a downstream release/deployment handoff.

## Evidence gates

- Requirements, release target, and owner are explicit.
- Eval thresholds and latest run status are explicit.
- Safety review and red-team status are explicit or intentionally not applicable.
- Inference operations, fallback, provider limits, and rollback path are explicit.
- Observability, dashboards, alerts, privacy/redaction, and incident ownership are explicit.
- Docs/support handoff and user-impact communication are explicit when applicable.

## Decision gates

- All blockers have owners or halt the launch.
- Accepted risks have explicit owner approval.
- Warnings are separated from blockers.
- Rollback triggers are measurable.
- The downstream release/deployment handoff has exact paths, commands, gates, and stop conditions.
