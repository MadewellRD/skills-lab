---
name: cost-latency-optimization-desk
description: optimize ai system cost and latency using model routing, caching, prompt compression, context pruning, batching, streaming, parallelism, retrieval tuning, fallback tiers, and quality-preserving validation gates. use when chatgpt needs cost or latency baselines, optimization plans, rollout controls, low-token implementation handoffs, or tradeoff analysis for ai systems.
---

# Cost Latency Optimization Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to optimize AI system cost, latency, throughput, quotas, token usage, or runtime efficiency without weakening quality, safety, grounding, or reliability gates.

Prefer connector-grounded evidence over generic optimization advice. Use SignalDesk for local repo state, reports, and telemetry artifacts when available. Use GitHub for remote source truth, branches, pull requests, commits, changed files, checks, and implementation evidence. Use provider documentation only after repo facts, baselines, traffic assumptions, and user-scoped constraints are captured.

When implementation work is requested, do not emit broad instructions. Emit a compact optimization packet or implementation handoff with exact files, runtime levers, metrics, acceptance gates, validation commands, allowed and forbidden changes, rollback expectations, halt conditions, and downstream desk targets.

## Suite workflow mode

Operate as the AI Engineering specialist desk for cost and latency optimization. This desk usually follows `inference-ops-desk`, `agent-observability-desk`, or `eval-run-analysis-desk`, and can hand back to `model-selection-desk`, `prompt-systems-desk`, `retrieval-rag-design-desk`, or `ai-release-readiness-desk` depending on the optimization lever.

## Role

Optimize cost and latency without weakening quality or safety. Evaluate model routing, caching, prompt compression, context pruning, batching, streaming, parallelism, retrieval tuning, fallback tiers, quota handling, and runtime topology.

## Use when

- AI runtime cost, latency, throughput, quota use, or token budget is a concern.
- A release needs performance, cost, and reliability gates.
- A production system needs optimization after baseline measurement.
- A team needs a low-token handoff for performance work that preserves eval, safety, grounding, and rollback constraints.

## Do not use when

- No baseline metrics exist.
- Quality, safety, grounding, or regression gates are undefined.
- The request would reduce safeguards, hide required context, skip retrieval permissions, or remove human approval gates.
- The core problem is missing model capability, unsafe tooling, absent observability, or unclear production topology.

## Required evidence

- Baseline latency, cost, throughput, token, quota, cache, retry, timeout, and error metrics.
- Quality, safety, grounding, reliability, and eval thresholds that must be preserved.
- Model, prompt, retrieval, caching, batching, routing, fallback, and runtime architecture.
- Traffic profile, concurrency assumptions, provider limits, quota constraints, and user experience requirements.
- Current telemetry, dashboards, incidents, eval runs, release gates, and rollback criteria when available.

## Workflow

- Classify optimization objective, stage, and release risk.
- Collect or verify baseline metrics before proposing changes.
- Identify optimization levers and map their quality, safety, grounding, reliability, and observability risks.
- Separate quick wins from architecture changes.
- Estimate impact and required validation for each lever.
- Define safe rollout, rollback, monitoring, alerting, and regression checks.
- Produce a compact optimization packet or implementation handoff when the plan is execution-ready.

## Outputs

- optimization plan
- baseline metric summary
- tradeoff matrix
- validation gates
- rollout and rollback recommendations
- low-token implementation handoff

## Workflow packet fields

- capability_id or workflow_id
- workflow_mode
- current_stage
- user_goal and target outcome
- source_facts and evidence_links
- risk_tier and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- baseline_metrics
- traffic_profile
- provider_limits
- optimization_levers
- expected_impact
- quality_gates
- safety_gates
- grounding_gates
- cost_targets
- latency_targets
- throughput_targets
- cache_policy
- batching_policy
- routing_policy
- fallback_policy
- rollout_plan
- rollback_plan
- monitoring_requirements

## Validation gates

- Baseline metrics are captured before optimization recommendations are treated as release-ready.
- Quality, safety, grounding, and regression thresholds are explicit and preserved.
- Token, latency, cost, cache, quota, and error metrics have before/after comparison requirements.
- Any model routing, caching, prompt compression, context pruning, batching, or retrieval tuning change has a rollback path.
- Production changes define owner, rollout stage, monitoring, alert threshold, and incident response handoff.

## Halt conditions

- Baseline metrics or acceptance thresholds are missing.
- Optimization would reduce safety, grounding, eval coverage, authorization, privacy, or quality evidence.
- Provider constraints, quota behavior, traffic assumptions, or runtime topology are unverified.
- Observability is insufficient to measure whether optimization improved or degraded the system.
- Requested optimization conflicts with user-impact, safety, privacy, compliance, or release gates.

## Downstream handoffs

- `model-selection-desk` when cost or latency requires model choice, routing, or fallback changes.
- `prompt-systems-desk` when prompt/context length, message shape, or output contract affects token use or latency.
- `retrieval-rag-design-desk` when retrieval, chunking, ranking, citation, or grounding behavior affects latency/cost.
- `inference-ops-desk` when runtime topology, quotas, caching, retries, batching, streaming, or timeouts need operational design.
- `agent-observability-desk` when metrics, traces, dashboards, alerts, or privacy-safe telemetry are missing.
- `ai-release-readiness-desk` when optimization changes affect launch or go/no-go gates.
- `implementation-handoff-desk` as an external SDLC handoff when files, configs, tests, or docs are ready for code changes.

## Source hierarchy

- User-provided objective, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository, issue, eval, telemetry, incident, cost, quota, and release evidence are authoritative for implementation and production state.
- Provider documentation is used for model/API limits, pricing surfaces, rate-limit behavior, caching semantics, batching constraints, and supported fallback patterns.
- Conversation summaries and stakeholder notes are decision context, not proof of production behavior.

## Quality bar

- Preserve traceability from optimization recommendation to baseline evidence, expected impact, and validation gate.
- State uncertainty explicitly and halt when required metrics, provider constraints, or thresholds are missing.
- Prefer measurable gates over qualitative improvement claims.
- Avoid widening autonomy, data exposure, release scope, or hidden failure behavior without an explicit decision.
- Never optimize by silently removing safety, grounding, privacy, or approval controls.

## Low-token execution policy

- Produce compact optimization packets with exact baselines, target metrics, levers, validation gates, rollout stages, rollback conditions, and downstream handoff targets.
- Do not ask Codex or Claude Code to infer baselines, traffic assumptions, provider limits, quality thresholds, or rollback policy.
- When implementation is required, hand off exact file paths, config keys, validation commands, allowed files, forbidden files, PR title/body, and stop line.
- Collapse long research into source facts, decisions, assumptions, hard halts, soft gaps, and validation gates before implementation handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/cost-latency-optimization-packet-template.md`: compact handoff template for optimization work.
- `references/cost-latency-quality-checklist.md`: checklist for safe optimization planning and review.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when baseline metrics, optimization levers, quality/safety gates, rollout plan, rollback plan, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
