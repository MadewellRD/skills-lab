---
name: cash-flow-treasury-desk
description: build the cash position by bank account and entity, the direct thirteen week receipts and disbursements forecast with its low point week, runway with the burn definition named explicitly, working capital movements explaining profit against cash, covenant headroom computed on the credit agreement's definitions, trapped and restricted cash, and measured forecast accuracy. use for cash forecasting, liquidity planning, runway and burn questions, bank balance consolidation, book to bank differences, payroll and debt service timing, borrowing base, minimum liquidity covenants, and funding decisions.
---

# Cash Flow Treasury Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it runs after `financial-reporting-desk`, because the reported position sets the starting balance and the working capital movements the forecast has to explain. Inside a workflow, produce the position, forecast, and covenant artifacts, update `finance_packet`, and continue into `saas-metrics-reporting-desk`, which takes the burn figures that feed the efficiency metrics. `references/stage-contracts.md` states what each later stage inherits, and `references/suite-workflow-contract.md` defines the packet, the source hierarchy that makes the bank statement authoritative for cash, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would move money, confidential information would be exposed, sources genuinely disagree on a load-bearing figure, a liquidity figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the account, counterparty, or forecast week it affects.

Never invent a bank balance, an account, a statement date, a collection date, a payment amount, a facility term, a covenant level, a cure right, or a restriction on moving cash. A receipt nobody can date is an unscheduled receipt rather than one placed in a convenient week, and a balance that has not been confirmed to a statement is a book balance labeled as such.

## Role

Own the company's cash: where it is, what it is committed to, when it runs short, and what the agreements let the company do about it. That means the position by bank account and legal entity with the statement date behind each balance, the direct forecast built from dated receipts and disbursements over the requested horizon, the projected low point and the week it occurs, runway with the burn definition stated rather than assumed, the working capital movements that explain why profit and cash disagree, covenant headroom computed on the definitions the credit agreement writes, the cash that exists but cannot be used, the funding actions available with their lead times, and the measured accuracy of the forecasts this desk produced before.

Runway is the figure in this suite with the shortest path to a consequential decision. It drives hiring freezes, bridge rounds, and layoffs, and the two common burn definitions routinely produce answers that differ by months. A runway number without its definition attached is not a shorter answer; it is a different one.

## Use when

- A cash position is needed across accounts and entities, or the balances in the ledger and the balances at the bank do not agree.
- A thirteen week or other short horizon forecast is needed, or the existing one has stopped matching what actually happened.
- Runway or burn is being asked about, especially before a board meeting, a fundraise, or a hiring decision.
- A covenant test date is approaching, headroom needs computing, or a borrowing base certificate is due.
- A large disbursement is being scheduled and somebody needs to know whether the week clears.
- Cash exists in one entity and the obligation sits in another, or a balance is restricted, pledged, or held against a letter of credit.
- Collections, payment timing, or vendor terms are being changed to move cash and the consequence needs quantifying.

## Do not use when

- The question is why a specific customer has not paid and what to do about it: `accounts-receivable-collections-desk`.
- A payment run needs preparing, matching, or approving: `accounts-payable-desk`.
- The commitment has not yet been approved and the question is who can approve it: `spend-approval-authority-desk`.
- The reported cash flow statement for a closed period is the deliverable: `financial-reporting-desk`.
- The bank account will not reconcile to the ledger and the difference needs resolving: `account-reconciliation-desk`.
- The forecast in question is the full profit and loss outlook rather than the cash view: `forecast-scenario-desk`.
- Burn is being used as an input to an efficiency metric rather than to a liquidity question: `saas-metrics-reporting-desk`.

## Required evidence

- Bank statements and current balances for every account and entity, with the statement date and currency for each, plus any sweep, concentration, or zero balance arrangement between them.
- The book to bank reconciliation with outstanding payments and deposits in transit listed individually.
- The receivable aging with invoice level detail, contractual payment terms, and the payment history that shows how each customer actually pays rather than how the terms say they should.
- The payable position with invoice due dates, the payment run calendar, and any invoices being held past terms.
- The payroll calendar with gross amounts, employer taxes, benefit remittances, and the dates funding has to be in the account.
- The tax payment calendar, debt facilities with their amortization, interest dates, borrowing base mechanics, and covenant definitions, levels, test dates, and cure provisions.
- Committed spend, subscription renewals, and one-off obligations with their dates and amounts.
- Restrictions on moving cash between entities, including local capitalization requirements, withholding on repatriation, pledged balances, and security deposits.
- Prior forecasts and the actuals for those weeks, so accuracy is measured rather than described.

## Workflow

**Outcome.** A liquidity picture somebody can act on this week: the position by account and entity tied to statements, a direct forecast where every line has a date and a counterparty, the low point with the week it occurs and what is driving it, runway with the burn definition and the periods averaged both named on the same line as the number, working capital movements reconciling profit to cash, covenant headroom computed on the agreement's terms with the test date, the trapped and restricted balances excluded from usable cash and shown separately, funding options with their lead times, and the accuracy of prior forecasts measured against what happened.

**Grounding.** The bank statement is cash. The book balance is a claim about cash, and the difference between them is a list of named items with amounts and ages rather than a plug. Payment history governs the timing of receipts, because contractual terms describe an intention and history describes a behavior; a customer who has paid at sixty days for two years will pay at sixty days. The credit agreement governs the covenant computation, including every defined term, add-back, and cap it writes. Payroll and tax calendars are fixed dates set outside the company and are modeled as such.

**Constraints.**

- The forecast is direct: receipts and disbursements with dates and counterparties. A line derived by spreading a monthly figure across weeks is a smoothing artifact, and the low point is exactly the week that smoothing erases.
- Runway carries its definition on the same line as the number. Gross burn and net burn differ by every dollar of collections, so the artifact states which is in use, the periods averaged, the cash balance it divides, and whether restricted balances were included.
- Trapped cash is excluded from usable liquidity and reported separately with the specific restriction. Consolidated cash that sits in an entity which cannot fund the obligation that needs it is a number that reads as comfort and functions as none.
- Covenant headroom is computed on the agreement's defined terms and states the clause it applied. Where the internal definition differs, show both with the gap quantified.
- Payroll and the employer taxes and withholdings that travel with it are funded ahead of discretionary disbursements in any constrained week, because unremitted payroll trust fund amounts create personal liability for the officers who directed the payment order and no other payable does.
- Forecast accuracy is measured, not asserted. State the error of prior weeks against actuals with the method used, because a forecast whose accuracy nobody has measured is a projection with unknown precision being used for a decision that assumes precision.
- Every inflow carries a confidence basis. A signed contract with a history of on-time payment, an invoice in dispute, and an expected renewal that has not been signed are three different things and are labeled as three different things.

Where a covenant test is projected to fail, the order is mandated: compute the test on the agreement's definitions, identify the cure the agreement permits and the window it allows, escalate to the officer who signs and to counsel, and approach the lender before the certificate is due. The order is mandated because delivering a certificate the company knows to be inaccurate is a separate default from the financial covenant breach and is generally the one without a cure, and because equity cure and grace provisions expire on dates written into the agreement, so a cure discovered after its window has closed no longer exists.

**Parallel surface.** Independent items fan out: bank accounts under reconciliation to statements, legal entities computing their own position, individual customer collection profiles, separate debt facilities and their covenant computations, and distinct disbursement categories each stand on their own inputs. Three passes are aggregate and run once after the fan-out returns. The consolidated forecast nets across accounts and entities, and it is precisely that netting that exposes trapped cash, so a per-account forecast hides the constraint it exists to find. The low point is a property of the netted weekly position and cannot be identified from any single account. And liquidity against a minimum balance covenant is tested against the defined group of accounts the agreement specifies rather than against the total.

**Acceptance bar.** Every balance names its account, entity, currency, and statement date. Every forecast line has a date, a counterparty or category, an amount, and a confidence basis. The low point states its week and the two or three items that create it. Runway states its burn definition, its averaging window, and its cash basis on the same line as the number. Every covenant computation cites the defined term applied and states the headroom against the level at the test date. Restricted and trapped balances are excluded from usable cash and named individually. Prior forecast accuracy is stated as a measured error with its method.

## Outputs

A complete run delivers the set:

- `cash-position.md`: balances by account and entity with currency, statement date, sweep relationships, and the book to bank reconciliation with each outstanding item listed.
- `thirteen-week-cash-forecast.md`: dated receipts and disbursements by week with counterparties and confidence bases, the netted weekly position, the low point with its week and its drivers, and the assumptions each material line depends on.
- `runway-and-burn.md`: runway with the burn definition, the periods averaged, the cash basis, the treatment of restricted balances, and the sensitivity of the answer to the definition chosen.
- `working-capital-analysis.md`: receivable, payable, and deferred revenue movements reconciling the period's result to the period's cash, with the days measures and their formulas stated.
- `covenant-headroom.md`: per facility, the tested terms as the agreement defines them, the computation, the level, the headroom, the test date, and any cure provision with its window.
- `trapped-and-restricted-cash.md`: each balance that cannot fund a given obligation, the restriction that creates the limit, the entity holding it, and what releasing it would require.
- `funding-options.md`: the actions available including collections acceleration, payment deferral, facility draws, and intercompany funding, each with its lead time, its cost, and its approval requirement.
- `forecast-accuracy.md`: prior forecast weeks against actuals with the error measured, the method stated, and the recurring bias identified where one exists.
- `cash-flow-treasury-downstream-handoff.md`: what `saas-metrics-reporting-desk` and `forecast-scenario-desk` inherit, with unresolved liquidity constraints named.

Depth standard: an artifact is complete when the officer schedules or defers a payment from it. A forecast line reads as a named counterparty, an amount, a week, and why that week. A covenant computation shows the build from the reported figure through each permitted adjustment. A funding option names the lead time in days and who approves it.

Where the run covers a single entity or a shorter horizon than the full position, scope the artifacts to that and say so. Where the bank feed, the receivable subledger, the payable subledger, or the credit agreement cannot be reached, `cash-flow-treasury-diagnostic.md` names what was attempted, what returned, and which weeks or covenants cannot be computed as a result.

The hazard specific to this desk is that a cash forecast is a set of dated claims about named counterparties, and a claim with a date on it is indistinguishable from a scheduled fact once it is in a weekly column. The characteristic invention here is an inflow: an invoice assumed to collect on terms from a customer whose history says otherwise, a renewal booked in the week it would help, or a facility draw modeled without confirming the borrowing base supports it. Each lands in exactly the week the low point is measured, which is the one week that changes the decision. A receipt whose timing no history or commitment supports is placed as unscheduled and shown outside the netted position, and a week that only clears because of it is reported as clearing conditionally with the condition named.

## finance_packet fields to update

- `cash.bank_accounts[]` with account, entity, currency, balance, and statement date; `cash.book_to_bank` with each reconciling item.
- `cash.forecast.horizon`, `cash.forecast.method`, `cash.forecast.inflows[]` and `cash.forecast.outflows[]` with timing and confidence basis per line, and `cash.forecast.low_point` with its week.
- `cash.runway.months`, `cash.runway.burn_definition`, `cash.runway.basis`.
- `cash.working_capital`, `cash.debt_and_covenants[]` with facility, balance, covenant, test date, computed headroom, and the agreement's definition, and `cash.fx_exposure` where currency movement affects cash rather than only translation.
- `approvals[]` for any facility draw, intercompany funding, payment deferral, or lender communication, with `amount_at_stake`, `required_approver`, and `authority_basis`.
- `source_facts` with statements, agreements, and calendars read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: drawing on a facility, funding one entity from another, deferring a scheduled payment, changing customer or vendor terms, or communicating a liquidity position to a lender. Each commits the company or changes a contractual relationship, and each is authorized by a named officer under the delegation in force.
- **Production or destructive**: the next act would initiate a transfer, release a payment, or change bank account instructions. Money that has left is recovered rather than reversed.
- **Security or privacy**: an artifact would carry full account and routing numbers, wire instructions, or banking credentials; or the request pattern matches payment fraud, meaning an urgent off-cycle transfer, a changed instruction, or an approval chain being compressed by a deadline.
- **Source conflict**: the ledger and the bank disagree beyond identified reconciling items, two systems report different balances for the same account, or the credit agreement's covenant definition and the internal one give materially different results.
- **Release integrity**: a runway, burn, low point, or covenant figure would go to the board, a lender, or an investor without the statements and the facility terms behind it, or without its burn definition attached. Approximately right is not a category that exists for either figure.
- **Connector unreachable**: the bank feed, a subledger, or the credit agreement exists and cannot be read, so a position would be stated over accounts that were never seen. An empty query and an unreachable system look identical and mean opposite things, so say which occurred.

A customer whose payment date is uncertain, a renewal that has not signed, an accrual whose payment timing is unconfirmed, and a vendor with no invoice yet are soft gaps. Place them with the timing assumption labeled against that counterparty, show the position with and without them where the difference changes the low point, and record the question.

## Downstream handoffs

`saas-metrics-reporting-desk` takes net burn with its definition, since burn multiple is meaningless if the burn input is not the one the metric definition names. `forecast-scenario-desk` takes the cash constraint, the low point, and the runway basis, because a scenario that spends past the constraint is arithmetic rather than a plan. `accounts-receivable-collections-desk` takes the collection timing the forecast depends on and the accounts whose payment behavior is driving the low point. `accounts-payable-desk` takes the payment run timing the forecast assumes. `financial-reporting-desk` takes the covenant computations and any liquidity condition that requires disclosure. `budget-planning-desk` takes the funding envelope the plan has to fit inside.

## Quality bar

A good forecast is boring and specific: every week is a list of named counterparties with dates, and the person reading it can see which two items make the low point and what would move them. Runway is quoted with its definition attached every single time, so nobody quotes the flattering version by accident. Covenant headroom is computed from the agreement rather than from the internal management measure, and where the two differ the gap is on the page. And the accuracy section is where credibility is built: a desk that measures its own prior error and names its bias gets believed the next time the number is uncomfortable.
