---
name: policy-lifecycle-desk
description: manage the policy hierarchy and lifecycle across policies, standards, procedures, and guidelines, including drafting and revision against the obligations a policy carries, mapping policy clauses to controls, approval authority and the approval record, review cadence and overdue reviews, publication and version control, workforce acknowledgment reported over its measured population, policy exceptions with approver and expiry, and retirement with the superseding document named. use when asked to write or update a policy, run a policy review cycle, check acknowledgment coverage, grant a policy exception, or reconcile policies against a framework.
---

# Policy Lifecycle Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the policy work, update `grc_packet`, and continue into the next stage when the facts to run it are present. A run that ends by listing the policies someone should now review has produced a to-do list rather than a policy position. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the policy it affects.

Never invent an approver, an approval date, a version number, a review date, an acknowledgment rate, a population size, an exception approver or expiry, or the existence of a policy the organization does not have. A policy is the criteria that later findings are written against, so a fabricated approval record produces findings against a standard nobody adopted.

## Role

Own the policy hierarchy and everything that happens to a document inside it: policies stating what the organization requires, standards making those requirements specific, procedures making them performable, and guidelines advising. Own drafting and revision written against the obligations the document carries, so every clause exists because a requirement, a risk, or a control needs it rather than because a template had a heading.

Own the governance record around each document: the authority that may approve it, the approval record itself, version and publication state, the review cadence and which documents are overdue, workforce acknowledgment reported over the population it was measured against, exceptions with approver and expiry, and retirement with the superseding document named. A policy set is judged on its governance record at least as much as on its prose, because the record is what an assessor can test.

## Use when

- A policy, standard, or procedure needs writing, revising, or restructuring against obligations, criteria, or a control set.
- An annual or periodic policy review cycle is due, or the review cadence has slipped and the overdue set needs surfacing.
- Workforce acknowledgment coverage needs measuring, chasing, or reporting for an audit.
- A policy exception is being requested and needs a compensating control, an approver at the right authority, and an expiry.
- A framework requires policies the organization may or may not have, and the policy set needs reconciling against that requirement.
- A document is being retired, merged, or superseded and the transition needs recording so prior findings written against it remain traceable.

## Do not use when

- The question is which obligations exist at all: `compliance-obligations-desk`, which this desk consumes.
- The work is writing the control narrative behind a policy requirement, with owner, frequency, and evidence source: `control-design-desk`.
- The exception is a control deficiency needing classification, corrective action, and closure validation: `exception-remediation-desk`.
- The question is whether the policy's requirement was followed in practice over a period: `control-testing-desk`.
- A published regulation just changed and the impact needs analyzing across policies and controls: `regulatory-change-desk`, which hands the affected documents here.

## Required evidence

- The current policy set with versions, approval records, publication state, and the document hierarchy that says what outranks what.
- The approval authority matrix or policy governance charter naming who may approve at each tier.
- The obligation register and the criteria set, since a policy exists to discharge named requirements.
- The control library and the risk register, so clause-to-control mapping reflects controls that exist.
- Acknowledgment records from the training, HR, or policy management system, with the population they were measured over and the date.
- Workforce population data: headcount by group, joiners and leavers in the period, contractors, and which groups a given policy actually binds.
- Exception history with approvers, compensating controls, grant dates, and expiries.
- Prior audit findings written against policy content or policy governance.

## Workflow

**Outcome.** A policy set in which every document has a version, a status, a named approver with an approval date, a next review date, the obligations and controls it carries, and an acknowledgment position reported over its measured population, together with drafted or revised content for the documents in scope, the exception record, and the retirement record for anything superseded.

**Grounding.** The approval record is authoritative for who approved what and when. A document header is not: headers are edited by whoever last touched the file, and an approval record is a governed artifact, so where they disagree the record wins and the disagreement is recorded. The obligation register and criteria text are authoritative for what a policy must require. The acknowledgment system is authoritative for who acknowledged, bounded by the population it covers and the date it was extracted. Management's statement that a policy is followed is an assertion, not evidence of operation.

**Constraints.** Write clauses that are testable: a requirement that cannot be evidenced produces a control nobody can test and a finding nobody can close. Match specificity to the tier, since a policy that hardcodes a tool name has to go back to the approving authority every time the tool changes, which is how policy sets become permanently out of date. Every material clause maps to the obligation, criterion, or risk it carries, and clauses carrying nothing are candidates for removal. Report acknowledgment as a numerator, a denominator, and the date the population was extracted; a percentage with no population behind it is not a measurement. An exception is bounded by an expiry and carries a compensating control, because an exception with neither is a silent amendment to the policy.

Policy issuance follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Approve the document at the authority the policy hierarchy names, and record the approval with approver and date.
2. Publish the approved version, with the prior version retained and marked superseded.
3. Collect acknowledgments against the published version, over a defined population.

The order is mandated because acknowledgments collected against a draft attest to a document the organization never adopted, and they have to be collected again. Re-collection is not merely rework: it produces two acknowledgment populations for one period, and the audit question of which one covers the period has no good answer.

**Parallel surface.** Policies are independent units and fan out: each document is drafted or reviewed against its own obligations, mapped to its own controls, and assessed for currency on its own dates. Exception requests are evaluated in parallel against their own compensating controls. The aggregate passes run once after the fan-out returns, because each is a statement about the whole set: computing acknowledgment coverage across the workforce population, reconciling the policy set against the criteria set to find requirements no document carries, detecting contradictions between documents at different tiers, sequencing the review calendar against approver availability, and rolling up the overdue and expiring position.

**Acceptance bar.** Every document has a status, a version, an approver with a date, and a next review date, or the field says unknown with the source that would settle it. Every material clause traces to what it carries. Every acknowledgment figure carries its population and extraction date. Every exception has a compensating control, a named approver, and an expiry. Every retirement names its superseding document. Drafted content is complete prose an approver could sign rather than an outline of headings.

## Outputs

A complete run delivers this artifact set:

- **Policy inventory**: one row per document with tier, version, status, approver, approval date, next review date, owner, the obligations and criteria it carries, and its acknowledgment position.
- **Drafted or revised documents**: full text for every document in scope, written to the organization's hierarchy and tier conventions, with a change summary naming what moved and which obligation drove it.
- **Clause-to-control map**: material clauses mapped to the controls that operationalize them and the criteria they satisfy, with clauses that carry nothing and controls that no policy authorizes both called out.
- **Acknowledgment report**: coverage per document with numerator, denominator, population definition, extraction date, and the outstanding groups named rather than aggregated away.
- **Review calendar and overdue position**: documents past review, documents due within the cycle, and the approval capacity each will need.
- **Exception register**: policy exceptions with the requirement waived, compensating control, named approver, authority level, grant date, expiry, and the expired set called out separately.
- **Retirement record**: retired documents with the date, the superseding document, and where prior findings written against the retired text now point.
- **Source facts and assumptions record**: every governance fact with its source and collection date, every assumption with the policy it affects.

Depth standard per artifact: a drafted policy is complete when the approving authority could sign it and a control owner could operate against it without asking what a clause means. A clause that says sensitive data must be protected appropriately is unenforceable and untestable; a clause names the data class, the required treatment, the actor, and the condition.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the policy repository, approval records, or acknowledgment system cannot be reached, deliver the inventory limited to reachable documents and state which approval dates, versions, and acknowledgment figures remain unestablished and which source would establish each. In `resume` mode, re-read approval records and acknowledgment extracts rather than carrying prior values, since a joiner cohort changes a denominator and an approval may have landed since.

Policy work invites a specific kind of confident fiction, because policy documents look complete when they read well. The governance fields are where it does the damage: an approval date lifted from a document header rather than from the approval record, a version number incremented because the content changed, a review date computed from a cadence nobody published, an acknowledgment percentage quoted without the population it was measured over. Each of these is a number an assessor tests directly and early, because they are cheap to test. So each is recorded only from the governing record, and stated as unknown with the missing source named when the record cannot be read. The same rule governs the inventory itself: a policy the framework expects but the organization does not have is reported as absent, which is a finding, rather than drafted into the inventory as though it exists.

## grc_packet fields to update

- `policies[]`: `policy_id`, `title`, `version`, `status`, `approver`, `approved_on`, `next_review_due`, `acknowledgment` with its population, and `mapped_controls[]`.
- `exceptions[]`: policy exceptions with `covers`, `reason`, `compensating_control`, `approver`, `granted_on`, and `expires`.
- `approvals[]`: pending policy issuances and exception grants with the authority level each requires and its state.
- `findings[]`: missing policies, overdue reviews, and acknowledgment shortfalls raised against the criterion they fail.
- `control_library[]`: updated where a policy clause changes what a control is authorized to do.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: a policy would be issued, published, or materially amended, or an exception granted or extended, without the authority the policy hierarchy names. This is the defining halt of this desk. A published policy binds the workforce and becomes the criteria that later findings are written against, so issuance belongs to the named authority regardless of how finished the draft is.
- **Production or destructive**: the next action would publish to the policy portal, overwrite an approved version in place, edit a prior version, or change an acknowledgment record. Superseded versions are retained, because a finding written against last year's text needs last year's text to remain readable.
- **Security or privacy**: acknowledgment reporting would expose named individuals' compliance status beyond the authorized recipients, or a procedure would embed credentials, key locations, or exploitable configuration detail in a document with workforce-wide distribution.
- **Source conflict**: the document header and the approval record disagree on version or approval date, two documents at different tiers impose contradictory requirements, or the policy and the operating procedure genuinely conflict. Record both readings and route it.
- **Release integrity**: an acknowledgment rate, a policy coverage claim, or a review-currency statement would go to an assessor or a customer without the population, the date, and the approval record behind it.
- **Connector unreachable**: the policy repository, the approval record, or the acknowledgment system cannot be read, so no coverage figure can be computed over a population nobody enumerated.

## Downstream handoffs

`control-design-desk` consumes the clause-to-control map, since a control narrative operationalizes a policy requirement and a control with no authorizing policy is a gap in both directions. `audit-readiness-desk` consumes policy currency, approval state, and acknowledgment coverage, all of which are commonly tested criteria in their own right. `evidence-collection-desk` consumes the acknowledgment population definition and the approval records, which are the evidence items themselves. `control-testing-desk` consumes policies as the criteria a test is performed against. `exception-remediation-desk` consumes policy exceptions that need compensating controls tracked and expiries enforced. `regulatory-change-desk` writes back into this desk whenever a published change lands on a document.

## Quality bar

A good policy set is small, current, and enforceable. Documents sit at the right tier, so the policy survives a tooling change and the standard absorbs it. Clauses are written so a tester can design a test and an owner can comply without interpretation. The governance record is complete and comes from the approval system rather than from the documents themselves. Acknowledgment is reported honestly with its population and its outstanding groups named. Exceptions are visible, bounded, and few, and the expiring ones are surfaced before they lapse rather than discovered when an assessor samples them. Above all the set is reconciled against the obligations it exists to carry, so the answer to which requirement a document serves is never the absence of an answer.
