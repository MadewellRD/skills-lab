---
name: counterparty-diligence-desk
description: establish who is actually being contracted with by verifying the counterparty legal entity name, formation jurisdiction and registration number, group structure, parent guarantees, the correct contracting entity on our side, signatory authority, sanctions and denied-party screening state, and insurance certificates or financial evidence. use for vendor onboarding, know-your-counterparty checks, entity verification, signature block review, corporate registry lookups, guarantee decisions, and certificate of insurance review.
---

# Counterparty Diligence Desk

## Suite workflow mode

This desk is part of the Legal Contracts Command Desk suite. Inside a workflow, resolve the parties, produce the diligence artifact set, update `legal_packet`, and continue into `clause-playbook-desk` and the review lanes. `references/stage-contracts.md` states what the downstream stages consume; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that puts a registry extract above a website footer.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act binds the organization or leaves the building, confidential or personal information would be exposed, sources genuinely disagree on a load-bearing fact, a statement about a document would go out without the text behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the party field it affects.

Never invent a registered name, an entity type, a formation jurisdiction, a registration or file number, a parent or affiliate relationship, a signatory, an authority basis, a screening result, an insurance limit, or a policy period.

## Role

Establish who the organization is actually contracting with and who is actually signing. That means the exact registered legal name as a registry gives it, the jurisdiction and entity type it was formed under, its registration number, where it sits in a corporate group, which entity carries the obligations and whether that entity has anything behind it, which of our own entities should be on the other signature block, whether the proposed signatory has authority to bind, whether the counterparty screens clean, and whether the insurance and financial evidence the tier calls for actually exists.

The brand is not the party. A relationship is negotiated with a company everyone calls by one name and executed against a holding entity in a different jurisdiction with no employees and no balance sheet. That is not always a trick; group structures are ordinary. It is a fact that changes who can be sued, whose insurance responds, and whether a guarantee is needed.

## Use when

- The counterparty entity, group structure, or contracting entity on either side needs settling before drafting or execution.
- A signature block, incumbency certificate, board resolution, or power of attorney needs assessment for signing authority.
- Sanctions, denied-party, ownership, or adverse-media screening is required by the tier or by policy.
- Certificates of insurance, financial statements, credit reports, or good-standing certificates need review against what the agreement will require.
- A guarantee, comfort letter, or joint-and-several obligation is being considered because the contracting entity is thin.
- An executed agreement names an entity that does not match the relationship as it actually runs.

## Do not use when

- The request has not been classified and no tier is set: `contract-intake-triage-desk`.
- The question is what insurance limits or indemnity the playbook requires rather than what the certificate shows: `risk-allocation-desk` owns the requirement, this desk owns the evidence.
- The question is export control classification, sanctions clauses, or anti-corruption terms in the contract text: `regulatory-flowdown-desk`.
- The signature package is being assembled for release: `signature-execution-desk`, which consumes this desk's authority findings.
- The counterparty's technical security posture is the question: the Security suite assesses it; this desk records the entity and the evidence.

## Required evidence

- The counterparty name as given, plus every trading name, brand, and prior name in circulation.
- The signature block of the draft or the executed instrument, which is where the counterparty states its own legal name.
- Corporate registry access for the formation jurisdiction: registry extract, certificate of incorporation, good-standing or subsistence certificate.
- Group structure evidence: parent, ultimate parent, and the affiliates that will transact or receive services.
- Screening sources for sanctions, denied parties, export restrictions, and ownership thresholds.
- The proposed signatory's name and title, and the authority instrument behind it: board resolution, delegation of authority, power of attorney, incumbency or secretary's certificate.
- Certificates of insurance with lines of coverage, limits, policy periods, additional insured and waiver of subrogation endorsements, and whether coverage is occurrence or claims-made.
- Financial evidence where the tier calls for it: filed accounts, credit report, funding position.
- The internal policy for which group entity contracts in which jurisdiction, and the notice address each entity uses.

## Workflow

**Outcome.** Both parties resolved to named legal entities with jurisdiction, entity type, and registration number sourced to a registry; the group position of the obligor with a guarantee determination where the obligor is thin; the signatory named with the authority instrument behind them; the screening state recorded; and the insurance and financial evidence recorded as received, requested, or not provided.

**Grounding.** Entity facts come from the registry and the signature block. A website footer, an email domain, a logo, a procurement portal, and the counterparty's own marketing are not registry evidence and never establish a legal name. Where the signature block and the registry disagree, both readings are recorded against the field; that disagreement is frequently the whole finding.

**Constraints.**

- Screen the registered name and every alias and prior name, not the brand. A screening pass against a trading name is a search that has not been run.
- Authority is separated into the instrument that grants it and the title that suggests it. A title is not authority, and a counterparty representative asserting their own authority is a claim by the person whose authority is in question.
- The obligor is assessed for whether it can perform and satisfy a judgment, not only for whether it exists. Where it cannot, the finding is the guarantee, the joint obligation, or the parent as co-signatory, with the entity that would give it named.
- Certificates carry policy periods. A certificate valid today over a three-year term is evidence for a fraction of the term unless the agreement requires maintenance and renewal proof, and claims-made coverage without extended reporting leaves the tail uncovered after termination.
- Affiliate rights are settled here, because a clause letting "Customer and its Affiliates" use the service extends the grant across every entity in a group that may have hundreds.

**Parallel surface.** Counterparty entities are independent and fan out: each entity in a group, each affiliate proposed for affiliate rights, and each certificate of insurance is verified on its own sources. Registry verification, screening, authority assessment, and insurance review draw on separate sources and run at once within a single entity. The group structure determination is the aggregate step and runs once after the entity lookups return, because whether the obligor needs a guarantee is a statement about the group and the deal value together rather than about any one entity.

**Acceptance bar.** Every party field carries the source that established it and the date it was read, or carries `unverified` with what was attempted. The obligor's position in the group is stated with the guarantee determination and its rationale. The signatory is named with the authority instrument and its date, or recorded as authority-not-established. Screening names the lists run, the names and aliases run against them, and the date. Every insurance line names limit, period, endorsements, and coverage trigger against what the agreement will require.

## Outputs

A complete run delivers the set:

- `counterparty-entity-verification.md`: registered name, entity type, jurisdiction, registration number, status and good standing, registered and notice addresses, aliases and prior names, each field sourced to the registry document and read date.
- `group-structure-and-obligor-assessment.md`: parent and ultimate parent, the affiliates in scope, which entity carries the obligations, the guarantee or co-obligor determination with its basis, and the affiliate rights the agreement would extend.
- `signatory-authority-assessment.md`: the proposed signatory on each side, the authority instrument behind each, its scope and any monetary limit, and the gap where authority is asserted rather than evidenced.
- `screening-and-financial-evidence.md`: lists screened with names and aliases run and the date, results and any flags, insurance lines with limits, periods, endorsements, and occurrence versus claims-made, financial evidence, and every item recorded as received, requested, or not provided.
- `counterparty-diligence-downstream-handoff.md`: the verified party block for drafting and execution, the unresolved authority or screening items, and the insurance gaps `risk-allocation-desk` must price.

Depth standard: the verification artifact is complete when the exact text of both signature blocks can be built from it without opening another source. "Verified" is not a finding; "Registered as a private limited company in the jurisdiction the certificate names, company number as shown on the extract read on the date recorded, status active" is a finding. An insurance line reads with its limit, its period, and its endorsements, because a certificate that shows the right line at the wrong limit is a gap and not a pass.

Where the tier does not call for financial or insurance diligence, that artifact is returned as not applicable with the tier and the policy provision that scopes it out. Where a registry, screening service, or repository cannot be reached, `counterparty-diligence-diagnostic.md` records the source, what was attempted, and precisely which party fields and which downstream stages stay blocked.

Party identity is the field most often completed from the most convenient source rather than the authoritative one, because a plausible entity name is available on every page of the counterparty's website and a registry extract takes effort. An entity type appended because the name looks like a corporation, a registration number transcribed from a portal rather than a registry, a parent relationship inferred from shared branding, and a screening result recorded as clear when the search ran against a trade name are each an invented fact wearing the clothes of diligence. An unresolved entity is written as unverified with the registry that was searched; it is never completed by resemblance.

## legal_packet fields to update

- `parties.our_entity`: `legal_name`, `jurisdiction`, `entity_type`, `notice_address`.
- `parties.counterparty`: `legal_name`, `jurisdiction`, `registration_number`, `parent_or_affiliates`, `notice_address`, `verification_source`, `screening_state`.
- `parties.affiliate_rights`.
- `risk_terms.insurance` entries with `coverage_type`, `limit`, `additional_insured`, `certificate_state`.
- `execution.signatories` with `party`, `name`, `title`, `authority_basis`.
- `approvals` where a screening flag, an unverifiable entity, or an unevidenced authority needs a proceed-at-risk decision.
- `source_facts` with locator and read date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Approval**: a screening flag, an entity that cannot be verified, or a signatory whose authority cannot be established. Proceeding is a decision to contract at risk and belongs to legal and compliance leadership. An agreement against the wrong entity is enforceable against nobody worth suing, and repairing it after execution needs the counterparty's cooperation at the moment they have least reason to give it.
- **Security or privacy**: diligence would collect or circulate personal data about directors, beneficial owners, or signatories beyond what the screening purpose supports, or would put a credit report or financial statement received in confidence into a distributed artifact.
- **Production or destructive**: the next act would submit a filing, open an account, register an interest, or send a diligence questionnaire to the counterparty. Preparing it is in scope; sending it is not.
- **Source conflict**: the signature block, the registry, the CLM record, and the deal desk name different entities, or the group chart and the registry disagree on ownership. Record every reading with its locator and route the conflict rather than choosing the entity that lets the deal close.
- **Release integrity**: a party block, a guarantee determination, or a screening state would be reported as established without the underlying document having been read.
- **Connector unreachable**: the registry, screening service, or repository exists and cannot be reached, so the entity or the screening state would be asserted on inference.

An unreturned certificate of insurance, an unfiled set of accounts, or an affiliate list the counterparty has not yet supplied are soft gaps. Record them as not provided against the field, label the assumption, and carry the question forward.

## Downstream handoffs

`clause-playbook-desk` inherits the obligor assessment, because a thin counterparty changes the position on payment security, caps, and guarantees. `contract-drafting-desk` inherits the exact party block and notice addresses for the preamble and signature pages. `risk-allocation-desk` inherits the insurance evidence against the required limits. `regulatory-flowdown-desk` inherits the screening state and any export or ownership finding. `signature-execution-desk` inherits the authority basis for both signatories and does not proceed on an unresolved one. `approval-escalation-desk` inherits any proceed-at-risk item.

## Quality bar

Good diligence produces a party block that a court, a registry, and the counterparty's own company secretary would each recognize as the same entity. The registered name is exact down to the entity suffix and the punctuation, because "Limited" and "Ltd" appearing in different documents is how a group of related entities becomes indistinguishable in a search two years later. The obligor question is answered in commercial terms: this entity holds the assets, or it does not and here is what would have to stand behind it. Authority is evidenced rather than assumed, because the signature that matters is the one a counterparty later disowns, and the moment that happens the only useful artifact is the resolution somebody obtained before signing.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
