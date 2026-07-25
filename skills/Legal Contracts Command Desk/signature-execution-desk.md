---
name: signature-execution-desk
description: prepare and run contract execution by fixing the execution version so the text signed is the text approved, building signature blocks that carry exact legal entity names, naming signatories with the resolution, power of attorney or delegation that authorizes them, handling counterparts and electronic execution as the agreement and the governing law permit, setting the signing sequence, determining the effective date separately from the execution date, and producing the fully executed copy with every exhibit attached and its distribution. use when asked to prepare a signature package, check signing authority, set up an e-signature envelope, confirm counterparts or wet ink requirements, fix an effective date, or confirm whether an agreement is fully executed.
---

# Signature Execution Desk

## Suite workflow mode

This desk is a stage of the Legal Contracts Command Desk suite. Complete the execution package, the authority record, the signing plan, and the executed copy handling, update `legal_packet`, and continue into the next stage when the instrument is executed and distributed. A run that ends by suggesting the document is ready for signature has stopped one step before the only step that binds anyone. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next act would bind the organization, confidential material would go to the wrong recipients, documents genuinely disagree on the text being signed, an execution status would be asserted without the signed page behind it, or a required document is unreachable. Every other gap proceeds with the assumption labeled inline against the execution item it affects.

Never invent a legal entity name, an entity suffix, a jurisdiction of formation, a signatory, a title, an authority basis, a signature date, an effective date, a counterpart permission, or an executed status. Every one of these is checkable by someone who will check it, and the moment they are checked is usually the moment the organization needs the agreement to be enforceable.

## Role

Own the last reversible moment. That means fixing the execution version so the text that goes out for signature is provably the text that was approved, building signature blocks that carry the exact registered names of the contracting entities, establishing that each signatory actually holds the authority to bind their party, handling counterparts and electronic execution as the agreement and the governing law permit, sequencing the signing where an order is required, determining the effective date as a separate question from the execution date, and producing a fully executed copy with every exhibit attached and distributed to the people who need it.

Own the difference between signed and fully executed. Signed means one party's page exists. Fully executed means every party has signed, every exhibit and schedule referenced in the document is attached, and the organization holds the complete instrument. A great deal of downstream work, from obligation extraction to revenue recognition to a dispute two years later, rests on that distinction, and it is routinely blurred by a status field set the moment the envelope was sent.

## Use when

- A negotiated agreement has all its approvals and needs preparing for signature.
- Signature blocks need building or correcting, or an entity name in a block does not match the registry.
- Signing authority needs establishing on either side: whose resolution, delegation, or power of attorney authorizes this person to sign this instrument.
- The execution method needs deciding: electronic, wet ink, counterparts, notarization, witnessing, or a form the governing law or the document itself requires.
- A signing sequence is needed because one party must sign first, or because a guarantee, a consent, or a parent countersignature has to land in a particular order.
- The effective date needs determining, especially where it differs from the execution date or depends on a condition.
- An agreement is believed to be executed and the executed copy, its exhibits, or a countersignature cannot be located.
- An executed copy needs distributing to the business owner, finance, the repository, and the counterparty.

## Do not use when

- Deviations remain unapproved or approval conditions are unclosed: `approval-escalation-desk` closes the gate, and sending an unapproved text for signature is the failure this stage exists to prevent.
- The text is still moving: `redline-negotiation-desk` settles the words before a version can be fixed.
- The counterparty entity has not been verified or screened: `counterparty-diligence-desk` establishes who is actually being contracted with.
- The instrument is executed and its obligations need extracting: `obligation-extraction-desk`.
- The executed copy needs filing, metadata, family linkage, and retention: `contract-repository-desk`.
- An executed agreement contains an error and someone wants the file corrected: an executed instrument is not edited, and the correction is an amendment or a side letter drafted by `contract-drafting-desk`.

## Required evidence

- The final negotiated text with every approval recorded and every approval condition closed.
- The verified legal names, jurisdictions of formation, entity types, and registration numbers for both contracting parties, from the registry rather than from the brand or the email footer.
- The authority basis for each signatory: the board resolution, secretary's certificate, power of attorney, or delegation of authority provision, with its scope and any monetary limit.
- The document's own execution provisions: the counterparts clause, the electronic signature clause, any requirement for a witness, a seal, notarization, or a specified form.
- The governing law's constraints on execution form, including the categories of instrument that cannot be executed electronically in that jurisdiction.
- The complete exhibit, schedule, and annex set as it will be attached, with any document incorporated by reference identified at its version.
- The effective date requirements: what the agreement says makes it effective, and any condition precedent that has to be satisfied first.
- The distribution list: business owner, finance and billing, the repository, the counterparty's named contact, and anyone the agreement itself requires to receive a copy.

## Workflow

**Outcome.** An executed instrument that is provably the approved text, signed by people who hold the authority to bind their parties, in a form the agreement and the governing law permit, with every exhibit attached, an effective date established from the document rather than assumed, and a complete copy in the hands of everyone who needs it.

Execution follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Confirm every approval is recorded and every approval condition is closed.
2. Verify the contracting entities and both signatories' authority.
3. Fix the execution version with every exhibit attached, and record its file identity.
4. Route for signature in the sequence the transaction requires.
5. Obtain the countersigned copy with its completion certificate or its wet ink pages.
6. Determine the effective date from the executed instrument.
7. Record and distribute.

The order is mandated because execution is the last irreversible step in the chain and nothing after it can be undone by editing a file. An agreement signed against the wrong entity or by someone without authority is not repaired by an amendment; it needs re-execution or ratification by a counterparty who has already obtained what they wanted and has no remaining reason to cooperate. Fixing the version before routing is what makes the claim that the signed text is the approved text checkable rather than asserted.

**Grounding.** The registry governs the legal name and entity type. The signature block governs how that name appears in the instrument, and where the two differ the difference is resolved before signing rather than after. The document's own execution provisions govern counterparts and form, read together with the governing law, which can prohibit what the clause permits. The authority instrument governs whether a signatory may bind their party, including its monetary and subject-matter limits, since a delegation that covers agreements below a threshold does not cover this one merely because the same person signed the last five. The executed pages and the completion certificate govern when signing actually happened.

**Constraints.** Fix the execution version by an identifier that cannot drift, and treat any change after that point as producing a new version requiring the approval trail to be revisited. Carry the exact registered name with its entity suffix and its formation jurisdiction into the block, since a parent and its subsidiary are different obligors with different balance sheets and the wrong one is enforceable against nobody worth suing. Keep the four dates apart, because the effective date, the execution date, the commencement date, and the date a term or notice window is measured from are four different things and are frequently four different values. Determine the effective date from what the document says makes it effective rather than from the date on a signature line. Never backdate an effective date; where the parties intend earlier commercial effect, that is drafted as an agreed commencement with effect from a stated date, and the document still records when it was actually signed. Attach exhibits at signature rather than promising them, since a referenced schedule that is not attached is the most common defect in an otherwise clean executed file. Where a wet ink, witnessed, notarized, or specific-form requirement applies, follow it exactly, since these requirements are formality rules and a defect in form can make the instrument unenforceable rather than merely untidy.

**Parallel surface.** Preparation items are independent and fan out: building each party's signature block, verifying each signatory's authority instrument, checking each exhibit against the document's references, and preparing each distribution package proceed concurrently, and across a batch of order forms or renewals under one master, each instrument's preparation is its own unit. Three things are single and sequential by nature rather than by convention. The signing sequence itself is ordered wherever a guarantee, a consent, a parent countersignature, or a condition precedent requires one party to sign first. The version fix is a single act over the whole document set, since the point of it is that one identifiable artifact went out. And the effective date determination is a statement about the executed instrument as a whole, made once the last signature exists.

**Acceptance bar.** The version sent for signature is identified and matches the approved text. Both entity names match the registry with their suffixes and jurisdictions. Both signatories have a named authority basis with its scope. The execution form satisfies the agreement and the governing law. Every referenced exhibit is attached. The effective date is stated with the provision that produces it. The fully executed copy is complete and located, or the status reads `not_yet_executed` with what is outstanding named.

## Outputs

A complete run delivers this artifact set:

- **Execution version record**: the exact file going out for signature with its identifier, the approval trail it corresponds to, and the exhibit and schedule inventory it contains.
- **Signature blocks**: prepared for each party with the exact registered name, entity type and jurisdiction, the signatory's name and title as it will appear, and the date field, matching how the document and the registry render the name.
- **Authority record**: per signatory, the instrument that authorizes them, its scope and any limit, its date, and whether this transaction sits inside that scope.
- **Execution method determination**: electronic or wet ink, counterparts permitted or not with the clause quoted, any witnessing, notarization, or form requirement, and the governing law constraint that drove the answer.
- **Signing plan**: the routing order with the reason where an order is required, the recipients and their roles in the envelope, the reminder and expiry handling, and the conditions that must be satisfied before signature is requested.
- **Effective date determination**: the date, the provision that produces it, any condition precedent, and how it relates to the execution date and to the commencement date.
- **Fully executed instrument package**: the complete signed document with every page, every signature page, every exhibit, and the completion certificate or audit trail where execution was electronic.
- **Distribution record**: who received the executed copy, when, in what form, and any redacted version prepared for wider internal circulation.
- **Source facts and assumptions record**: the registry extract, the authority instrument, and the execution clause each with its locator and read date, every assumption with the execution item it affects.

Depth standard per artifact: an item is complete when the signing can proceed without a further question and the file would satisfy someone auditing enforceability. "Signed by the VP of Sales" is a name. A complete authority record states the person, the title, the delegation provision that authorizes signature of agreements of this type, the monetary limit in that provision, the deal value against that limit, and the resulting conclusion that the signature is within scope or that a higher signatory is required.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the registry, the authority instrument, or an exhibit cannot be reached, deliver the execution version record, the signing plan, and the method determination, and record the authority and entity verification as blocked with the missing source named, since an execution package assembled around an unverified entity is the defect this stage exists to catch. In `resume` mode, where the matter returns after a delay, re-confirm that the approvals still attach to the current text and that no signatory has changed role, because both go stale quietly.

The failure this desk exists to prevent is an execution status asserted ahead of the paper. It happens because the envelope was sent, because a counterparty said the countersignature was coming, or because a system field flipped when the last internal signer finished. Everything downstream then treats the agreement as in force: obligations get extracted, revenue gets recognized, services get turned on, and the missing page is discovered when someone needs to enforce a term. So a fully executed copy is a file carrying every party's signature page and every exhibit; a countersignature someone said was on its way is `not_yet_executed` with the outstanding party named; the execution date is the date the last party actually signed, read from the page or the completion certificate rather than from the date the envelope went out; and an entity name that no registry extract or signature block supports is recorded as unverified rather than rendered from the brand. **An agreement is enforceable against the entity in the block, signed by a person with the authority to bind it, in the form the law requires, and each of those three is a separate way to hold nothing at all.**

## legal_packet fields to update

- `execution.execution_version_ref`: the fixed file identity that went out for signature.
- `execution.signature_method`, `execution.counterparts`: as the clause and the governing law permit, quoted.
- `execution.signatories[]`: `party`, `name`, `title`, and `authority_basis` with its scope and limit.
- `execution.fully_executed_copy`: the locator of the complete signed instrument, or `not_yet_executed` with what is outstanding.
- `execution.effective_date_trigger`: what makes the agreement effective, quoted from the text.
- `instrument.effective_date` and `instrument.execution_date`: kept as separate values, each from its own source.
- `instrument.family[]`: updated where this instrument joins an existing family, so precedence stays computable.
- `parties.our_entity` and `parties.counterparty`: legal names, jurisdictions, and `verification_source` confirmed against the block that was actually signed.
- `approvals[]`: state confirmed at the moment of release, with any approval found stale against the executed text flagged.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Production or destructive**: execution binds the organization and is not unwound by editing the file afterward. Sending for signature is the last reversible moment, so an unapproved deviation, an unclosed approval condition, an unverified entity, an unauthorized signatory, a missing exhibit, or a version that does not match the approved text stops here rather than after countersignature. This is the defining halt of this desk.
- **Approval**: an approval is missing, a condition attached to a conditional approval is unclosed, or the text moved after approval in a way that touches an approved item. Signature is the act the approval authorizes, so a stale approval is no approval at the moment it matters.
- **Release integrity**: an executed status, an effective date, or a countersignature would be recorded without the page behind it. Everything downstream inherits this status, and the error surfaces when someone tries to enforce.
- **Source conflict**: the clean copy and the version sent for signature differ, the counterparty returns a signed copy whose text does not match what was sent, the entity in the block and the registry disagree, or two dates in the executed document contradict each other. A counterparty-returned copy with altered text is signed by them and not agreed by us, and it is resolved before any status is recorded.
- **Security or privacy**: the envelope, the distribution list, or the executed copy would go to recipients outside the group entitled to see unredacted commercial terms, personal data, or another party's confidential information. Signature envelopes circulate by design, and a wrong recipient sees everything.
- **Connector unreachable**: the registry, the authority instrument, an exhibit, or the executed copy itself cannot be retrieved, so entity, authority, completeness, or execution status would be asserted from an unread source.

## Downstream handoffs

`obligation-extraction-desk` consumes the fully executed instrument with every exhibit and the effective date, and cannot start from a partially executed file, because an obligation calendar built from a document whose exhibits are missing is missing exactly the deliverable schedules that carry the deadlines. `contract-repository-desk` consumes the executed copy, the version of record designation, the family linkage, and the metadata reconciled to the instrument rather than to the deal desk summary. `renewal-termination-desk` consumes the effective date and the term, since every renewal window is computed from a date this stage established. The finance and revenue functions consume the executed copy and the effective date for billing and recognition, which is why the distribution record names them explicitly. `contract-drafting-desk` receives any post-execution correction as an amendment or a side letter, since the executed instrument is not edited.

## Quality bar

Good execution work is invisible when it is right and expensive when it is not. Entity names carry their suffix and their jurisdiction and match a registry extract someone actually pulled. Signatories are named with the instrument that authorizes them and the limit in that instrument, so nobody has to reason from seniority. The counterparts and electronic execution position is quoted from the clause rather than assumed from habit, because the assumption fails precisely on the instruments where formality matters. Exhibits are attached rather than referenced. The effective date has a provision behind it. And the file that ends up in the repository is complete: every page, every signature, every schedule, and the completion certificate, so that when someone opens it in three years to answer a question under pressure, the answer is in the file rather than in someone's recollection of how the deal was done.
