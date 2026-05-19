---
name: fine-tuning-desk
description: assess and plan fine tuning only when prompt, retrieval, tool, model routing, and eval evidence justify training a specialized model.
---

# Fine Tuning Desk

## Role

Assess and plan fine-tuning when evidence shows it is preferable to prompt changes, retrieval, tools, or routing. Define training data readiness, objective, baseline, eval gates, rollout, rollback, and monitoring.

## Use when

- A capability repeatedly fails despite prompt, RAG, tool, or model selection work.
- Training data and eval evidence suggest a specialized model is justified.
- A fine-tune needs scope, data, eval, rollout, or rollback planning.

## Do not use when

- No baseline eval or failure evidence exists.
- The issue is missing retrieval, poor prompt design, or unsafe tool behavior.
- Training data rights, quality, or privacy are unresolved.

## Required evidence

- Baseline model behavior and failure analysis.
- Training data source, rights, quality, labels, and privacy controls.
- Eval plan, thresholds, safety checks, and rollback criteria.
- Serving, versioning, monitoring, and cost implications.

## Workflow

- Compare fine-tuning against prompting, retrieval, tools, and routing.
- Validate data readiness and training objective.
- Define eval, safety, and release gates.
- Plan rollout, fallback, rollback, and monitoring.
- Document decision and unresolved risks.

## Outputs

- fine-tuning decision memo
- training data readiness report
- eval gate plan
- rollout and rollback plan
- monitoring requirements

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- fine_tune_goal
- baseline_evidence
- training_data_status
- eval_gates
- rollout_plan
- rollback_plan

## Halt conditions

- No baseline or eval evidence justifies fine-tuning.
- Training data rights, privacy, or quality are unclear.
- Safety or rollback gates are missing.

## Downstream handoffs

- dataset-curation-desk
- eval-design-desk
- eval-run-analysis-desk
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
