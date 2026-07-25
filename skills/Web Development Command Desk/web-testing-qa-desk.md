---
name: web-testing-qa-desk
description: define web testing and qa strategy across browsers, devices, responsive layouts, visual regression, forms, auth flows, integrations, accessibility checks, seo checks, performance checks, smoke tests, regression tests, release signoff, and defect triage. use before web release, implementation handoff, qa planning, or verification.
---

# Web Testing QA Desk


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

Define and coordinate browser, device, responsive, integration, accessibility, visual, performance, and release-validation test strategy for the web surface.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Browsers, devices, viewports, routes, flows, roles, and locales are independent test-matrix axes: coverage design and execution across them are parallel-safe.
- Continue to `web-release-deployment-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: every high-risk flow has at least one test with an owner and an environment, the matrix states which cells are automated versus manual, and blocker rules make it unambiguous which defects stop a release.

## Responsibilities

- Build the route and flow test matrix.
- Define manual versus automated coverage.
- Specify browser, device, viewport, role, locale, and environment coverage.
- Define smoke, regression, integration, visual, accessibility, SEO, and performance checks.
- Align QA evidence with release gates and blocker rules.

## Expected inputs

- Requirements, frontend, backend, accessibility/SEO, performance, and release constraints.
- Known risk areas and high-value flows.
- Environment and test data availability.

## Expected outputs

The set ships together: test strategy, test matrix, environment and data needs, launch signoff checklist, defect triage priorities, and regression watchlist.

A matrix cell is complete when it names the flow, the browser or device, the environment, the owner, whether it is automated or manual, and the pass condition. Environment and data needs state what has to exist before execution starts, including who provisions it. Triage priorities define severity in terms someone can apply to a defect they are looking at, and blocker rules make it unambiguous which defects stop a release. A matrix of axis labels with empty intersections is not coverage design.

Coverage is claimed only where it exists. Tests that have not been executed are not reported as passing, existing automation that was not observed is not counted, and a high-risk flow with no test is listed as uncovered rather than assigned a plausible one.

## Evidence packet additions

- Coverage matrix.
- High-risk flow list.
- Browser/device matrix.
- Smoke/regression scope.
- Signoff checklist and defect triage rules.

## Packet fields to update

- Routes, flows, browsers, devices, environments, data, automation, blockers.

## Halt conditions

Halt only on a hard class:

- Release integrity: release signoff would be given on coverage that has not been executed or evidenced.
- Production or destructive: testing would run against production data or a live system without an agreed safe path.
- Security or privacy: test data would carry real credentials or personal data.
- Connector unreachable: the CI, test-report, or environment source needed for coverage evidence cannot be reached.

A missing test environment, missing test data, an unaccepted high-risk flow list, and an unknown browser or device baseline are not halts for planning. Proceed with the assumed matrix labeled inline and recorded in `open_questions`.

## Default output modes

One run delivers all of these:

- `web-testing-qa.md`: strategy, coverage matrix, environment and data needs, signoff checklist, triage rules.
- `web-testing-qa-source-facts.md`: existing tests, CI results, and environment facts with their sources.
- `web-testing-qa-risk-register.md`: uncovered risk areas with the failure each one would let through.
- `web-testing-qa-downstream-handoff.md`: the signoff evidence `web-release-deployment-desk` gates on.

`connector-diagnostic.md` is the alternative when the CI, test-report, or environment source cannot be reached, not an extra item in the set.

Browsers, devices, viewports, routes, flows, roles, and locales are independent axes per the Workflow section, so building these artifacts is parallel-safe across them.

A complete set is not a coverage claim. Where evidence for a cell does not exist, the cell says so, and the signoff checklist reflects that rather than reading clean.

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `web-release-deployment-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
