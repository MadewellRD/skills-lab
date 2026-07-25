# Observability Readiness Checklist

Use this checklist before go/no-go recommendations.

## Required checks

- Target service and environment are identified.
- Critical user journeys are listed.
- Logs include structured events for success, failure, and degraded paths.
- Metrics cover rate, errors, duration, and saturation.
- Traces or correlation IDs connect user requests to downstream dependencies.
- Dashboards exist or gaps are documented.
- Alerts map to user impact and known failure modes.
- Alerts have routing and runbook references.
- SLOs or monitoring thresholds are defined or explicitly out of scope.
- Deployment monitoring checkpoints are defined.
- Rollback or mitigation signals are identified.
- Privacy and sensitive-data constraints are respected.

## Decision labels

- ready: required checks are satisfied with evidence.
- ready with caveats: non-blocking gaps are documented with owners.
- not ready: one or more blocker gaps remain.
- unknown pending evidence: required connectors or source facts are missing.
