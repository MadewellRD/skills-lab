---
name: data-protection-terms-desk
description: review and negotiate the data processing agreement by determining controller and processor roles against the processing that actually happens, describing categories data subjects purposes and duration, checking the transfer mechanism and its assessment, subprocessor authorization objection rights and flow-down, the breach notification trigger and window as quoted, deletion and return against what the product can perform, audit and assessment rights with cost allocation, and whether customer data may be used to train models. use for dpa review, processing annex drafting, standard contractual clauses and transfer terms, subprocessor list checks, breach notification windows, data deletion commitments, and ai training clauses.
---

# Data Protection Terms Desk

## Suite workflow mode

This desk is part of the Legal Contracts Command Desk suite and is one of the review lanes. Inside a workflow, complete the data protection assessment, update `legal_packet`, and continue; the lanes converge into one issues list at `redline-negotiation-desk`. `references/stage-contracts.md` states what each lane owns; `references/suite-workflow-contract.md` defines the packet and the rule that terms incorporated by a URL are read at the version in force with the date retrieved.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act binds the organization or leaves the building, confidential or personal information would be exposed, sources genuinely disagree on a load-bearing fact, a statement about a document would go out without the text behind it, or a required document is unreachable. Every other gap proceeds with the assumption labeled inline at the clause it affects.

Never invent a role determination, a transfer mechanism, a module selection, a subprocessor, a breach window, a deletion period, an audit right, a retention capability, or a training-data permission.

## Role

Own the data processing agreement and every data protection term wherever it sits: the role each party actually holds, the processing description, the transfer route and the mechanism that legitimizes it, how subprocessors are authorized and what flows down to them, what triggers breach notification and inside what window, what happens to the data at the end and whether the product can actually do it, what audit rights are granted and who pays for them, and whether the counterparty may use the data to train or improve models.

The recurring defect here is a DPA that describes an idealized processing arrangement rather than the one the product performs. Roles get assigned by whoever drafted the template, deletion windows get agreed against a retention capability nobody checked, and a subprocessor list incorporated by a URL is never opened.

## Use when

- A DPA, processing annex, data protection article, or transfer addendum needs review or drafting.
- Controller and processor roles need determining against what the product actually does with the data.
- Cross-border transfer terms, module selection, transfer assessments, or localization commitments are in question.
- The subprocessor authorization model, objection right, notice period, or flow-down obligations need assessment.
- Breach notification triggers and windows, deletion and return obligations, or audit and assessment rights need reading against operational reality.
- Terms about training, improving, or deriving from customer data need assessment, including aggregated and de-identified carve-outs.

## Do not use when

- The obligation is confidentiality rather than personal data processing: `nda-confidentiality-desk`. They are separate obligations and an NDA does not discharge a processing obligation.
- The question is technical and organizational security measures and whether the program evidences them: `security-exhibit-desk`, which owns the exhibit the DPA points at.
- The question is how liability for a data protection failure is capped or indemnified: `risk-allocation-desk`.
- The question is the lawful basis, the record of processing, an impact assessment, or a data subject rights process: the Privacy suite owns those; this desk owns the contractual terms.
- Deletion is being executed on termination: `renewal-termination-desk` activates the obligation, this desk sets it.

## Required evidence

- The DPA, processing annex, or data protection clauses at their version, with every annex actually attached.
- What personal data genuinely flows, in which direction, and for what: categories, special categories, data subjects, purposes, and duration, taken from the product and the deal rather than from the template.
- The processing the product actually performs, including telemetry, analytics, support access, and any derived data.
- Hosting locations, support locations, and transfer routes, including onward transfers to subprocessors.
- The subprocessor list the agreement incorporates, at its actual locator, with the version and date it displayed when retrieved.
- The retention and deletion capability the product actually has, including backup cycles and any technical constraint.
- The security exhibit or schedule the DPA points at.
- Privacy counsel guidance where one exists, attributed to the named lawyer.

## Workflow

**Outcome.** A data protection assessment stating the role determination with the reasoning that supports it, the processing description, the transfer mechanism and the state of any assessment it depends on, the subprocessor model with objection rights and flow-down, the breach trigger and window quoted, deletion and return checked against real capability, audit rights with cost allocation, and the training and improvement terms quoted including any de-identified or aggregated carve-out.

**Grounding.** Roles are determined from who decides purposes and means for each processing activity, not from the label the draft applies. Where a single agreement covers several processing activities, the role is determined per activity, because a supplier can be a processor for the customer content and a controller for its own account telemetry in the same product.

**Constraints.**

- Retrieve the incorporated subprocessor list at its locator and record the date and version it displayed. A list described from memory of what the vendor uses is not the list the agreement incorporates, and it changes under a stable URL.
- Quote the breach notification trigger and window exactly, including what starts the clock. "Becoming aware", "confirming", and "determining that a breach has occurred" are different triggers, and the gap between them is measured in the days a regulator counts.
- Check the deletion and return obligation against the product. A thirty-day deletion commitment against a ninety-day backup cycle is a breach from the effective date, and a backup carve-out is drafted or the commitment does not hold.
- Read the training and improvement terms alongside any aggregated, anonymized, de-identified, or derived-data clause. A no-training commitment sitting next to a permission to use aggregated data to improve services is two clauses that have to be reconciled, and the second one usually wins.
- Assess audit rights from the granting side for whether they can be serviced across the customer base, and from the receiving side for whether a third-party report in lieu of audit actually covers the service in scope.
- Match the transfer mechanism to the role pairing and the route, and record the state of any assessment the mechanism depends on. A mechanism named with no assessment behind it is named rather than in place.
- Silence is a finding on counterparty paper: no deletion obligation, no subprocessor notice, no breach window, no restriction on training, no flow-down requirement.

**Parallel surface.** Independent units fan out: subprocessors on the list, distinct processing activities within one agreement, transfer routes, and the clause groups covering breach, deletion, audit, and training all read from the same document without depending on each other. Two steps are aggregate and run once after the fan-out: the role determination for the agreement as a whole, which only resolves after every processing activity has been characterized, and the performability check, because whether the organization can honor the DPA depends on deletion, retention, transfer, and subprocessor commitments read together against one operational reality.

**Acceptance bar.** Every role is stated per processing activity with the decision-making that supports it. The processing description names categories, data subjects, purposes, and duration from source. The transfer mechanism names the instrument, the module or variant, and the annexes attached, with the assessment state recorded. The subprocessor list is cited at its locator with a retrieval date and displayed version. The breach window and trigger are quoted. Deletion and return carry the operational check that says whether the commitment is performable. Audit rights carry form, frequency, notice, and who pays. Training terms are quoted together with any derived-data carve-out.

## Outputs

A complete run delivers the set:

- `dpa-assessment.md`: role determination per processing activity, processing description, transfer mechanism and assessment state, subprocessor model, breach trigger and window quoted, deletion and return, audit rights, and training and derived-data terms, each at its clause or annex reference.
- `processing-description-annex.md`: categories, special categories, data subjects, purposes, processing operations, and duration, drawn from what the product actually does, with each line sourced.
- `subprocessor-and-transfer-review.md`: the incorporated list at its locator with retrieval date and displayed version, each subprocessor with its processing role and location, onward transfer routes, the mechanism per route, objection rights and notice periods, and the flow-down the text requires.
- `dpa-performability-check.md`: each commitment against what the organization or the counterparty can actually do, naming deletion windows against backup cycles, localization against hosting reality, and audit rights against operational capacity.
- `data-protection-issues-list.md`: issues ranked by severity with operative effect, regulatory consequence where a source establishes it, position sought, and fallback.
- `data-protection-downstream-handoff.md`: what `security-exhibit-desk` must cover, what `risk-allocation-desk` must price, and the obligations that will land in the register.

Depth standard: an entry reads "clause 9.2 requires notification without undue delay and in any event within twenty-four hours of becoming aware of a Personal Data Breach, with awareness defined at annex 2 as any indication of unauthorized access, which is earlier than the confirmation point the incident process currently uses" rather than "breach notification is twenty-four hours". A subprocessor entry names the entity, its role, its location, and the onward transfer mechanism.

Where the matter involves no personal data, that determination is delivered as the assessment artifact with the evidence that supports it, and the remaining artifacts are returned as not applicable with that reason attached. Where the DPA's annexes, the subprocessor list, or the security exhibit it points at cannot be retrieved, `data-protection-diagnostic.md` names each and states which determinations are unavailable.

A DPA is the document most likely to be summarized from what DPAs usually contain, because they share structure closely enough that a fluent description can be produced without opening the annexes, and the annexes are where the actual processing lives. Do not describe the subprocessor list; retrieve it and record its locator, its displayed version, and the date it was read. Do not paraphrase the breach clause; quote the trigger and the window. Do not assume the transfer mechanism from the parties' locations; name the instrument and the annexes actually attached. An annex that was not opened is recorded as unread, and a DPA whose annexes are missing establishes nothing about the processing, because the operative content of this document is almost entirely in its schedules.

## legal_packet fields to update

- `data_protection`: `role`, `personal_data_categories[]`, `data_subjects[]`, `processing_purposes[]`, `transfer_mechanism`, `transfer_assessment_state`, `subprocessors` with `list_locator`, `objection_right`, and `flow_down`, `security_measures_ref`, `breach_notification`, `deletion_and_return`, `audit_rights`, `ai_training_use`.
- `positions[]` state and deviation for data protection clauses; `issues[]` with clause references and turn raised.
- `obligations[]` for breach notification, subprocessor notice, deletion, audit response, and assistance obligations, each with trigger and window.
- `approvals[]` where a commitment departs from the approved position or cannot be performed as drafted.
- `regulatory_terms.ai_specific_terms` where training and output terms sit outside the DPA.
- `source_facts` with locator, displayed version, and read date for anything incorporated by reference, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `next_stage`.

## Halt conditions

- **Security or privacy**: the agreement would commit to a deletion window, a data location, a retention limit, or a processing restriction the product cannot honor, or would authorize a cross-border transfer with no mechanism named. A commitment the organization cannot perform is a breach from the effective date and a regulatory exposure that arrives on its own schedule. This class also covers an artifact that would carry live personal data, real data subject records, or a populated export as an example.
- **Approval**: a role determination, transfer position, subprocessor authorization model, audit right, or training permission outside the approved position, and any acceptance of a breach window the incident process cannot meet.
- **Source conflict**: the DPA, the main agreement, the privacy notice, and the incorporated subprocessor page disagree on roles, deletion, or transfers; or the draft's role label contradicts the processing as the product performs it.
- **Release integrity**: a data protection answer would go to a customer, an auditor, or a regulator citing terms nobody opened, including an annex, a subprocessor list, or an incorporated policy.
- **Production or destructive**: the next act is accepting the DPA, executing the transfer instrument, adding or removing a subprocessor, or performing a deletion.
- **Connector unreachable**: an annex, the subprocessor list at its locator, the security exhibit, or an incorporated policy exists and cannot be read, so the processing terms would be described from a document partly unread.

An unconfirmed retention figure, an unnamed internal owner for breach notification, or a data inventory the product team has not yet supplied are soft gaps. Assess on what is present, label the assumption at the clause, and record the question.

## Downstream handoffs

`security-exhibit-desk` inherits the `security_measures_ref` and the specific measures the DPA commits to, since the DPA points at that exhibit and inherits whatever it says. `risk-allocation-desk` inherits the data protection indemnity and whether it sits inside or outside the cap. `obligation-extraction-desk` inherits breach notification, subprocessor notice, deletion, and audit-response obligations with their triggers and windows. `regulatory-flowdown-desk` inherits transfer and sector obligations. `renewal-termination-desk` inherits the deletion and return obligation that activates on termination. The Privacy suite receives the processing description for the record of processing and any assessment the transfer mechanism requires.

## Quality bar

Good data protection review is recognizable by whether the operational owner agrees they can do it. Roles are determined from the processing rather than from the label, and where a supplier is a controller for part of the product that is said plainly, because it changes the whole instrument. The breach window is quoted with its trigger, so the incident team knows what starts the clock. The deletion commitment is checked against the backup cycle before it is agreed rather than after the first deletion request. The subprocessor list is a retrieved document with a date on it, not a description. And the training clause is read together with every derived-data and aggregation clause in the agreement, because that is where a no-training commitment is quietly given back.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
