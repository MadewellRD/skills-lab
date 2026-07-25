---
name: expense-management-desk
description: review travel and expense reports against the policy provision each item breaches, reconcile the corporate card program including unsubmitted spend and the accrual it drives, code entertainment benefits and non-deductible categories for their tax treatment, identify personal spend on company instruments with its recovery mechanism, and surface approval patterns and policy gaps. use for t and e compliance, per diem and mileage, receipt thresholds, card reconciliation, taxable fringe benefits, reimbursement disputes, and expense accruals.
---

# Expense Management Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite. Inside a workflow, produce the compliance review, the card reconciliation, and the accrual, update `finance_packet`, and continue into `equity-cap-table-desk` on the main chain. `references/stage-contracts.md` states what each stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would recover money from an employee or move a payment, personal or card data would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the report, card, or cost center it affects.

Never invent an employee name, a transaction, a merchant, an amount, a receipt, an approver, a per diem or mileage rate, or a policy provision. A policy breach attributed to a named person is read as an accusation by everyone who sees it, including the person named.

## Role

Own employee-initiated spend and the tax and control consequences it carries. That means policy compliance stated by the provision breached rather than by general judgment, the out-of-policy register with the amount, the employee, the approver who let it through, and the disposition, the corporate card reconciliation covering spend without a submitted report and the accrual it drives, the coding review that puts entertainment, benefits, and non-deductible items where tax treatment requires, personal spend on company instruments with its recovery mechanism, the approval pattern where one manager clears everything, and the policy gaps where the spend is legitimate and the policy simply does not address it.

The reason this desk exists separately from payables is that the population is people rather than vendors. The same finding written two ways is a control observation or a personnel matter, and which one it becomes depends almost entirely on how the artifact is assembled.

## Use when

- Expense reports need reviewing against the policy for a period, a department, or a specific submission.
- The corporate card program needs reconciling, or unsubmitted card spend has accumulated and the accrual is unknown.
- Items need coding for tax treatment: entertainment, meals, gifts, wellness, commuting, relocation, or anything that is a taxable benefit to the employee.
- Personal spend has landed on a company card and the recovery mechanism has to be established.
- Reimbursements are disputed, delayed, or being paid outside the process.
- An approval pattern looks wrong, for example one approver clearing every submission within seconds of receipt.
- The policy has no answer for a legitimate category of spend and keeps generating exceptions.

## Do not use when

- The spend is a vendor invoice under a purchase order or a contract: `accounts-payable-desk`.
- The spend needed a commitment approval before it happened and did not get one: `spend-approval-authority-desk`.
- The item is compensation, an allowance, or a benefit set by the employment terms rather than a reimbursement: state the accounting here and route the design to the People and Talent suite.
- The tax position itself is the question rather than the coding, for example whether a category is deductible in a jurisdiction: `tax-coordination-desk`.
- The accrual entry needs reviewing and posting with the close package: `month-end-close-desk`.
- The prepaid or accrued balance will not tie to its schedule: `account-reconciliation-desk`.
- The finding has become a conduct matter about an individual rather than a control observation: stop and route it through the named owner rather than widening the artifact.

## Required evidence

- The travel and expense policy in force with its version and effective date, including per diem and mileage rates, receipt thresholds, class of travel provisions, and preferred booking channels.
- Submitted expense reports with line detail, receipts, and the approval record including the approver and the time to approval.
- Corporate card statements and transaction feeds, with the program structure and who holds cards.
- Card transactions with no submitted report, with their age.
- The employee to cost center mapping and the manager hierarchy that sets the approver.
- Tax treatment rules for benefits, entertainment, and non-deductible categories in each jurisdiction where employees are based.
- Prior policy exceptions with how each was handled, and any recovery already in progress.
- The period cutoff and the payroll calendar for the periods in scope.

## Workflow

**Outcome.** A compliance review where every finding names the provision breached, an out-of-policy register with amount, cost center, approver, and disposition, the card reconciliation with unsubmitted spend quantified and the accrual it drives computed, coding assignments for tax treatment with the taxable items identified, personal spend with a recovery mechanism per item, an approval pattern review, and the policy gaps that will keep generating exceptions until the policy is amended.

**Grounding.** The policy in force at the date of the spend governs, not the current version, so a policy that changed mid-period is applied by transaction date. The card feed is the record of what was spent; the expense report is a claim about what it was for. A receipt establishes the merchant and the amount and rarely establishes the business purpose, which is why the business purpose is a written field rather than an inference from the merchant category.

**Constraints.**

- Cite the provision. "Out of policy" without the clause is a judgment about a colleague, and the first question in every dispute is which rule was broken.
- Report by cost center and policy category. Individual detail stays inside the review with the named owner, and an artifact that circulates aggregates rather than names.
- Unsubmitted card spend is an expense whether or not a report exists. Accrue it from the card feed with the coding assumption stated, and age it, because the accrual and the compliance problem are the same population viewed two ways.
- Tax treatment is coding, not judgment about the person. Gift cards, wellness payments, commuting subsidies, and certain relocation costs are taxable to the employee regardless of amount in many jurisdictions, and identifying them before the payroll cutoff is the whole value of catching them.
- Personal spend on a company instrument is a receivable from the employee with a recovery mechanism the policy actually provides. Payroll deduction is available only where the policy and local law permit it, and asserting it where they do not creates a second problem.
- An approval that took four seconds is a control observation about the approval process rather than a finding against the submitter, and it belongs in the pattern section rather than in the individual register.
- A policy gap is recorded as a gap. Where legitimate spend has no provision covering it, the finding is that the policy is silent, and the answer belongs to the policy owner rather than to this review.

Where an item is a taxable benefit, the order is mandated: identify the item and its taxable amount, determine the treatment for the employee's jurisdiction, and deliver it to payroll before the final payroll run of the reporting year. The order is mandated because a taxable benefit identified after the last payroll of the year cannot be adjusted through a subsequent payroll; it requires a corrected wage statement, which is a filing with the tax authority and a conversation with the employee about a prior year.

**Parallel surface.** Expense reports are independent and fan out: policy testing, receipt review, coding, and tax classification each run per report on its own lines. Cardholders fan out per card for the unsubmitted spend review. Three passes are aggregate and run once after the fan-out returns. The accrual is a single computation across the whole unsubmitted population. Approval pattern analysis is inherently population-level, since an approver who clears everything is invisible from inside any one approval. And policy gap identification is a pattern across the exception set, because a single unusual item is an exception and the same item appearing thirty times is a missing policy.

**Acceptance bar.** Every out-of-policy finding names the provision, the amount, the date, and the cost center. Unsubmitted card spend is quantified by age with the accrual computed and its coding assumption stated. Every taxable item names its treatment and the payroll period it must reach. Every personal expense names the recovery mechanism the policy actually provides. The approval pattern review reports at the approver and process level. Policy gaps name the category, the volume, and the decision the policy owner has to make.

## Outputs

A complete run delivers the set:

- `policy-compliance-review.md`: findings by policy provision with the amount, the count, the cost center, and the disposition, aggregated so the artifact can circulate.
- `out-of-policy-register.md`: the detailed register held for the named review owner, with the item, the provision, the approver of record, and the disposition per entry.
- `card-reconciliation-and-accrual.md`: card spend for the period against submitted reports, unsubmitted spend by cardholder aged, the accrual computation with its coding assumptions, and the reversal period.
- `tax-treatment-coding.md`: entertainment, benefit, gift, commuting, and non-deductible items with the account, the jurisdiction treatment, the taxable amount where one arises, and the payroll period it has to reach.
- `personal-expense-recovery.md`: each item with the amount, the date, the instrument, the recovery mechanism the policy provides, and the state of recovery.
- `approval-pattern-review.md`: approval behaviour by approver and by process, including time to approval, exception rates, and any approver clearing spend outside their authority.
- `policy-gap-register.md`: categories the policy does not address with the volume and value they represent, and the decision the policy owner needs to make.
- `expense-management-downstream-handoff.md`: the accrual for close, the taxable items for payroll and tax, and the control observations.

Depth standard: an entry is complete when the disposition can be executed without a follow-up question. A compliance finding names the provision and what the policy requires instead, so the corrective action is obvious. An accrual line states the population, the period, and the coding assumption used in the absence of a submitted report. A taxable item states the amount to be reported and the deadline it has to reach, since the value of the finding evaporates after the payroll cutoff.

Where the run covers one department or one report rather than the program, the accrual and the pattern analysis are scoped to that population and labeled as such. Where the card feed, the expense system, or the policy cannot be read, `expense-management-diagnostic.md` names what was attempted and which figures are unavailable without it.

The hazard specific to this desk is that every finding has a person attached to it. An out-of-policy line is not a variance; it is a written statement that a named colleague broke a rule, and it travels to their manager and sometimes into a performance conversation. A breach asserted against a provision the policy does not contain, a transaction attributed to the wrong cardholder because two employees share a surname, or a personal-use conclusion drawn from a merchant name rather than from the record turns a review into an accusation about a fabricated fact, and the correction never reaches everyone who saw the original. Provisions are quoted from the policy version in force on the transaction date, transactions are attributed by card and employee identifier rather than by name matching, an item whose business purpose the record does not establish is marked `purpose_not_documented` rather than characterised as personal, and full card numbers never enter an artifact at all.

## finance_packet fields to update

- `expenses.policy_ref` with its version and effective date, and `expenses.card_program` with the program structure.
- `expenses.out_of_policy[]` with item, amount, provision breached, cost center, approver, and disposition.
- `expenses.unsubmitted` with the aged total and the accrual it drives, and `expenses.reimbursement_state`.
- `expenses.personal_expense_recovery[]` with the amount and the recovery mechanism.
- `payables.accrued_liabilities[]` for the unsubmitted spend accrual with its basis and reversal period.
- `controls.deficiencies[]` seeded where an approval pattern or a segregation issue arises, and `basis.policy_conflicts[]` where practice diverges from the written policy.
- `source_facts` with the policy version, card feed, and expense system locators and their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Security or privacy**: expense detail exposes individual travel, health, family, and personal circumstances, and card data is payment data. Halt where an artifact would name employees alongside their spending detail outside the named review owner, would carry full card numbers or personal identifiers, or would circulate medical, legal, or personal context that appeared in a receipt. Aggregate by cost center and policy category for anything that travels.
- **Approval**: recovering money from an employee, deducting from pay, denying a submitted reimbursement, granting a policy exception, or amending the policy. Each has an employment consequence and belongs to the policy owner and the people function rather than to the review.
- **Production or destructive**: the next act would release a reimbursement payment, post the accrual, adjust payroll, or close an employee's card.
- **Source conflict**: the card feed and the submitted report disagree on a transaction, the policy version in force at the date of spend is disputed, or the approver of record differs between the expense system and the manager hierarchy. Record both readings and route it.
- **Release integrity**: an accrual or a compliance rate would go into the statements, to the board, or to an auditor without the card feed and the policy behind it.
- **Connector unreachable**: the expense system, the card feed, or the policy library exists and cannot be read, so unsubmitted spend would be estimated from what a program of this size usually carries.

A receipt below the threshold, a business purpose written thinly, an employee on leave who has not submitted, and a coding decision awaiting a jurisdiction view are soft gaps. State the treatment the record supports, label the assumption against that report or cardholder, and record what would settle it.

## Downstream handoffs

`month-end-close-desk` takes the unsubmitted spend accrual with its computation and its reversal period, and the coding assignments. `tax-coordination-desk` takes the non-deductible population and the indirect tax reclaim positions. Payroll takes the taxable benefit items before the cutoff, routed through the People and Talent suite where the item touches employment terms. `account-reconciliation-desk` takes the card clearing account and the employee receivable balance with their supporting detail. `internal-controls-desk` takes the approval pattern findings and any case where one person submits, approves, and codes. `accounting-policy-coa-desk` takes the policy gap register, because a category that generates thirty exceptions a quarter is a policy that needs a provision.

## Quality bar

A good expense review is precise about rules and careful about people. Findings cite the provision, so the conversation is about the policy rather than about character. Aggregates travel and detail stays with the owner who needs it. The unsubmitted card population is quantified and accrued rather than mentioned, because it is simultaneously the largest compliance problem and the largest missing expense in most programs. Taxable items are caught before the payroll cutoff, since afterwards the same finding costs a corrected filing. And the policy gap register is treated as the most useful output of all, because a rule that generates the same exception every month is a defect in the rule.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
