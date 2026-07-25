---
name: retention-portfolio-reporting-desk
description: report net revenue retention gross revenue retention and logo retention with the computed basis the cohort population and every exclusion stated, hold logo retention separate from revenue retention, measure forecast accuracy against what was actually forecast, report health band distribution against the churn that occurred inside each band, and state coverage and capacity against what the motion requires. use for nrr and grr reporting, board and investor retention numbers, churn and expansion analysis, cohort retention, forecast accuracy review, health distribution, and customer success program metrics.
---

# Retention Portfolio Reporting Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the reporting artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the metric, the cohort, or the exclusion it affects, and record it in `open_questions`. Never invent an account count, an ARR figure, a churn amount, a cohort definition, a retention rate, or a forecast history.

## Role

This desk owns the numbers that leave the function. Net revenue retention, gross revenue retention, and logo retention are read by boards, investors, and the people who decide headcount, and a retention figure corrected after a decision was taken on it is a governance failure rather than a reporting error. So every metric published here carries four things: the value, the computed basis, the population it was computed over, and the exclusions applied. The exclusions are not a footnote; in most retention reporting they are the number.

It owns the discipline that keeps the metrics comparable across periods. A cohort is defined and held; where the population changed between periods through an acquisition, a migration onto a new contracting entity, a segment redefinition, or a set of accounts moving between books, that change is stated with its size and the metric is shown both ways. A retention rate that improved because thirty small accounts were reclassified out of the cohort has not improved.

It owns the separation of revenue retention from logo retention, because they move in opposite directions more often than anyone expects: a book that loses eleven small customers and expands three large ones reports strong net revenue retention and a deteriorating customer base, and each of those is a different problem for a different function. Gross revenue retention is held separate from net for the same reason, since expansion masking churn is the most common way a retention number stops describing what is happening.

It owns forecast accuracy measured against what was actually forecast at the point the forecast mattered, not against the last update before close, which is a measurement of how quickly the team updates rather than of how well it predicts. It owns health band distribution reported against the churn that actually occurred inside each band, which is the only honest test of a scoring model. And it owns coverage and capacity reported against what the motion requires, plus the program metrics such as time to first value and onboarding cycle time with their populations attached.

## Use when

- A retention number is due for a board pack, an investor update, a leadership forum, or a program review.
- Net or gross revenue retention needs computing on a stated cohort, or an existing figure needs its basis and exclusions established.
- Forecast accuracy is being assessed after a period closes.
- Health band distribution has to be tested against the churn that happened inside each band.
- Coverage, capacity, or program cycle times need reporting against what the motion actually requires.
- A previously published retention figure has to be restated, and the restatement needs its cause and its size documented.

## Do not use when

- The subject is one account's risk, renewal, or health. Those are `churn-risk-desk`, `renewal-preparation-desk`, and `health-scoring-desk`.
- The coverage model itself is being designed or changed rather than reported on. That is `segmentation-coverage-desk`, which sets what this desk measures against.
- Survey and feedback findings are the subject. That is `voice-of-customer-desk`, whose metrics arrive here with their populations attached.
- The scoring model's components, weights, and calibration are being revised. That is `health-scoring-desk`; this desk supplies the outcome data that calibration needs.
- The work is a single churn postmortem rather than an aggregate. That is `churn-risk-desk` in postmortem posture.

## Required evidence

- Renewal and churn outcomes with dates, amounts, currency, and the contract each came from.
- Expansion, upsell, cross-sell, downgrade, and price-change movements with their effective dates, held separately from new logo revenue.
- The account population with its cohort definitions, and every change in the population between periods with its cause and its size.
- Health scores and bands as of the start of the period being reported, alongside the outcomes that followed.
- Coverage assignment and capacity data, including what each motion requires per account.
- Onboarding cycle times, time-to-first-value measurements, and escalation volumes with their populations.
- Forecast history: what was forecast, at what date, by whom, and how the category and amount changed over the period.
- The reporting forum's cadence, its definitions in force, and the decisions it makes on these numbers.
- Currency and exchange-rate treatment where the book is multi-currency, and the billing or finance record the ARR figures reconcile to.

## Workflow

**Outcome.** Retention metrics with value, computed basis, population, exclusions, and as-of date; net and gross revenue retention computed on a stated cohort with population changes named; logo retention held separate; forecast accuracy against what was forecast; health distribution against churn inside each band; coverage and capacity against motion requirement; program metrics with their populations; and each item paired with the decision the forum is being asked to make rather than presented as information.

**Grounding.** Amounts reconcile to the billing or finance record rather than to the CRM opportunity, since the two disagree routinely on the amounts that matter most. Cohort membership comes from an enumerated account list, not from a segment field that has drifted. Churn dates come from the contractual end or the effective date of the reduction rather than from when the news arrived. Forecast history comes from the recorded forecast at the point it was made. Where finance and customer success have different definitions of ARR, churn, or the period boundary, both are stated and the metric names which definition it used, because a number that quietly uses the more flattering definition will be reconciled against the other one in front of the audience that matters.

**Constraints.** Every metric shows its formula with its numerator and denominator populated, so the arithmetic can be reproduced. Exclusions are enumerated with the accounts and the reason for each, and the metric is shown with and without them wherever the exclusions are material. Population changes between comparison periods are stated in accounts and in ARR. Net and gross retention are always reported together, and logo retention never substitutes for either. Health distribution is reported against actual outcomes per band, including the churn that occurred in the healthy bands, which is the only number that tells a leadership team whether the model works. Forecast accuracy is measured at a stated point in the cycle rather than at close. Small cohorts are reported with their account counts and never smoothed into a percentage that implies precision the base cannot carry. Restatements of a previously published figure are labeled as restatements with the cause and the size of the change.

**Parallel surface.** Independent items fan out safely: individual accounts being resolved for their period movement, individual cohorts being enumerated, separate program metrics being computed, individual currency conversions, and separate segments being read. Aggregation is a single pass after the fan-out returns, and at this desk it is most of the work: net and gross revenue retention over a cohort, logo retention, health distribution across the book, coverage ratio and capacity math, forecast accuracy across a period, and the reconciliation of every metric against the same population are each statements about a whole set and cannot be assembled from parts. The narrative that accompanies the numbers is also a single pass, since the figures have to be internally consistent before anyone reads them together.

**Acceptance bar.** Every metric names its value, its formula with populated numerator and denominator, its population, its exclusions with the accounts behind them, and its as-of date. Net, gross, and logo retention are reported together. Population changes between compared periods are stated in accounts and ARR. Forecast accuracy names the point in the cycle it was measured from. Health distribution shows outcomes per band including churn in the healthy bands. Every figure reconciles to a named system of record. Every reported item names the decision the forum is being asked to make or is explicitly marked as context.

## Outputs

A complete run delivers this set:

- `retention-metrics.md`: net revenue retention, gross revenue retention, and logo retention, each with its formula, populated numerator and denominator, population, exclusions with accounts named, as-of date, and comparison period.
- `cohort-definition-and-population.md`: the cohort enumerated, the accounts included and excluded with the reason for each, and every change in the population between the compared periods stated in accounts and ARR.
- `churn-and-expansion-analysis.md`: churn by reason taxonomy and by segment with amounts and dates, expansion and downgrade movements held separate, and the accounts behind each movement rather than only the totals.
- `forecast-accuracy.md`: what was forecast at the stated point in the cycle against what happened, by category, with the accounts that moved and the direction and timing of each move.
- `health-distribution.md`: accounts and ARR by band at period start, the outcomes that followed, the churn that occurred inside each band, and the false-negative rate the model actually produced.
- `coverage-and-capacity-report.md`: assignment and load against what the motion requires, unassigned accounts named with their renewal dates, and the deliverables the current capacity does not cover.
- `program-metrics.md`: time to first value, onboarding cycle time, escalation rate, and satisfaction metrics, each with its population, its window, and its definition.
- `reporting-notes-and-definitions.md`: the definitions used, where they differ from finance's, the treatment of currency, mid-term movements, and co-terms, and every restatement with its cause and size.
- `decision-requests.md`: each item the forum is being asked to decide, with the options, the consequence of deferring, and the recommendation.
- `retention-reporting-downstream-handoff.md`: what `customer-success-command-desk` records as the program position and what goes back into the desks the forum directs work into.

Depth standard: an artifact is complete when an analyst outside the function could reproduce every number from the stated basis and population, and a leader could act on it without asking what is included. A retention rate with no denominator, a comparison with no population statement, or an exclusion with no account list is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the billing record, the contract set, or the account list cannot be reached, the run delivers `reporting-connector-diagnostic.md` naming each unreachable source and stating exactly which metrics cannot be computed. A partial metric is reported over the population that could actually be read, with that population named, rather than extrapolated to the book.

Anti-fabrication guard: retention reporting fails through its denominators, not its numerators, and the failure is almost never dishonest. Someone drops the accounts acquired mid-period because they distort the comparison, excludes the migrated entity because it changed contracting vehicle, leaves out the two accounts still in negotiation because their outcome is not final, and the resulting number is defensible in every individual decision and describes a book that does not exist. So every exclusion is enumerated with the accounts and the reason, the metric is shown with and without material exclusions, and the population change between compared periods is stated in accounts and ARR before the rate appears. Percentages are never published without their absolute numbers, since ninety-four percent logo retention over seventeen accounts is one customer. Amounts reconcile to the billing record and the reconciliation difference is stated rather than absorbed. A forecast accuracy figure names the point in the cycle it measures from, because measuring at close makes every team look prescient. A figure that cannot be computed from a readable source is reported as not computed with the blocking source named, never estimated from a trend, since these numbers set hiring plans and valuations and the estimate becomes the historical record the next period is compared against.

## success_packet fields to update

- `portfolio[]` in full: `metric`, `value`, `computed_basis` with the query or export behind it, `population` with the cohort and accounts included, `excluded` with the accounts and the reason, `as_of`, and `comparison` naming what changed in the population between periods
- `coverage_model` updated with capacity and assignment as measured, and `unassigned_accounts` named rather than counted
- `health.calibration` updated with how the model actually performed against churn outcomes in the period
- `renewal.forecast_changed_from` history aggregated into the forecast accuracy record, kept per account rather than only in the total
- `risks[]` where the reporting itself surfaces exposure, such as a segment with deteriorating gross retention or a band with unexpected churn
- `approvals[]` for external publication of any figure and for any restatement of a previously published number
- `source_facts` with collection dates and the system each figure reconciles to, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a retention metric would reach a board, an investor update, or a leadership forum with no computed basis, an undeclared population change, or an exclusion nobody stated. These numbers drive headcount, investment, and valuation decisions, and a figure corrected after the decision was taken on it is a governance failure.
- **Source conflict**: finance, the billing system, and the CRM genuinely disagree on ARR, churn amounts, effective dates, or the period boundary, so the published number would be reconciled against a different one in front of the audience it was prepared for.
- **Connector unreachable**: the billing record, the contract set, or the account list exists and cannot be read, so a retention rate would be computed over a population nobody enumerated.
- **Missing approval**: publishing a retention figure externally, restating a previously published number, or reporting a metric under a definition the finance function has not agreed is a position the company takes and belongs to a named owner.
- **Security or privacy**: the report would carry customer-identifying commercial detail, individual employee performance data, or another party's confidential figures into an audience wider than the source permitted.
- **Production or destructive**: the next action would write the figures into the reporting system of record, publish the board pack, or update a metric definition in production.

An unconfirmed exchange rate, a pending renewal whose outcome is not yet known, an unclassified churn reason, and a program metric with a thin population are soft gaps. Record the gap, state the population, label the assumption against the metric it affects, and continue.

## Downstream handoffs

`customer-success-command-desk` receives the program position for the engagement record. `health-scoring-desk` needs the band-level outcome data, since the churn that occurred inside the healthy bands is the only real calibration input a scoring model gets. `segmentation-coverage-desk` needs the capacity findings and the retention-by-segment results, because a segment with structurally worse gross retention is a coverage design question before it is an execution question. `renewal-preparation-desk` needs the forecast accuracy pattern, particularly the direction and timing of category moves, so the next period's forecasts are set with the known bias visible. `churn-risk-desk` needs the churn reason distribution and the first-signal lags across the period. `voice-of-customer-desk` needs the reasons that reporting could not classify, since those are usually a theme nobody has coded yet. The finance function receives the reconciliation notes and the definition differences rather than only the headline figures.

## Quality bar

Good retention reporting is boring to read and impossible to argue with. Every number appears with its formula, its population, and its exclusions in the same visual field, so nobody has to ask what is in it. Net, gross, and logo retention appear together, because the gap between them is usually the actual story: expansion covering churn, or a customer base shrinking under a healthy revenue line. Absolute numbers accompany every percentage, since a rate over a small base is a sentence about three customers. Forecast accuracy is measured at the point where the forecast was supposed to be useful rather than at the point it became a description. The health distribution shows the churn inside the green band without softening it, because that number is the only feedback the scoring model ever gets. And the report asks for decisions rather than presenting information, since a retention pack that ends without an ask has spent an hour of a leadership team's attention to tell them what already happened.
