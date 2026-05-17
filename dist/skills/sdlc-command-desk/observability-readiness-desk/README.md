# Observability Readiness Desk

`observability-readiness-desk` creates connector-grounded observability and operations-readiness artifacts for SDLC delivery.

## Lifecycle coverage

Primary stage: observability, telemetry, and operational readiness.

Adjacent stages: deployment, release operations, incident response, verification, maintenance, and production support.

## Intended inputs

- Product requirements and acceptance criteria
- Architecture or deployment plans
- Source code and configuration files
- Logging, metrics, tracing, alerting, and dashboard references
- Incident reports, CI outputs, release notes, and runbooks
- User-provided operational constraints or SLO targets

## Intended outputs

- Observability readiness report
- Telemetry design plan
- Metrics, logs, traces, and dashboard gap analysis
- Alerting and SLO/SLA recommendations
- Runbook readiness checklist
- Deployment monitoring checkpoint plan
- Downstream handoff notes for PR, deployment, release, or incident workflows

## Required connectors

Use GitHub when repo code, instrumentation, configuration, deployment files, or CI evidence matters. Use document connectors for product, architecture, deployment, release, incident, and runbook context. Use monitoring/incident connectors when available for dashboard, alert, SLO, and production evidence.

## Composition

Use this skill before release or deployment to confirm the system is observable and operable. If an implementation change is required, hand off to `implementation-handoff-desk`. If the issue is active production impact, hand off to `incident-response-desk`.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
