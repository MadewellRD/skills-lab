# Observability Quality Checklist

Use this checklist before emitting an observability design or implementation handoff.

## Runtime coverage

- Runtime path and owner are explicit.
- Model calls, prompt versions, tool calls, retrieval events, memory/state transitions, approvals, and errors are mapped.
- Trace/span boundaries are concrete enough for implementation.

## Metrics and alerts

- Latency, token usage, model-call counts, tool-call counts, retrieval counts, cache behavior, cost, error rate, and safety-signal metrics are defined when relevant.
- Alert thresholds have baselines or are marked provisional with calibration requirements.
- Dashboard ownership and escalation path are explicit.

## Privacy and governance

- Prompt, completion, user content, tool argument, tool result, retrieval snippet, and memory capture rules are explicit.
- Redaction, access controls, retention, and purpose limits are defined.
- Cross-tenant and sensitive-data risks are handled or listed as hard halts.

## Handoff readiness

- Exact files/configs/instrumentation points are named when implementation is requested.
- Validation commands or inspection steps are included.
- Allowed files, forbidden files, PR title/body, and stop line are explicit for coding-agent work.
