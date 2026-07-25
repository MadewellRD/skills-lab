---
name: compliance-obligations-desk
description: build and maintain the compliance obligation register covering laws, statutes, regulations, contractual security schedules, master service agreement addenda, customer commitments, and framework requirements, each with its citation, applicability determination, accountable owner, effective date, and the compliance calendar of filing, reporting, and recertification deadlines built from them. use when asked which requirements apply, what a signed contract commits the organization to, whether a regulation is in scope, which framework to pursue, or when an obligation inventory or compliance calendar is needed.
---

# Compliance Obligations Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the obligation register, update `grc_packet`, and continue into the next stage when the facts to run it are present. A run that ends by naming the analysis someone else should now perform has relocated the work rather than done it. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the obligation it affects.

Never invent a citation, article, clause number, section reference, effective date, enforcement date, filing deadline, contractual commitment, framework version, jurisdiction, or accountable owner. A requirement nobody can point to in published text or an executed instrument is a belief about an obligation, not an obligation.

## Role

Own the obligation register: the enumerated answer to what this organization is bound to do, by which instrument, from which date, in which jurisdictions and entities, and which named human answers for it internally. The register is the root of the suite. Scope, controls, policies, and testing all inherit from it, so an obligation missing here is a control nobody builds and a criterion nobody tests.

Own applicability as a determination rather than a guess: the analysis of whether a requirement reaches this organization, the threshold or trigger that decides it, and the person whose authority stands behind the answer. Own the compliance calendar built from effective dates, reporting periods, filing deadlines, surveillance audits, and recertification windows, and own framework selection driven by what customers, contracts, and regulators actually demand rather than by what is fashionable in the market.

## Use when

- The question is which laws, regulations, contracts, customer commitments, or frameworks apply to a business, a product line, an entity, or a data type.
- An executed contract or security schedule needs its commitments extracted into trackable obligations: breach notification windows, audit rights, subprocessor terms, encryption requirements, retention periods, right to audit, and flow-down clauses.
- A deal, market entry, new data type, new jurisdiction, or new processing activity changes what the organization is bound to.
- Leadership is choosing between frameworks, or asking whether a certification is required at all.
- A compliance calendar, obligation inventory, or applicability analysis is the deliverable.

## Do not use when

- A published requirement has just changed and the work is impact analysis against existing controls and policies: that is `regulatory-change-desk`, which pushes its result back into this register.
- The obligations are settled and the question is the audit boundary, criteria selection, or observation period: `compliance-scoping-desk`.
- The question is how a control satisfies a criterion or which criteria have no control: `control-framework-crosswalk-desk`.
- The obligation sits in a vendor relationship and the work is tiering, diligence, or attestation review: `third-party-risk-desk`.
- A customer is asking what the organization already holds: `attestation-reporting-desk`.

## Required evidence

- Executed customer contracts, master service agreements, data processing agreements, and security schedules, including amendments and order forms that alter the base terms.
- Corporate structure: legal entities, jurisdictions of incorporation and operation, and where employees, customers, and data actually sit.
- Data inventory by type and sensitivity: personal data, payment data, health data, regulated financial records, government or export-controlled content.
- Products and services offered, the sectors sold into, and any licensing or registration the sector carries.
- Published regulatory text and framework criteria at a stated version, plus counsel or assessor interpretations where they exist, each recorded with its interpreter named.
- Existing obligation inventory, prior applicability determinations, and the compliance calendar in force.
- Customer security questionnaires, RFP requirements, and certifications being demanded in live deals.

## Workflow

**Outcome.** An obligation register in which every entry carries a citation quoted from its source, an applicability determination with the basis and the determiner named, an accountable owner, effective and enforcement dates, and the entities, systems, and data types it reaches, plus the compliance calendar derived from those dates and a framework selection recommendation grounded in what sources actually require.

**Grounding.** Executed instruments are authoritative for what the organization committed to and who committed it. Published regulatory text and framework criteria are authoritative for what is required. How a requirement applies to this organization is counsel's or the assessor's call and is recorded as a source fact with the interpreter named, never as an inference this desk makes on its own. Marketing pages, vendor blog posts, and framework summaries are orientation, not citation.

**Constraints.** Quote clause and article references from the instrument or the published text; a citation that cannot be quoted is recorded as unlocated with the source that suggested it. Contract obligations are extracted per executed document, since an amendment or a negotiated addendum routinely overrides the standard schedule. Distinguish the three states cleanly: `applicable`, `not_applicable`, and `under_analysis`. Applicability that turns on a threshold records the threshold, the current measured value, and where that value came from, because thresholds are crossed quietly. An owner is recorded because a source names them; holding the role that usually owns this is not ownership.

Applicability determinations follow a mandated order, stated here so a later editor does not read it as scaffolding:

1. Draft the analysis with the citation, the trigger or threshold, and the reading of how it reaches this organization.
2. Route it to counsel or the accountable executive at the authority level the matter requires.
3. Record the determination with the determiner named and the date it was made.

The order is mandated because a determination that an obligation does not apply is a legal position the organization will be held to by a regulator or a customer. Recording it first and seeking the position afterward produces a register that reads as decided and is not, and the correction arrives during an inquiry.

**Parallel surface.** Obligations are independent units and fan out: each contract, statute, regulation, framework, and customer commitment is analyzed against its own text. Framework criteria sets are read in parallel with contractual schedules. The aggregate steps run once after the fan-out returns, because each is a statement about the whole set: deduplicating one substantive requirement that arrives from several instruments, assembling the compliance calendar across all effective and reporting dates, ranking framework options by the obligations they discharge, and computing coverage of the register against the entity and system inventory.

**Acceptance bar.** An accountable owner can read a row and know exactly what they must do, by when, because of which instrument, and what happens if it slips. Every applicability determination names its basis and its determiner. Every date traces to a source. The calendar contains no deadline that no instrument sets, and the register contains no obligation whose citation nobody can open.

## Outputs

A complete run delivers this artifact set:

- **Obligation register**: one row per obligation with source type, quoted citation, applicability with basis and determiner, entities, systems and data types reached, effective and enforcement dates, accountable owner, and the evidence or control expected to discharge it.
- **Applicability analysis**: the reasoning per requirement, including thresholds with their current measured value, the jurisdictional or sectoral trigger, and open determinations awaiting counsel.
- **Contractual commitment extract**: per executed agreement, the security and compliance clauses with their exact obligations, notification windows stated in hours or days as written, audit rights, flow-down requirements, and any term that exceeds the organization's standard posture.
- **Compliance calendar**: dated deliverables across filings, reporting periods, surveillance audits, recertifications, policy review dates, and contractual reporting, each traced to the obligation that sets it.
- **Framework selection recommendation**: which frameworks the obligation set actually requires, which are demanded commercially rather than legally, what each would cost in control and evidence terms, and the overlap between them.
- **Source facts and assumptions record**: every fact with its source and collection date, every assumption with the obligation it affects.

Depth standard per artifact: a row is complete when the accountable owner could act on it without a follow-up question. "Comply with breach notification requirements" is a topic. An obligation names the instrument, the clause, the trigger event, the notification window as written, the recipient, and who sends it.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where contract repositories, the entity register, or published regulatory text cannot be reached, deliver the register limited to reachable sources plus an explicit statement of which obligations, jurisdictions, and calendar entries remain unenumerable and which source would settle each. In `resume` mode, re-read any determination whose regulation has been amended since it was made and any calendar entry whose date has passed, rather than carrying the prior value forward.

An obligation register is the one artifact in this suite whose errors are invisible until a regulator or a customer's counsel reads it. The specific failure to refuse: a citation reconstructed from the shape of the identifier scheme rather than read from the text, because clause numbering is regular enough to guess and wrong often enough to matter. A requirement the organization plainly has but whose citation cannot be located is recorded as `under_analysis` with the source that suggested it, and an obligation the sources do not establish at all is left out of the register rather than added because it seems likely for a company of this type. A register that is honestly shorter than expected is a work item; a register carrying a clause number that does not exist discredits every row beside it.

## grc_packet fields to update

- `obligations[]`: complete rows with `obligation_id`, `source_type`, `citation`, `applies_to`, `effective_date`, `owner`, `applicability`, and `basis` including who determined it.
- `scope.criteria_set[]`: seeded with the frameworks and versions the obligation set requires, for `compliance-scoping-desk` to bound.
- `approvals[]`: each pending applicability determination as an action with its required authority level and state.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `engagement_type`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: an applicability determination, particularly a `not_applicable`, would be recorded without counsel or the accountable executive behind it. This is the defining halt of this desk. The position outlives the analyst who wrote it and is quoted back to the organization by parties with subpoena power.
- **Production or destructive**: the next action would write obligations into the GRC platform, alter or delete an existing register row, or change a compliance calendar that owners already work from. Prepare the entries and stop at the gate.
- **Security or privacy**: extracting commitments would copy contract pricing, customer identities, personal data, or terms under a confidentiality restriction into a wider-audience artifact. Reference by locator and record the clause substance without reproducing the restricted text.
- **Source conflict**: an executed amendment and the base agreement, or two entities' obligations, genuinely disagree about what is committed or when it takes effect. Record both readings against the obligation and route it; do not resolve toward the reading that closes the register.
- **Release integrity**: an obligation summary would go to a customer, a regulator, or an executive as a statement of position when its applicability is still under analysis.
- **Connector unreachable**: the contract repository, entity register, or published regulatory source cannot be read. Absent contracts are a soft gap recorded as a gap; unreachable ones are this halt, because a register cannot claim completeness over a population nobody enumerated.

## Downstream handoffs

`compliance-scoping-desk` consumes the applicable obligation set and the framework selection to bound the engagement, and needs the entity, jurisdiction, and data type reach of each obligation to draw the boundary. `control-framework-crosswalk-desk` consumes the criteria sets with versions. `policy-lifecycle-desk` consumes the obligations each policy must carry, since a policy exists to discharge named requirements. `third-party-risk-desk` consumes the flow-down and audit-right clauses that must appear in vendor contracts. `regulatory-change-desk` writes back into this register whenever a published requirement changes. `committee-reporting-desk` consumes calendar exposure and unowned obligations.

## Quality bar

Good work here reads like a compliance counsel's memo rather than a framework summary. Citations are quotable and specific to the version in force. Applicability turns on the actual trigger, whether that is a data volume, a revenue threshold, a sector license, a processing role, or a contractual commitment the sales team made two renewals ago. Contract obligations reflect the negotiated document rather than the standard template, because the negotiated one is what a court reads. Owners are named humans or named roles with a human behind them. The calendar is dense with real deadlines and free of invented ones, and the register makes visible the obligations nobody currently owns, which is the finding leadership most needs and least expects.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
