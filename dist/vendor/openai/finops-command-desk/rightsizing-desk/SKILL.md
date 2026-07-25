---
name: rightsizing-desk
description: identify cloud rightsizing candidates from utilization measured over a full business cycle including peaks, with a target configuration and stated headroom. covers instance storage and database sizing, cpu memory iops and throughput percentiles against the observation window that produced them, family and generation migration with compatibility and licensing constraints, autoscaling and scheduling where elasticity beats a smaller size, saving with its baseline, performance risk with the evidence behind the judgment, rollback and change window, and the candidates rejected because the measurement window missed their cycle.
---

# Rightsizing Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the candidate it affects and recorded in `open_questions`. Never invent utilization percentiles, observation windows, instance or resource identifiers, target configurations, saving amounts, service level obligations, or an owner who has not confirmed a workload's purpose.

## Role

Own the gap between what a workload was given and what it uses. This desk produces rightsizing candidates with measured utilization against the observation window that produced it, proposes a target configuration with the headroom it leaves and the peak it was checked against, sizes the saving with its baseline named, covers storage and database sizing alongside compute, evaluates family and generation migration with its compatibility and licensing constraints, identifies where the answer is elasticity or a schedule rather than a smaller size, states the performance risk with the evidence behind that judgment, and records the candidates rejected because the measurement window did not cover their cycle.

The rule that governs everything here is that a resource measured over a window shorter than its business cycle is not measured. Utilization over three quiet days is evidence about three quiet days. Month-end close, quarter-end reporting, batch windows, marketing events, and seasonal peaks are exactly where a rightsized instance becomes an incident, and they are exactly what a fourteen-day average smooths away. The second rule is that averages hide the failure: a workload averaging twelve percent with a daily peak at ninety-four percent is correctly sized for its peak and looks like the most obvious candidate in the estate.

## Use when

- A rightsizing or efficiency pass is being run across compute, storage, or database resources.
- Utilization looks low and somebody wants to know what could safely shrink.
- An anomaly resolved to capacity and the question is what the correct size is.
- Instance family or generation migration is being evaluated, including where a newer generation is cheaper at the same or better performance.
- The answer may be elasticity or scheduling rather than a smaller fixed size, and the alternatives need comparing.
- Provisioned throughput, IOPS, storage tier, or database instance class is oversized relative to measured demand.
- Container resource requests are set far above measured usage and are consuming cluster capacity that somebody is paying for.

## Do not use when

- The resource is not used at all, is unattached, or is orphaned: that is `waste-elimination-desk`. A resource with no consumer is a removal question, not a sizing one.
- The cost driver is the design rather than the size: chatty cross-zone traffic, retry storms, unbounded retention, or a missing cache belong to `cost-aware-architecture-desk`, where a smaller instance would not touch the cause.
- The question is whether to commit to the resulting usage: that is `commitment-portfolio-desk`, which is deliberately downstream because commitments are sized against post-optimization usage.
- The cluster is oversized because idle capacity is unallocated rather than because workloads are large: `shared-cost-allocation-desk` establishes the idle picture first.
- The resource belongs to a managed service whose sizing is a licensing decision: `licensing-saas-spend-desk` where the constraint is entitlement rather than capacity.
- The candidate list needs prioritizing against every other savings lever: that is `optimization-backlog-desk`, which nets overlaps this desk cannot see.
- The change itself needs implementing: that is the owning engineering team, with the SDLC suite packaging the work for Codex where it is code rather than console.

## Required evidence

- Workload-level utilization telemetry over at least one full business cycle including its peaks, with the metric resolution stated, since a five-minute average conceals a burst that a one-minute sample shows.
- The metrics that actually constrain the workload: CPU and memory for compute, IOPS, throughput and queue depth for storage, connections, buffer and query load for databases, and network throughput where it binds first.
- Current resource configuration and its cost, at the granularity the export carries.
- The workload's performance requirements and any service level it supports, including latency targets and the consequence of missing them.
- Autoscaling and scheduling behavior already in place, since a resource inside an autoscaling group is a different question from a fixed one.
- Licensing implications of a size or family change, which for some database and commercial software workloads dominate the infrastructure saving entirely.
- The owning team and the change process that would apply, including the change window and the approval it needs.
- Memory metrics specifically, which are frequently absent because they require an agent, and their absence is a finding rather than an assumption of low utilization.

## Workflow

**Outcome.** A candidate set where each entry carries measured utilization with its percentiles and the observation window that produced them, a target configuration with stated headroom and the peak it was checked against, the saving with its baseline, the performance risk with its evidence, the rollback path and the change window, and the owner; plus the elasticity and scheduling alternatives where those beat a fixed resize, and the candidates explicitly rejected because the window did not cover their cycle.

**Grounding.** Utilization comes from telemetry and cost comes from the billing export; the join between them is an inference that carries its own error and is labeled per `references/suite-workflow-contract.md`. Telemetry is authoritative for what a workload used and never for what it cost. The owning team is authoritative for what the workload is for, and their statement is checked against the metrics before it becomes a fact, in both directions: "it needs that headroom for the quarterly run" is verified against the quarterly window, and "nothing runs on that" is verified against activity.

**Constraints.** One ordering is mandated and holds regardless of how obvious a candidate looks, because resizing a running workload is a change to production with an availability consequence and a stateful service is the least reversible case in the estate:

1. Measure utilization over a window that covers the workload's real cycle, including its peaks.
2. Confirm the workload's purpose and its performance requirement with the owner.
3. State the target configuration, its headroom, and the rollback path.
4. Schedule the change into a change window, executed by the owning team.

Beyond that ordering: percentiles are used rather than averages, and the peak percentile that matters is stated with the window; a p99 is not inferred from a p50 and a missing percentile is reported as missing. The observation window is named on every candidate with its start and end, and a candidate whose window did not cover its cycle is rejected with that reason rather than sized anyway with a caveat. Headroom is explicit and justified against the observed peak plus the growth in the window, not left as a default percentage. Savings carry their baseline, since a saving against on-demand list, against the current effective rate, and against a committed rate are three different numbers for the same change. Where a resource is covered by a commitment, resizing it may strand that commitment and the net saving accounts for it. Licensing is checked before a family change is recommended, because a core-based licence can make a smaller instance more expensive overall. Elasticity and scheduling are evaluated as alternatives on the same footing as resizing, because a workload that is idle sixteen hours a day is a scheduling finding rather than a sizing one, and a variable workload rightsized to its peak stays oversized for the rest of the week.

**Parallel surface.** Individual workloads, instances, volumes, database resources, clusters, node groups, and per-candidate telemetry analysis are independent units and fan out, as does connector preflight across telemetry, the cost dataset, the configuration inventory, and the ownership map.

The aggregate is a single pass after the fan-out returns. The total saving requires netting candidates that touch the same spend, since resizing an instance and scheduling it down overlap, and both overlap with any commitment covering it. Cluster-level effects are aggregate by nature: reducing requests across many workloads only produces a saving when it removes a node, so per-workload savings summed across a cluster overstate the result until the node count actually falls. Commitment coverage effects across the estate are also whole-set, because shrinking covered usage moves coverage onto other workloads rather than releasing the commitment.

**Acceptance bar.** Every candidate names its measured utilization with percentiles and the observation window that produced them, a target configuration with headroom against a specific observed peak, a saving with its baseline, a rollback path, and an owner; and every rejected candidate names the cycle its window missed.

## Outputs

A complete run delivers this artifact set:

- `rightsizing-candidates.md`: each candidate with resource identifier, current configuration and cost, utilization percentiles per constraining metric, the observation window, the proposed target, the headroom it leaves against the observed peak, the saving with its baseline, and the owner.
- `rightsizing-risk-assessment.md`: per candidate, the performance risk with the evidence behind the judgment, the service level it supports, the blast radius, the reversibility, and the rollback path.
- `elasticity-and-scheduling-options.md`: where autoscaling, scheduled shutdown, or a burst-capable configuration beats a fixed resize, with the demand pattern that makes it safe and the saving compared against the resize option.
- `family-and-generation-migration.md`: family or generation changes with their compatibility constraints, licensing consequences, architecture or driver requirements, and the net saving after licensing.
- `storage-and-database-sizing.md`: provisioned throughput, IOPS, storage class, and database instance sizing against measured demand, with the recovery and performance consequence of each change.
- `rightsizing-rejected-candidates.md`: the resources that look like candidates and are not, with the cycle their window missed or the requirement that justifies their current size, recorded so the next sweep does not resurface them.
- `rightsizing-change-package.md`: the sequence, change windows, owners, rollback steps, and the monitoring signal that would show the change was wrong, prepared for the owning team to execute.

Depth standard per artifact: a candidate gives the actual percentile figures and window dates rather than "low utilization". A target names the configuration and the headroom against a specific observed peak. A risk entry gives the evidence, so "the p99 CPU of eighty-eight percent occurs during the nightly reconciliation batch, and the proposed size leaves eleven percent headroom against it" rather than "some performance risk". A rejected candidate names the cycle, since that is the information that stops it being re-proposed every quarter.

In `diagnostic` mode, when telemetry, the configuration inventory, or the cost dataset exists and cannot be read, the run delivers `rightsizing-connector-diagnostic.md` naming what was attempted and which workloads cannot be assessed. Candidates are not generated from cost data alone, because a large instance with no utilization data is an unmeasured instance rather than an idle one.

The failure specific to this desk has a body count in the form of incidents. A target size chosen from a catalog because it is the next size down, a p99 filled in from a p50, or a window quietly extended in the description but not in the query all produce a candidate list that looks rigorous and is not, and the cost of being wrong is not a bad report but a service that falls over during the busiest hour of the quarter. Every percentile in an artifact comes from a query over a stated window, a metric that was not collected is written as not collected rather than treated as low, and a workload whose observation window missed its cycle is rejected rather than sized with a caveat that nobody reads before executing. Memory in particular is often uninstrumented, and an instance that looks CPU-idle can be memory-bound; recommending a smaller instance on CPU evidence alone, without saying that memory was unmeasured, is the most common way this desk causes an outage.

## finops_packet fields to update

- `opportunities[]` with `opportunity_id`, `lever: rightsizing` or `scheduling`, `scope`, `current_state` with measured utilization and window, `proposed_state`, `estimated_savings` with amount, period, baseline and confidence basis, `savings_type`, `overlaps_with`, `implementation_effort`, `performance_risk`, `blast_radius`, `reversibility`, `owner`, and `state`.
- `opportunities[].rejection_reason` for candidates rejected on measurement window or requirement grounds.
- `anomalies[].state` updated where an anomaly resolves into a sizing opportunity.
- `governance.approvals[]` where a change needs a named approver before it enters a change window.
- `source_facts[]` with `locator` and `as_of` for every utilization figure and its window, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Production or destructive: resizing, restarting, or reconfiguring a running workload. This is the defining halt for this stage. Databases, stateful services, and anything carrying a service level are the least reversible cases, and a resize frequently requires a restart. Prepare the change with its evidence, its rollback, and its window; the owning team executes it.
- Missing approval: the change would affect a workload under a service level obligation, a regulated system, or a customer commitment, or the owner has not confirmed the workload's purpose.
- Release integrity: a candidate would be published with a utilization figure whose window is unstated, a percentile that was not measured, or a saving with no baseline.
- Source conflict: telemetry and the owning team disagree materially about what the workload does or when it peaks, or two telemetry sources disagree on utilization. Record both readings rather than choosing the one that produces a candidate.
- Security or privacy: the telemetry or configuration data would expose customer identifiers or system topology beyond its intended audience, or the resize would alter an encryption, isolation, or residency property.
- Connector unreachable: telemetry, the configuration inventory, or the cost dataset cannot be read. Say which, because absent metrics and unreachable metrics look identical in a candidate list and one of them means the workload is idle while the other means nobody knows.

An unconfirmed owner, an undocumented workload purpose, or a missing growth trend is a soft gap: proceed with the candidate built, the assumption labeled, and the confirmation named as a prerequisite in the change package.

## Downstream handoffs

`waste-elimination-desk` receives resources whose measured utilization is effectively zero, since those are removal candidates rather than sizing ones, with the activity evidence attached. `cost-aware-architecture-desk` receives workloads whose cost is driven by design behavior that sizing cannot fix. `commitment-portfolio-desk` needs the post-rightsizing usage baseline and the schedule of accepted changes, because sizing a commitment against pre-optimization usage locks the waste in for the whole term and that is the single most expensive sequencing error in this suite. `optimization-backlog-desk` needs every candidate with its overlaps declared, so the register nets rather than sums. `engineering-cost-review-desk` needs the candidates in the vocabulary of the services each team owns, with the risk and rollback already stated.

## Quality bar

Percentiles, not averages, each with the window that produced them. Headroom justified against an observed peak rather than set by habit. Elasticity and scheduling considered on equal footing with a smaller size. Licensing and commitment coverage effects netted before a saving is claimed. Every candidate carries a rollback and an owner. The rejected list is as carefully written as the candidate list, because the resources that look wasteful and are not are the ones that cost the practice its welcome with an engineering team.
