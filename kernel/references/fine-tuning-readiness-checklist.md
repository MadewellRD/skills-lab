# Fine-Tuning Readiness Checklist

## Decision gate

- Baseline failure evidence exists.
- Prompt, RAG, tool, model-selection, and routing alternatives were considered.
- Fine-tuning objective is narrower than general product behavior.
- Expected improvement is measurable.
- Non-goals are explicit.

## Data gate

- Data source, owner, rights, consent, and retention are explicit.
- Sensitive data classification and privacy controls are explicit.
- Label quality and split policy are explicit.
- Deduplication and contamination controls are explicit.
- Held-out eval and benchmark data are protected.

## Eval gate

- Baseline run is available.
- Thresholds and regression slices are explicit.
- Safety and privacy slices are explicit.
- Failure examples are preserved.
- Rerun criteria are defined.

## Release gate

- Model versioning and routing plan are explicit.
- Fallback and rollback behavior are explicit.
- Monitoring, cost, latency, and incident response expectations are explicit.
- Owner approval is explicit for release-bound work.
