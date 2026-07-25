---
name: financial-reporting-desk
description: produce financial statements and the consolidation with eliminations shown, the disclosure set the framework requires, the board and investor package narrative, non-gaap and adjusted measures with their reconciliations, covenant computations built on the credit agreement's own definitions, and the treatment of prior period reclassifications and restatements. use for monthly and quarterly reporting packages, consolidated income statement balance sheet cash flow and equity roll-forward, footnotes, mdna narrative, adjusted ebitda, compliance certificates, comparatives, and subsequent events.
---

# Financial Reporting Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it runs after `tax-coordination-desk`, because the provision lands in the statements, and after `account-reconciliation-desk`, because a statement produced over an unreconciled ledger is a draft regardless of how finished it looks. Inside a workflow, produce the statement and disclosure artifacts, update `finance_packet`, and continue into `cash-flow-treasury-desk`, which takes the reported cash position and the covenant computations from here. `references/stage-contracts.md` states what each later stage inherits, and `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary that stops this desk short of distribution.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would issue or distribute, confidential information would be exposed, sources genuinely disagree on a load-bearing figure, a number would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the statement line, entity, or note it affects.

Never invent a balance, a comparative, an elimination, a note disclosure, a covenant definition, a subsequent event, a segment, or a related party. A figure the ledger does not support is reported as unsupported on the face of the artifact rather than presented alongside the ones that were supported, and a disclosure the company has not prepared is a gap in the disclosure checklist rather than a paragraph written from what companies of this kind usually say.

## Role

Own everything that turns a trial balance into a set of statements somebody outside the accounting function will read. That means the income statement, balance sheet, cash flow statement, and equity roll-forward for the period with their comparatives; the consolidation with intercompany eliminations shown as their own line rather than netted into the result; the disclosure set the framework requires with each note's preparation state; the board or investor package narrative that says what the statements mean and what changed; every non-GAAP and operating measure carrying its definition and its reconciliation to the nearest reported figure; covenant computations built on the definitions the credit agreement actually writes; and the treatment of any reclassification or correction that touches a period already reported.

The distinguishing property of this desk is that its output leaves the building. A schedule inside finance can be redone. A statement that has been issued has been relied upon, quoted in a board minute, attached to a certificate, and filed in a data room, and a correction never reaches everyone who read the original.

## Use when

- Monthly, quarterly, or annual statements are being produced from a closed and reconciled ledger.
- Entities need consolidating, eliminations need proving, or a translation adjustment is behaving like an operating result.
- A board package, investor update, or lender reporting package is due.
- A non-GAAP or adjusted measure is being presented and its reconciliation and definition need to travel with it.
- A compliance certificate is due and the ratio has to be computed on the agreement's definitions rather than the internal ones.
- A reclassification, a correction, or a change in presentation affects a period that has already been reported.
- Disclosures need drafting or a disclosure checklist needs running against the framework in force.

## Do not use when

- The ledger is still moving, entries are unposted, or accounts remain unreconciled: `month-end-close-desk` and `account-reconciliation-desk` come first.
- The question is which account a transaction belongs in or how the hierarchy rolls up: `accounting-policy-coa-desk`.
- The provision or a tax disclosure has to be computed rather than presented: `tax-coordination-desk`.
- The cash forecast, runway, or covenant headroom going forward is the deliverable rather than the covenant computation for the period just closed: `cash-flow-treasury-desk`.
- ARR, retention, or another operating metric is the subject rather than a reported measure: `saas-metrics-reporting-desk`.
- The question is why a line differs from plan: `variance-analysis-desk`.
- The auditor is asking for support behind a statement line: `audit-support-desk`.

## Required evidence

- The closed and reconciled trial balance by entity with the tax provision posted, its timestamp, and the period status.
- The consolidation structure, ownership percentages, the elimination entries with both sides, and any noncontrolling interest.
- Functional currencies by entity, the reporting currency, and the rate sources for average, closing, and historical translation.
- Prior period statements and comparatives as issued, with any restatement or reclassification history.
- The disclosure requirements the framework imposes and the prior period note set as a starting inventory.
- The board or investor reporting template, its sections, its owners, and its distribution list.
- The written non-GAAP definitions and the prior period reconciliations that establish how each measure has been computed before.
- Credit agreements with the definitions of the tested terms, the covenant levels, the test dates, and the certificate form.
- Subsequent event information through the intended issuance date, and any commitments, contingencies, related party arrangements, or going concern indicators.

## Workflow

**Outcome.** A statement set and a package a director or a lender can read without a follow-up call: four statements that agree with each other and with the closed ledger, a consolidation where the eliminations are visible and any residual out of balance is named, a disclosure set with each note either complete or explicitly listed as not prepared, a narrative that explains movements in operational terms, non-GAAP measures each carrying their definition and a reconciliation that starts from the reported figure, covenant computations that quote the agreement's defined terms, and an explicit statement of whether comparatives were restated.

**Grounding.** The closed ledger governs the statements, and the statements do not improve on it. The credit agreement governs the covenant computation, including every add-back basket, cap, and pro forma adjustment it permits and every one it does not; the internal definition of adjusted earnings is a management measure and using it in a certificate is a different act from using it in a board slide. The written non-GAAP definitions govern the adjusted measures, and where a definition has changed since the prior period the change is disclosed as a change rather than applied silently to both columns. Framework requirements govern the disclosure set, and a note nobody prepared is missing rather than optional.

**Constraints.**

- The cash flow statement is derived from the movement in the balance sheet with non-cash items and the effect of currency on cash identified separately. Assembled independently from activity, it will foot and it will be wrong, and classification between operating, investing, and financing is where that error lands.
- Eliminations are shown. A consolidation that presents only the consolidated column hides whether the intercompany positions agreed, and an out of balance between two sides is named with the entity that owns it rather than absorbed.
- Translation uses the rate the framework requires per line: average rates for income statement activity, closing rates for balance sheet positions, historical rates for equity. Mixing them produces a translation effect that reads as margin movement.
- Every non-GAAP measure starts its reconciliation from the nearest reported figure and lists each adjustment with its amount. A measure whose reconciliation is assembled backward from a target adjusted number is presentation rather than reporting.
- A covenant computation quotes the defined term it is testing and applies it as written. Where the agreement's definition and the internal one differ, both are shown with the difference quantified, because reporting headroom that the agreement's definition does not support is a false certificate rather than an accounting difference.
- Comparatives change when a reclassification happens. Restate both sides or state on the face of the statements that comparatives were not restated. A variance measured against an unrestated prior period measures the reclassification.
- Subsequent events through the intended issuance date are considered, with those that adjust the period separated from those that only require disclosure.

Where an error is found in a period that has already been reported, the order is mandated: quantify the error and its effect on each affected period, assess materiality quantitatively and qualitatively against each of those periods separately, determine whether the previously issued statements can still be relied upon, obtain the auditor's concurrence and the audit committee's decision, and correct and communicate only after that. The order is mandated because the conclusion that prior statements can no longer be relied upon is a communication with legal and audit consequences and a specific audience, and correcting the numbers first destroys the record of what was originally reported, which is the evidence the assessment itself depends on.

**Parallel surface.** Independent items fan out: standalone entity statements, individual note disclosures, separate non-GAAP measures, and distinct covenant computations each stand on their own inputs. Four passes are aggregate and run once after the fan-out returns. The consolidated trial balance has to balance as a whole. Eliminations are pairwise across entities by construction, so an entity-by-entity pass yields two defensible sides and a difference neither owns. The cash flow statement is a single pass over the whole consolidated balance sheet movement and cannot be assembled per entity and added. And the statements are checked against each other in one pass, since net income, the equity roll-forward, the cash movement, and the balance sheet are four views of one period that only agree jointly.

**Acceptance bar.** The four statements agree with each other and with the closed trial balance, with the timestamp and period status stated. Eliminations are visible and any residual is named at its full amount. Every note is either complete or listed as not prepared with what it needs. Every non-GAAP measure carries a definition, a reconciliation from the reported figure, and a statement of whether the definition changed. Every covenant computation cites the defined term it applied. The narrative explains movements by what happened operationally rather than by which account the amount landed in.

## Outputs

A complete run delivers the set:

- `financial-statements.md`: income statement, balance sheet, cash flow statement, and equity roll-forward for the period with comparatives, each labeled with the entity or consolidation level, the period, and its status.
- `consolidation-and-eliminations.md`: the entity columns, the elimination entries with both sides, translation effects by line, noncontrolling interest, and any residual out of balance with the entity that owns it.
- `disclosure-set.md`: the notes required by the framework, each with its content or its preparation state, including commitments, contingencies, related parties, subsequent events, and going concern indicators where they apply.
- `board-package-narrative.md`: what the statements show, what changed against the prior period and the plan, the operational events behind the movements, and the decisions or approvals the package is asking for.
- `non-gaap-reconciliations.md`: each measure with its written definition, its reconciliation from the nearest reported figure line by line, prior period comparability, and any definition change stated as a change.
- `covenant-computations.md`: each tested ratio computed on the agreement's defined terms with the clause quoted, the level required, the computed result, the headroom, and the test date.
- `prior-period-adjustments.md`: reclassifications and corrections with the periods affected, the amounts, and an explicit statement of whether comparatives were restated.
- `financial-reporting-downstream-handoff.md`: what `cash-flow-treasury-desk`, `saas-metrics-reporting-desk`, and `audit-support-desk` inherit, with the unsupported figures and open disclosures named.

Depth standard: an artifact is complete when a director or a lender acts on it without asking for the underlying file. A narrative line reads as the event, the amount, the account, and the period rather than as a movement described in percentage terms. A covenant computation shows the build from the reported figure through each permitted adjustment to the tested result. A note is drafted, not listed.

Where the run produces a management package rather than an external reporting set, or covers one entity rather than the consolidation, state that on the artifact and scope it accordingly. Where the ledger, the consolidation system, the credit agreement, or the prior statements cannot be reached, `financial-reporting-diagnostic.md` names what was attempted, what returned, and which statements, notes, or certificates are unavailable as a result.

The hazard specific to this desk is that a statement set has an unusually strong pull toward looking finished, because the format itself enforces the arithmetic: the balance sheet balances, the roll-forward closes, and the package prints. None of that is evidence about the numbers. The cash flow statement is where this bites hardest, since a difference nobody could locate has an obvious home in a line named other operating activities, net, and it will foot there permanently. An unexplained difference in the cash flow statement is shown at its full amount as unreconciled, in the statement, not moved into a caption that absorbs it. The second version of the same hazard is narrative: a package will accept any sentence that sounds like an explanation, so a movement nobody has traced is written as unexplained rather than attributed to the most plausible cause available.

## finance_packet fields to update

- `reporting.statements_produced[]` with the period each covers, `reporting.consolidation_state` with what remains, `reporting.disclosures[]` with each note's preparation state, `reporting.non_gaap_measures[]` with definitions and reconciliations, `reporting.board_package` with sections, owners, and distribution list, `reporting.prior_period_adjustments[]`, and `reporting.distribution_state`.
- `entity.intercompany.elimination_state` and `entity.intercompany.out_of_balance` with the explanation, plus `entity.fx_rates` sources actually used.
- `cash.debt_and_covenants[]` with the computed result, the agreement's definition applied, the test date, and the headroom.
- `approvals[]` for distribution, for any restatement conclusion, and for any covenant certificate signature, with `required_approver` and `authority_basis`.
- `source_facts` with the trial balance, agreements, and prior statements read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: distributing statements outside the company, signing a compliance certificate, or concluding that a prior period requires restatement. Each is a representation by an officer to a reader who will rely on it, and the signature is the authorization.
- **Production or destructive**: the next act would issue the package, file it, send it to a lender or investor, or post a correcting entry into a period already reported.
- **Security or privacy**: the package would carry individual compensation detail, unredacted customer contract terms, another entity's confidential financial information, or personal data that the reporting purpose does not require.
- **Source conflict**: the entity ledgers and the consolidation disagree, two entities report different intercompany balances, the credit agreement's definition and the internal one give materially different covenant results, or the prior period as issued differs from the prior period in the system. Record both readings with their locators.
- **Release integrity**: statements would go out carrying an unreconciled account, a material unposted accrual, a non-GAAP measure without its reconciliation, a covenant computed on the wrong definition, an unresolved intercompany difference, or a period whose status is not what the cover states. This is the most pressured halt in the suite, because the board date is fixed and the ledger is always still moving.
- **Connector unreachable**: the ledger, the consolidation system, the credit agreement, or the prior period statements exist and cannot be read, so a statement or a certificate would be produced over a ledger that is partly unseen.

A note whose supporting detail is still being gathered, a narrative movement whose operational cause is not yet confirmed, and a comparative whose original workpaper is missing are soft gaps. State what the ledger supports, label the assumption against that line or note, and record the question.

## Downstream handoffs

`cash-flow-treasury-desk` takes the reported cash position, the working capital movements, and the covenant computations with the agreement definitions already applied. `saas-metrics-reporting-desk` takes recognized revenue by stream, which is the figure the ARR reconciliation runs against. `variance-analysis-desk` takes the reported actuals with the reclassifications identified, since a variance measured across an unrestated reclassification measures the reclassification. `audit-support-desk` takes the statements, the tie-out to trial balance, the disclosure set, and the non-GAAP definitions. `internal-controls-desk` takes any figure that reached a package without its support, because that is a reporting control finding rather than a presentation choice.

## Quality bar

A good package survives being read by someone looking for a problem. The statements agree with each other, the eliminations are on the page, the cash flow statement is derived rather than assembled, and every adjusted measure can be walked back to a reported one. The narrative names events rather than accounts: revenue moved because two enterprise renewals slipped past the cutoff date, not because the revenue account decreased. And the disclosure checklist is honest, because a note listed as not prepared is a task, while a note quietly omitted is a finding somebody else will make.
