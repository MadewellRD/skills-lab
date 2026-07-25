---
name: observability-readiness-desk
description: create connector-grounded observability readiness artifacts for software delivery. use when Gemini needs to design or review logging, metrics, traces, dashboards, alerts, slos, operational runbooks, deployment monitoring checkpoints, telemetry gaps, or production-readiness evidence from repositories, architecture docs, deployment plans, incidents, ci results, and monitoring context.
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

- GitHub for source code, logging/tracing/metrics instrumentation, config files, deployment manifests, CI checks, and recent PRs.
- Product, architecture, release, deployment, incident, or runbook docs for intended behavior and operational commitments.
- Monitoring, observability, or incident sources when the user asks about existing dashboards, alerts, SLOs, or production failures.

These sources are independent of each other and parallel-safe to retrieve concurrently.

If a required source is unavailable, state the limitation and produce either a scoped user-fact-only artifact or a connector diagnostic. Do not invent dashboards, metrics, alert names, incident IDs, service ownership, or SLO targets.

## Workflow

**Outcome.** The observability artifact the request calls for: readiness review, telemetry design, runbook, SLO/alerting plan, deployment monitoring checkpoints, incident follow-up, or gap analysis.

**Grounding.** Route to connectors using `references/connector-routing.md` and apply truth precedence from `references/source-hierarchy.md`.

**Templates.** Select the output shape from `references/output-contract.md` and build with the relevant template: `references/observability-plan-template.md`, `references/telemetry-design-template.md`, `references/runbook-template.md`, `references/slo-alerting-template.md`, or `references/readiness-checklist.md`.

**Parallel surface.** Services, endpoints, signals, dashboards, alert rules, and SLOs are independent review units — each one's coverage assessment stands on its own. Evaluate them in parallel rather than walking the list serially, then aggregate into one gap report.

**Runbooks are ordered content.** Recovery and mitigation steps inside a runbook are executed under pressure and in sequence. Keep them numbered and ordered; the operator following them must not have to derive the order.

**Handoff.** When the next step is implementation, provide downstream handoff notes for `implementation-handoff-desk`, `deployment-desk`, `incident-response-desk`, or `release-operations-desk`.

**Acceptance bar.** The artifact is done when every gap names the specific missing signal rather than a generic category; each proposed metric, log, trace, alert, or SLO is tied to a failure mode it would actually detect; alerts carry a threshold, an owner, and a stated action; existing coverage is distinguished from proposed coverage; and evidence, unknowns, and assumptions are labeled. Do not invent dashboards, metrics, alert names, incident IDs, service ownership, or SLO targets.

## Output rules

A readiness run delivers the set together: the current coverage picture, the telemetry design for what is missing, the SLO and alerting plan, the gap report ranked by the failure each gap hides, and a runbook entry for every alert the plan creates. An alert with no documented response is not finished work, which is why the runbook belongs to the set rather than to a later request. A standalone gap analysis is a narrower scope and stands alone when that is what was asked for.

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

Each of those is written to be implemented. A gap names the missing signal, not the category it belongs to. An alert names its threshold, evaluation window, owner, routing, and the action expected of whoever receives it. Runbook steps stay numbered and ordered, because whoever follows them is under pressure and should not be deriving order. A report saying telemetry "could be improved" has not identified anything.

Services, endpoints, signals, dashboards, alert rules, and SLOs are independent review units, so the pieces of this set are built in parallel and aggregated into one gap report.

Producing the whole set does not create coverage that is not there. Dashboards, metrics, alert names, service ownership, and SLO targets come from sources or are named as absent, existing coverage stays visibly separate from proposed coverage, and a threshold with no baseline behind it is marked proposed rather than stated as agreed.

For downloadable artifacts, use `scripts/write_observability_markdown.py` to wrap content in a standard Markdown file.

## Halt rules

Proceed by default. An unclear service boundary or a missing dashboard is a gap to record, not a stop — name the assumption inline and continue the readiness assessment. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval** — the artifact would commit the organization to an SLO, error budget, or on-call obligation that a human owner must authorize.
- **Production or destructive** — the request asks to change live alert rules, dashboards, or sampling configuration rather than plan the change.
- **Security or privacy** — proposed telemetry would capture secrets, credentials, or personal data.
- **Source conflict** — repo instrumentation, docs, dashboards, and incident notes genuinely disagree on what is actually monitored.
- **Release integrity** — a go/no-go readiness verdict is requested while logs, metrics, traces, alerts, or rollback context needed to support it are missing.
- **Connector unreachable** — a monitoring source exists but cannot be read, and the request depends on production claims. A source that is merely absent is a soft gap: produce a scoped user-fact-only artifact and continue.

When the task turns into implementation changes, route to `implementation-handoff-desk` rather than halting.

Use `references/halt-conditions.md` for the halt artifact and diagnostic format.

## Composition with SDLC desk skills

- Use `deployment-desk` for rollout mechanics and deployment gates.
- Use this skill for monitoring checkpoints, telemetry gaps, dashboards, alerts, runbooks, and SLO readiness.
- Use `incident-response-desk` for active incidents, RCA, severity handling, and remediation tracking.
- Use `release-operations-desk` for release runbooks and post-release verification packaging.
- Use `implementation-handoff-desk` when an observability gap needs a code/config PR prompt.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
