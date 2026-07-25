# Connector Routing

## GitHub

Use GitHub when the request depends on code or repository state.

Retrieve when relevant:

- service/module ownership and changed files
- logging, metrics, tracing, health check, and error handling code
- deployment manifests and environment config
- CI checks, release branches, and recent observability-related PRs
- README, runbook, and operational docs stored in the repo

Halt if the user asks for code-backed observability readiness and the repo or target service is unknown.

## Documentation sources

Use docs sources for product behavior, architecture, deployment, release, incident, and operations policy.

Retrieve when relevant:

- SLO/SLA commitments
- architecture diagrams and service dependencies
- deployment and rollback procedures
- incident postmortems and runbooks
- customer-impact or regulatory monitoring requirements

If docs conflict with repo state, preserve the conflict and identify what must be resolved before go/no-go.

## Monitoring and incident sources

Use monitoring, observability, or incident connectors when available for production evidence.

Retrieve when relevant:

- dashboard names and links
- alert rules and notification routes
- SLO burn-rate or error-budget evidence
- recent incidents and symptoms
- log, metric, and trace coverage for the target service

Do not invent dashboard or alert names when these connectors are unavailable.

## User-provided context

Use pasted context for intent and constraints. Treat it as lower authority than live repo or monitoring facts for operational claims unless the user explicitly states it is authoritative.
