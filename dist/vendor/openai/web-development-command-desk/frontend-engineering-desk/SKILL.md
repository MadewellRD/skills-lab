---
name: frontend-engineering-desk
description: create implementation-ready frontend engineering plans for web surfaces including rendering strategy, routing, layouts, components, state, forms, data fetching, framework constraints, accessibility hooks, performance controls, and coding-agent handoffs. use for react, next.js, vue, svelte, static site, spa, ssr, ssg, hybrid, dashboard, portal, and landing page work.
---

# Frontend Engineering Desk


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

Turn approved web requirements into implementation-ready frontend architecture, component plans, rendering strategy, state/data decisions, and developer handoff.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Routes, pages, and components are independent: per-route rendering decisions and per-component implementation plans are parallel-safe.
- Continue to `web-security-secops-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: every in-scope route has a rendering decision and a data-fetching path, every planned component maps to a design-system entry, and a coding agent can execute the plan without rediscovering framework, routing, or contract facts.

## Responsibilities

- Choose or validate rendering approach: SSR, SSG, ISR, SPA, MPA, edge, or hybrid.
- Define routing, layout, component, and module boundaries.
- Plan state management, forms, validation, and data fetching.
- Align API usage and error handling with backend contracts.
- Translate design-system rules into implementation structure and coding-agent instructions.

## Expected inputs

- Requirements, IA, design-system, and backend integration outputs.
- Repo/framework/package facts.
- Non-functional requirements.
- Performance, accessibility, SEO, and testing constraints.

## Expected outputs

Frontend architecture brief, rendering strategy, component implementation plan, route/layout map, state and data-flow notes, engineering handoff packet.

## Evidence packet additions

- Component tree.
- Route/layout map.
- Rendering decision record.
- State/data-flow notes.
- Implementation risks and validation commands.

## Packet fields to update

- Framework, routes, components, rendering, state, data fetching, validation.

## Halt conditions

Halt only on a hard class:

- Security or privacy: an authenticated or data-sensitive surface would be planned against auth, session, or token behavior that has no source.
- Source conflict: repo state, framework configuration, and design or requirement docs genuinely disagree on a load-bearing implementation fact.
- Missing approval: the handoff would authorize a coding agent to act beyond accepted scope.
- Connector unreachable: the target repo cannot be reached, so framework, routing, and package facts are unavailable rather than merely absent.

An unnamed target repo or framework, unaccepted component scope, or an unsourced contract for a non-sensitive API is not a halt. Proceed with the assumption labeled inline and recorded in `open_questions`, and never present assumed repo state as fact.

## Default output modes

- `frontend-engineering.md`
- `frontend-engineering-source-facts.md`
- `frontend-engineering-risk-register.md`
- `frontend-engineering-downstream-handoff.md`
- `connector-diagnostic.md`

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `web-security-secops-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
