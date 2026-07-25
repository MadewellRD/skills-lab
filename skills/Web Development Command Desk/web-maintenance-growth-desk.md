---
name: web-maintenance-growth-desk
description: coordinate post-launch web maintenance and growth including analytics-informed backlog, experiments, conversion optimization, content refresh, seo iteration, accessibility remediation, performance regression follow-up, dependency upgrades, refactors, migrations, and decommissioning triggers. use after launch or when improving an existing website or web app.
---

# Web Maintenance Growth Desk


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

Own the after-launch lifecycle: backlog refinement, experimentation, analytics-informed iteration, content refresh, refactor planning, migration, and retirement support.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Backlog candidates, content items, dependency upgrades, and remediation items are independent and parallel-safe to analyze. Concurrent live experiments on the same surface are not: they interact through shared traffic and must be sequenced or isolated.
- Continue to `site-product-requirements-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: every backlog item is traceable to telemetry, analytics, feedback, incident, or business-goal evidence, every experiment names its hypothesis, metric, guardrail, and stop rule, and unmeasured opportunities are labeled as hypotheses rather than findings.

## Responsibilities

- Prioritize post-launch improvements from telemetry, analytics, feedback, incidents, and business goals.
- Define experiments, hypotheses, metrics, guardrails, and rollback/stop rules.
- Plan content refresh, SEO iteration, accessibility remediation, performance follow-up, and dependency work.
- Track maintenance, upgrades, refactors, migrations, and decommissioning triggers.
- Feed material changes back into requirements and release workflows.

## Expected inputs

- Launch data.
- Observability, analytics, search, accessibility, performance, and user feedback signals.
- Content/editorial needs.
- Tech debt register.
- Roadmap constraints.

## Expected outputs

Iteration backlog, growth experiment plan, content refresh plan, refactor priorities, lifecycle health notes, retirement triggers.

## Evidence packet additions

- Post-launch issue list.
- Growth hypotheses.
- Experiment definitions.
- Content update cadence.
- Technical debt summary.
- Outcome review notes.

## Packet fields to update

- Analytics, experiments, feedback, content refresh, technical debt, migrations.

## Halt conditions

Halt only on a hard class:

- Production or destructive: a live experiment, redirect, content cutover, or dependency upgrade would run against production without an agreed metric, guardrail, and stop rule.
- Missing approval: a retirement, decommissioning, or user-visible change needs human authorization.
- Source conflict: analytics, telemetry, and feedback sources genuinely disagree on a load-bearing outcome.
- Connector unreachable: the analytics, observability, or repo source needed for evidence cannot be reached.

An unsourced growth opportunity, and maintenance work whose implementation facts are not yet available, are not halts. Proceed with the item labeled as a hypothesis rather than a finding and record the gap in `open_questions`. Never state an unmeasured outcome as a metric.

## Default output modes

- `web-maintenance-growth.md`
- `web-maintenance-growth-source-facts.md`
- `web-maintenance-growth-risk-register.md`
- `web-maintenance-growth-downstream-handoff.md`
- `connector-diagnostic.md`

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `site-product-requirements-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
