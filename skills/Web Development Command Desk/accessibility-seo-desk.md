---
name: accessibility-seo-desk
description: define accessibility and seo requirements for web surfaces including wcag, semantic html, keyboard navigation, focus, screen-reader behavior, metadata, structured data, canonicals, sitemaps, robots, crawlability, localization, and page-type search requirements. use before launch or during redesign, content, frontend, cms, or qa workflows.
---

# Accessibility SEO Desk


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

Ensure the web surface is usable, perceivable, operable, understandable, and discoverable through first-class accessibility and search requirements.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Routes and page types are independent: per-route accessibility evaluation and per-page-type SEO evaluation are parallel-safe.
- Continue to `web-performance-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: the accessibility standard is stated explicitly (WCAG 2.2 AA unless source facts require another standard), every in-scope page type carries semantic-structure, keyboard, focus, and screen-reader requirements alongside metadata, canonical, and structured-data requirements, and every remaining gap appears in the remediation backlog rather than being dropped.

## Responsibilities

- Define accessibility standard, usually WCAG 2.2 AA unless source facts require otherwise.
- Review semantic structure, headings, landmarks, keyboard access, focus behavior, alt text, forms, and screen-reader implications.
- Define metadata, structured data, canonicals, robots, sitemaps, internal linking, and crawlability.
- Align content structure with search and accessibility goals.
- Provide pre-launch acceptance gates and remediation backlog.

## Expected inputs

- Requirements, IA, design-system, CMS/content, and frontend plans.
- Current pages, analytics, search console notes, or accessibility reports when available.
- Localization or multi-domain constraints.

## Expected outputs

One run delivers all of these together rather than one of them: the accessibility checklist, the SEO checklist, metadata requirements, structured-data requirements, launch acceptance criteria, and the remediation backlog.

Each is written to be worked from directly. The accessibility checklist names the criterion, the page types it applies to, and the observable pass condition, not "check headings". Metadata and structured-data requirements state the field, its source, and the rule per page type. The remediation backlog carries a severity and an owner per item wherever sources name one. A checklist that lists only WCAG section numbers, or a backlog of one-line labels, is unfinished work.

Where a page type has no source basis for a requirement, because no content model, analytics, or existing markup could be inspected, record it as not applicable or as an open question. Do not populate it with a requirement that merely sounds right for a page of that kind.

## Evidence packet additions

- Accessibility standard statement.
- Semantic structure notes.
- Metadata and structured-data plan.
- Canonical/sitemap/robots notes.
- Keyboard/screen-reader checklist.

## Packet fields to update

- WCAG, semantics, keyboard, metadata, structured data, crawlability, localization.

## Halt conditions

Halt only on a hard class:

- Missing approval: a regulated context needs an accessibility conformance target or a conformance claim that only a human can accept.
- Release integrity: a launch gate would be marked passed on accessibility or SEO conformance that has not been evidenced.
- Source conflict: accessibility standard, localization, or canonical/indexation requirements genuinely disagree.
- Connector unreachable: the route inventory, content model, or audit source needed for evidence cannot be reached.

A missing page or route inventory, and a missing content model for metadata governance, are not halts. Proceed against the stated standard, label the assumed inventory inline, and record it in `open_questions`. Accessibility requirements are compliance obligations: never drop or downgrade one to keep the workflow moving.

## Default output modes

A complete run produces this set in one pass:

- `accessibility-seo.md`: the standard, the per-page-type requirements, and the launch acceptance gates.
- `accessibility-seo-source-facts.md`: every audit result, existing-markup fact, and analytics or search-console figure with the source it came from, kept separate from inference.
- `accessibility-seo-risk-register.md`: conformance and indexation risks with severity, affected page types, and what would clear each one.
- `accessibility-seo-downstream-handoff.md`: what `web-performance-desk` or the next selected stage inherits, including unresolved gaps named individually.

`connector-diagnostic.md` is not a fifth member of that set. It is what the run produces instead when a required connector is unreachable and the route inventory or audit evidence cannot be established at all.

These four are independent once the page-type inventory is fixed, so they belong to the parallel surface the Workflow section declares. Draft them concurrently rather than in sequence.

Producing four files is not the same as having four artifacts. If the risk register has no sourced risk to record, say that and leave it there. An empty section with an honest reason is better than a plausible one, and the same holds for handoff notes with nothing to hand off.

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `web-performance-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
