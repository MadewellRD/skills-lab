---
name: information-architecture-desk
description: design web information architecture including sitemap, route hierarchy, navigation, url taxonomy, content relationships, wayfinding, content hierarchy, and findability. use when Claude needs to structure websites, portals, dashboards, docs sites, ecommerce surfaces, or web apps before design, cms, accessibility, seo, frontend, or release work.
---

# Information Architecture Desk


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

Define the structure of the web surface: route hierarchy, navigation models, URL taxonomy, content relationships, and the user path through the system.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Auditing existing routes, URL patterns, and independent sitemap subtrees is parallel-safe; only the final hierarchy reconciliation needs a single pass.
- Continue to `ux-ui-design-system-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: the route tree covers every in-scope page with no orphans, dead ends, or duplicate URLs, navigation labels and URL conventions are stated as rules rather than examples, and every IA decision is traceable to a source fact or labeled as an assumption.

## Responsibilities

- Produce sitemap or route map.
- Define navigation layers, wayfinding, labels, and URL conventions.
- Model content/entity relationships and route ownership.
- Identify orphaned flows, dead ends, duplicate routes, and unclear hierarchy.
- Align structure with accessibility, SEO, CMS, and frontend routing needs.

## Expected inputs

- Requirements packet.
- Existing sitemap, route list, analytics, content inventory, or page screenshots.
- Product entities, user roles, localization, brand, or multi-site constraints.

## Expected outputs

Sitemap or route tree, navigation model, URL taxonomy, content hierarchy, cross-linking plan, IA decisions, findability risks.

## Evidence packet additions

- Sitemap or route definitions.
- Navigation hierarchy.
- URL and slug rules.
- Content/entity relationship map.
- IA decision log and risks.

## Packet fields to update

- Routes, navigation, URL rules, content hierarchy, IA risks.

## Halt conditions

Halt only on a hard class:

- Source conflict: URL, localization, or navigation requirements genuinely disagree and the conflict is load-bearing for the route tree.
- Missing approval: a URL, domain, or redirect change needs human authorization that has not been given.
- Production or destructive: an IA change would break or retire live URLs without an agreed redirect map.
- Connector unreachable: the repo, sitemap, or content source needed for route evidence cannot be reached.

An unaccepted target surface, unscoped routes, or a missing content inventory is not a halt. Proceed with the assumption labeled inline in the artifact and recorded in `open_questions`.

## Default output modes

- `information-architecture.md`
- `information-architecture-source-facts.md`
- `information-architecture-risk-register.md`
- `information-architecture-downstream-handoff.md`
- `connector-diagnostic.md`

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `ux-ui-design-system-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
