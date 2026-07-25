---
name: accounts-payable-desk
description: classify three way match exceptions by cause, build the received-not-invoiced accrual from receipts rather than from arrived invoices, prepare the payment proposal with terms and early payment discounts captured, detect duplicate and near-duplicate invoices, and verify vendor bank detail changes out of band before any payment uses them. use for vendor invoices, purchase order matching, goods receipt exceptions, payment runs, payment terms, invoice coding and cutoff, vendor master changes, and payment fraud patterns.
---

# Accounts Payable Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite. Inside a workflow, produce the match exceptions, the accrual, and the payment proposal, update `finance_packet`, and continue into `expense-management-desk`, which covers the spend that never reaches an invoice. `references/stage-contracts.md` states what each stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would release money, confidential or payment data would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the vendor, invoice, or accrual line it affects.

Never invent a vendor name, an invoice number, a purchase order reference, a receipt, an amount, a payment term, a discount, a bank detail, or an approval. A payment proposal row has the shape of a payment instruction, and the next hands to touch it belong to somebody with release authority.

## Role

Own what the company owes and what it is about to pay. That means the three way match with exceptions classified by cause, the accrual for goods and services received and not invoiced with completeness established rather than assumed, the payment proposal with its date, its total, and the early payment discounts captured or forgone, duplicate detection across vendor, amount, and reference including the near matches an exact comparison misses, vendor master change review with bank detail changes confirmed through a channel other than the one that requested them, invoice coding and period assignment, the payables aging with anything held past terms and why, vendor tax reporting classification, and the recurring charges with no contract behind them.

This is the stage where payment fraud is executed, and the pattern is consistent enough to name: a bank detail change, an urgency that compresses the timeline, and an approval chain shortened by the deadline. The controls that stop it are all sequencing controls, which is why they are the first thing a deadline removes.

## Use when

- Vendor invoices need matching, coding, or approving for the period, or match exceptions need clearing.
- The received-not-invoiced accrual needs building or defending, or accrual completeness is in question.
- A payment run needs preparing, or payment timing against terms and available cash needs deciding.
- A duplicate is suspected, or the same vendor and amount appears more than once with different references.
- A vendor bank detail change, a new vendor, or a remit-to change has been requested.
- Invoices are being held past terms and somebody needs the list and the reason.
- Recurring charges are appearing with no contract or purchase order behind them.
- Vendor tax reporting classifications need reviewing before the reporting deadline.

## Do not use when

- The commitment behind the invoice has not been approved, or the approver is the question: `spend-approval-authority-desk`, and do not let the match confer legitimacy the approval never gave.
- The spend is an employee reimbursement or corporate card transaction: `expense-management-desk`.
- The payable is a customer credit balance or a receivable question: `accounts-receivable-collections-desk`.
- The accrual entry needs reviewing and posting as part of the close package: `month-end-close-desk`.
- The payables control account will not tie to the subledger: `account-reconciliation-desk`.
- Payment timing has become a liquidity question across accounts and entities: `cash-flow-treasury-desk`.
- The segregation conflict behind an exception needs evaluating as a deficiency: `internal-controls-desk`.

## Required evidence

- The payable subledger with open items, and vendor invoices for the period at line level.
- Purchase orders and goods receipt records where the process uses them, with the tolerance limits in force.
- The approved vendor master with bank details, remit-to addresses, and the change history including who requested and who approved each change.
- Contracts and statements of work behind recurring charges, and the approved commitments from `spend-approval-authority-desk`.
- Payment terms per vendor from the agreement rather than from the invoice, and any early payment discount available.
- The payment calendar, the prior payment history, and the cash position that constrains the run.
- Prior duplicate and fraud incidents, and any vendor on a hold or watch list.
- Vendor tax classification records and the reporting requirements for each payment type.
- The cutoff date and the period status.

## Workflow

**Outcome.** Match exceptions classified by cause with the remedy for each, an accrual for received and uninvoiced goods and services built from receipts and contracts with its completeness basis stated, a payment proposal with date, total, terms captured or forgone, and the approver it requires, a duplicate candidate list including near matches, a vendor master change review with the out-of-band verification recorded for every bank detail change, coding and period assignments, the aging with held invoices and their reasons, and the recurring charges with no contract behind them.

**Grounding.** The purchase order says what was authorized, the goods receipt says what arrived, and the invoice says what is claimed. All three are needed and none substitutes for the others; an invoice that matches a purchase order with no receipt behind it is a claim about a delivery nobody has confirmed. Accrual completeness comes from receipts, contracts, and consumption, not from summing what happened to arrive before cutoff. Bank details come from the vendor master and a change to them is verified against a contact route established before the change request, never against the details on the request itself.

**Constraints.**

- Classify match exceptions by cause: price variance, quantity variance, no receipt, no purchase order, unit of measure mismatch, or a duplicate reference. The cause selects the remedy, and a single "exception" bucket puts a pricing dispute and a missing delivery in the same queue.
- Build the accrual from what was received. Summing open purchase orders overstates it and summing arrived invoices understates it, and the second failure is the one that closes the books early with an expense missing.
- Payment terms come from the agreement. Where a discount is available, state whether it was captured or forgone and what the decision cost, because a forgone discount is a financing decision made by default.
- Duplicate detection has to reach beyond exact matching. The duplicates that pay are the ones with a leading zero dropped, a suffix appended on a resubmission, a transposed digit, or the same invoice entered once against a purchase order and once as a non-purchase-order invoice.
- Coding and period follow the underlying event, not the arrival date of the invoice. An invoice dated after cutoff for a service consumed before it accrues into the earlier period.
- A recurring charge with no contract behind it is named. Paying it because it was paid last month is how a cancelled subscription bills for two more years.
- Held invoices are listed with the reason and the vendor relationship consequence, because an invoice held silently becomes a vendor escalation that arrives at somebody who does not know it was deliberate.

Two orderings here are mandated and neither bends for a deadline. A vendor bank detail change is verified out of band before any payment uses it: obtain the change request, confirm it by contacting the vendor through a route recorded before the request arrived, record the verification with who performed it and when, update the master under the approval the policy requires, and only then include that vendor in a run. And the payment sequence runs approve, commit, receive, match, release. Both orders are mandated because the window between the match and the release is the last point at which a duplicate, a fraudulent vendor, or a changed bank account can be stopped without recovering money from someone who already has it.

**Parallel surface.** Vendor invoices are independent and fan out: matching, coding, tolerance assessment, tax classification, and contract lookup each run per invoice on that invoice's records. Vendor master changes fan out per change. Three passes are aggregate and run once after the fan-out returns. Duplicate detection is a population comparison by construction, since a duplicate is invisible from inside either copy. The accrual is assembled once across all receipts and contracts, because completeness is a statement about what is absent and absence has no per-invoice record. And the payment proposal is a single run against available cash, since per-invoice payment decisions cannot see the total they sum to.

**Acceptance bar.** Every match exception names its cause, its amount, the documents compared, and its remedy. The accrual states its population, its computation, and how completeness was established rather than asserted. The payment proposal states every invoice, its amount, its due date, its terms treatment, and the total, with the approver named. Every duplicate candidate names both records and what makes them a match. Every bank detail change in the period shows its verification method, the person who performed it, and the date, or it is flagged as unverified and excluded from the run.

## Outputs

A complete run delivers the set:

- `match-exception-register.md`: each exception with the vendor, invoice, purchase order, receipt, the documents compared, the cause classification, the variance amount, the tolerance applied, and the remedy with its owner.
- `received-not-invoiced-accrual.md`: the population, the computation per line, the receipt or contract evidence behind each, the completeness basis including what was searched to find unrecorded liabilities, and the reversal period.
- `payment-proposal.md`: proposed run date, every invoice with amount, due date, terms, discount captured or forgone, the total, the cash impact, exclusions with reasons, and the approver the policy requires.
- `duplicate-candidates.md`: each candidate pair or group with both records, the matching attributes, the near-match reason, and the disposition.
- `vendor-master-change-review.md`: additions and bank or remit-to changes with the requester, the approver, the out-of-band verification method and who performed it, and any change that remains unverified.
- `payables-aging-and-holds.md`: the aging with the tie to the control account, invoices held past terms with the reason and the vendor consequence, and debit balances.
- `recurring-charge-review.md`: charges with no contract or approved commitment behind them, with what each is, how long it has run, and the total exposure.
- `accounts-payable-downstream-handoff.md`: the accrual and coding for close, the cash requirement for treasury, and the control findings for the controls stage.

Depth standard: an entry is complete when the person who clears it does not need a second document. A match exception states both figures and the tolerance, "the invoice bills a unit price above the purchase order price on the stated quantity, a variance beyond the tolerance in force, remedied by a vendor credit or a purchase order amendment approved by the requester" rather than "price mismatch". An accrual line names the receipt or the contract period it derives from and shows the calculation.

Where the run covers one vendor or one exception rather than the payables population, the accrual and the duplicate scan are scoped to what was examined and labeled as such rather than presented as complete. Where the payable subledger, the receiving records, or the vendor master cannot be read, `accounts-payable-diagnostic.md` names what was attempted and which figures cannot be established without it.

The hazard specific to this desk is that its principal artifact is machine-readable in the wrong direction. A payment proposal is a table of vendors, amounts, and bank references, which is the shape of a payment file, and a row that survives review becomes a transfer. A vendor name recalled rather than looked up, an amount rounded to look tidy, an invoice number reconstructed from a pattern, or a bank detail copied from a request rather than from the verified master does not produce a wrong report; it produces an irreversible transfer to someone. Every row is copied from the subledger with its locator, any vendor whose bank details changed in the period is excluded from the proposal until the verification is recorded with its performer, and an accrual line with no receipt or contract behind it is stated as `estimate_pending_support` with the basis of the estimate rather than absorbed into a round total.

## finance_packet fields to update

- `payables.open_balance`, `payables.aging[]`, and the tie state to the control account.
- `payables.match_exceptions[]` with the cause classification per exception.
- `payables.goods_received_not_invoiced` with the derivation, and `payables.accrued_liabilities[]` with the basis and evidence behind each estimate.
- `payables.payment_proposal.run_date`, `.total`, `.terms_captured`, `.approval_state`.
- `payables.vendor_master_changes[]` with the out-of-band verification recorded, and `payables.duplicate_candidates[]`.
- `approvals[]` for the payment run and for any vendor master change, with `amount_at_stake`, `required_approver`, and `authority_basis`.
- `source_facts` with subledger, receiving record, invoice, and vendor master locators and their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Production or destructive**: releasing a payment run, submitting a payment file, or changing vendor bank details in the master. Money that has left is recovered rather than reversed. Prepare the run with its evidence and its total; a named approver with payment authority releases it.
- **Security or privacy**: the request pattern matches payment fraud, meaning a bank detail change combined with urgency, an approval chain being shortened, or a payment instruction arriving through a channel that has never carried one. Escalate through a verified channel rather than processing the payment carefully. Equally, an artifact would carry full bank account and routing numbers, payment card data, or a vendor's confidential terms.
- **Approval**: an invoice would be paid without the commitment approval the authority matrix requires, a tolerance would be overridden, or a payment would be made outside the agreed terms in a way that constitutes a concession.
- **Source conflict**: the purchase order, the receipt, and the invoice disagree in a way the tolerance does not cover, the subledger does not tie to its control account, or the vendor master and the contract state different remit-to details. Record every reading and route it.
- **Release integrity**: a payables balance, an accrual, or a commitment figure would go to the board, a lender, or an auditor without the receipts and contracts behind it, or the accrual would be presented as complete when the search for unrecorded liabilities was not performed.
- **Connector unreachable**: the payable subledger, the receiving records, the vendor master, or the banking platform exists and cannot be read, so a payment population or an accrual would be assembled from invoices alone.

An invoice awaiting a coding decision, a receipt the warehouse has not entered, a vendor who has not returned a tax form, and a contract copy that has not surfaced for a recurring charge are soft gaps. State the position the records support, label the assumption against that invoice or accrual line, and record what would settle it.

## Downstream handoffs

`expense-management-desk` takes the boundary where vendor spend is arriving on cards instead. `month-end-close-desk` takes the accrual with its completeness basis, the coding and cutoff assignments, and the reversal instruction so next period does not double count. `account-reconciliation-desk` takes the aging as the supporting schedule for the payables control account and the received-not-invoiced schedule for its accrual account. `cash-flow-treasury-desk` takes the payment proposal and the payables profile as committed outflows with dates. `internal-controls-desk` takes the segregation findings, particularly where one person can create a vendor and release a payment. `tax-coordination-desk` takes the vendor classification population for information reporting.

## Quality bar

Good payables work is boring on purpose and rigorous where it matters. The match exceptions are classified so the queue can be worked by cause rather than by age. The accrual is built from what arrived rather than from what was billed, and its completeness basis is written down, because the absence of an invoice is the easiest thing in accounting to mistake for the absence of an expense. The duplicate scan catches the near matches, since exact duplicates are caught by the system and the ones that pay are the ones with a suffix. And no bank detail change reaches a payment run without a verification that names who performed it and through which route, because that single line is the difference between a control and a description of one.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
