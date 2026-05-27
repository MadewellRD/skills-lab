---
name: site-product-requirements-desk
description: create web-specific product requirements, page and route scope, user journeys, acceptance criteria, success metrics, analytics intent, source facts, risks, open questions, and downstream handoff notes for websites, web apps, landing pages, portals, dashboards, docs sites, ecommerce surfaces, and admin ui work. use before information architecture, design, engineering, testing, release, or growth work when scope is not already accepted.
---

# Site Product Requirements Desk


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

Translate business goals into web-specific scope, user journeys, page/screen requirements, acceptance criteria, content needs, and measurable success outcomes.

## Workflow

1. Classify the request and target surface.
2. Run connector preflight for repo, docs, product, design, analytics, or operational facts relevant to this stage.
3. Build source facts and separate assumptions from verified evidence.
4. Produce this desk's artifact and update the `web_delivery_packet`.
5. Continue to `information-architecture-desk` when the packet is ready and the target outcome requires additional downstream work.
6. Halt only when required source facts, approvals, or connector access are missing.

## Responsibilities

- Clarify business goals, target users, and conversion or operational outcomes.
- Define target surface, page types, routes, screens, and high-value flows.
- Capture content, integration, security, accessibility, SEO, analytics, and performance needs early.
- Separate launch scope from later phases.
- Preserve source facts and mark assumptions explicitly.

## Expected inputs

- Business brief or raw idea.
- Audience, persona, market, customer, or stakeholder notes.
- Existing site/app context, repo links, issues, screenshots, or docs.
- Content inventory or content gaps.
- Timeline, stack, compliance, and launch constraints.

## Expected outputs

Requirements packet, page or screen inventory, user journey map, acceptance criteria matrix, success metrics, analytics event candidates, scope exclusions, open questions.

## Evidence packet additions

- Accepted goal and non-goals.
- Route/page/screen inventory.
- Primary journeys and acceptance criteria.
- Success metrics and analytics intent.
- Content, design, integration, and compliance dependencies.

## Packet fields to update

- Business goal, audience, target surface, scope, acceptance criteria, analytics intent.

## Halt conditions

- Missing business goal or target audience.
- No source for launch scope or accepted success metric.
- Conflicting requirements with no decision owner.

## Default output modes

- `site-product-requirements.md`
- `site-product-requirements-source-facts.md`
- `site-product-requirements-risk-register.md`
- `site-product-requirements-downstream-handoff.md`
- `connector-diagnostic.md`

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `information-architecture-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
