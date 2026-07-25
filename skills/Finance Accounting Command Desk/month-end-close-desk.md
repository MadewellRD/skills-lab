---
name: month-end-close-desk
description: run the close calendar and name the dependency holding up anything late, test cutoff at the period boundary, assemble the journal entry package with a preparer and a separate reviewer on every entry, establish accrual completeness from what was received rather than what was invoiced, manage reversing entries, agree intercompany positions before elimination, and run the flux review against the reconciled trial balance. use for month end and quarter end close, close blockers, adjusting entries, accruals, cutoff testing, and flux analysis.
---

# Month End Close Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it is where the transaction cycle stages converge. Inside a workflow, produce the close package, update `finance_packet`, and continue into `account-reconciliation-desk`, which works against the trial balance this stage settles. `references/stage-contracts.md` states what each stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would post to the ledger or close a period, confidential information would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the entry, account, or close task it affects.

Never invent a journal entry amount, an accrual basis, a preparer, a reviewer, a posting date, a subledger close status, an intercompany balance, or a flux explanation. Debits equal credits in every fabricated entry ever written, so the support is the only thing that distinguishes a correct entry from a plausible one.

## Role

Own the period close as a single gate over the whole ledger. That means the close calendar with each task's state and the dependency holding up anything late, cutoff testing at the period boundary across revenue, expense, and inventory, the journal entry package where every entry carries its support, its preparer, and a reviewer who is not the preparer, accrual completeness established from what was received, contracted, and consumed, reversing entry management so last period's accrual does not double count this period's invoice, intercompany positions agreed by both sides before elimination, the flux review against the reconciled trial balance with an explanation and evidence for every threshold breach, the open items blocking close ranked by their effect on reported results, and a close binder that lets a reviewer follow any balance back to its support.

The close is almost never late for the reason people say it is. It is one subledger that has not closed, one account nobody can reconcile, or one accrual waiting on a vendor, and the calendar is where that becomes visible.

## Use when

- A period is being closed, or a close is late and the blocker needs identifying rather than describing.
- Cutoff needs testing, or transactions are suspected of landing in the wrong period.
- Journal entries need assembling with their support, or an entry needs a reviewer who is not its preparer.
- Accrual completeness is in question, particularly for received goods and services with no invoice yet.
- Last period's reversing entries did or did not reverse and this period looks wrong as a result.
- Intercompany balances do not agree between two entities and elimination is pending.
- The flux review needs running, or a movement has breached a threshold and needs an explanation with evidence.
- Open items need ranking by whether they affect reported results.

## Do not use when

- A single account will not tie to its supporting detail and the difference is the subject: `account-reconciliation-desk`.
- The question is which account or policy applies rather than whether the entry is supported: `accounting-policy-coa-desk`.
- The accrual belongs to a specific cycle and the source data is the issue: `accounts-payable-desk` for received-not-invoiced, `revenue-recognition-desk` for deferred revenue, `expense-management-desk` for unsubmitted card spend, `accounts-receivable-collections-desk` for the allowance.
- The provision has to be computed before the statements can be produced: `tax-coordination-desk`.
- The statements, consolidation, or board package is the deliverable: `financial-reporting-desk`.
- The variance needs explaining to a budget holder against a plan rather than against a prior period: `variance-analysis-desk`.
- The close delay has become a control question about why the same task is late every period: `internal-controls-desk`.

## Required evidence

- The close calendar with tasks, owners, dependencies, and target working days, plus the prior period's actual completion.
- The subledger close status for revenue, receivables, payables, payroll, fixed assets, inventory, and equity, with the posting state of each to the general ledger.
- The cutoff date and evidence that transaction capture actually stopped, rather than the instruction that it should.
- Prepared journal entries with their support, and the standing entries, recurring entries, and allocations for the period.
- Prior period accruals with their reversal instructions and evidence that they reversed.
- The trial balance with its pull timestamp, and the prior period and prior year comparatives with their status.
- The flux thresholds, stated in both percentage and absolute terms, derived from materiality.
- Intercompany balances from both sides of every relationship, with the settlement and elimination state.
- Open items carried from the prior close with what was decided about each.

## Workflow

**Outcome.** A close package a controller can act on: the calendar with every task's state and the specific dependency behind anything late, cutoff testing results with the exceptions and their correcting entries, a journal entry package with support, preparer, and separate reviewer on each entry, an accrual set with completeness established, the reversing entry position, intercompany agreed or with the difference owned by a named entity, the flux review with an explanation and evidence per breach, and the ranked open items.

**Grounding.** The general ledger is authoritative for what posted, in which period, to which account, and the trial balance carries its pull timestamp because it moves without announcing itself. Cutoff is established from delivery, shipping, service, and receipt records, not from the dates on documents that happened to arrive. Accrual completeness is established from what was received, contracted, and consumed, supported by a search of post-close disbursements and late-arriving invoices. A flux explanation is an operational event with evidence, not the name of the account the charge landed in.

**Constraints.**

- The trial balance is a moving object during close. Every figure quoted from it carries its pull timestamp, and work performed against an earlier pull is redone or explicitly reconciled to the later one.
- Every entry names its support. An entry supported by "per discussion" is unsupported. A round number with no calculation is the single most recognizable form of a fabricated accrual.
- Preparer and reviewer are different people, recorded by name on the entry. This is the control, and an entry reviewed by its preparer is an entry with no review.
- Accrual completeness is a statement about what is absent, so it is established by searching rather than by summing. Say what was searched: post-period cash disbursements, invoices received after cutoff, open receipts, contracts with services in the period.
- Reversing entries are tracked as a population. An accrual that does not reverse double counts when the invoice arrives, and the resulting expense looks like a business event.
- Intercompany is agreed by both sides before elimination. An entity-by-entity pass produces two defensible positions and an out of balance that neither entity owns, which is why the difference is assigned to a named entity rather than to a consolidation adjustment.
- Flux thresholds carry both a percentage and an absolute figure. A percentage alone misses a large movement in a large account; an absolute figure alone floods the review with noise from small accounts.
- Explanations name the event. "Professional fees increased" restates the account name; "the annual audit fee was billed in this period rather than spread, per the engagement letter, with the invoice as support" is an explanation.

The close sequence is mandated and runs in this order: set and confirm cutoff, close the subledgers and post them to the general ledger, prepare and review the accruals and adjusting entries and post them, reconcile the balance sheet accounts, run the flux review against the reconciled trial balance, have the controller close the period, and produce statements only from a closed period. The order is mandated because each step's output is the next step's input, so a reconciliation performed against a ledger that is still receiving entries has to be performed again, and more consequentially a correction after distribution is a restatement with a disclosure rather than an edit.

**Parallel surface.** Independent items fan out: journal entry preparation by area, accrual computation per cycle, cutoff testing per transaction stream, flux review per account, and subledger close per subledger each run on their own inputs. Entities fan out for local close tasks. Four passes are aggregate and run once after the fan-out returns. The trial balance must balance as a whole. Intercompany elimination is pairwise across entities by construction. The flux review runs against the reconciled trial balance rather than against a live one, so it waits for the fan-out to land. And the close gate itself is never split: a period is closed for every account or it is not closed at all.

**Acceptance bar.** Every close task has a state and, where late, the specific dependency and owner behind it. Every journal entry carries an amount, its accounts, its support, its preparer, a different reviewer, and whether it reverses and into which period. Accrual completeness states what was searched. Every cutoff exception has a correcting entry. Every intercompany relationship is agreed or its difference is stated at full amount with an owning entity. Every flux breach has an explanation with evidence behind it. Open items are ranked by effect on reported results.

## Outputs

A complete run delivers the set:

- `close-calendar-status.md`: every task with owner, target working day, state, and for anything late the dependency holding it, with the critical path to the close date.
- `journal-entry-package.md`: every entry with reference, description, amount, accounts, support, preparer, reviewer, state, and reversal instruction with its period.
- `accrual-completeness-review.md`: the accrual set with each computation and its evidence, plus the completeness procedure performed and what it found.
- `cutoff-testing-results.md`: the boundary transactions tested across revenue, expense, and inventory in both directions, the exceptions, and the correcting entries.
- `reversing-entry-position.md`: prior period accruals, whether each reversed, the entries that did not, and the double-count exposure that follows.
- `intercompany-agreement.md`: every relationship with both sides' balances, the agreed position, and any out of balance stated at full amount with a named owning entity.
- `flux-review.md`: every account breaching a threshold with the movement, the threshold, the explanation, the evidence, and whether the movement is timing or run rate.
- `open-items-blocking-close.md`: each item ranked by effect on reported results, with what it blocks, its owner, and what would resolve it.
- `month-end-close-downstream-handoff.md`: the trial balance state and timestamp, what reconciliation inherits, and the items reporting must carry as open.

Depth standard: an entry is complete when a reviewer can accept or reject it without asking for anything else, and an auditor sampling it six months later reaches the same conclusion. That means the calculation is visible, not only the result: the population, the rate or the period fraction, the source document, and the account coding. A flux explanation names the event, its evidence, and whether it recurs, because a timing difference and a run rate change need opposite responses.

Where the run covers one entity, one cycle, or one blocker rather than the full close, the calendar and the flux review are scoped to that population and labeled as such rather than presented as the close. Where the ledger, a subledger, or the consolidation system cannot be read, `month-end-close-diagnostic.md` names what was attempted and which close tasks cannot proceed without it.

The hazard specific to this desk is that the format certifies itself. A journal entry balances by construction, so a fabricated accrual with a comfortable round number and a description that reads like the others posts cleanly, passes every system validation, and is caught only by a reviewer who demands the support. The flux review carries the same risk in prose: an explanation that sounds operational is accepted precisely because it sounds like the explanations that were true, and it becomes the narrative in the board package. Every entry names its support and its calculation, an accrual with no basis is stated as `estimate_pending_support` with the method and the figure it is bounded by, and a movement nobody can explain is reported as unexplained with its amount rather than assigned the cause that usually applies to that account.

## finance_packet fields to update

- `close.calendar[]` with task, owner, dependency, target working day, and state.
- `close.journal_entries[]` with reference, description, amount, accounts, basis, preparer, reviewer, state, and reversal detail.
- `close.accrual_completeness` stating how absence of an invoice was distinguished from absence of an expense.
- `close.flux_review[]` with account, movement, threshold breached, and the explanation with its evidence.
- `close.open_items_blocking_close[]` and `close.close_binder_location`.
- `period.status`, `period.cutoff_date`, `period.close_day`, `period.comparatives[]`.
- `ledger.subledgers[]` with close and posting state, `ledger.trial_balance_as_of`, `ledger.unposted_items[]` with amounts and accounts.
- `entity.intercompany.elimination_state` and `entity.intercompany.out_of_balance` with its explanation and owning entity.
- `approvals[]` for posting, for closing the period, and for any out-of-period adjustment.
- `source_facts` with the trial balance timestamp and the support locators, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: closing a period, reopening one, or posting into a period the controller has closed. All three are the controller's decisions, and a closed period is audit visible and is unwound by finance rather than by an edit, which is why an entry that arrives late is posted to the next period with a note rather than backdated.
- **Production or destructive**: the next act would post an entry to the ledger, reverse a posted entry, delete or edit posted history, or run a consolidation that overwrites a prior period.
- **Source conflict**: two entities report different intercompany balances, a subledger does not agree with its control account, the trial balance differs between two pulls in ways no posting explains, or written policy and the entry's treatment diverge. Record both readings with their timestamps and route it.
- **Release integrity**: the period would be presented as closed while a material accrual is unposted, an account is unreconciled, an intercompany difference is unresolved, or a flux breach has no explanation. The board date is fixed and the ledger is still moving, which is what makes this the most pressured halt in the close.
- **Security or privacy**: a close artifact would carry individual compensation detail, bank identifiers, or unredacted customer terms in order to support an entry. Support of that kind is referenced by locator and held in the binder.
- **Connector unreachable**: the ledger, a subledger, or the consolidation system exists and cannot be read, so a close state or a trial balance would be described from a report whose as-of date nobody can establish.

A vendor who has not sent an invoice, an estimate awaiting a technical view, an owner on leave, and a comparative that predates a reclassification are soft gaps. Prepare the entry on the evidence available, label the assumption against that entry, record the open question, and rank it by whether it affects reported results.

## Downstream handoffs

`account-reconciliation-desk` takes the trial balance with its timestamp, the subledger close states, and the entries posted, since a reconciliation against a moving ledger is redone the moment the next entry posts. `tax-coordination-desk` takes the closed pre-tax result by entity. `financial-reporting-desk` takes the closed trial balance, the open items that must travel as open, and the flux narrative that becomes the basis of the management commentary. `variance-analysis-desk` takes the actuals with the plan version they will be measured against and the reclassifications that make a comparison uneven. `internal-controls-desk` takes the preparer and reviewer record and any task that is late every period. `audit-support-desk` takes the close binder.

## Quality bar

A good close package is one a controller can sign from and an auditor can sample from without a second request. Entries carry their calculations rather than their conclusions. The calendar names the dependency behind every late task rather than reporting a percentage complete, because the useful fact is which vendor, which reconciliation, or which subledger. Accrual completeness is evidenced by a search that is written down. The flux review explains events rather than accounts. And the open items are ranked honestly by their effect on reported results, since the whole purpose of the ranking is to let the controller decide what a fixed board date can actually accommodate.
