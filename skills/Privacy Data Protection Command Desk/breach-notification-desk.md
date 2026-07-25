---
name: breach-notification-desk
description: prepare supervisory authority filings including phased filings on incomplete facts, draft individual notification in plain language with the practical steps a person can take, prepare substitute notice where direct contact is impossible, issue processor to controller notice, and build the multi-jurisdiction filing matrix where thresholds deadlines and content requirements differ. use for 72 hour regulator notification, attorney general and consumer reporting agency notice, breach letters and email notification, media and website substitute notice, credit monitoring offers, and filing records with authority reference numbers.
---

# Breach Notification Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the notification artifact set, update `privacy_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the notification it affects, and record it in `open_questions`. Never invent an authority reference, a filing date, a submission channel, an affected count, or a remediation measure the organization has not taken.

Filing and sending are irreversible external acts and sit behind an approval gate in every mode. The deadline does not pause while approval is sought, so the item is prepared to submission-ready state, the approval is escalated immediately, and the running clock is stated on the halt.

## Role

This desk owns everything the organization says to the outside world about a breach, and the record of having said it. It prepares the authority filing with the content each regime requires, including the phased filing that goes in on incomplete facts rather than waiting for certainty and arriving late. It prepares the notification to affected individuals in language a person under stress can act on, which is a different writing problem from the regulator filing and is routinely solved worse. It prepares substitute notice where direct contact is impossible, with the basis that makes substitute notice available. Where the organization is a processor, it prepares the notice to the controller, which runs on its own clock and is often the tightest deadline in the incident.

Above all it owns the multi-jurisdiction matrix. A single incident routinely triggers several regimes with different thresholds, different deadlines, different content requirements, different regulator recipients, and different rules about whether individuals must be told at all. Those filings are read against each other. Consistency across them is not a presentational concern; a number that differs between two filings becomes the first question in the investigation.

## Use when

- An assessment has determined that an incident is notifiable under one or more regimes, or that it is arguably notifiable and the filing should be prepared while the determination is finalized.
- A deadline is approaching and the facts are incomplete, so a phased filing is the correct action rather than a delayed complete one.
- Affected individuals have to be told, and the letter or email has to say what happened and what they can do about it.
- Direct contact is impossible for some or all of the affected population and substitute notice has to be built with its basis.
- The organization is a processor and owes its controllers notice under contract, regulation, or both.
- A supplementary or corrective filing is needed because facts changed after an initial submission.
- The filing record itself has to be assembled for the register, for counsel, or for an authority asking what was filed and when.

## Do not use when

- The determination of whether the incident is a breach, how bad it is, and who is affected has not been made. That is `breach-assessment-desk`, whose output every field in a filing depends on.
- The work is technical containment or forensic investigation. That belongs to the security incident process, whose findings this desk describes but does not produce.
- The communication in question is a customer service response, a press statement, or an investor disclosure. Those are coordinated with, and consistent with, the filings prepared here, but they are not owned here.
- The obligation is a contractual notice to a partner with no personal data involved. That is a contract matter rather than a breach notification.
- An individual has responded to a notification by exercising a right. That is `rights-request-intake-desk`, and notification-driven request volume is worth anticipating.

## Required evidence

- The assessment output: the awareness timestamp, the personal data breach determination, the categories, the population figures with their bases, the risk conclusion, the mitigating factors, and the notifiability determination per regime.
- The deadline each regime computes from awareness, with the period and the provision that sets it.
- The authority's filing route and format as currently published: the online form and its fields, the email or portal address, the language required, and whether an initial submission can be supplemented.
- The lead authority analysis where a one-stop-shop mechanism applies, and the concerned authorities that also receive the filing.
- Contact data and reachable channels for affected individuals, with the share of the population for whom no working channel exists, since that share drives substitute notice.
- Contractual notification obligations to controllers and partners with the clock each sets and the recipient each names.
- Containment and remediation state as it stands now, described as measures taken or proposed rather than as intentions.
- The counsel position, the approval chain with authority levels, and any prior filings or public statements about the same incident.
- Where remediation services such as monitoring are offered, the enrollment route, the deadline, and who pays.

## Workflow

**Outcome.** Authority notification content per regime covering the nature of the breach, the categories and approximate numbers of individuals and records, the contact point, the likely consequences, and the measures taken or proposed; phased filings where facts are incomplete with what is known and what remains under investigation both stated; individual notification in clear plain language with the practical steps a person can take; substitute notice with the basis that makes it available; processor-to-controller notice where applicable; the multi-jurisdiction filing matrix; and the record of what was filed with whom and when.

**Grounding.** Every figure in a filing comes from the assessment with its basis attached, and where the assessment gave a range the filing gives the range rather than a point estimate. Filing routes and content requirements are read from the authority's current published form rather than from a previous incident's submission, because forms and required fields change between incidents. Measures are described as taken where a source confirms they were taken and as proposed otherwise, since a filing that lists a control as implemented is a statement the investigation will check.

**Constraints.** A filing on incomplete facts is the provided-for path and a late filing is a separate violation, so the deadline governs and the phased submission states plainly what is known, what is not, and when the supplement will follow. Individual notification is written for the person, not for the lawyer: it says what happened, what data of theirs was involved, when, what the organization is doing, and specifically what they can do, with the steps ordered by what protects them most. It avoids constructions that minimize without informing, and a notification whose first paragraph is about how seriously the organization takes privacy has spent its most-read sentence on the organization. Where the regime requires the same content elements in the individual notice, those elements are present as elements rather than assumed to be covered by the narrative. Substitute notice is available only on its stated basis, which is normally a cost threshold, a population threshold, or the absence of contact information, and the basis is recorded with the evidence for it; the method then has to actually reach people, which a buried website page does not. Notification does not go to a channel the breach compromised, so an email notice sent to addresses in the exposed mailbox system is recorded as unusable. Consistency across filings is checked as a property of the set: the same population figure, the same categories, the same awareness time, and the same description of what happened appear in every filing, and where a regime requires a different granularity the difference is deliberate and explained rather than incidental. Personal data of affected individuals is not reproduced in working artifacts; notification lists are referenced by locator and handled in a controlled location.

**The mandated notification sequence.** These steps continue the sequence begun at assessment and are ordered because a late notification is a separate violation and because an individual notice that arrives before the exposure is closed can direct attackers to a weakness that is still open:

5. Notify the authority within the deadline, filing in phases where facts are incomplete rather than filing late.
6. Notify affected individuals where the risk to them is high, in plain language with the steps they can take, and after containment where sending earlier would widen the exposure.
7. Complete the register entry with what was filed, to whom, when, and the reference received.

Where the organization is a processor, the notice to the controller runs in parallel on its own clock from the same awareness timestamp and does not wait for the organization's own regulatory analysis to conclude.

**Parallel surface.** Jurisdictions, authorities, and individual notification cohorts with different content or channel requirements are independent and fan out safely, as do the per-controller notices where the organization is a processor. Two steps are aggregate and run once after the fan-out returns: the consistency pass across every filing and notice, since the whole point is that they agree, and the filing matrix itself, which is a statement about the incident's total obligation set and cannot be assembled from parts that each looked at one regime.

**Acceptance bar.** Every notifiable regime has a prepared filing carrying its required content elements, addressed to the right authority through its current route, with its deadline and the arithmetic from awareness. Phased filings say what is unknown. The individual notice is readable by its audience and names concrete actions. Substitute notice has a basis with evidence. Every figure traces to the assessment. Nothing in the set contradicts anything else in it.

## Outputs

A complete run delivers this set:

- `authority-filing-pack.md`: per regime the submission-ready content mapped to the authority's current fields, the recipient and route, the deadline with its arithmetic from awareness, the phased scope where facts are incomplete, and the supplement committed to with its date.
- `individual-notification-draft.md`: the notice in plain language with what happened, the data involved, the date, what the organization is doing, the ordered steps the person can take, the contact route, and any remediation offer with its enrollment deadline, plus the reading level and the translations required.
- `substitute-notice-plan.md`: the basis with the evidence for it, the population it covers, the methods with their reach, the placement and duration, and the direct notice that still applies to the reachable share.
- `processor-to-controller-notice.md`: the notice per controller with the contractual clock it answers, the awareness time, what is known, and the assistance the organization is obliged to provide.
- `multi-jurisdiction-filing-matrix.md`: one row per regime with the authority, the threshold, the determination, the deadline, the content requirements, whether individual notice is required, the additional recipients such as attorneys general or consumer reporting agencies, and the filing state.
- `filing-record.md`: what was submitted, to whom, when, by whom, through which channel, the reference received, and the supplements still owed, assembled as the record the register and any later inquiry will read.
- `breach-notification-downstream-handoff.md`: what `privacy-program-metrics-desk` inherits, including awareness-to-notification intervals, and the request volume the notification is likely to generate for the rights desks.

Depth standard: an artifact is complete when the accountable owner could authorize submission without editing it and a recipient could act on it without calling to ask what it means. A filing with a placeholder for a number the assessment already produced, or an individual notice with no concrete action in it, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the authority's current form, the contact data for individuals, or the assessment output cannot be reached, the run delivers `notification-connector-diagnostic.md` naming each unreachable source, the filings it blocks, and every deadline still running with who has been told. A filing is never assembled against a remembered version of a form.

Anti-fabrication guard: filing forms have required fields, and a required field is an invitation to supply a plausible value so the form can be submitted. That is the specific hazard here. A field with no source behind it is left as unknown with the supplement committed, because a regulator accepts "under investigation, supplement to follow" and does not accept a number that later moves. The same discipline applies to remediation: measures are listed as taken only where something confirms they were taken, since a filing that claims a control the investigation finds absent converts an incident into a credibility problem. And because these documents are read side by side, the set is checked for agreement before any of it goes out: one incident, one awareness time, one population figure with one basis, described the same way to every authority and to the people affected. A discrepancy between two filings is not a drafting inconsistency; it is the first thing an investigator will ask about.

## privacy_packet fields to update

- `notifications[]` per audience with `notification_id`, `covers`, `audience`, `authority`, `phased`, `content_summary`, `submitted_on`, `reference`, and `approved_by`
- `notifications[].individual_notification` with `required`, `method`, `sent_on`, and `substitute_notice_basis`
- `breaches[].notifiability[]` updated with filing state per regime, keeping the determination and its threshold intact
- `breaches[].register_entry` completed with what was filed, to whom, and when
- `active_clocks[]` maintained for every filing deadline, every committed supplement, and any individual notification window, each with its start event
- `approvals[]` for each filing and each individual notification with the named approver and authority level, held as `pending` until granted rather than assumed
- `source_facts` with the authority route and form read dates, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a regulatory filing and a notification to affected individuals are irreversible external statements that set the terms of the investigation that follows, and both are authorized by the accountable owner with counsel. The deadline does not pause, so the filing is prepared, the approval is escalated immediately, and the running clock is stated on the halt.
- **Production or destructive**: submitting, sending, or publishing is the act itself and cannot be withdrawn once made; a correction afterward is a second public statement rather than an edit.
- **Release integrity**: a filing or a notice would carry a figure, a category, a cause, or a remediation claim that the assessment does not support, or two filings in the same set would state different facts.
- **Source conflict**: the assessment, the security account, and a prior public statement genuinely disagree on a fact the filing has to assert. Preserve every reading and route it, because a filing that resolves the conflict silently commits the organization to one version on the record.
- **Security or privacy**: the proposed notification channel is one the breach compromised, the notification list would be handled outside a controlled location, or sending now would reveal an exposure that is still open.
- **Connector unreachable**: the authority's current form or route, or the contact data for the affected population, cannot be reached, so submission would be attempted blind. The deadline is stated and escalated rather than allowed to pass quietly.

An unconfirmed remediation completion date, an unresolved translation, and an unfinalized monitoring vendor are soft gaps. Prepare the filing with the item labeled and the supplement committed, and continue.

## Downstream handoffs

`privacy-program-metrics-desk` is next and needs the awareness-to-filing interval per regime, deadline attainment, and the register completeness figure. `rights-request-intake-desk` should expect the request volume a notification generates, since a well-written notice tells people they have rights and a meaningful share will exercise them. `processor-vendor-agreement-desk` receives the contractual notification performance observed during the incident. `retention-deletion-desk` receives the retention position for the incident record itself and for the notification list, which is personal data created by the response. The security incident process receives the remediation commitments made in the filing, which are now external commitments with dates.

## Quality bar

Good notification work is judged by two readers who never meet. The regulator reads for completeness against the required content and for consistency with every other filing, and finds the awareness time, the population with its basis, and an honest statement of what is still unknown. The affected individual reads for one thing only, which is what they should do now, and finds it in the first screen rather than in the sixth paragraph. A notice that opens by asserting how much the organization values privacy has failed the second reader, and a filing that waited for certainty has failed the first. The matrix is where competence shows most plainly: several regimes, several deadlines, several thresholds, one set of facts, and no contradictions between them.
