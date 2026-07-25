---
name: data-platform-cost-desk
description: analyze data platform spend covering the compute storage and transfer breakdown from the billing export, top cost drivers named as specific queries pipelines and dashboards, spend attribution and the unattributable share, efficiency findings across partition pruning failures full scans exploding joins over-frequent refresh idle compute small files and redundant materializations, the stated cost of freshness, chargeback design, and query guardrails and quotas. use for warehouse cost reviews and spend reduction.
---

# Data Platform Cost Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the cost artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. An unattributable share of spend is a soft gap and is reported as a number rather than distributed by guesswork; a billing export that exists and cannot be read is a hard halt, because every figure in the artifact set would then be an estimate presented as an accounting. Never invent spend figures, unit prices, credit or slot consumption, query costs, savings percentages, or the team a workload belongs to.

## Role

Own what the platform costs and why. This desk holds the compute, storage, and transfer breakdown taken from the billing export, the top drivers named as specific queries, pipelines, dashboards, and jobs, the attribution of spend to teams, products, and workloads with the unattributable share stated, the efficiency findings that actually move the number, the cost of freshness stated as a trade, the chargeback or showback design, and the guardrails that stop a single query consuming a month of budget.

Two properties shape this stage. Cost in a data platform is a consequence of design decisions made in other stages, so the finding is almost never that the platform is expensive; it is that a partition key does not match the predicate that filters, that a mart refreshes hourly for a report read on Mondays, or that a dashboard runs its own aggregation over a billion rows on every page load. And attribution is genuinely hard rather than merely unfinished: shared compute means a warehouse bill does not decompose cleanly into per-team shares, so the honest artifact reports the attributable spend, the method, and the residue instead of allocating everything to make the pie add up.

## Use when

- Platform spend has grown, a budget is being set, or a cost review is due and the drivers need naming rather than describing.
- Specific workloads need identifying as the source of the spend, at the level of a named query, pipeline, dashboard, or job rather than a category.
- Spend needs attributing to a team, product, or workload, and the share that cannot be attributed needs stating honestly.
- Efficiency work needs a ranked list: pruning failures, full scans, exploding joins, over-frequent refresh, idle or oversized compute, small files, redundant materializations, and stored data nobody queries.
- A freshness requirement needs its cost stated, so an hourly refresh is a business decision rather than a default nobody priced.
- Chargeback or showback is being designed and the allocation method needs deciding along with what it will fail to allocate.
- Guardrails are needed: query timeouts, scan limits, result caps, warehouse auto-suspend, concurrency limits, and budget alerting.
- A migration or dual run has doubled the bill and the spend needs separating between the two platforms.

## Do not use when

- The subject is whether the data may be deleted rather than whether it is expensive. That is `data-retention-lifecycle-desk`, whose retention floor bounds every storage reduction proposed here.
- The subject is the partitioning, clustering, file sizing, or materialization choice as a design decision. That is `warehouse-lakehouse-architecture-desk` and `transformation-layer-desk`; this desk supplies the measured cost of the choice they made.
- The subject is schedule frequency and dependency triggering. That is `batch-orchestration-desk`, which receives the refresh frequency finding produced here.
- The subject is organization-level cloud spend policy, commitments, reserved capacity, or chargeback governance beyond this platform. That is a labeled cross-suite handoff to the FinOps suite.
- The subject is the underlying cloud infrastructure and its sizing. That is a labeled cross-suite handoff to the Cloud Infrastructure suite.

## Required evidence

- The billing or usage export at the granularity the platform provides, covering the period being analyzed, with its collection date.
- Query history with cost or consumption per statement: bytes or partitions scanned, slot or credit time, spill, queue time, and the user, role, or tag that issued it.
- The compute inventory: warehouses, clusters, pools, or reservations with their size, auto-suspend setting, uptime, and idle time.
- Storage inventory by table and partition, including snapshot and time travel storage, small file counts, and the last-queried date per asset.
- The pipeline and schedule inventory with run frequency, run duration, and the compute each run consumes.
- Dashboard and extract refresh schedules with their query cost, which is frequently a larger driver than the pipelines feeding them.
- The tagging or attribution scheme that maps a workload to an owner, and the fraction of spend it currently reaches.
- The freshness and concurrency requirements the spend is buying, from the data product definitions.

## Workflow

**Outcome.** A spend breakdown across compute, storage, and transfer taken from the export with its period; the top drivers named as specific workloads with their measured consumption; attribution to teams, products, and workloads with the unattributable share stated as a figure; a ranked efficiency finding set with the measured cost of each and the change that addresses it; the cost of freshness stated per data product as a comparison between refresh frequencies; a chargeback or showback design with its method and its limits; and a guardrail set.

**Grounding.** Every figure names the export, query history record, or usage view it came from, along with the period and the collection date, because platform spend moves week to week and a figure without a period is not a measurement. Drivers are identified from consumption records rather than from suspicion, so the pipeline everyone believes is expensive is either shown to be expensive with its consumption attached or shown not to be. Savings are separated into measured and estimated, and an estimate carries the assumption it rests on rather than being presented as a projection.

**Constraints.** Every top driver is named as a specific object: the query text or its hash, the pipeline and task, the dashboard and its panel, the warehouse and its idle window. A category such as transformation compute is a grouping rather than a driver, and a finding that names one is not actionable. Efficiency findings state the mechanism, the measured cost today, the change, and what the change would break, since most of them trade cost against latency, freshness, or concurrency that a consumer is currently relying on. Pruning failures name the predicate and the partition or cluster key that failed to serve it, including the common causes of a function wrapping the partition column, a type mismatch forcing a cast, and a join predicate the engine cannot push down. The cost of freshness is stated as a comparison between the current cadence and at least one slower cadence with the figure attached, so the trade is legible to the person who set the requirement. Attribution states its method and its residue; unattributed spend is reported as a number, and shared compute is described as shared rather than divided by headcount to make the allocation complete. Guardrails name the threshold, what happens when it is hit, and who is notified, because a quota that silently kills a finance job at quarter close is a worse outcome than the query it prevented.

**Parallel surface.** Individual workloads, queries, pipelines, dashboards, warehouses, and tables are independent analysis units and fan out safely, as does the per-object efficiency assessment and the per-asset storage and last-queried read. The aggregate work runs once after the fan-out returns: reconciling the sum of attributed workloads against the billing export total, allocating shared compute, ranking findings by measured impact against implementation cost, and composing the cost of freshness across a dependency chain where an hourly mart forces hourly refreshes on everything upstream of it. A per-query cost list that is never reconciled against the export total is how a review reports finding sixty percent of the spend and leaves the rest unexamined without saying so.

**Acceptance bar.** A reader could state where the money goes by component and by workload, which specific objects account for the top of the bill, what share could not be attributed and why, what each efficiency finding would save with the measurement behind it, and what an hourly refresh costs against a daily one. Every figure carries its source and its period, and estimated savings are labeled separately from measured ones.

## Outputs

A complete run delivers this set:

- `spend-breakdown.md`: compute, storage, and transfer with the export and period each figure came from, the trend across periods where history supports it, and the components the export does not itemize.
- `top-drivers.md`: the workloads accounting for the top of the bill, each named as a specific query, pipeline, dashboard, or warehouse with its measured consumption, its frequency, and its owner.
- `spend-attribution.md`: spend mapped to teams, products, and workloads with the method stated, the shared compute described as shared, and the unattributable share given as a figure rather than distributed.
- `efficiency-findings.md`: ranked findings with the mechanism, the measured cost today, the proposed change, the expected saving marked as measured or estimated, and what the change costs in latency, freshness, or concurrency.
- `cost-of-freshness.md`: per data product, the current cadence and its cost against at least one slower cadence, with the consumer requirement that set the cadence and the owner who can change it.
- `chargeback-design.md`: the allocation method, what it can and cannot attribute, the reporting cadence, and the behavior it will incentivize including the workloads it will push into untagged compute.
- `guardrails.md`: query timeouts, scan and result limits, warehouse sizing and auto-suspend, concurrency limits, budget alerts and their thresholds, with the owner and the exemption path for the jobs that legitimately exceed them.
- `cost-downstream-handoff.md`: what `data-incident-response-desk` and the architecture, orchestration, and enablement stages inherit, including the design decisions the findings trace back to.

Depth standard: an artifact is complete when an owner could act on a finding without re-running the analysis and a budget holder could accept the attribution. A driver named as a category, a saving with no measurement or stated assumption, and an attribution that quietly allocates the residue are unfinished rather than draft.

When the billing export, query history, or the compute and storage inventory exists and cannot be read, the run delivers `cost-connector-diagnostic.md` naming each unreachable source and the spend, attribution, and savings claims that depend on it, in place of the artifacts that source would have grounded. Spend is never described from the shape of the architecture.

Anti-fabrication guard: cost artifacts are read as accounting, and this desk's characteristic failure is arithmetic that looks audited. A percentage saving is the most quoted line any cost review produces, it survives into budget commitments, and it is the line most easily generated from a plausible model of the workload rather than from consumption records. So every saving states whether it was measured from an actual before-and-after or estimated from an assumption, and every estimate carries that assumption in the same sentence. Spend figures, unit prices, credit and slot consumption, and bytes scanned come from the export or the query history with the period attached, and where the export could not be read the figure is written as unmeasured rather than derived from published list prices. Attribution never closes the gap for tidiness: the unattributable share is a number in the artifact, because a chargeback model that allocates everything is one that has invented the last portion and will be defended in a budget meeting by someone who believes it. And a workload is named as a driver only when its consumption record says so, since accusing the wrong pipeline sends an engineering team to optimize something that was never the cost.

## data_packet fields to update

- `cost.spend_source` with the export and the period it covers
- `cost.compute_vs_storage` with the measured split and its source
- `cost.top_drivers` naming specific workloads with their consumption records
- `cost.attribution` with the method and the unattributable share
- `cost.efficiency_findings` with measured cost, proposed change, and measured against estimated saving
- `data_products[].freshness_target` annotated with the cost of the cadence it requires
- `storage_architecture.file_sizing` and `snapshot_retention` where small files or snapshot storage are drivers
- `data_risks[]` for guardrail gaps where one query can consume a budget
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: the billing or usage export, query history, or the compute and storage inventory needed for this stage exists and cannot be read, so every figure would be an estimate presented as an accounting.
- **Production or destructive**: the next action would resize, suspend, or delete compute a consumer depends on, apply a quota or timeout to live workloads, drop stored data, or change a refresh schedule.
- **Missing approval**: reducing the refresh frequency of a data product, applying a guardrail that can fail a production job, retiring stored data, or adopting a chargeback allocation needs the product owner or budget holder, who has not agreed.
- **Release integrity**: a saving would be recorded as measured without a before-and-after, or an attribution presented as complete while a material share is unattributed and unstated.
- **Security or privacy**: query text captured as evidence would carry personal, health, or cardholder values in literals or predicates, or attribution would expose a restricted workload to an audience that should not see it exists.
- **Source conflict**: the billing export and the platform's usage view genuinely disagree on consumption for the same period, and choosing one silently would publish a spend figure that does not hold.

An unattributable share, an untagged workload, an unknown workload owner, and a missing price for a component the export does not itemize are soft gaps. Name them, label the assumption, and continue. The requirement that a saving be labeled measured or estimated, and that the unattributable share be stated rather than allocated, is never relaxed to produce a better headline number.

## Downstream handoffs

`data-incident-response-desk` is next in the default sequence and inherits the guardrail set, since a runaway query and a cost incident are the same event seen from two sides. `warehouse-lakehouse-architecture-desk` receives the pruning, clustering, file sizing, and snapshot storage findings, which are design decisions rather than cost decisions. `batch-orchestration-desk` receives the refresh frequency findings and the idle compute windows. `transformation-layer-desk` receives redundant materializations and the models whose incremental strategy causes full recomputation. `analytics-enablement-desk` receives the dashboards and extracts driving spend, including the ones with low measured usage. `data-retention-lifecycle-desk` receives stored data nobody queries, and supplies the retention floor that bounds its removal. Send commitments, reserved capacity, organization-level chargeback governance, and cloud spend policy to the FinOps suite as a labeled cross-suite handoff.

## Quality bar

Good cost work names objects and cites records. Its drivers are queries and pipelines a person can open, not layers of the stack. Every figure carries a period and a source, and the analysis reconciles the workloads it examined against the total bill so the reader knows how much of the spend was actually looked at. Findings state what the change costs as well as what it saves, because most cost reductions are latency or freshness reductions wearing a different label. Savings are marked measured or estimated. The unattributable share is printed rather than absorbed. And the cost of freshness appears as a comparison with numbers on both sides, since the single most effective thing this desk produces is a conversation in which the person who asked for hourly data learns what hourly costs.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
