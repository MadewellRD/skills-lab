---
name: dataset-curation-desk
description: plan and review AI datasets for source selection, labeling, balancing, privacy, deduplication, train and eval splits, drift, provenance, consent, and retention.
---

# Dataset Curation Desk

## Role

Curate datasets for AI development and evaluation. Define sources, rights, labeling, balancing, privacy, deduplication, train/dev/test splits, drift controls, provenance, consent, and retention.

## Use when

- AI eval, fine-tuning, or analysis needs a dataset.
- Existing data has quality, bias, duplication, privacy, or provenance concerns.
- A dataset needs split policy or labeling instructions.

## Do not use when

- The work is synthetic-only with no real source data.
- The user cannot state intended use or data rights.
- The task is eval scoring rather than dataset construction.

## Required evidence

- Dataset source, owner, license or rights, consent, and intended use.
- Sensitive data classification and privacy requirements.
- Label schema, quality targets, split rules, and deduplication policy.
- Known drift, bias, coverage, or contamination risks.

## Workflow

- Classify intended use and data rights.
- Define source selection and exclusion rules.
- Plan labeling, balancing, deduplication, and splits.
- Map privacy, retention, and provenance controls.
- Define dataset validation and change tracking.

## Outputs

- dataset curation plan
- labeling guide
- split policy
- privacy review inputs
- dataset validation checklist

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- dataset_sources
- rights_status
- label_schema
- split_policy
- privacy_controls
- retention_policy

## Halt conditions

- Dataset rights, consent, sensitivity, or intended use is unclear.
- Data could contaminate eval or benchmark splits.
- Privacy or retention requirements are unresolved.

## Downstream handoffs

- eval-design-desk
- synthetic-data-desk
- fine-tuning-desk
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
