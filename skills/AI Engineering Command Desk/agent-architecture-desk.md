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

Produce a bounded control architecture: the level of agency the task actually requires, the loop and state model that supports it, the tools the agent may reach, where a human must approve, and what happens on every failure path.

Constraints:

- Choose the least agency that satisfies the goal. Autonomy is added against evidence, never by default.
- Approval gates, destructive-action boundaries, and tool permissions are runtime controls, not prompt wording. Never place a control in natural language that belongs in the runtime.
- Every tool route states its retry, timeout, fallback, and halt behavior.
- Memory, state, and retention behavior are explicit, including what persists and for how long.
- Label unresolved assumptions inline rather than presenting them as settled design facts.

Once the agency level is fixed, per-tool-route design; schema boundary, permission, retry, timeout, and failure semantics for each route; is parallel-safe across routes, as is per-failure-mode analysis. The agency classification and the shared state model are single decisions and are not.

## Outputs

One run delivers the whole design, not a piece of it. All five ship together:

- agent architecture: agency level, loop structure, decomposition into agents or steps, and the reason each boundary sits where it does. Complete when someone could implement the control flow from it without asking what happens between steps.
- state model: what is held, where, for how long, what survives a restart, and what is deliberately not persisted.
- approval map: every action requiring human authorization, who authorizes it, and what the agent does while it waits.
- tool routing plan: per route: which tool, under what condition, with what permission, timeout, retry, and failure behavior.
- halt policy: the conditions that stop the loop, and the state the agent leaves behind when it stops.

Each is done when a competent implementer could act on it without a follow-up round trip. A heading with nothing under it is an incomplete artifact, not a draft. Because routes and failure modes are already parallel-safe, the per-route sections and the per-failure-mode entries of the halt policy develop concurrently rather than in sequence.

Delivering the full set never means filling a gap with plausible text. Where no source establishes a tool's permission boundary, an owner for an approval gate, or an existing state store, that entry is recorded as unknown or blocked with the missing evidence named, never as an invented route, owner, or limit.

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

Default posture is to proceed and label the assumption inline. An unset timeout value or an unnamed observability owner is a soft gap: state the assumption, mark it, and continue. Halt only when one of the six hard-halt classes applies.

- Approval: the design would grant the agent an action the owner has not authorized, or no approval owner exists for a high-impact action.
- Production or destructive: the agent could mutate, delete, or dispatch against production systems without a gate in front of it.
- Security or privacy: the design would expose secrets, credentials, cross-tenant data, or personal data to the model, a tool, or a memory store.
- Source conflict: tool contracts, permission documentation, and stated requirements disagree on what the agent is actually allowed to do.
- Release integrity: the architecture would ship autonomy whose behavior cannot be observed or evaluated in production.
- Connector unreachable: tool contracts, permission definitions, or runtime configuration exist but cannot be read.

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
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means a reader can name the agency level and its justification, every tool route with its permission and failure behavior, every approval gate, the state and retention model, and the halt policy, each traced to a source fact or a labeled assumption.
