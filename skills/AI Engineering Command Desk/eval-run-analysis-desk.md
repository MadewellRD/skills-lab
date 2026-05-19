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

- Validate run completeness and scoring consistency.
- Compare against baseline and thresholds.
- Cluster failures by behavior and likely cause.
- Decide blocker, warning, or pass status.
- Recommend fixes, reruns, or release gate outcomes.

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

- Raw results, thresholds, or baseline are missing.
- Scoring reliability is too weak for release decisions.
- Failure examples indicate safety, privacy, or data leakage risk requiring review.

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
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
