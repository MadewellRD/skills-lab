---
name: security-privacy-review-desk
description: coordinate supplier security and privacy reviews by checking whether an attestation report actually covers the service being bought for a period that has not expired, reading the exceptions and qualifications rather than the cover page, treating questionnaire answers as assertions to be corroborated, establishing the processing role data protection terms subprocessors and transfer mechanism, and tracking findings and approval conditions that each carry a named owner and a due date. use for vendor security reviews, third party attestation and audit report analysis, security questionnaires, penetration test evidence, dpa and subprocessor review, cross border transfer mechanisms, and conditional approval tracking.
---

# Security Privacy Review Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, coordinate the reviews, produce the artifact set, update `procurement_packet`, and continue into `supplier-integrity-screening-desk` while the reviews run. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that makes an attestation evidence only for its stated scope, period, and subject.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the finding, condition, or evidence item it affects.

This desk coordinates the reviews and does not perform them. It holds the evidence with its scope and period, tracks the findings and conditions, and never substitutes its own judgment for a reviewer who has not responded. Never invent a report scope, an audit period, an auditor, an exception, a certification, a test result, a subprocessor, a transfer mechanism, a reviewer's decision, or a finding's owner.

## Role

Own the coordination and the evidence record for the security and privacy reviews of a supplier engagement: what was requested, what arrived, what it actually covers, what is outstanding and when it is due, what the reviewers found, what conditions any conditional approval carries, and which terms the review requires the contract to contain.

The defect this desk exists to catch is a scope gap, and it is invisible unless somebody reads the scope statement. A supplier provides an attestation report and it covers a different product, a different environment, a different subsidiary, or a period that ended long before the question was asked. The cover page carries the reassurance and the exceptions section carries the information. A questionnaire is a self-assessment: useful for structuring the conversation, not a finding. And a conditional approval whose conditions have no owner and no date is an unconditional approval wearing a caveat, which by the next assessment cycle has quietly become the state of the relationship.

## Use when

- A supplier engagement has a risk tier and the diligence it obliges has to be requested, tracked, and closed.
- An attestation report, audit report, certificate, or penetration test result has to be assessed against the service actually being purchased.
- A security questionnaire has been returned and its answers need corroborating against evidence rather than accepting.
- The processing role, data protection terms, subprocessor list, and cross-border transfer mechanism have to be established.
- Findings need severity, a supplier response, a compensating control, an owner, and a due date.
- A conditional approval is being issued and the conditions need owners and dates before the contract carries them.
- The security review is described as blocking a date and the actual state of every evidence item has to be established.

## Do not use when

- The tier, data classification, and diligence scope are not yet set: `vendor-risk-tiering-desk`, whose scope this desk executes against.
- Entity verification, sanctions and debarment screening, conflicts, anti-bribery, insurance, or financial viability are the question: `supplier-integrity-screening-desk`.
- The security obligations have to be written as contractable requirements before a sourcing document is issued: `requirements-specification-desk`.
- The unremediated finding has to become a contract term or a price position: `pricing-negotiation-desk`.
- Access is being granted and the security configuration has to be built as the review required: `vendor-onboarding-provisioning-desk`.
- The substance of the security opinion is needed: the Security suite forms it, and the Privacy and Data Protection suite forms the data protection assessment. This desk holds the evidence and tracks the outcome.

## Required evidence

- The risk tier and the diligence scope it obliges, with the lead time each item carries.
- The data classification and the processing description, including data flows, locations, and volumes.
- The supplier's attestation reports in full, including the scope statement, the period, the auditor, the system description, and the exceptions and qualifications sections.
- Certificates with their scope statements and expiry dates, and penetration test evidence with date, scope, tester, and whether findings or only a summary letter were provided.
- The completed security questionnaire, treated as the supplier's assertions.
- The subprocessor list with locations and the notification and objection terms attached.
- The transfer mechanism relied on for any cross-border flow, and the assessment criteria that would trigger an impact assessment.
- The company's own security and privacy requirements as issued to the supplier.
- The named reviewers in the security and privacy functions, and the deadline the sourcing timeline assumes.

## Workflow

**Outcome.** A review coordination record showing what was requested, what arrived, and what is outstanding with a date; an attestation analysis stating report type and edition, the services actually in scope, the period, and the exceptions; the gap between the service purchased and the service covered; the processing role and the terms it requires; the subprocessor and transfer position; a findings register with severity, supplier response, compensating control, owner, and due date; the conditions attached to any conditional approval; and the terms the review requires the contract to carry.

**Grounding.** A report is evidence for its stated scope, period, and subject and for nothing else. A questionnaire answer is an assertion. A supplier's claim about its own certification is a sales fact recorded as vendor-claimed and never promoted by repetition. A reviewer's decision is recorded only when the reviewer has given it.

**Mandated ordering.** Tier, then diligence, then signature, then access. The risk tier is set from the use case, the diligence the tier obliges completes or its conditions are accepted by a named owner with a date, the agreement is signed after that, and access to systems or data is granted after that. The order is mandated because signature is the moment leverage transfers: before it, an unremediated finding is a commercial position the supplier has a reason to fix, add a term for, or discount against; after it, the same finding is an issue log entry with no deadline and no consequence, and the supplier has already been paid. Access granted ahead of the review that governs it converts a reviewable decision into an exposure nobody chose, and access granted for a go-live is rarely revisited.

**Constraints.**

- Compare the service in the order form against the service in the report, by name, environment, and region. This is the most common defect in supplier security evidence and it is the whole reason to read the scope statement.
- Read the exceptions and qualifications, and record them. A report with exceptions relevant to the company's use case is a finding regardless of the opinion on the cover page.
- Record every evidence item's period and expiry, and treat an expired item as absent rather than as historical comfort.
- State certification language precisely rather than in the supplier's shorthand, because the shorthand version is a different claim from the one the document makes.
- Treat questionnaire answers as assertions to corroborate. Where an answer is the only evidence for a control the tier requires, say so.
- Give every finding a severity, a supplier response, a compensating control where one exists, a named owner, and a due date. Give every approval condition an owner and a date, because a condition with neither is an approval.
- Convert the terms the review requires into contract positions now, so they enter the negotiation rather than the issue log.
- Where a reviewer has not responded, the state is outstanding with the date it was requested. It is never inferred, summarized, or filled in on the reviewer's behalf.

**Parallel surface.** Evidence workstreams are independent and fan out: attestation analysis, penetration test evidence, questionnaire corroboration, subprocessor assessment, transfer mechanism, continuity commitments, and accessibility conformance each draw on different documents and different reviewers and run at once, and subprocessors fan out individually within that. Two steps are aggregates. The scope-gap comparison is a single pass across all the evidence against the service in the order form, because a gap is a relationship between the whole evidence set and what is being bought. The gate determination is the other, and it is the one thing in this suite that must never be split: a supplier is approved for a use case or it is not, and an approval assembled from a closed security review, an open privacy review, and an unexamined subprocessor list is not a partial approval; it is an unapproved supplier with three documents in front of it.

**Acceptance bar.** Every evidence item is recorded with its type, edition, scope, period, auditor or tester, and expiry. The scope gap between the service purchased and the service covered is stated explicitly, including when there is none. Every finding carries severity, owner, and due date. Every condition carries an owner and a date. The review state is the reviewer's, with the date they gave it. Vendor claims are labeled as claims wherever they appear.

## Outputs

A complete run delivers the set:

- `review-coordination-record.md`: every evidence item requested, from whom, when, what arrived, what is outstanding, the chase history, and the date each outstanding item is due.
- `attestation-analysis.md`: report type and edition, the services and environments actually in scope, the period covered, the auditor, the system description boundaries, and every exception and qualification with its relevance to this use case.
- `scope-gap-assessment.md`: the service in the order form against the service in the evidence, by product, environment, region, and subsidiary, with each gap stated and what it leaves unevidenced.
- `questionnaire-review.md`: each answer, whether it is corroborated by a document or stands alone as an assertion, and the controls whose only evidence is the supplier's own statement.
- `privacy-position.md`: personal data categories, the processing role, the data protection terms required, the subprocessor list with locations and objection rights, the transfer mechanism, retention and deletion terms, and whether an impact assessment is triggered and by which criterion.
- `findings-register.md`: each finding with severity, the supplier's response, the compensating control, the named owner, and the due date.
- `approval-conditions.md`: every condition attached to a conditional approval, its owner, its date, and what happens if it is not met.
- `required-contract-terms.md`: the terms the review requires the agreement to carry, written so they enter the negotiation rather than the issue log.
- `vendor-claimed-register.md`: the claims the supplier makes that no document supports, recorded as claims with where each was made.
- `security-privacy-review-downstream-handoff.md`: the gate state, the open findings and conditions, and the terms the negotiation and contract stages inherit.

Depth standard: an artifact is complete when a reviewer could act on it and an auditor could trace it. "Report reviewed, no issues" is a summary; "the report covers the named service in the named regions for the stated period, the exceptions section records the items listed here, and the environment the company would use is outside the described boundary" is an analysis. A finding is complete when it has an owner and a date; a condition without both is not recorded as closed.

Where the engagement processes no personal data, `privacy-position.md` states that with the basis and the data types checked, rather than being omitted, because a later scope change is measured against it. Where the supplier's evidence portal, the questionnaire platform, or the review system cannot be reached, `security-privacy-review-diagnostic.md` names the source, what was attempted, and which evidence items and which gate decisions stay unavailable.

The failure mode here is not an invented control; it is an invented reviewer. Under deadline pressure the tempting move is to read the evidence, form a reasonable view, and record it as the review outcome, which produces a security approval that no security function gave and that four downstream stages will treat as one. The same substitution happens in smaller pieces: a certification restated in the supplier's shorthand so it appears to cover more than the scope statement says, a control marked satisfied on the strength of a questionnaire answer, a subprocessor list accepted as complete because it was published, and a condition recorded as accepted when nobody agreed to own it. A review that has not come back is outstanding with the date it was requested and the reviewer named; the state of an engagement is never advanced by inference, and this desk records what reviewers decided rather than what the evidence would support.

## procurement_packet fields to update

- `diligence.security.questionnaire_state`, `attestations`, `penetration_test`, `certifications_claimed_without_evidence`, `findings`, `review_state`, `conditions`, `reviewing_function`.
- `diligence.privacy.personal_data_processed`, `processing_role`, `dpa_state`, `subprocessors`, `transfer_mechanism`, `assessment_required`, `retention_and_deletion_terms`.
- `diligence.accessibility_conformance` and `diligence.continuity` where the tier obliges them.
- `diligence.diligence_gate_state`, set as a single determination rather than per workstream.
- `contract.open_positions` with the terms the review requires and the risk owner for each.
- `approvals` for any conditional approval, risk acceptance, or request to proceed ahead of a closed review.
- `engagement.security_reviewer`, `engagement.privacy_reviewer`.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Security or privacy**: continuing would treat a supplier as reviewed when evidence for the service being bought does not exist or has expired, would move personal or customer data to a processor whose terms and subprocessors are unestablished, would grant access before the review governing it has closed, or would carry an approval condition into the contract with no owner and no date. Where the review cannot complete inside the timeline, the timeline is the thing that moves.
- **Approval**: a risk acceptance, a finding waiver, a conditional approval, or a decision to proceed with an open review. These belong to the reviewing function and the risk owner the policy names, and this desk never grants one on their behalf.
- **Production or destructive**: the next act would connect an integration, provision access, upload data for a pilot, or tell the supplier their security review has passed. A pilot with real data is the engagement rather than a preview of it.
- **Source conflict**: the questionnaire, the attestation report, the supplier's public documentation, and the contract draft describe different subprocessors, different locations, different retention, or different controls. Record every reading with its locator and date, because that disagreement is frequently the most useful finding the review produces.
- **Release integrity**: a review state, a certification, or a subprocessor position would be reported into a customer security questionnaire, a regulator response, an audit, or a risk committee without the underlying document having been read. This is the step that converts a supplier's claim into the company's own representation to its customers.
- **Connector unreachable**: the supplier's evidence portal, the questionnaire platform, the review system, or the document repository exists and cannot be reached, so a control state would rest on inference. An unreturned questionnaire is a soft gap; an unreachable evidence system is this halt.

An outstanding questionnaire, a report the supplier has not yet released under its confidentiality process, an unscheduled reviewer, and an unanswered subprocessor question are soft gaps. Record each as outstanding with the date requested and the date due, name what it blocks, and continue with the workstreams that can proceed.

## Downstream handoffs

`supplier-integrity-screening-desk` runs alongside on separate evidence and converges before negotiation. `pricing-negotiation-desk` inherits the unremediated findings and the required contract terms, and converts them into positions while leverage still exists, which is the entire reason the review precedes signature. `contract-execution-routing-desk` inherits the required terms, the conditions with their owners and dates, and the gate state, and does not route for signature against an open gate. `vendor-onboarding-provisioning-desk` inherits the security configuration the review obliges, since a review that produced requirements nobody configured has protected nothing. `supplier-relationship-governance-desk` inherits the open conditions and the reassessment triggers for the ongoing monitoring cadence.

## Quality bar

A good review record is one that survives an incident. When a supplier is breached and somebody asks what the company knew before it signed, the useful answer is an evidence list with scopes, periods, and exceptions on it, a findings register with owners and dates, and a clear statement of which controls rested on the supplier's word. The scope gap is named even when it is uncomfortable, because the report covering a different product is the finding that matters most and the one that is easiest to miss. Conditions have owners, so the next assessment cycle can tell what was agreed from what became habit. And the review state belongs to the reviewer, with their name and the date beside it, because an approval nobody gave is the one control failure that makes every other control in the file irrelevant.
