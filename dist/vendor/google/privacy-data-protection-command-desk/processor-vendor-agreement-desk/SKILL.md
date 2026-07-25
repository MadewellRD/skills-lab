---
name: processor-vendor-agreement-desk
description: determine the controller processor or service provider role per vendor relationship, check data protection agreement coverage clause by clause, manage sub-processor authorization notice and objection windows, test deletion and return commitments against what the vendor can technically do, and name vendors holding personal data with no executed agreement. use for dpa review and negotiation, article 28 clause coverage, service provider and contractor terms, joint controller arrangements, business associate agreements, sub-processor registers, vendor diligence and questionnaires, audit rights, and onboarding or renewal gates.
---

# Processor Vendor Agreement Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the vendor agreement artifact set, update `privacy_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the vendor it affects, and record it in `open_questions`. Never invent an executed agreement, a signature date, a clause, a sub-processor, an attestation scope, or a deletion commitment.

## Role

This desk owns the relationship between the organization and every party that touches personal data on its behalf or alongside it. It starts with role, because every obligation downstream hangs off it and the label in the contract is the least reliable evidence available: an analytics provider that trains its own models on the data is not a processor no matter what the order form says, a payment provider running its own fraud and anti-money-laundering duties is an independent controller for that purpose, an enrichment vendor selling from its own database is a controller of it, and a processor that starts deciding purposes has become a controller of that processing and carries the consequences.

From role it owns clause-level coverage of the data protection terms, the sub-processor register with the notification mechanism and the objection window that actually exists rather than the one the policy describes, the diligence evidence and what its scope covers, the audit right as written rather than as hoped, joint controller arrangements including the part that has to be made available to individuals, and the deletion or return commitment tested against what the vendor's platform can technically do. Its most valuable output is the list of vendors holding personal data with nothing executed behind them, named one by one.

## Use when

- A vendor, sub-processor, contractor, or partner is being onboarded, renewed, expanded to a new data category, or migrated to a different entity.
- Data protection terms are being drafted, reviewed, negotiated, or repapered, including where the vendor offers only its own standard terms.
- A sub-processor is added, changed, or objected to, or the notification mechanism has to be established and subscribed to.
- Termination or offboarding is in view and the deletion or return commitment has to be turned into something the vendor can actually execute.
- A questionnaire, an attestation, or a trust page is being used as diligence evidence and its scope has to be established.
- The relationship is being tested against a role determination that a contract label or an org chart currently supplies.
- A vendor inventory reconciliation shows systems receiving personal data that procurement never processed.

## Do not use when

- The question is which jurisdiction the vendor sits in and what instrument legitimizes the export. That is `cross-border-transfer-desk`, which runs against the same vendor list for the transfer clause set.
- The vendor list itself does not exist and the work is finding out which systems receive personal data. That is `data-inventory-mapping-desk`.
- The subject is a tracker, pixel, or SDK on a public surface and the question is what fires and who receives it. That is `cookie-tracking-governance-desk`, which feeds identified vendors into this desk.
- The vendor has to execute a deletion or a rights request on the organization's instruction and the work is the instruction and its confirmation. That is `retention-deletion-desk` or `rights-request-fulfillment-desk`.
- A vendor has suffered an incident. That is `breach-assessment-desk`, which uses this desk's notification terms as the clock the vendor was contractually held to.

## Required evidence

- The vendor inventory with what each vendor processes, for which activity, and on whose instruction, reconciled against systems and flows rather than against the procurement register alone.
- Executed agreements as signed: the master agreement, the data protection terms or exhibit, the security schedule, and the annexes, with the contracting entity, the signature dates, and the version incorporated.
- The vendor's current standard terms where the executed agreement incorporates them by reference, captured at the version in force with the date it was read, since a referenced online document changes without a signature.
- Sub-processor lists per vendor with locations and functions, the notification mechanism and whether anyone is subscribed to it, and the objection window with the remedy it leads to.
- Diligence evidence with its scope: attestation reports with the period covered, the systems in scope, and any exceptions; certification with its statement of applicability; penetration test summaries; and questionnaire responses with who signed them.
- Incident notification terms with the clock they set and the trigger that starts it.
- Deletion and return commitments including format, timing, the certificate offered, and the retained copies the terms carve out.
- Technical reality behind those commitments: what the platform can delete, backup and log retention windows, derived and aggregated data retained, support ticket and attachment stores, and sandbox or test copies refreshed from production.
- Procurement stage, renewal dates, and whether personal data has already been sent.

## Workflow

**Outcome.** A role determination per relationship with the evidence behind it; clause-by-clause coverage of the data protection terms with each gap named as a clause rather than as a topic; the sub-processor register with the notification mechanism, the objection window, and the remedy; the diligence position with what each attestation actually covers; the audit right as written; joint controller arrangements with the essence available to individuals; the deletion or return commitment tested against platform capability; and the vendors holding personal data with no executed agreement, named.

**Grounding.** Role is tested against who decides purposes and means, using the vendor's own product behavior and its terms of use as evidence alongside the contract label. Coverage is read from the executed version rather than from the template the organization sends out, because the executed version is the one that was negotiated and the deletions are where the interesting parts went. Where terms are incorporated by reference to a page the vendor controls, the page is captured with a date and treated as a claim about today, not as a fixed term. Trust pages, questionnaire answers, and vendor privacy statements are evidence of what someone said, and they never establish what a system does.

**Constraints.** Clause coverage is checked against the mandatory set the applicable regime specifies, clause by clause: processing only on documented instructions with the obligation to flag an infringing instruction, confidentiality binding on personnel, security measures at the level the regime requires, sub-processor authorization with notice and objection, assistance with rights requests, assistance with breach notification and with assessments, audit and information rights, and deletion or return at the end of provision. A gap is named as the missing clause and the exposure it creates, never as a score. Where a regime mandates specific contractual language for a service provider, contractor, or business associate, the presence of that language is checked as language rather than as intent, since these regimes make the words themselves the obligation. Sub-processor authorization is specific or general, and a general authorization is only meaningful where the notification actually reaches someone who can act inside the objection window: a list on a page nobody subscribed to is recorded as no notice. The objection remedy is stated honestly, because in most standard terms the only remedy is termination and calling it an objection right overstates it. Deletion commitments are tested against capability: backup rotation that outlives the deletion window, derived or aggregated data the vendor keeps, logs, ticket attachments, and sandbox copies are recorded as exceptions with what permits each, and a commitment the platform cannot execute is a gap rather than a coverage entry. Attestation scope is quoted, because a report covering a different product line, a different region, or a period that ended before the current architecture is diligence for something else.

**Ordered sequence for onboarding.** This order is mandated because sending personal data to an uncontracted processor is the violation itself and a later signature does not reach back over what already went:

1. Determine the role and the data categories, since both decide which terms are required.
2. Complete diligence proportionate to the data and the role, and record what the evidence covers.
3. Execute the data protection terms and any transfer instrument the route requires, dated.
4. Configure the integration and send personal data, and only then.
5. Subscribe to the sub-processor notification mechanism at the same time, because the objection window starts whether or not anyone is watching it.

**Parallel surface.** Vendors, agreements, clause checks, sub-processor lists, and diligence reviews are independent and fan out safely, as do the per-vendor capability tests on deletion. Three steps are aggregate and run once after the fan-out returns: the reconciliation between systems receiving personal data and vendors with executed terms, which is where the uncontracted list comes from and which cannot be computed per vendor; the sub-processor register across vendors, since the same sub-processor sitting behind four vendors is one concentration and four rows; and the renewal and review calendar, which is a statement about the portfolio.

**Acceptance bar.** Every relationship has a role with the evidence that established it, and no role rests on the contract label alone. Every executed agreement has clause-level coverage with gaps named as clauses. Every vendor with a general sub-processor authorization has a named notification mechanism and a stated objection window, or is recorded as having no effective notice. Every deletion commitment names what the vendor can technically do and what stays. Every vendor receiving personal data with no executed agreement appears by name with the data it holds.

## Outputs

A complete run delivers this set:

- `vendor-role-determinations.md`: per relationship the role, who decides purposes and means, the evidence including the vendor's own product behavior, the contract label where it differs, and the obligations the determination triggers.
- `dpa-coverage-matrix.md`: per vendor the mandatory clause set with covered, partial, or absent per clause, the executed version and date it was read from, the negotiated deviations, and the exposure each gap creates.
- `sub-processor-register.md`: per vendor the sub-processors with locations and functions, the notification mechanism and subscription state, the objection window and its remedy, the date the list was read, and the sub-processors appearing behind more than one vendor.
- `vendor-diligence-record.md`: per vendor the evidence held, the scope and period each attestation covers, the exceptions noted in it, what the evidence does not reach, and the diligence still outstanding relative to the data category.
- `deletion-and-return-assessment.md`: per vendor the contractual commitment, the platform capability behind it, the retained copies with what permits each, the certificate available, and the offboarding steps that will actually be executable at termination.
- `uncontracted-vendor-list.md`: vendors receiving personal data with no executed agreement, each named with the data categories, the activity, how long the flow has been running where a date can be established, and the escalation raised.
- `processor-vendor-downstream-handoff.md`: what `rights-request-intake-desk` and the retention and breach desks inherit, including which vendors are contractually obliged to assist and within what time.

Depth standard: an artifact is complete when a contract owner could negotiate from it and an auditor could trace each coverage claim to an executed clause. A coverage matrix carrying a rating rather than a clause disposition, or a deletion entry that repeats the contractual promise without the capability behind it, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the contract repository, the executed terms, or the vendor's current standard terms cannot be read, the run delivers `vendor-agreement-connector-diagnostic.md` naming each unreachable source and the vendors whose coverage stays undetermined. Coverage is never inferred from the template the organization normally sends.

Anti-fabrication guard: the failure here is the coverage matrix built from a template rather than from a signature. Standard terms are so consistent across the market that a plausible clause list can be written for any vendor from memory, and once it is in the matrix the organization believes it has an audit right it never negotiated. Every clause disposition is quoted from the executed document, with the version and the date it was read, and a vendor whose executed terms were not opened is `unknown` rather than assumed to carry the market standard. A trust center page, a security portal, and a completed questionnaire are recorded as vendor statements with the date collected, never promoted into contract terms. A sub-processor list is recorded as read on a date, because those lists change silently and yesterday's list is evidence about yesterday. And where the executed agreement is with one legal entity while the data goes to an affiliate, that is recorded as a gap rather than smoothed into a group-level assumption.

## privacy_packet fields to update

- `processors[]` in full: `vendor`, `role`, `activities`, `data_categories`, `agreement` with `executed`, `executed_on`, `clause_coverage`, and `gaps`, `sub_processors` with `list`, `notification_mechanism`, and `objection_right`, `audit_rights`, `deletion_or_return`, `transfer_ref`, `review_state`, `next_review_due`
- `applicability[].role` and `role_basis` updated where the determination here contradicts an earlier role assumption, with both readings preserved
- `processing_activities[].recipients` reconciled against the vendors actually receiving data
- `data_flows[].authorization` set to the clause or contract that permits each flow, or recorded as absent
- `approvals[]` for onboarding decisions, negotiated deviations, and accepted clause gaps, each with the named approver and authority level
- `source_facts` with collection dates separating executed documents from vendor statements, `assumptions`, `open_questions`, `active_clocks` for objection windows and renewal dates
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: onboarding a vendor, accepting a clause gap, waiving a diligence requirement, or agreeing a joint controller arrangement commits the organization and needs the data owner with legal review wherever the regime or the data category requires it.
- **Production or destructive**: the next action would execute an agreement, enable an integration that starts a data flow, instruct a vendor to delete, or terminate a service that holds the only copy of something.
- **Security or privacy**: a vendor is holding personal data now with no executed data protection terms, or a sub-processor has been added that processes data the agreement does not cover. The exposure is live and grows with every day of processing, and an agreement signed later does not cover what already went.
- **Source conflict**: the executed agreement, the vendor's current published terms, and the observed integration genuinely disagree about role, scope, sub-processors, or retention. Preserve every reading, because resolving toward the reading that leaves the relationship compliant is how an uncontracted flow stays invisible.
- **Release integrity**: a customer response, a questionnaire answer, or a register would state that vendor coverage is complete on the strength of templates rather than executed terms.
- **Connector unreachable**: the contract repository, the executed agreement, or the vendor's terms exists and cannot be read, so coverage would be described rather than established.

An unconfirmed renewal date, a missing attestation for a low-risk vendor, and an unpublished audit procedure are soft gaps. Label the assumption against the vendor and continue.

## Downstream handoffs

`rights-request-intake-desk` is next and needs the vendors obliged to assist with rights requests, the mechanism each assistance clause specifies, and the response time it commits to. `rights-request-fulfillment-desk` needs the processor list filtered to those holding in-scope data and the instruction route for each. `retention-deletion-desk` needs the deletion capability assessment, since a schedule that assumes a vendor can hard delete on request will not execute. `breach-assessment-desk` needs the incident notification terms and the clock each sets. `cross-border-transfer-desk` receives the sub-processor locations found here as transfers it may not have. `dpia-desk` needs the residual risk carried by clause gaps on high-risk processing.

## Quality bar

Good vendor agreement work is recognizable by its uncontracted list and by what it says about deletion. If every vendor in the register has coverage, the register was built from vendors that procurement knew about rather than from systems that receive data, and the marketing tool someone expensed is missing from it. The role determinations cite the vendor's own product behavior, because that is what a regulator will look at when a processor turns out to have been training on the data. The coverage matrix names clauses, not scores, since "80 percent covered" tells a contract owner nothing about which twenty percent is the audit right. And the deletion section is honest about backup rotations, derived data, and support attachments, because the difference between a deletion promise and a deletion capability is the gap that surfaces at termination, when the leverage is gone and the data is still there.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
