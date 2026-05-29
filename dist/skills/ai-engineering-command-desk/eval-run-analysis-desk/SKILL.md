---
name: eval-run-analysis-desk
description: analyze completed ai eval runs, regression deltas, failure clusters, grading reliability, threshold status, release blockers, and rerun recommendations for model, prompt, tool, rag, and agent changes. use when chatgpt needs to interpret eval evidence, decide pass/fail or release-blocker status, diagnose failures, compare against baselines, create rerun plans, or produce low-token downstream handoffs grounded in source facts.
---

# Eval Run Analysis Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to analyze completed AI evaluation evidence. Prefer raw eval outputs, run metadata, baselines, rubrics, thresholds, reviewer notes, production incidents, and release criteria over generic quality commentary. Use GitHub and connected repo sources for run artifacts, PR context, changed files, eval fixtures, and release records when available. Use SignalDesk for local repo state and report files when available.

Do not design a new eval unless the run cannot be analyzed because required criteria are missing. In that case, return `Workflow Halt` and route to `eval-design-desk` with exact missing inputs.

## Suite workflow mode

Operate as the AI Engineering specialist desk for completed eval interpretation. This desk usually follows `eval-design-desk` and precedes fix routing, `ai-safety-review-desk`, `ai-release-readiness-desk`, or implementation handoff.

## Role

Analyze completed eval evidence. Identify pass/fail status, regression deltas, failure clusters, grader reliability, threshold misses, release blockers, required reruns, likely upstream cause, and downstream fix targets.

## Use when

- Eval results need interpretation.
- A model, prompt, tool, RAG, or agent change may have regressed behavior.
- A release decision depends on eval evidence.
- An eval run needs failure taxonomy, rerun guidance, or blocker classification.

## Do not use when

- No raw eval results are available.
- The scoring criteria or thresholds are undefined.
- The task is to design a new eval rather than analyze a completed run.
- The user asks for release approval without sufficient eval, safety, or owner evidence.

## Required evidence

- Raw eval results, run metadata, model and prompt versions, dataset slice IDs, grader versions, and run timestamps.
- Rubric, grading method, threshold definitions, release gates, and baseline runs.
- Failure examples, reviewer notes, known regressions, relevant incidents, and PR/change context.
- Dataset slice definitions for normal, edge, adversarial, safety, retrieval, tool-use, and high-impact cases when applicable.
- Confidence or reliability indicators for automated graders and human review process when available.

## Workflow modes

- `release_gate_analysis`: decide whether eval evidence blocks, warns, or clears release.
- `regression_analysis`: compare current run against baseline and identify behavior deltas.
- `failure_cluster_analysis`: group failures by likely cause and downstream owner.
- `grader_reliability_review`: assess rubric, grader consistency, and human review needs.
- `rerun_planning`: define exact rerun scope after fixes, dataset updates, or grader changes.
- `implementation_handoff`: produce compact fix or rerun instructions for another desk or coding agent.

## Workflow

- Verify run completeness, artifact integrity, version metadata, and scoring consistency.
- Compare results against baseline runs, thresholds, and release gates.
- Break down performance by dataset slice, risk tier, failure type, and changed component.
- Cluster failures by observed behavior and likely root cause: prompt, model, tool schema, RAG, dataset, safety policy, agent architecture, or runtime issue.
- Assess grader reliability and human-review sufficiency.
- Classify each finding as blocker, warning, accepted risk, or pass.
- Recommend fixes, reruns, threshold updates, release gates, or downstream desk handoffs.

## Output behavior

Produce the smallest complete artifact needed:

- eval analysis report
- failure taxonomy
- threshold status table
- regression delta summary
- release blocker list
- rerun plan
- downstream fix handoff
- `Workflow Halt` report when required evidence is missing

## Workflow packet fields

- capability_id or workflow_id
- workflow_mode
- current_stage
- user_goal and target outcome
- source_facts and evidence_links
- run_ids
- run_metadata
- baseline_run
- dataset_slices
- rubric
- grader_versions
- thresholds
- threshold_status
- regression_deltas
- failure_examples
- failure_clusters
- grader_reliability
- blockers
- warnings
- accepted_risks
- rerun_requirements
- release_gate_status
- hard_halts
- soft_gaps
- ready_to_continue
- downstream_handoff_targets

## Validation gates

- Raw results, baseline, thresholds, and rubric are all present or explicitly marked as blockers.
- Run metadata identifies model, prompt, dataset, grader, and code/config versions.
- Failure clusters include evidence examples and likely owning desk.
- Release status is stated as pass, warning, blocker, or halt with reason.
- Rerun requirements specify exact slices, fixtures, thresholds, and changed components.
- Safety, privacy, data leakage, prompt injection, and high-impact failures are escalated instead of averaged away.

## Hard halt conditions

- Raw results, thresholds, rubric, or baseline are missing.
- Run metadata is insufficient to identify model/prompt/tool/RAG/agent versions.
- Scoring reliability is too weak for release decisions.
- Failure examples indicate safety, privacy, data leakage, cross-tenant exposure, or policy-evasion risk requiring review.
- A requested release decision lacks required approval owner or safety gate evidence.

## Soft halt conditions

- Some dataset slices are underrepresented but not release-critical.
- Automated grader reliability is uncertain but human review can resolve a bounded subset.
- Baseline exists but is stale; analysis can proceed with explicit caveat and rerun requirement.
- Failure examples are sparse but sufficient to classify likely owner and next desk.

## Downstream handoffs

- `prompt-systems-desk` for instruction, context, refusal, output, or prompt-injection regressions.
- `model-selection-desk` for model capability, routing, fallback, or provider-behavior issues.
- `retrieval-rag-design-desk` for grounding, citation, corpus, freshness, or permission-filter failures.
- `tool-schema-design-desk` for argument validation, authorization, idempotency, or error-contract failures.
- `agent-architecture-desk` for planning-loop, memory, delegation, retry, or halt-policy failures.
- `ai-safety-review-desk` for safety, misuse, privacy, or high-impact harm concerns.
- `ai-release-readiness-desk` when release status can be decided from the analyzed evidence.
- `implementation-handoff-desk` as an external SDLC handoff when fix or rerun work is ready for Codex or Claude Code.

## Source hierarchy

- Raw eval artifacts, run metadata, baselines, rubrics, reviewer notes, telemetry, incidents, and release records are authoritative for eval state.
- User-provided objective, acceptance criteria, and risk tolerance define scope and release constraints.
- Repo source files, PRs, issues, and changelogs define changed components and implementation state.
- Provider documentation and external model documentation are used for model or API behavior when internal evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of eval outcome.

## Quality bar

- Preserve traceability from conclusion to run evidence, failure examples, and thresholds.
- State uncertainty explicitly and halt when required eval facts are missing.
- Prefer measured deltas and slice-level status over aggregate claims.
- Do not average away severe safety, privacy, data leakage, or high-impact failures.
- Produce downstream handoffs with exact owner desk, fix hypothesis, required evidence, validation gate, and rerun plan.

## Low-token execution policy

- Produce compact eval-run packets with run IDs, baseline, threshold status, failure clusters, blocker status, and rerun requirements.
- Do not ask Codex or Claude Code to infer failure ownership, test scope, release blockers, or rerun commands from raw eval logs.
- When implementation is required, hand off exact files or components when known, failing examples, expected fix owner, validation commands, allowed and forbidden changes, PR title/body, and stop line.
- Collapse long eval evidence into source facts, decisions, assumptions, hard halts, soft gaps, and downstream handoff targets before any coding-agent handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/eval-run-analysis-packet-template.md`: compact packet template for eval-run analysis outputs.
- `references/eval-run-quality-checklist.md`: gate checklist for run completeness, reliability, blockers, and reruns.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when run completeness, baseline, thresholds, failure clusters, release status, rerun requirements, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
