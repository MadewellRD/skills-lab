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

- Classify tool purpose and risk.
- Design argument and result schema.
- Define permission and approval boundaries.
- Specify validation, errors, retries, idempotency, and audit events.
- Map tool tests and failure cases.

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

- External system behavior or auth boundary is unclear.
- The tool can mutate state but approval policy is missing.
- Data exposure or tenancy rules are unresolved.

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
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
