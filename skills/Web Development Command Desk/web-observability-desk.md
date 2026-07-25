---
name: web-observability-desk
description: design production web observability including rum, synthetic checks, availability, frontend errors, api errors, latency, core web vitals, analytics events, dashboards, alerts, ownership, incident hooks, launch monitoring, and post-launch review. use before release, during launch readiness, after incidents, or when improving operating visibility.
---

# Web Observability Desk


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

Define production telemetry, dashboards, alerting, real-user monitoring, synthetic coverage, and incident hooks for web properties.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Critical journeys, services, and dashboards are independent: per-journey synthetic definitions and per-signal alert thresholds are parallel-safe.
- Continue to `web-maintenance-growth-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: every critical journey has a monitored signal, every alert has a threshold, an owner, and an escalation path, and every dashboard maps to a decision someone makes with it.

## Responsibilities

- Define monitoring across availability, latency, frontend errors, backend errors, user journeys, and conversion-critical flows.
- Set event, metric, log, trace, RUM, synthetic, and analytics expectations.
- Establish dashboards for launch and steady-state operations.
- Connect alert routing, ownership, incident response, and post-launch review.
- Ensure evidence is measurable and actionable.

## Expected inputs

- Performance and deployment plans.
- Security notes.
- Critical user flows.
- Analytics intent.
- Environment topology.
- SLO or availability expectations.

## Expected outputs

The full set from one run: observability plan, dashboard requirements, alert thresholds, RUM and synthetic plan, incident hooks, and the launch-day monitoring checklist.

An alert entry is complete when it names the signal, the threshold, the evaluation window, the owner, the routing destination, and the action expected of whoever is paged. A synthetic check names the journey, the frequency, the assertion, and the environment. Dashboards are specified by the decision they support and the panels that support it. A list of metric names is an inventory, not an observability plan.

Thresholds and SLO targets are the invention risk here, because a plausible number reads like a decided one. If no source establishes a baseline, state the threshold as proposed and unvalidated, or record the baseline as the blocking gap. Never report telemetry as live when nothing confirmed that it is.

## Evidence packet additions

- Monitoring inventory.
- Dashboard spec.
- Alert routing.
- Synthetic journey list.
- Ownership map.
- Incident response references.

## Packet fields to update

- RUM, synthetic, dashboards, alerts, events, ownership, launch monitoring.

## Halt conditions

Halt only on a hard class:

- Release integrity: a launch or release gate depends on monitoring that has no owner, no escalation path, or no evidence that it is live.
- Production or destructive: the next action would change live alerting, sampling, or routing configuration.
- Security or privacy: proposed telemetry would capture credentials, tokens, or personal data.
- Connector unreachable: the monitoring, analytics, or repo source needed for telemetry evidence cannot be reached.

A missing critical-journey list and an unknown observability stack are not halts for planning. Proceed with the assumed journeys and stack labeled inline and recorded in `open_questions`.

## Default output modes

One run delivers:

- `web-observability.md`: monitoring plan, dashboards, alerts, synthetic and RUM coverage, launch checklist.
- `web-observability-source-facts.md`: existing telemetry, tooling, ownership, and SLO facts with their sources.
- `web-observability-risk-register.md`: blind spots and unowned alerts with the failure each one would miss.
- `web-observability-downstream-handoff.md`: what `web-maintenance-growth-desk` and incident response inherit.

`connector-diagnostic.md` replaces the set when the monitoring, analytics, or repo source cannot be reached.

Journeys, signals, dashboards, and alert rules are independent review units per the Workflow section, so these artifacts belong to the same parallel surface.

The set is complete; its contents are only as complete as the evidence. Coverage that exists stays distinguished from coverage that is proposed, and an unmonitored journey is named as uncovered rather than given a threshold to fill the row.

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `web-maintenance-growth-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
