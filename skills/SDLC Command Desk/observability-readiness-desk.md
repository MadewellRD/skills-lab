---
name: observability-readiness-desk
description: create connector-grounded observability readiness artifacts for software delivery. use when chatgpt needs to design or review logging, metrics, traces, dashboards, alerts, slos, operational runbooks, deployment monitoring checkpoints, telemetry gaps, or production-readiness evidence from repositories, architecture docs, deployment plans, incidents, ci results, and monitoring context.
---

# Observability Readiness Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Use this skill to turn product, architecture, deployment, and operations context into observability readiness artifacts. The skill answers whether a system can be monitored, diagnosed, alerted on, and operated safely before or after release.

Default outputs are Markdown artifacts: observability plans, telemetry design notes, runbook readiness checks, SLO/SLA notes, alerting recommendations, deployment monitoring checkpoints, and observability gap reports.

## Connector preflight

Before producing operational recommendations, gather the best available source facts.

Required when available:

1. GitHub for source code, logging/tracing/metrics instrumentation, config files, deployment manifests, CI checks, and recent PRs.
2. Product, architecture, release, deployment, incident, or runbook docs for intended behavior and operational commitments.
3. Monitoring, observability, or incident sources when the user asks about existing dashboards, alerts, SLOs, or production failures.

If a required source is unavailable, state the limitation and produce either a scoped user-fact-only artifact or a connector diagnostic. Do not invent dashboards, metrics, alert names, incident IDs, service ownership, or SLO targets.

## Workflow

1. Classify the request: readiness review, telemetry design, runbook, SLO/alerting, deployment monitoring, incident follow-up, or gap analysis.
2. Route to connectors using `references/connector-routing.md`.
3. Apply truth precedence from `references/source-hierarchy.md`.
4. Select the output shape from `references/output-contract.md`.
5. Build the artifact using the relevant template:
   - `references/observability-plan-template.md`
   - `references/telemetry-design-template.md`
   - `references/runbook-template.md`
   - `references/slo-alerting-template.md`
   - `references/readiness-checklist.md`
6. Include evidence, unknowns, and assumptions. Use halt behavior from `references/halt-conditions.md` when source truth is missing or conflicting.
7. When the next step is implementation, provide downstream handoff notes for `implementation-handoff-desk`, `deployment-desk`, `incident-response-desk`, or `release-operations-desk`.

## Output rules

Use concise, operational language. Prefer source-backed findings, specific gaps, and concrete next actions.

Every substantive artifact should include:

- scope and service/system under review
- source facts used
- current observability surface
- required telemetry or operational readiness gaps
- risks and severity
- owner/action recommendations when known
- validation or follow-up checks
- downstream handoff notes

For downloadable artifacts, use `scripts/write_observability_markdown.py` to wrap content in a standard Markdown file.

## Halt rules

Halt or produce a connector diagnostic when:

- the service, repo, or deployment target is unclear
- requested production claims require monitoring sources that are unavailable
- source facts conflict across repo, docs, dashboards, or incident notes
- the user asks for go/no-go readiness but logs, metrics, traces, alerts, or rollback/deployment context are missing
- the task requires implementation changes better handled through `implementation-handoff-desk`

## Composition with SDLC desk skills

- Use `deployment-desk` for rollout mechanics and deployment gates.
- Use this skill for monitoring checkpoints, telemetry gaps, dashboards, alerts, runbooks, and SLO readiness.
- Use `incident-response-desk` for active incidents, RCA, severity handling, and remediation tracking.
- Use `release-operations-desk` for release runbooks and post-release verification packaging.
- Use `implementation-handoff-desk` when an observability gap needs a code/config PR prompt.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/codex-conservation-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `CODEX_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
