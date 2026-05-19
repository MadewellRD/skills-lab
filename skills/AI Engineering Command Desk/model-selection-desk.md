---
name: model-selection-desk
description: select model candidates, routing constraints, fallback behavior, and model tradeoffs for AI capabilities using task fit, quality, latency, cost, safety, modality, context, and deployment evidence.
---

# Model Selection Desk

## Role

Choose and justify model candidates for an AI capability. Compare task fit, quality target, latency, cost, context window, modality, tool support, safety profile, provider constraints, data residency, and fallback posture.

## Use when

- A capability needs a model or model family decision.
- A system needs routing tiers or fallback model behavior.
- A current model is too slow, expensive, unsafe, or low quality.

## Do not use when

- The issue is primarily prompt wording, retrieval design, or tooling behavior.
- No task objective or quality target exists.
- The user wants a model picked by popularity without tradeoff evidence.

## Required evidence

- Task type, expected inputs and outputs, modalities, context size, and quality bar.
- Latency, throughput, cost, privacy, compliance, and deployment constraints.
- Existing evals or benchmark slices relevant to the capability.
- Provider or platform constraints for tool use, streaming, rate limits, and data handling.

## Workflow

- Frame the model decision and constraints.
- List candidate models and exclusion reasons.
- Map candidates to task slices and eval expectations.
- Define routing, fallback, and rollback posture.
- Document unresolved assumptions and required tests.

## Outputs

- model comparison matrix
- recommended model set
- routing policy
- fallback plan
- eval requirements

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- candidate_models
- model_constraints
- routing_policy
- fallback_policy
- evaluation_needed

## Halt conditions

- Task requirements, safety tier, budget, latency target, or deployment environment is missing.
- Required provider or model capability facts cannot be verified.
- No eval or acceptance threshold exists for a high-impact model choice.

## Downstream handoffs

- prompt-systems-desk
- eval-design-desk
- inference-ops-desk
- cost-latency-optimization-desk
- ai-safety-review-desk

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

## Low-token execution policy

- Produce a compact model decision packet that includes task class, candidates, exclusion reasons, routing rules, fallback model, eval requirement, and unresolved assumptions.
- Do not ask Codex or Claude Code to infer provider constraints, cost class, latency target, safety tier, or acceptance thresholds; require those facts or return `Workflow Halt`.
- When implementation is required, hand off exact model identifiers, configuration names, allowed provider surfaces, environment constraints, validation commands, and rollback expectations.

## Continuity Kernel Adoption

- Read and update `references/suite-workflow-contract.md` before advancing to another AI Engineering desk.
- Set `ready_to_continue: true` only when the selected model path, fallback policy, required evals, and remaining risks are explicit enough for the next desk.
- Preserve `source_facts`, `decisions`, `assumptions`, `open_questions`, `validation_gates`, and `downstream_handoff_targets` in the workflow packet.
