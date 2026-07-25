---
name: tool-schema-design-desk
description: design AI tool schemas, resource contracts, permission boundaries, argument validation, idempotency rules, error semantics, and result contracts for agentic workflows.
---

# Tool Schema Design Desk

## Role

Define safe, deterministic tool interfaces for assistants and agents. Specify schemas, resource contracts, permission boundaries, argument validation, idempotency, destructive action gates, error contracts, and result semantics.

## Use when

- An AI system needs tools, functions, connectors, resources, or external actions.
- A tool contract is ambiguous, over-permissioned, or unsafe.
- An agent needs deterministic tool outputs and error behavior.

## Do not use when

- The task can be solved without external actions or connector access.
- The external API or authorization boundary is unknown.
- The user asks to bypass permission, audit, or approval controls.

## Required evidence

- External API or resource behavior.
- Auth, permission, and tenancy boundaries.
- Allowed and forbidden actions, especially destructive actions.
- Argument schema, validation rules, output shape, and error cases.
- Audit, logging, idempotency, and retry expectations.

## Workflow

Produce tool contracts an implementer can build against without inference: argument and result schema, the permission and tenancy boundary, which actions are destructive and what gates them, and the exact error semantics on every failure.

Constraints:

- Every mutating tool declares its destructive-action gate, approval requirement, and idempotency behavior. A tool that can mutate state without a stated gate is not finished.
- Permission and tenancy boundaries are enforced by the tool and its runtime, never by prompt wording.
- Never invent external API behavior, error codes, rate limits, or auth semantics. Cite the API source or record the behavior as unverified.
- Result contracts are deterministic: same arguments, same shape, with errors modeled rather than returned as prose.
- Label unresolved assumptions inline rather than presenting them as settled contract facts.

Tool schemas are independent. Designing each tool's argument schema, result contract, permission boundary, validation rules, error cases, and test matrix is parallel-safe across tools. The shared auth model, tenancy rule, and audit event format are cross-cutting decisions and are made once.

## Outputs

- tool contract
- schema specification
- permission model
- error contract
- tool test matrix

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- tool_names
- schemas
- permission_boundaries
- approval_gates
- error_contracts

## Halt conditions

Default posture is to proceed and label the assumption inline. An unconfirmed retry count or an undecided field name is a soft gap: state the assumption, mark it, and continue. Halt only when one of the six hard-halt classes applies.

- Approval — a tool can mutate state and no approval policy or approval owner exists for it.
- Production or destructive — the tool would delete, overwrite, dispatch, or otherwise irreversibly act on production systems without a gate in front of it.
- Security or privacy — the auth boundary, tenancy rule, or data exposure surface is unresolved, or the schema would carry secrets, credentials, or personal data.
- Source conflict — API documentation, observed behavior, and stated requirements disagree on what the external system actually does.
- Release integrity — a tool would ship with error semantics or idempotency behavior that cannot be established as correct.
- Connector unreachable — the external API definition, permission model, or existing tool implementation exists but cannot be read.

## Downstream handoffs

- agent-architecture-desk
- ai-safety-review-desk
- red-team-eval-desk
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
- Passing means every tool carries a complete argument and result schema, a stated permission and tenancy boundary, an explicit destructive-action gate where it mutates state, modeled error cases, and a test matrix — each traced to a source fact or a labeled assumption.
