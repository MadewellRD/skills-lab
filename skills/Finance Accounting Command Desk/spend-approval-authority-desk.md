---
name: spend-approval-authority-desk
description: determine the approver a commitment requires under the delegation of authority matrix, compute total commitment value including renewal and auto-renewal exposure rather than the first invoice, check budget headroom on the specific line the spend consumes, test for split purchases sized under a threshold, and record spend committed without approval as a control finding. use for purchase approvals, contract signature authority questions, multi-year commitments, capital versus operating spend, sole source justification, and unapproved or maverick spend.
---

# Spend Approval And Authority Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite. Inside a workflow, produce the authority determination and the commitment view, update `finance_packet`, and continue into `accounts-payable-desk`, which will process the invoices this commitment generates. `references/stage-contracts.md` states what each stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would commit the company, confidential information would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the commitment it affects.

Never invent an approver, an approval, an authority threshold, a matrix provision, a budget line, a headroom figure, a contract term, a renewal notice period, or a total contract value. This desk exists to enforce an approval gate, so a plausible approver written into a determination manufactures the exact control it was asked to check.

## Role

Own the question of whether this spend may be committed, by whom, against what budget. That means the authority determination naming the approver the policy requires and the provision that sets the level, the total commitment value including renewal and auto-renewal exposure rather than the first invoice, the budget check identifying the specific line the spend consumes and the headroom left on it after existing commitments, the split-purchase test where a request appears sized to sit under a threshold, the accounting treatment the commitment will require when it lands, the exception record where authority was granted outside the matrix, and the commitments that entered without any approval at all.

The characteristic failure is arithmetic rather than governance. A request presents a monthly figure, the approver reads a monthly figure, and the company signs a three-year auto-renewing obligation two authority levels above the person who approved it. Nobody in that chain did anything wrong except read the number that was put in front of them.

## Use when

- A purchase, subscription, contract, or renewal needs its approver determined before it is committed.
- The commitment is multi-year, auto-renewing, usage-based with a minimum, or has a notice period that creates exposure past the current budget year.
- Budget headroom needs checking against the line the spend actually consumes, net of what is already committed.
- A request looks sized to a threshold, or a vendor relationship is arriving as several small requisitions.
- Signature authority and spend authority are being confused, which they usually are because they live in different documents.
- Spend has already been committed without approval and somebody wants to know what to do about it.
- Capital and operating classification changes which authority applies.

## Do not use when

- The commitment is approved and the invoice needs matching, coding, or paying: `accounts-payable-desk`.
- The spend is an employee reimbursement or corporate card transaction under the travel and expense policy: `expense-management-desk`.
- The delegation of authority matrix itself is being written or amended: prepare the change and stop at the gate, because the board or the executive who owns the matrix authors it.
- The question is which budget line should exist or how the commitment is classified in the chart: `accounting-policy-coa-desk`.
- The budget itself is being built or reforecast: `budget-planning-desk` and `forecast-scenario-desk`.
- Vendor selection, sourcing strategy, or the commercial negotiation is the subject: route to the Procurement and Vendor Management suite with the commitment position and the approval requirements supplied from here.
- The unapproved spend has become a control question about how it got through: `internal-controls-desk`.

## Required evidence

- The delegation of authority matrix at its current version, with the board resolutions or policy provisions behind each level.
- The approved budget with the specific line the request would consume, and the commitments already encumbering that line.
- The purchase request or commitment with its amount, its term, its renewal and notice provisions, and its total contract value rather than only its first invoice.
- The vendor and any existing agreement with them, including master agreements the request would order against.
- The requester, their cost center, and their approval chain.
- Prior exceptions granted, with who authorized each and on what basis.
- The procurement process where one exists, including competitive bid or sole source requirements at the relevant threshold.
- The capital and operating classification, since capital authority is usually a separate and lower threshold.

## Workflow

**Outcome.** Per commitment, the authority determination with the approver role and the matrix provision that sets it, the total commitment value with its components and its renewal exposure, the budget line and remaining headroom after existing commitments, the split-purchase assessment, the accounting treatment the commitment will require, and the approval state. Across the population in scope, the exception record and the register of spend committed without approval.

**Grounding.** The matrix sets the level and it is quoted by provision rather than inferred from the size of the number. The contract or order form sets the term, the renewal mechanism, and the notice period. The budget system sets the headroom, and headroom is the approved amount less both actuals and existing commitments, because a line with budget remaining and a signed commitment against it has no headroom regardless of what the actuals show. An approval is an artifact with an approver, a date, and a scope; a verbal agreement recalled in a thread is context.

**Constraints.**

- Value the whole commitment. Total contract value includes the initial term, every automatic renewal the company would have to act to prevent, minimum commitments, and any termination fee. A monthly figure approved as though it were the obligation is the most common way authority is bypassed without anyone intending to.
- Auto-renewal is exposure with a date attached. Record the notice window and the last date to act, because a renewal that arrives is an approval that was never sought.
- Signature authority and spend authority are different powers set by different documents. Say which one is being determined, and where the person who can sign cannot approve the amount, say so plainly.
- Test for split purchases on pattern rather than intent: the same vendor, the same requester, the same period, and amounts that sit just under a level. Report the pattern and the aggregate value, and let the approver at the aggregate level decide.
- Check the budget line the spend actually consumes rather than the department total. A department with headroom overall and none on the line the request hits is a real constraint that a department-level check will miss.
- Capital and operating classification is settled before the authority is determined, because capital thresholds are usually lower and a misclassified request is routed to the wrong approver with a correct-looking determination.
- Spend already committed without approval is a control finding. It is recorded as unapproved with its amount and its origin, and routed. Backfilling an approver who would probably have said yes destroys the only evidence that the control failed.

The approval sequence is mandated: determine the total commitment value, identify the authority level and the provision that sets it, check budget headroom on the consuming line, route to the named approver, and only then commit. The order is mandated because an approval sought after the commitment exists is a formality performed on a decision already made, and every subsequent control in the procure-to-pay chain assumes this gate operated first.

**Parallel surface.** Commitments are independent and fan out: the value computation, the matrix lookup, the budget line check, the accounting treatment, and the vendor agreement review each run per commitment on its own documents. Three passes are aggregate and run once after the fan-out returns. The split-purchase test is inherently a population test, since a split is invisible from inside either half. Vendor-level total exposure aggregates across every commitment with that vendor, which is where a fourth small subscription reveals a relationship above a threshold. And budget headroom is consumed cumulatively, so a set of requests each fitting the remaining line will not all fit once they are ordered.

**Acceptance bar.** Every commitment has a total value with its components shown, a named approver role with the matrix provision quoted, a budget line with headroom computed net of existing commitments, and a stated approval state. Every renewal exposure carries its notice date. Every split-purchase flag names the aggregate and the threshold it crosses. Every unapproved commitment appears in the register with its amount, its date, and how it entered, with no approver inferred.

## Outputs

A complete run delivers the set:

- `authority-determination.md`: per commitment, the required approver role, the matrix provision that sets the level, the classification driving it, and whether signature authority sits with the same person.
- `total-commitment-view.md`: per commitment, initial term value, renewal terms and auto-renewal exposure, minimums and true-ups, termination fees, the total, and the last date to act on notice.
- `budget-headroom-check.md`: the consuming line, approved amount, actuals to date, existing commitments, remaining headroom, and the effect of this commitment, with the cumulative effect where several requests compete for one line.
- `split-purchase-assessment.md`: patterns by vendor, requester, and period, with the aggregate value, the threshold it reaches, and the approver that aggregate would require.
- `commitment-accounting-treatment.md`: how each commitment lands, covering capital or operating classification, prepaid treatment, accrual profile, lease assessment where applicable, and the disclosure it may create.
- `authority-exception-register.md`: exceptions granted outside the matrix with who authorized each and on what basis, and spend committed without approval with amount, date, and origin.
- `spend-approval-downstream-handoff.md`: what payables inherits about approved commitments and expected invoices, and what controls inherits about the gate failures.

Depth standard: a determination is complete when the approver can act on it without asking what they are approving. That means the total obligation with its components visible, the specific consequence of not acting on a renewal notice, and the budget position stated as a figure rather than as "within budget". An exception entry names the person who authorized the departure and the basis they gave, because an exception with no author is indistinguishable from an omission.

Where the run covers a single request rather than a spend population, the split-purchase test and the vendor aggregation are scoped to what was visible and labeled as such. Where the matrix, the budget system, or the contract cannot be read, `spend-approval-diagnostic.md` names what was attempted and which determinations cannot be made without it.

The hazard specific to this desk is that its output is the control. Everywhere else in this suite a fabricated figure produces a wrong number; here a fabricated approver produces a governance record showing that an authority gate operated when it did not, and that record is what an auditor will sample and what management will rely on. Approver roles are quoted from the matrix provision, thresholds are quoted rather than rounded to a familiar figure, and a commitment whose approval cannot be located is recorded as `no_approval_on_file` with the search performed. Total contract value is computed from the executed terms; where the renewal mechanism is not in the documents available, the value is stated for the term that is documented and the unknown exposure is named rather than estimated into the total.

## finance_packet fields to update

- `spend_approvals.authority_matrix_ref` with its version, and `spend_approvals.commitments[]` with amount, total value, term, renewal exposure, approver required, and approval state.
- `spend_approvals.budget_check` naming the consuming line and the headroom computed net of commitments.
- `spend_approvals.exceptions[]` with who authorized each departure and the basis given.
- `approvals[]` per commitment with `amount_at_stake`, `required_approver`, `authority_basis` quoting the provision, and `state`.
- `plan.departments[]` where the commitment changes a department's committed position, and `controls.deficiencies[]` seeded where spend entered without approval.
- `source_facts` with the matrix version, budget report, and contract locators and their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: this desk determines that a commitment requires a named authority and stops there. It never grants the approval it identifies, because determining the requirement and then proceeding without it removes the only control in the sequence.
- **Production or destructive**: the next act would sign, submit, or accept a commitment, issue a purchase order, or allow an auto-renewal to pass its notice date without a decision.
- **Source conflict**: the matrix version in circulation and the one in the policy library set different thresholds, the contract and the request state different terms or values, or the budget system and the approved plan show different amounts on the consuming line. Record both readings and route it.
- **Release integrity**: a commitment position, a headroom figure, or an exposure total would go to the board, a lender, or a diligence process without the contracts and the budget records behind it.
- **Security or privacy**: an artifact would carry another vendor's confidential pricing, a counterparty's non-public terms, or personal data gathered during a vendor assessment.
- **Connector unreachable**: the authority matrix, the budget system, or the contract repository exists and cannot be read, so an approver or a headroom figure would be asserted from what a policy of this kind usually says.

A requester who has not confirmed the intended term, a vendor quote that predates the current price list, a cost center whose owner is between holders, or an unclear capital classification pending a technical view are soft gaps. State the determination the available evidence supports, label the assumption against that commitment, and record what would settle it.

## Downstream handoffs

`accounts-payable-desk` takes the approved commitments, the expected invoice profile, and the purchase order references that the three way match will use, plus any commitment that has no approval so that its invoices are not matched into legitimacy. `expense-management-desk` takes the boundary where spend that should have run through procurement is arriving on cards. `accounts-payable-desk` and `month-end-close-desk` take the commitment accounting treatment for accrual and prepaid purposes. `budget-planning-desk` takes committed spend as a separate population from discretionary, which is the only way a cut conversation can start. `internal-controls-desk` takes the unapproved commitments and the exception pattern as findings. `financial-reporting-desk` takes multi-year commitments for the obligations disclosure.

## Quality bar

A good determination changes what the approver knows before they decide. It shows the whole obligation rather than the first payment, the date past which the decision makes itself, and the budget position as a number. Exceptions are visible and attributed, because an exception register with an author is a functioning control and one without is a paperwork exercise. And unapproved spend is reported as unapproved: the temptation to tidy it into an approval chain is exactly the instinct that makes the next one easier, and the register of how spend entered without a gate is more useful to the company than a complete-looking approval file.
