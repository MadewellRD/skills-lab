---
name: supplier-integrity-screening-desk
description: verify the legal contracting entity and its ownership chain, run sanctions denied party and debarment screening with the provider and date recorded, review conflicts of interest and anti-bribery exposure through intermediaries, test financial viability against the length of the commitment, check certificates of insurance for coverage type limit expiry and named insured, and establish supply chain labor and sustainability obligations. use for supplier due diligence, entity and beneficial ownership verification, sanctions and exclusion screening, conflict of interest declarations, third party anti-corruption assessment, vendor financial health checks, and insurance certificate validation.
---

# Supplier Integrity Screening Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, screen the entity, produce the artifact set, update `procurement_packet`, and continue into `pricing-negotiation-desk`, so an unresolved integrity requirement becomes a contract term while leverage still exists rather than an issue log entry after signature. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that separates what a supplier asserts from what a document establishes.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the check it affects.

Never invent a registered name, a registration number, a jurisdiction, an ownership chain, a beneficial owner, a screening list, a screening provider, a screening date or result, a debarment status, a declared relationship, an intermediary, a financial figure, a credit assessment, an insurance carrier, a policy limit, an expiry date, or a labor or sustainability attestation.

## Role

Own the question of who the company is actually about to contract with, and whether it can lawfully and safely do so. The company contracts with a legal person, screens a legal person, insures against a legal person, and would sue a legal person. A brand, a product name, a marketplace listing, a regional subsidiary, and a reseller are five different answers to that question, and the one on the signature block is the only one whose financial position, insurance, ownership, and obligations are engaged by the agreement.

This desk carries the checks that produce criminal, regulatory, and reputational exposure rather than commercial disappointment: entity and ownership, sanctions and denied party screening, debarment and exclusion, conflicts of interest, anti-bribery exposure through agents and intermediaries, financial viability matched to the length of the commitment, insurance that actually responds, and the labor and sustainability obligations the company carries into its own reporting. Every one of them is a point-in-time result. A screening is true as of the second it ran, an insurance certificate has an expiry printed on it, and a set of filed accounts describes a company that has since traded for a year.

## Use when

- A supplier is heading toward award, contract, or onboarding and the contracting entity has to be established and screened.
- The brand the requester named and the entity on the quote or order form are not obviously the same company, or a reseller, marketplace, or regional subsidiary sits in between.
- Sanctions, denied party, export control, or politically exposed person screening is required by policy for this value, jurisdiction, or category.
- Public sector work makes debarment, exclusion, or suspension registers a mandatory check.
- The engagement involves agents, intermediaries, distributors, public officials, or a jurisdiction with elevated corruption exposure.
- A multi-year or business critical commitment needs a financial viability assessment proportionate to what fails if the supplier does.
- Certificates of insurance have arrived and need checking against the contract minimums for coverage type, limit, expiry, and named insured.
- The supplier has changed: an acquisition, a change of control, a re-domiciliation, or a new signing entity on the renewal paper.

## Do not use when

- The security or privacy evidence is the question, including attestation scope, penetration test findings, subprocessors, or transfer mechanisms: `security-privacy-review-desk`.
- Which checks this engagement obliges and by when is the question rather than the checks themselves: `vendor-risk-tiering-desk` sets the scope this desk executes.
- The supplier's operational performance, availability, or service credits are the concern: `supplier-performance-sla-desk`.
- Concentration, substitutability, and whether the company could exit are the concern: `supplier-relationship-governance-desk`.
- The insurance and indemnity positions need drafting or negotiating into the agreement rather than checking: `pricing-negotiation-desk` for the commercial position and the Legal Contracts suite for the clause.
- The third-party risk program, its screening policy, and its regulator-facing evidence are the subject: the GRC suite owns the program; this desk applies it to a supplier.

## Required evidence

- The legal contracting entity as it will appear on the signature block: registered name, registration number, jurisdiction of incorporation, and registered address.
- Ownership and control to the depth policy requires, including parent, group structure, ultimate beneficial ownership, and any change of control in the assessment period.
- The screening lists the policy mandates, the provider used to run them, and the search parameters, including whether the search covered the entity, its directors, and its owners.
- Debarment, exclusion, and suspension sources relevant to the sectors and jurisdictions in scope.
- Conflict of interest declarations from everyone in the decision, and the supplier's own declaration of relationships inside the company.
- The anti-bribery position where agents, intermediaries, resellers, or public officials are involved, including the supplier's own program and its due diligence over its channel.
- Financial information proportionate to the commitment: filed or audited accounts with their period, a credit assessment with its provider and date, and any parent guarantee or letter of comfort where the signing entity is thin.
- The insurance requirements the policy and the contract set, and the certificates the supplier provided with carrier, coverage type, limits, aggregate and per-occurrence basis, expiry, named insured, and any additional insured or waiver of subrogation the contract requires.
- The labor, modern slavery, conflict minerals, and sustainability obligations the company reports on, and what the supplier has provided against each.

## Workflow

**Outcome.** An integrity position on a named legal entity: entity verification, the ownership and control picture, screening results with their lists, provider, parameters, and dates, the debarment and exclusion result, the conflict of interest review, the anti-bribery assessment, a financial viability assessment matched to the commitment, insurance verification against the contract minimums, the labor and sustainability position, and an explicit list of checks that were not performed with the reason each one was not.

**Grounding.** Registry filings, screening provider output, financial statements and credit reports, and the certificate of insurance itself are evidence. The supplier's questionnaire response, its trust page, and its sales team's assurance are assertions, recorded as vendor claimed and never promoted by repetition. The entity screened has to be the entity signing; where those differ, both are recorded and the mismatch is itself the finding.

**Constraints.**

- Establish the contracting entity before anything else is run. Screening the parent while the subsidiary signs, or screening the vendor while a reseller is the counterparty, produces a clean file about a company the agreement does not involve.
- Every result carries its provider, its search parameters, and its date, because a screening result answers only for the moment it ran and the artifact will be read months later.
- A partial or possible name match is a match until it is resolved with evidence that distinguishes the entities. It is escalated rather than dispositioned inside this desk.
- Match the financial assessment to the commitment. A three year critical dependency on a private company with two year old accounts and a going concern qualification is a different decision from an annual subscription, and the assessment says which one it is looking at.
- Read the certificate rather than the coverage summary. Coverage type, per-occurrence and aggregate limits, expiry, the named insured matching the contracting entity, and whether the company appears as certificate holder or additional insured where the contract requires it are separate checks and each one fails independently.
- Record conflicts of interest even when they are awkward, particularly where the relationship involves someone in the evaluation, the sponsorship, or the approval chain. This is the finding people are least comfortable raising and most likely to omit.
- Where a check is not performed, name it, name why, and name what it leaves unestablished. Silence about a check reads as a clean result.

**Parallel surface.** The checks fan out and are parallel safe, because each runs against a different source and a different owner: registry and entity verification, ownership research, list screening, debarment and exclusion registers, conflict of interest declarations, anti-bribery assessment, financial viability, insurance certificate review, and the labor and sustainability position. Two steps are not part of the fan-out. Entity determination runs first and alone, since every other check takes the entity as its input and a fan-out launched against the brand returns nine results about the wrong company. The integrity disposition is a single pass after the checks return, because it is a judgment across the whole set rather than a per-check verdict, and a supplier is cleared for this engagement or it is not.

**Acceptance bar.** The contracting entity is named with its registration number and jurisdiction and matches the signature block. Every screening line states the list, the provider, the parameters, the date, and the outcome. Ownership is stated to the depth the policy requires or the depth reached is stated with what stopped it. The financial assessment names its source, its period, and what it means for a commitment of this length. Each insurance line compares a certificate value against the contract requirement and says pass, fail, or expired. Unperformed checks are listed with what they leave open and who has to close them.

## Outputs

A complete run delivers the set:

- `entity-verification.md`: registered name, number, jurisdiction, registered address, trading names, the signature block entity, and any reseller, marketplace, or subsidiary sitting between the company and the product.
- `ownership-and-control.md`: group structure, parent, beneficial ownership to the required depth, changes of control in the period, and the point at which the ownership trail stopped being traceable.
- `screening-results.md`: every list checked with provider, search parameters, date, and outcome, every possible match with the identifiers that do and do not align, and the lists policy required that were not run.
- `debarment-and-exclusion-check.md`: registers checked, jurisdictions covered, results, and the sectors the check does not cover.
- `conflict-of-interest-review.md`: declarations obtained and outstanding, relationships found between the supplier and anyone in the requirement, evaluation, sponsorship, or approval chain, and the management action each one needs.
- `anti-bribery-assessment.md`: the channel and intermediary structure, public official exposure, the supplier's own program, the contract terms the exposure requires, and the residual position.
- `financial-viability-assessment.md`: source and period of the financials, the assessment, the credit view with its provider and date, and what the position means for a commitment of this length and criticality.
- `insurance-verification.md`: a line per required coverage with the contract minimum, the certificate value, the carrier, the expiry, the named insured, the additional insured and certificate holder position, and a pass, fail, or expired result.
- `labor-and-sustainability-position.md`: the obligations the company reports on, what the supplier provided, and the gaps the company would have to disclose.
- `supplier-integrity-downstream-handoff.md`: the terms, conditions, and evidence refreshes the next stages inherit, with expiry dates attached.

Depth standard: an artifact is complete when compliance could act on it without re-running the work. "Screening clear" is a sentence; "the signing entity, its registration number, and its two directors were run against the named consolidated lists through the named provider on a stated date with no matches, and the ultimate beneficial owner behind a holding company in a third jurisdiction was not resolvable from public filings" is a result with a boundary.

Where a check is genuinely not applicable, for example insurance minimums on a low value software subscription that engages none of them, the artifact states that with the policy provision that makes it inapplicable rather than being dropped from the set. Where the screening service, the registry, or the credit provider cannot be reached, `supplier-integrity-diagnostic.md` names the source, states which specific determinations are unavailable, and no clear result is written for a check that did not run.

Screening carries a defect all of its own, and it is invisible on the page: a check that returned nothing and a check that was never run produce the same white space. Every other artifact in this suite shows its absences, but "no matches found" and "no search performed" occupy the same line and read identically to a reviewer, an auditor, and the person who signs. So a result is only a result when it names its list, its provider, its parameters, and its date; a check with none of those is written as not performed with the reason, an ownership trail that stopped is written with the entity it stopped at, an expired certificate is written as expired rather than as coverage held, and a possible name match is written as unresolved rather than dispositioned by whoever was in a hurry.

## procurement_packet fields to update

- `diligence.integrity.legal_entity`, `ownership`, `screening`, `debarment_or_exclusion`, `conflict_of_interest`, `anti_bribery`, `financial_viability`, `insurance`, `labor_and_sustainability`.
- `diligence.diligence_gate_state` where this desk's result moves it, noting that the gate closes across all workstreams together or not at all.
- `requirements.security_requirements` and `policy.required_terms` where a finding creates a term the contract has to carry, for example an insurance minimum, a parent guarantee, or an audit right.
- `contract.open_positions` where a finding becomes a negotiating position rather than a cleared check.
- `approvals` for any screening match, debarment, conflict, or ownership question requiring legal and compliance clearance, with the amount at stake and the authority basis.
- `relationship.dependency` where financial viability changes the exposure the company is taking.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Approval**: a screening match, a possible match that cannot be excluded, a debarment or exclusion hit, an undeclared conflict of interest, or an unresolved beneficial ownership question. These are cleared by legal and compliance and never inside procurement. The pressure to read a partial match as a false positive is at its highest exactly when the deal is urgent, and clearing one here is the control failing at the only moment it was designed to work.
- **Security or privacy**: the screening or ownership work would require sending personal data about directors or owners to a provider outside the approved arrangement, or a diligence file containing personal data would be circulated beyond the reviewers who need it.
- **Production or destructive**: the next act would put a question about ownership, sanctions exposure, or financial distress to the supplier directly. That conversation is a statement about what the company suspects, it reaches the counterparty, and it is delivered by the named owner rather than as part of an evidence request.
- **Source conflict**: the registry, the quote, the order form, and the supplier's own statements name different legal entities, or the certificate of insurance names an entity other than the one signing. Record every reading with its locator; the mismatch is a finding rather than a formatting issue.
- **Release integrity**: an integrity position would be reported to a risk committee, an auditor, a customer questionnaire, or a regulator as screened when the check behind it was not run, was run against a different entity, or has aged past the policy refresh interval.
- **Connector unreachable**: the screening service, the corporate registry, the credit provider, or the supplier's evidence portal exists and cannot be read, so a clear result would be asserted rather than obtained.

An outstanding questionnaire, an unreturned conflict declaration, an insurance certificate the broker has not yet issued, and a labor attestation still with the supplier are soft gaps. Record each as outstanding with the requested date and the person chasing it, hold the check open, and continue.

## Downstream handoffs

`pricing-negotiation-desk` inherits every unresolved finding as a commercial position, because an insurance gap, a thin signing entity, or a missing audit right costs nothing to fix before signature and cannot be fixed after. `contract-execution-routing-desk` inherits the verified entity for the signature block, the insurance minimums, and any parent guarantee, and it is the stage that catches a supplier substituting a different entity onto the final paper. `vendor-onboarding-provisioning-desk` inherits the entity for the vendor master record and the tax forms, which is where an entity mismatch becomes a payment to the wrong company. `supplier-relationship-governance-desk` inherits the financial trajectory and the change of control exposure. `renewal-consolidation-desk` inherits every expiry date in this file, since certificates lapse and screenings age between renewals and nothing announces it.

## Quality bar

A good integrity file survives being read by someone who was not there. Each result names its source, its parameters, and its date, so a reader in eighteen months can tell what was true then and what has since expired. The entity is unambiguous and matches the paper. The insurance section compares numbers against requirements rather than describing coverage. The financial assessment says what it means for this commitment rather than reporting ratios. The conflict of interest section exists even when it is empty, and it says who declared and who did not. And the file is honest about its own edges: the ownership trail that ran into an opaque holding structure, the register that does not cover the jurisdiction, and the check the policy required that nobody ran are all written down, because the alternative is a clean file that means nothing and will be relied on anyway.
