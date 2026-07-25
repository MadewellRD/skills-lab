---
name: eval-run-analysis-desk
description: analyze completed AI eval runs, regression deltas, failure clusters, grading reliability, threshold status, release blockers, and rerun recommendations.
---

# Eval Run Analysis Desk

## Role

Analyze completed eval evidence. Identify pass/fail status, regression deltas, failure clusters, grader reliability, threshold misses, release blockers, and required reruns.

## Use when

- Eval results need interpretation.
- A model, prompt, tool, RAG, or agent change may have regressed behavior.
- A release decision depends on eval evidence.

## Do not use when

- No raw eval results are available.
- The scoring criteria or thresholds are undefined.
- The task is to design a new eval rather than analyze a run.

## Required evidence

- Raw eval results, run metadata, model and prompt versions, and dataset slice IDs.
- Rubric, grading method, threshold definitions, and baseline runs.
- Failure examples, reviewer notes, and known production incidents.

## Workflow

Produce a decision about the run: whether it is trustworthy, how it moved against baseline and thresholds, what the failures have in common, and what that means for the release gate.

Constraints:

- Establish the run's own trustworthiness before drawing conclusions from it — completeness, scoring consistency, and grader reliability. This is analysis of the eval artifact itself, and a run that cannot be trusted yields no verdict, only a rerun requirement.
- Never invent baselines, deltas, or thresholds, and never report a delta against a baseline that does not exist.
- Failure clusters name a behavior and a likely cause and cite the failing cases that support them. An unsupported cluster is a hypothesis and is labeled as one.
- Blocker, warning, and pass status are assigned against pre-existing thresholds, never against thresholds inferred from the results.
- Preserve disagreement between graders or between runs rather than averaging it away.
- Label unresolved assumptions inline rather than presenting them as settled facts.

Cases and slices are independent. Per-case scoring review, per-slice baseline comparison, and per-cluster cause analysis are parallel-safe. Grader-reliability assessment across the run, the release-gate verdict, and the rerun decision are aggregate judgments over the complete result set.

## Outputs

- eval analysis report
- failure taxonomy
- release blocker list
- rerun plan
- downstream fix recommendations

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- run_ids
- baseline_run
- threshold_status
- failure_clusters
- blockers
- rerun_requirements

## Halt conditions

Default posture is to proceed and label the assumption inline. A partially annotated failure case or an unknown reviewer identity is a soft gap: state the assumption, mark it, and continue. Halt only when one of the six hard-halt classes applies.

- Approval — the analysis would waive, relax, or reinterpret a release threshold that an owner must authorize.
- Production or destructive — a recommended rerun or remediation would act against production systems or overwrite a stored baseline run.
- Security or privacy — failure examples, transcripts, or exports contain personal, regulated, or customer-confidential data, or the failures themselves indicate data leakage.
- Source conflict — run metadata, baseline records, and threshold definitions disagree on what was measured or on what it was measured against.
- Release integrity — a release decision would rest on this run while scoring reliability is too weak to support it, or while thresholds or baseline are undefined.
- Connector unreachable — raw results, run metadata, or baseline runs exist but cannot be read.

## Downstream handoffs

- prompt-systems-desk
- model-selection-desk
- retrieval-rag-design-desk
- ai-safety-review-desk
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
- Passing means every threshold carries a stated status, every material failure belongs to a named cluster with cited cases, the release-gate verdict is stated with its blockers, and any rerun requirement names what must change.
