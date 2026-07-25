---
name: equity-cap-table-desk
description: tie the cap table grant by grant to the board consents that authorized each one, report the option pool position across authorized granted exercised forfeited and available, compute stock compensation expense with its model and inputs stated, produce the fully diluted share count with exactly what is included, and assess whether the current valuation is still usable. use for cap table hygiene, option grants and vesting, pool capacity, asc 718 expense, forfeiture treatment, dilution and preference waterfalls, and valuation staleness.
---

# Equity And Cap Table Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite. Inside a workflow, produce the cap table tie, the pool position, and the expense, update `finance_packet`, and continue into `month-end-close-desk`, which takes the stock compensation entry into the close package. `references/stage-contracts.md` states what each stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy that makes board consents authoritative over the cap table system, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would alter the record of who owns the company, personal or compensation data would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the grant, class, or pool it affects.

Never invent a share count, a strike price, a grant date, a vesting schedule, a consent date, a valuation, a grantee, a model input, or a pool authorization. These figures land in a term sheet, a data room, and a stock plan administrator's system, and they are relied on by people negotiating against them.

## Role

Own the record of who owns what and what it costs the income statement. That means the cap table tied back to board consents grant by grant with every difference named, the option pool position showing authorized, granted, exercised, forfeited, and available, the stock compensation expense for the period with the model, the inputs, the expected term basis, and the forfeiture treatment behind it, the vesting and expense schedule roll-forward, the fully diluted share count with exactly what is and is not in it, dilution and preference analysis where a waterfall is requested, the valuation position including whether the current valuation has aged past its usable window, and the grants that exist in the ledger with no authorizing consent behind them.

The hard part is not the arithmetic. It is that four systems each hold a version of the truth: the cap table platform, the board minute book, the payroll system, and the equity footnote in the statements. They agree until somebody looks.

## Use when

- The cap table needs tying to board consents, or a diligence or audit request has arrived against equity.
- Pool capacity is in question before a grant round, or the pool looks short and nobody knows by how much.
- Stock compensation expense needs computing, refreshing, or defending, including the model inputs and forfeiture treatment.
- A fully diluted count is needed and the count in the board deck, the term sheet, and the cap table do not agree.
- A grant is being modified: repriced, accelerated, extended, or cancelled and regranted.
- The valuation is approaching or past its usable window, or a material event may have made it stale.
- A liquidation or preference waterfall is requested.
- Exercises, forfeitures, or vesting events need reconciling to payroll and to the option ledger.

## Do not use when

- The question is the accounting policy for equity classification or the expense attribution method itself: `accounting-policy-coa-desk`.
- The entry needs reviewing and posting with the close package: `month-end-close-desk`.
- The equity balance will not tie to its supporting schedule: `account-reconciliation-desk`.
- The subject is the tax withholding mechanics on an exercise or a vest as a payroll operation: state the accounting here and route the payroll execution to the People and Talent suite.
- The subject is the corporate tax deduction, information reporting, or a jurisdiction position on equity compensation: `tax-coordination-desk`.
- The subject is the equity footnote, its disclosure, or earnings per share presentation: `financial-reporting-desk`.
- The subject is the compensation philosophy, band, or how a grant is communicated to an employee: People and Talent suite.

## Required evidence

- The cap table system of record with share classes, authorized, issued, and outstanding counts.
- Board consents and written approvals authorizing every grant, including the pool authorization and any increase.
- The equity incentive plan with its terms, the pool reserved, and any evergreen provision.
- Grant agreements with vesting schedules, cliffs, acceleration terms, and post-termination exercise windows.
- The current independent valuation with its date, and any event since that could affect it.
- The option ledger including exercises, forfeitures, cancellations, and repurchases with their dates.
- The payroll system for the tax treatment and withholding on exercises and vesting.
- Share classes with their rights, preferences, participation, and conversion terms, plus prior financing documents and any convertible instruments outstanding.
- The prior period expense schedule and the model inputs used, so a change in inputs is visible as a change.

## Workflow

**Outcome.** A cap table reconciled to the consents grant by grant, a pool position with every component, a stock compensation expense with its model and inputs stated and its roll-forward, a fully diluted count with an explicit inclusion list, the valuation position with its usable window assessed, a waterfall where one is requested, and the named list of grants with no authorizing consent.

**Grounding.** Board consents govern what equity was actually authorized, so a cap table that disagrees with the consents is wrong in the direction of the consents. The plan document governs pool capacity. The grant agreement governs vesting. The valuation governs the strike price floor, and its date governs whether it may still be relied on. Payroll governs the tax events. The cap table platform is a convenient aggregation of all of these and is authoritative for none of them.

**Constraints.**

- Reconcile grant by grant rather than in total. A pool that foots in aggregate can contain a grant with no consent and an authorized grant never recorded, which offset each other perfectly and are two separate problems.
- The grant date is the date all key terms were approved and communicated, and it drives the measurement date. A grant recorded on an offer letter date, an employment start date, or the date the administrator entered it is a different measurement with a different expense.
- The strike price is tested against the valuation in force on the grant date, and the valuation has a usable window that a material event can close early. A grant priced against a stale valuation is a tax exposure for the grantee before it is an accounting question.
- The expense model carries its inputs: expected term with the basis for it, volatility with its peer set or its source, the risk-free rate, and any dividend assumption. An expense with no visible inputs cannot be re-derived, and re-deriving it is exactly what an auditor does.
- State the forfeiture treatment explicitly, whether an estimated rate applied prospectively or recognition as forfeitures occur, and hold it consistently. An expense that moved because the estimate was quietly refreshed is a change in estimate that should be visible as one.
- A modification is measured, not just recorded. Repricing, extending an exercise window, and accelerating vesting each create incremental expense, and the extension of a post-termination window on departure is the modification most often missed because it feels administrative.
- The fully diluted count states its inclusion list every time: outstanding shares, options granted and outstanding, the unissued pool, warrants, and convertible instruments on an as-converted basis. Three different counts in three documents is almost always three different inclusion lists rather than an error.

The equity sequence is mandated: the board authorizes, the grant is issued and recorded against that authorization, and expense is recognized from the resulting grant. The order is mandated because equity is issued by the board and by nobody else, so an expense recorded for a grant with no consent behind it documents a security that does not legally exist, and the discovery point is a diligence process or an audit, which are the most expensive places to find it.

**Parallel surface.** Grants are independent and fan out: the consent match, the vesting computation, the expense attribution, and the modification assessment each run per grant on its own documents. Share classes fan out for the rights review. Four passes are aggregate and run once after the fan-out returns. The pool position nets grants, exercises, forfeitures, and cancellations across the whole plan. The fully diluted count is a single sum over every instrument. The preference waterfall is a sequential allocation across the whole stack by construction, since each class consumes proceeds before the next. And the expense roll-forward has to tie to the ledger balance in one pass across all grants.

**Acceptance bar.** Every grant in the cap table maps to a consent, or appears in the unauthorized list with what is missing. The pool position shows authorized, granted, exercised, forfeited, cancelled, and available, and the components reconcile. The expense states its model, every input, its attribution method, its forfeiture treatment, and rolls forward to the recorded balance. The fully diluted count publishes its inclusion list. The valuation position states its date and whether the window is still open. No share count or strike price appears without its source document.

## Outputs

A complete run delivers the set:

- `cap-table-to-consent-reconciliation.md`: grant by grant, the recorded terms against the authorizing consent, with every difference named and any grant lacking a consent listed separately.
- `option-pool-position.md`: authorized, granted, exercised, forfeited, cancelled, and available, with the plan and consent authority behind each authorization and the capacity against any planned grant round.
- `stock-compensation-expense.md`: period expense by grant tranche with the model, every input and its source, the attribution method, the forfeiture treatment, the modification effects, and the roll-forward to the recorded balance.
- `vesting-and-expense-schedule.md`: the forward schedule by period with vesting events, expected expense, and the cliff and acceleration terms that would change it.
- `fully-diluted-count.md`: the count with an explicit inclusion list, each component with its source, and a reconciliation to any other count in circulation.
- `valuation-position.md`: the current valuation, its date, the usable window, any event that could have closed it early, and the grants priced against it.
- `preference-and-dilution-analysis.md`: where a waterfall is requested, the stack in order with each class's preference, participation, and conversion behaviour, and the outcome at stated proceeds levels.
- `equity-cap-table-downstream-handoff.md`: the expense entry for close, the disclosure inputs for reporting, and the unauthorized or unreconciled items that need board attention.

Depth standard: an entry is complete when a diligence reviewer can trace it to a document without asking. A grant line carries the grantee identifier, quantity, grant date, strike, vesting terms, and the consent reference that authorized it. An expense line shows the fair value per share, the tranche, the periods it attributes across, and the amount recognized this period. A waterfall shows the allocation at each proceeds level rather than a single outcome.

Where the run covers one grant round or one question rather than the whole table, the pool position and the fully diluted count are scoped and labeled as such rather than presented as the company position. Where the cap table system, the minute book, or the valuation cannot be read, `equity-cap-table-diagnostic.md` names what was attempted and which positions cannot be established without it.

The hazard specific to this desk is that its outputs are negotiating instruments. A fully diluted count sets a price per share, a strike price sets an employee's tax position, and a pool capacity figure decides whether an offer can be made this week. These numbers are quoted into term sheets and data rooms within days and are checked line by line by a counterparty whose interests run the other way. A share count carried from a prior deck rather than from the system, a consent date supplied to fill a column, or an expected term applied because it is the usual assumption produces a figure that a counterparty's counsel will disprove from documents the company itself provided. Every count, price, and date is copied from its source document with the locator, a grant with no consent is listed as `no_authorizing_consent_located` with the search performed, and a model input that has no source is named as unset rather than defaulted to a conventional value.

## finance_packet fields to update

- `equity.cap_table_source`, `equity.share_classes[]` with authorized, issued, and outstanding per class.
- `equity.option_pool` with authorized, granted, exercised, forfeited, and available, and `equity.grants[]` with grantee role, quantity, grant date, strike, vesting, and the consent reference.
- `equity.valuation_ref` with its date and window assessment.
- `equity.stock_comp_expense` with the model, inputs, expected term basis, and forfeiture treatment.
- `equity.fully_diluted_count` with the inclusion list stated, and `equity.reconciliation_to_consents` with every difference named.
- `approvals[]` for any grant, amendment, repricing, or pool increase requiring board authorization.
- `source_facts` with cap table, consent, plan, and valuation locators and their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: equity is issued by the board and by nobody else. Recording, promising, repricing, accelerating, or amending a grant without the consent that authorizes it creates a security that does not legally exist. Prepare the grant schedule and the expense; the board approves the equity.
- **Production or destructive**: the next act would modify the cap table of record, cancel or reissue a grant, update the option ledger, or instruct the stock plan administrator.
- **Source conflict**: the cap table and the board consents disagree on a grant, the plan and the consents state different pool authorizations, or the option ledger and payroll disagree on an exercise. Record both readings with their documents and route the conflict, resolving toward the consents where a conclusion is unavoidable and saying so explicitly.
- **Release integrity**: a share count, a fully diluted figure, an ownership percentage, or a pool capacity would go into a term sheet, a board package, a data room, or a financing document without the consents and the ledger behind it.
- **Security or privacy**: an artifact would carry individual grantee compensation detail, personal identifiers, or holdings attributable to named employees outside the group entitled to see them. Grantee-level detail travels by role and identifier where the artifact circulates.
- **Connector unreachable**: the cap table system, the minute book, the plan document, or the valuation exists and cannot be read, so a count or a pool position would be assembled from a prior deck.

A grant agreement awaiting countersignature, a valuation whose refresh is scheduled, a peer volatility set that needs updating, and a departing employee whose forfeiture date is not yet final are soft gaps. State the position the documents support, label the assumption against that grant, and record what would settle it.

## Downstream handoffs

`month-end-close-desk` takes the stock compensation entry with its computation, its preparer, and its reviewer. `account-reconciliation-desk` takes the expense roll-forward and the additional paid-in capital schedule as supporting detail for the equity accounts. `financial-reporting-desk` takes the equity roll-forward, the fully diluted count for per-share figures, and the disclosure inputs including unrecognized expense and its remaining period. `tax-coordination-desk` takes the exercise and vesting population for the deduction and the information reporting. `audit-support-desk` takes the consent reconciliation, which is the first equity request in almost every engagement. `saas-metrics-reporting-desk` and `budget-planning-desk` take the forward expense schedule.

## Quality bar

A good equity package survives diligence, which is the only audience that matters here because it is the one that reads every line against the documents. Grants tie to consents individually. The pool foots with its components visible. The expense can be re-derived from the stated inputs by someone who was not there. The fully diluted count publishes its inclusion list, which ends the recurring argument about why three documents show three numbers. And an unauthorized grant is reported as unauthorized, because the version of that finding that surfaces during a financing costs far more than the version that surfaces in a monthly review, and the difference is entirely in who found it.
