---
name: web-release-deployment-desk
description: plan web release and deployment across ci/cd, preview environments, build commands, environment promotion, hosting, cdn, edge config, cache invalidation, feature flags, launch checklist, rollback, post-release validation, and release-to-observability handoff. use when preparing or executing web launches, rollouts, migrations, hotfixes, or rollbacks.
---

# Web Release Deployment Desk


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

Take validated web changes through build, environment promotion, deployment, launch, rollback, and post-release verification.

## Workflow

Outcome: this desk's artifact for the classified target surface, with the `web_delivery_packet` updated and carried forward.

Constraints:

- Ground the stage in connector evidence for the repo, docs, product, design, analytics, or operational facts it depends on. Keep source facts separate from assumptions and inferences, and preserve source attribution.
- Gathering environment, hosting, CDN, and configuration facts across environments is parallel-safe. Promotion, cache invalidation, rollback, and launch-gate execution are ordered content: keep their sequence exact in the artifacts this desk produces, and never parallelize or reorder them.
- Continue to `web-observability-desk` when the packet is ready and the target outcome requires additional downstream work.
- Halt only for a hard-halt class listed under Halt conditions. Otherwise proceed and label the assumption inline.

Acceptance bar: the release plan names the environment promotion order, the exact rollback path and its owner, the cache and CDN invalidation order, and the post-release checks that decide whether the launch stands, with every gate marked passed, waived with rationale, or blocking.

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

A release run delivers every one of these: release plan, deployment checklist, rollback plan, environment documentation, launch checklist, and post-release validation plan. A release plan without its rollback plan is not a partial delivery, it is an unsafe one.

Each item is written to be executed under time pressure by someone who did not write it. The deployment checklist gives the commands, in order, with the owner and the pass condition per step. The rollback plan gives the exact reversal path, who runs it, how long it takes, and what it does not undo. Post-release validation names the signals watched, for how long, and the threshold that triggers the rollback. Gate ordering stays exactly as the Workflow section requires it.

None of this may be reconstructed. Deploy commands, environment names, rollback procedures, and approval status are either sourced or recorded as missing, and a missing rollback path is a halt rather than a blank to fill with a reasonable-sounding sequence.

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

Deployment is production-affecting, so this desk halts more readily than upstream stages. Halt on any of these hard classes:

- Production or destructive: no confirmed deployment target or hosting facts, so a deploy would act on an unverified environment.
- Production or destructive: no rollback path, or no named rollback owner.
- Release integrity: a critical security, QA, accessibility, performance, or observability gate is unpassed, unwaived, or unevidenced.
- Missing approval: the release window, cutover, or gate waiver has not been authorized by a human.
- Source conflict: release scope, build artifact, or environment configuration evidence genuinely disagrees.
- Connector unreachable: the CI, hosting, or configuration source needed for release evidence cannot be reached.

Planning-only gaps that touch no live environment, such as an undecided launch communication template, are not halts. Proceed with the assumption labeled inline and recorded in `open_questions`.

## Default output modes

One run produces the set:

- `web-release-deployment.md`: environment map, promotion and cutover sequence, launch checklist, rollback path, post-release validation.
- `web-release-deployment-source-facts.md`: CI, hosting, CDN, config, and approval facts with their sources.
- `web-release-deployment-risk-register.md`: release risks with the gate that catches each and the fallback if it does not.
- `web-release-deployment-downstream-handoff.md`: what `web-observability-desk` monitors once the release stands.

`connector-diagnostic.md` is what the run returns instead when the CI, hosting, or configuration source cannot be reached. Deployment content is not drafted around unreachable evidence.

Gathering environment and configuration facts across environments is parallel-safe per the Workflow section. The promotion, invalidation, and rollback sequences those artifacts contain stay strictly ordered.

Completing the set does not soften anything above it. An unsourced deploy command or approval is left as a named gap and the affected gate is marked blocking, never filled in so the checklist reads finished.

## Downstream handoff

When continuing, preserve the full `web_delivery_packet`, summarize only deltas from this stage, and hand off to `web-observability-desk` unless the command desk selects a different next stage based on target outcome.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as formal product requirements, technical discovery, architecture decisions, issue planning, implementation handoff, verification, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
