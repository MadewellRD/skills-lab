---
name: account-reconciliation-desk
description: reconcile balance sheet accounts to their supporting detail, tie subledgers to their general ledger control accounts, reconcile bank statements to book balances with outstanding items listed individually, age reconciling items and flag those surviving multiple periods, record preparer and reviewer separately, and state the unexplained residual at its full amount rather than plugging it to zero. use for balance sheet reconciliations, subledger ties, bank reconciliations, clearing and suspense accounts, intercompany out of balance, and aged reconciling items.
---

# Account Reconciliation Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it sits after close, because a reconciliation against a moving trial balance is redone the moment the next entry posts. Inside a workflow, produce the reconciliation set, update `finance_packet`, and continue into `tax-coordination-desk`, which computes the provision from results that are only defensible once the balance sheet is reconciled. `references/stage-contracts.md` states what each stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would post or overwrite a reconciliation, confidential information would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the account and the reconciling item it affects.

Never invent a reconciling item, an amount, an age, a supporting document, a bank transaction, a preparer, or a reviewer. An item created to make a difference disappear is the specific fabrication this desk exists to prevent, and it is undetectable from inside the reconciliation that contains it.

## Role

Own the proof that each balance is what the ledger says it is. That means the reconciliation set covering every account the policy requires, each showing the ledger balance, the supporting balance, and the difference; reconciling items with an amount, an age, and the evidence behind each; the unexplained residual stated at full amount; the subledger to control account tie for receivables, payables, revenue, fixed assets, payroll liabilities, and equity; the bank to book reconciliation with outstanding payments and deposits in transit listed individually; intercompany reconciliation with the out of balance owned by a named entity; aged items flagged where they have survived several periods; the preparer and reviewer record showing separation between them; and the accounts that could not be reconciled, reported as unreconciled with what would resolve them.

Reconciliation is the only control in the cycle that can prove a balance is wrong. Everything upstream can be internally consistent and still wrong; this is the step that compares the ledger to something outside it.

## Use when

- Balance sheet accounts need reconciling for the period, or the reconciliation set needs reviewing before statements are produced.
- A subledger does not tie to its control account and the difference needs identifying rather than netting.
- A bank account needs reconciling, or outstanding items and deposits in transit have accumulated.
- A clearing or suspense account carries a balance when it should clear to zero.
- Reconciling items have aged across periods without resolution.
- Intercompany balances differ and the out of balance needs an owning entity.
- An account nobody can explain is holding up close, statements, or an audit request.
- A reconciliation looks complete and somebody wants the reconciling items tested rather than counted.

## Do not use when

- The period is still open and entries are still posting: `month-end-close-desk` first, because the reconciliation will be invalidated by the next entry.
- The subject is which account a transaction should hit or what the reconciliation policy requires: `accounting-policy-coa-desk`.
- The difference is a known operational exception in a specific cycle: `accounts-receivable-collections-desk` for cash application exceptions, `accounts-payable-desk` for match exceptions, `billing-order-to-cash-desk` for billing defects, and bring the resolution back here.
- The subject is the cash position, forecast, or bank balances for liquidity rather than the book to bank difference: `cash-flow-treasury-desk`.
- The statements or the consolidation are the deliverable: `financial-reporting-desk`.
- The finding has become a control question about who prepares and who reviews: `internal-controls-desk`.
- An auditor has sampled a reconciling item and wants the support package: `audit-support-desk`.

## Required evidence

- The trial balance for the period with its pull timestamp and the period status.
- Subledger balances and their detail for every control account in scope.
- Bank statements for every account and entity, at the statement date rather than an online balance snapshot.
- Supporting schedules for prepaid, accrued, fixed asset, deferred revenue, equity, and payroll liability balances.
- Prior period reconciliations with their open items and what was decided about each.
- The reconciliation policy: which accounts require preparation, at what frequency, and to what standard, with the risk ranking behind it.
- The preparer and reviewer assignments, and the certification record where the company uses one.
- Intercompany balances from both sides, and the elimination state from close.

## Workflow

**Outcome.** A reconciliation per account in scope, each stating the ledger balance with its timestamp, the supporting balance with its source, the difference, every reconciling item with an amount an age and its evidence, the unexplained residual at full amount, the preparer, the reviewer, and a state. Across the set, the subledger ties, the bank to book position, the intercompany out of balance with an owning entity, the aged item register, and the accounts that could not be reconciled with what would resolve each.

**Grounding.** The ledger is authoritative for the balance and the subledger for the detail, so a subledger that does not tie to its control account is a finding rather than a rounding difference. The bank statement is cash and the book balance is a claim about cash. A supporting schedule is only support if it was built from source records rather than derived from the ledger balance it is meant to prove, which is the quiet failure mode in prepaid and accrual schedules.

**Constraints.**

- Both balances carry their as-of moment. A ledger balance from one timestamp against a subledger extract from another produces a difference that is entirely an artifact of timing and will not reproduce.
- Every reconciling item has an amount, a date, an age, and a document. An item described by category alone, "timing difference" or "in transit", with no date and no document, is the standard form of a plug.
- Age reconciling items and flag anything that has survived multiple periods. An item that is genuinely in transit clears; an item that has been in transit for five periods is something else that has been called in transit.
- The unexplained residual is reported at its full amount and never forced to zero, never netted against a difference in another account, and never absorbed into a rounding line. A visible difference is a problem somebody can work on; a hidden one is discovered by an auditor.
- Clearing and suspense accounts are reconciled to zero or their balance is itemized. A clearing account with a growing balance is an unposted population, and its growth rate is the useful signal.
- Intercompany differences get an owning entity. A difference recorded at the consolidation level belongs to nobody and reappears every period.
- `reconciled_with_open_items` is a legitimate state and is more useful than a forced `reconciled`. State which items are open and what each one needs.
- Support that was derived from the ledger balance is not support. Say where a schedule came from.

The reconciliation control follows a mandated order: the subledger or supporting source is closed and extracted at a stated moment, the ledger balance is taken at the same moment, the reconciliation is prepared with its items evidenced, and a reviewer who is not the preparer accepts it. The order is mandated because the separation between preparer and reviewer is the control itself, and a reconciliation reviewed by the person who prepared it provides no assurance regardless of how carefully it was built.

**Parallel surface.** Accounts are independent and fan out: each account's balance comparison, item identification, evidence gathering, and aging run on that account's own sources. Bank accounts fan out per account and entity. Entities fan out for their local balance sheets. Four passes are aggregate and run once after the fan-out returns. Intercompany reconciliation is pairwise across entities by construction, so a per-entity pass yields two defensible sides and an out of balance neither owns. The deferred revenue tie is one pass over the whole waterfall against the balance sheet, because per-contract schedules that each look right still miss the balance. Materiality is assessed against the whole, so a population of individually trivial differences is evaluated in aggregate before any of it is passed. And the completeness check, which accounts the policy requires against which were prepared, is a single pass over the account list.

**Acceptance bar.** Every account the policy requires appears with a state, including `not_attempted` where that is the truth. Both balances carry their source and their as-of moment. Every reconciling item has an amount, a date, an age, and a document reference. The unexplained residual is stated at full amount with its age. Every reconciliation names a preparer and a different reviewer. Every subledger tie is stated as a comparison rather than asserted. Aged items are flagged with the number of periods they have survived.

## Outputs

A complete run delivers the set:

- `reconciliation-set.md`: per account, the ledger balance and its timestamp, the supporting balance and its source, the difference, the reconciling items with amounts ages and documents, the unexplained residual, the preparer, the reviewer, and the state.
- `subledger-to-control-ties.md`: receivables, payables, revenue, fixed assets, payroll liabilities, and equity, each with both balances, the difference at full amount, and the population that explains it or the fact that none does.
- `bank-to-book-reconciliation.md`: per account and entity, the statement balance at the statement date, the book balance, outstanding payments and deposits in transit listed individually with dates and ages, bank charges and returned items, and interbank transfers in transit.
- `aged-reconciling-items.md`: items surviving multiple periods with their original date, the number of periods carried, the amount, the prior period disposition, and what resolution requires.
- `intercompany-reconciliation.md`: each relationship with both sides' balances, the matched population, the out of balance at full amount, and the entity that owns it.
- `unreconciled-accounts-register.md`: accounts that could not be reconciled, with the balance, what was attempted, why it failed, and the record that would resolve it.
- `reconciliation-completeness-and-review-record.md`: the policy population against what was prepared, with preparer and reviewer per account and any account where they are the same person.
- `account-reconciliation-downstream-handoff.md`: the reconciled position for tax and reporting, the residuals that must travel as open, and the control findings.

Depth standard: a reconciliation is complete when a reviewer can accept it without opening another system, and an auditor sampling any item can trace it to a document. That means an item reads "payment issued on the stated date, cleared the bank in the following period, per the check register and the subsequent statement" rather than "outstanding payments". A subledger tie states both figures and the difference rather than the word "agrees". A residual states its amount, its age, and what has been ruled out.

Where the run covers a single account or a single tie rather than the policy population, the completeness record is scoped and labeled as such rather than presented as the full set. Where the ledger, a subledger, or a bank statement cannot be read, `account-reconciliation-diagnostic.md` names what was attempted and which accounts cannot be reconciled without it.

The hazard specific to this desk has a name in the profession, and it is the reason this desk exists. A reconciliation is the one artifact whose format is a proof of its own correctness: it reaches zero, therefore it looks right, and the arithmetic that makes it convincing was never the part in question. A reconciling item invented to close a difference converts a visible problem into an invisible one, and it survives for exactly as long as nobody samples it. The tells are consistent: an item with a category but no date, a round amount, a difference that closes to zero in every period against a subledger that never agrees, and a schedule built by starting from the ledger balance. Every item carries a date, an amount, and a document. A difference that no item explains is reported at its full amount as unexplained with the account and its age, and an account whose support cannot be located is stated as `unreconciled` with the record that would settle it. An honest unreconciled account is something a controller can act on; a reconciled-looking account with a manufactured item is a misstatement with a cover on it.

## finance_packet fields to update

- `reconciliations[]` per account: `account`, `gl_balance`, `supporting_balance`, `difference`, `reconciling_items[]` with amount age and evidence, `unexplained_difference` at full amount, `preparer`, `reviewer`, `state`.
- `ledger.subledgers[]` with the tie result per subledger.
- `cash.book_to_bank` with outstanding items and deposits in transit.
- `entity.intercompany.out_of_balance` with its explanation and the owning entity.
- `revenue.deferred_revenue.ties_to_balance_sheet` with the difference where false.
- `controls.deficiencies[]` seeded where preparer and reviewer are the same person or a required reconciliation was not prepared.
- `source_facts` with ledger, subledger, and statement locators and their as-of timestamps, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Release integrity**: statements, a covenant certificate, a borrowing base, or an audit deliverable would be produced over an account whose difference is unexplained or whose reconciling items are unsupported. This is the defining halt for this desk, because a forced zero is invisible until it is sampled, and the person who finds it is an auditor rather than the person who created it.
- **Production or destructive**: the next act would post an adjusting entry to clear a difference, overwrite a completed reconciliation, certify an account, or write off a residual.
- **Approval**: writing off an aged reconciling item or an unexplained residual, whatever its size, because that is a decision to accept a difference nobody explained rather than a bookkeeping step.
- **Source conflict**: the subledger and its control account disagree beyond identified items, the bank statement and the book differ beyond identified reconciling items, or two entities report different intercompany balances. Record both readings with their as-of moments and route it.
- **Security or privacy**: a reconciliation artifact would carry full bank account and routing numbers, individual payroll detail supporting a liability balance, or customer-identifying data beyond what the reconciliation requires.
- **Connector unreachable**: the ledger, a subledger, or a bank statement source exists and cannot be read, so a balance would be reconciled against a figure whose origin nobody can establish. An empty query result and an unreachable system look identical and mean opposite things; say which one occurred.

A supporting document awaiting retrieval, an item whose original transaction predates the current system, a preparer on leave, and a bank charge pending its statement description are soft gaps. Prepare the reconciliation with the item stated and evidenced as far as it goes, label the assumption against that item, record what would resolve it, and leave the state as `reconciled_with_open_items` rather than promoting it.

## Downstream handoffs

`tax-coordination-desk` takes the reconciled pre-tax result and the temporary difference schedules that depend on reconciled balances. `financial-reporting-desk` takes the reconciliation states, the residuals that must travel as open, and the fact of any unreconciled account, since a statement produced from an unreconciled ledger is a draft regardless of how finished it looks. `cash-flow-treasury-desk` takes the bank to book position and the outstanding items. `month-end-close-desk` takes back any difference that requires an entry in the current period. `internal-controls-desk` takes the preparer and reviewer record, the accounts the policy required and nobody prepared, and the aged item population. `audit-support-desk` takes the set as the primary evidence package, because reconciliations are the first thing sampled.

## Quality bar

A good reconciliation set is honest about what it cannot explain, and it is judged on that rather than on how many accounts show zero. Items carry dates and documents, so an auditor sampling one finds a record rather than a category. Aged items are visible and counted, because the same item carried for five periods is a finding about the process rather than about the balance. Clearing accounts clear or their contents are listed. And a residual is stated at its full amount with its age, since a controller who knows there is an unexplained difference in one account can act, while a controller looking at a complete set of zeros has been told nothing at all.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
