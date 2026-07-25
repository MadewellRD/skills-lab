---
name: audit-engagement-desk
description: coordinate an external audit or certification engagement across request list tracking with submitted accepted and rejected states, walkthrough preparation and the record of what was demonstrated, evidence-grounded responses to assessor questions, exception and deviation handling with management response drafted for signature, draft report review against the packet, and the management representation letter with every assertion traced to its basis. use for soc 2 fieldwork, iso stage 1 and stage 2 audits, pbc list management, auditor question logs, and draft report review.
---

# Audit Engagement Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the engagement artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the request or question it affects, and record it in `open_questions`. Never invent request item statuses, assessor questions or their rejection reasons, walkthrough content, sample selections, exception wording, report language, or a representation the organization has not made.

## Role

Own everything the organization says to the assessor and everything the assessor sends back. This desk tracks the request list item by item through submitted, accepted, and rejected with the assessor's stated reason for each rejection, prepares the people who will be walked through their own processes and records what was actually demonstrated, answers assessor questions from evidence rather than from the control narrative, handles exceptions and deviations with a management response drafted for signature, reviews the draft report against the packet, and prepares the management representation letter with every assertion traced to the basis that supports it.

The governing fact of this stage is that nothing said to an assessor is casual. A sentence in a walkthrough, an answer in a question log, and a line in the representation letter are all management assertions, and they are tested against everything else the organization has said. Correcting one afterward is a restatement rather than an edit, and it changes how the assessor reads the rest of the engagement, including the parts that were fine.

## Use when

- An external assessor or certification body is engaged, fieldwork has a calendar, and the request list needs running.
- A request item was rejected and needs re-fulfilling against the assessor's stated reason rather than resubmitting the same artifact.
- Walkthroughs are scheduled and the participants need preparing on what will be demonstrated and what the boundaries of the answer are.
- An assessor question has arrived and the answer needs grounding in a specific artifact before it goes on the record.
- An exception or deviation has been identified in the field and a management response is being drafted for the report.
- A draft report has arrived and needs reviewing against the packet for scope, period, system description accuracy, and exception wording.
- The management representation letter is due and each of its assertions needs tracing to its basis.

## Do not use when

- The audit is the organization's own internal audit function auditing itself. That is `internal-audit-desk`.
- The engagement has not started and the question is whether the organization is ready. That is `audit-readiness-desk`.
- Evidence needs collecting, populations extracting, or freshness assessing against the period. That is `evidence-collection-desk`, whose packages this desk submits rather than assembles.
- The control conclusion itself is being formed with a population and a sample. That is `control-testing-desk`.
- The report has been issued and the question is who may receive it, whether a bridge letter is needed, or how to answer a customer questionnaire from it. That is `attestation-reporting-desk`.
- A finding needs a corrective action plan, an exception grant, or aging. That is `exception-remediation-desk`.

## Required evidence

- Assessor and engagement details: the firm or certification body, the engagement type named by a source, the agreed scope and period, the fieldwork calendar, and the reporting deadline.
- The request list as the assessor issued it, item by item, with each item's due date and the assessor's own identifier for it.
- Evidence packages from the collection stage with their locators, periods covered, populations, and completeness basis.
- Control narratives and the system description as they will be presented, alongside the process as it actually runs.
- Walkthrough participants, the processes each will demonstrate, and the systems they will show live.
- The prior period report with its exceptions, since an assessor opens with what was open last time.
- Sample selections issued by the assessor, and the population each was drawn from.
- Management representation requirements for the engagement type, including the subsequent events period.
- The organization's own view of open deficiencies, so an exception is not discovered by the assessor first.

## Workflow

**Outcome.** A request tracker with a state and a date per item, walkthrough preparation notes and a record of what was demonstrated, an answered question log with each answer's evidence reference, exception handling with management responses drafted for signature, a draft report review against the packet, and a representation letter with every assertion traced to its basis.

**Grounding.** Evidence is the basis for every answer that goes to the assessor; the control narrative describes intent and is not evidence that a control operated. A rejected request item is re-fulfilled against the assessor's stated reason, quoted, because assessors reject for specific reasons such as a period that does not cover the window, a population with no completeness basis, an undated screenshot, or an artifact showing configuration rather than operation, and resubmitting the same file with a new cover note burns calendar the engagement does not have. Where the organization's answer and the assessor's premise differ, the difference is surfaced with evidence rather than absorbed to keep the conversation smooth.

**Constraints.** Every request item carries its assessor identifier, what was submitted, when, its current state, and the assessor's reason where rejected. Walkthrough preparation names the process, the participant, the artifact that will be shown, and the answer boundary, so a participant asked something outside their knowledge says so rather than improvising; the record afterward states what was demonstrated, what was said, and what was promised as follow-up. Question responses cite the artifact that supports them by locator and period, and where no evidence supports an answer the response says what is known and what is not rather than filling the gap. Exceptions are handled by preparing the management response for signature: the response states what happened, its extent, its cause where evidenced, what compensating control operated, and what will change, in language the organization can stand behind after the report is issued and quoted back. Draft report review checks scope wording, entity naming, period, system description accuracy, criteria referenced, exception wording and extent, and any statement about remediation that the evidence does not support. Everything with a signature line is prepared and routed rather than issued.

**Mandated order, authorization precedes anything that leaves the organization.** This order holds regardless of the assessor's deadline and is not scaffolding: these statements bind the organization to a party that will rely on them, and a correction afterward is a restatement that changes how the assessor reads every other answer.

1. Ground the statement in evidence and record the artifact reference behind each assertion.
2. Route it for internal review by the owner accountable for the subject matter.
3. Obtain authorization at the authority level the rubric requires for a statement that leaves the organization.
4. Send, and record what was sent, to whom, and when.

The order cannot be recovered by sending first and correcting later, because the assessor's working papers already carry the original.

**Parallel surface.** Individual request items, individual evidence submissions, individual question responses, and individual walkthrough preparations fan out and are parallel-safe; each rests on its own artifact and its own process owner. The request list completion position against the fieldwork calendar, the reconciliation of exceptions found by the assessor against the deficiencies the program already knew about, the draft report review as a whole, the consistency check across everything the organization has said in this engagement, and the representation letter are single passes after the fan-out returns, because each is a statement about the engagement rather than about an item.

**Acceptance bar.** Every request item has a state and a date, every answer on the record names the artifact behind it, every walkthrough has a record of what was demonstrated, and every assertion in the representation letter traces to a basis a reviewer could open. Nothing with a signature line has been sent without its authorization.

## Outputs

A complete run delivers this set:

- `request-tracker.md`: per item, the assessor's identifier and wording, owner, due date, what was submitted with its locator, state as open, submitted, accepted, or rejected, and the assessor's stated rejection reason quoted.
- `walkthrough-preparation.md`: per walkthrough, the process, participant, systems to be shown live, the artifacts that will be demonstrated, the expected line of questioning, and the boundary of what each participant can speak to.
- `walkthrough-record.md`: per walkthrough, date, attendees, what was demonstrated, what was stated, follow-up items promised, and anything the assessor flagged in the room.
- `assessor-question-log.md`: per question, the question as asked, the answer given, the artifact reference and period behind it, the date answered, and any answer deliberately deferred pending evidence.
- `exception-handling.md`: per exception or deviation, the assessor's characterization, the organization's evidence-based position, extent, compensating control, and the management response drafted for signature.
- `draft-report-review.md`: comments against the draft by section, covering scope, entity, period, system description accuracy, criteria references, exception wording and extent, and any statement the evidence does not support.
- `representation-letter-package.md`: the letter prepared for signature with each assertion traced to its basis, the subsequent events position, and the assertions that cannot be made with the reason.
- `audit-engagement-downstream-handoff.md`: what `attestation-reporting-desk` inherits, including the issued report's scope, period, exceptions, and distribution constraints.

Depth standard: an artifact is complete when the assessor could work from the submission without a clarifying email, and when a reviewer could confirm every recorded answer against its cited artifact. A request tracker that records only submitted and outstanding, without rejection reasons and resubmission history, hides the real state of fieldwork until the deadline.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the evidence repository, the request list system, or the assessor's portal cannot be reached, the run delivers `engagement-connector-diagnostic.md` naming each unreachable source, the request items whose state is therefore unknown, and the questions that cannot be answered from evidence. No answer is sent from recollection to keep the calendar moving.

Anti-fabrication guard: the pressure in fieldwork is conversational, and that is what makes it dangerous. An assessor asks a question in a meeting, the room does not want to look unprepared, and someone answers from the narrative because the narrative describes what should happen. That answer is now a management assertion, and the assessor will select a sample against it. So every answer that goes on the record carries the artifact and period behind it, "we will confirm and come back with the evidence" is a complete and professional answer that is used freely, and a walkthrough participant is prepared to say what they do not know rather than describe the process as designed. Exception wording is drafted from the evidence of what happened rather than from what would read best, extent is quantified from the population rather than characterized as isolated, and no representation is included in the letter unless someone can point at what supports it. The organization is better served by an exception it reported accurately than by a clean paragraph the next sample contradicts.

## grc_packet fields to update

- `audit_engagement.assessor`, `engagement_type`, and `report_state` moved through `fieldwork`, `draft`, `management_response`, and `issued`
- `audit_engagement.request_list` with items moved between `open`, `submitted`, `accepted`, and `rejected`, each rejection carrying the assessor's stated reason
- `audit_engagement.walkthroughs` with what was demonstrated and by whom, and `open_questions` with the answer state per question
- `audit_engagement.exceptions_in_report` with the assessor's characterization and the management response prepared for signature
- `findings[]` for deficiencies the assessor identified, with `origin` set to `external_audit`, criteria reference, and owner
- `evidence[]` updated where an item was rejected, with `state` set to `rejected_by_auditor` and the reason recorded rather than the item silently resubmitted
- `approvals[]` for every statement leaving the organization: question responses on the record, the management response, and the representation letter, each with the authority level required
- `attestations[]` seeded once the report is issued, with scope statement, validity, and distribution constraint
- `source_facts[]` with `collected` dates, `assumptions[]`, `open_questions[]`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: an answer to the assessor, a walkthrough statement, an exception response, or a management representation would go on the record without evidence behind it. This is the most common hard halt in the engagement and the one under the most schedule pressure, because the fieldwork date is real and the evidence is always late.
- **Missing approval**: the management response, the representation letter, and any statement that binds the organization need the named signatory at the authority level the rubric requires. A deadline does not create authority, and an unsigned draft sent to keep momentum is a signed statement in the assessor's file.
- **Security or privacy**: fulfilling a request as written would place personal data, credentials, customer records, or regulated content into a submission or a shared portal, or would send it beyond the authorized recipient set or across a residency boundary. Over-collection is the usual failure, and the assessor generally needs a population and a sample rather than the underlying records.
- **Source conflict**: the assessor's characterization of a control or an exception and the organization's evidence genuinely disagree, or the system description and the process as demonstrated diverge. Record both readings and route the conflict rather than accepting the assessor's premise to move on.
- **Production or destructive**: the next action would submit an item on the record, send a response to the assessor, or write engagement state into the system of record. Prepare it and stop at the gate.
- **Connector unreachable**: the evidence repository or request list system exists and cannot be read, so a submission state or an answer would be reported from memory.

An unscheduled walkthrough, an unnamed process participant, or an assessor deadline nobody has confirmed is a soft gap: name it, label the assumption inline against that item, and continue with the preparation drafted.

## Downstream handoffs

`attestation-reporting-desk` is next and needs the issued report's exact scope statement, period, exception list, validity, and distribution constraint, since every customer answer afterward is bounded by those four facts. `exception-remediation-desk` receives assessor-identified deficiencies as classified findings with owners and closure evidence. `evidence-collection-desk` receives rejection reasons so the next period's collection produces artifacts that pass on first submission, which is the single largest saving available in a repeat engagement. `control-design-desk` receives places where the narrative and the demonstrated process diverged. `committee-reporting-desk` receives the engagement state, exceptions expected in the report, and any representation the organization could not make.

## Quality bar

Good engagement work is judged by how little has to be corrected. The request tracker shows real state, including rejections and their reasons, so the fieldwork position is never a surprise on the last day. Answers cite artifacts, so the assessor's sample confirms what was said instead of contradicting it. Walkthrough participants demonstrate what they actually do and say so where a step differs from the narrative, because the divergence found by the organization is a finding it controls and the same divergence found in the room is one it does not. Exceptions are reported with quantified extent and a response the organization will still stand behind a year later, when a customer reads it. And the representation letter contains only assertions someone can evidence, which occasionally means it is shorter than the template, and that is the correct outcome.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
