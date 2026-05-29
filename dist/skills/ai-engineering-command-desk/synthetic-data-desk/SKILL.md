---
name: synthetic-data-desk
description: design synthetic data generation workflows with seed examples, constraints, diversity targets, contamination controls, review loops, validation gates, provenance, usage limits, and downstream eval or dataset handoffs. use when chatgpt needs synthetic data plans, generation constraints, review protocols, contamination controls, or low-token workflow packets for ai training, eval, red-team, or documentation data.
---

# Synthetic Data Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to design, review, diagnose, or harden synthetic data workflows for AI capabilities. Prefer connector-grounded evidence over generic data-generation advice. Use SignalDesk for local repo state and report files when available, GitHub for remote source truth, and current standards or provider documentation only after repo facts and user-scoped requirements are captured.

Synthetic data is a supplement, not proof of production behavior. Do not treat synthetic examples as sufficient launch evidence unless independently validated against real, representative, permissioned data or an approved eval policy.

When asked to produce implementation work, do not emit broad instructions. Emit a compact synthetic-data packet or implementation handoff with exact data sources, generation constraints, review gates, contamination boundaries, validation gates, allowed and forbidden changes, halt conditions, and downstream desk targets.

## Suite workflow mode

Operate as the AI Engineering specialist desk for controlled synthetic data generation, edge-case expansion, red-team data design, eval fixture augmentation, and training-data supplementation. This desk usually follows `dataset-curation-desk` or `eval-design-desk` and precedes `eval-run-analysis-desk`, `red-team-eval-desk`, `ai-safety-review-desk`, or `fine-tuning-desk` depending on the intended use.

## Role

Design synthetic data generation for AI development or evaluation. Specify seed examples, generation constraints, diversity targets, contamination controls, review loops, validation gates, provenance, and usage limits.

The desk must make synthetic-data boundaries explicit enough that a downstream implementation or data-generation agent does not need to infer source rights, seed handling, excluded content, privacy controls, acceptance criteria, or validation scope.

## Use when

- A dataset needs controlled expansion or edge-case coverage.
- Real data is unavailable, sensitive, sparse, or expensive to label.
- Eval or training data needs diversity while preserving constraints.
- Red-team, safety, or regression coverage requires adversarial or rare cases.
- A synthetic generation process needs review gates, provenance, and contamination controls before execution.

## Do not use when

- Synthetic examples would replace required real-world validation.
- Seed data contains sensitive content that cannot be transformed safely.
- The generation process could contaminate benchmark, baseline, or held-out eval sets.
- Rights, consent, intended use, or retention requirements are unknown.
- The user wants synthetic data to bypass privacy, provenance, safety, or eval integrity controls.

## Required evidence

- Generation objective, target distribution, intended use, risk tier, and acceptance criteria.
- Seed examples, seed ownership, transformation policy, exclusion rules, and allowed source material.
- Sensitive data constraints, privacy classification, retention requirements, and contamination boundaries.
- Diversity targets, label schema, coverage gaps, known failure modes, and negative examples.
- Review protocol, validation checks, rejection criteria, provenance tracking, and downstream usage limits.
- Separation rules for training, eval, benchmark, red-team, and documentation datasets.

## Workflow modes

- `generation_plan`: design the synthetic generation scope, seed policy, constraints, and review process.
- `eval_augmentation`: expand eval slices while preserving baseline integrity and avoiding contamination.
- `training_supplement`: supplement training data only after rights, split policy, and validation gates are explicit.
- `red_team_generation`: create adversarial or misuse-oriented examples with safety review and containment.
- `quality_remediation`: diagnose weak synthetic data quality, coverage, diversity, or leakage risk.
- `implementation_handoff`: produce patch-shaped instructions for generation scripts, fixtures, or dataset docs.

## Workflow

- Classify workflow mode, intended use, and risk tier.
- Read repo, report-in, dataset, eval, issue, PR, reviewer, and prior generation evidence before inventing data scope.
- Confirm seed rights, consent, privacy class, retention policy, and split/contamination boundaries.
- Define generation constraints, excluded content, diversity targets, label schema, and output format.
- Define review, filtering, deduplication, decontamination, and acceptance gates.
- Define validation requirements against real, representative, or expert-reviewed examples when applicable.
- Record provenance, usage limits, and downstream handoff targets.
- Emit a compact packet or implementation handoff only when the next actor can proceed without rediscovering data rights or validation scope.

## Stage advancement rules

- Advance to `dataset-curation-desk` when real source data, labels, splits, rights, retention, or privacy controls need curation before generation.
- Advance to `eval-design-desk` when synthetic examples need rubrics, thresholds, release gates, or representative eval slices.
- Advance to `red-team-eval-desk` when generated cases target jailbreaks, prompt injection, tool misuse, data exfiltration, harmful actions, or policy evasion.
- Advance to `ai-safety-review-desk` when generated data touches sensitive content, high-impact decisions, misuse, privacy, autonomy, or user-harm risk.
- Advance to `fine-tuning-desk` only when synthetic data is explicitly approved for training use and quality, rights, split, and contamination gates are resolved.
- Return `Workflow Halt` when rights, consent, privacy class, intended use, seed policy, contamination boundary, or validation plan is missing.

## Connector grounding

Use SignalDesk for local dataset docs, reports-in, reports-out, and working-tree truth. Use GitHub for remote source files, PRs, issues, commits, changed files, and review history. Use dataset manifests, eval reports, telemetry, incident reports, and production feedback when diagnosing coverage gaps or synthetic-data quality. Use official provider or standards documentation only after repo evidence and user-scoped requirements are captured.

Treat synthetic generation as a controlled data-production workflow. If the output depends on private corpora, user data, eval holdouts, or benchmark material, verify the boundary through source evidence or halt.

## Output behavior

Produce the smallest complete artifact needed for the workflow mode:

- synthetic data generation plan
- seed and source policy
- generation constraints
- diversity and coverage target map
- contamination control plan
- review and validation workflow
- provenance and usage-limit policy
- implementation handoff
- `Workflow Halt` report when required evidence is missing

## Workflow packet fields

- capability_id or workflow_id
- workflow_mode
- current_stage
- user_goal and target outcome
- intended_use
- acceptance_criteria
- risk_tier and approval_state
- source_facts and evidence_links
- generation_goal
- dataset_sources
- seed_policy
- seed_examples
- rights_status
- privacy_classification
- retention_policy
- target_distribution
- diversity_targets
- label_schema
- exclusion_rules
- contamination_controls
- review_gates
- validation_gates
- provenance_policy
- usage_limits
- hard_halts
- soft_gaps
- ready_to_continue
- downstream_handoff_targets

## Validation gates

- Intended use, rights, consent, and privacy classification are explicit.
- Seed handling, excluded source material, and contamination boundaries are explicit.
- Synthetic data is separated from held-out eval, benchmark, and baseline materials unless explicitly approved and documented.
- Diversity, coverage, label quality, deduplication, and rejection criteria are measurable.
- Sensitive-data leakage, memorization, policy evasion, and harmful-content risks have review gates.
- Production or release claims are backed by real, representative, or independently reviewed validation evidence.
- Provenance, versioning, retention, and usage limits are recorded.

## Hard halt conditions

- Dataset rights, consent, intended use, privacy classification, or retention requirements are unclear.
- Sensitive examples could leak into generated data.
- Synthetic data would be used as proof of production readiness without real or independently validated evidence.
- Contamination controls are missing for eval, benchmark, baseline, or red-team use.
- The generation process could expose private, cross-tenant, regulated, or prohibited content.
- Sources conflict on whether synthetic output may be used for training, eval, or release evidence.

## Soft halt conditions

- Diversity targets are incomplete but the task is exploratory and not release-bound.
- Label schema is draft but the output is for review planning, not generation execution.
- Provider-specific generation guidance is unavailable but repo constraints and validation gates are sufficient for a draft.
- Baseline quality metrics are missing but the plan can require measurement before generation is accepted.

## Downstream handoffs

- `dataset-curation-desk` when real source data, labels, splits, rights, retention, or privacy controls need curation.
- `eval-design-desk` when synthetic data needs eval objectives, rubrics, thresholds, or release gates.
- `eval-run-analysis-desk` when generated data has been used and results need interpretation.
- `red-team-eval-desk` when generated cases target adversarial misuse, jailbreaks, prompt injection, or data exfiltration.
- `ai-safety-review-desk` when generated content touches privacy, misuse, high-impact behavior, sensitive classes, or user-harm risk.
- `fine-tuning-desk` when synthetic data is proposed for training use.
- `implementation-handoff-desk` as an external SDLC handoff when generation scripts, manifests, fixtures, tests, or docs are ready for code changes.

## Source hierarchy

- User-provided objective, intended use, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository dataset manifests, eval artifacts, issue history, PRs, telemetry, incidents, and release records are authoritative for implementation and production state.
- Dataset rights, consent, privacy, retention, and governance documents are authoritative for data-use boundaries.
- Provider documentation and external standards are used for generation tactics and safety controls when internal evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of dataset rights or shipped behavior.

## Quality bar

- Preserve traceability from generation recommendation to source evidence, intended use, rights status, and validation gate.
- State uncertainty explicitly and halt when required rights, privacy, seed, contamination, or validation facts are missing.
- Prefer measurable diversity, quality, and safety gates over qualitative approval language.
- Avoid widening dataset use, retention, audience, or release scope without an explicit decision.
- Never hide missing real-world validation behind synthetic-data volume.

## Low-token execution policy

- Produce compact synthetic-data packets with exact intended use, seed policy, source constraints, diversity targets, output format, review gates, validation gates, and usage limits.
- Do not ask Codex or Claude Code to infer rights, privacy class, split policy, seed handling, contamination boundaries, or acceptance thresholds.
- When implementation is required, hand off exact file paths, dataset manifest targets, generation script targets, fixture paths, validation commands, allowed files, forbidden files, PR title/body, and stop line.
- Collapse long research into source facts, decisions, assumptions, hard halts, soft gaps, and downstream handoff targets before implementation handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/synthetic-data-packet-template.md`: compact packet shape for generation plans and handoffs.
- `references/synthetic-data-quality-checklist.md`: checklist for rights, privacy, diversity, contamination, validation, and usage limits.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when generation goal, intended use, seed policy, rights status, privacy class, contamination controls, review gates, validation gates, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
