---
name: platform-observability-desk
description: design the default instrumentation baseline and telemetry pipeline for an internal developer platform including auto-instrumentation, collector routing, metrics logs traces and profiles, resource attributes and naming conventions, cardinality and retention limits with their cost consequence, tenant-scoped dashboards and access, and the coverage gaps where the platform cannot see its own consumers.
---

# Platform Observability Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the observability artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent signal names, retention settings, active series counts, ingest volumes, backend costs, dashboard inventories, or instrumentation coverage figures.

## Role

Own what every tenant gets instrumented without asking, where those signals go, what they are allowed to cost, and what the platform can see about the experience it is delivering.

This desk works on two planes at once. The first is the telemetry the platform hands to tenants as part of the paved road. The second is the platform's own visibility into its consumers: provisioning latency, pipeline queue wait, template adoption, policy denials, portal usage. A platform that ships excellent tenant dashboards and cannot answer "how long does a new service wait for a database" is instrumented on the wrong plane.

## Use when

- Setting or revising the default instrumentation a scaffolded service receives on day one, including what arrives without code change and what the tenant must add.
- Designing or reworking the telemetry pipeline: agents, collectors, gateways, processors, sampling, and backend routing.
- Signal schema work: resource attributes, service and environment identity, metric and log naming conventions, trace context propagation.
- Cardinality or retention has become a cost problem, or a limit needs to be set before it becomes one.
- Tenant-scoped dashboards and data access need designing, including which tenant can see which signals.
- A stage downstream reported that a platform objective cannot be measured, and the measurement gap needs closing.

## Do not use when

- Objectives, error budgets, burn-rate policy, or dependency failure analysis are the subject: that is `platform-slo-reliability-desk`, which consumes this desk's measurement state.
- The signals exist and the question is what a page or an on-call rotation does with them: that is `platform-support-operations-desk` for platform request load, and the SRE suite for tenant-workload incident practice.
- Telemetry ingest spend needs allocating to tenants and turned into a chargeback line: that is `platform-cost-attribution-desk`. This desk sets the limits; that desk assigns the bill.
- Wiring the instrumentation into the generated repository is template work owned by `scaffolding-templates-desk`.

## Required evidence

- Template and pipeline injection points: what the scaffolding actually wires in, at which template version, and how far the generated fleet has drifted from it.
- Collector and agent configuration as deployed: receivers, processors, exporters, sampling policy, failure and retry behavior.
- Backend usage data: active series, ingest volume by signal, top cardinality contributors, and the query or usage report each figure came from.
- Current retention and downsampling configuration per signal and per tier.
- Existing dashboard and alert inventory with ownership, plus the access model that scopes them per tenant.
- Tenancy boundaries from the packet, since signal isolation follows the tenancy model rather than inventing its own.
- The platform's own control-plane, provisioning, and pipeline emission points, and which of them are currently unemitted.

## Workflow

**Outcome.** A default instrumentation baseline stated as what a tenant receives without asking, a routed pipeline from emitter to backend with its limits, a naming and attribute convention that makes cross-tenant queries possible, and an honest coverage map naming where the platform is blind.

**Grounding.** Read the deployed collector configuration and the backend's own usage output for reality; read the observability standard, the runbook, and the portal documentation for intent. Where the standard specifies attributes that the deployed pipeline drops, that gap is the finding, recorded with both sources attributed per `references/suite-workflow-contract.md`.

**Constraints.** Every signal in the baseline carries an owner, a route, a retention tier, and a cardinality expectation, because an unbounded label value is the failure that arrives as a bill rather than as an alert. Resource attributes are set once at the platform boundary so that tenant, service, and environment identity is not left to each team's convention; a signal that cannot be attributed to a tenant cannot be scoped, budgeted, or charged. Sampling decisions state what they make unanswerable, not only what they save. Retention is set per tier against a stated question the retained data answers. Tenant access to signals inherits the isolation controls already in the packet and does not weaken them.

Cost consequence is part of the specification rather than an afterthought: each limit records the unit it protects, whether that is active series, ingested gigabytes, or spans per second, so a later request to raise the limit is a priced decision instead of a configuration edit.

**Parallel surface.** Signals, tenants, services, pipelines, dashboards, and injection points are independent units and are parallel-safe; per-signal schema work, per-tenant coverage assessment, and connector preflight across the templates, collector configuration, and telemetry backend all fan out.

The aggregate work runs once after the fan-out returns: the total cardinality and ingest budget split across signals, the fleet-wide coverage percentage, the ranking of which blind spot gets closed first, and the reconciliation of per-tenant views into a single platform picture.

**Acceptance bar.** A tenant onboarding tomorrow can be told exactly which signals appear without any work on their side, where to find them, and what they are not allowed to do to them. Every number about volume, cardinality, retention, or coverage names the query or usage report behind it. Each blind spot names the decision it currently prevents.

## Outputs

A complete run delivers this artifact set:

- `platform-observability-baseline.md`: the default instrumentation per signal class, what arrives with no tenant effort, what requires tenant code, and the template version that delivers it.
- `platform-observability-pipeline.md`: emitter to collector to backend routing with processors, sampling, failure behavior, retention tiers, and the cardinality limits with their protected unit.
- `platform-observability-coverage-map.md`: what the platform can see about each tenant and about its own control plane, provisioning path, and pipelines, with the blind spots named and each one tied to the question it blocks.
- `platform-observability-downstream-handoff.md`: for `platform-slo-reliability-desk`, which candidate SLIs have a real emitting signal today and which would need instrumentation first, stated per objective.

Depth standard per artifact: a baseline entry names the actual signal, its attributes, and its emission mechanism, not the observability pillar it belongs to. "Traces are enabled" is a pillar; a baseline entry states which instrumentation produces the span, which attributes carry tenant and service identity, what the sampling policy keeps, and where the trace lands. A pipeline entry that omits the drop and refusal behavior is incomplete, because that is where signals disappear silently. A coverage-map entry states how the gap was established, whether by a query returning nothing or by configuration showing nothing is emitted.

In `diagnostic` mode, when the collector configuration, template repository, or telemetry backend exists and cannot be read, the run delivers `platform-observability-connector-diagnostic.md` reporting reachability, the queries attempted, and the exact access needed. Coverage is not asserted from documentation in that mode.

Observability writing fails through fluent quantities. Active series counts, ingest volumes, retention windows, and coverage percentages read as though they came from a usage report even when they came from a sensible default, and no reviewer challenges a number that looks exported. Every figure in these artifacts carries the query, dashboard, or usage export that produced it, or it is written as uncounted. "Instrumented by default" is claimed from the template version the fleet actually runs, not from the template repository's main branch, because those two disagree in every platform that has existed for more than a year. A coverage map that honestly says the platform cannot see something is the most valuable page in the set.

## platform_packet fields to update

- `telemetry_defaults[]`: `signal`, `instrumentation`, `routing`, `retention_and_cardinality`.
- `devex_metrics[]` for any experience metric this stage made measurable, with its source.
- `templates[].scaffolds` where telemetry defaults are injected, and `templates[].downstream_drift` where the fleet lags.
- `platform_slos[].current_state` set to measured or unmeasured based on emitting-signal evidence.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: raising a retention window, cardinality ceiling, or ingest budget changes committed spend and needs the named owner who has not given it.
- Production or destructive: the next action would change live collector configuration, drop or reroute a production signal, delete telemetry data, or alter retention on data already collected.
- Security or privacy: continuing would route logs or traces that may carry credentials, tokens, or personal data without a scrubbing decision, or would grant a tenant visibility into another tenant's signals.
- Source conflict: the deployed pipeline, the observability standard, and the backend's usage output disagree about what is collected or retained, and picking one silently would misstate coverage.
- Release integrity: an objective would be declared measurable, or a signal declared collected by default, without evidence that anything emits it.
- Connector unreachable: the collector configuration, template repository, or telemetry backend exists and cannot be read.

Missing cardinality figures, absent usage exports, and undocumented dashboard ownership are soft gaps: proceed with them named as uncounted. Tenant signal isolation is not a soft gap and is never relaxed to simplify a pipeline.

## Downstream handoffs

`platform-slo-reliability-desk` needs the measured-versus-unmeasured verdict per candidate SLI, because that split decides which objectives can be committed and which stay aspirational. `platform-cost-attribution-desk` needs ingest and storage volume broken out by tenant-identifying attribute so telemetry spend is allocable. `platform-support-operations-desk` needs the signals its runbooks depend on. `platform-adoption-migration-desk` needs the telemetry that distinguishes a tenant on the paved road from one using an escape hatch.

## Quality bar

A new service gets useful telemetry with no observability work by its team, and the platform can answer questions about its own consumers without asking them. Names and attributes are consistent enough that one query spans tenants. Limits are stated with the cost they protect. Blind spots are written down rather than discovered during the next incident.
