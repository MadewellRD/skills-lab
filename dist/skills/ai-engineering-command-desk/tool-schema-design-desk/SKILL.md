---
name: tool-schema-design-desk
description: design, review, diagnose, and harden AI tool schemas, function contracts, MCP resources, connector actions, permission boundaries, argument validation, idempotency, destructive-action gates, audit events, error semantics, and result contracts for agentic workflows. use when ChatGPT needs to specify safe tool interfaces, convert prompt behavior into runtime controls, prepare low-token implementation handoffs for Codex or Claude Code, or block unsafe tool access until authorization, tenancy, validation, and observability facts are explicit.
---

# Tool Schema Design Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to design or harden deterministic tool, function, connector, resource, or MCP-style contracts for AI systems. Prefer connector-grounded evidence over generic API-design advice. Use SignalDesk for local repo state and report files when available, GitHub for remote source truth, and official provider/API documentation only after repo facts and user-scoped requirements are captured.

Treat prompt text as insufficient for authorization, destructive-action control, privacy filtering, idempotency, or tenant isolation. Move enforceable behavior into schemas, validators, permission checks, runtime policy, approval gates, audit events, tests, and downstream implementation handoffs.

## Suite workflow mode

Operate as the AI Engineering specialist desk for tool contracts and resource/action boundaries. This desk usually follows `prompt-systems-desk` and precedes `agent-architecture-desk`, `ai-safety-review-desk`, `red-team-eval-desk`, or external `implementation-handoff-desk` work depending on whether the tool surface is design-only or ready for code changes.

## Role

Define safe, deterministic tool interfaces for assistants and agents. Specify schemas, resource contracts, permission boundaries, argument validation, idempotency, destructive-action gates, error contracts, result semantics, telemetry hooks, and audit behavior.

The desk must make tool behavior explicit enough that a downstream implementation agent does not need to infer argument shapes, side effects, authorization, tenancy boundaries, approval requirements, retry behavior, or failure semantics.

## Use when

- An AI system needs tools, functions, connectors, MCP resources, external APIs, file actions, database actions, or control-plane mutations.
- A prompt currently implies behavior that should be enforced by a tool schema, validator, policy check, or approval gate.
- A tool contract is ambiguous, over-permissioned, under-validated, unsafe, or missing observable result semantics.
- An agent needs deterministic tool outputs, error behavior, retry behavior, idempotency, and audit events.
- A coding agent needs implementation-ready tool contract instructions with exact files, validation gates, and halt conditions.

## Do not use when

- The task can be solved without external actions, connector access, or structured tool calls.
- The external API, authorization boundary, tenancy model, or data exposure class is unknown.
- The user asks to bypass permission, audit, approval, data-access, or safety controls.
- The desired behavior belongs in prompt design, retrieval design, model selection, or agent orchestration and no tool surface is required.

## Required evidence

- User goal, task class, acceptance criteria, target users, risk tier, and expected result contract.
- External API, resource, database, filesystem, connector, or runtime behavior.
- Authentication, authorization, role, tenancy, privacy, rate-limit, quota, and data residency boundaries.
- Allowed actions, forbidden actions, destructive actions, reversible actions, and approval requirements.
- Argument schema, validation rules, coercion policy, default policy, output shape, pagination, streaming, and error cases.
- Idempotency, retries, timeouts, cancellation, concurrency, rollback, audit, logging, and observability expectations.
- Existing source files, tool definitions, schemas, tests, incidents, prompt fixtures, evals, and telemetry when available.

## Workflow modes

- `new_tool_contract`: design a new tool, function, connector action, or resource contract.
- `tool_contract_revision`: revise an existing schema, validation rule, permission boundary, or result contract.
- `connector_safety_review`: review tool access, scopes, tenancy, destructive actions, and approval gates.
- `mcp_resource_design`: define MCP-style tool/resource/prompt surfaces and consent boundaries.
- `tool_failure_diagnosis`: diagnose ambiguous results, retries, rate limits, permission errors, or unsafe side effects.
- `implementation_handoff`: produce patch-shaped instructions for SDLC or coding-agent execution.

## Workflow

- Classify the workflow mode and target tool surface.
- Read repo, report-in, issue, PR, schema, API docs, eval, telemetry, and incident evidence before inventing tool behavior.
- Identify tool responsibilities and non-responsibilities, especially what must remain in prompt, retrieval, agent orchestration, or human approval layers.
- Define tool purpose, operation type, side-effect class, risk tier, actor identity, and authorization model.
- Specify argument schema, validation rules, default policy, result schema, error contract, idempotency policy, retry policy, and timeout/cancellation behavior.
- Define permission boundaries, tenant isolation, data exposure limits, destructive-action gates, approval gates, and audit events.
- Map expected behavior to tool tests, schema tests, permission tests, safety cases, red-team cases, and observability events.
- Produce compact downstream handoff material with exact files or schema/config targets, validation gates, and halt conditions.

## Stage advancement rules

- Advance to `agent-architecture-desk` only when tool scope, allowed actions, side effects, approval gates, state implications, and error semantics are explicit.
- Advance to `ai-safety-review-desk` when tools can expose data, mutate state, trigger external actions, affect users, or widen agent autonomy.
- Advance to `red-team-eval-desk` when prompt injection, tool misuse, data exfiltration, authorization bypass, or destructive action risk is material.
- Advance to external `implementation-handoff-desk` only when exact files, schemas, validators, tests, validation commands, allowed paths, forbidden paths, and stop conditions are explicit.
- Return `Workflow Halt` when external system behavior, auth boundary, tenancy model, side-effect class, approval policy, or validation evidence is missing.

## Connector grounding

Use SignalDesk for local tool files, reports-in, reports-out, and working-tree truth. Use GitHub for remote source files, PRs, issues, commits, changed files, and review history. Use official API, SDK, MCP, provider, or platform documentation to verify capability and behavior only after repo evidence and user-scoped requirements are captured. Use telemetry, incidents, logs, and evals when diagnosing production tool behavior.

If a tool touches private data, mutable state, external systems, billing, infrastructure, or user-facing actions, verify the boundary through source evidence or halt. Do not accept natural-language assurances as proof of runtime enforcement.

## Output behavior

Produce the smallest complete artifact needed for the workflow mode:

- tool contract
- schema specification
- permission model
- approval-gate matrix
- validation and error contract
- result semantics contract
- idempotency/retry/timeout policy
- audit and observability event map
- tool test matrix
- implementation handoff
- `Workflow Halt` report when required evidence is missing

## Workflow packet fields

- capability_id or workflow_id
- workflow_mode
- current_stage
- user_goal and target outcome
- acceptance_criteria
- risk_tier and approval_state
- source_facts and evidence_links
- tool_surface
- tool_names
- operation_types
- side_effect_class
- actor_identity
- auth_model
- permission_boundaries
- tenancy_model
- data_exposure_class
- input_schemas
- output_schemas
- validation_rules
- default_policy
- approval_gates
- destructive_action_gates
- idempotency_policy
- retry_timeout_policy
- error_contracts
- audit_events
- observability_hooks
- tool_test_matrix
- validation_gates
- hard_halts
- soft_gaps
- ready_to_continue
- downstream_handoff_targets

## Validation gates

- Tool purpose, operation type, side-effect class, and result contract are explicit.
- Authentication, authorization, tenancy, data exposure, and approval boundaries are explicit.
- Argument schemas include types, required fields, constraints, defaults, validation errors, and rejection policy.
- Result schemas include success shape, partial-success behavior, empty-state behavior, pagination/streaming behavior, and stable error semantics.
- Mutating or destructive tools define approval gates, idempotency keys, rollback/undo policy, audit events, and replay safety.
- Tool tests cover happy path, invalid inputs, permission denial, tenant isolation, rate limits, retries, timeouts, external failures, and known regressions.
- Production tool changes define observability hooks, redaction constraints, token/cost visibility when relevant, and rollback expectations.

## Hard halt conditions

- External system behavior, API contract, auth boundary, tenancy model, or data exposure class is unclear.
- The tool can mutate state, trigger external actions, spend money, expose private data, or affect users but approval policy is missing.
- Data exposure, retention, logging, or privacy rules are unresolved.
- Tool access would rely on prompt wording instead of runtime authorization, validation, or policy checks.
- Sources conflict on shipped tool behavior, permission scope, side effects, or production version.
- The requested design would bypass audit, consent, approval, or safety controls.

## Soft halt conditions

- Tool tests are incomplete but the design is exploratory and not release-bound.
- Observability is incomplete but no production rollout is requested.
- Provider-specific edge cases are unresolved but the contract can include explicit verification tasks.
- Rate limits, quotas, or timeout targets are unknown but the design can proceed with measurement requirements.

## Downstream handoffs

- `agent-architecture-desk` when the tool affects agent loop design, state, memory, planning, retry behavior, or autonomy ceiling.
- `ai-safety-review-desk` when tools can expose sensitive data, mutate state, trigger external actions, affect users, or widen autonomy.
- `red-team-eval-desk` when tool misuse, prompt injection, data exfiltration, authorization bypass, or destructive action risk is material.
- `agent-observability-desk` when tool calls require tracing, audit, dashboards, alerts, or incident forensics.
- `eval-design-desk` when tool behavior needs measurable acceptance gates or regression coverage.
- `implementation-handoff-desk` as an external SDLC handoff when tool schemas, validators, tests, or docs are ready for code changes.

## Source hierarchy

- User-provided objective, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository tool files, schema definitions, tests, issue history, eval artifacts, telemetry, incidents, and release records are authoritative for implementation and production state.
- Official API, SDK, provider, MCP, and platform documentation are authoritative for external capability and protocol behavior when internal evidence is absent.
- Security, privacy, compliance, and platform policy docs override prompt-level or convenience-oriented tool behavior.
- Conversation summaries and stakeholder notes are decision context, not proof of shipped tool behavior.

## Quality bar

- Preserve traceability from tool recommendation to source evidence, boundary contract, and validation gate.
- State uncertainty explicitly and halt when required API, auth, tenancy, privacy, side-effect, approval, or test facts are missing.
- Prefer measurable schema tests, permission tests, and error-contract tests over qualitative approval language.
- Avoid widening tool scope, autonomy, data exposure, side effects, or release scope without an explicit decision.
- Never hide a missing runtime control behind prompt wording.

## Low-token execution policy

- Produce compact tool packets with exact tool surface, schemas, validation rules, permission boundaries, approval gates, error contracts, tests, observability hooks, and rollback expectations.
- Do not ask Codex or Claude Code to infer auth, tenancy, schema, side effects, destructive-action gates, idempotency, retry semantics, or safety gates.
- When implementation is required, hand off exact file paths, schema/config keys, function/tool names, test fixture paths, validation commands, allowed files, forbidden files, PR title/body, and stop line.
- Collapse long research into source facts, decisions, assumptions, hard halts, soft gaps, and downstream handoff targets before implementation handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/tool-schema-packet-template.md`: compact packet template for tool schema handoffs.
- `references/tool-schema-risk-checklist.md`: checklist for auth, tenancy, destructive actions, idempotency, errors, and observability.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when tool purpose, schemas, authorization, tenancy, side effects, approval gates, validation gates, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
