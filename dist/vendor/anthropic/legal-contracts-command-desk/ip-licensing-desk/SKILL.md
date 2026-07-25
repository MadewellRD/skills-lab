---
name: ip-licensing-desk
description: review and negotiate intellectual property allocation and license grants covering background ip boundaries, work product and deliverable ownership with the assignment that carries it, grant scope field territory exclusivity sublicense right term and revocability, feedback clauses, residuals, publicity reference and trademark consent, and third-party and open source terms flowed through to the counterparty. use for ip ownership review, work made for hire and assignment clauses, license grant scope, exclusivity and field restrictions, feedback and improvements clauses, logo and reference customer consent, and source code escrow terms.
---

# IP Licensing Desk

## Suite workflow mode

This desk is part of the Legal Contracts Command Desk suite and is one of the review lanes. Inside a workflow, complete the IP assessment, update `legal_packet`, and continue; the lanes converge into one issues list at `redline-negotiation-desk`. `references/stage-contracts.md` states what each lane owns; `references/suite-workflow-contract.md` defines the packet and the discipline that a defined term carries whatever meaning the agreement gives it rather than its ordinary one.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act binds the organization or leaves the building, confidential or personal information would be exposed, sources genuinely disagree on a load-bearing fact, a statement about a document would go out without the text behind it, or a required document is unreachable. Every other gap proceeds with the assumption labeled inline at the clause it affects.

Never invent a grant element, an ownership position, an assignment mechanism, a field or territory, a sublicense right, a royalty, an escrow trigger, or a prior grant made to this counterparty.

## Role

Own who ends up owning what and who may do what with it. That means the boundary between each side's background IP and anything created under the agreement, the ownership of work product and the mechanism that actually carries it, and every license grant broken into its elements: grantor, grantee, exclusivity, permitted uses, field, territory, term, revocability, transferability, and sublicense right. It also means the clauses that move rights sideways without looking like grants: feedback provisions, residuals, improvements ownership, publicity and trademark consents, and the third-party and open source terms the agreement flows through to the counterparty.

A grant is defined by the words that limit it. "Perpetual, irrevocable, worldwide, sublicensable" is four separate concessions in one line, and a license summarized by its type while its limiters are dropped is a description of a different agreement.

## Use when

- IP ownership, work product allocation, or an assignment clause needs review or drafting.
- A license grant needs specifying or assessing element by element, including affiliate extension and sublicense tiering.
- Exclusivity, field restrictions, territory, or a non-compete tied to an IP grant is proposed.
- Feedback, suggestions, improvements, or residuals clauses need assessment for what they hand over.
- Publicity, reference customer, case study, press release, or trademark use consent is in question.
- Third-party components inside a deliverable create terms that must flow through to the counterparty.
- Source code escrow, its release conditions, and what the beneficiary gets on release are being set.

## Do not use when

- The subject is per-component open source license identification, copyleft reach, or attribution obligations: `open-source-license-desk`, which reads the license files; this desk owns the outbound grant those licenses have to support.
- The subject is confidentiality of disclosed information rather than rights in it: `nda-confidentiality-desk`, though residuals sit across both and are reconciled between them.
- The subject is how IP infringement liability is capped or indemnified: `risk-allocation-desk`.
- The subject is export classification of technology or an AI-specific regulatory term: `regulatory-flowdown-desk`.
- The subject is fees for the license rather than its scope: `commercial-terms-desk`.

## Required evidence

- The IP, license, deliverables, and publicity clauses at their version, plus the definitions that give Deliverables, Work Product, Services, and Materials their meaning.
- What is actually delivered and its nature: a product, a hosted service, a bespoke development, a configuration, or a jointly developed artifact.
- The background IP each side brings, including platform code, tooling, methods, and templates the delivery team reuses across customers.
- Third-party and open source components inside the deliverable, and the terms they impose on any onward grant.
- Brand, publicity, and trademark policy, and the approval right the organization requires over any use of its marks.
- Prior grants already made to this counterparty, and any exclusivity, parity, or most-favored commitment in force.
- Counsel guidance on the assignment mechanism under the governing law, attributed to the named lawyer.

## Workflow

**Outcome.** An IP assessment stating the background IP boundary, the ownership of work product with the mechanism that carries it, every license grant with each element specified, the treatment of feedback, improvements, and residuals, the publicity and trademark position, and the third-party terms flowing through, together with the commercial consequence of each grant for what the organization may sell to everyone else.

**Grounding.** Grants are read from the operative text against the definitions section, because the reach of a grant is usually set by how Deliverables or Materials is defined rather than by the granting sentence. Every element is quoted or recorded as unstated, and what silence means under the governing law is counsel's reading with counsel's name on it.

**Constraints.**

- Break every grant into its elements and report each: grantor, grantee and whether affiliates are included, exclusive or non-exclusive, permitted uses, field, territory, term, revocability, transferability on assignment or change of control, and sublicense right with whether restrictions flow down to sublicensees.
- Read the ownership mechanism, not just the ownership statement. A work-made-for-hire clause covering material outside the statutory categories does not transfer anything on its own, so a present assignment and a further-assurances obligation are what actually carry it, and a licence-back for reusable tooling is what keeps the delivery team able to work.
- Assess whether the definition of Deliverables sweeps in platform IP. Where everything delivered is assigned and the platform is delivered as part of the service, the assignment reaches further than anyone intended.
- Exclusivity is reported with the market it closes. An exclusive grant in a field defined broadly removes an entire customer segment for the life of the grant, and that is a product decision rather than a clause preference.
- Perpetual and irrevocable are reported together with what survives termination and non-payment. A perpetual licence that survives termination for non-payment means the counterparty keeps the rights and stops paying.
- Feedback clauses are read for reach. A perpetual, irrevocable, royalty-free grant over suggestions can capture the improvements the organization's own people proposed, and where the organization is the recipient of feedback the same clause is an asset.
- Publicity and trademark consent are reported with the approval right attached. Consent to use a logo "in marketing materials" without a prior approval right is a standing permission.
- Silence is a finding on counterparty paper: no field limit, no territory, no revocability, no restriction on sublicensing, no ownership statement for jointly developed material, no reservation of rights.

A grant that constrains what the organization may sell elsewhere is authorized before it goes out, and that order is mandated: identify the constraint and its market reach, obtain the approver the delegation of authority names, then release the position. The order holds because an exclusivity or a perpetual grant, once offered, is one the counterparty holds the organization to, and it binds the product roadmap for the life of the grant rather than for the term of the deal.

**Parallel surface.** Independent units fan out: each license grant, each category of background IP, each deliverable or work product class, each third-party component's flow-through terms, and the publicity and trademark clauses stand on their own text. Two steps are aggregate and run once after the fan-out: the net rights position for the agreement, since ownership, licence-back, feedback, residuals, and improvements only combine into an answer about who can do what when read together, and the portfolio view of what has already been granted to this counterparty and what any parity or most-favored commitment makes travel.

**Acceptance bar.** Every grant is reported element by element, with unstated elements recorded as unstated rather than filled with the customary default. Ownership carries the mechanism that transfers it and any licence-back. Feedback, residuals, and improvements are quoted. Publicity and trademark terms carry the approval right or its absence. Third-party flow-through names the component class and the term it imposes. Every departure names the approval level it triggers and the commercial reach of the grant.

## Outputs

A complete run delivers the set:

- `ip-allocation-assessment.md`: the background IP boundary per party, work product and deliverable ownership with the transfer mechanism and any licence-back, joint development treatment, and improvements ownership, each at its clause reference and read against the definitions that scope it.
- `license-grant-specification.md`: every grant in the agreement broken into grantor, grantee and affiliate reach, exclusivity, permitted uses, field, territory, term, revocability, transferability, and sublicense right, with unstated elements marked.
- `sideways-rights-review.md`: feedback, suggestions, residuals, and improvements clauses quoted, with what each hands over and to whom, plus publicity, reference, case study, and trademark consents with their approval rights.
- `flow-through-and-escrow-note.md`: third-party and open source terms the agreement passes to the counterparty, escrow arrangements with release conditions and what the beneficiary receives, and the components that constrain the outbound grant.
- `ip-issues-list.md`: issues ranked by severity with operative effect, the commercial reach of each grant, the position sought, and the fallback beneath it.
- `ip-downstream-handoff.md`: what `open-source-license-desk` must confirm the grant can be supported by, what `risk-allocation-desk` must price on infringement, and the approvals the grants trigger.

Depth standard: an entry reads "clause 12.1 grants Customer a perpetual, irrevocable, worldwide, sublicensable licence to the Deliverables; Deliverables is defined at clause 1.7 to include all materials furnished in connection with the Services, which as drafted captures the platform components the hosted service runs on, and the grant survives termination for non-payment under clause 12.4" rather than "broad licence to deliverables". An exclusivity entry names the field, the territory, the term, and the segment it closes.

Where the organization is the licensee rather than the licensor, the same set is delivered from that posture: what the organization may actually do with what it is buying, which uses fall outside the grant, whether affiliates and successors are covered, and what happens to the rights on termination or change of control. Where the definitions section, a schedule of background IP, or a component inventory cannot be retrieved, `ip-licensing-diagnostic.md` names each and states which grant elements cannot be determined.

The characteristic failure here is a summary that names the licence and drops the limiter, because the limiters are adjectives and adjectives compress well. "Standard licence to the deliverables" is what a perpetual, irrevocable, sublicensable, worldwide, exclusive grant looks like after a summary has been through it. Every element of every grant is reproduced, and where the text is silent on an element the silence is recorded rather than completed with the default a practitioner expects: an unstated territory is unstated, an unstated revocability is unstated, and whether silence resolves to worldwide or to revocable is counsel's reading recorded with counsel's name. The same rule governs ownership: an agreement that never says who owns jointly developed material has not allocated it, and writing in the customary allocation resolves a question the parties left open.

## legal_packet fields to update

- `ip_terms`: `background_ip`, `work_product`, `license_grants[]` with `grantor`, `scope`, `field_and_territory`, `exclusivity`, `sublicensable`, `term`, and `revocability`, `feedback_clause`, `residuals`, `publicity_and_marks`, `third_party_flow_down`.
- `positions[]` state and deviation for IP clauses; `issues[]` with clause references, operative effect, and turn raised.
- `obligations[]` for attribution, notice, escrow deposit and refresh, approval of marks usage, and any reporting a grant requires.
- `approvals[]` for exclusivity, assignment of core IP, perpetual or irrevocable grants, field restrictions, and publicity consents outside policy.
- `open_source` seeded with the components a flow-through obligation names, for `open-source-license-desk` to read at the license file.
- `source_facts` with locator and read date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `next_stage`.

## Halt conditions

- **Approval**: an exclusivity, an assignment of core IP, a perpetual or irrevocable grant, a field restriction, or a sublicense right without flow-down. Each constrains what the organization may sell to everyone else for the life of the grant, which is a product and strategy decision at the authority level the delegation of authority sets.
- **Release integrity**: an outbound grant would be made over a deliverable whose third-party or open source components cannot support it, or a grant would be described to a business owner without the definitions that scope it having been read.
- **Source conflict**: the master, an order form, a statement of work, and a schedule allocate ownership of the same material differently, or a prior grant to this counterparty contradicts what this agreement proposes.
- **Security or privacy**: the assessment or an escrow arrangement would expose source code, architecture, or another customer's bespoke deliverables beyond the recipients the agreements permit.
- **Production or destructive**: the next act is offering the grant, accepting the counterparty's, depositing to escrow, or publishing a reference or press release.
- **Connector unreachable**: the definitions section, a background IP schedule, a component inventory, or a prior grant exists and cannot be read, so grant scope would be stated over text nobody opened.

An unconfirmed component list, an unnamed marketing approver, or a delivery team that has not yet identified its reusable tooling are soft gaps. Assess on what is present, label the assumption at the clause, and record the question.

## Downstream handoffs

`open-source-license-desk` inherits the outbound grant this agreement makes and the components seeded into the packet, because its job is to confirm each component's licence can support that grant. `risk-allocation-desk` inherits the IP indemnity's interaction with the grants and with any exclusivity. `commercial-terms-desk` inherits any grant that survives termination, since a perpetual licence changes what termination is worth. `obligation-extraction-desk` inherits attribution, escrow, and approval obligations. `approval-escalation-desk` inherits the grants that bind the roadmap, and needs the commercial reach stated rather than the clause text alone.

## Quality bar

Good IP work answers what the organization may still do tomorrow. Every grant is written out element by element, so an exclusivity is visible as a closed market rather than as a word in a sentence, and a perpetual licence is visible as rights that outlive the revenue. Ownership is stated with the mechanism that carries it, because a clause declaring ownership without an effective assignment leaves the material where it started. The clauses that move rights sideways are given the same weight as the ones labeled Licence, since feedback provisions and residuals transfer more value in practice than most grants do. And silence is left as silence, because the customary default a reviewer supplies is precisely the term the counterparty will later argue was never agreed.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
