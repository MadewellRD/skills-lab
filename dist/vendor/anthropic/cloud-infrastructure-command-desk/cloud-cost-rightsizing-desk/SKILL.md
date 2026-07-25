---
name: cloud-cost-rightsizing-desk
description: build the cloud cost allocation model and allocable share, set budgets and anomaly thresholds with named recipients, identify rightsizing candidates from percentile utilization evidence with the performance risk each carries, measure commitment and reservation coverage and utilization against a stable baseline, plan storage tiering and retention savings net of retrieval and early-delete cost, reclaim idle and orphaned resources behind dependency checks, and define unit cost metrics the business recognizes.
---

# Cloud Cost Rightsizing Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the cost artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent cost figures, savings estimates, utilization percentages, instance families or sizes, commitment terms, discount rates, or budget owners.

## Role

Own spend as an engineering property rather than an accounting report. This desk builds the allocation model and states honestly what share of spend can be allocated at current tag coverage, sets budgets and anomaly thresholds that reach a named person, finds rightsizing candidates with the utilization evidence and the performance risk each carries, measures commitment coverage against a baseline that will still exist when the commitment matures, plans tiering and retention changes net of the costs they create, reclaims waste behind a dependency check, and defines unit cost metrics that connect spend to something the business already counts.

Two separations run through everything here. First, a saving that requires only an apply is a different object from a saving that requires a human decision, and mixing them produces a number nobody will approve. Second, cost data and utilization data come from different systems with different granularity and different lag, and a rightsizing recommendation that treats a monthly cost figure and a five-minute utilization sample as equally settled will be wrong in a way that is expensive to discover.

## Use when

- Cost allocation is being designed or repaired: direct versus shared cost, the split rule for shared services, and showback versus chargeback.
- Budgets and anomaly detection need thresholds, recipients, and a defined response.
- Rightsizing candidates are needed with real utilization evidence rather than a provider recommendation list taken at face value.
- Commitment and reservation coverage needs measuring, or a purchase is being considered and the baseline behind it needs testing.
- Storage tiering, lifecycle, retention, or snapshot policy is a cost question.
- Idle, orphaned, unattached, or oversized resources need reclaiming, and the dependency check has to come first.
- A unit cost metric is needed: cost per tenant, per request, per environment, or per whatever the business already measures.
- Spend jumped and nobody can say whose it is, and tag coverage is known.

## Do not use when

- Tag coverage is unknown or unmeasured: start at `tagging-inventory-desk`, because an allocation model built on unmeasured coverage produces an argument about attribution rather than a decision about spend.
- Instance family selection, autoscaling policy, or image lineage is the subject for a new workload: that is `compute-platform-desk`. This desk changes sizing on what exists using utilization evidence.
- Cluster bin packing, node group shape, and in-cluster resource requests: that is `container-platform-desk`.
- Deleting the waste this desk identifies: that is `cloud-decommissioning-desk` and its ordered teardown, which requires the dependent evidence this desk does not gather.
- Reducing spend by retiring a workload entirely rather than resizing it: that is a disposition decision for `cloud-migration-desk`.
- Organization-wide spend policy, commitment portfolio strategy, vendor negotiation, and forecast commitments: cross-suite handoff to the FinOps suite.

## Required evidence

- The cost or billing export at resource granularity, in amortized form when commitments exist, since unblended figures misattribute the discount and make every allocation argument unwinnable.
- Tag coverage and the ownership map from `tagging-inventory-desk`, with the untaggable residue named.
- Utilization telemetry with its actual granularity and retention window stated, covering processor, memory where an agent supplies it, storage throughput and operations, and network.
- Commitment and reservation inventory with term, scope, expiry, and current utilization and coverage figures as the provider reports them.
- Criticality tiers from `cloud-workload-intake-desk`, because a rightsizing recommendation on a tier-one workload carries a different risk than the same recommendation in a sandbox.
- Resource dependency evidence for anything proposed for reclamation: attachment state, recent access, snapshot lineage, and target registration.
- Any existing budget, threshold, or anomaly configuration with its current recipients.

## Workflow

**Outcome.** An allocation model with a stated allocable share and a named split rule for the rest; budgets and anomaly thresholds with recipients and a defined response; a rightsizing list where every candidate carries percentile utilization over a named window, the proposed change, the performance risk, and whether the change requires downtime; a commitment position with coverage and utilization measured separately against a baseline whose stability is argued; a tiering and retention plan net of the costs it creates; a waste list with dependency evidence per item; and unit cost metrics with their denominators.

**Grounding.** Read the billing export for spend and the telemetry for utilization, and keep them labeled separately per `references/suite-workflow-contract.md`. They disagree on granularity, on lag, and on what a resource even is. The billing export is the more complete inventory and the slower signal; the telemetry is the faster signal and is frequently missing memory entirely unless an agent was installed, which means a memory-based recommendation on a fleet without agents is an inference and is labeled as one.

**Constraints.** Rightsizing evidence is percentile rather than average over a stated window, because an average hides the peak that sizing exists to serve, and the window covers at least one full business cycle including the monthly and quarterly jobs. Every candidate names its performance risk in concrete terms: what changes about the network baseline, the storage attachment limits, the burst credit accrual, or the memory headroom, and whether the resize requires a stop. Commitment recommendations are tested against baseline stability, since a commitment bought against usage that a migration or a decommissioning wave is about to remove is a multi-year payment for capacity nobody will use; the packet's migration and decommission entries are read before any coverage target is proposed. Tiering and retention savings are stated net of retrieval charges, minimum storage duration, early-delete fees, and per-object transition costs, which for a store of many small objects can exceed the saving outright. Every reclamation item carries dependency evidence rather than an idle-looking metric. Savings that require only an apply are listed separately from savings that require a human decision, and both are separated from savings that require a workload change by another team. Unit cost metrics name their denominator and its source, because a per-tenant figure divided by a tenant count nobody agrees on is a debate rather than a metric.

**Parallel surface.** Accounts, cost line items, resource types, individual rightsizing candidates, commitment pools, and waste findings are independent units and are parallel-safe; per-candidate utilization analysis, per-account allocation mapping, per-item dependency checking, and connector preflight across the billing export, telemetry, and commitment inventory all fan out.

The aggregate work runs once after the fan-out returns: the allocation rollup and the allocable share, commitment coverage judged across the whole eligible footprint rather than per candidate, the shared-cost split, the unit cost calculation, and the savings ranking. Commitment coverage is the case where parallel analysis actively misleads, because reserved capacity is a finite shared pool and per-team recommendations summed together routinely propose buying more coverage than the estate has baseline to absorb.

**Acceptance bar.** A platform owner can read any rightsizing candidate and say what evidence supports it, what could go wrong, and whether it needs a maintenance window; a finance partner can read the allocation model and reproduce the allocable share from the same export; and every savings figure names the billing line it came from. Every figure traces to an export or a telemetry query, or is written as unmeasured.

## Outputs

A complete run delivers this artifact set:

- `cloud-cost-allocation-model.md`: direct and shared cost categories, the split rule with its rationale, the allocable share as a measured figure at current tag coverage, the unallocable residue enumerated, and the showback or chargeback position.
- `cloud-cost-budgets-alerts.md`: budget envelopes per scope, anomaly thresholds with the sensitivity chosen and why, named recipients, and the defined response when one fires.
- `cloud-cost-rightsizing-candidates.md`: each candidate with current size, percentile utilization over the named window, proposed change, expected saving from the billing rate, performance risk, downtime requirement, and criticality tier.
- `cloud-cost-commitment-position.md`: current coverage and utilization as separate figures, expiry ladder, the baseline argued as stable with the migration and decommission plans read against it, and the exposure if that baseline moves.
- `cloud-cost-storage-lifecycle.md`: tiering and retention proposals with savings stated net of retrieval, minimum duration, early-delete, and transition costs, plus the access patterns that would make each one wrong.
- `cloud-cost-waste-reclamation.md`: idle, orphaned, unattached, and oversized resources with dependency evidence per item and the retirement path each must take.
- `cloud-cost-unit-metrics.md`: the unit cost metrics with numerator, denominator, source of each, and the trend where history supports one.
- `cloud-cost-downstream-handoff.md`: reclamation candidates for `cloud-decommissioning-desk` with their evidence, and retirement dispositions for `cloud-migration-desk`.

Depth standard per artifact: a candidate entry gives the specific current and proposed configuration and the specific evidence, not the observation that the resource looks underused. A commitment entry separates coverage from utilization, since high coverage with low utilization is money already lost and the two are constantly conflated. A waste entry gives the dependency check that was actually run.

In `diagnostic` mode, when the billing export, telemetry, or commitment inventory exists and cannot be read, the run delivers `cloud-cost-connector-diagnostic.md` naming what was attempted and the access needed. Savings are not estimated from list pricing in that mode, because a saving computed against a rate the organization does not pay is a fiction with a decimal point.

Cost is the one desk in this suite whose output arrives pre-trusted. A figure with a currency symbol reads as measured even when nothing measured it, it gets forwarded into a business review inside a day, and by the time anyone asks which export it came from the number has become a commitment. So every figure here names its billing line, its rate basis, and its period, and a saving with no billing line behind it is written as unquantified with the query that would quantify it. Utilization gets the same discipline: a memory recommendation on a fleet with no memory agent is labeled inferred, not measured, and a candidate whose telemetry window is shorter than a business cycle says so instead of quietly averaging across the gap. An honestly short savings list that survives review beats a large one that collapses under its first question.

## infrastructure_packet fields to update

- `cost.allocation_state`, `cost.budget_envelope`, `cost.committed_coverage`, `cost.rightsizing_candidates`, `cost.waste_findings`, `cost.unit_cost_metric`.
- `compute[].sizing` and `compute[].capacity_model` where a rightsizing decision changes either.
- `data_stores[].lifecycle_or_tiering` where a tiering change is decided.
- `inventory.unmanaged_resources` where reclamation analysis surfaces resources the inventory stage missed.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: a commitment or reservation purchase, a budget increase, a chargeback model change, or a rightsizing action on a tier-one workload needs a named human owner who has not given it. Commitment purchases are the sharpest case, since the term is contractual and the money is spent whether or not the capacity is used.
- Production or destructive: the next action would resize, stop, or delete live resources, change a retention or lifecycle rule that expires data, or modify a snapshot policy that backups depend on.
- Security or privacy: the cost export carries tenant, customer, or personal identifiers in resource names or tags, or a unit cost metric would expose customer-level commercial data to an audience that should not see it.
- Source conflict: the billing export, the inventory, and the telemetry genuinely disagree about what exists or how heavily it is used, and choosing one silently would justify a resize with the wrong evidence.
- Release integrity: a savings figure, a coverage percentage, or an allocable share would be declared without the export behind it, or a rightsizing recommendation would be declared safe without utilization evidence covering a full business cycle.
- Connector unreachable: the billing export, telemetry, commitment inventory, or tag coverage source exists and cannot be read.

Absent memory telemetry, a short utilization window, an unmeasured unit denominator, or a missing historical trend is a soft gap: proceed with the limitation named at the point it affects a recommendation. Retention obligations, backup requirements, and data residency constraints are not soft gaps and are never traded for a saving.

## Downstream handoffs

`drift-detection-reconciliation-desk` needs any sizing change that will be made outside the pipeline, since a hand-resized instance is drift that the next apply will revert at the worst possible moment. `cloud-decommissioning-desk` inherits the waste list with its dependency evidence as a candidate inventory rather than a delete list. `cloud-migration-desk` receives the retire dispositions that a cost review surfaced, since the cheapest workload to run is the one that stops existing. `provisioning-pipeline-desk` receives the sizing changes that should land as code rather than as console edits. Cross-suite: commitment portfolio strategy and forecast negotiation go to the FinOps suite.

## Quality bar

An allocation model whose allocable share is a measured number and whose residue is named rather than smoothed away. Rightsizing candidates a service owner will actually accept, because the evidence covers their peak and the risk is stated in terms they recognize. A commitment position that separates coverage from utilization and tests its own baseline against the migration plan. Every number traceable to a line on an invoice.
