---
name: regulatory-flowdown-desk
description: review the compliance clauses in an agreement covering export control and sanctions, anti-corruption, prime contract flow-downs read clause by clause, sector obligations the counterparty passes through, accessibility commitments, and ai-specific terms on model use, training data, output ownership and disclosure, then name the internal owner and the operational obligation each accepted clause creates. use when asked about ear or itar classification, eccn, ofac and denied party screening, fcpa or bribery act clauses, far and dfars flow-downs, cmmc, hipaa business associate terms, glba, dora, nis2, pci, fedramp, section 508 or en 301 549 and vpat commitments, eu ai act roles, or a counterparty compliance addendum.
---

# Regulatory Flowdown Desk

## Suite workflow mode

This desk is a stage of the Legal Contracts Command Desk suite. Complete the clause-by-clause compliance review, the flow-down analysis, and the internal obligation map, update `legal_packet`, and continue into the next stage when the facts to run it are present. A run that ends by advising that compliance should look at the addendum has forwarded the document rather than reviewed it. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, and reading discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next act would bind the organization, restricted technology or personal data would be exposed, a published requirement and a clause genuinely disagree, a conformance statement would go out without evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the clause it affects.

Never invent a clause number, an ECCN, a license exception, a certification status, a conformance level, an accreditation, an audit right, a screening result, or the text of a regulation. A compliance clause is read and quoted, never recalled. The clause the organization signs is the standard it is measured against, and it is frequently not the same as the rule underneath it.

## Role

Own the part of the agreement that imports outside law and someone else's contract into this one. That means export control and sanctions terms with the classification and screening duties they create, anti-corruption terms with their audit and termination rights, prime contract flow-downs identified clause by clause rather than accepted as a block, sector obligations the counterparty carries and is passing through, accessibility commitments matched against what the product actually conforms to, and AI terms covering model use, training data, output ownership, and disclosure.

Own the translation step that this domain usually skips: every accepted clause becomes an internal obligation with a named owner and an operational act. A flow-down that says the subcontractor shall report cyber incidents within seventy-two hours is not a legal position; it is a change to the incident runbook, an escalation path, and a duty that lands on a security team that has not been asked. Signing the clause without naming that owner is how the organization acquires obligations nobody is performing.

## Use when

- The agreement carries an export, sanctions, anti-corruption, trade, or compliance addendum, or a counterparty questionnaire has produced one.
- A prime contract, a government contract, or a large customer's master agreement flows terms into this subcontract and the flow-down list has to be read rather than accepted.
- The counterparty is a regulated entity passing through sector obligations from banking, healthcare, insurance, defense, telecom, or critical infrastructure supervision.
- The agreement makes an accessibility commitment, or asks for a conformance report over a product whose actual conformance state is a separate question.
- The agreement contains AI terms: restrictions on model use, training on customer data, ownership of outputs, model disclosure, human oversight commitments, or a role allocation under an AI regime.
- The organization operates or delivers across jurisdictions whose requirements interact, for example a data localization commitment sitting next to an export restriction.
- A compliance clause the organization already accepted needs its internal owner and operational obligation established.

## Do not use when

- The clause is about processing personal data, transfer mechanisms, subprocessors, breach windows, or deletion: `data-protection-terms-desk` owns those and this desk owns the regulatory terms around them.
- The clause commits to security controls, attestations, remediation windows, or assessment rights: `security-exhibit-desk`.
- The question is whether the counterparty entity is screened, verified, or sanctioned: `counterparty-diligence-desk` runs screening, and this desk owns the clause that creates the ongoing screening duty.
- The question is component licensing inside the deliverable: `open-source-license-desk`.
- The accepted clause now needs a control, a test, and evidence on a cadence: that belongs to the GRC suite, and this desk hands over the obligation with its clause reference and window.
- The clause needs drafting into a counterproposal and rationale for the counterparty: `redline-negotiation-desk`.

## Required evidence

- The draft or executed agreement with every compliance addendum, exhibit, and attachment, at the version in force.
- The prime contract or upstream agreement with its actual flow-down clause list, including clauses incorporated by reference and the substitution instructions that tell you how to read party names in a flow-down.
- The jurisdictions and sectors both parties operate in, and where the product is delivered, hosted, supported, and accessed from.
- Export classification for what is delivered, with the basis: the classification determination, who made it, and when, including whether encryption functionality changes the answer.
- Screening obligations already in force and the systems that perform them.
- The organization's accessibility conformance evidence: the current conformance report, its date, the standard and level it was tested against, and its known exceptions.
- AI system facts where AI terms are present: what the system does, whether the organization is supplying or deploying, what data trains or fine-tunes it, and what disclosure the product already makes.
- Compliance counsel guidance where one exists, recorded with the named lawyer.
- The internal function map, so an accepted obligation can be assigned to an owner rather than to a department name.

## Workflow

**Outcome.** A clause-by-clause disposition of every compliance term in the agreement, each carrying what the clause actually requires in operative terms, whether the underlying obligation genuinely applies to this transaction, the position sought where it does not, and for every clause the organization accepts, the internal obligation it creates with a named owner, an act, a cadence, and the evidence that would show performance.

**Grounding.** The clause text governs what the organization owes the counterparty. The published requirement governs what the law requires, and the two are read separately because they diverge constantly: a flow-down often overstates, understates, or freezes an obligation at a superseded version. The prime contract's own clause list governs which flow-downs are actually mandatory, since a counterparty's compliance addendum routinely includes clauses the prime never required. Conformance is established by a conformance report with its date, standard, and scope, never by the product's reputation. Interpretation of how a regulation applies is counsel's, recorded with the named lawyer who gave it.

**Constraints.** Read flow-downs clause by clause and record each as mandatory under the prime, negotiable, or not present in the prime at all, because the third category is common and is where most of the recoverable ground sits. Preserve the distinction between a clause that requires an outcome and a clause that requires an effort standard, since `shall comply` and `shall use commercially reasonable efforts to comply` allocate the failure differently. Where a clause states a legal requirement, quote the clause and separately record whether the underlying rule says the same thing; accepting a clause that misstates the rule leaves the organization liable to the counterparty against a standard neither party actually owes. Match every accessibility commitment against a dated conformance report and its exceptions, and never state a conformance level the report does not support. For AI terms, establish the role allocation the text creates rather than the role the parties assume, since supplier and deployer duties differ and the clause is what assigns them. Treat a certification, accreditation, or authorization the organization does not hold as a future commitment with a date and an owner, not as a current state.

**Parallel surface.** Clauses are independent units and fan out: reading each compliance clause, checking each flow-down against the prime contract's list, testing each sector obligation against what this transaction actually involves, and drafting each position proceed concurrently, and the export, anti-corruption, sector, accessibility, and AI lanes stand on their own inputs. Three passes run once after the fan-out returns, because each is a statement about the whole set: the conflict check across clauses, where a data localization commitment, an export restriction, and an audit right can each be acceptable alone and impossible together; the internal owner map, where the aggregate load on a single function determines whether the accepted set is performable rather than whether any one clause is; and the jurisdictional overlay, where the same delivery model has to satisfy several regimes at once.

**Acceptance bar.** Every compliance clause in the agreement has a disposition and none is left as reviewed. Every flow-down is traced to the prime contract's clause list or recorded as not located there. Every accepted clause has a named internal owner, the act it requires, its cadence, and what would evidence it. Every accessibility or conformance statement traces to a dated report. No clause is described by the rule it invokes rather than by the words it uses.

## Outputs

A complete run delivers this artifact set:

- **Compliance clause register**: one row per clause with its reference, the regime it belongs to, what it requires in operative terms, whether it applies to this transaction, its disposition of accept, negotiate, or reject, and the position sought.
- **Flow-down analysis**: each flow-down clause with the prime contract clause it claims to derive from, whether that clause appears in the prime's list, whether it is mandatory or elective, how party names substitute in the subcontract, and clauses in the addendum that the prime does not require at all.
- **Export and sanctions position**: the classification with its basis and who determined it, the screening duties the clauses create and which system performs them, end-use and end-user restrictions, re-export and deemed export exposure, and the certifications the agreement asks the organization to make.
- **Sector and AI obligation set**: the obligations passed through by regulated counterparties and by AI terms, each with the role it assigns, the operational commitment it creates, and what the product currently does against it.
- **Accessibility commitment record**: what the agreement commits to, what the current conformance report supports with its date and scope, the gap between them, and the remediation or the carve-out that closes it.
- **Internal obligation map**: every accepted clause converted to an owner, an act, a cadence, a first due date derived from a date the document states, and the evidence of performance, with obligations no owner has accepted recorded as unowned.
- **Source facts and assumptions record**: every clause read with its locator and read date, every classification and conformance fact with its source, every assumption with the clause it affects.

Depth standard per artifact: an entry is complete when the function that inherits the obligation can start performing it and the negotiator can argue the clause. "Accept the export clause" is a disposition with no content. A complete row states that the clause requires screening of every recipient against denied party lists before each delivery, that trade compliance already screens at onboarding but not per delivery, that the gap is a per-shipment check nobody performs today, and that the position is to align the clause to the screening cadence the organization actually runs.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the prime contract, its clause list, or the conformance report cannot be reached, deliver the clause register and the questions in full, and record the flow-down analysis and the conformance comparison as blocked with the missing document named, since a flow-down conclusion without the prime's clause list is a guess about someone else's contract. In `resume` mode, re-read the compliance addendum rather than carrying its summary, because compliance exhibits are the ones counterparties refresh between turns without marking the change.

The failure this desk exists to prevent is a regulatory clause described from memory of the rule instead of from the words on the page. It reads authoritatively, it uses the right acronyms, and it is wrong in the way that costs most: the clause the organization signed is what the counterparty enforces, and a review that summarized the regulation rather than the clause never noticed that the clause demanded more, demanded something else, or demanded it of the wrong party. So a clause number that the prime contract's own list does not contain is recorded as not located rather than reconstructed from the standard clause set, a regulatory requirement is stated as the accepted clause words it with any divergence from the underlying rule recorded next to it, an ECCN or a conformance level appears only with the determination and date behind it, and a clause nobody could open is unread in writing. **The organization is bound by the clause, not by the rule the clause claims to be about.**

## legal_packet fields to update

- `regulatory_terms.export_and_sanctions`: the clauses, the classification and its basis, and the screening obligations they create.
- `regulatory_terms.anti_corruption`: the clauses with their audit, records, and termination rights.
- `regulatory_terms.flow_down_requirements[]`: each flow-down with its prime clause reference, mandatory or elective state, and disposition.
- `regulatory_terms.sector_obligations[]`: obligations passed through, with the regime and the operational commitment.
- `regulatory_terms.accessibility_commitments`: what the text commits to, and the conformance report with its date and scope that supports or fails to support it.
- `regulatory_terms.ai_specific_terms`: model use, training data, output ownership, disclosure, oversight, and the role allocation the text creates.
- `obligations[]`: every accepted clause converted into a row with `clause_ref`, `obligated_party`, `trigger`, `due_or_recurrence`, `owner`, and `evidence_of_performance`.
- `issues[]` and `positions[]`: rejected or negotiated clauses with `operative_effect`, `proposed_change`, `deviation`, and `approver_required`.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Source conflict**: the published requirement and the flow-down clause disagree about what is required, a prime obligation and the organization's standard position cannot both hold, or two regimes in the agreement impose incompatible duties on the same act. Record both readings with locators and route the conflict rather than resolving toward the reading that lets the deal close.
- **Release integrity**: a certification, a conformance level, a classification, or a compliance representation would go to a counterparty, a prime, a regulator, or an auditor without the determination, report, or evidence behind it. A conformance statement in a contract becomes the standard the product is measured against and the basis of a procurement decision.
- **Approval**: accepting an audit right, an inspection right, a certification obligation, a termination trigger for a compliance failure, or a flow-down the prime does not actually mandate commits the organization to a compliance program it does not run. That is a decision at the authority level the delegation of authority sets, and compliance leadership owns it rather than the negotiator.
- **Security or privacy**: reviewing or evidencing the clause would move controlled technology, restricted technical data, personal data, or another customer's regulated content into an artifact or across a border. A deemed export happens on access, so scope the review before anything moves.
- **Production or destructive**: the next act would submit a certification, file a registration, make a disclosure to a regulator, or serve a compliance notice. Prepare the item with what it asserts and stop at the gate.
- **Connector unreachable**: the prime contract, its clause list, the classification determination, the conformance report, or an addendum incorporated by reference cannot be read, so the analysis would describe obligations whose source text is unread.

## Downstream handoffs

`redline-negotiation-desk` consumes the negotiated clauses as issues with proposed language and the fallback the organization would accept, and needs the reason a flow-down is refusable, which is usually that the prime never required it. `approval-escalation-desk` consumes accepted clauses that create compliance programs the organization does not run today, with the aggregate load rather than a clause list, since the combined burden is what the approver is actually deciding on. `obligation-extraction-desk` consumes the internal obligation map as register rows once the agreement is executed. `signature-execution-desk` consumes any certification the signatory is being asked to make, since a compliance certification signed alongside the agreement carries its own liability. The GRC suite consumes accepted obligations for control mapping, testing, and evidence, and needs the clause reference and window rather than a description. The Security suite consumes incident reporting windows and technical commitments that land on operations.

## Quality bar

Good flow-down work reads like someone opened both contracts. Every clause carries a reference. Every flow-down is traced to the prime's list or marked as absent from it, and the absent ones are named out loud, because that is where the negotiator gets ground back without arguing about compliance. The export section separates what was classified from what was assumed. The accessibility section says what the report actually covers, including the pages, the platforms, and the date, rather than a level. The AI section states the role the clause assigns and what changes if that role is wrong. And the map at the end names people, not departments: a compliance obligation assigned to "Legal" is unowned, and the first evidence of that is a counterparty audit request that arrives with a deadline attached and no one who knows what the answer is supposed to be.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
