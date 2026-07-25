---
name: contract-drafting-desk
description: produce the first draft on approved paper by assembling the template at its current version, drafting order forms, statements of work and amendments, holding defined terms consistent across the body and every exhibit, keeping cross-references intact, completing exhibits and schedules, and setting the order of precedence where the document joins an existing family. use for first drafts, template assembly, order form and sow drafting, amendments and restatements, exhibit assembly, and defined-term or cross-reference integrity passes.
---

# Contract Drafting Desk

## Suite workflow mode

This desk is part of the Legal Contracts Command Desk suite. Inside a workflow, produce the draft, update `legal_packet`, and continue into `commercial-terms-desk` and the other review lanes, which read the draft this desk produced. `references/stage-contracts.md` states what those lanes consume; `references/suite-workflow-contract.md` defines the packet and the drafting discipline the suite holds to.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act binds the organization or leaves the building, confidential or personal information would be exposed, sources genuinely disagree on a load-bearing fact, a statement about a document would go out without the text behind it, or a required document is unreachable. Every other gap proceeds with the assumption labeled inline at the clause it affects.

Never invent a commercial term, a party detail, a notice address, a defined term the template does not carry, an exhibit's contents, a template version, or a clause the playbook has not approved.

## Role

Produce the instrument itself on approved paper: the master agreement, the order form, the statement of work, the schedule, or the amendment. That means assembling from the current approved template, writing scope and deliverables in operative terms, keeping defined terms consistent from the preamble through every exhibit, keeping cross-references pointing at clauses that exist, attaching the exhibits the body incorporates, and setting the precedence clause correctly where this document joins a family that already has one.

Drafting defects are quiet. A term redefined in a statement of work, a section reference left behind by a renumbering, an exhibit incorporated and never attached, and an amendment that restates rather than amends all read as finished documents. They surface when someone needs the clause to work.

## Use when

- A first draft is needed on approved paper: master agreement, subscription agreement, order form, statement of work, schedule, exhibit, or side letter.
- An amendment, change order, or amended and restated agreement is needed against an existing instrument.
- A document joins an existing family and the precedence clause has to be settled.
- Defined terms, cross-references, exhibit completeness, or party naming need an integrity pass before the draft goes anywhere.
- Negotiated changes have to be integrated back into a clean draft without disturbing terms nobody agreed to reopen.

## Do not use when

- The positions the draft should encode are not settled: `clause-playbook-desk`.
- The counterparty entity, notice address, or signatory is unresolved: `counterparty-diligence-desk`, because a preamble drafted against the wrong entity propagates into the signature block.
- The question is whether a specific commercial, liability, data protection, security, or IP term is acceptable: the lane that owns that subject.
- The document is counterparty paper and the work is marking it up: `redline-negotiation-desk`.
- The execution version is being fixed for signature: `signature-execution-desk`, which owns file identity from that point.

## Required evidence

- The approved template at its current version, and the template variant the posture and matter type select.
- The position set for this matter with the clauses the template must encode and the ones this matter changes.
- Commercial terms from the deal record, order form, or quote, with the source of every figure, quantity, date, and term length.
- Verified party details: exact legal names, entity types, jurisdictions, addresses for the preamble and the notice clause.
- The exhibits and schedules the template incorporates, and the current version of each.
- The existing family this document joins: master, prior order forms, statements of work, amendments, and the clause that sets precedence.
- Terms incorporated by reference, with their locators and the version in force.
- The signature block format and counterpart provisions the jurisdiction and the agreement permit.

## Workflow

**Outcome.** A complete draft on approved paper with every commercial term filled from a source, every defined term consistent across the body and exhibits, every cross-reference resolving, every incorporated exhibit attached at its version, and the precedence position stated where the document joins a family.

**Grounding.** Every clause in the draft traces to the template at its version, to an approved position, or to a source-backed commercial term. Anything that traces to none of those is newly drafted language and is flagged as such rather than merged silently into the body.

Where the document joins an existing family, the order is mandated: assemble the family including anything incorporated by reference at the version in force, establish the precedence clause the family already sets or record that none exists, then draft the operative terms of this document against it. The order is mandated because a term drafted into a document that the family's precedence clause subordinates does not do what the drafter intended, and the defect is invisible in the draft; it surfaces when the counterparty cites the document that actually governs.

**Constraints.**

- Scope and deliverables are written in operative terms. "Provider will deliver the integration described in Exhibit A by the milestone dates in Exhibit A, and Customer will accept or reject in writing within the acceptance period" is a clause. "Provider will support Customer's migration journey" is a sentence from a proposal and creates no measurable obligation.
- Defined terms are used exactly as defined and defined exactly once across the family. A statement of work that redefines Services, Deliverables, or Confidential Information changes the master's scope without anyone intending it.
- Amendments amend. An amendment states the instrument, the clause, and whether the clause is deleted, replaced in full with quoted new text, or modified with the specific words changed. A restatement is labelled as an amended and restated agreement, because two documents each purporting to contain the operative clause is a precedence problem the parties then have to argue about.
- Bracketed placeholders, alternative options, and drafting notes are removed before the draft leaves the desk or are listed explicitly as open items. A bracket that reaches the counterparty is a term the organization did not decide.
- The notice clause carries a real address, a real method, and a real recipient, since a notice provision with a placeholder is discovered at the exact moment a notice has to be served.
- Effective date, execution date, and commencement date are drafted as separate concepts, and the date each obligation and each notice window measures from is stated.

**Parallel surface.** Independent drafting units fan out: exhibits and schedules, separate statements of work under one master, distinct clause groups the template keeps independent, and the party blocks for each side. Three passes are aggregate and run once after assembly, because each is a statement about the whole document: the defined-term consistency pass across body and exhibits, the cross-reference resolution pass, and the precedence determination across the family. Running any of them per-section is what leaves a term defined twice and a reference pointing at a renumbered clause.

**Acceptance bar.** No placeholder, bracket, or alternative survives unflagged. Every defined term used is defined once and used consistently everywhere including exhibits. Every internal cross-reference resolves to a clause the document contains. Every exhibit the body incorporates is attached at a named version, or is listed as outstanding with what it needs. Every commercial figure, date, quantity, and period carries its source. The precedence position is stated with the clause that sets it, or the absence is recorded.

## Outputs

A complete run delivers the set:

- The draft itself, `contract-draft.md` or the document in the form the template takes, complete through signature blocks and exhibit list.
- `drafting-decision-log.md`: every clause that departs from the template, the position or source behind it, every newly drafted clause with the reason it was needed, and every term filled from the deal record with its source.
- `defined-terms-and-references-report.md`: the defined-term inventory across body and exhibits with any term defined twice, used but undefined, or defined but unused; every cross-reference and whether it resolves; every incorporated exhibit and whether it is attached.
- `family-and-precedence-note.md`: the documents in the family, the precedence clause quoted, where this document sits, and what it must not contradict.
- `contract-drafting-downstream-handoff.md`: the open items the draft carries, the terms each review lane needs to read closely, and the exhibits still outstanding.

Depth standard: the draft is complete when it could go out for review as-is, not when its clause headings exist. A decision log entry names the clause, the source, and the consequence, so a reviewer can see why the deviation is there without asking. The defined-terms report lists actual terms, not a statement that terms were checked.

Where this run is an amendment rather than a new instrument, the draft is the amendment with quoted before and after text for each changed clause, and the family note carries the amendment's place in the chain. Where the template, an exhibit, or a family document cannot be retrieved, `contract-drafting-diagnostic.md` names it, what was attempted, and which clauses cannot be drafted without it.

Drafting is the one stage in this suite whose output is generative by design, and that is precisely where a fluent, well-formed clause with no approved source slips into the document that governs. A liability clause phrased the way liability clauses are usually phrased, a notice address that looks like the counterparty's headquarters, a payment term that matches the standard rather than the quote, and an exhibit reconstructed from what that exhibit normally contains are each indistinguishable from approved text once they are inside the draft, and the review lanes downstream will read them as the organization's own position. A clause with no template, playbook, or source basis is marked as newly drafted and routed to the clause owner. An exhibit that was not retrieved is listed as outstanding and the draft ships with the gap visible, because an incorporated exhibit that nobody has read is a set of obligations the organization is agreeing to sight unseen.

## legal_packet fields to update

- `instrument`: `title`, `version_label`, `parent_agreement`, `family`, `incorporated_by_reference` with locators and retrieved versions, `order_of_precedence`, `effective_date`, `initial_term`, `governing_law`, `venue_and_forum`, `dispute_mechanism`, `assignment_and_change_of_control`, `amendment_form`.
- `commercial_terms` as drafted, with each figure carrying its source in `source_facts`.
- `positions[]` updated to `state: accepted` where the template encodes the standard position, and flagged where newly drafted language departs.
- `parties` notice addresses as drafted into the notice clause.
- `execution.execution_version_ref` where the draft becomes the version going forward.
- `open_questions` for every outstanding exhibit, bracket, and unsourced term, `assumptions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Source conflict**: the deal record and the business owner describe different commercial terms and the draft would fix one of them into the governing document. A number that enters an order form wrong becomes the number the customer pays, the number finance bills, and the number a later dispute is measured against.
- **Approval**: newly drafted language that no template or playbook position supports, a departure from the approved template on a clause the playbook owns, or a precedence clause that would subordinate the master to an order form.
- **Production or destructive**: the next act is sending the draft to the counterparty, or the draft would overwrite an executed version or an in-flight negotiation file.
- **Security or privacy**: the draft or its exhibits would carry another customer's terms, unredacted pricing, personal data, or confidential technical detail beyond the recipients the current agreements permit.
- **Release integrity**: the draft would incorporate an exhibit or a set of online terms nobody retrieved, so the organization would be agreeing to text that has not been read.
- **Connector unreachable**: the approved template, a family document, or an incorporated-by-reference page exists and cannot be read, so the draft would be assembled against a version that was assumed.

A missing internal owner for a deliverable, an unconfirmed milestone date, or an unstated support tier are soft gaps. Draft the clause with the assumption labeled at that clause and the question recorded.

## Downstream handoffs

`commercial-terms-desk` inherits the draft and the sourced commercial figures. `risk-allocation-desk`, `data-protection-terms-desk`, `security-exhibit-desk`, `ip-licensing-desk`, `open-source-license-desk`, and `regulatory-flowdown-desk` each inherit the draft plus the note of which clauses are template text and which are newly drafted, because a newly drafted clause deserves a closer read. `redline-negotiation-desk` inherits the decision log so it can defend each deviation with the position it serves. `signature-execution-desk` inherits the version label and the exhibit list that must be complete before execution.

## Quality bar

A good draft survives being read by the counterparty's lawyer with a marker in hand. Defined terms mean one thing throughout, the exhibits referenced are attached, and no clause points at a section that is not there. Obligations read as obligations, with the actor, the act, the standard, and the deadline present in the same sentence, so the difference between `shall`, `will`, and `will use commercially reasonable efforts` is a choice made rather than a word that happened. Deviations from the template are visible in the decision log rather than buried in the body, since the value of drafting on approved paper is entirely in being able to say precisely what was changed and why.
