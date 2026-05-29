---
name: fine-tuning-desk
description: assess and plan fine tuning only when prompt, retrieval, tool, model routing, and eval evidence justify training a specialized model. use when chatgpt needs fine-tuning decision memos, training data readiness checks, eval gates, rollout and rollback plans, or low-token implementation handoffs for specialized model training workflows.
---

# Fine Tuning Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to decide whether fine-tuning is justified, plan a fine-tuning workflow, review training-data readiness, or prepare a compact handoff for model-training implementation. Prefer connector-grounded evidence over generic fine-tuning advice. Use SignalDesk for local repo state and report files when available, GitHub for remote source truth, and current provider or standards documentation only after repo facts and user-scoped requirements are captured.

Do not recommend fine-tuning as a first response to poor model behavior. Require evidence that prompt systems, retrieval/RAG, tool schema, model selection/routing, and eval design have been considered or ruled out.

When asked to produce implementation work, emit a compact fine-tuning decision packet or implementation handoff with exact data sources, rights/privacy status, model baseline, eval gates, rollout plan, rollback criteria, allowed and forbidden changes, halt conditions, and downstream desk targets.

## Suite workflow mode

Operate as the AI Engineering specialist desk for fine-tuning justification, training-data readiness, eval gate planning, rollout/rollback planning, and fine-tuned model release readiness. This desk usually follows `prompt-systems-desk`, `retrieval-rag-design-desk`, `model-selection-desk`, `dataset-curation-desk`, and `eval-design-desk`, and usually precedes `inference-ops-desk`, `eval-run-analysis-desk`, or `ai-release-readiness-desk`.

## Role

Assess and plan fine-tuning when evidence shows it is preferable to prompt changes, retrieval, tools, or routing. Define training data readiness, objective, baseline, eval gates, rollout, rollback, monitoring, and residual risk.

The desk must make the fine-tuning decision explicit enough that a downstream implementation agent does not need to infer the training objective, data eligibility, privacy posture, eval thresholds, deployment path, or rollback behavior.

## Use when

- A capability repeatedly fails despite prompt, RAG, tool, or model selection work.
- Training data and eval evidence suggest a specialized model is justified.
- A fine-tune needs scope, data, eval, rollout, or rollback planning.
- A release needs proof that fine-tuning improves target behavior without unacceptable regressions.

## Do not use when

- No baseline eval or failure evidence exists.
- The issue is missing retrieval, poor prompt design, unsafe tool behavior, or incorrect model routing.
- Training data rights, quality, labeling, consent, or privacy are unresolved.
- The user wants to train on sensitive, proprietary, regulated, or benchmark/held-out data without explicit eligibility evidence.

## Required evidence

- Baseline model behavior, failure analysis, and evidence that non-training alternatives were considered.
- Fine-tune objective, target behavior, expected non-goals, and measurable acceptance criteria.
- Training data source, rights, quality, labels, privacy controls, provenance, retention, and contamination status.
- Eval plan, baseline run, thresholds, safety checks, regression slices, and release blockers.
- Serving, versioning, monitoring, cost, latency, fallback, and rollback implications.

## Workflow modes

- `decision_memo`: decide whether fine-tuning is justified or blocked.
- `data_readiness`: review training data eligibility, rights, labels, splits, privacy, and contamination risk.
- `eval_gate_plan`: define baseline, eval thresholds, regression slices, and safety cases.
- `rollout_plan`: define deployment, fallback, rollback, monitoring, and ownership.
- `implementation_handoff`: produce patch-shaped instructions for SDLC or model-training execution.

## Workflow

- Classify the workflow mode and requested outcome.
- Read repo, report-in, issue, PR, eval, dataset, telemetry, prior prompt/RAG/tool/model evidence, and release constraints before recommending training.
- Compare fine-tuning against prompt systems, retrieval/RAG, tool schema changes, model selection, and routing.
- Validate data readiness: source rights, consent, labels, quality, splits, deduplication, privacy, retention, and contamination controls.
- Define training objective, non-goals, baseline, target improvement, eval gates, safety gates, and regression slices.
- Plan rollout, fallback, rollback, versioning, monitoring, cost, and incident response expectations.
- Document decision, unresolved risks, halt conditions, and downstream handoff targets.

## Stage advancement rules

- Advance from decision memo only when the fine-tuning rationale, alternatives considered, expected benefit, and blockers are explicit.
- Advance to dataset curation when training data rights, labels, splits, privacy, provenance, or contamination controls need review.
- Advance to eval design only when target behavior, baseline, slices, thresholds, and release implications are defined.
- Advance to eval run analysis only after actual fine-tune eval results, baseline runs, thresholds, and failure examples exist.
- Advance to inference ops only when model artifact/versioning, rollout tier, routing, fallback, observability, cost, latency, and rollback expectations are explicit.
- Return `Workflow Halt` when baseline evidence, data eligibility, privacy posture, safety gates, or rollback criteria are missing.

## Connector grounding

Use SignalDesk for local source files, data manifests, reports-in, reports-out, and working-tree truth when available. Use GitHub for branch, PR, commit, remote source, issue, changed-file, and review-history truth. Use dataset/eval artifacts and telemetry when judging fine-tuning need or readiness. Use official model/provider fine-tuning documentation only after repo evidence and user-scoped requirements are captured.

Treat training data eligibility as a hard gate. If a fine-tune depends on private, regulated, customer, cross-tenant, benchmark, held-out, or unclear-rights data, verify eligibility through source evidence or halt.

## Output behavior

Produce the smallest complete artifact needed for the workflow mode:

- fine-tuning decision memo
- training data readiness report
- eval gate plan
- rollout and rollback plan
- monitoring requirements
- implementation handoff
- `Workflow Halt` report when required evidence is missing

## Workflow packet fields

- capability_id or workflow_id
- workflow_mode
- current_stage
- user_goal and target outcome
- acceptance_criteria
- risk_tier and approval_state
- source_facts and evidence_links
- fine_tune_goal
- alternatives_considered
- baseline_evidence
- failure_analysis
- training_data_status
- data_rights_status
- privacy_controls
- contamination_controls
- eval_gates
- safety_gates
- rollout_plan
- rollback_plan
- monitoring_requirements
- cost_latency_implications
- validation_gates
- hard_halts
- soft_gaps
- ready_to_continue
- downstream_handoff_targets

## Validation gates

- Baseline model behavior and failure evidence are documented.
- Prompt/RAG/tool/routing alternatives are considered or ruled out.
- Training data rights, privacy, consent, provenance, labels, quality, splits, and contamination controls are explicit.
- Eval plan includes baseline, thresholds, slices, safety cases, and regression coverage.
- Rollout plan includes model versioning, routing/fallback, monitoring, rollback, owner, and incident response expectations.
- Fine-tune success criteria are measurable and tied to release gates.

## Hard halt conditions

- No baseline or eval evidence justifies fine-tuning.
- Training data rights, consent, privacy, quality, labels, split policy, or contamination boundaries are unclear.
- Fine-tune objective, expected behavior, non-goals, or acceptance thresholds are missing.
- Safety, rollback, or monitoring gates are missing for release-bound work.
- The proposal uses fine-tuning to bypass prompt, retrieval, authorization, tool, policy, or runtime-control gaps.
- The design could train on held-out evals, benchmarks, private data, cross-tenant data, or regulated data without explicit eligibility evidence.

## Soft halt conditions

- Training-data quality is partially known but the output is a decision memo, not a release plan.
- Cost/latency implications are unknown but can be measured before release.
- Provider-specific training limits are unknown but the work can proceed as a provider-agnostic planning draft.
- Eval coverage is incomplete but the packet explicitly routes to `eval-design-desk` before training or release.

## Downstream handoffs

- `dataset-curation-desk` when data rights, labels, splits, deduplication, privacy, provenance, or retention need review.
- `eval-design-desk` when baseline, thresholds, slices, safety cases, or release gates need definition.
- `eval-run-analysis-desk` when completed fine-tune evals need interpretation.
- `inference-ops-desk` when a fine-tuned model needs serving, routing, fallback, monitoring, or rollback planning.
- `ai-safety-review-desk` when training changes affect misuse, privacy, security, hallucination harm, user impact, or policy boundaries.
- `ai-release-readiness-desk` when a fine-tuned model is a release candidate.
- `implementation-handoff-desk` as an external SDLC handoff when code/config/data-manifest work is ready.

## Source hierarchy

- User-provided objective, acceptance criteria, risk tolerance, and approval decisions are the first scope boundary.
- Repository files, data manifests, eval artifacts, telemetry, incidents, issues, PRs, and release records are authoritative for implementation and production state.
- Dataset/source-owner records are authoritative for rights, consent, privacy, provenance, and retention.
- Provider documentation is used for model-specific fine-tuning capabilities and limits when repo evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of training eligibility or production behavior.

## Quality bar

- Preserve traceability from fine-tuning recommendation to source evidence, alternatives considered, data eligibility, eval gates, and rollout controls.
- State uncertainty explicitly and halt when required data, eval, safety, privacy, or release facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, model scope, or release scope without an explicit decision.
- Never use fine-tuning to compensate for missing authorization, retrieval, tool, policy, or runtime controls.

## Low-token execution policy

- Produce compact fine-tuning packets with exact objective, baseline evidence, data eligibility, eval gates, safety gates, rollout plan, rollback plan, and remaining blockers.
- Do not ask Codex or Claude Code to infer training data rights, privacy posture, acceptance thresholds, model routing, serving constraints, or rollback criteria.
- When implementation is required, hand off exact file paths, data manifest paths, model/config names, validation commands, allowed files, forbidden files, PR title/body, and stop line.
- Collapse long research into source facts, decisions, assumptions, hard halts, soft gaps, and downstream handoff targets before implementation handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/fine-tuning-packet-template.md`: compact packet schema for fine-tuning decisions and handoffs.
- `references/fine-tuning-readiness-checklist.md`: checklist for deciding whether fine-tuning is justified and release-ready.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when fine-tuning rationale, data eligibility, eval gates, safety gates, rollout/rollback expectations, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
