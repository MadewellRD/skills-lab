---
name: frontend-engineering-desk
description: create implementation-ready frontend engineering plans for web surfaces including rendering strategy, routing, layouts, components, state, forms, data fetching, framework constraints, accessibility hooks, performance controls, and coding-agent handoffs. use for react, next.js, vue, svelte, static site, spa, ssr, ssg, hybrid, dashboard, portal, and landing page work.
---

# Frontend Engineering Desk


## Suite workflow mode

This desk is part of the Web Development Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, update the `web_delivery_packet`, and continue to the next stage when enough source facts are available.

If required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Do not invent repo state, business goals, audiences, routes, content models, owners, compliance requirements, performance budgets, release dates, telemetry, or deployment facts.

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

1. Classify the request and target surface.
2. Run connector preflight for repo, docs, product, design, analytics, or operational facts relevant to this stage.
3. Build source facts and separate assumptions from verified evidence.
4. Produce this desk's artifact and update the `web_delivery_packet`.
5. Continue to `web-security-secops-desk` when the packet is ready and the target outcome requires additional downstream work.
6. Halt only when required source facts, approvals, or connector access are missing.

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

- No target repo/framework for implementation handoff.
- Missing accepted requirements or component scope.
- Unknown API/auth contracts for data-heavy surfaces.

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
