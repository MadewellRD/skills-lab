---
name: synthetic-data-desk
description: design synthetic data generation workflows with seed examples, constraints, diversity targets, contamination controls, review loops, and validation gates.
---

# Synthetic Data Desk

## Role

Design synthetic data generation for AI development or evaluation. Specify seed examples, generation constraints, diversity targets, contamination controls, review loops, validation gates, and provenance.

## Use when

- A dataset needs controlled expansion or edge-case coverage.
- Real data is unavailable, sensitive, sparse, or expensive to label.
- Eval or training data needs diversity while preserving constraints.

## Do not use when

- Synthetic examples would replace required real-world validation.
- Seed data contains sensitive content that cannot be transformed safely.
- The generation process could contaminate benchmark or held-out eval sets.

## Required evidence

- Generation objective, target distribution, seed examples, and exclusion rules.
- Sensitive data constraints and contamination boundaries.
- Review protocol, validation checks, and provenance tracking.
- Intended use for training, eval, red-team, or documentation.

## Workflow

Produce a generation plan that states what will be generated, from what seeds, under what constraints, how it is reviewed and filtered, and what it may and may not be used for afterward.

Constraints:

- Contamination controls and sensitive-data handling are settled before any generation runs. Contamination of a benchmark or held-out split is irreversible, and a control added afterward does not undo it.
- Seed provenance and usage limits travel with every generated record. Synthetic provenance is never recorded as real provenance.
- Diversity targets are stated as measurable distribution properties, not as adjectives.
- Synthetic data supplements real-world validation and never substitutes for it. State explicitly which claims it can and cannot support.
- Label unresolved assumptions inline rather than presenting them as settled facts.

Generation batches are independent. Producing, filtering, and reviewing each batch, seed cluster, or scenario category is parallel-safe. Deduplication against seeds and against held-out splits, and the final distribution check against diversity targets, are global operations over the combined output.

## Outputs

- synthetic data plan
- generation constraints
- review workflow
- contamination controls
- validation checklist

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- generation_goal
- seed_policy
- diversity_targets
- contamination_controls
- review_gates
- usage_limits

## Halt conditions

Default posture is to proceed and label the assumption inline. An undecided batch size or an unset generation temperature is a soft gap: state the assumption, mark it, and continue. Halt only when one of the six hard-halt classes applies.

- Approval — generated data would be used for a purpose, or derived from seeds, beyond what the data owner authorized.
- Production or destructive — generated records would be merged into a dataset or split that existing eval baselines depend on, without a reversible path.
- Security or privacy — sensitive, regulated, or personal content in the seeds could survive into generated output, or generation would send that content to an uncleared surface.
- Source conflict — seed provenance, consent scope, or usage limits are documented inconsistently.
- Release integrity — synthetic data would stand as release evidence for a claim that requires real-world validation, or contamination controls are absent for eval or benchmark use.
- Connector unreachable — seed data, provenance records, or existing split definitions exist but cannot be read.

## Downstream handoffs

- dataset-curation-desk
- eval-design-desk
- red-team-eval-desk
- ai-safety-review-desk

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
- Passing means the generation objective, seed policy, measurable diversity targets, contamination controls, review gates, and usage limits are all stated, and every generated record can be traced to its seed and its permitted use.
