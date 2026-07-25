---
name: accounts-receivable-collections-desk
description: produce the receivable aging tied to its control account, days sales outstanding with the formula stated, dispute triage separating billing defects from delivery problems from credit risk, a collections plan with an action owner and date per account, the expected credit loss allowance with its methodology and roll-forward, and write-off candidates with their evidence and approvals. use for aging analysis, dso, collections and escalation, credit holds and limits, cash application exceptions, unapplied cash, short pays, and bad debt reserve.
---

# Accounts Receivable And Collections Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite. Inside a workflow, produce the aging, the collections plan, and the allowance, update `finance_packet`, and continue into `spend-approval-authority-desk` on the main chain and into `cash-flow-treasury-desk` for the collection timing the forecast depends on. `references/stage-contracts.md` states what each stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would give away money or contact a customer under a false premise, confidential information would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the customer, invoice, or aging bucket it affects.

Never invent a customer name, an invoice number, a balance, a payment term, a contact, a promise to pay, a dispute reason, a bankruptcy filing, or an allowance rate. A collections plan is read as a script by the person who makes the call.

## Role

Own the receivable position and what is being done about it. That means the aging tied to its general ledger control account, days sales outstanding with the formula written down, the exposure ranking by balance and by days past due, dispute triage that separates a billing defect from a delivery problem from a customer who is simply not paying, the collections plan with an action, an owner, and a date per account, cash application exceptions including unapplied receipts and short payments, the expected credit loss allowance with its methodology and its roll-forward, and write-off candidates with the evidence and the approval each requires.

The recurring mistake here is treating the aging as a measure of customer behaviour. A large share of what sits past ninety days is the company's own doing: an invoice with no purchase order number that a customer's payables portal rejected, a credit that was promised and never issued, a payment applied to the wrong invoice, or an invoice sent to the entity that does not pay.

## Use when

- An aging needs producing, tying to the ledger, or explaining, or days sales outstanding has moved and nobody agrees why.
- Collections need a plan: who calls whom, about which invoices, by when, and with what escalation.
- Disputes need triage and routing, or a customer is withholding payment against a claim.
- Cash application has exceptions: unapplied receipts, short payments, deductions, or payments that cannot be matched to a remittance.
- The expected credit loss allowance needs computing, refreshing, or defending, or the roll-forward does not explain the movement.
- Write-off candidates need assembling with evidence, or somebody proposes writing off an aged balance to improve the aging.
- Concentration risk needs quantifying because a small number of customers carry most of the balance.

## Do not use when

- The invoice itself is wrong, or the exception is a billing configuration defect: `billing-order-to-cash-desk`, and route the dispute back there rather than dunning against a bad invoice.
- The question is when revenue is recognized rather than when cash arrives: `revenue-recognition-desk`.
- The receivable control account will not tie to the subledger: `account-reconciliation-desk` owns the tie once the difference is the subject.
- The ask is a cash forecast, a collection timing curve, or runway: `cash-flow-treasury-desk`.
- The receivable is a vendor debit balance or a supplier credit: `accounts-payable-desk`.
- Credit terms are becoming a commercial negotiation about winning or keeping the account: state the accounting and exposure consequence here and route the commercial decision to the Sales and Revenue suite.

## Required evidence

- The receivable subledger at invoice level with payment application, and the aging as of the reporting date.
- The general ledger control account balance for receivables at the same as-of timestamp.
- Payment terms from the executed contracts rather than from the invoice template, including any negotiated extension.
- Cash application records, remittance advices, unapplied cash, short payments, and deductions.
- Dispute and support ticket history with the reason and the current owner.
- The credit policy, any credit limits and holds in force, and the customer's credit history.
- The allowance methodology, prior write-offs and recoveries, and the current allowance balance and its roll-forward.
- The collections owner per account and the escalation path the contract permits.

## Workflow

**Outcome.** An aging that ties to its control account and states its aging convention, days sales outstanding computed with the formula written out, an exposure ranking, dispute triage with each dispute classified and routed, a collections plan with a named action, owner, and date per account in scope, cash application exceptions listed individually, an allowance computed from a stated methodology with a roll-forward that explains every movement, and write-off candidates with their evidence of uncollectibility and the approval each requires.

**Grounding.** The subledger is authoritative for invoice-level detail and the ledger for the balance, so the tie is stated rather than assumed and any difference is reported at full amount. Payment terms come from the contract. A dispute is what the customer actually said, with its record, rather than what the collections note inferred. Uncollectibility is evidenced by something external: a filing, an agency return, a failed payment plan, or a period of no contact against a documented attempt history.

**Constraints.**

- State the aging convention. Aging from invoice date and aging from due date give different pictures of the same portfolio, and a portfolio on net sixty terms aged from invoice date looks a month worse than it is.
- State the days sales outstanding formula in full, including the revenue base and the number of days. The simple ratio and the countback method give different answers on the same data, and a period-over-period comparison across a formula change measures the formula.
- Triage before dunning. A disputed invoice, an unapplied payment, and a genuine non-payer need three different actions, and sending the third action to the first customer costs the relationship and does not collect the invoice.
- A collections action names the invoice, not the customer balance. "Follow up with the account" is a reminder; "obtain the purchase order reference the portal rejected on these invoices, resubmit, and confirm receipt by the stated date" is an action.
- Escalation follows the contract's remedies. Suspension, late interest, and acceleration exist where the agreement provides them, and a generic dunning ladder that threatens a remedy the contract does not contain is not a credible position.
- The allowance is a method applied consistently, whether a loss rate matrix by aging bucket adjusted for forward-looking factors, a specific reserve on identified accounts, or both. An allowance that lands on the prior period percentage is a rate carried forward rather than a computation.
- Write-offs remove an asset and close the file. They do not improve collections, and a period where the aging improved because old balances were written off is reported as exactly that.

Writing off a receivable follows a mandated order: assemble the evidence of uncollectibility with the collection attempts already made, confirm the allowance already carries the exposure so the write-off does not hit the income statement twice, obtain approval from the authority the policy names for that amount, and only then remove the balance and close the file. The order is mandated because the write-off is irreversible in practice, ends collection activity, and is the fastest available way to make an aging look healthy without collecting anything.

**Parallel surface.** Customer accounts are independent and fan out: the exposure assessment, dispute triage, collection action design, cash application exception research, and write-off evidence assembly each run per account on that account's records. Disputes fan out per invoice. Three passes are aggregate and run once after the fan-out returns. The tie to the control account is a single comparison over the whole subledger. Days sales outstanding is a portfolio measure with one revenue base. The allowance is computed over the whole population, because a loss rate is a property of the portfolio and a per-account reserve assembled independently will neither total to a defensible rate nor pick up concentration.

**Acceptance bar.** The aging ties to the control account, or the difference is stated at full amount with its age. Days sales outstanding shows its formula and its inputs. Every dispute is classified by cause and has an owner. Every account in the collections plan has an action, an owner, a date, and the invoices it covers. The allowance states its methodology and its roll-forward opens, provisions, writes off, recovers, and closes to the recorded balance. Every write-off candidate names its evidence and its approver.

## Outputs

A complete run delivers the set:

- `receivable-aging.md`: buckets with balances, the aging convention stated, the tie to the control account, concentration by customer, and the movement against the prior period.
- `dso-and-exposure-analysis.md`: days sales outstanding with the formula and inputs written out, the trend on a consistent formula, and the exposure ranking by balance and by days past due.
- `dispute-register.md`: each dispute with the invoice, the amount, what the customer actually claimed, the classification as billing defect, delivery issue, or credit risk, the owner, and the routing.
- `collections-plan.md`: per account, the invoices in scope, the action, the owner, the date, the escalation step available under the contract, and the prior contact history.
- `cash-application-exceptions.md`: unapplied receipts, short payments, and deductions listed individually with the amount, the age, and what would resolve each.
- `allowance-and-roll-forward.md`: the methodology, the computation with its inputs, the loss rates by bucket or the specific reserves, and the roll-forward from opening to closing.
- `write-off-candidates.md`: per candidate, the balance, the age, the collection attempts made, the evidence of uncollectibility, the allowance already carried, and the approver the policy names.
- `accounts-receivable-collections-downstream-handoff.md`: the collection timing for the forecast, the billing defects routed back, and the credit exposures the commercial team owns.

Depth standard: an entry is complete when the person who owns the action can perform it without opening another system. A collections line carries the invoice numbers and the amount, the reason this account is unpaid as far as the record establishes it, and the specific next step. An allowance entry shows the rate, the base it applies to, and where the rate came from.

Where the run covers one customer or one bucket rather than the portfolio, the allowance and the days sales outstanding computation are scoped and labeled as such rather than presented as the portfolio position. Where the subledger, the cash application records, or the ledger control account cannot be read, `accounts-receivable-collections-diagnostic.md` names what was attempted and which figures are unavailable without it.

The hazard specific to this desk is that its main artifact is a call list. A collections plan naming a customer, a contact, a promised payment date, and a disputed amount goes straight into a conversation with a real person who will correct any detail that is wrong and will remember that finance got it wrong. A promise to pay that no record contains, a contact recalled rather than looked up, or a dispute reason inferred from the age of the invoice all damage the position they were meant to support. Contacts and promises are taken from the record with their date, an account with no contact history is marked `no_documented_contact`, and the allowance rate is computed rather than set to the number that keeps the provision flat.

## finance_packet fields to update

- `receivables.aging_buckets[]` with balances and the convention, and the tie state to the control account.
- `receivables.dso` with the formula used, `receivables.top_exposures[]` by balance and by days past due.
- `receivables.disputes[]` with invoice, amount, reason, classification, and owner; `receivables.credit_memos[]` where a dispute resolves into one.
- `receivables.allowance.method`, `receivables.allowance.balance`, `receivables.allowance.roll_forward`.
- `receivables.collections_actions[]` with customer, action, owner, date, and outcome; `receivables.write_off_candidates[]` with evidence and required approval.
- `approvals[]` for each write-off, payment plan, credit hold release, or terms change, with `amount_at_stake` and `authority_basis`.
- `source_facts` with subledger, ledger, and cash application locators and as-of timestamps, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: writing off a receivable, granting an extended payment plan, releasing a credit hold, changing a customer's payment terms, or waiving contractual late interest. Each gives away money or risk at an authority level the credit policy assigns to a named person, and the write-off is the one that matters most because it removes an asset and ends the file.
- **Production or destructive**: the next act would post the allowance or the write-off entry, apply cash in the subledger, suspend a customer's service, or send a demand or a referral to a collection agency.
- **Source conflict**: the subledger does not tie to the control account, the contract and the invoice state different payment terms, or the cash application record and the customer's remittance advice disagree on what was paid against what. Record both readings and route it.
- **Release integrity**: an aging, a days sales outstanding figure, or an allowance would go to the board, a lender, or a diligence process without the subledger tie and the methodology behind it. A receivable balance is a borrowing base input in many facilities, which changes what an approximate figure costs.
- **Security or privacy**: an artifact would carry a customer's bank details, full payment instrument data, or another customer's negotiated terms, or would circulate a customer's financial distress outside the group that needs it.
- **Connector unreachable**: the receivable subledger, the cash application records, or the ledger exists and cannot be read, so an aging would be assembled from a report whose as-of date nobody can establish.

An unreturned collections call, a customer contact who has changed roles, a dispute whose supporting ticket is thin, and a forward-looking factor for the allowance that has to be judged are soft gaps. State the position the records support, label the assumption against that account, and record what would settle it.

## Downstream handoffs

`cash-flow-treasury-desk` takes expected collection timing per account with its confidence basis, which is the single largest input to a direct forecast. `billing-order-to-cash-desk` takes back every dispute classified as a billing defect, with the invoice and the clause. `month-end-close-desk` takes the allowance entry with its computation and the write-off entries with their approvals. `account-reconciliation-desk` takes the aging as the supporting schedule for the receivable control account. `financial-reporting-desk` takes the concentration and credit risk disclosure inputs. `internal-controls-desk` takes any pattern where one person applies cash, raises credits, and approves write-offs.

## Quality bar

A good collections package tells the truth about why the money has not arrived, and that truth is frequently uncomfortable for finance rather than for the customer. Disputes are separated from delinquency, unapplied cash is cleared before anyone is chased for it, and the plan names invoices and dates rather than sentiments. The allowance is a computation somebody could reproduce, with a rate that moves when the portfolio moves. And the aging carries its convention and its tie, because two people comparing agings built on different conventions will argue for an hour about a portfolio they both understand correctly.
