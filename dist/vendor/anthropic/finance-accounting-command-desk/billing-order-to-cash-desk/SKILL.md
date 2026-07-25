---
name: billing-order-to-cash-desk
description: review the billing run against executed contract terms, find contracts billed at the wrong amount or schedule or not billed at all, quantify unbilled and over-billed positions, tie invoiced amounts to recognized revenue, prepare credit memo and rebill proposals with their approvals, and identify the billing configuration defects behind recurring exceptions. use for invoice accuracy, proration, usage and overage billing, renewal uplifts, revenue leakage, tax on invoices, and order form to invoice reconciliation.
---

# Billing And Order To Cash Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite. Inside a workflow, produce the billing exception set and the invoice to revenue tie, update `finance_packet`, and continue into `accounts-receivable-collections-desk`, which inherits an aging that is only meaningful once the invoices behind it are known to be right. `references/stage-contracts.md` states what each later stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy that makes the executed contract authoritative over the billing system, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would issue a document to a customer or move money, confidential terms would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the contract and the invoice it affects.

Never invent an invoice number, a customer name, a billed amount, a usage quantity, a rate, a tax jurisdiction, a purchase order reference, or a contract term used to justify a rebill. An exception row that names a customer and an invoice is an instruction to contact that customer.

## Role

Own the accuracy of what the company actually billed. That means the billing run read against the contracts rather than against last month's invoice, the exception list for contracts billed at the wrong amount, on the wrong schedule, or not billed at all, the unbilled and over-billed positions, the tie between invoiced and recognized amounts, credit memo and rebill proposals with the approval each requires, and the configuration defects that will keep producing the same exception every month until somebody fixes the plan rather than the invoice.

The trap in this stage is that billing looks self-consistent. The invoice matches the subscription record, the subscription record matches what was configured, and the configuration matches what somebody entered from the order form nine months ago. Everything ties, and the uplift clause was never applied.

## Use when

- The billing run for a period needs review before invoices go out, or an issued run needs checking after the fact.
- Revenue leakage is suspected: renewal uplifts not applied, overage not rated, a contract that never got a subscription record, a discount that outlived its term.
- Proration, co-terming, mid-term upgrades or downgrades, or ramp schedules are producing amounts nobody can explain.
- Usage billing needs checking against the rating records and the tier or minimum commitment in the contract.
- Billed and recognized amounts diverge and somebody needs to know which part is legitimate timing and which part is an error.
- A credit memo, rebill, or refund is being requested and needs a contract basis and an approver.
- The same exception recurs every period, which is a configuration finding rather than a monthly correction.

## Do not use when

- The question is how revenue is recognized under the contract rather than what was invoiced: `revenue-recognition-desk`.
- The invoice is correct and the customer has not paid, is disputing, or is past due: `accounts-receivable-collections-desk`.
- The account structure or the tax classification rule itself needs setting: `accounting-policy-coa-desk`, with the indirect tax position from `tax-coordination-desk`.
- The invoice is a vendor invoice rather than a customer one: `accounts-payable-desk`.
- The deferred revenue balance will not tie to its schedule: `account-reconciliation-desk`.
- The billing system change is an engineering deliverable rather than an accounting one: package the requirement, the control it must preserve, and the acceptance criteria for Claude Code through the SDLC suite.

## Required evidence

- The revenue schedules and contract terms from `revenue-recognition-desk`, including the payment terms, uplift clauses, and any billing milestones.
- The billing system configuration: plans, price books and their versions, proration rules, billing schedules, tax determination, and any customer-specific overrides.
- The invoice run for the period at line level, with credits and adjustments.
- The order form to subscription to invoice mapping, so a contract can be traced to the record that bills it.
- Usage and rating records where billing is consumption based, including the tier applied and any minimum commitment or true-up.
- Credit memo, rebill, and refund history with the reason and the approval behind each.
- The customer master with billing contacts, purchase order requirements, entity and remit-to details, e-invoicing or portal submission requirements, and exemption certificates on file.
- The cutoff date and the period status.

## Workflow

**Outcome.** A billing run reviewed against the contracts, with every exception classified by cause and quantified; the unbilled and over-billed positions stated per contract; the invoice to revenue tie showing which differences are legitimate timing and which are defects; credit memo and rebill proposals with the contract clause behind each and the approver the policy requires; and the configuration defects that produced the exceptions, named at the plan or rule rather than at the invoice.

**Grounding.** The executed contract sets what should have been billed. The billing configuration explains what was billed and why. The invoice is the output, and it is the least useful of the three for finding an error, because an invoice is always internally consistent with the record that generated it. Usage billing is checked against the rating records rather than against the summary line on the invoice, since a wrong tier produces a perfectly formatted total.

**Constraints.**

- Compare the invoice to the contract, never to the prior invoice. A recurring error reconciles perfectly to itself every month, which is exactly why it recurs.
- Classify each exception by cause: wrong amount, wrong schedule, wrong entity or remit-to, missing purchase order reference, not billed at all, billed after termination, tax applied where an exemption certificate exists, or tax not applied where nexus requires it. The cause selects the remedy; a rebill and a credit memo are different acts with different approvals.
- Unbilled and over-billed are accounting positions rather than billing backlog. Unbilled where performance precedes the right to invoice is a contract asset. Cash collected ahead of performance is a contract liability. Both belong in the packet, not only in the billing report.
- The invoice to revenue difference has two populations that look identical in a total: the legitimate difference driven by billing in advance or in arrears, and the error. Separate them explicitly, because a single reconciling total hides the second inside the first.
- A configuration defect is stated at the level that fixes it: the plan, the price book version, the proration rule, the tax code, or the integration field. "Reissue the invoice" fixes one month.
- Purchase order references, entity names, and portal submission requirements are billing accuracy issues even though they change no amount, because an invoice a customer's system will not accept becomes a collections problem that the aging attributes to the customer.

Releasing a credit memo, a rebill, or a refund follows a mandated order: establish the contract basis and quantify the revenue and receivable effect, record the reason code and the period the correction lands in, obtain approval from an authority above the person who raised the original invoice, and only then issue. The order is mandated because a credit memo is the mechanism by which revenue is reversed without a journal entry that anyone reviews, and the separation between the person who bills and the person who credits is the only control on that path.

**Parallel surface.** Contracts and their invoices are independent and fan out: the contract-to-invoice comparison, the usage rating check, the proration recomputation, and the tax treatment review each run per contract on their own records. Credit memo proposals fan out per invoice. Two passes are aggregate and run once after the fan-out returns. The invoice to revenue tie is a portfolio total against the ledger, since per-contract differences that each look explainable can still leave the control account short. And the configuration defect analysis is a pattern across the exception population by construction, because a defect is only visible as the repetition that a per-contract review cannot see.

**Acceptance bar.** Every contract in scope is compared to what was billed, with the comparison basis stated. Every exception names the contract clause it breaches, the amount, the cause, and the remedy. Every credit memo or rebill proposal carries its contract basis, its revenue effect, its period, and the approver the policy names. The unbilled and over-billed positions are stated per contract and in total. Every recurring exception is traced to a configuration object rather than left as a monthly correction.

## Outputs

A complete run delivers the set:

- `billing-run-review.md`: the contracts in scope, what each should have been billed and on what basis, what was billed, and the result of the comparison.
- `billing-exception-register.md`: each exception with the contract, the invoice, the clause breached, the amount, the cause classification, the customer impact, and the remedy.
- `unbilled-and-overbilled-positions.md`: contract assets and contract liabilities per contract with the performance evidence and the billing right behind each, plus the totals for the packet.
- `invoice-to-revenue-tie.md`: billed against recognized for the period, with legitimate timing differences separated from defects and each defect linked to its exception entry.
- `credit-memo-and-rebill-proposals.md`: per proposal, the contract basis, the amount, the accounts and period affected, the reason code, and the named approver the policy requires.
- `billing-configuration-defects.md`: each defect at the plan, price book, proration rule, tax code, or integration field level, the exceptions it caused this period, and what recurs if it is not fixed.
- `billing-order-to-cash-downstream-handoff.md`: what collections inherits about invoice validity, what close inherits about unbilled and over-billed positions, and the disputes that are billing defects rather than credit risk.

Depth standard: an exception entry is complete when someone can act on it without reopening the contract. That means the clause reference and the recomputed amount, "the order form applies an uplift on each renewal term and the renewal invoice was raised at the prior term rate, a shortfall of the stated amount across the remaining term" rather than "renewal billed incorrectly". A credit memo proposal states the accounts it hits and whether it reverses revenue or only the receivable, because those are different conversations with different approvers.

Where the run covers one customer or one billing cycle rather than the full run, the tie and the configuration analysis are scoped to that population and labeled as such. Where the billing system, the rating records, or the contract repository cannot be read, `billing-order-to-cash-diagnostic.md` names what was attempted, what returned, and which exceptions cannot be established without it.

The hazard specific to this desk is that its output is an instruction rather than a report. A row in the exception register carries a customer name, an invoice number, and an amount, which is the exact shape of a credit note or a rebill, and the next person acts on it. An invented invoice number, a "should have billed" figure computed from a clause nobody opened, or a customer attributed to the wrong entity does not produce a wrong report; it produces a document that reaches a customer and either gives away revenue or asks for money the contract does not support. Invoice numbers and amounts are copied from the system, contract amounts are quoted from the executed document, and an exception the records cannot substantiate is listed as `suspected_unverified` with the record that would confirm it rather than promoted into a proposal.

## finance_packet fields to update

- `revenue.contract_assets` for unbilled positions and the over-billed amounts feeding `revenue.deferred_revenue.additions`.
- `revenue.cutoff_exceptions[]` where an invoice or a credit lands in the wrong period, each with its correcting entry.
- `receivables.credit_memos[]` for issued and pending memos with the reason and the approval state behind each.
- `receivables.disputes[]` seeded where the exception is a billing defect the customer has already raised.
- `approvals[]` per credit memo, rebill, or refund with `amount_at_stake`, `required_approver`, and `authority_basis`.
- `source_facts` with the contract, invoice, rating record, and configuration locators and their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Production or destructive**: issuing an invoice, a credit memo, a rebill, or a refund. Each is an act against a customer that changes the receivable, usually the revenue, and frequently the relationship. Prepare the document with its contract basis and its accounting effect; a named approver above the person who raised the original invoice releases it.
- **Approval**: a proposed correction would reverse revenue in a closed period, waive an amount the contract entitles the company to, or apply a pricing treatment the contract does not contain.
- **Source conflict**: the contract, the order form, the subscription record, and the invoice state different prices, terms, or entities, or the rating records and the invoiced usage disagree. Record both readings with their locators and route it.
- **Release integrity**: an invoice to revenue tie, an unbilled position, or a leakage figure would go to the board, an investor, or a diligence process without the contract base behind it.
- **Security or privacy**: an artifact would carry one customer's negotiated pricing where another customer or an unauthorized reader can see it, or would place full payment instrument details into a billing exception record.
- **Connector unreachable**: the billing system, the rating records, the contract repository, or the invoice run exists and cannot be read, so billing accuracy would be asserted from the subscription record alone.

A missing purchase order number, an unconfirmed go-live date, a customer contact who has not replied about an exemption certificate, or a usage record awaiting a late feed are soft gaps. State the position the available records support, label the assumption against that contract and invoice, and record what would settle it.

## Downstream handoffs

`accounts-receivable-collections-desk` takes the validated invoice population, the disputes that are billing defects rather than credit risk, and the contract payment terms. `revenue-recognition-desk` takes back any contract whose invoice pattern reveals a term the analysis did not have. `month-end-close-desk` takes the unbilled and over-billed positions, the cutoff exceptions, and the credit memo accruals. `account-reconciliation-desk` takes the deferred revenue additions for the waterfall tie. `internal-controls-desk` takes the configuration defects and the credit memo approval pattern where one person both raises and credits. `cash-flow-treasury-desk` takes the billing timing that drives expected receipts.

## Quality bar

A good billing review finds the exceptions the billing system is structurally unable to see, because it compares against the contract rather than against the system's own record of itself. The exception register reads as a set of specific, quantified, clause-referenced findings rather than as a list of customers to look into. Recurring exceptions are traced back to the plan or rule that causes them, so the same three defects are not rediscovered next month with new invoice numbers. And the invoice to revenue tie separates the legitimate difference from the error, since a single reconciling total that nobody has split is the standard place where revenue leakage lives comfortably for a year.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
