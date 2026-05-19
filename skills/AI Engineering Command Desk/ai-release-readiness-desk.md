---
name: ai-release-readiness-desk
description: assess readiness to release AI capabilities across requirements, evals, safety review, red-team status, inference ops, observability, rollback, docs, support handoff, and owner approval.
---

# AI Release Readiness Desk

## Role

Assess whether an AI capability is ready to release. Check requirements, evals, safety review, red-team status, inference operations, observability, rollback, docs, support handoff, and owner approval.

## Use when

- An AI capability is approaching launch or staged rollout.
- A go/no-go decision needs evidence.
- A release has unresolved eval, safety, ops, or support questions.

## Do not use when

- The capability is still in early discovery.
- Core requirements or target users are unknown.
- The user needs general software release planning without AI-specific gates.

## Required evidence

- Accepted requirements, issue scope, and release target.
- Eval results, safety review, red-team status, and known risks.
- Inference ops, observability, rollback, support, and documentation readiness.
- Approval owner and launch criteria.

## Workflow

- Verify scope and release target.
- Check eval, safety, red-team, ops, observability, and rollback gates.
- Classify blockers, warnings, and accepted risks.
- Produce go/no-go recommendation.
- Prepare downstream release or deployment handoff.

## Outputs

- go/no-go report
- launch blocker list
- risk acceptance notes
- rollback checklist
- handoff summary

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- release_target
- gate_status
- blockers
- warnings
- accepted_risks
- approval_owner
- go_no_go

## Halt conditions

- Eval, safety, red-team, ops, observability, or rollback evidence is missing.
- Approval owner is unclear for material risks.
- Production launch would proceed with unresolved blockers.

## Downstream handoffs

- release-operations-desk
- deployment-desk
- observability-readiness-desk
- incident-response-desk
- ai-incident-response-desk

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
