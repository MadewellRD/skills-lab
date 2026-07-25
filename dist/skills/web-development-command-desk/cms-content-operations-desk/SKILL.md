---
name: cms-content-operations-desk
description: define cms and content operations for web properties including structured content models, editorial workflow, publishing rules, approvals, localization, migration, governance, content debt, metadata ownership, and day-two content maintenance. use for marketing sites, docs sites, blogs, landing pages, headless cms, ecommerce content, and content-heavy portals.
---

# CMS Content Operations Desk


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

Define structured content models, editorial workflows, publishing rules, localization processes, and day-two content operations for web properties.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Content types and locales are independent: per-type field modeling and per-locale rule definition are parallel-safe.
- Continue to `accessibility-seo-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: every content type has fields, validation, an owner, and a publish path; the editorial workflow names who authors, approves, publishes, and rolls back; and localization and compliance rules are stated per type rather than globally assumed.

## Responsibilities

- Design content types, fields, validation rules, and ownership.
- Separate presentation concerns from editorial concerns.
- Define authoring, approval, preview, publish, rollback, and archive flows.
- Establish localization, regionalization, multi-brand, and compliance rules.
- Plan content governance, audits, migration, and refresh cadence.

## Expected inputs

- Requirements and IA outputs.
- Existing content inventory.
- CMS/platform constraints.
- Editorial team roles and approval requirements.
- Localization, compliance, or migration context.

## Expected outputs

These ship together as one deliverable set: content model, editorial workflow, publishing rules, governance plan, localization plan, content debt backlog, and migration notes.

Each has to be operable by an editor and an implementer without a second conversation. The content model lists every type with its fields, field types, validation, required or optional status, and owner. The editorial workflow names the actual roles that author, review, approve, publish, and revert. Migration notes state what moves, from where, in what order, and what happens to whatever does not move. A content model given as a list of type names is a stub, not a model.

Migration notes are the sharpest case for restraint. If the existing content inventory could not be reached, say the migration is unplanned and name the inventory as the blocker. Do not project a field mapping onto content nobody has counted.

## Evidence packet additions

- Content types and fields.
- Editorial role matrix.
- Publish/approval flow.
- Localization rules.
- Content migration and debt notes.

## Packet fields to update

- Content model, editorial owners, publish rules, metadata, localization.

## Halt conditions

Halt only on a hard class:

- Missing approval: compliance-sensitive or regulated content would publish without a named approval owner.
- Production or destructive: a content migration, bulk republish, archive, or delete would run against live content without a source-backed inventory and a reversible path.
- Source conflict: content model, taxonomy, or localization rules genuinely disagree across sources.
- Connector unreachable: the CMS, repo, or content inventory source cannot be reached.

Unknown CMS or platform constraints, and gaps in a planning-only inventory, are not halts. Proceed with the assumption labeled inline and recorded in `open_questions`.

## Default output modes

A run delivers all of these:

- `cms-content-operations.md`: content model, editorial workflow, publishing and localization rules, governance cadence.
- `cms-content-operations-source-facts.md`: CMS capabilities, existing types, inventory counts, and role assignments, each attributed.
- `cms-content-operations-risk-register.md`: governance, localization, migration, and content-debt risks with likelihood and blast radius.
- `cms-content-operations-downstream-handoff.md`: the content contract `accessibility-seo-desk` and the frontend stage build against.

`connector-diagnostic.md` replaces the set when the CMS, repo, or content inventory cannot be reached. It is the alternative outcome of a run, not a fifth file.

Content types and locales are independent units, so drafting across these artifacts falls inside the parallel surface the Workflow section declares.

A full set is not a licence to guess. Locale rules, approval owners, and inventory counts that no source supplies are marked unknown and carried into `open_questions`. Plausible editorial process is still fabricated editorial process.

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `accessibility-seo-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
