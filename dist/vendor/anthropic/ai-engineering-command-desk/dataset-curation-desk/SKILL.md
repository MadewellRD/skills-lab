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

Produce a curation plan a data engineer can execute without further interpretation: which sources are in, which are out and why, how records are labeled and split, and what privacy, provenance, and retention controls apply.

Constraints:

- Intended use and data rights are established before a source is treated as usable. A source with unresolved rights stays excluded and is recorded as excluded, not silently dropped.
- Eval and benchmark splits are contamination boundaries. State the deduplication and leakage controls that keep training data out of held-out sets.
- Never invent provenance, license terms, consent status, or owner names. Unknown provenance is recorded as unknown, never inferred from context.
- Label schema, quality target, and split rule are stated precisely enough to be applied mechanically.
- Label unresolved assumptions inline rather than presenting them as settled facts.

Sources and shards are independent. Per-source rights review, quality assessment, sensitivity classification, and duplicate profiling are parallel-safe across sources and across shards of one source. Split assignment and cross-source deduplication are global operations over the combined set and run once.

## Outputs

One run delivers the whole curation package:

- dataset curation plan — sources, volumes, inclusion and exclusion rules, rights status per source, and the assembly order.
- labeling guide — label schema, definitions, boundary cases, adjudication rule, and the agreement expectation. Complete when two labelers using it independently resolve the same edge case the same way.
- split policy — train, validation, and test construction, the leakage controls between them, and what keeps a held-out split held out.
- privacy review inputs — sensitive-field classification, retention, access, and the handling constraint per source.
- dataset validation checklist — the checks that must pass before the set is used, each with an explicit pass condition.

Per-source review is the parallel-safe unit; split assignment and cross-source deduplication stay a single global pass over the combined set.

Delivering all five is not license to assert facts about data nobody inspected. Rights status, license terms, PII presence, provenance, and record counts are reported from evidence or reported as unverified. A source marked cleared for training without a basis is a legal exposure wearing the shape of a completed field.

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

Default posture is to proceed and label the assumption inline. An unknown record count or an undecided balancing ratio is a soft gap: state the assumption, mark it, and continue. Halt only when one of the six hard-halt classes applies.

- Approval — a source would be used beyond the consent, license, or contractual scope its owner granted.
- Production or destructive — a curation step would overwrite, delete, or re-split a dataset that a shipped eval baseline depends on.
- Security or privacy — regulated, personal, or customer-confidential records would be included, exported, or sent for labeling without the controls that data class requires.
- Source conflict — license, consent, or provenance records disagree about whether a source may be used or for what purpose.
- Release integrity — a dataset would be used as release evidence while a contamination path between training data and held-out splits remains open.
- Connector unreachable — the source data, license records, or existing split definitions exist but cannot be read.

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
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means every source carries a rights status and an inclusion or exclusion reason, the split policy and contamination controls are stated, and every sensitive field carries a named privacy treatment.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
