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

- Identify observability questions and failure modes.
- Map trace events, metrics, logs, and spans.
- Define dashboards, alerts, runbooks, and ownership.
- Apply privacy and retention constraints.
- Connect telemetry to eval and incident workflows.

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

- Runtime architecture or operational ownership is unclear.
- Telemetry would capture sensitive data without controls.
- Alert thresholds cannot be set due to missing baselines.

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
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
