---
name: agent-observability-desk
description: design observability for AI agents and workflows including traces, prompts, model calls, tool calls, retrieval events, approvals, errors, eval probes, cost, latency, and safety signals.
---

# Agent Observability Desk

## Role

Design observability for AI agents and AI workflows. Define traces, prompts, model calls, tool calls, retrieval events, state transitions, approvals, errors, eval probes, cost, latency, and safety signals.

## Use when

- An AI capability is entering production or needs operational visibility.
- Agent, tool, RAG, or model behavior needs debugging or auditability.
- Incidents require better telemetry, dashboards, or runbooks.

## Do not use when

- The system has no runtime path yet.
- The only need is offline eval design.
- Telemetry would expose sensitive data without a privacy policy.

## Required evidence

- Architecture, runtime path, tool contracts, retrieval path, and state transitions.
- Operational questions, SLOs, incident types, and owner responsibilities.
- Logging, retention, privacy, redaction, and access-control constraints.
- Existing telemetry and dashboard gaps.

## Workflow

Produce an observability design that answers named operational questions: what a trace must contain, which metrics and alerts exist, who owns each signal, what the runbook says, and what must never be logged.

Constraints:

- Start from the operational questions and failure modes the telemetry must answer. A signal with no question behind it is noise.
- Privacy, redaction, retention, and access control are constraints on every signal, not a later pass.
- Every alert names a threshold, an owner, and a runbook. Never invent a baseline to justify a threshold; where no baseline exists, say so and state the measurement that would produce one.
- Telemetry connects to eval and incident workflows explicitly.
- Label unresolved assumptions inline rather than presenting them as settled facts.

Individual signals are independent. Designing each trace event, metric, log field, dashboard panel, and alert is parallel-safe. The privacy, redaction, and retention policy is shared and applies uniformly across all of them.

## Outputs

- observability design
- event schema
- dashboard plan
- alert plan
- runbook inputs

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- trace_events
- metrics
- log_policy
- dashboards
- alerts
- runbook_links
- privacy_constraints

## Halt conditions

Default posture is to proceed and label the assumption inline. A missing baseline for an alert threshold is a soft gap: propose a provisional threshold, mark it as provisional, name the measurement that would confirm it, and continue. Halt only when one of the six hard-halt classes applies.

- Approval — telemetry would be enabled in an environment, or at a retention level, the data owner has not authorized.
- Production or destructive — the change would alter or drop an existing production telemetry stream that incident response or audit depends on.
- Security or privacy — proposed signals would capture secrets, credentials, personal data, or customer content without redaction and access control.
- Source conflict — architecture docs, runtime configuration, and existing dashboards disagree on the runtime path actually being instrumented.
- Release integrity — a capability would reach production with no signal capable of detecting its known failure modes.
- Connector unreachable — existing telemetry, dashboards, or runbooks exist but cannot be read.

## Downstream handoffs

- inference-ops-desk
- cost-latency-optimization-desk
- ai-incident-response-desk
- ai-release-readiness-desk
- observability-readiness-desk when platform-level readiness is needed

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
- Passing means every named operational question maps to at least one signal, every alert carries a threshold, an owner, and a runbook, and every captured field carries a stated redaction and retention treatment.
