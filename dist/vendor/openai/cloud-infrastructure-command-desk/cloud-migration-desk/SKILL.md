---
name: cloud-migration-desk
description: plan cloud migration from source estate discovery and the dependency graph through disposition per workload across rehost replatform refactor repurchase retain and retire, wave sequencing derived from coupling, landing readiness and target quota per wave, data migration method with lag-driven cutover windows, the rollback boundary past which rollback stops existing, coexistence and dual-running behavior, and post-cutover validation against a baseline captured before the move.
---

# Cloud Migration Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the migration artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent workload names, dependencies, data volumes, change rates, replication lag figures, cutover dates, quota limits, or application owners.

## Role

Own the path from a source estate to a target one, workload by workload and wave by wave. This desk discovers what is actually running, builds the dependency graph that decides what must move together, assigns a disposition to each workload, sequences waves from coupling rather than convenience, establishes landing readiness before a wave starts, chooses the data movement method and derives the cutover window from measured replication lag, marks the rollback boundary, defines coexistence behavior for the period when both estates are live, and sets post-cutover validation against a baseline that has to be captured before anything moves.

The discipline that separates a migration plan from a migration wish is the dependency graph, and specifically its completeness. Everything downstream is derived from it: waves, windows, rollback, coexistence. A graph built from what teams remember rather than from observed connections produces a wave plan that looks orderly and breaks on the first thing nobody mentioned.

## Use when

- Workloads are moving between estates, providers, regions, or from on-premises into cloud, and the plan needs to exist before anything moves.
- Source estate discovery and dependency mapping are needed, including the connections nobody documented.
- Disposition decisions are due across rehost, replatform, refactor, repurchase, retain, and retire.
- Waves need sequencing, and the current proposal is ordered by which team volunteered.
- Landing readiness needs checking per wave: accounts, address space, connectivity, identity, guardrails, monitoring, and target quota.
- The data movement method and the cutover window need deriving from replication lag and validation time rather than from a calendar slot.
- Coexistence behavior needs defining because both estates will be live at once and something has to be authoritative.
- The rollback boundary has never been written down and the team is about to find it experimentally.

## Do not use when

- The target landing zone does not exist or is incomplete: run the design chain from `landing-zone-account-structure-desk` through `resilience-multi-region-desk` first, because a wave with nowhere to land is a schedule rather than a plan.
- The subject is retiring the source after a successful move, or retiring a workload outright with no target: that is `cloud-decommissioning-desk`, which owns the teardown and the proof that spend stopped.
- Address space for the target is being allocated: that is `cloud-network-architecture-desk`, which owns the register that a migration must draw from rather than carve into.
- The divergence is between code and live state within one estate: that is `drift-detection-reconciliation-desk`.
- Database engine selection and sizing for the target: that is `managed-database-platform-desk`, whose decisions this desk sequences.
- Application refactoring work, code changes, and release engineering for a replatformed workload: cross-suite handoff to the SDLC suite.

## Required evidence

- Source estate inventory from discovery tooling, with the collection method and its coverage stated, since agentless discovery and agent-based discovery see different things.
- Observed connection evidence over a stated window: flow logs, connection tables, load balancer logs, or discovery tool dependency output. The window must span at least one full business cycle, because the job that runs on the last business day of the month does not appear in a two-week sample.
- Application ownership records, and the operational runbooks that exist.
- Data volumes and change rates per data store, which together determine whether replication can ever catch up.
- Target estate state: accounts, address ranges available from the register, connectivity capacity, identity readiness, guardrail attachment, and current quota values in the target region.
- Licensing, support, and contractual constraints that bind a disposition, including anything that changes cost or legality when the workload moves.
- The business constraints on cutover: acceptable downtime, freeze periods, and the calendar dates that are non-negotiable for reasons outside engineering.

## Workflow

**Outcome.** A migration plan with a dependency graph backed by observed connections, a disposition and rationale per workload, waves derived from coupling with a landing readiness checklist per wave, a data movement method and a cutover window derived from measured lag, a marked rollback boundary per wave, defined coexistence behavior, and post-cutover validation criteria measured against a pre-migration baseline.

**Grounding.** Read discovery output and connection evidence for what the estate does, and architecture documents and team interviews for what it is believed to do, keeping the two labeled separately per `references/suite-workflow-contract.md`. They differ in a predictable direction: documentation is missing the connections that were added under pressure, and interviews are missing the ones whose owner left. Where a documented dependency has no observed traffic, record both facts rather than deleting either, since a quarterly job and a dead integration look identical for eleven weeks.

**Constraints.** Wave composition follows the dependency graph: a move group is everything that must move together because splitting it puts a chatty or latency-sensitive connection across the estate boundary. The first wave is low-risk and representative rather than trivial, because a pilot with no dependencies proves only that the pilot had no dependencies. Landing readiness is a precondition rather than a discovery, and target quota specifically is raised and confirmed before the wave rather than during it, since quota requests have lead times measured in days and a cutover discovers them at the worst hour. The cutover window is derived, not chosen: measured replication lag plus validation time plus the time rollback would take, and if that sum exceeds the acceptable downtime then the method changes rather than the arithmetic. Coexistence names what is authoritative for each data set during dual-running and how the two are reconciled, because "both" is not an answer and is how duplicate records enter a production system. Retire is a real disposition and is systematically under-chosen; every workload gets asked whether it should move at all, and retain gets a reason and a revisit date rather than being a default. Nothing on the source side is deleted at cutover; source retirement is a separate decision handled by `cloud-decommissioning-desk` after the validation window closes.

A wave cutover runs in this order, and the order is mandated because the pre-migration baseline cannot be captured after the move, replication lag cannot be verified after the source stops changing, and step 5 is the point where rollback stops being a switch and starts being a restore:

1. Capture the pre-migration baseline: performance, error rates, throughput, and data counts on the source, because after cutover there is nothing left to compare against.
2. Confirm landing readiness for this wave, including target quota, connectivity, identity, guardrails, and monitoring already receiving signal.
3. Freeze source-side change as the method requires, and confirm measured replication lag is inside the stated threshold rather than assumed to be.
4. Validate the target against the baseline while the source is still authoritative and rollback is still a redirect.
5. Switch authority to the target. This is the rollback boundary: the first write the target accepts that does not replicate back is the point past which rollback becomes a data reconciliation rather than a redirection.
6. Observe through at least one full business cycle with the source intact and untouched, then hand source retirement to the decommissioning stage as a separate decision.

**Parallel surface.** Workloads, data stores, applications, discovery targets, and independent move groups are independent units and are parallel-safe; per-workload disposition analysis, per-store data method selection, per-application ownership resolution, and connector preflight across discovery output, flow logs, and target inventory all fan out.

The aggregate work runs once after the fan-out returns: the dependency graph itself, wave sequencing derived from it, the target quota and capacity rollup across all waves, the address space draw against the register, and the cutover calendar. The graph is the definitive aggregate, since a dependency is a relationship between two workloads and no per-workload analysis can produce it; and target capacity is a finite shared pool, so waves planned independently can each be feasible while their sum exceeds the region's quota.

**Acceptance bar.** A wave owner can state what moves in their wave, what it depends on that is not moving with it, what the cutover window is and what derived it, what happens if validation fails at each step, and where rollback stops being available. Every dependency traces to observed evidence or is labeled as asserted by an owner and unconfirmed.

## Outputs

A complete run delivers this artifact set:

- `cloud-migration-discovery.md`: the source estate inventory with the collection method and its coverage, the resources discovery could not see, and the observation window behind the connection evidence.
- `cloud-migration-dependency-graph.md`: workloads with their observed connections, the move groups that follow, the asserted-but-unobserved dependencies kept separately, and the hidden coupling classes checked for, including hardcoded addresses, shared mounts, license servers, scheduled jobs on other hosts, and firewall rules keyed to source address.
- `cloud-migration-disposition-register.md`: disposition per workload with its rationale, the constraint that bound it, the owner, and the retain entries with a revisit date.
- `cloud-migration-wave-plan.md`: waves derived from the graph, their composition, the landing readiness checklist per wave including target quota, and the sequencing rationale.
- `cloud-migration-data-plan.md`: per data store, the movement method, volume and change rate, expected replication lag, the lag threshold that opens the cutover window, and the reconciliation approach.
- `cloud-migration-cutover-runbook.md`: the ordered cutover per wave, the decision authority at each gate, the rollback procedure and the boundary past which it does not exist, and the coexistence behavior with the authoritative side named per data set.
- `cloud-migration-validation.md`: the pre-migration baseline to capture, the post-cutover criteria measured against it, the observation window, and the source-side resources that must not be touched until it closes.
- `cloud-migration-downstream-handoff.md`: what `cloud-decommissioning-desk` inherits for source retirement once validation closes, and the target-side items that return to the design desks.

Depth standard per artifact: a wave entry names the workloads and their move group rationale, not the count. A data plan entry gives the volume, the change rate, and the lag threshold, since those three determine whether the method can work at all. A cutover entry names who decides to proceed at each gate. A validation entry names the metric and its baseline value, or states that the baseline is not yet captured, which is itself a gate on starting.

In `diagnostic` mode, when discovery output, flow logs, or the target inventory exists and cannot be read, the run delivers `cloud-migration-connector-diagnostic.md` naming what was attempted and the access needed. A wave plan is not drafted from an architecture diagram in that mode, because a diagram is a record of intent from the day it was drawn.

The artifact that fails quietly here is the dependency graph, and it fails by looking finished. A graph completed by inference is smooth, plausible, and short, and the workload that appeared to have no callers is the one the quarterly close depends on. So every edge names its evidence and its observation window, an asserted dependency with no observed traffic stays in the graph as asserted rather than being pruned for tidiness, and a workload whose evidence window is shorter than a business cycle is marked as incompletely observed rather than as independent. The same restraint governs replication lag and data volumes: a lag figure that no measurement produced is written as unmeasured, because a cutover window is arithmetic performed on those numbers and a fabricated input produces a window the business accepts and the replication cannot meet.

## infrastructure_packet fields to update

- `migration[]`: `workload`, `disposition`, `wave`, `dependencies`, `data_move_method`, `cutover_window`, `rollback_boundary`.
- `workload_profile` where discovery corrects criticality tier, data classification, or residency for a moving workload.
- `resilience.quota_headroom` for the target region, since a wave consumes it and a later wave inherits what is left.
- `network.ipam_plan` where a wave draws ranges from the register, recorded as allocated rather than reserved.
- `decommission[]` seeded with source-side targets for the retirement decision that follows validation.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: a cutover date, a disposition that changes a contractual or licensing position, a freeze-period exception, or a wave affecting a tier-one workload needs a named human owner who has not given it.
- Production or destructive: the next action would switch authority to the target, stop source-side services, delete source data, or begin an irreversible data movement. Source deletion at any point in a migration is out of scope here and belongs to the decommissioning stage after the validation window closes.
- Security or privacy: moving the data crosses a residency boundary, changes the applicable regime, or would place regulated data into a target whose controls are not evidenced as equivalent.
- Source conflict: discovery output, connection evidence, and owner statements genuinely disagree about what a workload depends on, and choosing one silently would compose a wave that breaks something nobody expected.
- Release integrity: a cutover would be declared ready without the pre-migration baseline captured, without measured replication lag, or without landing readiness confirmed including target quota.
- Connector unreachable: discovery output, flow logs, the target inventory, or the quota source exists and cannot be read.

Missing documentation, an unavailable application owner, or an unmeasured performance profile is a soft gap: proceed with it named and carried into the wave plan as a risk. Data residency constraints, retention obligations, and the pre-migration baseline requirement are not soft gaps and are never traded for a date.

## Downstream handoffs

`cloud-decommissioning-desk` inherits the source-side estate as a retirement candidate set once the validation window closes, along with the coexistence dependencies that must end first. `drift-detection-reconciliation-desk` needs the target resources created outside the pipeline during a cutover, which are unmanaged from the moment they exist. `cloud-cost-rightsizing-desk` needs the wave schedule, because a commitment purchased against a baseline that a migration is about to remove is a multi-year payment for capacity nobody will use. `tagging-inventory-desk` needs the migrated resources for ownership and tag coverage. Cross-suite: application refactoring and release engineering go to the SDLC suite.

## Quality bar

A wave plan whose ordering an engineer can defend from the graph rather than from the calendar. Cutover windows derived from measured lag instead of negotiated into existence. A rollback boundary that is marked, understood, and stated before the wave begins. And a dependency graph honest enough to show its own gaps, including the edges that are asserted and the workloads whose observation window was too short to trust.
