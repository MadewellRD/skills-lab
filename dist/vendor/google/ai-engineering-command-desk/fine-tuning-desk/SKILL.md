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

This order is mandated. Cheaper alternatives are ruled out before training is justified, data readiness is settled before an objective is committed to, and eval, safety, and rollback gates exist before any rollout is planned. A rollout planned ahead of its gates cannot be safely reversed.

1. Compare fine-tuning against prompting, retrieval, tools, and routing, using cited baseline failure evidence.
2. Establish training data readiness and the training objective.
3. Define eval, safety, and release gates.
4. Plan rollout, fallback, rollback triggers, and monitoring.
5. Document the decision and unresolved risks.

Within step 1 the alternatives are independent: assessing prompting, retrieval, tooling, and routing against the same baseline failures is parallel-safe. Within step 2, per-source data readiness assessment is parallel-safe across sources. Steps 3 through 5 depend on the step 1 decision and do not run alongside it.

## Outputs

The decision comes first, and it determines which set the run delivers. Every run produces:

- fine-tuning decision memo: the failure the tune is meant to fix, the cheaper alternatives assessed against it (prompting, retrieval, tooling, routing), the recommendation, and the exclusion reason for each rejected option.

When the recommendation is to fine-tune, the remaining four ship with it in the same run rather than in later turns:

- training data readiness report: per source: volume, rights status, quality, contamination against eval sets, and what blocks use.
- eval gate plan: the pre-tune baseline, the slices that must improve, and the regression slices that must not degrade, each with a numeric threshold.
- rollout and rollback plan: exposure sequence, the comparison against the base model in production, the rollback trigger, and the artifact rolled back to.
- monitoring requirements: the signals that would show the tuned model degrading, and their owners.

When the recommendation is *not* to fine-tune, those four are genuinely not applicable. The memo plus the recommended alternative path is then the complete run, and each omitted artifact is named with the decision that made it unnecessary, not produced for symmetry.

Depth bar for whichever set applies: a practitioner could begin the work from it without a follow-up round trip.

No part of this is filled in from expectation. Base-model performance, training-set size, tuning cost, and provider tuning limits are cited or recorded as unknown. A projected improvement with no measured baseline behind it is not a gate, and presenting one as a gate puts an untested model on a rollout path.

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

Default posture is to proceed and label the assumption inline. An unconfirmed training cost estimate or an undecided checkpoint cadence is a soft gap: state the assumption, mark it, and continue. Halt only when one of the six hard-halt classes applies.

- Approval: training spend, data use, or model publication would exceed what the owner has authorized.
- Production or destructive: a rollout would replace a serving model without a tested rollback path, or training would consume or overwrite data another system depends on.
- Security or privacy: training data rights, consent, or sensitivity are unresolved, or personal or regulated data would be memorized into model weights.
- Source conflict: baseline evidence, failure analysis, and stakeholder expectations disagree on whether the current approach actually fails.
- Release integrity: no baseline or eval evidence establishes that fine-tuning is warranted, or safety and rollback gates are missing for a model intended to ship.
- Connector unreachable: baseline evals, failure analyses, or training data exist but cannot be read.

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
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means the decision states why fine-tuning beats prompting, retrieval, tooling, and routing against cited baseline evidence; training data carries a rights and quality status; eval, safety, and release gates are numeric; and the rollout plan names its fallback, rollback trigger, and monitoring.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
