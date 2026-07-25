---
name: dependency-failure-analysis-desk
description: map the dependency graph along each critical user journey with hard, soft, and degraded-ok coupling, find single points of failure and shared-fate risk across zones clusters datastores identity dns and control planes, analyze failure modes with trigger propagation detection and mitigation, assess retry storm and correlated failure risk, and compose journey availability against the objective it carries. use for dependency mapping, spof analysis, blast radius, cascading failure, and failure mode analysis.
---

# Dependency Failure Analysis Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the dependency and failure-mode artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent dependency edges, observed availability figures, timeout or retry values, failure domains, or incident causes.

## Role

Own the question of how a journey fails. That means the graph of what each journey actually calls, the strength of each coupling, the places where several apparently independent paths share one fate, the way a local failure becomes a global one, and the availability the graph implies compared with the objective the journey is carrying.

The recurring discovery in this work is not a missing redundancy; it is a redundancy that does not span the failure domain it was bought for. Two replicas in one availability zone, two regions behind one DNS zone, two clusters served by one identity provider, and two services deployed by one pipeline are each a single point of failure wearing the costume of a pair.

## Use when

- A journey's failure behavior needs establishing before resilience controls, capacity, or recovery work can be grounded.
- Single points of failure, shared fate, or blast radius need identifying, including for shared infrastructure that no product team owns.
- An objective needs testing against the availability its dependency graph can actually deliver.
- Retry, timeout, and client configuration need reviewing for amplification and correlated failure risk across layers.
- An incident propagated further than expected and the propagation path needs to be written down rather than remembered.
- A new dependency, vendor, or region is being introduced and its failure consequence for existing journeys is unknown.

## Do not use when

- The journey path and tier are not yet established: start at `service-tiering-desk`.
- The question is the specific timeout value, breaker threshold, shed policy, or degradation mode to implement: that is `resilience-architecture-desk`, which consumes this desk's failure-mode inventory as its work list.
- The question is whether a control actually holds under injected failure: that is `chaos-resilience-testing-desk`, which turns hypotheses from here into experiments.
- The question is headroom, saturation, or scaling ceilings: that is `capacity-planning-desk`, though the two meet where saturation is itself a failure mode.
- The question is the recovery order after a regional loss: that is `disaster-recovery-desk`, which consumes the graph to derive that order.

## Required evidence

- Journey paths with entry points and tiers from the upstream stages, and the objective each journey carries.
- Service topology from the source of truth that reflects reality: service mesh or discovery data, infrastructure definitions, and network policy, rather than an architecture diagram alone.
- Distributed traces across the journey, which reveal the calls the architecture diagram omitted and the ones it claims that no longer happen.
- Client and server configuration: timeouts, retry counts and backoff, connection and thread pool sizes, circuit breaker settings, health check definitions, and queue bounds, read from configuration rather than from documentation.
- Placement facts: availability zone and region layout, cluster membership, database primaries and replicas, shared datastores, shared caches, DNS zones, certificate authorities, identity providers, and the deployment and configuration control planes.
- Observed dependency availability and latency with the query behind each figure, and third-party status history for external dependencies.
- Incident history with propagation paths, and the postmortems that recorded what actually spread.

## Workflow

**Outcome.** A dependency graph per journey with coupling strength on every edge, a ranked single-point-of-failure and shared-fate inventory, a failure-mode inventory with trigger, propagation, detection, mitigation, and residual risk per mode, an assessment of retry amplification and correlated failure, and the composed availability the graph implies against the objective the journey carries.

**Grounding.** Traces, configuration, and topology state what the system does; architecture documents state what someone designed. Where they disagree, both are recorded with attribution and the conflict is preserved per `references/suite-workflow-contract.md`. An edge that appears in traces and in no diagram is the finding.

**Constraints.** Classify every edge as hard, soft, or degraded-ok, and define the classification by what the user experiences rather than by how the call is written. A dependency is hard when its failure fails the journey, soft when the journey completes with reduced function, and degraded-ok when the journey completes with a stated and acceptable difference the product has agreed to. An asynchronous call is not automatically soft: a queue write that fails closed on a synchronous path is a hard dependency wearing asynchronous clothing.

Analyze shared fate by failure domain, not by component count. For every pair of components described as redundant, name the domain the redundancy spans and the domain it does not, and check the domains that sit underneath everything: identity, DNS, certificate issuance and expiry, secret distribution, configuration and feature flag delivery, the container registry, the deployment control plane, and the observability stack the responders will need while it is failing. A recovery path that depends on the failed component is a circular dependency and is called out by name, because it converts a degradation into an unrecoverable one.

Assess amplification arithmetic explicitly. Retries compose multiplicatively across layers, so independently reasonable retry policies at client, gateway, and service produce a load multiple on the dependency that is the product of the three, arriving exactly when that dependency is least able to serve it. Look for the shapes that make failure metastable rather than transient: retry storms, cache stampedes after a cold start, health checks that depend on the failing dependency and mark an entire fleet unhealthy at once, thundering herds on reconnect with synchronized backoff, and queues that keep accepting work faster than recovery can drain it.

Compose journey availability from the hard dependencies on the path and state the independence assumption in the same breath, because the multiplication is only valid where failures are independent, and shared fate is precisely the reason they are not. Where the composed figure sits below the journey's objective, that is a design finding of the first order and is stated plainly rather than absorbed into a rounding.

**Parallel surface.** Services, edges, dependencies, failure modes, and configuration reads are independent units and are parallel-safe; per-dependency observed-availability lookups, per-service configuration reads, and connector preflight across traces, topology, configuration, and incident history all fan out.

The aggregate work runs once after the fan-out returns: assembling per-edge findings into the journey graph, composing availability along the path, identifying shared fate across services that no single-service view can see, ranking single points of failure by the journeys and tiers they sit under, deriving the correlated-failure clusters, and reconciling propagation paths against incident history.

**Acceptance bar.** Every edge on a journey path has a coupling classification with the user-visible consequence behind it. Every redundancy claim names the failure domain it spans. Every failure mode states detection, including the ones detected by nothing. Composed availability names its inputs and its independence assumption, or is stated as uncomputable. Every observed availability figure names its query.

## Outputs

A complete run delivers this artifact set:

- `journey-dependency-graph.md`: per journey, the ordered path with every dependency, its kind, its coupling, the user-visible consequence of its failure, and the configured timeout and retry on the edge with the source of those values.
- `spof-shared-fate-register.md`: single points of failure and shared-fate clusters ranked by the tier and number of journeys behind them, each naming the failure domain, what the redundancy actually spans, and the recovery-path circularity where one exists.
- `failure-mode-inventory.md`: per mode, the trigger, the propagation path including correlated and metastable behavior, the detection signal or an explicit undetected marker, the mitigation that stops user impact, and the residual risk after that mitigation.
- `amplification-and-correlation-analysis.md`: the composed retry multiple per path with the layer values it came from, the synchronization and herd risks, the health-check and fate-sharing interactions, and the load a dependency sees during its own degradation.
- `composed-availability-assessment.md`: the availability the graph implies per journey, its inputs, the independence assumption, and the comparison against the objective with the gap stated.
- `dependency-analysis-downstream-handoff.md`: the failure modes and residual risks `resilience-architecture-desk` inherits as its work list, and the recovery ordering constraints `disaster-recovery-desk` inherits.

Depth standard per artifact: a graph entry that a responder can use during an incident to answer "if this is down, what does the user see", which requires the consequence, not just the edge. A failure mode with "detection: none" is a complete and valuable entry; a failure mode with a vague detection claim is not. A shared-fate entry names the concrete shared thing, since "these share infrastructure" hides whether the shared thing is a rack, a control plane, or a certificate.

In `diagnostic` mode, when traces, topology, or configuration exist and cannot be read, the run delivers `dependency-connector-diagnostic.md` reporting reachability, what was attempted, and the access needed. The graph is not asserted from architecture documents alone in that mode; it is labeled as documented intent awaiting confirmation.

A dependency graph is the artifact in this suite most easily completed from architectural intuition, and that is what makes it dangerous in both directions. Invented edges add fictional risk that consumes real engineering time; omitted edges are worse, because the graph is then used as the definitive answer to what breaks, and the missing edge is exactly the one that takes the journey down. The same applies to the numbers: multiplying four plausible availability figures produces a composed figure with four significant digits and no basis. So every edge names the trace, configuration file, topology record, or incident that established it; an edge suspected but unconfirmed is listed as suspected with the confirmation step named; every timeout, retry count, and pool size is read from configuration or written as unknown; and composed availability is computed only from observed figures that name their queries, and is otherwise stated as uncomputable with the missing inputs listed. A graph that admits it is incomplete can be finished. A graph that looks complete stops anyone from looking.

## reliability_packet fields to update

- `dependencies[]`: `name`, `kind`, `coupling`, `observed_availability`, `timeout_and_retry`, `blast_radius`.
- `failure_modes[]`: `id`, `trigger`, `propagation`, `detection`, `mitigation`, `residual_risk`.
- `reliability_risks[]` for single points of failure, shared-fate clusters, and journeys whose composed availability sits below their objective.
- `recovery.dependency_recovery_order` seeded with the ordering the graph implies for identity, DNS, data tier, and control plane.
- `reliability_surface` set to `dependency_analysis`.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: accepting a known single point of failure on a tier 0 journey as a residual risk requires the service owner or accountable leader, not this desk.
- Production or destructive: the next action would probe, fail, disable, or reconfigure a live dependency to confirm coupling, including toggling a client timeout or a health check to observe the effect.
- Security or privacy: mapping identity, secret distribution, or trust-root dependencies would expose credential paths, trust relationships, or an exploitable failure sequence in an artifact with wider circulation than the finding warrants.
- Source conflict: traces and topology records disagree with the architecture documentation on whether a hard dependency exists, so the journey's failure behavior is genuinely undetermined.
- Release integrity: a dependency would be recorded as redundant, isolated, or non-critical, or a composed availability asserted, without evidence establishing it.
- Connector unreachable: the trace store, topology source, configuration repository, or dependency status history exists and cannot be read, so the graph cannot be grounded in observed behavior.

Absent third-party availability history, missing traces on a low-volume path, and an undocumented external dependency owner are soft gaps: proceed with the edge marked as suspected or its availability unmeasured, and record the assumption where it was used. A coupling is never softened from hard to soft to make a composed figure clear an objective.

## Downstream handoffs

`resilience-architecture-desk` needs the failure-mode inventory and the coupling classification, since each mode is either absorbed by a control or accepted as residual risk. `capacity-planning-desk` needs the amplification analysis, because retry multiples change the load a dependency must be sized for. `chaos-resilience-testing-desk` needs the failure modes with their claimed mitigations as its hypothesis list. `disaster-recovery-desk` needs the graph and the circular-dependency findings to derive recovery order. `alerting-quality-desk` needs the undetected failure modes as its detection gap list. `runbook-engineering-desk` needs the propagation paths and mitigations. Cross-suite: architectural changes that remove a single point of failure go to the SDLC suite.

## Quality bar

A graph that matches what traces show rather than what the diagram claims. Coupling stated in terms of what the user loses. Shared fate named down to the specific shared component, including the ones nobody owns. Amplification worked out arithmetically rather than described as a concern. A composed availability that either names its inputs or admits it cannot be computed, and a gap against the objective that is stated rather than smoothed.
