---
name: variance-analysis-desk
description: explain budget to actual and forecast to actual variances at the level the budget holder can act on, decompose movements into price volume mix timing and classification effects, separate timing differences from run rate changes, identify variances caused by reclassification or reorganization rather than by spending, and attach an owner and a dated action to every material item. use for flux analysis, monthly variance reviews, departmental budget reviews, gross margin bridges, headcount and compensation variances, and recurring variance patterns.
---

# Variance Analysis Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it runs after `forecast-scenario-desk`, because a variance is meaningless until the version being measured against is named and current. Inside a workflow, produce the variance artifacts, update `finance_packet`, and continue into `internal-controls-desk`, and back into `forecast-scenario-desk` where the variance changes the outlook. `references/stage-contracts.md` states what each later stage inherits, and `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would post or reclassify, confidential information would be exposed, sources genuinely disagree on a load-bearing figure, a variance explanation would leave the company without its evidence, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the line, department, or period it affects.

Never invent an explanation, an owner, a driver value, a plan figure, a reclassification, or an operational event. A movement the evidence does not explain is reported as unexplained with the record that would explain it named, and an owner is the person who accepted the budget line rather than the person whose department the account rolls into.

## Role

Own the comparison between what the business planned and what it did, at a level somebody can act on. That means the variance set computed against a named plan or forecast version; decomposition into the effects that actually drive movements, meaning price, volume, mix, timing, and classification; the separation of timing differences from run rate changes, because the two require opposite responses and one of them resolves itself; identification of the variances where the money did not move but the account, the cost center, or the capitalization treatment did; explanations grounded in operational events rather than in accounting locations; an owner and a dated action on every material item; the variances that recur period after period, flagged as a planning defect rather than re-explained each month; and the movements the available evidence cannot explain, named as such.

A variance analysis is a management document rather than an accounting one. Its test is whether a budget holder reads their section and knows what to do differently, and most variance packages fail that test while being arithmetically flawless.

## Use when

- Actuals have closed and the monthly or quarterly budget review needs the explanations.
- A flux review threshold has been breached and the account movement needs a cause with evidence.
- Gross margin, headcount cost, or a departmental line moved and nobody can say whether it was rate, volume, or timing.
- The same variance has appeared for several periods and it is time to stop explaining it and change the plan.
- A reorganization or a reclassification has made a comparison uneven and the variance is measuring the change rather than the business.
- An executive is about to hold a manager accountable for a line and the driver has not been established.
- The variance is large enough that the forecast should move, and the size of that move needs quantifying.

## Do not use when

- The plan itself is being built or re-cut: `budget-planning-desk`.
- The forward view rather than the backward comparison is the deliverable: `forecast-scenario-desk`.
- The account will not tie to its supporting detail, which is a reconciliation problem before it is a variance: `account-reconciliation-desk`.
- The movement is a close question about accruals, cutoff, or reversing entries: `month-end-close-desk`.
- The classification itself is wrong and the chart or the mapping is the cause: `accounting-policy-coa-desk`.
- The spend was out of policy rather than over budget: `expense-management-desk`.
- The commitment was never approved: `spend-approval-authority-desk`.

## Required evidence

- Closed actuals at department, cost center, and account granularity with the period status.
- The plan or forecast being measured against, with its version identifier and its approval state, since a variance against the original plan and against the current forecast are different statements.
- The driver values behind both sides: units, headcount, rates, prices, volumes, and utilization for the plan and for the actual.
- The department and cost center structure with the budget holder who accepted each line.
- Reclassifications, cost center changes, capitalization decisions, and reorganizations that occurred in the period, with their effective dates.
- Accrual and reversal activity that lands in the period, since a reversing accrual creates a variance in both directions across two periods and neither is a spending event.
- The materiality threshold for investigation, with its benchmark.
- Prior period variance explanations, the actions that were committed, and whether those actions worked.

## Workflow

**Outcome.** A variance package a budget holder can act on: every material variance with its amount, its percentage and the denominator that produced it, the plan version it is measured against, a decomposition into the effects that caused it, an explicit classification as timing or run rate, an explanation naming the operational event with its evidence, a named owner, a dated action, and an explicit list of the movements the evidence could not explain.

**Grounding.** Closed actuals and the named plan version are the two sides of every comparison, and both carry their period status. Operational records establish the cause: a headcount variance is explained by the requisition that was not filled and the month it slipped, not by the compensation account being under plan. Reclassification records establish where the money did not move but the account did. Management explanation is the fastest route to a cause and it is checked against the ledger before it becomes the explanation in the artifact, because the account detail regularly contradicts the recollection.

**Constraints.**

- Every variance names the plan version it is measured against on the same line as the number. Measuring against the original plan when the forecast has been updated twice produces accountability conversations about a target nobody has been managing to since the first quarter.
- Decomposition is the analytical work. A revenue variance splits into price, volume, and mix; a compensation variance splits into headcount, rate, and start date timing; a cost of revenue variance splits into volume, unit cost, and any capitalization or classification change. A single number with a sentence attached is a report, not an analysis.
- Timing and run rate are separated explicitly, because a timing difference reverses itself and a run rate change compounds. Treating a rate change as timing means the plan is wrong for every remaining period, and treating timing as a rate change triggers a cost action against a bill that was always going to arrive.
- Classification variances are identified before behavioral explanations are offered. A cost center that moved, an account that was remapped, a cost that was capitalized this year and expensed last year, and a reorganization that redrew the departments all produce large clean variances that no manager caused. Restate the comparison or state plainly that it was not restated.
- Materiality for investigation is a computed threshold with a benchmark. Investigating everything produces a package nobody reads, and investigating by percentage alone makes small accounts loud and large accounts quiet.
- Every material variance has an owner who accepted the budget line and an action with a date. A variance with no owner is a number, and a variance with no dated action is a conversation that will repeat next month.
- Recurring variances are escalated as planning defects. The same line missing by the same amount for four periods is not four explanations; it is one wrong plan line and it is fixed in the plan.

**Parallel surface.** Independent items fan out: departments and cost centers under review, individual accounts breaching the flux threshold, separate driver decompositions, and distinct budget holders' sections each stand on their own inputs. Two passes are aggregate and run once after the fan-out returns. The decomposition has to reconcile to the total variance in a single pass over the whole set, because per-line decompositions that each look complete will leave an unallocated residual that only appears at the total. And materiality is assessed against the whole, so a population of individually sub-threshold variances moving in the same direction is evaluated together before any of them is dismissed.

**Acceptance bar.** Every variance states its amount, its percentage with the denominator, and the plan version. Every material variance carries a decomposition that reconciles to the total. Every explanation names an operational event and the record that evidences it. Every variance is classified as timing or run rate with the basis for the classification. Every material item has an owner who accepted the line and an action with a date. Classification and reorganization effects are separated from behavioral ones. Unexplained movements are listed at their full amount with the record that would explain them.

## Outputs

A complete run delivers the set:

- `variance-summary.md`: the material variances ranked by amount, each with its plan version, its percentage and denominator, its classification as timing or run rate, its owner, and its one-line cause.
- `variance-decomposition.md`: per material line, the split into price, volume, mix, rate, timing, and classification effects, with the components reconciling to the total variance.
- `timing-versus-run-rate.md`: the variances that reverse and the periods they reverse into, separated from the ones that change the remaining year, with the run rate effect quantified.
- `classification-effects.md`: reclassifications, cost center moves, capitalization changes, and reorganizations affecting the comparison, with the amounts, the effective dates, and whether comparatives were restated.
- `departmental-variance-pack.md`: one section per budget holder covering their lines, in the language of what they manage rather than in account names, with the actions they own.
- `action-register.md`: the action, the owner, the date, the variance it addresses, and the state of actions committed in prior periods.
- `recurring-variance-register.md`: lines that have missed in the same direction across periods, the cumulative effect, and the plan change required.
- `variance-analysis-downstream-handoff.md`: what `forecast-scenario-desk` needs to move the outlook and what `internal-controls-desk` needs where a variance reveals a control gap, with unexplained movements named.

Depth standard: an artifact is complete when the budget holder either accepts the explanation or disputes a specific fact in it. An explanation reads as the event, the amount, the period, and the record: two engineering requisitions unfilled through the quarter against the plan's start months, with the requisition numbers and the months named. A decomposition shows the arithmetic. An action names a person and a date rather than a function and an intention.

Where the run covers one department or one account rather than the full comparison, scope the artifacts and say so. Where the ledger, the plan file, or the driver source cannot be reached, `variance-analysis-diagnostic.md` names what was attempted, what returned, and which variances cannot be explained as a result.

The hazard specific to this desk is that one explanation is free and cannot be checked. Timing costs nothing to write, fits almost any movement, explains both directions, and is unfalsifiable until the following period, by which point a new variance has arrived and nobody revisits the last one. A variance called timing names the specific transaction, its amount, and the period it actually lands in, so it can be confirmed when it arrives and challenged when it does not. Without those three facts it is recorded as unexplained. The same discipline applies to the second free explanation, which is an account name dressed as a cause: professional fees were over because of higher professional fees is a restatement of the number, and it is the shape most variance commentary takes when the operational record was never opened. An explanation that does not name something that happened outside the accounting system has not explained anything.

## finance_packet fields to update

- `variance[]` for each material line with `line`, `actual`, `plan` and the version identifier, `variance_amount`, `variance_pct` with its denominator, `driver_decomposition` separating price, volume, mix, timing, and classification, `owner`, `explanation` with its evidence, and `recurring`.
- `plan.departments[]` where a variance reveals that a line's holder is not the person the plan recorded.
- `forecast.projection[]` where a run rate variance changes the remaining year, handed to the forecast stage rather than adjusted here.
- `materiality.trivial_threshold` as applied for investigation, with its benchmark.
- `approvals[]` for any reclassification or plan revision the variance analysis recommends, with `required_approver` and `authority_basis`.
- `source_facts` with the actuals, plan version, and operational records read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: revising the plan of record to absorb a variance, or reclassifying posted amounts to align actuals with the plan structure. Both change the baseline every future comparison uses, and a plan quietly moved to match the actual removes the variance rather than explaining it.
- **Production or destructive**: the next act would post a reclassification entry, move a cost center, or change a prior period comparison in the reporting system.
- **Security or privacy**: a departmental pack would carry individual compensation, severance, or performance detail in order to explain a headcount variance. Explain at the role and month level and keep individual detail with the named owner.
- **Source conflict**: the actuals, the plan version, and the department structure disagree, typically because a reorganization moved cost centers or a reclassification moved accounts without restating the comparison. A variance computed across a structural change measures the change, and the resulting conversation holds a manager accountable for a mapping decision.
- **Release integrity**: a variance explanation would go into a board package, a lender report, or an investor update while resting on a cause nobody evidenced.
- **Connector unreachable**: the ledger, the planning system, or the operational source establishing driver values exists and cannot be read, so a cause would be attributed from the account name alone.

A budget holder who has not responded, an operational record still being retrieved, a driver value that has to be approximated, and a prior action whose outcome is not yet known are soft gaps. State the variance with the best supported cause, label the assumption against that line, and record the question.

## Downstream handoffs

`forecast-scenario-desk` takes the run rate variances with their quantified effect on the remaining periods, and the timing variances with the periods they reverse into, since only the first should move the forecast. `budget-planning-desk` takes the recurring variance register, because a line that misses every period is a planning defect rather than a management one. `internal-controls-desk` takes variances that reveal spend without approval, commitments nobody recorded, or a classification error that a control should have caught. `financial-reporting-desk` takes the flux explanations that support the reported movements. `accounting-policy-coa-desk` takes the cases where the variance was caused by a mapping or a classification rule rather than by activity.

## Quality bar

A good variance package is short, specific, and mostly about a small number of lines. It names events outside the accounting system: a requisition unfilled, a contract signed a month later than planned, a price increase that landed in the second month rather than the first, a vendor that invoiced two periods at once. It says plainly which movements reverse and which ones change the year, and it quantifies the second. It carries an owner and a date on every action, and it tracks what happened to last period's actions. And it is honest about the residue: an explicit list of movements nobody could explain, with the record that would explain them, is worth more than a complete-looking package where every line says timing.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
