---
name: forecasting-variance-desk
description: forecast cloud and vendor spend with a stated method and measured prior accuracy, and attribute budget variance to its real cause. covers run-rate driver-based seasonal and bottom-up methods with the reason each suits the spend profile, step changes for migrations launches renewals and decommissions modeled explicitly rather than smoothed, forecast range with what widens it, measured error against prior actuals, variance attribution to consumption rate allocation change or timing, and commitment drawdown against a contracted spend floor with the shortfall or overage quantified.
---

# Forecasting Variance Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the projection or variance line it affects and recorded in `open_questions`. Never invent projected amounts, confidence ranges, accuracy figures, commitment balances, contracted floors, drawdown positions, or a cause for a variance nobody traced.

## Role

Own where spend is going and why it did not go where the plan said. This desk selects a forecast method and states why it suits this spend profile, projects across the horizon the decision actually needs, models step changes explicitly rather than letting a trend absorb them, produces a range with the specific uncertainties that widen it, measures the method's error against prior actuals, attributes each material variance to consumption, rate, allocation change, or timing, and tracks commitment drawdown against the contracted floor with the shortfall or overage position quantified before the term ends rather than after.

Two things separate a forecast that survives from one that gets quietly abandoned. The first is that step changes are modeled rather than trended: a migration completing, a launch landing, a commitment expiring, and a data centre shutting down are all events with dates, and a trend line drawn through them is wrong in a way that gets worse the further out it goes. The second is that the method's accuracy is measured. A forecast whose prior error nobody has computed carries an unstated confidence that the reader supplies themselves, and they are generally more confident than the record supports.

## Use when

- A spend projection is needed for a plan, a commitment decision, a hiring case, a renewal, or a board cycle.
- Actuals have diverged from budget and the variance needs attributing to a real cause rather than to a service name.
- Commitment drawdown against a contracted spend floor needs tracking, especially where a shortfall true-up is possible.
- A prior forecast missed and the method needs revisiting rather than the number being re-anchored.
- Known step changes such as migrations, launches, decommissions, or expiries need incorporating into a projection that currently smooths them.
- Forecast accuracy has never been measured and somebody is about to make a purchase decision on the strength of the projection.
- A range or a confidence statement is being asked for and needs a method behind it.

## Do not use when

- The question is what the plan should be rather than what spend will actually do: that is `budget-planning-desk`. A budget is accepted by a holder; a forecast is an estimate of reality.
- A specific charge spiked and needs a cause traced to a change: that is `anomaly-detection-desk`. Variance attribution works at plan-line granularity; anomaly root cause works at resource and change granularity.
- The question is which commitments to buy and at what quantity: that is `commitment-portfolio-desk`, which this desk feeds with the trajectory and the confidence behind it.
- The historical series is unreconciled or its period states are unknown: that is `cost-data-ingestion-desk`, and a forecast built on months that were still open inherits the lag as a trend.
- The variance is caused by an allocation method change rather than by spend: that is `shared-cost-allocation-desk` or `cost-allocation-tagging-desk`, and this desk names it as an allocation variance rather than a consumption one.
- The forecast is being used to negotiate with a provider: that is `cloud-commercial-negotiation-desk`.

## Required evidence

- The historical cost series with every period marked complete, partial, or restated, at the granularity the forecast needs.
- The budget with its lines, its bases, and its step change components.
- The drivers with their sources, where a driver-based method is available.
- Known step changes: migrations, launches, decommissions, renewals, expiries, and contract changes with their dates and sponsors.
- The commitment agreements with commit amounts, term dates, eligible spend definitions, and true-up mechanics as written.
- Drawdown to date against each commitment, from the provider's own reporting where it exists.
- Prior forecasts with their actuals, so error can be measured rather than asserted.
- The horizon the decision needs, since a purchase decision and a quarterly plan need different horizons and different confidence.

## Workflow

**Outcome.** A forecast with its method and the reason that method suits this spend profile, projections across the needed horizon with a range and the specific uncertainties that produce it, step changes modeled as dated events with their amounts, measured accuracy against prior actuals with the error method stated, variance attribution assigning each material gap to consumption, rate, allocation change, or timing with an amount for each, and the commitment trajectory showing drawdown against the contracted floor with the shortfall or overage quantified and the date it becomes unavoidable.

**Grounding.** The historical series comes from the reconciled dataset with period states attached. The commitment terms come from the executed agreement rather than from the provider console, because only the agreement says what happens when the commitment is missed and what spend counts toward it. Drawdown comes from provider reporting checked against the agreement's eligible spend definition, since the two routinely differ on marketplace and third-party charges.

**Constraints.** Partial periods are excluded from the fitted series or explicitly adjusted for their lag with the adjustment stated, because including an incomplete month teaches the model that spend is falling. A closed period that has since been restated is re-pulled rather than carried. Step changes are modeled as dated events with their own amounts and are visible as separate lines in the projection, never smoothed into a growth rate. The method is stated and matched to the profile: run rate suits stable estates, driver-based suits spend that tracks a measurable business volume, seasonal suits estates with a demonstrated cycle, and bottom-up suits a small number of large planned items. Accuracy is measured with the error method named and computed against actuals, and where no prior forecast exists that is stated rather than filled with a default confidence. A range is produced only where the method produces one, and its width is explained by named uncertainties rather than chosen to look prudent. Variance attribution distinguishes a consumption change from a rate change from an allocation change from a timing difference, because those four have different owners and only the first is usually anybody's fault. Commitment shortfall is quantified against the agreement's true-up mechanics with the last date action can still change the outcome.

**Parallel surface.** Accounts, services, product lines, individual budget lines, separate commitment instruments, and per-line variance attribution are independent units and fan out, as does connector preflight across the cost series, the budget, the agreements, and the drawdown reporting.

The aggregate is a single pass after the fan-out returns. The forecast rollup is a whole-set figure, since projecting each line independently and summing produces a total whose range is wrong in both directions: correlated drivers make the true range wider and independent noise makes the naive sum's range narrower. Commitment drawdown is measured against eligible spend across the whole footprint, so a per-team view of coverage is meaningless. Total variance against total budget has to reconcile to the sum of the attributed components, and the residual is the honest measure of how much of the movement is understood.

**Acceptance bar.** The forecast states its method, its horizon, its step changes with dates, and its measured prior error; every material variance carries an attributed cause with an amount; and the commitment position states drawdown, required run rate, and the projected shortfall or overage with the date beyond which it cannot be changed.

## Outputs

A complete run delivers this artifact set:

- `spend-forecast.md`: method with its rationale, projections by period with amounts and ranges, the drivers and their sources where driver-based, and the horizon with the decision it serves.
- `forecast-step-changes.md`: each migration, launch, decommission, renewal, or expiry as a dated event with its amount, its sponsor, and its confidence basis, shown separately from the underlying trend.
- `forecast-accuracy.md`: measured error against prior actuals with the error method named, per period and in aggregate, and the specific periods where the method broke down with the reason.
- `budget-variance-analysis.md`: variance per budget line with the amount attributed to consumption, rate, allocation change, and timing, plus the residual left unattributed at its real size.
- `commitment-trajectory.md`: per agreement, the commit amount, term dates, consumed to date, required run rate to meet it, projected position with its figure, the true-up exposure as the agreement writes it, and the last date action can still change the outcome.
- `forecast-assumptions.md`: every assumption the projection rests on, with the figure it moves and the size of that effect where it can be quantified.

Depth standard per artifact: a projection gives amounts by period rather than a growth rate. A step change gives its date, its amount, and who is accountable for it landing. An accuracy entry gives the computed error, not a characterization of it. A variance entry gives an amount per cause, so "of the eighty-thousand overrun, sixty is consumption growth in the ingestion pipeline, fifteen is the expiry of a commitment on the third, and five is unattributed" rather than a paragraph about pressures. A commitment entry gives the required run rate, because that single number is what makes a shortfall actionable.

In `diagnostic` mode, when the historical series, the agreements, or the drawdown reporting exists and cannot be read, the run delivers `forecast-connector-diagnostic.md` naming what was attempted and which projections and commitment positions the gap makes unavailable. A drawdown position is not estimated from spend that has not been checked against the eligible spend definition.

The failure this desk has to police is the manufactured range. A projection with a plus-or-minus band reads as rigorous, and a band chosen because it looks appropriately humble is decoration on an unmeasured estimate. It is worse than a point estimate, because a decision-maker treats the band as a bound and sizes a commitment against its lower edge. A range is produced only where the method produces one, and where the method does not, the projection is a point figure with its assumptions listed and no band at all. Prior accuracy gets the same treatment: where no prior forecast has been measured against actuals, the artifact says accuracy is unmeasured and names the periods that would need to be compared, because an invented error percentage is the one number in this desk's output that makes every other number look more trustworthy than it is.

## finops_packet fields to update

- `forecast.method`, `forecast.drivers`, `forecast.horizon`, `forecast.projection[]` with `period`, `amount`, `range`, and `confidence_basis`.
- `forecast.known_step_changes` with dates and amounts.
- `forecast.accuracy` with `prior_period_error` and the `method` used to measure it, or an explicit unmeasured state.
- `forecast.commitment_trajectory` with `agreement_ref`, `commit_amount`, `term_end`, `consumed_to_date`, `required_run_rate`, and `projected_position`.
- `budgets[].variance_amount` and `budgets[].variance_drivers` with the attributed cause per component.
- `commercial.agreements[].consumed_pct` and `shortfall_exposure` where the trajectory establishes them.
- `source_facts[]` with `locator` and `as_of`, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Release integrity: a forecast would go to finance, leadership, a board, or a vendor built on periods that were still open, on a series containing an unflagged partial month, or on a method whose prior accuracy is unmeasured and unmentioned. This is the defining halt for this stage, because a forecast becomes a commitment the moment somebody plans against it and the practice inherits the gap.
- Source conflict: the provider's drawdown reporting and the agreement's eligible spend definition give materially different consumed positions, or the budget and the ledger disagree on actuals for a closed period. Record both readings with their locators.
- Missing approval: the forecast would be used as a budget of record, submitted externally, or presented as the basis for a commitment purchase, each of which raises the decision class beyond internal analysis.
- Production or destructive: the next action would purchase or modify a commitment to close a projected shortfall. Sizing the position is this desk's work; buying it is a gated act at `commitment-portfolio-desk`.
- Security or privacy: the forecast detail would expose unannounced launches, headcount plans, or contract terms to an audience that should not have them.
- Connector unreachable: the historical series, the agreements, or the drawdown reporting cannot be read. State whether the source was empty or unreachable, since a drawdown query returning nothing and a reporting endpoint being down mean opposite things about a shortfall.

An unconfirmed step change date, a driver whose owner has not validated it, or an unattributed residual below the materiality threshold is a soft gap: proceed with it labeled against the projection line it affects.

## Downstream handoffs

`anomaly-detection-desk` receives every variance component that could not be attributed, with its amount and period, as triage input. `commitment-portfolio-desk` needs the forecast, its confidence basis, its measured accuracy, and the step changes, because a commitment is sized against projected post-optimization usage and its downside case is computed from the forecast's low end. `budget-planning-desk` receives the accuracy record so the next planning cycle knows how much the method has historically missed by. `cloud-commercial-negotiation-desk` needs the trajectory and the shortfall exposure, which is the single most load-bearing figure in a renewal conversation. `optimization-backlog-desk` needs the forecast to size what a savings target has to deliver.

## Quality bar

A method chosen for a reason that is written down. Step changes visible as dated events rather than absorbed into a slope. Accuracy measured or declared unmeasured, never implied. Variance attributed to consumption, rate, allocation, or timing with amounts, and an honest unattributed residual. A commitment position that names the required run rate and the last date anybody can act on it, which is the difference between a shortfall somebody can fix and a true-up that arrives as a surprise.
