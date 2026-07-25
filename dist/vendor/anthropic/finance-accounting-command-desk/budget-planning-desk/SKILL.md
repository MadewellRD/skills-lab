---
name: budget-planning-desk
description: build the annual operating plan by department and account with a named budget holder on every line, the driver and headcount model with start date timing and fully loaded cost, committed contractual spend separated from discretionary spend, the revenue build with its coverage basis, and the reconciliation between the bottom-up departmental build and any top-down target. use for annual planning, departmental budgets, headcount and hiring plans, driver models, cost center ownership, capex and opex planning, budget versions, and plan approval packages.
---

# Budget Planning Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it runs after `saas-metrics-reporting-desk`, because the revenue build starts from retention and expansion rates that mean nothing until their cohort and window are settled. Inside a workflow, produce the plan artifacts, update `finance_packet`, and continue into `forecast-scenario-desk`, which reforecasts against the plan built here. `references/stage-contracts.md` states what each later stage inherits, and `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary that stops this desk short of approving a plan.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would set a budget of record or commit spending authority, confidential information would be exposed, sources genuinely disagree on a load-bearing figure, a plan would leave the company without its basis, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the department, line, or driver it affects.

Never invent a budget holder, a headcount requisition, a start date, a salary, a contractual commitment, a renewal date, a driver value, or an approval. A line nobody has accepted is recorded as unowned rather than assigned to the department it looks like it belongs to, and a compensation figure that no offer, payroll record, or approved band supports is a placeholder labeled as one.

## Role

Own the operating plan and the model underneath it. That means the plan by department and by account with a named holder on every line who has actually accepted it; the driver model showing which operational assumptions move which financial lines and where each driver value came from; headcount as the largest and most timing-sensitive item, modeled by start date and fully loaded cost rather than annualized; contractual commitments separated from discretionary spend so a reduction conversation has somewhere to begin; the revenue build with the coverage behind it; the assumption register naming what each line depends on and what would break it; the reconciliation between the bottom-up departmental build and any top-down target, with the gap owned rather than spread; and the accuracy of the prior plan measured to calibrate this one.

The property that distinguishes a plan from a model is acceptance. A plan is a set of commitments by named people who will be asked about them every month for a year, and a beautifully constructed model that no department head has agreed to is a spreadsheet that will lose its first argument.

## Use when

- The annual operating plan or a new budget version is being built, rebuilt, or re-cut after a target change.
- Departmental budgets need assembling, owners need assigning, or a cost center has no holder.
- A headcount plan is needed, or the existing one annualizes hires and hides the timing lever.
- A driver model is needed to connect operational assumptions to financial lines.
- Committed spend needs separating from discretionary spend ahead of a reduction or a reallocation.
- A bottom-up build and a top-down target disagree and the gap needs owning.
- The plan is going to the executive team or the board for approval and needs its assumptions and its accuracy history attached.

## Do not use when

- The period is already underway and the question is the updated outlook rather than the plan: `forecast-scenario-desk`.
- The plan exists and actuals have come in against it: `variance-analysis-desk`.
- A specific commitment needs an approver under the delegation of authority: `spend-approval-authority-desk`.
- The constraint is cash rather than plan: `cash-flow-treasury-desk` sets the envelope the plan has to fit inside.
- Retention and expansion rates themselves are in question rather than being consumed: `saas-metrics-reporting-desk`.
- The question is which account or cost center a cost belongs in: `accounting-policy-coa-desk`.
- The plan is fine and the spend is out of policy: `expense-management-desk`.

## Required evidence

- Closed actuals for the baseline period with their period status, at the department and account granularity the plan will use.
- The current headcount roster with roles, departments, and cost, plus open requisitions with their approval state.
- Compensation bands or offer data for planned roles, employer tax and benefit loading rates, and the equipment and software cost per head.
- Contractual commitments already in force: leases, multi-year software agreements, service contracts, and their renewal dates, auto-renewal provisions, and notice periods.
- The revenue drivers and the coverage behind them, including retention and expansion rates with their cohorts, pipeline or contract coverage, quota capacity, and ramp assumptions for new sellers.
- The departmental input from each budget holder and the record of what each one accepted.
- Any top-down target and where it came from, including board expectations or guidance already communicated.
- The planning calendar with submission and approval dates, the prior plan, and the actual outcome against it.
- The cash envelope and any funding constraint from the treasury stage.

## Workflow

**Outcome.** A plan an executive team can approve and a department head can be measured against: every line carrying an account, a department, a holder who accepted it, and the basis it was built on; headcount timed by start date with fully loaded cost; committed and discretionary spend separated; a revenue build whose coverage is stated; drivers with sources and sensitivities; an assumption register naming what breaks each line; a reconciliation between the bottom-up build and the target with the gap explicitly owned; and prior plan accuracy measured.

**Grounding.** Closed actuals establish the baseline, and a baseline built on a period that is still open is a baseline that will move. Executed agreements establish committed cost, including the renewal and notice terms that determine whether a commitment is actually reducible in the plan year. Payroll records and approved compensation bands establish personnel cost, and the loading rate is a computed figure rather than a convention. Departmental input establishes ownership only where the holder accepted it, so an input that was assembled on a holder's behalf is labeled as such.

**Constraints.**

- Every line has a named holder who accepted it. A line with a department label and no person behind it is unowned, and it is listed as unowned rather than assigned by inference from the cost center.
- Headcount is modeled by start date. A role starting late in the year costs a fraction of its annual rate in the plan year and its full rate in the next one, so annualizing hires overstates the plan year and understates the exit run rate, which is the figure the next plan starts from.
- Personnel cost is fully loaded and the loading is shown: base, employer taxes, benefits, and the per-head equipment and software cost that scales with the roster.
- Committed cost is separated from discretionary cost, with the contractual term and the notice period stated for each commitment. A cost that cannot be reduced this year is a fact about the agreement, not about the department's willingness.
- Every driver has a source and a sensitivity. A driver value carried forward because it was last year's is labeled as carried forward, and the plan states which drivers actually move the outcome.
- The revenue build states its coverage: how much of the plan is already contracted, how much depends on retention at a stated rate, and how much requires new business that does not yet exist.
- The gap between a bottom-up build and a top-down target is stated at its full amount and owned by a named decision. Spreading it proportionally across departments creates a plan every holder knows is unreachable, and the first variance conversation is about the allocation rather than about the spending.
- Prior plan accuracy is measured and stated, because a planning process that has never looked at its own error repeats it.

The approval chain is mandated: departmental submission by the accepting holder, consolidation and reconciliation to the target, executive review, board approval where the company has one, and only then loading as the budget of record and deriving spending authority from it. The order is mandated because the approved budget is what the delegation of authority matrix reads to decide who may commit what, so a plan loaded before it is approved lets commitments be made against authority that does not yet exist, and those commitments are contractual and are not undone by revising the plan afterwards.

**Parallel surface.** Independent items fan out: departments building their own submissions, individual cost lines under review, separate driver models, contract-by-contract commitment extraction, and role-by-role headcount costing each stand on their own inputs. Three passes are aggregate and run once after the fan-out returns. The consolidated plan is reconciled to the target as a whole, because the gap is a property of the total and cannot be assessed department by department. Total headcount and its cost are checked against the exit run rate in one pass, since each department's timing looks reasonable in isolation and the aggregate ending run rate is what next year inherits. And the plan is tested against the cash envelope as a whole, because a plan that each department can afford and the company cannot is the failure this check exists to catch.

**Acceptance bar.** Every plan line names its account, department, holder, and basis. Every headcount line names the role, department, start month, and fully loaded cost with the loading shown. Every commitment names its agreement, its term, and its notice period. Every driver names its source and its value. The bottom-up to top-down reconciliation shows the gap at its full amount with the decision that closes it named. Unowned lines are listed as unowned. Prior plan accuracy is stated as a measured figure with its method.

## Outputs

A complete run delivers the set:

- `operating-plan.md`: the plan by department and account for each period of the horizon, with the holder, the basis, and the committed against discretionary classification on every line.
- `headcount-plan.md`: role, department, start month, fully loaded cost with its components, backfill against new position, requisition approval state, and the ending run rate the plan exits with.
- `driver-model.md`: each operational driver, its source, its value, the financial lines it moves, and the sensitivity of the plan to it.
- `revenue-build.md`: the revenue plan with contracted, retention-dependent, and new business components separated, the rates applied with their cohorts, and the coverage ratio behind the new business assumption.
- `committed-cost-register.md`: every contractual commitment with its counterparty, amount, term, renewal date, notice period, and whether it is reducible within the plan year.
- `assumption-register.md`: what each material line depends on, what would break it, and which assumptions the plan is most sensitive to.
- `plan-reconciliation.md`: the bottom-up build against the top-down target, the gap at its full amount, the options that would close it, and the decision required with its owner.
- `plan-accuracy-review.md`: the prior plan against actuals by department, the error measured, and the systematic bias where one exists.
- `budget-planning-downstream-handoff.md`: what `forecast-scenario-desk`, `variance-analysis-desk`, and `spend-approval-authority-desk` inherit, with unowned lines and unresolved gaps named.

Depth standard: an artifact is complete when a department head reads their section and either accepts it or disputes a specific line. A plan line reads as the account, the amount by period, the driver or contract behind it, and the holder. A headcount line reads as the role, its start month, and its loaded cost build. A commitment reads as the agreement, the notice date, and what happens if that date passes.

Where the run covers one department or one component rather than the full plan, scope the artifacts and say so rather than presenting a partial build as the plan. Where the ledger, the payroll system, the contract repository, or the departmental inputs cannot be reached, `budget-planning-diagnostic.md` names what was attempted, what returned, and which parts of the plan cannot be built as a result.

The hazard specific to this desk is that the fabrication that matters here is not a number, it is a person. A plan reads as complete the moment every line has a name against it, and a name is the easiest field in the whole artifact to fill from an org chart. A holder who has never seen the line will not defend it, will not manage to it, and will correctly say so in the first variance review, at which point the plan loses authority for every line including the ones that were agreed. Lines are marked accepted only where the holder accepted them, provisional where finance built them on the holder's behalf, and unowned where no holder exists. The same rule governs headcount: a start date is a hiring commitment with a requisition behind it, or it is a placeholder date labeled as one, because a plan whose hiring dates were chosen to make the annual total land on the target is a cost curve nobody is managing to.

## finance_packet fields to update

- `plan.budget_version` with its identifier and `plan.approval_state`.
- `plan.drivers[]` with each driver's source and value; `plan.headcount_plan[]` with role, department, start date, and fully loaded cost basis; `plan.departments[]` with cost center, owner, and approved amount.
- `plan.assumptions_register[]` with what each line depends on and what breaks it.
- `approvals[]` for the plan itself and for any commitment the plan assumes, with `amount_at_stake`, `required_approver`, and `authority_basis`.
- `source_facts` with the actuals, agreements, payroll records, and departmental inputs read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: setting or changing the budget of record. The approved plan confers spending authority for the year and becomes the number every department is measured against, so it belongs to the executive team and, where one exists, the board. A plan quietly adopted by finance is a target nobody agreed to defend.
- **Production or destructive**: the next act would load the plan into the ledger or planning system, replace an approved version, or open requisitions against it.
- **Security or privacy**: the artifact would carry individual salary or compensation detail by name rather than by role and band, or would expose an individual's offer or performance information through a headcount line.
- **Source conflict**: the actuals baseline, the headcount roster, and the payroll system disagree; a commitment appears in the plan with different terms than the agreement states; or two versions of the target are in circulation with different numbers.
- **Release integrity**: a plan would go to the board or into a financing process without its assumptions, its coverage basis, and the gap between the build and the target stated.
- **Connector unreachable**: the ledger, the payroll system, the contract repository, or the planning system exists and cannot be read, so a plan would be built over a baseline that was never examined.

A department that has not returned its submission, a role whose compensation band is not yet set, a renewal whose terms are still being negotiated, and a driver whose source is disputed are soft gaps. Build the line on the best available basis, label the assumption against that department or line, and record the question.

## Downstream handoffs

`forecast-scenario-desk` takes the plan as the baseline it reforecasts against, along with the drivers and the assumption register, because a scenario is a change to a named assumption rather than to the total. `variance-analysis-desk` takes the plan version identifier, the departmental structure, and the holder per line, since a variance without a named holder has no action attached to it. `spend-approval-authority-desk` takes the approved budget lines and their remaining headroom, which is what a commitment is checked against. `cash-flow-treasury-desk` takes the timing of planned hiring and committed spend for the disbursement forecast. `internal-controls-desk` takes any commitment found in force with no approval behind it.

## Quality bar

A good plan is one the department heads argue about before it is approved rather than after. Every line has a person, every hire has a month, every commitment has a notice date, and the gap between what the business built and what the board wants is on the page rather than distributed quietly into travel and software. The headcount model is the tell: a plan that annualizes hires is a plan nobody intends to manage monthly. And the accuracy review is what makes the next plan credible, because a planning function that names its own bias is one whose numbers get believed when they are inconvenient.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
