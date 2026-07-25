# Inference Ops Quality Checklist

Use this checklist before emitting an inference operations plan or implementation handoff.

## Runtime facts

- Deployment target is explicit.
- Expected traffic, concurrency, burst profile, and request size are captured.
- Latency, availability, and cost targets are explicit.
- Model/provider identifiers, versions, limits, quotas, and rate-limit behavior are verified or blocked.

## Reliability controls

- Retry policy includes retryable/non-retryable errors and max attempts.
- Timeout policy covers model, tool, retrieval, and end-to-end request limits.
- Fallback policy covers provider outage, model outage, quota exhaustion, and degraded quality.
- Caching/batching/streaming decisions preserve correctness and privacy constraints.

## Security and privacy

- Secret handling and environment boundaries are explicit.
- Logging, redaction, retention, and data residency are explicit.
- No sensitive prompt, completion, user data, or retrieved content is logged without an approved policy.

## Operations

- SLOs and alert thresholds are explicit.
- Runbook owner and escalation path are identified.
- Rollback and disablement paths are explicit.
- Observability and release-readiness handoffs are named.
