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

- Define generation scope and constraints.
- Specify seed handling and diversity targets.
- Design review, filtering, and validation gates.
- Prevent contamination and sensitive data leakage.
- Record provenance and usage limits.

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

- Sensitive examples could leak into generated data.
- Synthetic data would be used as proof without real validation.
- Contamination controls are missing for eval or benchmark use.

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
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
