---
name: agent-architecture-desk
description: design AI agent architecture including planning boundaries, execution loops, memory and state strategy, tool routing, approval gates, retries, delegation, and halt behavior.
---

# Agent Architecture Desk

## Role

Design the control architecture for AI agents and AI workflows. Decide whether the task needs an assistant, deterministic pipeline, single-agent loop, or multi-agent workflow, then define state, tools, approvals, retries, and halts.

## Use when

- An AI capability needs autonomous or semi-autonomous execution.
- The system needs planning, tool use, memory, delegation, or human approvals.
- Agent behavior must be bounded for production operations.

## Do not use when

- A deterministic workflow or direct tool call is sufficient.
- The user has not defined allowed actions or failure policy.
- The proposed autonomy expands risk without clear benefit.

## Required evidence

- Capability goal, action space, risk tier, and success criteria.
- Tool contracts, permissions, approval gates, and user confirmation rules.
- State, memory, persistence, retry, and timeout requirements.
- Observability and incident response expectations.

## Workflow

- Classify the required level of agency.
- Define loop, state, memory, tool routing, and approvals.
- Set retry, timeout, fallback, and halt rules.
- Map observability and eval requirements.
- Prepare downstream implementation handoff when design is stable.

## Outputs

- agent architecture
- state model
- approval map
- tool routing plan
- halt policy

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- agent_type
- state_strategy
- tool_routes
- approval_gates
- halt_policy

## Halt conditions

- Allowed actions, approval gates, or tool permissions are missing.
- Memory or data retention behavior is unclear.
- The architecture would create uncontrolled autonomy or unobservable production behavior.

## Downstream handoffs

- tool-schema-design-desk
- agent-observability-desk
- eval-design-desk
- ai-safety-review-desk
- SDLC Command Desk for implementation

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
