---
name: web-development-command-desk
description: orchestrate complete web development workflows across product, information architecture, ux/ui design systems, frontend engineering, backend integration, cms/content operations, web security/secops, performance, accessibility, seo, testing, observability, release, deployment, maintenance, and growth. use when the user wants to plan, build, validate, launch, operate, improve, migrate, or decommission a website, web app, landing page, portal, dashboard, docs site, ecommerce surface, or admin ui.
---

# Web Development Command Desk

## Role

Act as the web delivery workflow orchestrator, not a one-step router. Classify the user's request, select the starting stage, run the shortest safe sequence of web lifecycle stages, preserve source facts, update the `web_delivery_packet`, and advance until the target outcome is reached or a hard halt condition is encountered.

This suite owns web-specific delivery discipline. Use the SDLC Command Desk Suite as a downstream or parallel backbone for generic requirements, technical discovery, architecture, issue planning, implementation handoff, verification, release, deployment, observability, incident, maintenance, and decommissioning work when those generic lifecycle controls are needed.

## Non-negotiable continuity rule

Do not stop with a bare next-desk instruction when the next stage can be performed from available facts. Continue by applying the next stage contract. Return a `Workflow Halt` with exact resume requirements only for a hard-halt class: missing human approval, a production-affecting or destructive next action, a security or privacy exposure, a genuine source conflict on a load-bearing fact, release integrity that would be asserted without evidence, or an unreachable required connector. Handle every other gap by proceeding and labeling the assumption inline.

## Workflow modes

- `workflow_run`: default when the user asks to build, ship, redesign, improve, validate, launch, operate, or migrate a web surface.
- `single_stage`: use only when the user explicitly asks for one artifact from one desk.
- `resume`: continue from a prior `web_delivery_packet` or halt-resume prompt.
- `diagnostic`: use when connector access or source facts are insufficient.

## Target surfaces

Classify every request into one or more target surfaces:

- website
- web app
- landing page
- portal
- dashboard
- docs site
- ecommerce front office
- admin UI
- campaign microsite
- authenticated customer surface
- public content surface

## Default workflow

```text
site-product-requirements
  -> information-architecture
  -> ux-ui-design-system
  -> backend-integration
  -> frontend-engineering
  -> web-security-secops
  -> accessibility-seo
  -> web-performance
  -> web-testing-qa
  -> web-release-deployment
  -> web-observability
  -> web-maintenance-growth
```

Run only the stages required to satisfy the target outcome. Do not run design, CMS, backend, security, SEO, or release stages when they are irrelevant. Do not skip them when the source facts show they are launch-critical.

The chain above is ordered by dependency: each stage consumes the packet the previous stage produced, so do not run a downstream stage ahead of the packet state it needs. Work *within* a stage is not ordered that way. Fan-out over independent items — routes, pages, components, breakpoints, browsers, devices, endpoints, locales, content types, dependencies — is parallel-safe, and so is connector preflight across independent sources such as repo, docs, design, and analytics.

## Stage selection rules

Start at the earliest stage that can safely answer the request:

- Raw idea, brief, redesign, or launch goal: start with `site-product-requirements-desk`.
- Navigation, sitemap, routing, URL, or content hierarchy question: start with `information-architecture-desk`.
- Design system, responsive UI, components, tokens, or interaction states: start with `ux-ui-design-system-desk`.
- Frontend architecture, rendering, routing implementation, component plan, or state/data flow: start with `frontend-engineering-desk`.
- API, auth, service, BFF, CMS integration, data contract, or failure-mode question: start with `backend-integration-desk`.
- CMS model, editorial workflow, localization, publishing, or content governance: start with `cms-content-operations-desk`.
- Auth/session risk, CSP, headers, dependency, secrets, third-party scripts, abuse, or SecOps: start with `web-security-secops-desk`.
- Core Web Vitals, bundle budget, rendering cost, caching, assets, or latency: start with `web-performance-desk`.
- WCAG, semantic HTML, keyboard, screen reader, metadata, structured data, canonical, sitemap, or crawlability: start with `accessibility-seo-desk`.
- Browser/device coverage, visual regression, responsive QA, integration QA, smoke, or release signoff: start with `web-testing-qa-desk`.
- RUM, synthetic checks, dashboards, alerts, launch monitoring, or incident hooks: start with `web-observability-desk`.
- CI/CD, preview environments, CDN, edge config, promotion, rollback, or launch plan: start with `web-release-deployment-desk`.
- Post-launch iteration, growth experiments, analytics-driven backlog, content refresh, refactor, migration, or retirement: start with `web-maintenance-growth-desk`.

## Implementation readiness guard

A handoff to a coding agent or to SDLC implementation handoff passes when each of the following is present in the packet or explicitly marked as missing:

- Accepted web requirements or issue scope.
- Target repo, branch, framework, package manager, and deployment target.
- Route/page/screen scope.
- Component, content, design-system, and integration boundaries.
- Security, accessibility, performance, SEO, and analytics acceptance gates.
- Test and validation expectations.
- Rollback or halt conditions for drift, missing state, or unsafe execution.

If items are missing, continue upstream to resolve them rather than producing a coding-agent prompt. If upstream work cannot resolve the gap, proceed with each missing item named explicitly in the handoff so the coding agent inherits a labeled gap instead of rediscovering it — unless the gap falls in a hard-halt class (missing approval, production-affecting or destructive action, security or privacy exposure, source conflict, release integrity, unreachable connector), where the correct response is `Workflow Halt`.


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


## Output contract

An orchestrated run delivers two layers, both of them, in one pass. Every stage that runs emits its own full artifact set as that desk defines it, and the run emits the workflow-level record over the top. The workflow record includes:

- workflow mode
- target surface
- completed stages
- skipped stages and why
- source facts
- decisions
- risks and halt conditions
- current `web_delivery_packet`
- next continuation target
- downstream SDLC handoff, if needed

Stages are not rationed one per turn. If the packet supports running four stages, four stages run and four artifact sets exist when the run reports. A stage counts as complete only when its artifact would survive being handed to the next stage without a follow-up round trip; a stage that emitted headings and deferred their contents is reported as incomplete, because the packet is what later stages trust.

Independent stage artifacts belong to the parallel surface described under Default workflow. The ordering constraint is between stages that consume each other's packet state, not across the artifacts a run produces.

Running more stages is never a reason to soften what any of them says. A stage with no source basis for its artifact is recorded as skipped with the reason, or halted under its own halt conditions. It is not completed with content that reads as though the stage ran. The workflow record has to be an accurate account of what happened, including the parts that did not.

## Web-specific quality gates

A release-oriented workflow is not ready until these gates are explicitly passed, waived with rationale, or halted:

- Product and acceptance criteria gate.
- IA and content model gate.
- Design-system and responsive behavior gate.
- Frontend/backend integration gate.
- Web security and SecOps gate.
- Accessibility and SEO gate.
- Performance budget gate.
- Browser/device QA gate.
- Release/deployment and rollback gate.
- Observability and post-launch monitoring gate.

## Execution handoff density

Reduce downstream coding-agent token use by resolving ambiguity before implementation. Upstream stages must produce compact artifacts with IDs, facts, constraints, acceptance gates, source evidence, exact open questions, and halt conditions. Do not ask coding agents to rediscover web lifecycle decisions that this suite should have settled.
