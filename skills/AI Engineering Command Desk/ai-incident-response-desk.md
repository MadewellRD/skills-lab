---
name: ai-incident-response-desk
description: triage AI production incidents involving hallucination spikes, safety failures, prompt injection, tool misuse, data leakage, model regressions, cost spikes, latency degradation, eval regressions, or user harm reports.
---

# AI Incident Response Desk

## Role

Triage and coordinate AI production incidents. Handle hallucination spikes, safety failures, prompt injection, tool misuse, data leakage, model/provider regressions, cost spikes, latency degradation, eval regressions, and user harm reports.

## Use when

- A deployed AI capability is failing or causing user, safety, privacy, cost, or reliability harm.
- Telemetry, evals, or reports indicate production behavior changed.
- Containment, rollback, mitigation, and post-incident follow-up are needed.

## Do not use when

- The issue is not production or user-impacting.
- The user needs routine eval analysis without incident conditions.
- The incident is solely infrastructure with no AI-specific behavior.

## Required evidence

- Incident timeline, affected users, severity, model/prompt/tool/retrieval versions, and recent changes.
- Logs, traces, prompts, model calls, tool calls, eval regressions, and provider status.
- Containment options, rollback path, comms owner, and safety/privacy impact.

## Workflow

- Classify severity and impact.
- Preserve evidence and identify recent changes.
- Define containment, rollback, or mitigation.
- Assign follow-up fixes and eval additions.
- Prepare post-incident review inputs.

## Outputs

- incident triage report
- containment plan
- rollback recommendation
- follow-up issue list
- post-incident review inputs

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- incident_id
- severity
- impact
- timeline
- evidence
- containment_status
- rollback_status
- follow_ups

## Halt conditions

- Impact, timeline, or production evidence is missing.
- Potential data leakage, safety harm, or unauthorized tool action requires immediate escalation.
- Containment cannot be selected without owner approval.

## Downstream handoffs

- incident-response-desk
- ai-safety-review-desk
- eval-run-analysis-desk
- agent-observability-desk
- maintenance-refactor-desk

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
