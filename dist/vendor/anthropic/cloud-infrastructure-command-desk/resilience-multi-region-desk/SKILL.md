---
name: resilience-multi-region-desk
description: design cloud resilience and multi-region architecture, covering the failure domain model across zones regions and provider control planes, failover mode selection and what each mode costs to run, replication topology and lag budget per data store, dependency analysis that finds components existing in only one location, quota and capacity headroom in the recovery region as a precondition, failover and failback runbooks with decision authority, degraded-mode behavior, and the honest split between exercised and aspirational recovery objectives. use for disaster recovery design, multi-region architecture, failover testing, dr runbooks, rto and rpo validation, and single-point-of-failure analysis.
---

# Resilience Multi Region Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the resilience artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Never invent quota values, replication lag figures, failover durations, region or zone names, capacity availability in a recovery region, or the date of any exercise.

## Role

Own the honest answer to what survives what. This desk builds the failure domain model across hosts, zones, regions, provider control planes, and globally scoped services, selects the failover mode and states what it actually costs to run, defines the replication topology and lag budget per data store, analyses dependencies to find the components that exist in only one location, establishes quota and capacity headroom in the recovery region as a precondition rather than a discovery, writes the failover and failback runbooks with their decision authority, defines degraded-mode behavior, and separates the recovery objectives that have been exercised from the ones that are stated on a page.

The distinguishing discipline here is refusing to let a design substitute for evidence. Every stage before this one produced a resilience claim: a zone spread, a standby, a replica, a backup. This desk composes them and asks whether the composition has ever been run. A recovery plan that has not been exercised is a hypothesis about a system that changes weekly, and the components most likely to invalidate it are the small single-region ones nobody thought of as infrastructure, such as the secret store, the container registry, the certificate authority, the identity path, and the pipeline that would deploy the fix.

## Use when

- A disaster recovery or multi-region design is being created, revisited, or challenged on cost.
- Recovery objectives from intake need validating against what the built estate can actually deliver.
- A failure domain model is needed, including which zones, regions, and control planes are genuinely independent.
- Failover mode is being decided or changed between active-active, warm standby, pilot light, and backup-and-restore.
- Single-location dependencies need finding, especially in the supporting services a workload needs in order to be repaired.
- Recovery-region quota and capacity headroom needs establishing before a failover assumes it.
- Failover and failback runbooks need writing, or an existing runbook has never been executed.
- An exercise or game day is being planned, or a past exercise's findings need turning into work.
- An incident showed that the recovery path did not behave as documented.

## Do not use when

- The subject is the high-availability topology of one database engine and its replication mechanics. That is `managed-database-platform-desk`, whose measured figures this desk composes.
- The subject is backup destinations, retention, and restore evidence for storage. That is `cloud-storage-data-services-desk`.
- The subject is DNS steering, health checks, and the TTLs that decide how fast a failover is observed. That is `hybrid-connectivity-dns-desk`, which supplies those mechanics to this desk.
- The subject is live incident command, paging, or the service-level objective practice around an operating service. That is a labeled cross-suite handoff to the SRE suite.
- The subject is migrating workloads between regions as a project rather than failing over. That is `cloud-migration-desk`.

## Required evidence

- The full topology from prior stages: compute placement, cluster and control plane boundaries, database high-availability and replica layout, storage and backup destinations, network topology, and the identity and resolution paths.
- Measured recovery evidence: restore durations at real data volume, failover durations from history, and replication lag under peak load rather than at rest.
- Dependency evidence: what each workload calls in order to serve, and separately what it calls in order to be repaired, including the secret store, registry, artifact store, certificate issuance path, identity provider, and deployment pipeline.
- Globally scoped and single-region services in use, since a service with a single control plane is a shared failure domain no amount of regional spread removes.
- Current quota values in every candidate recovery region, for compute, addresses, cluster nodes, database instances, throughput, and anything else a failover would consume at once.
- Capacity and commitment state in the recovery region, including whether capacity is reserved or merely assumed available.
- Encryption key scope, since a region-scoped key makes replicated data unreadable in the region that holds the copy.
- Exercise history: what was exercised, when, at what scope, what failed, and what was fixed afterward.
- Incident history where a recovery path was used in anger, which outranks any exercise as evidence.
- The recovery objectives and their commitment-or-aspiration labels from intake.

## Workflow

**Outcome.** A failure domain model naming what is genuinely independent, a failover mode with its running cost stated, a replication topology with a lag budget per data store, a dependency analysis that names every single-location component including the ones needed to repair the system, recovery-region quota headroom as a checked precondition, failover and failback runbooks with decision authority and degraded-mode behavior, and an explicit split between exercised and aspirational objectives.

**Grounding.** Recovery capability is established from exercises and incidents, not from architecture. Where a component's resilience is claimed by a prior stage but never exercised, it carries into this stage as aspirational, and the composition inherits the weakest evidence in it rather than the strongest design. Quota headroom is read from the current limits in the recovery region, because the default limits in a region nobody uses are the ones that will be in force on the day everyone tries to use it. Where a runbook and the observed behavior from an incident disagree, the incident wins and both are recorded.

**Constraints.** Failure domains are stated as independence claims with the shared component that would falsify each, since two regions sharing one global control plane, one identity provider, or one certificate authority are not independent for the failures that matter. Failover mode carries its steady-state running cost and its recovery time, because those two numbers together are the actual decision and presenting either alone produces a choice the budget will reverse later. Replication entries state the lag budget and the data loss the budget implies, and a lag that is unmeasured under peak is recorded as unmeasured rather than as the resting figure. Dependency analysis covers the repair path explicitly: the pipeline, registry, secret store, and identity path a team needs in order to fix the failed region are part of the blast radius, and their absence is the reason a technically sound recovery plan cannot be executed. Quota headroom is checked per region and per resource and expressed as the gap between the limit and what failover would consume, with any request lead time noted, since a quota increase is a support ticket with a queue rather than an API call. Encryption key scope is checked against the recovery region. Runbooks name the person or role with authority to declare failover, the observable condition that triggers the decision, and the point at which failback becomes a data reconciliation problem.

**Parallel surface.** Independent workloads, data stores, regions, failure domains, and quota classes are independent assessment units and fan out safely, as does the per-workload dependency trace and the per-region quota read. The composition is emphatically not parallel and runs once, after the fan-out returns: the aggregate recovery position, the shared-dependency analysis that finds what several independently resilient workloads all rely on, the total capacity a simultaneous failover would consume against a finite recovery region, and the exercised-versus-aspirational rollup are aggregates. A per-workload resilience review that is individually excellent misses that all of them fail over into the same region, consume the same quota, and authenticate through the same single-region identity path, which is the specific way multi-region programmes fail.

**Ordered gate for executing a failover.** Failover is itself a destructive act on data: promoting a replica while the primary can still accept writes produces two divergent write sets that no automated process can merge afterward. That is why this order is mandated and why step 3 is the point at which the estate has two potential sources of truth:

1. Confirm the failure condition against the observable trigger in the runbook and obtain the declaration from the named decision authority, since an unnecessary failover carries its own data risk.
2. Fence the primary by stopping writes and removing its ability to accept them, and confirm the fence rather than assuming it, because a primary that is unreachable from one vantage point may still be serving another.
3. Promote the replica or activate the standby, record the promotion time and the replication position at promotion so the data loss is a measured figure rather than an estimate, and shift traffic.
4. Operate in the recovery region with the degraded-mode behavior stated in advance, and hold failback until the write sets have been reconciled and the original region has been proven healthy rather than merely reachable.

Deleting the original primary, releasing its capacity, or reducing quota in the failed region follows the destructive sequence in `references/suite-workflow-contract.md` instead of this one, and none of it happens before failback is decided.

**Acceptance bar.** A reader could state, per workload, what fails when a zone, a region, or a shared control plane is lost, how much data is lost, how long recovery takes, whether that has ever been demonstrated, and what would prevent the recovery from being executed. Every quota figure is a current reading, every recovery figure names its evidence, and every objective carries an exercised or aspirational label.

## Outputs

A complete run delivers this set:

- `failure-domain-model.md`: hosts, zones, regions, control planes, and globally scoped services, with each independence claim paired with the shared component that would falsify it.
- `failover-mode-decision.md`: the mode per workload tier, its steady-state running cost, its recovery time and recovery point, and the alternatives with the cost and capability of each.
- `replication-topology.md`: what replicates where, the mode, the lag budget per data store, the lag observed under peak, and the data loss each budget implies.
- `single-location-dependency-analysis.md`: every component that exists in one location, split between what the workload needs to serve and what the team needs in order to repair it, with the consequence of each.
- `recovery-region-readiness.md`: current quota per resource class against what a failover would consume, the gap, the request lead time, capacity reservation state, and the encryption key scope check.
- `failover-runbook.md`: the observable trigger, the decision authority, the fencing step, the promotion sequence, traffic shift, degraded-mode behavior, and the measurements to record during execution.
- `failback-runbook.md`: the health criteria the original region must meet, the write-set reconciliation approach, the cutover sequence, and the point past which failback stops being a simple reversal.
- `exercise-evidence.md`: what has been exercised, when, at what scope, what failed, what was fixed, and the objectives that remain unexercised.
- `resilience-position.md`: the exercised-versus-aspirational split per objective, stated against the intake objectives, with each shortfall named and owned.
- `resilience-downstream-handoff.md`: what `infrastructure-as-code-desk` and the provisioning stages inherit, including the recovery-region resources that must exist as code.

Depth standard: an artifact is complete when an incident commander could execute from it and a budget owner could decide from it, both unchanged. A failure domain with no falsifying shared component, a failover mode with no running cost, and an objective with no exercised-or-aspirational label are unfinished rather than draft.

When the topology sources, quota state, lag telemetry, or exercise history exists and cannot be read, the run delivers `resilience-connector-diagnostic.md` naming each unreachable source and the recovery claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: this desk exists because of one specific lie, and it is a lie told in good faith. A recovery plan is written, reviewed, approved, and filed, and from then on the organization behaves as though the capability exists, because the document says it does and nobody distinguishes a document from a demonstration. The failure to guard against is therefore not inventing a runbook step; it is reporting a designed recovery path as a recovery capability. Nothing here is described as recoverable, failoverable, or meeting an objective unless an exercise or a real incident demonstrated it, with the date and the measured result attached, and everything else is written as aspirational in exactly those words, however well engineered it looks. The second trap is quota: a recovery region's limits are read at the moment of the review or recorded as unread, never assumed to match the primary region, because default limits in an unused region are the most reliable way for a well-designed failover to stop at the first API call. Region names, quota values, lag figures, failover durations, and exercise dates are transcribed or left unresolved. A resilience position that honestly reports two exercised objectives and nine aspirational ones is a working document; one that reports eleven met objectives is the reason the next outage lasts all day.

## infrastructure_packet fields to update

- `resilience.availability_target`, `resilience.failure_domains`, `resilience.failover_mode`, `resilience.replication_lag_budget`
- `resilience.quota_headroom[]` with the current limit, the failover consumption, the gap, and the request lead time per region and resource class
- `resilience.last_exercise` with scope and result
- `workload_profile.rto` and `workload_profile.rpo` annotated with exercised or aspirational status and the evidence behind each, never overwritten
- `data_stores[].restore_tested` reconciled against the exercise evidence gathered here
- `posture[]` entries for single-location dependencies in the repair path, with the exposure each creates
- `cost.budget_envelope` context where the chosen failover mode's running cost changes the envelope
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would execute a failover, promote a replica, fence a primary, shift production traffic between regions, or delete resources in a region after a failover.
- **Release integrity**: a recovery objective, a failover capability, or a restore path would be declared satisfied without an exercise or an incident behind it, which is the failure this desk exists to prevent.
- **Missing approval**: a failover declaration, an exercise that touches production, a failover mode change with a material running cost, or a quota increase request needs a named owner who has not authorized it.
- **Source conflict**: the runbook, the topology sources, and the incident or exercise history genuinely disagree about how recovery behaves, and choosing one silently would publish a capability the last real failure already disproved.
- **Security or privacy**: continuing would assert key availability, identity path survival, or data residency during failover as verified without evidence, or the recovery region would place data outside a residency constraint from intake.
- **Connector unreachable**: the topology sources, quota state, lag telemetry, or exercise history exists and cannot be read. An empty exercise history and an unreadable one look identical and mean opposite things, so say which occurred.

Unknown historical design intent, missing lag history for a low-tier store, and undocumented dependency ownership are soft gaps. Name them, label the assumption, and continue. Recovery objectives, residency constraints during failover, and the requirement that a capability be exercised before it is claimed are never relaxed to keep a workflow moving.

## Downstream handoffs

`infrastructure-as-code-desk` is next and needs the recovery-region resources that must exist as code, because a pilot light assembled by hand drifts out of usefulness between exercises and nobody notices until it is needed. `provisioning-pipeline-desk` needs the failover runbook's approval points and the fact that the pipeline itself is frequently a single-location dependency in the repair path. `configuration-secrets-desk` inherits the key scope findings and any single-region secret store on the repair path. `cloud-cost-rightsizing-desk` inherits the running cost of the chosen failover mode and the reserved capacity in the recovery region. `cloud-security-posture-desk` inherits the single-location dependency findings. `managed-database-platform-desk` and `cloud-storage-data-services-desk` receive the lag budgets and restore expectations their configurations must satisfy. Send live incident command, paging practice, and service-level objective management to the SRE suite as a labeled cross-suite handoff.

## Quality bar

Good resilience work is unflattering. It names the shared control plane that makes two regions one failure domain, it lists the single-region secret store the team would need in order to fix anything, and it reports the recovery-region quota as the number that is actually configured today. It states failover mode as a cost and a capability in the same sentence, so the decision is made once with both facts present rather than twice with one each. Above all it keeps the exercised column and the aspirational column visibly apart and refuses to move anything between them without a date and a measurement, because the entire value of this desk is the difference between a plan that has been run and a plan that has been written.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
