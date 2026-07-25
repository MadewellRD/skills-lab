---
name: capacity-planning-desk
description: build the demand model and its drivers, measure headroom against the binding saturation signal rather than average cpu, find quota connection partition thread and licence ceilings, state provisioning lead time, compute failover headroom at real peak, and separate every measured number from every assumed one. use for capacity planning, headroom analysis, saturation signals, scaling limits, quota exhaustion, and peak readiness.
---

# Capacity Planning Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the capacity artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent utilization figures, quota limits, growth rates, provisioning lead times, or peak traffic values.

## Role

Own the relationship between demand and the limit that demand runs into first. That means a demand model with named drivers rather than a growth percentage, headroom measured against whichever signal actually binds, an inventory of the ceilings that stop scaling regardless of budget, the lead time to add capacity, and whether the surviving zone or region can absorb real peak when one is lost.

The signal that binds is rarely the one on the dashboard. Average CPU is the most reported and least often binding constraint in this domain; the thing that saturates first is usually a connection pool, a thread pool, disk throughput, a partition count, a lock, a garbage collector, a network packet rate, or a quota that belongs to an account rather than to a service.

## Use when

- Headroom, saturation, or time-to-exhaustion needs establishing for a service, a data store, or a shared platform component.
- A demand change is coming: a launch, a campaign, a migration, a seasonal peak, a large customer onboarding, or a new market.
- Scaling ceilings need finding before they are found by an incident, including quotas, autoscaler bounds, and limits owned by a vendor.
- Failover headroom needs computing, because a recovery plan that assumes the surviving region can take the load is a capacity claim.
- Provisioning lead time needs stating against the time remaining before exhaustion, which is the only comparison that makes lead time actionable.
- Efficiency changed and the cost per request moved, so an existing capacity model no longer describes the system.

## Do not use when

- The question is where the knee actually is under a realistic workload rather than what the model predicts: that is `load-performance-testing-desk`, which measures what this desk hypothesizes.
- The question is what the system does past its limit: that is `resilience-architecture-desk` for shedding and backpressure design, and the load stage for observed behavior.
- The question is the recovery topology, the RTO, or the evacuation procedure: that is `disaster-recovery-desk`, which consumes the failover headroom this desk computes.
- The question is cost policy, commitment purchasing, or spend attribution: cross-suite handoff to the FinOps suite. This desk states what capacity is needed and by when; that suite decides how it is bought.
- Tiering, journeys, or objectives are not established yet: start upstream.

## Required evidence

- Demand history at the granularity where peaks are visible, since hourly averages erase the burst that saturates a pool, along with the drivers behind past growth.
- Forecast inputs from the business: launches, campaigns, onboarding schedules, seasonal patterns, and contractual volume commitments, with their sources.
- Utilization and saturation telemetry per resource class: CPU, memory, disk throughput and IOPS, network throughput and packet rate, connection and thread pools, queue depth and consumer lag, lock and contention metrics, and garbage collection behavior.
- Cost per unit of work where it exists: CPU-seconds or requests per instance, so demand can be translated into resource requirements rather than into a shrug.
- Quota and limit inventory: cloud API and resource quotas with the account they belong to, autoscaler minimums and maximums, database connection limits, partition and shard counts, address space, file descriptors, licence seats, and vendor rate limits.
- Provisioning lead times from the actual constraint: instance family availability, specialized hardware, vendor contracts, address allocation, and any approval step in the path.
- The topology and redundancy model, so failover headroom can be computed against the real surviving set.
- Retry and amplification behavior from the dependency stage, because retries change the load a dependency must be sized for.

## Workflow

**Outcome.** A demand model with named drivers and a stated forecast horizon, headroom per service and per shared resource measured against the binding saturation signal with the time to exhaustion it implies, a ceiling inventory that bounds scaling independently of budget, a provisioning plan with lead times set against that time to exhaustion, failover headroom computed at real peak, and an explicit measured-versus-assumed marking on every number.

**Grounding.** Utilization, saturation, and demand come from the metrics backend with the query and range named; quotas come from the provider or the configuration rather than from memory; lead times come from a purchasing or provisioning record. Forecast inputs from the business are labeled as forecast, not as measurement, per `references/suite-workflow-contract.md`.

**Constraints.** Identify the binding signal per component before stating any headroom figure, and state headroom against that signal. A component at 30 percent CPU and 95 percent connection pool utilization has 5 percent headroom, and reporting 70 percent is not a rounding difference; it is the wrong constraint. Where the binding signal is unknown, say so rather than defaulting to the one that happens to be graphed.

Plan against peak, not against mean, and state the peak-to-mean ratio explicitly along with the observation window it came from. A daily peak, a weekly peak, and an annual peak are different numbers, and capacity that covers the first fails on the third. Where demand is bursty, the burst shape matters more than the total: a queue that absorbs a burst has different capacity requirements than a synchronous path that must serve it inline.

Translate demand into resource requirement through a stated unit of work, so the model can be re-derived when efficiency changes. A model that maps request rate to instance count without the cost per request silently becomes wrong the first time a code change moves that cost, and nobody notices until saturation.

Treat ceilings as first-class, because they cannot be bought past on the day. A quota attached to an account shared with other teams is a ceiling somebody else can consume, an autoscaler maximum below the required peak is a limit no amount of demand will override, and a scale-out that requires more database connections than the database allows stops at the database. Compare every lead time against the time to exhaustion the demand model implies, since a lead time longer than the runway is a scheduled outage.

Compute failover headroom against the load the surviving set must actually carry at peak, not at average, and include the recovery-time load spike from reconnects, cache refill, and retry backlog, which routinely exceeds steady-state peak. State whether the surviving capacity is warm, whether it can start fast enough to matter, and whether the scale-up path itself depends on a control plane that may be part of the failure.

**Parallel surface.** Services, resource classes, quotas, saturation signals, and demand drivers are independent units and are parallel-safe; per-component utilization queries, per-quota lookups, and lead-time inquiries all fan out.

The aggregate work runs once after the fan-out returns: identifying which single signal binds first across the journey rather than per component, composing per-service demand into the shared resources several services contend for, computing failover headroom across the surviving topology, ranking ceilings by time to exhaustion, and reconciling the demand model against the objectives the journeys carry.

**Acceptance bar.** Every headroom figure names the binding signal and the query behind it. Every capacity number is marked measured or assumed. The demand model names its drivers and its horizon. Every ceiling names its owner and its limit value with the source. Failover headroom is computed at peak with the recovery spike included, or stated as uncomputed with the missing input named.

## Outputs

A complete run delivers this artifact set:

- `demand-model.md`: current demand with its measurement source, the drivers behind it, the forecast with its horizon and its inputs labeled as business forecast, the peak-to-mean ratio with its observation window, and the sensitivity of the model to each driver.
- `headroom-and-saturation.md`: per component, the binding saturation signal, current utilization against it with the query, the headroom that remains, the time to exhaustion at forecast growth, and the signals that were checked and found not binding.
- `scaling-ceiling-inventory.md`: every quota, pool, partition, address space, autoscaler bound, licence, and vendor rate limit that bounds scaling, with its value, its source, the account or scope it belongs to, and who can raise it.
- `provisioning-plan.md`: what needs adding, by when, the lead time for each item with its source, the approval or purchase step in the path, and the items where lead time exceeds runway.
- `failover-headroom-assessment.md`: the load the surviving zone or region must absorb at peak, whether it can, the recovery-time spike from reconnect and cache refill, the warm-versus-cold state of the standby capacity, and the control-plane dependency the scale-up path carries.
- `capacity-downstream-handoff.md`: the saturation hypotheses `load-performance-testing-desk` should test, and the headroom assumptions `disaster-recovery-desk` relies on.

Depth standard per artifact: a headroom entry that names the signal, the number, the query, and the date, since headroom without a date is a claim about a moment nobody can identify. A ceiling entry that says who can raise the limit and how long that takes, because the value alone does not tell an on-call engineer whether it is fixable tonight. A demand model whose arithmetic can be re-run when a driver changes rather than a single projected number.

In `diagnostic` mode, when utilization telemetry, quota inventories, or demand history exists and cannot be read, the run delivers `capacity-connector-diagnostic.md` reporting reachability, the queries and lookups attempted, and the access needed. No headroom or exhaustion figure is stated in that mode.

Capacity artifacts get used in two directions, and both directions punish invention. A headroom figure authorizes spending and it authorizes declining to spend; a time-to-exhaustion date sets whether a provisioning request is urgent or ignorable. Both are easy to produce from a mean, a plausible growth rate, and a utilization number pulled from whichever dashboard was open, and the result carries no visible sign of how it was derived. So every utilization and demand figure names its query and its window, a peak is quoted only from an observation that contains the peak rather than inferred from an average, a growth rate comes from history or from a stated business input rather than from a round number, a quota value is read from the provider or the configuration rather than recalled, and a lead time comes from a provisioning record. Where the binding signal has not been identified, the artifact says the binding signal is unknown instead of reporting headroom against the signal that was convenient. A capacity plan that says "we cannot compute failover headroom because peak-hour per-zone load is not broken out" sends an engineer to build one query. A plan that guesses it sends a region into a peak it cannot serve.

## reliability_packet fields to update

- `capacity.demand_forecast`, `capacity.current_headroom`, `capacity.saturation_signals`, `capacity.scaling_limits`, `capacity.provisioning_lead_time`, `capacity.failover_headroom`.
- `failure_modes[]` extended with saturation-driven modes the analysis exposed.
- `reliability_risks[]` for ceilings whose lead time exceeds runway and for journeys with no failover headroom at peak.
- `readiness_gates[]` for the capacity gate with the evidence behind its state.
- `reliability_surface` set to `capacity`.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: committing spend, requesting a quota increase, or accepting a known capacity shortfall on a tier 0 journey requires the accountable owner.
- Production or destructive: the next action would reduce capacity, change autoscaler bounds, resize a cluster or database, lower a quota, or drain a zone in a live system.
- Security or privacy: capacity evidence would require reading customer-level volume or usage data beyond what the model needs, or exposing per-tenant traffic that identifies a customer.
- Source conflict: the metrics backend and the business forecast disagree on current or projected demand by enough to change the provisioning decision, and choosing one silently would set the wrong runway.
- Release integrity: headroom, failover capability, or peak readiness would be recorded as sufficient without a measurement establishing it.
- Connector unreachable: the metrics backend, quota inventory, or provisioning records needed for the model exist and cannot be read.

Absent per-tenant breakdowns, an unknown cost per request, missing historical peaks beyond the retention window, and an unrecorded lead time are soft gaps: proceed with the number marked assumed, the derivation shown, and the gap recorded in `open_questions`. Headroom is never reported against a non-binding signal because the binding one is unmeasured.

## Downstream handoffs

`load-performance-testing-desk` needs the saturation hypotheses, the binding signals, and the peak the workload model must reproduce. `disaster-recovery-desk` needs the failover headroom assessment, since a recovery plan that exceeds surviving capacity is not a recovery plan. `chaos-resilience-testing-desk` needs the ceilings that a fault injection might push a system into. `change-safety-desk` needs the headroom state, because a rollout that doubles resource consumption during a canary needs room to do it. `alerting-quality-desk` needs the binding signals as saturation alert candidates. Cross-suite: purchasing, commitments, and spend policy go to the FinOps suite.

## Quality bar

A demand model whose drivers a product manager recognizes and whose arithmetic an engineer can re-run. Headroom stated against the constraint that actually binds, with the constraint named. Ceilings that include the ones owned by a vendor and the ones shared with another team. Lead times set against runway rather than listed in isolation. Failover headroom computed at peak with the recovery spike included, and stated as uncomputed when the data to compute it does not exist.
