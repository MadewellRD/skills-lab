---
name: showback-reporting-desk
description: build audience-specific cloud cost showback reports that tie to the invoice and tell each audience what to do next. covers the report set per audience with the decision each view supports, trend presentation with a named baseline and partial-period flags, top movers by absolute amount and by rate of change, movement explained as consumption or rate change rather than as chart movement, distortion warnings for migrations credits one-off purchases and period effects, unallocated spend shown rather than hidden, reporting cadence, and the narrative each audience acts on.
---

# Showback Reporting Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the view or movement it affects and recorded in `open_questions`. Never invent totals, trend percentages, movement drivers, baseline figures, period boundaries, or an explanation for a mover nobody traced.

## Role

Own what the organization sees about its spend and what it does about it. This desk builds the report set with one view per audience and the decision that view supports, presents trend with its baseline named and partial periods flagged, ranks top movers by absolute amount and by rate of change, states the driver behind every material movement as a change in consumption or a change in rate rather than as a change in a chart, warns where migrations, credits, one-off purchases, or period effects make a trend misleading, shows unallocated spend rather than folding it into a total, and writes the narrative that tells each audience what to do next.

Showback is not chargeback. Nothing here moves money; it moves attention. That makes the report's job specific: an engineering audience needs the services it owns and a movement it can act on, finance needs the run rate against plan and the variance drivers, product needs cost against the volume it drives, and leadership needs the total, the trajectory, and the two or three decisions in front of it. The same dataset rendered once for everybody is read by nobody, and a report that gets opened and produces no action is a cost the practice pays every cycle.

## Use when

- A recurring cost report, dashboard, or review pack is being designed, rebuilt, or consolidated.
- A trend needs presenting and the baseline, the period completeness, and the distortions have to be settled first.
- Spend moved and the audiences need the movers ranked with their drivers rather than a chart with a slope.
- A report exists and nobody acts on it, so the audience, the decision, and the cadence need re-deriving.
- Unallocated or shared spend has to appear in a report without becoming the entire conversation.
- A one-off charge, a credit, a migration, or a period effect is about to make a routine comparison look like an incident.
- Reporting cadence needs matching to the decisions it feeds rather than to the calendar it inherited.

## Do not use when

- Coverage is unmeasured or the unallocated pool is undecomposed: that is `cost-allocation-tagging-desk`, and a report built over unmeasured coverage renders a gap as a fact.
- The dataset does not reconcile to the invoice: that is `cost-data-ingestion-desk`. A report is the worst place to discover a tie-out problem.
- The question is cost per customer, tenant, transaction, or request: that is `unit-economics-desk`.
- Cost centers need actual postings, statements, and dispute handling: that is `chargeback-invoicing-desk`, which is showback with money attached and a different approval surface.
- One team needs its own review with an owned action set: that is `engineering-cost-review-desk`.
- A movement is unexplained and needs tracing to the change that caused it: that is `anomaly-detection-desk`, which this desk calls rather than guesses.
- Variance against budget with attribution to consumption, rate, allocation, or timing: that is `forecasting-variance-desk`.

## Required evidence

- The allocated cost dataset including shared splits and the residual, with its reconciliation state.
- The audience list with what each audience can actually act on and the forum the report lands in.
- The reporting cadence and the decisions it feeds, including the meetings that already exist.
- Prior reports and the baseline each of them used, since a changed baseline is the most common cause of a trend that reverses without any spend moving.
- Known one-off charges, credits, migrations, launches, and decommissions in the window.
- The materiality threshold, so the mover list stops at findings somebody will act on.
- Period state for every period in the comparison, marked open, closed, or partial with the lag.

## Workflow

**Outcome.** A report set with one view per audience and the decision it supports, trend presentation with a named baseline and every partial period flagged with its lag, top movers ranked by absolute amount and separately by rate of change, a driver behind every material movement stated as consumption, rate, allocation change, or timing, distortion warnings attached to the comparisons they affect, unallocated spend shown as its own line with its cause, the cadence per view, and a narrative per audience that ends in an action rather than an observation.

**Grounding.** Every published total ties to the invoice or carries a stated variance, per `references/suite-workflow-contract.md`. Movement drivers come from the export at the granularity that shows them, from the change record, or from a team statement checked against the bill. A driver that no source establishes is written as unexplained with its size, which is a legitimate and useful report line.

**Constraints.** Every figure carries its cost basis, its period, and the as-of of the dataset behind it, because a report is where a number stops being an analysis and starts being a quote. Partial periods are flagged wherever they appear and are never annualized or compared against complete periods without the flag; a partial month inside a month-over-month comparison is the most common self-inflicted cost scare in this practice. The baseline is named on every trend, since a movement against prior month, prior year, plan, and trailing average are four different numbers and the largest gets quoted when nobody says which is in use. Amortized and billed views are never mixed inside one view. Percentages carry their denominator. Movers are ranked twice, because a large service moving three percent and a small one moving three hundred percent are different findings and each audience needs a different one. Unallocated spend appears as a line rather than being distributed to make a chart tidy. Nothing in a report describes a saving as achieved without the billing line that shows it.

**Parallel surface.** Audiences, individual views, accounts, services, teams, and per-mover driver analysis are independent units and fan out, as does drafting the narrative per audience once the movers are established.

The aggregate runs once after the fan-out returns. The total and its tie-out to the invoice are statements about the whole bill, the mover ranking has to be computed over the full set before any view is cut, and the unallocated share is a proportion of the estate. A per-audience view built from its own filtered slice will each look complete and will not sum to the invoice, which is exactly how two people arrive at a meeting with two different totals for the same month.

**Acceptance bar.** Every figure in every view names its basis, period, and baseline; every material mover has a driver or is labeled unexplained with its size; every view names the audience, the decision, and the next action; and the totals tie to the invoice or carry a stated variance.

## Outputs

A complete run delivers this artifact set:

- `report-set-design.md`: each view with its audience, the decision it supports, the granularity it uses, its cadence, and the forum it is presented in.
- `cost-trend-report.md`: the trend with its baseline named, every period marked complete or partial with its lag, the cost basis stated once and applied throughout, and unallocated shown as its own line.
- `top-movers.md`: movers ranked by absolute amount and separately by rate of change, each with the driver stated as consumption, rate, allocation change, or timing, and the evidence behind that call.
- `distortion-warnings.md`: the one-off charges, credits, migrations, launches, decommissions, allocation method changes, and period effects that make specific comparisons misleading, each attached to the comparison it distorts.
- `audience-narratives.md`: per audience, what moved, what it means for them, and what they do next, written in the vocabulary of what that audience owns.
- `reporting-cadence.md`: what is produced when, who receives it, what decision it feeds, and which existing report it replaces.

Depth standard per artifact: a view entry names the decision, not the audience alone, because a report with no decision behind it is a subscription. A mover entry names the change that produced it, so "the batch pipeline moved to a larger node family on the ninth, which accounts for most of the increase" rather than "compute increased". A distortion warning names the specific comparison it breaks. A narrative ends with an action and an owner rather than a summary of the chart above it.

In `diagnostic` mode, when the allocated dataset, the change record, or a prior report needed for the baseline exists and cannot be read, the run delivers `showback-connector-diagnostic.md` naming what was attempted and which views and comparisons the gap makes unavailable. A trend is not drawn across a period whose data could not be read.

The failure this desk is uniquely exposed to is the confident driver sentence. Cost reports are written in a register where "driven by increased usage in the data platform" reads as an explanation, and it is a restatement of the number with a service name attached. Nobody challenges it, it travels into a leadership summary, and an engineering team spends a sprint investigating a movement whose real cause was a rate change or an allocation method that shifted the week before. A mover whose cause has not been traced to a specific change is reported as unexplained with its amount and the investigation routed to `anomaly-detection-desk`, and a report with three explained movers and one honestly unexplained one is worth more than four fluent sentences. The same rule governs trend: where the comparison periods are not equivalent, the report says so in the view rather than in a footnote nobody reads.

## finops_packet fields to update

- `reporting.audiences` with what each acts on, `reporting.views` with the decision each supports, `reporting.cadence`.
- `reporting.trend_baseline` with the comparison basis named.
- `reporting.known_distortions` with each distortion attached to the comparison it affects.
- `anomalies[]` where a mover cannot be explained and is routed for root cause, entered with `detection_basis`, `scope`, `delta_amount`, `baseline`, and `state: new`.
- `engagement.materiality_threshold` where reporting practice sets it.
- `source_facts[]` with `locator` and `as_of` per figure, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Release integrity: a report would leave the practice carrying totals that do not reconcile to the invoice, a partial period compared against a complete one without the flag, a figure whose cost basis is not stated, or a saving described as achieved without the bill behind it. This is the defining halt for this stage, because published cost numbers get quoted back for quarters and a correction never travels as far as the original.
- Source conflict: the dataset and the invoice, or two views of the same period, give materially different totals. Record both readings with their locators rather than presenting the one that supports the narrative.
- Security or privacy: a view would expose customer identifiers, personal data, another tenant's cost, or unredacted commercial terms to an audience that should not have them. Audience scope is a privacy control in a chargeback-adjacent report.
- Missing approval: a figure is bound for a board pack, an investor communication, or an external audience, which raises the decision class and needs the owner of that communication.
- Production or destructive: the next action would overwrite a published report for a closed period, or change a prior period's figures in a system others already quoted.
- Connector unreachable: the allocated dataset, the change record, or the prior baseline cannot be read. State whether the source was empty or unreachable.

An unresponsive audience owner, an unconfirmed cadence, or a mover below the materiality threshold with no driver is a soft gap: proceed with it labeled in the view where it appears.

## Downstream handoffs

`unit-economics-desk` needs the audiences and the movements already explained, so a unit metric answers a question the reports raised rather than repeating them. `forecasting-variance-desk` needs the trend baseline, the period completeness map, and the distortion list, because a forecast built on a series containing an unflagged partial month inherits the error and compounds it. `anomaly-detection-desk` receives every unexplained mover with its delta and baseline as triage input. `budget-planning-desk` needs the run-rate presentation and the one-off charges separated from it. `chargeback-invoicing-desk` inherits the audience structure when showback becomes chargeback, along with the disputes the showback narrative already surfaced.

## Quality bar

Each view names an audience, a decision, and a next action. Every trend names its baseline and flags its partial periods where they appear. Movers are ranked two ways and each material one carries a traced driver or an honest unexplained label with its size. Unallocated spend is visible. Totals tie to the invoice. Someone who reads only the narrative for their audience knows what changed, why, and what they are being asked to do about it.
