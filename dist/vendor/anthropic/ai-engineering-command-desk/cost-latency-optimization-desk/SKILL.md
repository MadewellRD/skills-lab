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

This order is mandated. Optimization without a baseline cannot be shown to have helped, and a rollout planned before its validation and rollback path cannot be safely reversed when quality regresses.

1. Collect the baseline metrics, or confirm that an existing baseline is still current.
2. Identify optimization levers and the risk each carries to quality, grounding, and safety.
3. Estimate impact per lever and state the validation each one requires.
4. Define safe rollout, rollback triggers, and monitoring.
5. Separate quick wins from architecture changes.

Within steps 2 and 3 the levers are independent: assessing model routing, caching, prompt compression, context pruning, batching, streaming, parallelism, retrieval tuning, and fallback tiers is parallel-safe, each measured against the same baseline. Step 1 precedes all of them; steps 4 and 5 are aggregate over the selected set.

## Outputs

A full run delivers the complete optimization case, not a single recommendation:

- optimization plan — the selected levers with expected effect, the mechanism each acts on, and what each one costs elsewhere.
- baseline metric summary — current cost and latency along the dimensions that matter (route, model, stage, percentile), each figure attributed to its measurement source.
- tradeoff matrix — every lever considered, including the rejected ones and the reason for rejection, scored against the same baseline.
- validation gates — the quality and safety thresholds that must still hold after the change, stated numerically.
- rollout recommendations — sequencing, traffic exposure, the monitoring signal per lever, and the rollback trigger.

Depth bar: an engineer should be able to implement and gate the first lever without returning for detail. A lever with an expected effect but no measurement method is unfinished. Levers are the parallel-safe unit, each measured against the same baseline.

Numbers carry the whole argument here, so none may be manufactured. Where a baseline cost, token count, latency percentile, or provider price cannot be read from telemetry, billing, or provider documentation, it is recorded as unmeasured and the dependent estimate is marked blocked on it. A confident projected saving resting on an invented baseline is worse than reporting that the baseline is missing.

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

Default posture is to proceed and label the assumption inline. An unconfirmed traffic mix or an estimated cache hit rate is a soft gap, provided it is marked as an estimate and the measurement that would confirm it is named. Halt only when one of the six hard-halt classes applies.

- Approval — the change would move spend tier, provider commitment, or user-visible behavior beyond what the owner has authorized.
- Production or destructive — the optimization would change live routing, caching, or runtime topology without a rollback trigger.
- Security or privacy — context pruning, caching, or logging would retain or expose personal, regulated, or cross-tenant data, or would weaken an existing redaction boundary.
- Source conflict — telemetry, provider billing, and internal cost models disagree on where the cost or latency actually is.
- Release integrity — the optimization would ship without evidence that quality, grounding, and safety thresholds still hold, or no baseline exists against which improvement could be established.
- Connector unreachable — baseline telemetry, cost data, or runtime configuration exists but cannot be read.

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
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means the baseline is stated with its measurement window, every proposed lever carries an estimated impact and the validation that confirms it, quality and safety thresholds are restated as preserved, and the rollout plan names its rollback trigger and monitoring.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
