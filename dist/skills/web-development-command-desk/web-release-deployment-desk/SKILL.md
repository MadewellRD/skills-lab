---
name: web-release-deployment-desk
description: plan web release and deployment across ci/cd, preview environments, build commands, environment promotion, hosting, cdn, edge config, cache invalidation, feature flags, launch checklist, rollback, post-release validation, and release-to-observability handoff. use when preparing or executing web launches, rollouts, migrations, hotfixes, or rollbacks.
---

# Web Release Deployment Desk


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

Take validated web changes through build, environment promotion, deployment, launch, rollback, and post-release verification.

## Workflow

1. Classify the request and target surface.
2. Run connector preflight for repo, docs, product, design, analytics, or operational facts relevant to this stage.
3. Build source facts and separate assumptions from verified evidence.
4. Produce this desk's artifact and update the `web_delivery_packet`.
5. Continue to `web-observability-desk` when the packet is ready and the target outcome requires additional downstream work.
6. Halt only when required source facts, approvals, or connector access are missing.

## Responsibilities

- Define environment flow, build commands, preview behavior, and promotion rules.
- Align CI/CD with web-specific build, artifact, config, and hosting needs.
- Plan CDN, edge, DNS, cache, feature-flag, and environment-variable considerations.
- Set rollback, recovery, launch communication, and post-release validation expectations.
- Prevent unsafe or unobservable releases.

## Expected inputs

- Approved implementation or release scope.
- QA, security, performance, and observability readiness.
- Hosting, CI/CD, CDN, DNS, environment, and config facts.
- Release timing and owners.

## Expected outputs

Release plan, deployment checklist, rollback plan, environment documentation, launch checklist, post-release validation plan.

## Evidence packet additions

- Environment map.
- Promotion rules.
- Rollback steps.
- Cache/CDN/edge notes.
- Launch window and owners.
- Production verification checklist.

## Packet fields to update

- CI/CD, hosting, env vars, preview, CDN, rollback, launch, verification.

## Halt conditions

- No deployment target or hosting facts.
- Missing rollback owner or rollback path.
- Unpassed critical security, QA, or observability gates.

## Default output modes

- `web-release-deployment.md`
- `web-release-deployment-source-facts.md`
- `web-release-deployment-risk-register.md`
- `web-release-deployment-downstream-handoff.md`
- `connector-diagnostic.md`

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `web-observability-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
