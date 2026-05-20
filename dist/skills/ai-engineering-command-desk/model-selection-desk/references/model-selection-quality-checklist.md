# Model Selection Quality Checklist

## Required checks

- Task class, input/output modalities, and behavior contract are explicit.
- Quality target and acceptance threshold are explicit.
- Latency, throughput, cost, privacy, and deployment constraints are explicit.
- Candidate models are compared against task slices, not only generic benchmark scores.
- Exclusion reasons are recorded for rejected candidates.
- Routing, fallback, rollback, and provider outage behavior are defined.
- Eval requirements are named before release or implementation handoff.
- Safety tier and high-impact risk handling are explicit.
- `Workflow Halt` is returned if required model/provider facts cannot be verified.

## Low-token handoff check

A downstream coding agent should not need to infer model IDs, provider surfaces, config keys, routing rules, fallback behavior, eval thresholds, or rollback expectations.
