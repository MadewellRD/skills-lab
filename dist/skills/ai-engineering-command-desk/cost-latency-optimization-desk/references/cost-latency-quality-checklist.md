# Cost Latency Quality Checklist

## Required before optimization

- Baseline latency, token, cost, throughput, quota, and error metrics exist.
- Quality, safety, grounding, and regression thresholds are explicit.
- Provider limits, pricing surfaces, and quota behavior are verified.
- Traffic profile and user experience expectations are defined.
- Observability can measure before/after effects.

## Safe optimization levers

- Model routing and fallback tiers.
- Prompt and context compression.
- Context pruning with grounding preservation.
- Retrieval tuning, chunk/rank changes, and citation quality checks.
- Request batching, streaming, parallelism, caching, and timeout tuning.
- Runtime topology and quota management.

## Halt checks

- Do not optimize by removing safety, privacy, approval, or grounding controls.
- Do not claim improvement without before/after measurement.
- Do not release optimization changes without rollback and monitoring.
- Do not hide provider-rate-limit, cost, or latency uncertainty.
