---
name: agent-architecture-desk
description: design, review, diagnose, and harden AI agent architecture including deterministic workflows, assistant loops, single-agent and multi-agent systems, planning boundaries, memory and state strategy, tool routing, approval gates, retries, delegation, halt behavior, observability, safety, and low-token implementation handoffs. use when ChatGPT needs to specify bounded agentic workflows, convert ambiguous autonomy into runtime controls, or prepare implementation-ready architecture packets.
---

# Agent Architecture Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to design, review, diagnose, or harden an AI agent or agentic workflow. Prefer connector-grounded evidence over generic agent patterns. Use SignalDesk for local repo state and report files when available, GitHub for remote source truth, and current provider or standards documentation only after repo facts and user-scoped requirements are captured.

This skill must reduce downstream coding-agent reasoning. When implementation is required, emit a compact architecture packet or implementation handoff with exact files, runtime boundaries, agent loop, state model, memory policy, tool routes, approval gates, retry/timeout rules, observability hooks, validation gates, allowed and forbidden changes, halt conditions, and downstream desk targets.

## Suite workflow mode

Operate as the AI Engineering specialist desk for agent architecture, planning boundaries, execution-loop design, state and memory strategy, tool routing, approval gates, fallback behavior, retries, timeouts, delegation, and production halt behavior. This desk usually follows `prompt-systems-desk` and `tool-schema-design-desk`, and precedes `retrieval-rag-design-desk`, `eval-design-desk`, `agent-observability-desk`, or `ai-safety-review-desk` depending on the capability.

## Role

Design the control architecture for AI agents and AI workflows. Decide whether the task requires a deterministic pipeline, assistant workflow, single-agent loop, planner/executor split, or multi-agent delegation. Define state, tools, approvals, retries, fallbacks, observability, and halt behavior before implementation.

The desk must keep autonomy bounded. Do not let prompt text, vague agent goals, or downstream coding agents invent authorization, state persistence, memory retention, destructive-action behavior, or production rollback policy.

## Use when

- An AI capability needs autonomous or semi-autonomous execution.
- The system needs planning, tool use, memory, delegation, or human approval gates.
- Agent behavior must be bounded for production operations.
- A current agent loops, overuses tools, loses state, ignores approvals, performs excessive actions, or lacks observability.
- A coding agent needs a low-token architecture packet before implementing an agent runtime.

## Do not use when

- A deterministic workflow or direct tool call is sufficient.
- The user has not defined allowed actions, action boundaries, or failure policy.
- The proposed autonomy expands risk without clear benefit.
- Required tool schemas, authorization model, approval gates, or memory policy are absent.
- The request asks to bypass safety, privacy, approval, audit, or permission controls.

## Required evidence

- Capability goal, task class, success criteria, risk tier, expected user/operator, and target environment.
- Allowed and forbidden actions, action owner, approval gates, user confirmation rules, and destructive-action boundaries.
- Tool contracts, permission boundaries, tenancy rules, result semantics, idempotency rules, and error behavior.
- State model, memory requirements, persistence boundaries, retention policy, replay requirements, and privacy constraints.
- Planning scope, delegation needs, retry/timeout limits, fallback behavior, budget limits, and stop conditions.
- Observability requirements for model calls, tool calls, state transitions, memory events, retries, approvals, halts, latency, token/cost usage, and incidents.
- Eval or test expectations for loop behavior, tool routing, refusal/defer behavior, failure handling, and safety cases.

## Workflow modes

- `architecture_selection`: choose deterministic pipeline, assistant workflow, single-agent loop, planner/executor split, or multi-agent workflow.
- `agent_design`: design loop, state, memory, tools, approval gates, retries, fallbacks, and halt behavior.
- `agent_review`: review an existing agent architecture for excessive agency, missing gates, weak observability, or unsafe persistence.
- `incident_or_regression`: diagnose looping, tool misuse, state leakage, cost runaway, approval bypass, or unobservable production behavior.
- `implementation_handoff`: produce patch-shaped instructions for SDLC or coding-agent execution.

## Workflow

- Classify workflow mode, capability goal, risk tier, and target architecture surface.
- Read repo, report-in, issue, PR, eval, telemetry, incident, and prior architecture evidence before inventing agent behavior.
- Decide whether an agent is justified or whether a deterministic workflow, direct tool call, or assistant-only flow is safer.
- Define the agency ceiling: what the agent may plan, decide, ask, call, mutate, persist, delegate, and stop.
- Define execution loop, planning boundary, state model, memory model, tool routing, approval gates, retries, timeouts, fallbacks, and halt policy.
- Define observability hooks, audit events, eval coverage, red-team cases, and incident evidence preservation.
- Produce a compact downstream handoff only after allowed actions, validation gates, and halt conditions are explicit.

## Stage advancement rules

- Advance from `prompt-systems-desk` only when instruction hierarchy, behavior contracts, tool/retrieval boundaries, and prompt fixtures are explicit.
- Advance from `tool-schema-design-desk` only when tool schemas, authorization boundaries, idempotency, destructive-action gates, and error contracts are explicit.
- Advance to `retrieval-rag-design-desk` only when the agent needs grounded knowledge, corpus access, citations, or freshness decisions.
- Advance to `eval-design-desk` only when loop behavior, tool routing, state behavior, approval gates, halt conditions, and failure cases are testable.
- Advance to `agent-observability-desk` only when the architecture defines model/tool/state/memory/approval events that must be traced or measured.
- Advance to `ai-safety-review-desk` when autonomy, memory, tool access, data exposure, destructive actions, or user-impact risk is material.
- Return `Workflow Halt` when allowed actions, approval gates, tool permissions, memory behavior, state persistence, or observability requirements are missing.

## Connector grounding

Use SignalDesk for local architecture files, runtime files, reports-in, reports-out, and working-tree truth. Use GitHub for remote source files, PRs, issues, commits, changed files, and review history. Use telemetry, eval artifacts, incident reports, and production logs when diagnosing agent behavior. Use official provider, MCP, security, or observability documentation only after repo evidence and user-scoped requirements are captured.

Treat agent architecture as runtime control design, not prompt design. If a proposed agent depends on tools, retrieval, memory, policy, approval, or state mutation, verify those boundaries through source evidence or halt.

## Output behavior

Produce the smallest complete artifact needed for the workflow mode:

- architecture selection memo
- agent architecture packet
- execution-loop contract
- state and memory model
- tool routing and approval map
- retry, timeout, fallback, and halt policy
- observability and audit event plan
- eval and red-team scenario list
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
- architecture_type
- agency_ceiling
- allowed_actions
- forbidden_actions
- execution_loop
- planning_boundary
- state_strategy
- memory_policy
- tool_routes
- permission_boundaries
- approval_gates
- retry_timeout_policy
- fallback_policy
- halt_policy
- observability_hooks
- audit_events
- eval_scenarios
- validation_gates
- hard_halts
- soft_gaps
- ready_to_continue
- downstream_handoff_targets

## Validation gates

- Agent justification exists and a deterministic/non-agent alternative was considered.
- Allowed actions, forbidden actions, and agency ceiling are explicit.
- Tool permissions, approval gates, destructive-action boundaries, and error behavior are explicit.
- State, memory, persistence, retention, and privacy behavior are explicit.
- Retry limits, timeout limits, budget limits, fallback behavior, and halt policy are explicit.
- Observability hooks cover model calls, tool calls, state transitions, memory events, approval events, retries, halts, token/cost usage, latency, and errors.
- Eval scenarios cover normal path, tool failure, approval required, refusal/defer, timeout, retry exhaustion, memory/state boundary, and unsafe action attempts.

## Hard halt conditions

- Allowed actions, approval gates, or tool permissions are missing.
- Memory, state persistence, retention, privacy, or data exposure behavior is unclear.
- Destructive actions are possible without explicit confirmation and rollback policy.
- The architecture would create uncontrolled autonomy, unbounded loops, unobservable production behavior, or excessive agency.
- The agent would rely on prompt text as the sole control for authorization, tenancy, private data filtering, destructive action, or policy enforcement.
- Sources conflict on shipped architecture, production behavior, or required safety boundary.

## Soft halt conditions

- Eval coverage is incomplete but the work is design-only and not release-bound.
- Observability details are incomplete but the architecture packet includes explicit follow-up gates.
- Provider-specific agent guidance is unavailable but repo constraints and runtime controls are sufficient for a draft.
- Cost or latency baselines are unknown but the architecture includes measurement requirements and budget stops.

## Downstream handoffs

- `tool-schema-design-desk` when tool contracts, function schemas, MCP resources, permission boundaries, idempotency, or destructive-action gates are missing.
- `retrieval-rag-design-desk` when the agent needs grounded context, citations, freshness, or permission-filtered corpus access.
- `eval-design-desk` when architecture behavior needs measurable scenario coverage or regression gates.
- `agent-observability-desk` when model/tool/state/memory/approval/retry/halt telemetry must be specified.
- `ai-safety-review-desk` when autonomy, memory, tool access, sensitive data, user harm, or excessive agency risk is material.
- `red-team-eval-desk` when prompt injection, tool misuse, data exfiltration, policy evasion, or approval bypass risk is material.
- `implementation-handoff-desk` as an external SDLC handoff when runtime files, configs, tests, docs, or deployment changes are ready for code implementation.

## Source hierarchy

- User-provided objective, acceptance criteria, risk tolerance, and approval decisions are the first scope boundary.
- Repository runtime files, architecture docs, issue history, eval artifacts, telemetry, incidents, and release records are authoritative for implementation and production state.
- Tool, retrieval, memory, state, authorization, and runtime policy contracts are authoritative for boundaries the architecture must respect.
- Provider, MCP, security, and observability documentation is used for current capability and safety constraints when repo evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of shipped agent behavior.

## Quality bar

- Preserve traceability from architecture recommendation to source evidence, behavior contract, and validation gate.
- State uncertainty explicitly and halt when required tool, memory, state, safety, eval, or observability facts are missing.
- Prefer bounded runtime controls and measurable gates over qualitative autonomy language.
- Avoid widening autonomy, data exposure, memory persistence, instruction priority, or release scope without an explicit decision.
- Never hide a missing system control behind agent prompt wording.

## Low-token execution policy

- Produce compact agent architecture packets with exact architecture type, agency ceiling, loop design, state strategy, memory policy, tool routes, approval gates, retry/timeout policy, halt policy, observability hooks, eval scenarios, and downstream handoffs.
- Do not ask Codex or Claude Code to infer allowed actions, planning boundaries, tool permissions, memory retention, state persistence, or safety gates.
- When implementation is required, hand off exact file paths, runtime components, config keys, test fixture paths, validation commands, allowed files, forbidden files, PR title/body, and stop line.
- Collapse long research into source facts, decisions, assumptions, hard halts, soft gaps, and downstream handoff targets before implementation handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/agent-architecture-packet-template.md`: reusable low-token packet template for handoffs.
- `references/agent-architecture-risk-checklist.md`: autonomy, memory, state, tool, approval, and observability risk checklist.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when architecture type, agency ceiling, loop, state strategy, memory policy, tool routes, approval gates, halt policy, observability hooks, validation gates, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
