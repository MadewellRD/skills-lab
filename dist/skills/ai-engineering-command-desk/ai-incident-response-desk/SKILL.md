---
name: ai-incident-response-desk
description: triage ai production incidents involving hallucination spikes, safety failures, prompt injection, tool misuse, data leakage, model regressions, cost spikes, latency degradation, eval regressions, user harm reports, containment, rollback, mitigation, and post-incident follow-up.
---

# AI Incident Response Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to triage, coordinate, or document production AI incidents. Prefer connector-grounded evidence over generic incident advice. Use GitHub for branches, PRs, recent changes, issues, and checks; use SignalDesk for local repo state, worktree evidence, logs, and report files when available; use telemetry, eval artifacts, provider status, user reports, and support tickets when the user provides or connects them.

Treat this desk as an AI-specific incident controller. It does not replace the SDLC `incident-response-desk`; it prepares AI-specific evidence, containment, rollback, safety, eval, and observability facts, then hands off to SDLC incident response or implementation desks when software delivery work is required.

When asked to produce implementation work, do not emit broad instructions. Emit a compact incident packet or implementation handoff with exact source facts, affected surfaces, containment state, rollback option, validation gates, allowed and forbidden changes, halt conditions, owner approvals, and downstream desk targets.

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

## Low-token execution policy

- Produce compact incident packets with exact affected capability, versions, evidence links, suspected change window, severity, containment options, rollback status, validation gates, and downstream owners.
- Do not ask Codex or Claude Code to infer incident scope, affected files, release SHA, model/prompt version, rollback path, or safety gate.
- When implementation is required, hand off exact repo, base branch, allowed files, forbidden files, validation commands, PR title/body, report path, and stop line.
- Collapse long logs and reports into source facts, decisions, assumptions, hard halts, soft gaps, and follow-up targets before implementation handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/ai-incident-response-packet-template.md`: reusable packet for incident triage and handoff.
- `references/ai-incident-quality-checklist.md`: validation checklist for incident evidence, containment, rollback, and follow-up.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when incident severity, affected surfaces, evidence, containment status, rollback status, follow-up targets, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
