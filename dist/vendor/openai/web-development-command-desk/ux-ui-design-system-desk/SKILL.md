---
name: ux-ui-design-system-desk
description: define ux/ui design system guidance for web surfaces including component inventory, responsive behavior, design tokens, interaction states, accessibility-aware patterns, brand consistency, and design governance. use before frontend implementation or design-system refactor work for websites, web apps, dashboards, portals, landing pages, and ecommerce surfaces.
---

# UX UI Design System Desk


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

Define the experience model, component system, responsive behavior, interaction states, and brand-safe interface patterns for web delivery.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Components and breakpoints are independent: component-by-component inventory and per-breakpoint responsive behavior are parallel-safe.
- Continue to `backend-integration-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: every component in the inventory has its variants and interaction states covered (default, hover, focus, active, disabled, loading, empty, error, success), responsive behavior is defined at each named breakpoint, and token usage is stated as a rule rather than a per-screen exception.

## Responsibilities

- Create or extend the design system.
- Define component inventory, reuse rules, variants, and state coverage.
- Specify responsive layout behavior and breakpoints.
- Capture motion, empty, loading, error, success, and validation states.
- Align visual language with brand, accessibility, frontend, and content constraints.

## Expected inputs

- Requirements and IA outputs.
- Brand guidelines, existing design system, screenshots, component library, or CSS framework.
- Target device mix and accessibility requirements.
- Frontend framework constraints.

## Expected outputs

Design-system plan, component inventory, token guidance, responsive patterns, interaction-state matrix, design debt, implementation handoff notes.

## Evidence packet additions

- Component map.
- Token and theme guidance.
- Responsive pattern library.
- State matrix.
- Design debt and governance notes.

## Packet fields to update

- Components, tokens, responsive rules, interaction states, design debt.

## Halt conditions

Halt only on a hard class:

- Source conflict: component, token, or brand rules genuinely disagree and no owner decision resolves them.
- Missing approval: a brand-governed change needs signoff that has not been given.
- Connector unreachable: the brand guideline, design file, or component library needed as evidence cannot be reached.

A missing design baseline, unknown device mix, or unstated accessibility constraint is not a halt. Proceed against the packet default (WCAG 2.2 AA unless source facts require another standard), label the assumption inline, and record it in `open_questions`.

## Default output modes

- `ux-ui-design-system.md`
- `ux-ui-design-system-source-facts.md`
- `ux-ui-design-system-risk-register.md`
- `ux-ui-design-system-downstream-handoff.md`
- `connector-diagnostic.md`

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `backend-integration-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
