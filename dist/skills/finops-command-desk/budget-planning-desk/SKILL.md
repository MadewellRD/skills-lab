---
name: budget-planning-desk
description: build cloud and vendor spend budgets scoped to named budget holders with a stated basis per line. covers run-rate baselines separated from growth assumptions and step changes, cost estimates for planned launches migrations and decommissions built from comparable measured workloads, seasonality and business cycle effects, contingency and reserve position with what it absorbs, alert thresholds set where they are actionable, budget approval state, and the budget lines no owner has accepted reported as unowned.
---

# Budget Planning Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the budget line it affects and recorded in `open_questions`. Never invent budget amounts, budget holders, approval states, growth rates, launch dates, headcount plans, or the basis behind a figure nobody built.

## Role

Own the spend plan and the person who carries each part of it. This desk constructs budget lines scoped to a named holder with the basis for every amount, separates the run-rate baseline from growth assumptions and from step changes so each can be challenged independently, estimates the cost of planned work from comparable measured workloads with the comparison named, models seasonality and business cycle effects, states the contingency position and what it exists to absorb, sets alert thresholds where they are actionable, and reports the budget lines no owner has accepted as unowned rather than assigning them by inference.

A budget is three different things stacked in one number and they are almost never separated: what the current estate costs if nothing changes, what growth in the existing business will add, and what deliberate new work will add. Only the third is a decision anybody made, and it is the only one a holder can defend line by line. When they are fused into a single figure with a percentage on top, the conversation becomes an argument about the percentage, and nobody can tell whether a variance later in the year came from consumption drifting, a launch landing early, or a growth assumption that was optimistic in the first place.

## Use when

- An annual, quarterly, or project budget for cloud and vendor spend is being built or rebuilt.
- A run-rate baseline needs establishing and separating from the growth and step changes layered on top of it.
- Planned launches, migrations, decommissions, or capacity changes need costing before they are committed to a plan.
- Budget holders need identifying and matching to the allocation hierarchy, including the spend nobody has accepted.
- Alert thresholds need setting or retuning because they fire constantly or never fire at all.
- A prior budget missed and the planning basis needs rebuilding rather than re-anchoring on the same number plus a percentage.
- Contingency needs sizing against a named list of things it is meant to absorb.

## Do not use when

- The projection question is what spend will actually be, with a method and measured accuracy: that is `forecasting-variance-desk`. A budget is a target somebody accepted; a forecast is an estimate of reality, and confusing them is why variance conversations go badly.
- Variance against an existing budget needs attributing: that is `forecasting-variance-desk`.
- The allocation hierarchy or coverage that would tell you who holds which spend is unmeasured: that is `cost-allocation-tagging-desk`.
- The plan needs a margin view or a cost of revenue split: that is `software-cogs-margin-desk`.
- A commitment purchase is part of the plan: that is `commitment-portfolio-desk`, which sizes commitments against post-optimization usage rather than against a budget line.
- The budget needs the savings a planned optimization program will deliver: that is `optimization-backlog-desk`, whose realization record says what past estimates actually produced.
- The budget line is a SaaS renewal: that is `licensing-saas-spend-desk` for the entitlement and renewal analysis.

## Required evidence

- The run rate from the reconciled dataset, with the periods behind it marked complete or partial.
- The allocation hierarchy and the budget holders it maps to, with coverage stated.
- Planned launches, migrations, decommissions, and capacity changes with their timing and their sponsors.
- The business plan that drives consumption: headcount, customer growth, transaction volume, or whatever driver actually moves this estate.
- The prior budget with its actual outcome and its variance, because how the last plan failed is the best available evidence about how this one will.
- The planning calendar with submission dates, review forums, and the approval chain.
- The commitment position already carried, since committed spend is a floor the budget cannot go below without a penalty.
- Known seasonality and business cycle effects with the periods they land in.

## Workflow

**Outcome.** A budget line set scoped to named holders with a stated basis per amount, a run-rate baseline separated from growth and from step changes, planned work costed from comparable measured workloads with the comparison named, seasonality modeled where it is material, a contingency position with the named exposures it absorbs, alert thresholds with the action each one triggers, the approval state of each line, and the lines no owner has accepted reported as unowned with their amounts.

**Grounding.** The baseline comes from the reconciled dataset rather than from last year's budget, because a budget built on a budget compounds every prior error. Step change estimates come from comparable measured workloads with the comparison named, not from vendor calculators or from analogy to a workload nobody sized. Growth assumptions come from the business plan and carry the source, since a growth rate the practice supplied is a growth rate nobody will own when it is wrong.

**Constraints.** One ordering is mandated, because a budget of record commits an organization's spending authority and becomes the number teams are measured against for a year:

1. Build the lines with their bases and identify the holder for each.
2. Review each line with its holder, who accepts or disputes the amount and the basis.
3. Submit the accepted set through the finance approval chain.
4. Record the approved figures as the budget of record, with the approver and the date.

A budget quietly derived by the practice and circulated as approved is a target nobody agreed to defend, and the first variance conversation discovers the gap.

Beyond that ordering: every line carries its basis, and a line with no basis is not a budget line. The baseline is stated for a named period with its state, and a partial period is never annualized into a baseline. Growth, step changes, and run rate stay separable in the artifact so each can be challenged independently. Estimates for planned work name the comparable workload, its measured cost, and the scaling assumption between them. Alert thresholds are set where they are actionable and are tied to an action and an owner, since a threshold at a round number that nobody responds to is an unsubscribe waiting to happen. Committed spend is shown as a floor, and any budget line below it names the shortfall consequence. Savings assumed in the budget are named with the opportunity that produces them and their acceptance state, because a budget that pre-spends unrealized savings is a variance scheduled for later in the year.

**Parallel surface.** Individual budget lines, cost centers, teams, product lines, planned projects, and the per-line holder conversations are independent units and fan out, as does connector preflight across the cost dataset, the prior budget, the business plan, and the commitment position.

The aggregate is a single pass after the fan-out returns. The organizational total, the reconciliation of budgeted lines to the current run rate, the contingency sizing, and the check that committed spend is covered are whole-set calculations. Lines built independently sum to a number nobody planned, and the gap between the line sum and the top-down envelope is the actual planning conversation rather than an arithmetic problem.

**Acceptance bar.** Every line names a holder, an amount, a basis, and an approval state; the run rate, growth, and step change components are separable in the artifact; and every unowned line is visible with its amount rather than distributed to make the total resolve.

## Outputs

A complete run delivers this artifact set:

- `budget-lines.md`: each line with its scope, named holder, period, amount, basis, and approval state, with run rate, growth, and step change shown as separate components.
- `run-rate-baseline.md`: the baseline by scope with the periods behind it, their state, the one-off charges removed, and the adjustments made with their reasons.
- `planned-work-estimates.md`: each launch, migration, capacity change, or decommission with its timing, its estimated cost, the comparable measured workload used, the scaling assumption, and the estimate's confidence basis.
- `seasonality-and-cycle.md`: the periodic effects this estate actually shows with the evidence from prior periods, and the months they land in.
- `contingency-position.md`: the reserve with the named exposures it absorbs and the amount attributed to each, rather than a percentage on top of the total.
- `budget-alert-thresholds.md`: each threshold with its scope, its level, the reason that level rather than a round number, the action it triggers, and the owner who receives it.
- `unowned-budget-lines.md`: spend that belongs in the plan with no holder who has accepted it, with amounts and the specific reason ownership is unresolved.

Depth standard per artifact: a line entry gives the basis in enough detail to rebuild the amount, so "current run rate of the four production accounts, less the decommission of the legacy pipeline in the second quarter, plus twelve percent for the customer growth in the business plan" rather than "prior year plus growth". An estimate names the comparable workload and its measured cost. A threshold names the action, because a threshold with no action is a notification. An unowned line names why: no holder identified, holder identified but has not accepted, or the spend is shared and the split is unapproved.

In `diagnostic` mode, when the cost dataset, the prior budget, or the business plan exists and cannot be read, the run delivers `budget-connector-diagnostic.md` naming what was attempted and which lines cannot be built. A baseline is not reconstructed from a partial year.

The characteristic error on this desk is the confident holder name. Budget lines have a slot for an owner, the org chart makes one name obviously plausible, and filling it produces a plan that looks complete and approvable. It is discovered in the second month of the year when a manager is asked about a variance on spend they never agreed to carry, and the practice loses the argument even though the number was right. A line whose holder has not accepted it is written as unowned with its amount, and an unowned total of fifteen percent is a planning finding that belongs in front of finance rather than a gap to be tidied. Amounts get the same treatment: a budget figure with no basis is not entered, because the basis is what makes the line defensible later and a number placed to make the total work is unrecoverable by the time it matters.

## finops_packet fields to update

- `budgets[]` with `budget_id`, `scope`, `owner`, `period`, `amount`, `basis`, `alert_thresholds`, and `approval_state`.
- `budgets[].variance_drivers` seeded where the prior budget's outcome informs this one.
- `forecast.known_step_changes` with the planned launches, migrations, and decommissions this desk costed.
- `governance.approvals[]` for the budget of record, with `required_approver`, `authority_basis`, and `state`.
- `opportunities[]` referenced where a budget line assumes a saving, with the opportunity id and its acceptance state.
- `source_facts[]` with `locator` and `as_of`, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: setting or changing a budget of record. This is the defining halt for this stage, because a budget commits spending authority and becomes the number teams are measured against; it belongs to the budget holder with finance, and the practice prepares it rather than sets it.
- Missing approval: a budget line assumes savings from an optimization that no owner has accepted or scheduled, which turns an estimate into a commitment somebody else has to meet.
- Release integrity: a budget would be submitted with lines carrying no basis, with a baseline built on partial periods presented as complete, or with assumed savings counted as certain.
- Source conflict: the prior budget, the ledger, and the cost dataset give materially different actuals for the same period, so the baseline itself is disputed. Record both readings with their locators.
- Production or destructive: the next action would set a hard budget stop or a provisioning block, which is an availability control wearing a cost label, or would overwrite an approved budget of record.
- Security or privacy: the budget detail would expose headcount plans, unannounced launches, or commercial terms to an audience that should not have them.
- Connector unreachable: the cost dataset, the prior budget, or the commitment position cannot be read. State whether the source was empty or unreachable.

An unconfirmed launch date, a holder who has not yet responded, or a growth driver whose owner has not signed off is a soft gap: proceed with the line built, the assumption labeled, and the line marked unowned or unaccepted as applicable.

## Downstream handoffs

`forecasting-variance-desk` needs the budget lines with their bases and their step changes, because variance attribution is only meaningful against a plan whose components are separable. `commitment-portfolio-desk` needs the planned decommissions and migrations, since committing against workloads scheduled to disappear is one of the more expensive mistakes available. `chargeback-invoicing-desk` needs the holder mapping and the approval state. `engineering-cost-review-desk` needs each team's line with its basis, so the review is about the difference between plan and behavior rather than about whether the plan was fair. `optimization-backlog-desk` receives any savings the budget assumes, so they are tracked as commitments rather than as hopes.

## Quality bar

Lines that a holder can defend because they can see how the number was built. Run rate, growth, and step change visible as separate components. Estimates anchored to workloads somebody actually measured. Thresholds tied to actions and owners. Contingency sized against named exposures rather than expressed as a percentage. Unowned spend stated at its real size, because an honest unowned line in November is a planning conversation and the same line in March is an argument.
