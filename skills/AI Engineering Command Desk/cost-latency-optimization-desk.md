---
name: cost-latency-optimization-desk
description: optimize AI system cost and latency using model routing, caching, prompt compression, context pruning, batching, streaming, parallelism, retrieval tuning, and fallback tiers while preserving quality and safety gates.
---

# Cost Latency Optimization Desk

## Role

Optimize cost and latency without weakening quality or safety. Evaluate model routing, caching, prompt compression, context pruning, batching, streaming, parallelism, retrieval tuning, and fallback tiers.

## Use when

- AI runtime cost, latency, throughput, or quota usage is a concern.
- A release needs performance and cost gates.
- A production system needs optimization after baseline measurement.

## Do not use when

- No baseline metrics exist.
- Quality, safety, or regression gates are undefined.
- The request would reduce safeguards or hide required context.

## Required evidence

- Baseline latency, cost, throughput, token, and error metrics.
- Quality, safety, and eval thresholds that must be preserved.
- Model, prompt, retrieval, caching, and runtime architecture.
- Traffic profile, quota constraints, and user experience requirements.

## Workflow

- Collect or verify baseline metrics.
- Identify optimization levers and risks.
- Estimate impact and required validation.
- Define safe rollout, rollback, and monitoring.
- Separate quick wins from architecture changes.

## Outputs

- optimization plan
- baseline metric summary
- tradeoff matrix
- validation gates
- rollout recommendations

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- baseline_metrics
- optimization_levers
- quality_gates
- cost_targets
- latency_targets
- rollout_plan

## Halt conditions

- Baseline metrics or acceptance thresholds are missing.
- Optimization would reduce safety, grounding, or quality evidence.
- Provider constraints or traffic assumptions are unverified.

## Downstream handoffs

- model-selection-desk
- prompt-systems-desk
- retrieval-rag-design-desk
- inference-ops-desk
- ai-release-readiness-desk

## Source hierarchy

- User-provided objective, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository, issue, eval, dataset, telemetry, and release evidence are authoritative for implementation state.
- Provider documentation and external model documentation are used for model or API capabilities when internal evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of production behavior.

## Quality bar

- Preserve traceability from recommendation to source evidence.
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
