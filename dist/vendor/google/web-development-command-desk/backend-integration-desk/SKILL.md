---
name: backend-integration-desk
description: plan web backend integration across api contracts, auth, sessions, bff layers, cms connections, data models, caching, rate limits, pagination, failure modes, and ownership. use when a web surface depends on services, databases, third-party systems, identity, forms, crm, ecommerce, analytics, or internal APIs.
---

# Backend Integration Desk


## Suite workflow mode

This desk is part of the Web Development Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, update the `web_delivery_packet`, and continue to the next stage when enough source facts are available.

Return `Workflow Halt` only for a hard-halt class: a required human approval is missing, the next action is production-affecting or destructive, there is a security or privacy exposure, sources genuinely conflict on a load-bearing fact, release integrity would be asserted without evidence, or a required connector is unreachable. Include specific resume requirements. For every other gap, proceed and label the assumption inline in the artifact so it stays auditable and cheap to correct. Do not invent repo state, business goals, audiences, routes, content models, owners, compliance requirements, performance budgets, release dates, telemetry, or deployment facts.

## Shared web delivery packet

Preserve and update this packet shape across stages:

```yaml
web_delivery_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  current_stage: "stage-name"
  completed_stages:
    - "stage-name"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  target_surface: "website | web_app | landing_page | portal | dashboard | docs_site | ecommerce | admin_ui | unknown"
  business_goal: "source-backed goal or unknown"
  audience_segments: []
  content_model: []
  routes_pages: []
  user_flows: []
  design_system_requirements: []
  frontend_stack: []
  backend_integrations: []
  security_controls: []
  performance_budgets: []
  accessibility_standard: "WCAG 2.2 AA unless source facts require another standard"
  seo_requirements: []
  analytics_events: []
  test_matrix: []
  deployment_target: []
  observability_requirements: []
  release_gates: []
  rollback_plan: []
  source_facts:
    - fact: "source-backed fact"
      source: "github | docs | user | connector | uploaded_file | unknown"
  decisions:
    - "decision made at this stage"
  open_questions:
    - "question blocking later work"
  artifacts:
    - "artifact name or path"
  halt_conditions:
    - "condition that requires stopping"
  ready_to_continue: true
```

## Connector grounding

Treat GitHub as source of truth for repository state, branches, commits, pull requests, issues, workflows, files, dependencies, tests, configuration, and deployment manifests. Treat product docs, design docs, analytics notes, roadmaps, and uploaded files as source of truth for product, content, brand, design, policy, business, and stakeholder context. Treat communication sources as decision context, not as repo-state truth.

## Output behavior

For multi-stage workflows, return a concise stage-by-stage report or a reusable Markdown artifact. Include completed stages, skipped stages with reasons, source facts, decisions, open questions, halt conditions, the current `web_delivery_packet`, and the next continuation target.


## Role

Define how the web surface connects to backend services, APIs, auth systems, data models, caching layers, third-party systems, and failure handling.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Endpoints, services, and third-party integrations are independent: contract, failure-mode, and ownership analysis across them is parallel-safe.
- Continue to `frontend-engineering-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: every integration the surface depends on has a named owner, a request/response contract, defined error and degraded-state behavior, and an auth/session boundary, each either sourced or labeled as an assumption.

## Responsibilities

- Clarify service boundaries and ownership.
- Define API contracts, payloads, validation, and error behavior.
- Establish auth/session/role requirements and browser storage rules.
- Identify caching, pagination, rate-limit, idempotency, and consistency assumptions.
- Plan degraded states and reduce frontend/backend coupling.

## Expected inputs

- Requirements packet.
- IA and frontend plans.
- API docs, service docs, schema notes, auth constraints, data models, and third-party inventories.
- Performance and security requirements.

## Expected outputs

A complete run delivers the whole list, not the most convenient item on it: integration map, API contract checklist, auth/session requirements, failure-mode plan, caching and data-consistency notes, and backend dependency risks.

Depth is what makes these usable. A contract entry states method, path, request and response shape, status codes, and validation rules, enough that a frontend engineer can code against it. The failure-mode plan says what the surface renders on timeout, 4xx, 5xx, partial data, and empty state, per integration. "Handle errors gracefully" is not a failure-mode plan.

An integration whose contract nothing in the sources describes gets listed with its gap named, not with a contract reconstructed from convention. An invented endpoint shape is worse than an acknowledged unknown, because the next stage will build against it.

## Evidence packet additions

- Integration inventory.
- Request/response contract notes.
- Auth/session boundaries.
- Failure-state matrix.
- Dependency and ownership map.

## Packet fields to update

- APIs, auth, data contracts, cache rules, failure states, ownership.

## Halt conditions

Halt only on a hard class:

- Security or privacy: an integration touches credentials, secrets, tokens, or personal data and continuing would require asserting auth, session, or exposure behavior that has no source.
- Production or destructive: the next action would write to, migrate, or mutate a production data store or a live third-party system.
- Source conflict: API docs, schema, and repo state genuinely disagree on a load-bearing contract.
- Connector unreachable: the repo, API docs, or schema source needed for contract evidence cannot be reached.

An unknown dependency owner, or an unsourced contract for a non-sensitive integration, is not a halt. Proceed with the contract labeled as an assumption inline and recorded in `open_questions`.

## Default output modes

One run produces the set:

- `backend-integration.md`: integration map, contracts, auth and session boundaries, failure modes, caching rules.
- `backend-integration-source-facts.md`: each contract, schema, and auth fact with the repo path, doc, or spec it came from.
- `backend-integration-risk-register.md`: coupling, ownership, rate-limit, consistency, and dependency-availability risks with impact and the evidence behind each.
- `backend-integration-downstream-handoff.md`: what `frontend-engineering-desk` needs in order to consume the contracts without rediscovering them.

`connector-diagnostic.md` stands in place of that set rather than joining it, and only when the repo, API docs, or schema source cannot be reached at all.

Endpoints and services are independent, so these artifacts are part of the parallel surface named in the Workflow section.

Delivering all four does not authorize filling one. A contract, an owner, or a rate limit that no source establishes is recorded as unknown in the artifact and as an open question in the packet, never written in because a table had a blank cell.

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `frontend-engineering-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
