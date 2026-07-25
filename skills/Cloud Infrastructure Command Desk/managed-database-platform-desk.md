---
name: managed-database-platform-desk
description: design managed database platforms, covering engine and service selection against the access pattern, instance sizing and storage configuration, high-availability topology across failure domains, read replica placement and replication lag, backup and point-in-time recovery windows measured against stated rto and rpo, parameter baselines and the static settings that require a reboot, connection limits and pooling, major version upgrades against provider end-of-support dates, and database credential handling. use for database engine selection, ha topology, replica design, pitr and backup windows, parameter tuning, connection exhaustion, and version end-of-life upgrades.
---

# Managed Database Platform Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the database artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Never invent instance identifiers or endpoints, engine versions, end-of-support dates, parameter names or values, connection limits, backup retention periods, recovery window figures, replication lag measurements, or the date of any failover or restore exercise.

## Role

Own the managed data engines and the recovery they actually provide. This desk selects the engine and service against the access pattern, sizes instances and storage, designs the high-availability topology across failure domains, places read replicas and states their replication lag behavior, sets backup and point-in-time recovery windows measured against the recovery objectives from intake, defines parameter baselines and identifies the settings whose change requires a restart, sets connection limits and the pooling that keeps within them, plans major version upgrades against provider end-of-support dates, and specifies how applications authenticate to the database.

The gap this desk exists to close is between a recovery objective and a recovery mechanism. A recovery point objective of five minutes is a statement about transaction log retention and replication lag, not about whether backups are enabled. A recovery time objective is a statement about restore duration at the current data volume plus the time to repoint every client, because a managed restore creates a new instance with a new endpoint rather than returning the old one. Objectives that were never translated into those numbers are the most common finding here, and they are usually found during the incident.

## Use when

- An engine or managed service is being selected against an access pattern, consistency requirement, or scaling shape.
- Instance sizing, storage type, provisioned throughput, or storage autoscaling is being decided or revisited.
- High-availability topology is being designed, or a failover has never been tested and its duration is unknown.
- Read replicas are being placed, replication lag is unbounded, or a replica is being considered for promotion.
- Backup retention or point-in-time recovery is being set or checked against a stated recovery objective.
- Parameter baselines are being defined, or a change is needed and the static-versus-dynamic distinction decides whether it costs a restart.
- Connections are exhausting, or pooling needs introducing between an application and an engine whose limit derives from instance memory.
- A major version is approaching or past end of support, extended support is being billed, or the provider has scheduled a forced upgrade.

## Do not use when

- The subject is object, block, or file storage and its backup destinations. That is `cloud-storage-data-services-desk`, whose backup and key ownership model this desk inherits.
- The subject is the private endpoint, subnet placement, or firewall path to the database. That is `cloud-network-architecture-desk`.
- The subject is regional failover mode, replication topology across regions, and the exercised-versus-aspirational split. That is `resilience-multi-region-desk`, which measures this desk's output against the objectives.
- The subject is the schema, query design, data model, or application-level access pattern. That is a labeled cross-suite handoff to the Data or SDLC suites.
- The subject is the secret that holds a database password and its rotation. That is `configuration-secrets-desk`.

## Required evidence

- The database inventory: instances and clusters with engine, exact version, instance class, storage type and size, allocated and used throughput, region and zone placement, and account.
- Provider lifecycle data: the end-of-support or end-of-life date for every version in use, the extended support terms and whether they are already being billed, and any forced upgrade date already scheduled.
- High-availability configuration: the standby or zone-redundant topology, synchronous or asynchronous replication mode, the failover mechanism, and the failover history with measured durations.
- Replica inventory: placement, replication mode, current and peak replication lag, and the promotion procedure.
- Backup configuration: automated backup window, retention period, snapshot inventory and ages, the transaction log retention that actually bounds the point-in-time recovery window, and cross-region or cross-account copies.
- Restore evidence: the date a restore was last executed, the measured duration at the data volume involved, and what was restored.
- Parameter state: the parameter group or configuration set in force, its deviations from the default, which of those are static, and any pending change waiting on a restart.
- Connection state: the effective connection limit and how it is derived, observed concurrent connections against it, pooler presence and configuration, and connection error history.
- Performance evidence: processor, memory, storage throughput, input and output operations, buffer or cache hit behavior, lock waits, and the storage growth rate against the storage ceiling.
- Access configuration: authentication mode, whether credentials are static passwords or short-lived tokens, transport encryption enforcement, and encryption at rest with its key owner.
- Recovery objectives and data classification from intake, and the key ownership and backup destination model from the storage stage.

## Workflow

**Outcome.** An engine and sizing decision with its evidence, a high-availability topology with a measured or explicitly unmeasured failover duration, replica placement with a stated lag budget, backup and point-in-time recovery windows expressed as the actual retention that bounds them and compared against the recovery objectives, a parameter baseline with its static settings flagged, connection limits with the pooling that respects them, an upgrade plan against published end-of-support dates, and a credential and encryption model.

**Grounding.** Recovery windows are read from the configured retention and the transaction log retention rather than from the recovery objective they are supposed to serve, and the two are compared explicitly so a shortfall appears as a finding rather than as an assumption of adequacy. Failover duration comes from failover history where it exists; where it does not, the topology is described as untested rather than assigned a typical figure. Connection limits are read from the effective value in force, since that value is frequently derived from instance memory and changes silently when the instance is resized. Where the parameter group and the running configuration disagree because a static change is pending a restart, record both and preserve the conflict, because that pending change will apply during the next maintenance window whether or not anyone is expecting it.

**Constraints.** Every recovery claim states the mechanism and the number behind it: the retention that bounds the point-in-time window, the measured restore duration at current data volume, and the client repointing time, since a managed restore produces a new endpoint and the recovery time objective is not met until traffic reaches it. Replica entries state the lag under peak load rather than at rest, and any replica considered for promotion states the data loss its current lag implies. High-availability topology names the failure domains it spans and what a zone loss actually removes, distinguishing a synchronous standby from an asynchronous replica because only one of them bounds data loss. Parameter baselines separate static from dynamic settings and name the restart each static change costs, and a pending static change is recorded as a scheduled restart with a date. Connection limits are stated with their derivation and compared against observed peak concurrency, with pooling placed where the connection count is actually generated. Storage configuration states the growth rate against the ceiling, because a full storage volume takes the engine read-only and that failure looks like an application bug for the first twenty minutes. Version entries carry the published end-of-support date and the extended support billing status.

**Parallel surface.** Independent instances, clusters, replicas, parameter groups, and engines are independent assessment units and fan out safely, as does the per-instance read of configuration and performance evidence. The estate-wide upgrade sequence against end-of-support dates, the aggregate recovery position measured against the objectives, and the cross-database dependency judgment where one application spans several engines run once after the fan-out returns, because a per-instance recovery statement cannot see that two databases must be recovered to a consistent point together and neither backup schedule was aligned to make that possible.

**Ordered gate for a major version upgrade.** A managed major version upgrade is one-way: the engine cannot be downgraded in place, and the only rollback is restoring the pre-upgrade snapshot to a new instance with a new endpoint, which means rollback costs a second client cutover. That is why this order is mandated and why step 3 is the point past which recovery means restore rather than revert:

1. Establish the target version's breaking changes against this workload, including removed parameters, changed defaults, extension and collation compatibility, and any behavior the application depends on, and run the provider's pre-upgrade checks.
2. Take a snapshot immediately before the upgrade and confirm it is restorable, since it is the only rollback that exists, and confirm the client repointing path is ready for the endpoint the rollback would create.
3. Upgrade in a lower environment carrying representative data volume and query mix first, and measure the actual upgrade duration there, because the maintenance window has to be sized from a measurement rather than from an estimate.
4. Upgrade production inside the approved window, then rebuild replicas, reapply the parameter baseline against the new version's defaults, and confirm the connection limit did not change with the instance.

Deleting an instance, dropping a replica, or reducing backup retention follows the destructive sequence in `references/suite-workflow-contract.md` instead of this one.

**Acceptance bar.** A reader could state, per database, how much data is lost in the worst case, how long recovery takes including client repointing, when the engine version stops being supported, and how many connections the instance will actually accept. Every recovery figure names its mechanism, every failover duration is measured or explicitly untested, and every version carries a dated support position.

## Outputs

A complete run delivers this set:

- `engine-selection.md`: the engine and service per workload with the access pattern, consistency requirement, and operational consequence behind the choice.
- `sizing-and-storage.md`: instance class, storage type and throughput, the performance evidence behind the sizing, the storage growth rate against the ceiling, and the autoscaling behavior if any.
- `ha-topology.md`: the standby or zone-redundant layout, synchronous against asynchronous replication, the failure domains spanned, and the failover duration as measured or explicitly untested.
- `replica-plan.md`: replica placement, replication mode, lag under peak load, the lag budget, and the data loss a promotion at current lag would cause.
- `recovery-windows.md`: backup retention, transaction log retention as the real bound on point-in-time recovery, measured restore duration at current data volume, client repointing time, and the comparison against the recovery objectives from intake with any shortfall named.
- `parameter-baseline.md`: settings in force, deviations from default with the reason, static settings flagged with the restart each costs, and any pending change waiting on a maintenance window.
- `connection-model.md`: the effective connection limit and its derivation, observed peak concurrency, pooler placement and configuration, and the failure behavior at exhaustion.
- `version-upgrade-plan.md`: current versions with published end-of-support dates, extended support billing status, breaking changes per target version, and the upgrade sequence with measured durations where available.
- `database-access-model.md`: authentication mode, the path away from static passwords, transport encryption enforcement, and encryption at rest with its named key owner.
- `database-downstream-handoff.md`: what `resilience-multi-region-desk` inherits, including per-database lag budgets, measured recovery figures, and the shortfalls against objectives.

Depth standard: an artifact is complete when a database engineer could implement it and an incident commander could act on it, both unchanged. A recovery window with no retention figure behind it, a failover topology with no duration, and a version with no dated support position are unfinished rather than draft.

When the database inventory, configuration, performance telemetry, backup history, or provider lifecycle calendar exists and cannot be read, the run delivers `database-connector-diagnostic.md` naming each unreachable source and the recovery or version claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: the numbers this desk produces are the ones an incident commander reads under pressure, and the specific failure is arithmetic that looks like measurement. Writing a recovery point objective of five minutes because point-in-time recovery is enabled, or a failover of about sixty seconds because that is the usual figure for this class of service, converts an unknown into a commitment that an outage will disprove. Recovery point comes from the transaction log retention and the replication lag actually observed; recovery time comes from a restore that was executed, at this data volume, with the client repointing counted. Where either is unmeasured, it is recorded as unmeasured with the exercise that would establish it, and the shortfall against the stated objective is left visible rather than reconciled. End-of-support dates, engine versions, parameter names and values, and connection limits are transcribed from the inventory and the provider's published calendar or left unresolved, because a parameter value invented into a baseline document is applied by someone who trusts it, and a static parameter applied wrongly reboots production during the next maintenance window with no obvious link back to the document that caused it.

## infrastructure_packet fields to update

- `data_stores[]` for each engine with `kind`, `engine_and_version` including its end-of-support date, `ha_topology`, `backup_policy`, `restore_tested`, and `encryption` with key ownership
- `resilience.replication_lag_budget` per replicated data store
- `resilience.availability_target` context where measured recovery contradicts the stated objective
- `workload_profile.rto` and `workload_profile.rpo` annotated with the measured mechanism behind each, never overwritten
- `secrets_and_config.dynamic_credentials` where token-based authentication replaces stored passwords
- `posture[]` entries for unencrypted transport, static database credentials, or publicly reachable endpoints
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would upgrade a live engine, apply a static parameter change, resize or fail over an instance, promote or drop a replica, reduce backup retention, or delete a snapshot.
- **Release integrity**: a recovery point or recovery time objective would be declared met without the retention figure, the measured restore, and the repointing time behind it, or a failover capability declared without an exercise.
- **Security or privacy**: continuing would assert encryption, credential handling, or network exposure as verified without configuration evidence, or would place database credentials or sample data into an artifact.
- **Missing approval**: a major version upgrade, a maintenance window that reboots production, a retention reduction, or acceptance of extended support billing needs a named owner who has not authorized it.
- **Source conflict**: the inventory, the parameter group, and the running configuration genuinely disagree, and choosing one silently would hide a pending static change that reboots the instance at the next window.
- **Connector unreachable**: the database inventory, configuration, performance telemetry, backup and restore history, or provider lifecycle calendar exists and cannot be read.

Unknown historical parameter intent, missing query-level performance evidence, and undocumented schema ownership are soft gaps. Name them, label the assumption, and continue. Recovery objectives, encryption obligations, and upgrade approval are never relaxed to keep a workflow moving; a shortfall against an objective is reported, not narrowed.

## Downstream handoffs

`resilience-multi-region-desk` is next and needs the per-database lag budgets, the measured recovery figures, the failover durations, and every shortfall against a stated objective, because those are the raw material for its exercised-versus-aspirational split. `cloud-storage-data-services-desk` receives the backup destination and retention requirements that its vaults must satisfy. `configuration-secrets-desk` inherits the static database credentials found here and the token-based path replacing them. `cloud-security-posture-desk` inherits unencrypted transport, static credential, and public endpoint findings. `cloud-cost-rightsizing-desk` inherits the sizing evidence and the extended-support billing exposure. `infrastructure-as-code-desk` needs the parameter baselines to bring under code so a manual parameter change becomes visible drift. Send schema design, query optimization, and data modeling to the Data suite as a labeled cross-suite handoff.

## Quality bar

Good database platform work is numeric where it matters and silent where it does not know. It states the worst-case data loss as a figure derived from log retention and observed lag, and the recovery time as a duration measured at the real data volume with the client cutover counted. It flags the static parameters, because those are the changes that reboot production without anyone connecting the reboot to a document written months earlier. It carries end-of-support dates as dates. And where an objective and a mechanism disagree, it says so plainly and leaves the gap open, since a recovery objective quietly rounded down to what the current configuration provides is how an organization discovers during an outage that nobody ever built what was promised.
