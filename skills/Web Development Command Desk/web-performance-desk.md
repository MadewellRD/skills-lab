---
name: web-performance-desk
description: plan and gate web performance using core web vitals, performance budgets, rendering cost, hydration, bundle size, images, fonts, scripts, cdn, caching, data fetching, latency, field and lab measurement, launch thresholds, and regression controls. use before or after frontend implementation and before release for websites and web apps.
---

# Web Performance Desk


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

Set and enforce performance budgets, rendering strategy, caching rules, asset optimization, and measurement standards for production web delivery.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Routes, page types, device classes, and network classes are independent: budget derivation and cost analysis across them are parallel-safe.
- Continue to `web-testing-qa-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: every budgeted route carries a numeric threshold per metric, lab and field/RUM metrics are labeled separately and never merged, and no measurement is stated as observed unless it comes from a source.

## Responsibilities

- Define performance budgets by route, page type, device, and network class.
- Evaluate rendering, hydration, bundle, script, image, and font cost.
- Plan cache layers, CDN behavior, invalidation, prefetching, and data-fetching strategy.
- Separate lab metrics from field/RUM metrics.
- Align launch readiness with regression thresholds and measurement evidence.

## Expected inputs

- Frontend architecture.
- Backend integration plan.
- Target device/network assumptions.
- Hosting/CDN constraints.
- Existing performance baseline if available.

## Expected outputs

A run delivers all of it: performance budget, optimization plan, measurement plan, launch gate criteria, regression watchlist, and improvement backlog.

The budget is a table with a numeric threshold per metric per budgeted route, not a target for the site as a whole. The optimization plan names the specific cost, meaning this bundle, this font, this third-party script, this waterfall, and the change that reduces it. The measurement plan states which tool produces each number, in which environment, and how often. A budget of "good Core Web Vitals" cannot gate a release and does not count as delivered.

Numbers are the whole substance of this artifact, which is why none of them may be produced from expectation. Where no baseline exists, budgets are marked proposed rather than measured, lab and field figures stay separately labeled, and a route with no measurement is listed as unmeasured. A regression watchlist with nothing observed behind it says so.

## Evidence packet additions

- Budget table.
- Render/data-flow risk notes.
- Asset and caching strategy.
- Measurement definitions.
- Acceptance thresholds and blocker rules.

## Packet fields to update

- LCP, CLS, INP, TTFB, bundle, cache, assets, measurement, thresholds.

## Halt conditions

Halt only on a hard class:

- Release integrity: a performance launch gate would be marked passed without measurement evidence.
- Production or destructive: the next action would change live cache, CDN, or edge configuration.
- Source conflict: baseline measurements, budgets, or hosting behavior genuinely disagree across sources.
- Connector unreachable: the analytics, RUM, or CI performance source needed for measurement evidence cannot be reached.

A missing baseline, unknown device or network mix, and unknown hosting or CDN behavior are not halts. Proceed with budgets stated as proposed rather than measured, label the assumption inline, and record it in `open_questions`. Never state a metric or a regression as observed without a source.

## Default output modes

A complete run produces:

- `web-performance.md`: budgets by route, optimization plan, measurement plan, launch gates, regression watchlist.
- `web-performance-source-facts.md`: every baseline, RUM figure, and hosting or CDN fact with its source and capture context.
- `web-performance-risk-register.md`: regression and budget-breach risks with the route and the change that would cause each.
- `web-performance-downstream-handoff.md`: the thresholds `web-testing-qa-desk` and the release stage enforce.

`connector-diagnostic.md` is the alternative when the analytics, RUM, or CI performance source cannot be reached, not a companion to the set.

Routes, page types, device classes, and network classes are independent per the Workflow section, so budget derivation across these artifacts is parallel-safe.

Filling the set never means filling a cell. An unmeasured metric stays unmeasured in writing, whatever that does to the shape of the table.

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `web-testing-qa-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
