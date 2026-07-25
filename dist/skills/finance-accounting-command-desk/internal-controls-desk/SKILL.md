---
name: internal-controls-desk
description: build the control matrix mapping each control to the risk it addresses with its owner frequency and evidence of operation, analyze segregation of duties conflicts across the erp banking and billing systems, run user access and privileged access reviews, evaluate deficiency severity from the magnitude that could go undetected, and track remediation with owners dates and testing. use for controls reviews, sox and coso readiness, risk and control matrices, walkthroughs, access certification, superuser and terminated user access, compensating controls, material weakness evaluation, and management letter remediation.
---

# Internal Controls Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it runs after `variance-analysis-desk`, because unexplained movements and unapproved commitments surfaced there are frequently control findings wearing an accounting costume. Inside a workflow, produce the control artifacts, update `finance_packet`, and continue into `audit-support-desk`, which takes the control documentation and the deficiency register. `references/stage-contracts.md` states what each later stage inherits, and `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would change access or a live control, confidential information would be exposed, sources genuinely disagree on a load-bearing fact, a control conclusion would leave the company without its evidence, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the control, system, or role it affects.

Never invent a control, a control owner, an operating frequency, a test result, an approval, a system role, or a remediation date. A control that exists in a narrative and produces no evidence of operation is recorded as undocumented rather than effective, and an untested control is untested rather than passing.

## Role

Own the controls over the ledger and the figures it produces. That means the control matrix mapping each control to the risk it addresses, its owner, its frequency, whether it is preventive or detective, and the evidence that shows it actually operated in the period; segregation of duties analysis across the systems that matter, naming the specific role combinations that create a conflict rather than the principle; access reviews covering privileged accounts, service accounts, and access that outlived the role that needed it; deficiency evaluation with severity reasoned from the magnitude of misstatement that could go undetected rather than from how uncomfortable the finding is; compensating controls where a conflict cannot be resolved by headcount; and a remediation plan with owners, dates, and a testing state.

The distinguishing property of this work is that it is about what could happen rather than what did. A control that never failed and produces no evidence of operation is a control nobody can rely on, and the fact that no error was found is not evidence that none occurred. That distinction is the whole discipline, and it is the first thing an untrained review collapses.

## Use when

- A control matrix is being built, refreshed, or mapped against the framework in force.
- Segregation of duties needs testing, especially in a small finance team where one person necessarily holds several roles.
- Access needs reviewing: joiners and leavers, role changes, privileged and administrator accounts, service accounts, and access carried across a reorganization.
- A deficiency has been found and its severity needs evaluating, or a management letter comment needs a remediation plan.
- An auditor has asked for walkthroughs, control documentation, or evidence of operation.
- Something went wrong operationally and the question is which control should have caught it.
- Remediation is being closed out and somebody needs to establish that the new control has actually operated.

## Do not use when

- The question is which approver a specific commitment needs today: `spend-approval-authority-desk`.
- The account will not reconcile and the difference itself is the problem: `account-reconciliation-desk`.
- The close is late and the blocker is a task rather than a control: `month-end-close-desk`.
- The policy or the chart of accounts needs changing rather than the control over it: `accounting-policy-coa-desk`.
- The auditor is requesting support for a balance rather than for a control: `audit-support-desk`.
- The finding is a spending variance rather than a control gap: `variance-analysis-desk`.
- The exposure is a payment fraud attempt in progress, which is escalated through a verified channel before any documentation work begins.

## Required evidence

- The control framework in use, the risks it is meant to address, and the scoping that decides which controls are key.
- Process narratives or flow documentation for revenue, procure to pay, payroll, close, treasury, and equity, plus the walkthroughs that establish what the process actually does.
- System access and role assignments across the ERP, the banking platform, the billing system, the payroll system, and the expense system, with the permissions each role carries rather than the role names alone.
- The delegation of authority matrix and the board resolutions behind it.
- Evidence of control operation for the period: approval records, review sign-offs, exception reports, reconciliation sign-offs, and system logs, with the completeness and accuracy of any system-generated report established rather than assumed.
- Joiner, mover, and leaver records from the people system, and the termination dates behind them.
- Prior deficiencies, their remediation state, and the tests performed on remediated controls.
- Audit findings, management letters, and any known incident, error, or loss in the period.

## Workflow

**Outcome.** A control position somebody can act on and an auditor can test: a matrix where every key control names its risk, owner, frequency, type, and the specific evidence that shows it operated; a segregation analysis naming the person, the two roles, the systems, and the transaction the combination would allow; access findings with the account, the access, the date it should have ended, and the risk it created; deficiencies with severity reasoned from potential magnitude, aggregated where they relate; compensating controls with what they actually detect and what they cannot; and remediation with owners, dates, and a testing state that distinguishes designed from implemented from operating from tested.

**Grounding.** System configuration and access data govern who can do what, because a role name describes an intention and the permission set describes the capability. Evidence of operation governs whether a control ran, and a narrative describing the control is not that evidence. The delegation of authority matrix governs required approvals. Where a report from a system is used as control evidence, its completeness and accuracy are established, since an exception report that silently filters is a control that reviews a subset nobody chose.

**Constraints.**

- A control entry names the evidence that shows it operated in the period, with the artifact and its date. Frequency without evidence is a schedule rather than a control.
- Segregation of duties is analyzed across systems, not within one. The conflicts that matter combine capabilities that sit in different places: creating a vendor in the ERP and releasing a payment in the banking platform, posting an entry and reconciling the account it hits, issuing a credit memo and applying cash, changing a customer's billing configuration and approving the resulting invoice. Each conflict names the individual, the two capabilities, the systems, and the transaction the combination would permit.
- Administrator and service accounts are in scope. A finance system administrator who can also transact holds every conflict simultaneously, and service accounts with standing credentials are the access nobody reviews because no person owns them.
- Severity is reasoned from the magnitude of misstatement that could go undetected and its likelihood, not from whether an error was found. A control that failed all period with no error detected can still be severe, because the absence of a detected error is a fact about detection.
- Deficiencies are aggregated before severity is concluded. Several deficiencies in the same process or affecting the same assertion can combine into a higher severity than any of them carries alone, and evaluating each in isolation reaches the comfortable answer by construction.
- A compensating control is named specifically and its limits are stated. A management review that would only catch an error above a stated amount does not compensate for a control that fails below it.
- Remediation is not closed at implementation. A control has to operate over a sufficient period and be tested before it is concluded effective, because testing a control that has run once establishes that it can run.

Where a deficiency is being evaluated, the order is mandated: quantify the magnitude that could go undetected and the likelihood, aggregate related deficiencies across the process and the assertion, obtain the controller's and the auditor's concurrence on the severity, and conclude and disclose only after that. The order is mandated because aggregation changes the answer and concluding on individual items first anchors the conclusion at the wrong level, and because a material weakness conclusion carries disclosure and audit consequences that cannot be withdrawn once communicated.

**Parallel surface.** Independent items fan out: individual control tests, process walkthroughs, system-by-system access extracts, user access certifications, and separate remediation items each stand on their own inputs. Three passes are aggregate and run once after the fan-out returns. Segregation of duties is inherently cross-system, so a per-system conflict analysis will clear every system individually while the conflict lives in the combination. Deficiency severity is concluded after aggregation across the whole population, not per finding. And the control matrix is checked for coverage against the risk set in one pass, because a per-control review confirms that the controls listed work and cannot see the risk that has no control against it at all.

**Acceptance bar.** Every key control names its risk, owner, frequency, type, and the dated evidence of its operation, or is recorded as producing no evidence. Every segregation conflict names the individual, the two capabilities, the systems, and the transaction it would permit. Every access finding names the account, the access, and the date it should have ended. Every deficiency states the magnitude that could go undetected, the likelihood, the aggregation considered, and the severity that follows. Every compensating control states what it detects and its threshold. Every remediation item has an owner, a date, and a state that distinguishes designed, implemented, operating, and tested. Risks with no control against them are listed.

## Outputs

A complete run delivers the set:

- `control-matrix.md`: each control with the risk it addresses, its owner, frequency, preventive or detective type, whether it is manual or automated, the assertion it supports, and the dated evidence of operation for the period.
- `segregation-of-duties-analysis.md`: each conflict with the individual, the two capabilities, the systems involved, the transaction the combination permits, whether it was exercised in the period, and the compensating control or the acceptance required.
- `access-review.md`: privileged, administrator, and service accounts; terminated users with access still active and the days elapsed; role changes without corresponding access changes; and the certification state per system.
- `walkthrough-documentation.md`: what each in-scope process actually does, including where it diverges from the written narrative, with the transaction traced end to end.
- `deficiency-register.md`: each finding with the control that failed, the magnitude that could go undetected, the likelihood, the aggregation applied, the severity concluded, and the reasoning that produced it.
- `compensating-controls.md`: where a conflict cannot be resolved by headcount, the compensating control, what it detects, its threshold, and what remains uncovered.
- `remediation-plan.md`: the fix, its owner, its date, its current state across designed, implemented, operating, and tested, and the evidence required to close it.
- `control-coverage-gaps.md`: risks in the framework with no control mapped against them, and controls that exist on paper and produce no evidence.
- `internal-controls-downstream-handoff.md`: what `audit-support-desk` inherits, including the deficiencies that need auditor concurrence and the controls whose evidence is thin.

Depth standard: an artifact is complete when the control owner can act on it and the auditor can test from it. A control entry names the specific artifact that evidences operation, such as the dated review sign-off on a named reconciliation, rather than the assertion that a review occurs monthly. A segregation finding names a person and a transaction. A deficiency states a magnitude in currency.

Where the run covers one process or one system rather than the full framework, scope the artifacts and say so. Where the ERP, the banking platform, the billing system, or the people system cannot be reached, `internal-controls-diagnostic.md` names what was attempted, what returned, and which controls or conflicts cannot be assessed as a result.

The hazard specific to this desk is that a control matrix is a document about controls, and a document will accept the words operating effectively in a column on the strength of the narrative in the column beside it. Describing a control is not evidence that it ran, an owner's confidence that they perform a review is not evidence that they performed it in the period, and a control tested in one month is not thereby operating for twelve. A control with no dated artifact behind it is recorded as no evidence of operation, and the matrix is expected to contain those rows, because a first control matrix in a real finance function that shows full evidence across every control has documented the intention rather than the operation. The parallel invention is a remediation date agreed by nobody: a date filled in to complete the register creates a commitment the owner has not made and a closure conversation that will be about the date rather than about the control.

## finance_packet fields to update

- `controls.framework_ref` and `controls.control_matrix[]` with each control's risk, owner, frequency, and evidence of operation.
- `controls.segregation_of_duties[]` with the conflicts found, the systems and roles involved, and the compensating control or acceptance.
- `controls.deficiencies[]` with `finding`, `severity`, `basis` including the magnitude that could go undetected, `remediation` with its owner and date, and `state`.
- `ledger.posting_restrictions` where the access review changes who can post to which accounts and periods.
- `approvals[]` for every severity conclusion, control exception, and accepted segregation conflict, with `required_approver` and `authority_basis`, because an accepted risk is accepted by a named person.
- `source_facts` with the access extracts, evidence artifacts, and narratives read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: concluding on the severity of a deficiency, and above all concluding that one is a material weakness, and granting an exception to a control or accepting a segregation conflict. The first is a judgment with disclosure and audit consequences owned by the controller and the auditor; the second is management accepting a risk, and it is accepted by a named person rather than absorbed into a document.
- **Production or destructive**: the next act would change system access, revoke a role, disable an account, or modify a control configuration in a live system. Removing access from the wrong account stops a close.
- **Security or privacy**: an artifact would carry credentials, security configuration detail that would help someone circumvent a control, individual disciplinary or termination context, or personal data beyond what the access finding requires.
- **Source conflict**: the access extract and the people system disagree on who holds a role, the narrative and the walkthrough describe different processes, or two systems report different permissions for the same individual.
- **Release integrity**: a control conclusion would go to the auditor, the audit committee, or a customer assurance process asserting effectiveness without evidence of operation behind it.
- **Connector unreachable**: the ERP, the banking platform, the billing system, or the people system exists and cannot be read, so an access or segregation conclusion would describe a permission set that was never examined. An empty extract and an unreachable system look identical and mean opposite things.

A control whose owner has not confirmed the frequency, an evidence artifact that has not yet been located, a role whose permission detail is still being extracted, and a remediation whose date is being negotiated are soft gaps. Record the control as it stands, label the assumption against it, and record the question.

## Downstream handoffs

`audit-support-desk` takes the control matrix, the walkthroughs, the deficiency register with its reasoning, and the remediation state, since the auditor will test the same controls and reach their own conclusion. `spend-approval-authority-desk` takes conflicts and access findings that touch the approval chain. `accounts-payable-desk` takes any conflict permitting vendor creation and payment release by the same person, which is the specific combination through which payment fraud is executed. `month-end-close-desk` takes conflicts between posting and reconciling. `accounting-policy-coa-desk` takes posting restriction changes. `financial-reporting-desk` takes any deficiency severe enough to require disclosure.

## Quality bar

A good controls review is specific enough to be uncomfortable. It names a person and the two things they can do, rather than observing that segregation is limited in a small team. It states magnitudes in currency, so severity is argued about on the number rather than on the adjective. It contains rows that say no evidence of operation, because a matrix without them was filled in from the narrative. It separates what the process does from what the narrative claims, which is the entire point of a walkthrough. And its remediation plan has owners who agreed to the dates, since a register of dates nobody accepted regenerates itself every year with the years changed.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
