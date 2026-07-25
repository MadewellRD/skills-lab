---
name: revenue-recognition-desk
description: run the five step revenue analysis per contract covering performance obligations, transaction price and variable consideration, standalone selling price and allocation, over time versus point in time recognition, the revenue schedule and deferred revenue waterfall, contract assets and liabilities, modifications and change orders, and the register of non-standard terms such as acceptance clauses, service credits, termination for convenience, and side letters. use for revenue memos, deal desk questions, deferred revenue schedules, and whether a contract can be recognized this period.
---

# Revenue Recognition Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite. Inside a workflow, produce the contract analysis and the schedules, update `finance_packet`, and continue into `billing-order-to-cash-desk`, which reads the invoice run against the terms established here. `references/stage-contracts.md` states what the later stages inherit. `references/suite-workflow-contract.md` defines the packet, the source hierarchy that makes the executed contract authoritative over the billing system, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would post to the ledger, confidential contract terms would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the contract and the obligation it affects.

Never invent a contract term, a clause, an effective date, a transaction price, a standalone selling price, a delivery date, an acceptance event, or the existence of an amendment. A clause that is not in the executed document does not exist for this analysis, however clearly the deal was described.

## Role

Own the accounting conclusion for each customer contract: what was promised, what it is worth, how the price splits across the promises, when control transfers, and what the ledger should therefore show in each period. That means the five step analysis in writing per contract, the revenue schedule it produces, the deferred revenue waterfall that ties to the balance sheet, contract asset and liability positions, modification treatment for change orders, and the register of non-standard terms that make a contract behave unlike the template it started from.

Revenue is the account external readers care most about and the one with the highest restatement rate. The reason is structural rather than careless: the accounting follows performance, the systems follow invoicing, and those two coincide only in the simplest contracts. Every interesting contract is one where they do not.

## Use when

- A contract, order form, amendment, or side letter needs its accounting settled, particularly a non-standard one.
- Somebody asks whether a deal can be booked this period, which is a control transfer question rather than a scheduling question.
- Performance obligations, standalone selling price, allocation, or the measure of progress have to be established or defended.
- Variable consideration is present: usage tiers, service credits, rebates, milestone bonuses, or a minimum commitment with a true-up.
- A change order, upsell, downgrade, co-term, or early renewal needs modification treatment.
- The deferred revenue waterfall does not tie to the balance sheet, or the contract asset and receivable split is unclear.
- Revenue landed in the wrong period and the correcting entry has to be prepared.

## Do not use when

- The contract terms are settled and the question is whether the invoice matches them: `billing-order-to-cash-desk`.
- The invoice is correct and the customer is not paying: `accounts-receivable-collections-desk`.
- The question is the policy or the election itself rather than its application to one contract: `accounting-policy-coa-desk`.
- The revenue entries are prepared and the question is cutoff testing or the close calendar: `month-end-close-desk`.
- The deferred revenue balance is being tied to its supporting schedule as a balance sheet reconciliation: `account-reconciliation-desk`.
- The ask is ARR, retention, or a run rate rather than recognized revenue: `saas-metrics-reporting-desk`.
- The clause meaning is legally disputed rather than accounting-ambiguous: route to the Legal Contracts suite and read the outcome back here.

## Required evidence

- The executed contract in the form the parties signed, including the order form, every amendment, any statement of work, and any side letter.
- The revenue policy and the elections it takes, from `accounting-policy-coa-desk`.
- Standalone selling price evidence: observable standalone sales, the price list against actual realized pricing, or the cost plus margin or residual basis where no observable price exists.
- Delivery, provisioning, milestone, and usage records establishing when control transferred and how much was consumed.
- The billing schedule and the invoices issued to date, read as evidence of billing rather than as evidence of performance.
- Prior period treatment for comparable contracts, and the treatment of the same customer's prior contract.
- Sales compensation and incentive arrangements where they change the transaction price or create a material right.
- The period status and the cutoff date.

## Workflow

**Outcome.** Per contract, a written five step analysis a reviewer can follow to the conclusion, the revenue schedule it produces by period, the contract asset and contract liability positions it creates, and the entries required. Across the portfolio in scope, the deferred revenue waterfall that ties to the balance sheet, the non-standard terms register, and the named list of contracts whose treatment the available evidence cannot settle.

**Grounding.** The executed contract governs. The billing system says what was invoiced and the sales record says what was sold, and neither says what was promised. Where an order form and a master agreement conflict, the precedence clause decides and the analysis quotes it. Standalone selling price is evidence rather than assertion, and a list price that is never realized is not observable evidence of anything. Delivery and usage records establish control transfer; a project manager's view that the work is essentially done is context that gets checked against the record.

**Constraints.**

- The five step model is applied in order because each step consumes the previous one. Obligations cannot be identified before the contract is identified and combined with any related contract; the price cannot be allocated before the obligations exist; the pattern cannot be set before the allocation is known. The order is mandated by the standard itself, and skipping to the recognition pattern is the shortcut that produces a schedule matching the invoice run by coincidence.
- Distinct is tested against both the good or service on its own and its separability within the contract. Implementation that materially customizes the subscription is not distinct, whatever the order form charges for it separately.
- Variable consideration is estimated with a stated method, expected value or most likely amount, and the constraint is applied and shown. An estimate recorded at the maximum is the constraint not applied rather than the constraint satisfied.
- A renewal option, a discount on future purchases, or a free extension period may be a material right, which is an obligation with a price allocated to it rather than a marketing term.
- Recognition over time requires one of the criteria to be met and a measure of progress that reflects performance. A ratable schedule chosen because it is convenient is a presentation of a decision nobody made.
- A modification is classified before it is scheduled: a separate contract, a prospective termination and replacement, or a cumulative catch-up. The classification is driven by whether the added goods are distinct and priced at standalone selling price, not by whether the customer called it an upsell.
- Non-standard terms are registered individually with their clause reference: acceptance criteria and whether they are objective, service credits and how they are estimated, termination for convenience and what it does to the contract term, most favored nation, and any side letter.

**Parallel surface.** Contracts are independent and fan out. Each contract's five step analysis, schedule, modification treatment, and non-standard terms review runs on its own documents. Standalone selling price studies fan out per performance obligation type. Three passes are aggregate and run once after the fan-out returns. The deferred revenue waterfall ties to the balance sheet across every contract at once, because per-contract schedules that each look right still miss the balance. Revenue by stream is a portfolio total. And consistency of treatment across comparable contracts is a portfolio question by definition, since the same clause accounted for two ways in two contracts is invisible from inside either one.

**Acceptance bar.** Every contract in scope has each of the five steps answered with the clause or record that supports it, not asserted. Every performance obligation states why it is distinct. Every standalone selling price names its basis and its evidence. Every recognition pattern names the criterion met and the measure of progress. The waterfall opens, adds, recognizes, and closes to the balance sheet figure, with any difference stated at its full amount. Every non-standard term appears in the register with its clause reference and its accounting effect.

## Outputs

A complete run delivers the set:

- `revenue-memo-per-contract.md`: the five step analysis per contract with facts, the criteria applied, the analysis against each, the conclusion, and the entries it produces.
- `revenue-schedules.md`: per contract, revenue by period with the measure of progress, alongside the billing schedule so the difference between billed and recognized is visible rather than implied.
- `deferred-revenue-waterfall.md`: opening balance, additions, recognized, closing balance, with the tie to the balance sheet stated and any difference named at full amount.
- `contract-asset-liability-positions.md`: unbilled amounts where performance precedes the right to bill, over-billed amounts where cash preceded performance, and the receivable split, each per contract.
- `non-standard-terms-register.md`: every acceptance clause, service credit, termination right, most favored nation term, and side letter, with the clause reference, the accounting effect, and which contracts carry it.
- `modification-log.md`: each change order with its classification, the rule that decides it, and the catch-up or prospective effect quantified.
- `revenue-recognition-downstream-handoff.md`: terms, schedules, and unbilled and over-billed positions as billing and close will consume them, with unsettled contracts named.

Depth standard: a memo is complete when a reviewer reaches the same conclusion without reopening the contract, and when an auditor sampling it does not have to ask what the criteria were. That means quoting the operative clause, not summarizing it: the acceptance provision as written, the credit mechanism as written, the termination notice period as written. A schedule states the measure of progress and its inputs, so a reader can see why period three recognizes what it does.

Where the run covers one contract rather than the portfolio, the waterfall and the consistency review are scoped to that contract and labeled as such rather than presented as the portfolio position. Where the contract repository, the billing system, or the usage records cannot be read, `revenue-recognition-diagnostic.md` names what was attempted and which conclusions are unavailable without it.

The hazard specific to this desk is that the five step model has a fixed shape, so an analysis with all five headings filled in reads as complete whether or not steps two and four were derived from anything. Standalone selling price is where this concentrates: a number with no observable evidence behind it allocates the entire transaction price and moves revenue between periods, and it is the one input nobody can check without redoing the study. Every allocation input carries its basis, an obligation with no standalone selling price evidence is recorded as `ssp_not_established` with the study that would settle it, and a contract whose terms the documents do not resolve is named as unsettled rather than assigned the treatment the last similar contract received.

## finance_packet fields to update

- `revenue.contracts[]` per contract: `contract_ref`, `customer`, `term`, `transaction_price` with the variable consideration treatment and constraint applied, `performance_obligations[]`, `ssp_basis`, `allocation`, `recognition_pattern`, `non_standard_terms[]`, `modification_treatment`.
- `revenue.deferred_revenue` opening, additions, recognized, closing, and `ties_to_balance_sheet` with the difference where false.
- `revenue.contract_assets`, `revenue.revenue_by_stream[]`, `revenue.cutoff_exceptions[]` with the correcting entry for each.
- `basis.policy_conflicts[]` where a contract is being treated against the written revenue policy.
- `source_facts` with the contract, amendment, and usage record locators and their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Source conflict**: the contract, the order form, the billing system, and the sales record disagree on term, price, scope, or delivery date, or a side letter changes a contract that already looked settled. Record every reading with its document and route the conflict rather than adopting whichever version the system happens to hold.
- **Release integrity**: a revenue figure or a deferred revenue balance would reach the statements, the board, an investor, or a diligence process without the contract basis behind it, or a waterfall that does not tie would travel as though it did.
- **Approval**: the conclusion requires a policy election not already taken, a departure from the written revenue policy, or an out-of-period correction to a closed period.
- **Production or destructive**: the next act would post the revenue entries, release the deferred revenue schedule into the subledger, or amend a contract record in the system of record.
- **Security or privacy**: the artifact would carry unredacted pricing, discount, or commercial terms from a customer contract into a document that leaves finance, or would place one customer's negotiated terms where another can see them.
- **Connector unreachable**: the contract repository, the billing system, or the delivery and usage records exist and cannot be read, so control transfer would be asserted from the invoice schedule.

A missing standalone selling price study, an unconfirmed go-live date, an unsigned but negotiated amendment, or an acceptance whose formal sign-off has not arrived are soft gaps. State the treatment the executed documents support, label the assumption against that contract and obligation, and record what would settle it.

## Downstream handoffs

`billing-order-to-cash-desk` takes the contract terms, the billing schedule against the revenue schedule, and the unbilled and over-billed positions. `accounts-receivable-collections-desk` takes the payment terms as the contract states them rather than as the invoice template does. `month-end-close-desk` takes the revenue entries with their support, the cutoff exceptions, and the deferred revenue roll-forward. `account-reconciliation-desk` takes the waterfall as the supporting schedule for the deferred revenue control account. `financial-reporting-desk` takes the revenue by stream and the disclosure inputs including remaining performance obligations. `saas-metrics-reporting-desk` takes the contract base, with the reminder that the run rate and recognized revenue are different measures.

## Quality bar

A good revenue memo survives being read by someone who wants a different answer. It quotes the clause, states the criterion, and shows why the facts meet it or do not, so the disagreement lands on the analysis rather than on the assertion. The schedule and the billing schedule sit side by side, because the whole value of this desk is making visible the gap that the accounting system cannot see. Non-standard terms are registered before they matter rather than discovered at year end, since the side letter that nobody routed to finance is the single most common origin of a revenue restatement, and the contract it modifies always looked settled.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
