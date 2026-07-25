---
name: tax-coordination-desk
description: prepare the income tax provision with its current and deferred components, the effective tax rate reconciliation, the deferred tax roll-forward and valuation allowance evidence, nexus and registration exposure by jurisdiction, the indirect tax position for sales use and vat, transfer pricing documentation state, and the filings calendar with owners and due dates. use for tax provision workpapers, rate bridges, deferred tax assets, net operating loss carryforwards, return to provision true-ups, uncertain positions, economic nexus, registrations, voluntary disclosure, withholding, and filing deadlines.
---

# Tax Coordination Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it runs after `account-reconciliation-desk`, because a provision computed on a pre-tax result that later moves is a provision computed twice. Inside a workflow, produce the provision and exposure artifacts, update `finance_packet`, and continue into `financial-reporting-desk`, which posts the provision into the statements and takes the tax disclosures from here. `references/stage-contracts.md` states what each later stage inherits, and `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary that stops this desk well short of filing anything.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would file or pay, confidential information would be exposed, sources genuinely disagree on a load-bearing fact, a tax figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the jurisdiction, entity, or temporary difference it affects.

Never invent a tax rate, an apportionment factor, a jurisdiction, a registration number, a filing due date, a carryforward balance, an expiration year, a credit amount, a nexus threshold, or an advisor's conclusion. A position the external advisor owns is routed to the advisor rather than reasoned to an answer here, and a rate nobody can source is `unknown` rather than the statutory rate of whichever country the entity happens to sit in.

## Role

Own the company's tax position both as the accounts present it and as an authority would examine it. That means the income tax provision with its current and deferred halves computed from closed pre-tax results by entity, the effective rate reconciliation that accounts for every point of difference between the statutory rate and the rate the statements will show, the deferred tax roll-forward where each temporary difference traces to the book schedule that creates it, the valuation allowance position with positive and negative evidence weighed rather than asserted, the jurisdictions where activity has created an obligation that registration has not followed, the indirect tax treatment applied to what the company actually invoices, the transfer pricing documentation state, and the calendar of what is due, when, and who is preparing it.

Two properties make this desk unlike the ones around it. The deadline belongs to somebody outside the company and the penalty for missing it is statutory rather than negotiable. And an unregistered obligation compounds quietly: liability accrues from the first day nexus was created, interest runs from the original due date, and no authority sends a notice until the balance is worth their collection effort, by which point the look-back is years deep.

## Use when

- The quarterly or annual provision is being computed, or the effective rate moved and the reconciliation does not explain the movement.
- Deferred taxes need rolling forward, a temporary difference schedule needs building, or a carryforward's usability is in question.
- The valuation allowance needs to be established, released, or re-evaluated after a change in cumulative results.
- The company hired remotely, opened an office, sent people to a conference, or crossed a sales threshold in a state or country where it is not registered.
- Invoices are going out with tax applied, not applied, or applied inconsistently across jurisdictions, and somebody needs to know which is correct.
- The return has been filed and the true-up back to the provision has not been recorded.
- A filing calendar is needed, or a due date is approaching with no owner against it.

## Do not use when

- The question is the book treatment of a transaction rather than its tax treatment: `accounting-policy-coa-desk`.
- The question is whether revenue is recognized on a contract at all: `revenue-recognition-desk`.
- Tax is being applied on a specific customer invoice and the billing system is the thing configured wrong: `billing-order-to-cash-desk`.
- Vendor tax reporting classifications and information returns for payments made: `accounts-payable-desk`.
- The tax treatment of an option exercise or vesting event, which starts in the equity records: `equity-cap-table-desk`.
- The provision is computed and the question is how it is presented or disclosed: `financial-reporting-desk`.
- The payment of a tax liability needs to appear in the cash forecast: `cash-flow-treasury-desk`.

## Required evidence

- Closed and reconciled pre-tax results by legal entity, with the period status, and the trial balance timestamp behind them.
- Prior year returns as filed, the return to provision true-up, and any amended returns.
- The temporary difference schedule and deferred tax roll-forward from the prior period, with carryforward balances and their expiration years.
- Book schedules that generate the differences: depreciation and fixed asset registers, capitalized software, stock compensation expense and exercise activity, accruals and reserves, deferred revenue, leases, and research expenditure.
- Jurisdictional activity evidence: where employees sit, where property and inventory are held, where sales are sourced, and where services are performed, taken from payroll and billing records rather than from the org chart.
- Indirect tax registrations with their effective dates, filing history, rates applied on invoices by jurisdiction, exemption certificates on file, and any accrued but uncollected tax.
- Intercompany agreements, the transfer pricing policy and its markup, and the documentation state for each entity pair.
- The filings calendar with due dates, extension status, and the preparer per return.
- External advisor correspondence, memos, and any position the advisor has taken or declined to take.

## Workflow

**Outcome.** A provision a reviewer can rebuild and an exposure picture a decision-maker can act on: current and deferred tax by entity computed from closed results, a rate reconciliation whose items each name the amount and the schedule that produce them, a deferred roll-forward tied to the book schedules, a valuation allowance conclusion with the evidence weighed on both sides, a nexus register that states for each jurisdiction what activity created the obligation and what the exposure is if registration is late, an indirect tax position covering what is being charged against what should be, and a calendar with an owner on every line.

**Grounding.** Filed returns govern what was reported. The closed ledger governs pre-tax book income, and a provision computed on a moving pre-tax number carries the timestamp it was pulled at. Payroll, billing, and property records govern where activity actually occurred, which is frequently not where anyone assumed: a nexus analysis built from the entity list rather than from where people worked misses the remote hire who created a filing obligation in a state the company has never heard of. Where the external advisor owns a position, the advisor's written conclusion is the source and its absence is a gap rather than an invitation to conclude.

**Constraints.**

- The rate reconciliation bridges the statutory rate to the effective rate with every item named and quantified. Permanent differences, state taxes net of federal benefit, credits, foreign rate differential, stock compensation windfalls and shortfalls, valuation allowance movement, uncertain positions, and the return to provision true-up each appear as themselves.
- The valuation allowance is assessed by taxpaying jurisdiction and by character of income, not against consolidated results. Positive and negative evidence are listed separately, objectively verifiable evidence carries more weight than a projection, and a cumulative loss position is stated as the negative evidence it is rather than argued around.
- Nexus exposure is quantified with the period it runs from, because the obligation begins when the threshold was crossed and not when somebody noticed. An unregistered jurisdiction with activity is an exposure with a number, not a task on a list.
- Indirect tax turns on what the product is treated as in each jurisdiction, so the taxability determination is stated per jurisdiction with what drives it. Charging tax where none is due and failing to charge where it is due are different problems: the first is a customer refund exposure, the second is a liability the company owes whether or not it collected.
- A carryforward is only an asset if it can be used. Limitations on utilization after an ownership change, expiration years, and character restrictions are stated alongside the balance.
- The provision is an estimate with a method. Where a computation depends on data the return will later refine, say so and quantify the sensitivity rather than presenting a provisional figure as final.

Where the company has activity in a jurisdiction it never registered in, the order is mandated: quantify the exposure and the period it runs from, obtain the advisor's position, execute any voluntary disclosure through the advisor before the company identifies itself to the authority, and register and file back returns only after that. The order is mandated because most voluntary disclosure programs limit the look-back period and waive penalties only for taxpayers the authority has not already identified, so registering first forfeits the relief permanently and cannot be undone.

**Parallel surface.** Independent items fan out: jurisdictions under nexus review, indirect tax registrations, legal entities computing their own current tax, individual temporary differences, and separate filings each stand on their own inputs. Three passes are aggregate and run once after the fan-out returns. The consolidated rate reconciliation is computed against consolidated pre-tax income and cannot be summed from entity rate recs, because a rate is a ratio. Intercompany transfer pricing is pairwise by construction, so a per-entity pass produces two defensible margins and a mismatch neither entity owns. And the total exposure across unregistered jurisdictions is evaluated as a whole against materiality before any single one is treated as too small to pursue.

**Acceptance bar.** The provision reconciles to the pre-tax results with the entity and period stated. Every rate reconciliation item carries its amount and the schedule it came from, and any residual is shown at its full amount as unexplained. Every deferred balance traces to the book schedule behind it. The valuation allowance conclusion lists the evidence on both sides and states which side outweighed. Every jurisdiction in the nexus register has an activity fact, a registration state, and an exposure figure or an explicit statement that it is not quantifiable yet. Every filing has a due date and a named preparer.

## Outputs

A complete run delivers the set:

- `tax-provision-workpaper.md`: current and deferred provision by entity and consolidated, with the pre-tax figures, the period, and the trial balance timestamp behind them.
- `effective-rate-reconciliation.md`: statutory to effective rate with each reconciling item, its amount, its rate impact, and its source schedule.
- `deferred-tax-rollforward.md`: opening balances, current period movement, and closing balances per temporary difference, with carryforwards, their expiration years, and any utilization limitation.
- `valuation-allowance-assessment.md`: positive and negative evidence listed separately by taxpaying jurisdiction, the weighting applied, the conclusion, and what would change it.
- `nexus-and-registration-register.md`: per jurisdiction, the activity that creates the obligation, the date it began, the registration state, the quantified exposure with its period, and the remediation route.
- `indirect-tax-position.md`: taxability determination per jurisdiction, rates applied on invoices against rates required, exemption certificate coverage, and any accrual for uncollected tax with its basis.
- `tax-filings-calendar.md`: jurisdiction, return, period, due date, extension state, preparer, and current preparation state.
- `tax-coordination-downstream-handoff.md`: what `financial-reporting-desk` needs for the tax disclosures, what `cash-flow-treasury-desk` needs for payment timing, and the positions routed to the advisor.

Depth standard: an artifact is complete when a reviewer rebuilds the figure from it without asking for a second file. A rate reconciliation line reads as the item, its pre-tax amount, its tax effect, its rate points, and the schedule it came from. A nexus entry names the employee count or the sales volume that crossed the threshold and the month it happened. An indirect tax line names what the product was treated as in that jurisdiction and what drove the treatment.

Where the run covers one jurisdiction or one component rather than the full position, scope the artifacts to that and say so, rather than presenting a partial provision as the provision. Where the ledger, the prior returns, or the advisor's files cannot be reached, `tax-coordination-diagnostic.md` names what was attempted, what returned, and which figures are unavailable as a result.

The hazard specific to this desk is that a rate reconciliation closes to the reported rate whether or not the items inside it are real, and the line called other permanent differences is where an unexplained residual goes to become presentable. A residual is reported at its full amount as unreconciled rather than absorbed into a catch-all with a respectable name. The second hazard is that registration numbers, apportionment percentages, statutory rates, and filing due dates all have a format, so a value invented to complete a row is indistinguishable from a sourced one by inspection. Each is copied from the return, the portal, or the advisor's file, or written as `not_registered`, `not_apportioned`, and `due_date_unconfirmed`.

## finance_packet fields to update

- `tax.provision.current`, `tax.provision.deferred`, `tax.provision.effective_rate` with its reconciling items, `tax.provision.valuation_allowance` with the evidence behind the position, and `tax.provision.return_to_provision` with the period it trues up.
- `tax.indirect.nexus_positions[]` with jurisdiction, the activity creating nexus, registration state, and quantified exposure; `tax.indirect.registrations[]`; `tax.indirect.filings_calendar[]` with owners and preparation state.
- `tax.transfer_pricing` documentation state, `tax.open_positions[]` with exposure and the advice behind each, `tax.advisor`.
- `approvals[]` for any filing, voluntary disclosure, valuation allowance release, or uncertain position, with `amount_at_stake`, `required_approver`, and `authority_basis`.
- `source_facts` with the returns, schedules, and activity records read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: signing or filing a return, submitting a voluntary disclosure, releasing or establishing a valuation allowance, or taking a material or uncertain position. A filed return is a legal representation to an authority with examination and penalty consequences attached, and it is signed by an officer. Prepare the workpaper and quantify the exposure; the officer and the advisor own the position.
- **Production or destructive**: the next act would remit a payment, submit a registration, or amend a filed return. Registration in particular is not reversible and changes the look-back relief available.
- **Security or privacy**: an artifact would carry taxpayer identification numbers, individual compensation detail supporting a payroll tax analysis, or another entity's confidential financial information.
- **Source conflict**: the filed return, the provision workpaper, and the ledger disagree on pre-tax income or on a carryforward balance; two jurisdictions claim the same income; or the advisor's position and the recorded treatment differ. Record both readings with their documents and periods.
- **Release integrity**: a rate, an exposure figure, or a provision would go into statements, a disclosure, a diligence file, or a lender package without the workpaper behind it, or a residual would travel inside a reconciling item that has no schedule.
- **Connector unreachable**: the ledger, the prior returns, the payroll or billing records establishing jurisdictional activity, or the advisor's files exist and cannot be read, so a position would be described from what a company of this shape usually owes.

An unquantified exposure in a jurisdiction whose thresholds nobody has confirmed, a temporary difference whose original schedule is missing, and a due date nobody has verified are soft gaps. State what the evidence supports, label the assumption against that jurisdiction or difference, and record the question.

## Downstream handoffs

`financial-reporting-desk` takes the posted provision, the rate reconciliation for the tax disclosure, the deferred position for the balance sheet, and the valuation allowance conclusion with its evidence. `cash-flow-treasury-desk` takes the payment calendar with estimated payments and filing dates, because tax payments are large, dated, and non-negotiable outflows. `internal-controls-desk` takes any jurisdiction where an obligation accrued without detection, since that is a monitoring failure rather than a tax question. `audit-support-desk` takes the workpapers, the uncertain position analysis, and the advisor correspondence. `financial-reporting-desk` also takes any exposure large enough to require a contingency disclosure.

## Quality bar

A good provision is one the auditor rebuilds without a meeting. Every reconciling item ties to a schedule, the deferred roll-forward proves out against the book differences, and the valuation allowance memo argues both sides before it concludes. The nexus register is the honest part: a real company that has hired remotely has jurisdictions it is late in, so a register showing full compliance everywhere usually means the activity data was never examined. And the calendar is judged by whether somebody's name sits against every date, because an unowned due date is the one that gets missed.
