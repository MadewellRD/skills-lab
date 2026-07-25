# Observability Readiness Report Template

## Executive summary

State whether the system is ready, partially ready, or not ready from an observability standpoint.

## Scope

- Service/system:
- Environment:
- Release/deployment context:
- User-visible behaviors:

## Source facts

List repo files, docs, dashboards, alerts, incidents, CI checks, and user instructions used.

## Current observability surface

### Logs

What is logged, where it is emitted, and whether logs are structured and searchable.

### Metrics

Service, business, latency, error, saturation, queue, dependency, and resource metrics.

### Traces

Request path, background jobs, dependencies, async flows, and correlation IDs.

### Dashboards

Dashboards, owners, scope, and environment coverage.

### Alerts

Alert rules, severity, routing, thresholds, and runbook links.

## Gaps and risks

Use severity: blocker, high, medium, low.

| Severity | Gap | Evidence | Impact | Recommended action |
|---|---|---|---|---|

## Readiness decision

Use one of: ready, ready with caveats, not ready, unknown pending evidence.

## Downstream handoff

Identify whether follow-up belongs to `implementation-handoff-desk`, `deployment-desk`, `release-operations-desk`, or `incident-response-desk`.
