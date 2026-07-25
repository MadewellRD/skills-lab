---
name: vendor-offboarding-desk
description: execute a supplier exit by preparing the termination or non-renewal notice in the form and method the clause requires, sequencing transition with a realistic overlap, retrieving company data in the contracted format while the agreement is still in force, deprovisioning the supplier's access and the company's accounts on the supplier's platform, obtaining the deletion certification the contract requires, settling final invoices credits and unused prepayment, and listing the obligations that survive termination. use for vendor termination and non renewal, contract exit and transition planning, supplier data return and export, certificate of deletion, access deprovisioning and offboarding, final settlement and disputed amounts, and surviving obligations after a supplier relationship ends.
---

# Vendor Offboarding Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, prepare the exit, execute the reversible parts, produce the artifact set, update `procurement_packet`, and continue by returning the closure record to `procurement-vendor-management-command-desk` and the exit into `spend-analysis-desk` so it shows up in the next baseline. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the action boundary that keeps the notice, the deprovisioning, and the final payment behind named owners.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the exit step it affects.

Never invent a termination clause, a notice period, a notice address or method, a transition assistance obligation, a data retrieval window, an export format, a deletion certificate, a deprovisioning confirmation, a final balance, a credit, an unused prepayment, or a surviving obligation the agreement does not contain.

## Role

Own the exit as an operation with a deadline rather than as a decision that has been taken. The decision to leave is the easy part; what makes an exit succeed or fail is that several of its steps destroy the means of performing the others, and the sequence is governed by dates the supplier controls. Retrieval capability is commonly switched off on the termination effective date, the transition assistance obligation ends with the term, deprovisioning removes the access an extraction needs, and the final payment is the last leverage that exists to obtain a deletion certificate.

The company's data is the asset at risk. Everything else in an exit can be repeated at some cost; an export not taken before the service ends is generally gone, whatever the clause promised, and the discovery happens weeks later when somebody needs a record. The second asset at risk is the record itself: an exit that ends without a deletion certificate, a deprovisioning confirmation per system, and a list of surviving obligations leaves the company with a supplier that still holds data, still holds access, and still holds rights nobody is tracking.

## Use when

- A decision to terminate, not renew, or replace a supplier has been taken and the exit has to be executed.
- A notice has to be prepared in the exact form, to the exact addressee, by the exact method the clause requires.
- Company data has to be retrieved from a supplier's platform before a term ends, in the format and inside the window the contract grants.
- The supplier's access to company systems and the company's own accounts, tokens, and integrations on the supplier's platform have to be removed and confirmed.
- A deletion obligation has to be enforced and its certification obtained and recorded.
- A final settlement is needed covering last invoices, credits owed, unused prepayment, early termination charges, and disputed amounts.
- Surviving obligations have to be listed with their durations, because confidentiality, audit rights, IP terms, and data protection obligations outlive the relationship.
- A supplier is being replaced and the transition needs sequencing with a realistic overlap period.
- A supplier has failed and an exit is being executed under time pressure with the contract's cure and termination provisions in play.

## Do not use when

- The decision has not been made and the renewal position, deadline, or consolidation case is the question: `renewal-consolidation-desk`.
- The exit is hypothetical and the question is whether one could be executed at all: `supplier-relationship-governance-desk`, which owns exit readiness.
- A replacement has to be sourced: run the sourcing sequence from `requirements-specification-desk` forward, alongside this exit rather than after it.
- The dispute is contractual and needs enforcement, a claim, or a termination for cause opinion: prepare the evidence here and route the claim to the Legal Contracts suite.
- The performance case that justifies termination for cause has not been built: `supplier-performance-sla-desk`.
- The system decommissioning, data migration engineering, or integration teardown is the work rather than the supplier exit: route it to the SDLC suite with the retention obligation and the acceptance criteria attached.

## Required evidence

- The executed agreement with its termination, non-renewal, transition assistance, data return, deletion, and survival clauses, plus every amendment.
- The notice provision in full: the period, the addressee, the address, the method, any copy-to requirement, and what constitutes delivery.
- The termination basis being relied on and the clause that supports it, including any cure period that must run first.
- The data the supplier holds: scope, systems, volume, formats available for export, and what the export tooling does not include such as attachments, audit logs, historical versions, or metadata.
- The retrieval window the contract grants after termination, and what the supplier disables on the effective date.
- The access footprint in both directions: the supplier's accounts and access into company systems, and the company's accounts, service accounts, API tokens, integrations, webhooks, single sign-on applications, and provisioning connectors on the supplier's platform.
- The replacement plan and the overlap period both suppliers will run in parallel.
- Financial position: outstanding invoices, credits owed, unclaimed service credits, unused prepayment or committed balance, early termination charges, and disputed amounts.
- Retention obligations: what the company must keep for tax, audit, legal hold, or regulatory reasons, and where it will live.
- The knowledge that exists only inside the supplier relationship, and the internal owner and affected users.

## Workflow

**Outcome.** A termination package with the basis, the clause, and the notice prepared to the required form and method, a transition plan with a realistic overlap, a data return specification executed while the agreement is in force, a deletion obligation with its certification tracked, a deprovisioning record covering both directions with dates and named confirmers, a final settlement position, a record retention position, a knowledge transfer plan, a residual dependency register, and a list of surviving obligations with their durations.

**Grounding.** The executed agreement defines what the company can require and by when. A supplier's stated offboarding process is a service description, not an obligation, and the two differ most on the points that matter: the export format, the retrieval window, and what the deletion actually covers. Where the contract is silent, that is recorded as a gap the company has no right to close rather than as a process the supplier will presumably follow.

**Constraints.**

- Prepare the notice to the clause: the correct addressee, the correct address, the required method, any copy to legal, and the evidence of delivery the clause treats as effective. A notice sent by an unspecified method to an unspecified address is contested at exactly the moment it matters.
- Where termination is for cause, confirm the cure period has run and is documented before the notice relies on it, because a defective for-cause notice frequently converts into a termination for convenience with its charges attached.
- Specify the data return before the term ends: scope, format, completeness, and what the export does not include. Run the export early enough that a second attempt is possible inside the window.
- Deprovision in both directions and confirm each. The company's own accounts, tokens, and integrations on the supplier's platform are routinely forgotten, and they are the ones that keep sending data after the relationship ends.
- Treat the deletion certificate as a deliverable with an owner and a date, covering backups and subprocessors, and obtain it while payment is still outstanding.
- Settle last, and settle against the contract: unused prepayment, unclaimed credits, and early termination charges are all live at this point and none of them collects itself.
- List surviving obligations with durations. Confidentiality, IP, audit rights, liability provisions, and data protection terms do not end when the service does, and neither do the company's own obligations to the supplier.
- Register residual dependencies honestly. Anything still calling the supplier's interface, any embedded script, and any record the company cannot reproduce internally after the exit date is a live dependency regardless of what the plan said.

**Mandated order.** The exit sequence below is externally constrained and each step destroys the means of performing an earlier one, so it is kept as an order rather than as guidance:

1. Serve notice in the form and by the method the contract requires, inside the window.
2. Retrieve the company's data while the agreement is still in force, in the format and inside the retrieval period the exit clause grants.
3. Remove the supplier's access to company systems, and the company's accounts and integrations on the supplier's platform.
4. Obtain the deletion certification the contract requires, covering backups and subprocessors.
5. Settle the final invoices, credits, and unused prepayment, and close the record with the surviving obligations listed.

Retrieval is commonly disabled on the termination effective date and transition assistance ends with the term, so data not extracted before then is gone regardless of what the clause promised. Deprovisioning ahead of extraction removes the access the extraction needs. Final payment is the last leverage that exists to obtain a deletion certificate, and a supplier paid in full has no commercial reason to produce one.

**Parallel surface.** Independent items fan out and are parallel safe within the sequence above: each system's deprovisioning once extraction is complete, each data domain's export, each open invoice and credit line, each surviving obligation's assessment, and the knowledge transfer topics. Where several suppliers are being exited, each exit runs independently. Two things are single passes. The exit sequence itself is not parallelized across its numbered steps, for the reason stated above. The closure position is one pass at the end, since an exit is complete or it is not and a closure assembled from a finished extraction, an unconfirmed deprovisioning, and an outstanding deletion certificate is an open exit with three documents in front of it.

**Acceptance bar.** The notice quotes its clause and names the addressee, the method, and the deadline. The data return states scope, format, what the export omits, the window, and the date it was taken. Every deprovisioning line names the system, the direction, the date, and the person who confirmed it. The deletion certification is either received and recorded or listed as outstanding with the owner and the leverage still available. The final settlement reconciles invoices, credits, prepayment, and charges to a stated position. Surviving obligations are listed with durations. Residual dependencies are named rather than declared closed.

## Outputs

A complete run delivers the set:

- `termination-package.md`: the basis, the clause relied on, any cure period and its evidence, the notice text, the addressee and address, the method, the copy-to requirements, the delivery evidence required, and the deadline for sending.
- `transition-plan.md`: the replacement, the sequence, the overlap period both suppliers run in parallel, the cutover dependencies, and the transition assistance the contract obliges with its duration and fee.
- `data-return-specification.md`: scope by system and data domain, the export format available against the format the contract requires, what the export does not include, the retrieval window and its hard end date, the extraction dates, and the completeness position.
- `deletion-obligation-record.md`: what the contract requires deleted, the scope including backups and subprocessors, the certification form required, the owner, the date requested, and the state.
- `deprovisioning-record.md`: a line per system in both directions covering supplier accounts in company systems and company accounts, service accounts, API tokens, integrations, webhooks, single sign-on applications, and provisioning connectors on the supplier's platform, each with the date and a named confirmer.
- `final-settlement.md`: outstanding invoices, credits owed and unclaimed, unused prepayment or committed balance, early termination charges, disputed amounts with the basis for each, and the resulting position.
- `record-retention-position.md`: what the company keeps, where it now lives, in what format, for how long, and under which obligation, including anything under legal hold.
- `knowledge-transfer-plan.md`: what only the supplier knows, who receives it, in what form, and by when, with the items that will not transfer stated.
- `residual-dependency-register.md`: anything still running on, calling, or embedded from the supplier after the stated exit date, with an owner and a removal date.
- `surviving-obligations.md`: the clauses that outlive the agreement in both directions, with their durations and the owner of each on the company side.
- `vendor-offboarding-closure-record.md`: the exit summarized for the record, with everything still open named.

Depth standard: an artifact is complete when someone could execute the exit from it without opening the contract, and audit it afterward without asking anyone. "Data will be returned" is an expectation; "the named export covering the stated domains in the stated format, excluding attachments and audit history which are not in scope of the export tool, taken on a stated date, inside a retrieval window that ends on the termination effective date after which the tenant is disabled" is a specification.

Where the agreement is silent on data return, deletion, or transition assistance, the artifact says so explicitly with what the company therefore cannot require, since that silence is the finding and it belongs in the requirements for the replacement. Where the supplier's platform, the contract, or the access records cannot be reached, `vendor-offboarding-diagnostic.md` names the gap and states which exit steps cannot be evidenced.

An exit record is written in the same grammar as an exit plan, and that single fact is where this desk goes wrong. Every line is a claim that a specific act was performed, on a date, by a person, and the tense is the only thing separating "accounts removed" from "accounts to be removed"; both look like completed work in a closure summary, and the whole document is read as a record of what happened. Nobody re-opens it until the moment it fails: an access review that finds a live service account eight months later, a data subject request that reaches a supplier the company believed had deleted everything, or a customer audit asking for the deletion certificate. So each line here carries the date and the person who confirmed it or it is written as outstanding; a deletion certificate that has not arrived is recorded as outstanding with the payment still held rather than as an obligation discharged; a data export nobody has opened is recorded as taken but not confirmed complete; and an integration somebody believes was switched off is a residual dependency until a named person says otherwise.

## procurement_packet fields to update

- `offboarding.termination_basis`, `notice_state`, `transition_plan`, `data_return`, `data_deletion`, `access_deprovisioning`, `final_settlement`, `record_retention`, `knowledge_transfer`, `residual_dependency`.
- `contract.execution_state` and the surviving obligations carried into `key_obligations` with their durations and owners.
- `leverage_window` moved to the termination or post-termination state, and `commitment_class` updated, since a supplier still holding data is still a production dependency after the service ends.
- `relationship.exit_readiness` corrected against what the exit actually proved, which is the only real test that assessment ever gets.
- `spend.by_supplier` context so the exit is visible in the next baseline rather than appearing as an unexplained reduction.
- `approvals` for the notice, each deprovisioning action, the settlement, and the final payment release.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Production or destructive**: serving the notice, disabling access, deleting company-side records, and releasing the final payment. Each is irreversible and each sits in a sequence where doing it early destroys something. Deprovisioning before extraction removes the access the extraction needs; paying in full before the deletion certificate arrives removes the only leverage that produces it.
- **Approval**: the termination decision itself, the basis relied on, any early termination charge accepted, the settlement position, the write-off of a disputed amount or an unused prepayment, and the release of final payment. Each has a named authority.
- **Security or privacy**: the supplier holds personal or customer data and the deletion obligation cannot be evidenced, or an export containing personal data would be moved to a destination that has not been approved for it. An exit that ends with data at a former supplier and no certificate is an open processing relationship the company has stopped managing.
- **Source conflict**: the agreement and the amendment state different termination or notice terms, the supplier disputes the basis or the effective date, or the contract and the supplier's platform disagree about the retrieval window. Record both readings with their locators; the effective date is the fact everything else in the sequence depends on.
- **Release integrity**: an exit would be recorded as complete, into an audit response, a customer questionnaire, a regulator submission, or a risk register, when the deletion certificate is outstanding, deprovisioning is unconfirmed, or a residual dependency is still live.
- **Connector unreachable**: the executed agreement, the supplier's administration console, or the access records exist and cannot be read, so the notice terms, the retrieval window, or the account inventory would be assumed at the one point in the relationship where assumptions expire on a fixed date.

An unanswered request for an export format, a supplier who has not yet confirmed the effective date, an unreconciled credit line, and a knowledge transfer session not yet scheduled are soft gaps. Record each with its owner and its own deadline against the exit date, and continue the steps that do not depend on it; the exit date does not move because a question is open.

## Downstream handoffs

`spend-analysis-desk` inherits the exit so the reduction appears in the next baseline attributed rather than as an unexplained drop, and so any residual spend after the exit date is visible. `supplier-relationship-governance-desk` inherits what the exit actually proved about exit readiness, switching cost, and switching lead time, which is the only evidence that assessment ever gets and is usually less flattering than the plan. `procurement-vendor-management-command-desk` receives the closure record with everything still open. `requirements-specification-desk` inherits the exit requirements this experience showed were missing, so the replacement agreement contains the data return format, retrieval window, and deletion certification that this one did not. `contract-execution-routing-desk` inherits the surviving obligations for the obligation register, because they persist with owners and dates after the file is closed.

## Quality bar

A good exit is one nobody has to revisit. The notice went by the method the clause named and there is evidence of delivery. The data came back before the door closed, in a format somebody has opened, with the gaps in the export written down. Every account in both directions is accounted for, with a date and a name against each. The deletion certificate is in the file, obtained while the company still had the payment. The settlement collected the prepayment and the credits rather than leaving them with the supplier out of fatigue. And the closure record lists what is still open, including the integration that turned out to still be calling the supplier's interface, because the honest version of that list is what prevents the same exit being declared complete twice.
