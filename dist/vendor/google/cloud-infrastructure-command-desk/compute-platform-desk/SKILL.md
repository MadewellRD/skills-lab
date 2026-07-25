---
name: compute-platform-desk
description: select and size cloud compute, covering platform choice across virtual machines autoscaling groups serverless functions and managed container runtimes, instance family and size rationale from utilization evidence, machine image lineage and the rebuild path, autoscaling triggers bounds and cooldowns with health check grace, interruptible capacity mix and its resilience cost, placement across availability zones and failure domains, and the patch and provider-forced upgrade path. use for compute platform selection, instance sizing, autoscaling policy, golden image pipelines, spot capacity strategy, and instance retirement planning.
---

# Compute Platform Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the compute artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Never invent instance families or sizes, image identifiers or versions, utilization figures, scaling thresholds, interruption rates, availability zone names, quota limits, or provider retirement dates.

## Role

Own what the workload runs on and how it survives the platform underneath it changing. This desk selects the compute platform per workload, chooses instance families and sizes with the reason each was chosen, defines the machine image lineage and the path that rebuilds it, sets autoscaling triggers, bounds, and cooldowns, decides the interruptible-capacity mix and states what it costs in resilience, places capacity across failure domains, and documents the patch and upgrade path including what the provider will force and when.

The recurring mistake in compute is treating the instance as the unit of design. The real unit is the replacement cycle: a provider will retire a hardware generation, force a host maintenance event, or reclaim interruptible capacity on its own schedule, and the only question that matters is whether the fleet can be rebuilt from source on demand. A perfectly sized instance that nobody can recreate is a liability with good utilization figures.

## Use when

- Compute platform selection is open for a workload, including managed runtime against self-managed instances against event-driven functions.
- Instance families and sizes are being chosen or revisited, and utilization evidence exists or needs gathering.
- Autoscaling is being designed or is misbehaving: wrong trigger, wrong bounds, thrash, or instances terminated before they finish starting.
- Machine images are being defined, their lineage is unclear, or nobody can rebuild the current image from source.
- Interruptible capacity is being introduced or expanded, and the resilience consequence needs stating rather than assuming.
- Placement across availability zones and failure domains needs deciding, including spread and partition requirements.
- A provider retirement, forced host maintenance, or runtime end-of-support has a date on it and the fleet needs a path off.

## Do not use when

- The subject is cluster topology, node groups, cluster version upgrades, or in-cluster scheduling. That is `container-platform-desk`; this desk owns the machines and capacity model, that desk owns the orchestrator on top.
- The subject is which subnet, zone, or address range compute lands in. That is `cloud-network-architecture-desk`, whose layout this desk consumes.
- The subject is commitment and reservation coverage or rightsizing driven by billing data. That is `cloud-cost-rightsizing-desk`; this desk states the capacity model, that desk buys against it.
- The subject is regional failover mode and recovery-region capacity headroom. That is `resilience-multi-region-desk`.
- The subject is the workload identity a compute instance assumes. That is `cloud-identity-access-desk`.

## Required evidence

- The current compute inventory: instances, scaling groups, functions, and managed runtimes with their families, sizes, counts, ages, and accounts.
- Utilization telemetry over a window long enough to include peak and periodic load: processor, memory, network, storage throughput, and queue depth or concurrency where the workload is not processor-bound.
- Scaling configuration at applied values: policies, metrics, thresholds, minimum and maximum bounds, cooldowns, health check type and grace period, and the scaling history showing what actually fired.
- Machine image inventory: images in use, their lineage back to a base, the build definition and whether it still runs, the patch level, and any deprecation or expiry the provider has set.
- Interruptible capacity state where used: the instance pools in use, the diversification across families and zones, the interruption notice handling, and the observed interruption history.
- Capacity and quota state per account and region, including limits that would block scaling before the configured maximum is reached.
- Provider lifecycle notices: instance generation retirements, forced maintenance events, runtime end-of-support dates, and any migration deadline already communicated.
- Placement requirements from the workload: affinity, anti-affinity, licensing constraints tied to hosts, and latency sensitivity between components.
- The subnet and availability zone layout from the network stage, and the workload identity mechanism from the identity stage.

## Workflow

**Outcome.** A compute platform decision per workload with its reasoning, instance families and sizes justified from utilization evidence, an image lineage with a working rebuild path, autoscaling configuration whose triggers match how the workload actually saturates, an interruptible-capacity mix with its resilience cost stated, placement across failure domains, and an upgrade path that names every provider-forced date already known.

**Grounding.** Sizing comes from utilization telemetry over a window that includes peak and periodic load, not from the current instance size, because the current size is usually the previous guess. Where the workload saturates on something other than processor, the sizing rationale names that dimension explicitly. Image lineage is established by tracing the running image back to a build definition that still executes; an image whose build no longer runs is recorded as unreproducible, which is a finding rather than a footnote. Where the declared scaling configuration and the scaling history disagree about what actually triggers, record both and preserve the conflict.

**Constraints.** Every family and size names the evidence and the constraint that selected it, and a size chosen for headroom states the headroom it buys. Autoscaling states its trigger metric, its bounds, its cooldown, and its health check grace period together, since a grace period shorter than the boot and warm-up time produces a group that terminates healthy instances forever and looks like a capacity problem. Bounds are checked against the account and regional quota that would stop scaling before the maximum is reached, because a maximum above the quota is a number that has never been true. Interruptible capacity states the diversification across families and zones, the interruption handling, and the fraction of the fleet that may disappear at once, and a single-instance-type interruptible fleet is recorded as a correlated failure rather than as a cost optimization. Image lineage names the base, the build definition, the patch level, and the rebuild path, and any provider deprecation date on the image or its base is carried as a dated obligation. Placement states the failure domain spread and what a single zone loss removes.

**Parallel surface.** Independent workloads, scaling groups, instance families, images, and accounts are independent assessment units and fan out safely, as does per-workload utilization analysis. The aggregate capacity picture against account and regional quota, the correlated-failure judgment across everything sharing an instance family or an interruptible pool, and the fleet-wide image lineage rollup run once after the fan-out returns, because per-workload sizing that is individually reasonable can still exceed a shared quota or concentrate the whole estate on one family that the provider is about to retire.

**Acceptance bar.** An engineer could provision the fleet from these artifacts and an operations owner could say what happens when a zone fails, when interruptible capacity is reclaimed, and when the provider retires the current generation. Every size names its utilization evidence, every image names its rebuild path, and every scaling bound has been checked against the quota that governs it.

## Outputs

A complete run delivers this set:

- `compute-platform-selection.md`: the platform chosen per workload, the alternatives considered, and the operational and cost consequence of the choice.
- `instance-sizing-rationale.md`: family and size per workload with the utilization evidence, the saturating dimension, and the headroom the choice buys.
- `machine-image-lineage.md`: images in use, their base, the build definition and whether it still runs, patch level, deprecation dates, and the rebuild path with its owner.
- `autoscaling-policy.md`: trigger metrics, thresholds, bounds checked against quota, cooldowns, health check grace, warm-up behavior, and the scaling history that corroborates or contradicts the configuration.
- `capacity-model.md`: the on-demand, reserved, and interruptible mix, the diversification behind any interruptible portion, the interruption handling, and the fraction of fleet that can be reclaimed at once.
- `failure-domain-placement.md`: zone and placement strategy per workload and what a single domain loss removes.
- `upgrade-and-retirement-path.md`: patch cadence and owner, runtime end-of-support dates, provider generation retirements and forced maintenance already announced, and the fleet's path off each.
- `compute-downstream-handoff.md`: what `container-platform-desk` inherits, including the node capacity model and image lineage the cluster will build on.

Depth standard: an artifact is complete when a platform engineer could build the fleet and an operations owner could run it, both without a follow-up round trip. A size with no utilization evidence, an image with no rebuild path, and a scaling bound never checked against quota are unfinished rather than draft.

When the compute inventory, utilization telemetry, image build definitions, or quota state exists and cannot be read, the run delivers `compute-connector-diagnostic.md` naming each unreachable source and the sizing or capacity claims that depend on it, in place of the artifacts that source would have grounded. Sizing is never presented as evidence-based against telemetry that could not be read.

Anti-fabrication guard: instance families and sizes have a naming grammar that is trivially easy to extend, and a machine can produce a plausible identifier for a size that the provider does not offer, or offers everywhere except the region the design targets. That is the specific failure here: a sizing table that reads as a decision, gets pasted into a module, and fails at apply time in one region while succeeding in the others, which is the most confusing possible way to find out. Every family, size, and image identifier is transcribed from the inventory, the provider catalogue as read, or the source that produced it, and where the catalogue was not consulted the requirement is expressed in processor, memory, and throughput terms with the selection left open. Utilization figures carry the metric, the window, and the telemetry source; a percentage with no window behind it is not evidence, and a rightsizing recommendation built on one is a performance incident with a spreadsheet behind it. Provider retirement and end-of-support dates are quoted from the notice or recorded as unconfirmed, because an invented date either creates a false emergency or, far worse, a false sense of time remaining.

## infrastructure_packet fields to update

- `compute[]` with `platform`, `image_or_runtime`, `sizing`, `scaling_policy`, `capacity_model`, and `upgrade_path` per workload
- `resilience.failure_domains` extended with the compute placement spread and any correlated-failure concentration found
- `resilience.quota_headroom` for the limits that bound scaling in each region
- `cost.rightsizing_candidates` where utilization evidence supports a change, with the evidence attached
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would resize, replace, or terminate running instances, change scaling bounds on a live group, replace the image a running fleet rebuilds from, or shift production capacity onto interruptible pools.
- **Missing approval**: an instance generation migration, a capacity commitment, a move to interruptible capacity for a production tier, or a maintenance window needs a named owner who has not authorized it.
- **Security or privacy**: continuing would assert image provenance, patch level, or workload credential handling as verified without source evidence, or an image or user data payload contains embedded credentials.
- **Source conflict**: the inventory, the scaling configuration, and the scaling history genuinely disagree about what the fleet is or what triggers it, and choosing one silently would size against a fleet that does not exist.
- **Release integrity**: a rebuild path, a patch cadence, or a capacity claim would be declared satisfied without evidence that the build actually runs or the quota actually allows it.
- **Connector unreachable**: the compute inventory, utilization telemetry, image build definitions, quota state, or provider lifecycle notices exist and cannot be read.

Missing utilization history, unknown historical sizing intent, and unstated growth projections are soft gaps. Name them, label the assumption, and continue. Image provenance requirements, patch obligations that come from a compliance regime, and approval for production capacity changes are never relaxed to keep a workflow moving.

## Downstream handoffs

`container-platform-desk` is next and needs the node capacity model, the image lineage, the interruptible mix, and the failure domain placement, because node groups inherit all four and a cluster built on an unreproducible image inherits that problem at scale. `cloud-storage-data-services-desk` needs the block storage attachment and throughput expectations that come from the instance choice. `resilience-multi-region-desk` inherits the placement spread, the correlated-failure concentrations, and the quota headroom required in the recovery region. `cloud-cost-rightsizing-desk` inherits the capacity model and the rightsizing candidates with their utilization evidence. `infrastructure-as-code-desk` needs the image build path to bring it under code. `drift-detection-reconciliation-desk` inherits the fleets whose live configuration diverged from their declared scaling policy.

## Quality bar

Good compute work is written around the replacement cycle rather than around the instance. It can answer, without hedging, how the current image gets rebuilt, who owns that pipeline, and what happens the week the provider retires the generation the fleet runs on. Sizing is defended with a metric, a window, and a saturating dimension rather than with a percentage. Scaling bounds have been reconciled against the quota that actually stops them. And the interruptible portion of the fleet is described honestly as capacity that will be taken away, with the diversification and the drain behavior that make that survivable, rather than as a discount.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
