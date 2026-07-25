# Agent Architecture Risk Checklist

Use this checklist before approving an agent architecture or issuing an implementation handoff.

## Agency ceiling

- Is the architecture type explicit: deterministic pipeline, assistant workflow, single-agent loop, planner/executor, or multi-agent workflow?
- Are allowed and forbidden actions explicit?
- Are autonomy limits, budget limits, timeout limits, and stop conditions explicit?
- Is a deterministic or lower-agency alternative considered?

## Tool and action safety

- Are tool schemas and permission boundaries explicit?
- Are destructive actions gated by confirmation and rollback policy?
- Are retries idempotent or otherwise safe?
- Are tenant, user, and resource boundaries enforced outside prompt text?

## State and memory

- Is state persistence explicit?
- Is memory retention explicit?
- Are privacy, redaction, and deletion expectations explicit?
- Is replay or audit behavior defined?

## Observability

- Are model calls, tool calls, state transitions, memory events, approval events, retries, halts, errors, token/cost usage, and latency observable?
- Are incident evidence and runbook expectations explicit?

## Validation

- Do eval scenarios cover happy path, unsafe action attempt, approval required, tool failure, timeout, retry exhaustion, memory boundary, and halt behavior?
- Is release blocked until high-risk scenarios pass?
