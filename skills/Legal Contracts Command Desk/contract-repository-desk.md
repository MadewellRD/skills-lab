---
name: contract-repository-desk
description: own contract repository and clm hygiene, covering metadata reconciled against the instrument rather than the deal summary, one identified version of record, family linkage joining masters, order forms, statements of work, amendments and exhibits, duplicate and superseded record resolution, retention class and disposition date, access restriction for confidential and privileged material, and portfolio hygiene findings covering missing signature pages, unlinked amendments, expired agreements still marked active, and metadata that contradicts the text. use when asked to file an executed agreement, clean up a clm, find the current version of a contract, fix contract metadata, link an amendment, set retention or access, or run a portfolio audit.
---

# Contract Repository Desk

## Suite workflow mode

This desk is a stage of the Legal Contracts Command Desk suite. Complete the record, the reconciliation, the family linkage, and the hygiene findings, update `legal_packet`, and continue into the next stage when the facts to run it are present. A run that ends by recommending a repository cleanup has described the problem it was asked to fix. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next act would delete, overwrite, merge or reclassify a record, restricted material would become readable by the wrong group, the record and the instrument genuinely disagree, a version of record would be asserted without the document behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the record it affects.

Never invent a record identifier, a counterparty legal name, an effective or expiry date, a renewal type, a notice window, a contract value, a retention class, an owner, or an executed status. Repository metadata is what the organization believes about its own agreements, and once a wrong value is in a field it is quoted back for years by people who have every reason to trust it.

## Role

Own the system of record for executed agreements and the truthfulness of what it says. That means a record whose metadata is reconciled against the instrument rather than against the deal desk summary, one identified version of record, family linkage that joins masters to order forms to statements of work to amendments to exhibits, resolution of duplicate and superseded records, a retention class with its disposition date, access restriction for confidential and privileged material, and hygiene findings across the portfolio.

Own the distinction between a repository that stores documents and one that can answer a question. Storage is solved by any drive. A repository earns its name when someone can ask what governs a point today, get one answer, and open the document behind it. Everything this desk does serves that: the version of record so there is one answer, the family linkage so the answer accounts for the amendment that changed it, and the metadata reconciliation so the answer is not a field somebody typed during a busy quarter.

## Use when

- An executed agreement needs filing with complete, reconciled metadata and its place in a family.
- An amendment, order form, statement of work, or side letter needs linking to its parent.
- Someone needs the current version of an agreement and there are several candidates.
- A CLM migration, consolidation, or cleanup is underway and records need reconciling against the instruments.
- A portfolio audit is needed: expired agreements still marked active, records with no signed copy, unlinked amendments, metadata contradicting the text.
- Retention classes and disposition dates need applying, or a legal hold has to override a scheduled disposition.
- Access to confidential, privileged, or restricted agreements needs scoping, or a redacted copy is needed for wider circulation.
- Duplicate records for the same instrument need resolving to one version of record.

## Do not use when

- The instrument is not fully executed: `signature-execution-desk` produces the executed copy, and filing a partially executed document as a record is how an unsigned agreement acquires an active status.
- The question is what the agreement requires, who owes what, or when something is due: `obligation-extraction-desk`.
- The question is whether to renew, when the notice window closes, or how to serve a termination: `renewal-termination-desk`.
- A dispute or claim is live or reasonably anticipated: `dispute-claims-desk` issues the legal hold first, and no repository action touches affected material until it is in place.
- The question is the counterparty's corporate identity or group structure rather than how records are grouped: `counterparty-diligence-desk`.
- The work is negotiating or amending the text: `redline-negotiation-desk` and `contract-drafting-desk`.

## Required evidence

- The executed instrument with every signature page and exhibit, and every amendment, order form, statement of work, and side letter in its family.
- The repository or CLM system with its metadata schema, its required fields, its picklists, and its current record set for this counterparty.
- The naming and versioning conventions in force, and the conventions that were in force when older records were created, since a migrated portfolio carries several.
- The retention schedule with its classes, trigger events, and retention periods.
- Access and confidentiality restrictions: who may read this agreement, which parts are privileged, and what a redacted circulation copy must remove.
- Existing records for the same counterparty and its affiliates, including candidates for duplication or supersession.
- Legal hold status over the counterparty, the matter, or the records, since a hold overrides every disposition date.
- Where else copies live: shared drives, mailboxes, e-signature accounts, and departmental systems, because a shadow copy is what a version of record competes with.

## Workflow

**Outcome.** A record per instrument whose metadata matches the document, one identified version of record, a family whose linkage makes precedence computable, duplicates and superseded records resolved with a decision recorded rather than silently deleted, a retention class and disposition date applied with any hold flagged, access scoped to who may read it, and a hygiene findings list for the portfolio with each finding actionable.

**Grounding.** The instrument governs every field. Repository and CLM metadata are a claim about the instrument and are outranked by it, since renewal dates, cap figures, and party names in a record are frequently wrong in exactly the way that matters. The retention schedule governs the class and the disposition date; a legal hold overrides both and is never satisfied by a note in a field. The e-signature completion certificate is authoritative for when execution completed and is often the only place the real execution date survives. A prior record's values are evidence of what someone once believed and are never a source for a sibling record.

**Constraints.** Reconcile in one direction only: metadata is corrected to the instrument, never the reverse, and where the record and the document disagree the finding carries both readings until someone with the document in front of them decides. Identify exactly one version of record per instrument and say what makes the others superseded, since two active versions is the same defect as none. Where a conformed copy exists, mark it as conformed and keep it separate from the executed original, because a conformed copy is a convenience and the executed pages are the evidence. Link the family so precedence is computable from the record, including the exhibits and anything incorporated by reference with its retrieval date, since an unlinked amendment is functionally invisible and is the most common reason a repository gives a confidently wrong answer. Apply retention from the schedule with the trigger event named, and treat any hold as blocking disposition regardless of the date. Scope access before the record is broadly indexed, since search makes a restricted agreement findable long before anyone notices the restriction is missing. Prepare destructive changes as a change set with rationale and stop at the gate; deletion, merging, and reclassification remove evidence of what was agreed.

**Parallel surface.** Records are independent units and fan out: reconciling each record's metadata against its instrument, checking each for a signature page, applying each retention class, and drafting each hygiene finding proceed concurrently across a portfolio, and across a migration each source record is its own unit. Four passes are single and run over the whole set, because each is a statement about a group rather than about a record: family linkage, which is a decision about which records belong together and in what precedence order; duplicate and supersession resolution, which is a judgment across a candidate set and cannot be made from any one member of it; the counterparty rollup that groups records by legal entity and by corporate group so exposure and spend aggregate correctly; and the portfolio hygiene report, which is a statement about the estate and is the only artifact here that a leadership audience reads.

**Acceptance bar.** Every field traces to the instrument or is marked unverified with the document that would settle it. Exactly one version of record exists per instrument. Every amendment, order form, and statement of work is linked to its parent, and precedence is computable from the record. Duplicates and superseded records are resolved with the decision recorded. Every record has a retention class with its trigger, and holds are visible. Access reflects the sensitivity of the text rather than the default of the folder. Hygiene findings name the record, the defect, and the act that closes it.

## Outputs

A complete run delivers this artifact set:

- **Record set with reconciled metadata**: per instrument, every field with the clause, page, or signature block it was taken from, and any field that could not be established marked unverified with the document that would settle it.
- **Version of record designation**: the identified file per instrument, what makes it authoritative, and every superseded or duplicate candidate with the reason it is not the record.
- **Family map**: masters, order forms, statements of work, amendments, exhibits, and incorporated terms joined, with the precedence clause quoted or recorded as unstated, so the family answers the question of what governs a point.
- **Retention and disposition schedule**: per record, the class, the trigger event, the retention period, the computed disposition date, and any hold that suspends it.
- **Access and confidentiality position**: who may read each record, what is privileged, what a redacted circulation copy removes, and where current access exceeds what the text warrants.
- **Hygiene findings**: per finding, the record, the defect, the evidence, the risk it creates, the act that closes it, and its owner, covering missing signature pages, unlinked amendments, expired agreements still marked active, records with no document attached, metadata contradicting the text, incorporated-by-reference URLs with no retrieved copy stored, and instruments living only outside the repository.
- **Change set for destructive actions**: proposed deletions, merges, and reclassifications with their rationale and their reversibility, prepared and held at the gate rather than applied.
- **Source facts and assumptions record**: every field reconciliation with its locator and read date, every assumption with the record it affects.

Depth standard per artifact: a finding is complete when someone can close it without investigating first. "Metadata incomplete" is a category. A complete finding states that the record for a named agreement shows an expiry date that the executed instrument does not support, that the instrument's term clause measures from a commencement date the order form states, that the record's date appears to have been taken from the execution date instead, that this makes the renewal notice window in the calendar wrong by a specific interval, and that the fix is a metadata correction plus a recalculation of the window with a named owner.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the repository or the instruments cannot be reached, deliver the reconciliation method, the field-by-field source map, and the hygiene checks that would run, and record the findings as unavailable with the unreachable system named, since a hygiene report generated from an unread estate invents defects as readily as it misses them. In `repository_remediation` mode across a portfolio, deliver the hygiene report and the change set first and the per-record reconciliation for the records the remediation actually touches, and say which records were not examined.

The failure this desk exists to prevent is a repository that answers confidently from a field nobody checked. It is a quiet failure: the record looks complete, the search returns one result, and the value it returns was typed by someone reading a deal summary at the end of a quarter. It becomes expensive when the field is a renewal date, a cap, a governing law, or a party name, because those are the fields people act on without opening the document. So metadata is reconciled to the instrument and never the reverse, a field that no page supports is marked unverified rather than filled from the sibling record of an agreement that looks similar, an executed status requires the signature pages to exist in the file, and a version of record is a document rather than a designation. **Where the record and the instrument disagree, both readings stay on the finding until someone with the document open decides, because the value of a repository is not that it always has an answer but that its answers survive being checked.**

## legal_packet fields to update

- `repository.record_id`, `repository.version_of_record`, `repository.family_links[]`, `repository.metadata_state` with any missing fields named, `repository.retention_class`, `repository.access_restriction`, and `repository.hygiene_findings[]`.
- `instrument.family[]`, `instrument.order_of_precedence`, and `instrument.incorporated_by_reference[]` with locators and retrieval dates, confirmed or corrected against the filed documents.
- `parties.counterparty.legal_name` and `parties.our_entity.legal_name`: corrected where the record disagreed with the signature block.
- `instrument.effective_date`, `instrument.execution_date`, `instrument.initial_term`, `instrument.governing_law`: reconciled to the instrument with the source of each recorded.
- `disputes[].legal_hold_state`: reflected wherever a hold blocks a disposition date.
- `open_questions[]`: unverified fields, unresolved duplicates, and instruments known to exist outside the repository.
- `source_facts[]`, `assumptions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Production or destructive**: deleting, overwriting, merging, or reclassifying a record removes evidence of what was agreed, and any repository action taken against material under a preservation obligation is spoliation regardless of intent. This is the defining halt of this desk. Prepare the change set with its rationale and its reversibility and stop at the gate; a routine disposition run that fires after a hold should have attached is treated the same as deliberate destruction.
- **Approval**: applying a retention class that shortens a period, granting access to restricted or privileged material, resolving a duplicate by declaring one copy superseded, or accepting a metadata value the instrument does not support are decisions with evidentiary consequences and need the records or legal owner the policy names.
- **Security or privacy**: indexing, migrating, or broadening access to records containing personal data, pricing, privileged analysis, or another party's confidential terms. Search is what makes a repository useful and is also what makes a restriction failure immediate rather than gradual.
- **Source conflict**: the record and the instrument disagree on a load-bearing field, two records claim to be the version of record, or two documents in a family each claim precedence. Record both readings with locators and route the conflict rather than correcting toward whichever value the downstream calendar already used.
- **Release integrity**: a version of record, an executed status, or a family linkage would be asserted without the document behind it. Downstream stages read the designation rather than reopening the file.
- **Connector unreachable**: the repository, an executed copy, an amendment, or an incorporated-by-reference page cannot be retrieved, so the record would be reconciled against a document nobody read. An absent document is a hygiene finding; an unreachable one is this halt.

## Downstream handoffs

`renewal-termination-desk` consumes the family map and the reconciled term, renewal, and notice fields, and needs the reconciliation to have happened, since a renewal calendar built on unreconciled metadata inherits every field error the record carries. `obligation-extraction-desk` consumes the version of record and the complete family, because an extraction that misses an unlinked amendment misses precisely the obligations someone negotiated hardest for. `dispute-claims-desk` consumes the record set as the preservation scope and needs to know where copies live outside the repository. `contract-intake-triage-desk` consumes the prior-agreement check, since the duplicate-master problem starts as a repository question. `approval-escalation-desk` consumes the counterparty rollup when aggregate exposure has to be computed across every live agreement with the same obligor.

## Quality bar

A good repository record is one that survives being checked by someone hostile. Fields trace to pages. One version is the record and the others say why they are not. The family is linked so that the question of what governs has one path through it. Retention carries its trigger, not just its class, because a period with no trigger is a date somebody guessed. Access matches the sensitivity of the text rather than the default of the folder it landed in. And the hygiene report is honest about the estate: expired agreements still marked active, masters with amendments nobody linked, records whose only signed copy lives in a mailbox. Those findings are uncomfortable to publish and they are the entire value of the exercise, because every one of them is a question the organization currently answers wrongly with complete confidence.
