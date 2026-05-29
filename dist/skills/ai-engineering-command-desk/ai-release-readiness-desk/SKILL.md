---
name: ai-release-readiness-desk
description: assess readiness to release AI capabilities across requirements, evals, safety review, red-team status, inference ops, observability, rollback, docs, support handoff, approval, and go/no-go gates. use when chatgpt needs launch readiness review, staged rollout gates, risk acceptance notes, ai release blockers, or low-token release handoffs for ai systems.
---

# AI Release Readiness Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to decide whether an AI capability is ready for launch, staged rollout, or downstream release/deployment handoff. Prefer connector-grounded evidence over generic launch checklists. Use GitHub for PRs, branches, commits, changed files, checks, and release evidence. Use SignalDesk for local repo state, `work/reports-in/`, and `work/reports-out/` when available. Use eval, safety, red-team, inference, observability, incident, and support artifacts as release evidence.

Do not produce a go recommendation from incomplete evidence. Return `Workflow Halt` when required eval, safety, red-team, inference, observability, rollback, approval, or support readiness facts are missing.

## Role

Assess whether an AI capability is ready to release. Check requirements, evals, safety review, red-team status, inference operations, observability, rollback, docs, support handoff, and owner approval.

This desk converts AI launch ambiguity into an explicit go/no-go decision, blocker list, risk acceptance note, or downstream release/deployment handoff.

## Use when

- An AI capability is approaching launch, staged rollout, canary, beta, or production promotion.
- A go/no-go decision needs evidence.
- A release has unresolved eval, safety, ops, observability, rollback, support, or approval questions.
- A downstream SDLC release/deployment prompt needs compact, evidence-backed launch gates.

## Do not use when

- The capability is still in early discovery.
- Core requirements, target users, or release target are unknown.
- The user needs general software release planning without AI-specific gates.
- The request asks to bypass safety review, eval thresholds, rollback policy, or approval gates.

## Required evidence

- Accepted requirements, issue scope, product owner, and release target.
- Eval results, thresholds, baseline comparison, regression status, and known failures.
- Safety review, red-team status, misuse risk, privacy risk, tool-use risk, and residual risk notes.
- Inference ops, provider quotas, fallback behavior, observability, incident response, rollback, support, and documentation readiness.
- Approval owner, accepted risks, launch criteria, and staged rollout or rollback decision path.

## Workflow modes

- `release_readiness_review`: assess all AI launch gates and produce go/no-go output.
- `blocker_triage`: classify blockers, warnings, accepted risks, and missing evidence.
- `staged_rollout_plan`: define canary, beta, percentage rollout, monitor gates, and rollback triggers.
- `handoff_packet`: prepare SDLC release, deployment, observability, or support handoff material.
- `halt_resume`: resume from a prior missing-evidence or blocked-launch report.

## Workflow

- Resolve release target, scope, current branch/PR/release artifact, and launch mode.
- Read repo, PR, eval, safety, red-team, ops, observability, incident, support, docs, and report-in evidence before making a launch recommendation.
- Check eval, safety, red-team, inference ops, observability, rollback, docs, support, and approval gates.
- Classify each gate as `pass`, `warning`, `blocked`, `not_applicable`, or `missing_evidence`.
- Separate release blockers from accepted residual risks.
- Produce go/no-go recommendation with explicit evidence and owner approval state.
- Prepare downstream handoff only when gates are sufficient for the target release mode.

## Outputs

- go/no-go report
- launch blocker list
- missing-evidence list
- accepted-risk notes
- staged rollout and rollback checklist
- release/deployment/support handoff summary
- `Workflow Halt` report when required evidence is missing

## Workflow packet fields

- capability_id or workflow_id
- workflow_mode
- release_target
- user_goal and target outcome
- source_facts and evidence_links
- risk_tier and approval_state
- approval_owner
- gate_status
- eval_status
- safety_status
- red_team_status
- inference_ops_status
- observability_status
- rollback_status
- docs_support_status
- blockers
- warnings
- accepted_risks
- missing_evidence
- go_no_go
- downstream_handoff_targets
- hard_halts
- soft_gaps
- ready_to_continue

## Validation gates

- Requirements and release target are explicit.
- Eval evidence meets the release threshold or is listed as a blocker.
- Safety review and red-team status are explicit for user-impacting, tool-using, private-data, or autonomous capabilities.
- Inference ops, observability, rollback, and incident response readiness are explicit for production launches.
- Docs, support handoff, owner approval, and accepted-risk notes are explicit when users or support teams are affected.
- Downstream release/deployment handoff contains exact branch, PR, commit, allowed files, forbidden files, validation commands, rollback triggers, and stop line when implementation is requested.

## Hard halt conditions

- Eval, safety, red-team, ops, observability, rollback, support, or approval evidence is required but missing.
- Approval owner is unclear for material risk.
- Production launch would proceed with unresolved blockers.
- Risk acceptance is implied but not explicitly owned.
- Source evidence conflicts on release scope, launch date, gate status, or owner approval.

## Soft gap conditions

- A non-production prototype has partial evidence and the user explicitly accepts prototype-only scope.
- Some support documentation is incomplete but rollout is internal and has an accountable owner.
- Monitoring thresholds are provisional but baseline collection is part of a controlled canary.

## Downstream handoffs

- `release-operations-desk` for SDLC release packaging, release notes, tag/version plan, and release runbook.
- `deployment-desk` for staged rollout, feature flags, deployment gates, and rollback execution.
- `observability-readiness-desk` for platform-level dashboards, alerts, SLOs, and runbooks.
- `incident-response-desk` or `ai-incident-response-desk` when launch risks require incident preparation or production issue handling.
- `eval-run-analysis-desk`, `ai-safety-review-desk`, `red-team-eval-desk`, `inference-ops-desk`, or `agent-observability-desk` when gate evidence is insufficient.

## Source hierarchy

- User-provided objective, acceptance criteria, approval decisions, and risk tolerance are the first scope boundary.
- Repository, PR, issue, eval, telemetry, incident, release, docs, and support evidence are authoritative for implementation and production state.
- AI Engineering suite references and official standards/vendor docs define domain constraints and current best practice.
- Conversation summaries and stakeholder notes are decision context, not proof of shipped behavior or approval.

## Quality bar

- Preserve traceability from recommendation to source evidence.
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, release scope, or user impact without explicit approval.
- Never mark a launch `go` when a blocker is unresolved or risk ownership is implicit.

## Low-token execution policy

- Produce compact release-readiness packets with release target, gate status, blockers, warnings, accepted risks, approval owner, validation gates, rollback triggers, and downstream handoff targets.
- Do not ask Codex or Claude Code to infer launch gates, risk acceptance, owner approval, validation commands, or rollback behavior.
- When implementation is required, hand off exact file paths, branch names, PR numbers, commit SHAs, allowed files, forbidden files, validation commands, PR title/body, and stop line.
- Collapse long reports into source facts, decisions, missing evidence, hard halts, soft gaps, and downstream handoffs before implementation handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/ai-release-readiness-packet-template.md`: compact go/no-go packet template.
- `references/release-readiness-quality-checklist.md`: release gate checklist.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when release target, gate status, blockers/warnings, risk acceptance, approval owner, rollback plan, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
