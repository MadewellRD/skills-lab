---
name: unit-economics-desk
description: compute cloud unit cost metrics such as cost per tenant, per customer, per transaction, per active user, per inference, and per gigabyte served, with a sourced denominator definition. covers numerator scope and cost basis, denominator system of record with its definition quoted, driver decomposition separating rate from volume from mix, cohort and segment views where the aggregate hides the answer, trend against a named baseline, allocation and shared cost caveats that move the number, the owner who can act on it, and the metrics the data cannot yet support.
---

# Unit Economics Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the metric it affects and recorded in `open_questions`. Never invent denominator values, business volumes, customer or tenant counts, metric definitions, trend figures, or an owner for a metric nobody has accepted.

## Role

Own the ratio that connects spend to the business. This desk defines each unit cost metric with its numerator scope and cost basis, sources its denominator from the system of record for that business volume and quotes the definition that system uses, computes the value for a stated period, decomposes movement into rate, volume, and mix, cuts cohort and segment views where the aggregate hides the answer, attaches the allocation and shared cost caveats that materially move the number, names the owner who can actually change it, and names the metrics the data cannot yet support instead of approximating them.

A unit cost is the only figure in this suite that makes cloud spend legible to people who do not read billing exports. It is also the figure most easily broken, because it has two independent sources of error and they multiply. The numerator inherits every allocation gap upstream of it. The denominator comes from a different system, owned by a different team, using a word that means several different things inside one company. "Active user" alone has a definition in the product analytics system, another in the billing system, and a third in the board deck, and the three are rarely within twenty percent of each other.

## Use when

- Cost per tenant, customer, transaction, request, inference, seat, order, or gigabyte served is being computed for the first time or recomputed for a decision.
- A pricing, packaging, or tier conversation needs the cost side of the margin.
- Spend is growing and the question is whether it is growing faster than the business it serves, which no absolute figure answers.
- A cost movement needs decomposing into rate change, volume change, and mix change, because those three have completely different owners.
- Cohort, segment, plan tier, or region views are needed because the aggregate unit cost hides a small set of expensive consumers.
- An efficiency target is being set and needs a metric that survives the growth the company is planning for.
- Someone is quoting a unit cost whose denominator nobody has sourced.

## Do not use when

- Allocation coverage is unmeasured: that is `cost-allocation-tagging-desk`, and a unit cost over an unmeasured numerator carries an unknown error into a ratio.
- Shared and container splits are unsettled: that is `shared-cost-allocation-desk`, whose method assumptions become this metric's caveats.
- The question is gross margin, cost of revenue classification, or a figure that lands in a financial statement: that is `software-cogs-margin-desk`, which applies the accounting policy this desk does not.
- The question is what to present to an audience with a trend and a narrative: that is `showback-reporting-desk`.
- The metric is being used to build a plan or a budget line: that is `budget-planning-desk`.
- Cost per unit is high because a workload is oversized: that is `rightsizing-desk`, and because the design is expensive per request: `cost-aware-architecture-desk`.
- The denominator itself needs instrumenting or a data model built: cross-suite handoff to the Data suite.

## Required evidence

- Allocated cost at the granularity the metric needs, with its coverage figure and its shared cost assumptions.
- The business volume from its system of record, not from a dashboard that reads it, and the refresh behavior of that system.
- The definition of that volume as the owning system defines it, quoted rather than paraphrased, including its exclusions.
- Product, plan, tier, and customer structure where the metric is cut by segment.
- The decision the metric is meant to support, since it sets the numerator scope: a pricing floor needs a different scope from an engineering efficiency target.
- Prior periods for both numerator and denominator, on the same definitions, for trend.
- Known changes to the denominator's definition or instrumentation, which break a series without changing anything real.

## Workflow

**Outcome.** A metric set where each metric states its numerator scope and cost basis, its denominator with its system of record and quoted definition, its computed value and period, its trend against a named baseline, a driver decomposition separating rate from volume from mix, cohort or segment views where they change the conclusion, the caveats that materially move the figure, the owner who can act on it, and a named list of the metrics this data cannot yet support.

**Grounding.** The numerator comes from the allocated dataset with its coverage stated. The denominator comes from the system of record for that business metric, per the source hierarchy in `references/suite-workflow-contract.md`, and the definition travels with it as a quotation. Where two systems give different values for the same denominator, both readings are recorded with their locators rather than averaged or resolved toward the one that produces a better trend.

**Constraints.** The numerator scope is explicit about what is in and what is out, because a unit cost that includes shared platform cost and one that does not are different metrics with the same name. The cost basis is stated and is the same across periods in a trend, since switching between billed and amortized mid-series produces a movement that no consumption explains. The denominator's definition is quoted from its owning system and its period is aligned to the numerator's period, including the same partial-period treatment; a complete cost month divided by a partial usage month is a fabricated improvement. Allocation coverage below full is carried as a caveat with its figure, because the metric inherits that gap silently otherwise. Driver decomposition separates rate, volume, and mix explicitly, since a unit cost that fell because cheap customers grew faster than expensive ones is a mix effect that no engineering action produced and no engineering action will sustain. Cohort views are cut where the aggregate hides the answer, which in tenanted products it usually does, because a small number of heavy tenants routinely carry a large share of infrastructure and the mean tells nobody anything.

**Parallel surface.** Individual metrics, segments, cohorts, plan tiers, regions, and per-metric driver decomposition are independent units and fan out, as does connector preflight across the allocated dataset, the product analytics system, the billing system, and the customer structure source.

The aggregate is a single pass afterward. The blended unit cost across the estate is not the mean of the per-segment unit costs; it is total cost over total volume, and those differ whenever segments have different sizes, which is always. Coverage caveats are estate-level facts that apply to every metric computed from the same numerator, so they are established once and attached to all of them.

**Acceptance bar.** Every metric names its numerator scope, its cost basis, its denominator, the system that denominator came from, and that system's definition quoted, and a reader can recompute the value from the stated inputs and reach the same number.

## Outputs

A complete run delivers this artifact set:

- `unit-economics-definitions.md`: each metric with its identifier, numerator scope, cost basis, denominator, denominator source, the quoted definition including exclusions, and the decision it supports.
- `unit-economics-values.md`: computed values with period, trend against a named baseline, and the coverage state of the numerator behind each.
- `unit-cost-driver-decomposition.md`: movement split into rate, volume, and mix with the amount attributed to each, and the owner of each component.
- `unit-economics-cohorts.md`: segment, tier, cohort, or region cuts where the aggregate hides the finding, including the concentration picture where a small share of consumers carries a large share of cost.
- `unit-economics-caveats.md`: the allocation gaps, shared cost split assumptions, denominator instrumentation changes, and period alignment issues that materially move each metric, each quantified where the effect can be sized.
- `unit-economics-gaps.md`: the metrics the data cannot yet support, each with the specific missing instrumentation, field, or system of record, and what would unblock it.

Depth standard per artifact: a definition entry quotes the denominator's definition rather than naming the metric, because the whole failure mode lives in that sentence. A value entry gives numerator, denominator, and result, so the arithmetic is visible. A decomposition attributes an amount to each of rate, volume, and mix rather than describing which direction each moved. A cohort entry gives the distribution, since the useful finding is usually the tail. A gap entry names the system that would have to change, not the concept that is missing.

In `diagnostic` mode, when the denominator's system of record or the allocated dataset exists and cannot be read, the run delivers `unit-economics-connector-diagnostic.md` naming what was attempted and which metrics that leaves uncomputable. A metric is not computed against a denominator taken from a slide.

The specific hazard on this desk is the denominator that arrives without a source. Somebody in the conversation knows roughly how many tenants there are, the number is approximately right, and it is exactly the kind of input nobody re-derives once it has been divided into a cost. From there the ratio becomes a pricing floor, a board metric, and an efficiency target, and the error is invisible because the result looks reasonable at every step. A denominator with no system of record behind it makes the metric not computable, and not computable is written into the artifact with the system that would resolve it. Working backward from a per-unit figure somebody already quoted, in order to produce the volume that reproduces it, is the same error wearing arithmetic. Where two systems disagree on the denominator, both values appear with their sources and the metric carries both readings until the owners settle it.

## finops_packet fields to update

- `unit_economics[]` with `metric_id`, `metric`, `numerator_scope`, `denominator`, `denominator_source`, `denominator_definition`, `value`, `period`, `trend`, `owner`, and `caveats`.
- `reporting.known_distortions` where a denominator instrumentation change breaks a series.
- `cost_basis.view` referenced per metric where a metric uses a different view from the reporting default, with the reason recorded.
- `open_questions` for every metric the data cannot yet support, naming the missing source.
- `source_facts[]` with `locator` and `as_of` for both numerator and denominator, plus `assumptions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Source conflict: two systems of record give materially different values for the same business denominator. This is the defining halt for this stage, because a unit cost is a ratio and a denominator dispute is not a rounding question; it changes the number the company manages to and frequently reverses the trend.
- Release integrity: a unit cost would leave the practice without its denominator source and definition attached, computed across mismatched periods, or built on a numerator whose allocation coverage is unstated.
- Security or privacy: computing or presenting the metric would put customer identifiers, individual tenant consumption, or another customer's cost into an artifact or a shared view. Per-tenant cost is customer-identifying by construction and its audience is a privacy decision.
- Missing approval: the metric is bound for external reporting, an investor communication, or a customer-facing margin commitment, which raises the decision class beyond internal exploration.
- Production or destructive: the next action would change a metric definition in a system others already report from, or restate a published unit cost series.
- Connector unreachable: the allocated dataset or the denominator's system of record cannot be read. State whether the source was empty or unreachable, because a volume query returning zero and a volume system being down produce identical output and opposite meanings.

An unconfirmed metric owner, an unmeasured prior period, or a segment cut the customer structure does not yet support is a soft gap: proceed with it labeled against the metric it affects.

## Downstream handoffs

`software-cogs-margin-desk` needs the metric definitions and their numerator scopes, since a unit cost and a cost of revenue figure built on different scopes will not reconcile and somebody will eventually put them on the same slide. `budget-planning-desk` needs the driver relationships, because a driver-based budget is a unit cost multiplied by a planned volume. `forecasting-variance-desk` needs the rate, volume, and mix decomposition, which is the same decomposition variance attribution uses. `cost-aware-architecture-desk` receives the metrics whose movement traces to design behavior rather than to volume. `engineering-cost-review-desk` needs the metrics a team can actually move, with the owner named.

## Quality bar

Every metric is reproducible from the definition alone. The denominator's definition is quoted and its system named. Movement is decomposed into rate, volume, and mix with amounts rather than directions. Cohort views appear wherever the aggregate would mislead. Caveats are sized rather than listed. The metrics the data cannot support are named as clearly as the ones it can, so nobody builds a target on a number that does not exist yet.
