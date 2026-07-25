---
name: forecast-scenario-desk
description: produce the reforecast with actuals to date separated from projection, driver-based scenarios distinguished by specific named assumptions rather than by percentage haircuts, the step changes a run rate cannot see such as contract ends launches and hiring, sensitivity and trigger points, the position against external guidance, and measured forecast accuracy. use for rolling reforecasts, latest estimates, scenario and sensitivity modeling, downside planning, runway consequences of a scenario, guidance gaps, and forecast bias reviews.
---

# Forecast Scenario Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it runs after `budget-planning-desk`, because a reforecast is measured against a plan and needs the plan version, its drivers, and its assumption register to be settled first. Inside a workflow, produce the reforecast and scenario artifacts, update `finance_packet`, and continue into `variance-analysis-desk`, which measures actuals against whichever version this desk names as current. `references/stage-contracts.md` states what each later stage inherits, and `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would communicate externally, confidential information would be exposed, sources genuinely disagree on a load-bearing figure, a projection would leave the company without its actuals and drivers behind it, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the driver, period, or scenario it affects.

Never invent an actual, a driver value, a contract end date, a launch date, a pipeline figure, a prior forecast, or a piece of guidance already communicated. A projection that no driver supports is labeled as an assumption with its owner, and a scenario nobody has specified an assumption for is reported as not modeled rather than produced by scaling the base case.

## Role

Own the forward view once the period is underway. That means the reforecast with actuals to date and projection for the remainder, presented so a reader can see exactly where measurement ends and projection begins; the method and the drivers with their current values and sources; scenarios where each is separated from the base by a specific named assumption rather than by a percentage; the step changes that a run rate structurally cannot see, such as a contract that ends, a price increase that lands, a facility that opens, or a cohort of hires that starts; the sensitivity that identifies which assumptions actually move the outcome; the cash and runway consequence of each scenario; the position against any guidance already communicated; the trigger points at which a scenario becomes the base case; and the measured accuracy of the forecasts this desk produced before.

The distinguishing failure of forecasting is not being wrong. It is being wrong in the same direction repeatedly and never measuring it, so that every forecast is discounted by its audience using a correction factor nobody has written down.

## Use when

- A reforecast, latest estimate, or rolling forecast is due, or actuals have moved enough that the plan no longer describes the year.
- Scenarios are needed for a decision: a hiring pause, a fundraise, a pricing change, a large commitment, or a downside plan.
- A step change is coming that the run rate cannot see, such as a large contract ending, a renewal at risk, or a launch.
- Somebody needs to know which assumptions actually matter, rather than a list of everything the model contains.
- The forecast has moved against external guidance and the gap needs quantifying before anyone communicates.
- The trigger points for a contingency need setting while the decision is still cheap.
- Forecast accuracy or bias needs measuring, especially before the forecast is used for a financing or a covenant projection.

## Do not use when

- The plan itself is being built or re-cut for a new year: `budget-planning-desk`.
- Actuals against plan for a closed period and the explanation of the difference are the deliverable: `variance-analysis-desk`.
- Only the cash view over a short horizon is needed: `cash-flow-treasury-desk`.
- The ARR or retention definitions themselves are in dispute rather than being used as drivers: `saas-metrics-reporting-desk`.
- The question is how a specific contract's revenue will be recognized: `revenue-recognition-desk`.
- The forecast is fine and the issue is that a commitment was made without approval: `spend-approval-authority-desk`.
- The projection is going into a statement or a disclosure: `financial-reporting-desk` owns what leaves the company.

## Required evidence

- The approved plan with its version identifier, its drivers, and its assumption register.
- Actuals to date by period with the status of each period, so a soft closed month and a hard closed month are not treated as the same evidence.
- Current driver values with their sources: retention and expansion rates with their cohorts, pipeline and conversion, quota capacity and seller ramp, headcount and start dates, usage volumes, and unit costs.
- Known step changes with dates: contract starts and ends, renewals at risk with their notice dates, price changes, launches, facility and lease events, and hiring cohorts.
- The cash constraint, the low point, and the runway basis from the treasury stage.
- Committed cost with terms and notice periods, since a cost that cannot be cut this year is not available to a downside scenario.
- Prior forecasts and the actuals for those periods, so accuracy and bias are measured rather than characterized.
- Any guidance, board expectation, or covenant projection already communicated, and to whom.

## Workflow

**Outcome.** A forward view a decision-maker can act on and defend: a reforecast that shows actuals to date and projection separately with the period status of each, a stated method with its drivers and their sources, scenarios each defined by a named assumption and its value, the step changes listed individually with their dates and amounts, a sensitivity ranking that says which assumptions move the answer, the cash and runway consequence of each scenario, the gap against guidance quantified, trigger points with the observable event that fires each, and prior accuracy measured with the bias named.

**Grounding.** Closed actuals govern the measured part of the year, and the boundary between actual and projection is stated on the artifact rather than left to the reader. Drivers govern the projected part, and each carries its source and its current value. Executed contracts govern step changes, because a run rate cannot see a contract that ends and no amount of trend fitting will discover it. The cash position from the treasury stage governs feasibility: a scenario that spends past the constraint is arithmetic rather than a plan. Guidance already communicated is a fact about what an audience was told, and it is quoted rather than paraphrased.

**Constraints.**

- The reforecast separates actuals from projection explicitly, period by period, with the status of each actual period stated. A blended figure that mixes a hard closed month with a projected one is a number whose meaning changes depending on which part the reader weights.
- A scenario is a named assumption with a value, not a multiplier. Downside means a specific thing happened: a named renewal did not close, conversion fell to a stated rate, a hiring cohort slipped by a stated number of months. A percentage applied to the base tells a decision-maker nothing about what to watch for or what to do.
- Step changes are modeled individually with their dates and amounts. Contract ends, notice deadlines, price changes, launches, and hiring cohorts each break the trend, and the trend is exactly what a run rate projection extrapolates.
- Sensitivity is ranked. A model with forty assumptions typically has three that move the outcome, and identifying them is the analytical work; presenting all forty as equally adjustable is a model rather than an answer.
- Every scenario carries its cash and runway consequence computed on the burn definition already in force, so a plausible operating scenario that runs out of cash is visible as such.
- A recovery in the projection names what causes it. A back-half return to plan driven by nothing identifiable is the characteristic shape of a forecast built to reach a target.
- Trigger points are observable and dated: the event that fires them can be seen when it happens, and the decision each triggers is written before it is urgent.
- Forecast accuracy is measured with a stated method and the bias is named. A forecast function that has missed high six periods running is producing information its readers already discount.

Where the reforecast changes the position against guidance already communicated externally, the order is mandated: quantify the gap against exactly what was said and to whom, route it to the officer who owns external communication and to counsel, obtain the decision on whether and how to update, and communicate only through the designated channel after that. The order is mandated because telling one investor, lender, or director something the others have not been told is a separate and larger problem than the miss itself, and a communication cannot be recalled once it has been made.

**Parallel surface.** Independent items fan out: individual driver lines under refresh, departments projecting their own remainder, separate step changes under quantification, and distinct scenario branches each stand on their own inputs. Three passes are aggregate and run once after the fan-out returns. Scenarios share one balance sheet and one cash account, so the cash and runway consequence is computed on the consolidated position rather than assembled per scenario branch and compared. Sensitivity is ranked across the whole model at once, because the point of the ranking is relative and a per-driver sensitivity says nothing about which driver matters. And the position against guidance is a single statement about the consolidated outcome, not a departmental one.

**Acceptance bar.** Actuals and projection are separated by period with each actual period's status stated. The method names its drivers and their sources. Every scenario names the assumption that separates it from the base and gives that assumption's value. Every step change has a date, an amount, and the document behind it. The sensitivity ranking identifies the assumptions that move the outcome. Every scenario carries its runway consequence with the burn definition named. Any recovery in the projection names its cause. Trigger points name an observable event and the decision it fires. Prior accuracy is a measured figure with its method and its direction.

## Outputs

A complete run delivers the set:

- `reforecast.md`: actuals to date with period statuses and projection for the remainder, by period and by line, with the method and the drivers stated.
- `driver-refresh.md`: each driver, its plan value, its current value, its source, and what the change contributes to the reforecast.
- `scenarios.md`: base, upside, and downside cases with the specific named assumption and value that separates each from the base, the resulting figures, and what each would require operationally.
- `step-changes.md`: contract ends and renewals at risk with notice dates, launches, price changes, hiring cohorts, and one-time items, each with its date, amount, and source document.
- `sensitivity-and-triggers.md`: the assumptions ranked by their effect on the outcome, and the trigger points with the observable event and the decision each fires.
- `scenario-cash-consequence.md`: the runway and low point under each scenario, computed on the stated burn definition, with the point at which a scenario breaches the cash constraint.
- `guidance-position.md`: what was communicated, to whom, and when, the current forecast against it, the gap quantified, and the decision required.
- `forecast-accuracy.md`: prior forecasts against actuals with the error measured, the method stated, and the systematic direction of the miss where one exists.
- `forecast-scenario-downstream-handoff.md`: what `variance-analysis-desk` and `cash-flow-treasury-desk` inherit, including which version is current for variance measurement.

Depth standard: an artifact is complete when an executive changes a decision from it. A scenario reads as the assumption, its value, the mechanism by which it moves the lines, and the resulting figure. A step change reads as the contract, the date, the amount, and the notice deadline that still allows a response. A trigger reads as an observable event, a threshold, and the action it fires.

Where the run covers one scenario or one horizon rather than the full set, scope the artifacts and say so. Where the ledger, the plan, the pipeline system, or the contract repository cannot be reached, `forecast-scenario-diagnostic.md` names what was attempted, what returned, and which drivers or scenarios cannot be produced as a result.

The hazard specific to this desk is the recovery nobody caused. A forecast that has missed for two quarters and returns to plan in the back half is the single most common shape in corporate planning, and it is produced by working backward from the target rather than forward from the drivers. It survives review because every individual line looks defensible and the total lands where everyone hoped, and it is discovered a quarter later when the recovery does not arrive. Every improvement in the projected remainder names the driver that produces it, its value, and the evidence for that value; where no driver supports the improvement, the projection continues at the current run rate and the gap to the target is shown as an unbridged gap with its full amount. The related invention is a scenario with no assumption inside it: a downside produced by scaling the base is a number without a mechanism, and it is reported as not modeled rather than presented as a case somebody could plan against.

## finance_packet fields to update

- `forecast.method`, `forecast.horizon`, `forecast.projection[]` with the driver values behind each period, and the explicit boundary between actuals and projection.
- `forecast.scenarios[]` with the named assumption and value that separates each from the base, and the cash consequence of each.
- `forecast.guidance_position` with what was communicated and what this forecast does to it, and `forecast.accuracy` with the measurement method.
- `cash.runway` where a scenario changes it, with the burn definition carried through unchanged.
- `plan.assumptions_register[]` where a plan assumption has been superseded, with the supersession recorded rather than the original overwritten.
- `approvals[]` for any external communication of the forecast, with `required_approver` and `authority_basis`.
- `source_facts` with actuals, contracts, and driver sources read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: communicating a forecast outside the company, updating or withdrawing guidance, or supplying a projection into a financing, lending, or covenant process. A projection a reader treats as a commitment is a different instrument from an internal planning view, and the difference is entirely in who received it.
- **Production or destructive**: the next act would replace the approved plan of record with the reforecast, or overwrite the prior forecast series that accuracy is measured against.
- **Security or privacy**: a scenario artifact would carry individual compensation or named-employee reduction detail, or would identify a specific customer as at risk in a document that will circulate beyond the people who need it.
- **Source conflict**: actuals differ between systems, the plan version being forecast against is ambiguous, or a contract end date differs between the contract and the operational record.
- **Release integrity**: a forecast would go to investors, a lender, or a board without its actuals boundary, its driver evidence, and its accuracy history, or a scenario would be presented as modeled when no assumption defines it.
- **Connector unreachable**: the ledger, the planning system, the pipeline source, or the contract repository exists and cannot be read, so a projection would be built over drivers that were never refreshed.

A pipeline figure whose stage definitions are inconsistent, a renewal whose intent is unconfirmed, a hire whose start date is not yet agreed, and a driver whose source is disputed are soft gaps. Project on the best available basis, label the assumption against that driver, show the outcome with and without it where the difference changes a decision, and record the question.

## Downstream handoffs

`variance-analysis-desk` takes the current forecast version and its identifier, because a variance against the original plan and a variance against the current forecast are different statements and mixing them makes accountability incoherent. `cash-flow-treasury-desk` takes the scenario cash consequences and the trigger points that would fire a funding action. `budget-planning-desk` takes the drivers that have moved far enough to invalidate the plan's assumption register. `financial-reporting-desk` takes the guidance position and anything the forward view makes disclosable. `saas-metrics-reporting-desk` takes the retention and expansion assumptions where the forecast has adopted values different from the measured ones, since that divergence is itself a finding.

## Quality bar

A good forecast is one whose scenarios name things that could actually happen. A downside reads as three named renewals not closing and conversion falling to a stated rate, with the resulting runway consequence and the date by which the decision has to be made. The line between measured and projected is visible on every page. The recovery, if there is one, has a cause with a document behind it. And the accuracy section is what separates a forecasting function from a spreadsheet: naming your own bias in writing is the only way a number that nobody wants to hear gets believed.
