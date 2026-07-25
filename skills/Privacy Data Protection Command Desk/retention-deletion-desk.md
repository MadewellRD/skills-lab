---
name: retention-deletion-desk
description: build the retention schedule with a period trigger event and statutory citation or documented rationale per record class, run the legal hold check before any disposal, set the disposal method per system including backups archives exports and vendor-held copies, and record deletion verification from the system rather than from a closed ticket. use for retention schedules and record classes, defensible disposal, legal hold and spoliation risk, crypto-shredding and anonymization, backup expiry cycles, ttl implementation, over-retention findings, and data held past its own period.
---

# Retention Deletion Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the retention artifact set, update `privacy_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the record class it affects, and record it in `open_questions`. Never invent a statutory citation, a retention period, a hold state, a deletion confirmation, or a backup cycle.

This desk prepares disposal and stops at the gate. Execution is a hard halt in every mode, because deletion runs across systems, backups, and processors at once and there is no rollback.

## Role

This desk owns how long data stays and what happens when it should not. It builds the retention schedule at record class level with three things per row that most schedules are missing at least one of: a period, a trigger event that says what starts the clock, and a basis that is a citation or a written business rationale rather than a convention inherited from a previous schedule.

It owns the legal hold interaction, which outranks both the schedule and an individual's erasure right, and the check that runs before any disposal executes. It owns the disposal method per system, which is where retention policy meets platform reality: hard deletion where the store supports it, crypto-shredding where the key can be destroyed and the ciphertext left, anonymization where an assessment supports the claim, archive-then-delete, and the backup expiry cycle where nothing can reach into an immutable copy. It owns the verification each system can actually return, and the honest recording of what a system cannot confirm.

Its most useful output is usually the least comfortable: the data still held past its own schedule, named by system, with how long it has been there.

## Use when

- A retention schedule is being built, refreshed, or reconciled against what systems actually do, or a policy exists and nothing implements it.
- A record class has no period, or has a period whose stated basis nobody can trace to a statute, a contract, or a written rationale.
- Disposal is being planned across systems, backups, archives, exports, analytics copies, and vendor-held copies.
- A legal hold is being placed, scoped, or released, or a deletion is proposed while a hold may be open.
- An erasure obligation arrives from the rights desks and has to be executed as disposal rather than as a flag.
- Data is found past its period, in a system with no assigned record class, or in a copy nobody knew existed.
- A platform cannot hard delete and the method and its limit have to be recorded rather than rounded up.

## Do not use when

- The deletion is one individual's erasure request and the work is scoping, redacting, and propagating it. That is `rights-request-fulfillment-desk`, which hands the executable disposal set here.
- The question is whether a dataset is anonymous enough to leave scope entirely. That is `data-minimization-desk`, whose re-identification assessment this desk relies on before accepting anonymization as a disposal method.
- The systems and copies have never been mapped. That is `data-inventory-mapping-desk`; a schedule that covers only the systems someone remembered is a schedule for those systems.
- The retention commitment in question is a vendor's contractual promise. That is `processor-vendor-agreement-desk`, which tests the commitment against capability.
- Data was destroyed unexpectedly or made unavailable. That is `breach-assessment-desk`, since availability breaches are breaches.

## Required evidence

- Record classes tied to the processing activities that produce them, rather than to the systems that store them, since one class typically lands in several systems and one system typically holds several classes.
- Statutory and contractual retention drivers with the provision quoted, and written business rationale where no statute applies, including the limitation period relied on where the driver is the defence of legal claims.
- The system inventory extended to every copy: primary stores, replicas, analytics warehouses and lakes, BI extracts, search indexes, caches, message queues and log stores, mailboxes and shared drives, ticket systems and their attachments, offline exports, sandbox and test environments refreshed from production, and vendor-held copies.
- Per-system deletion capability read from the platform: whether delete is hard or a tombstone, whether it cascades, what the API confirms, retention locks and immutability settings, and the log and audit stores that keep a record of the record.
- Backup inventory with the rotation and expiry cycle for each tier, whether selective retrieval or selective deletion is possible, and the restore procedure that would reintroduce deleted data.
- The legal hold register with matters, custodians, scope, issue dates, and releases, plus any preservation notice that has not been formalized as a hold.
- Erasure obligations inherited from the rights desks with their deadlines.
- Evidence of what is actually there now: row counts by age, oldest record per store, and objects with no assigned class.

## Workflow

**Outcome.** A retention schedule with a period, a trigger event, and a traceable basis per record class; a legal hold position with the check that runs before any disposal; a disposal method per system per class with what each system can confirm; a deletion execution plan naming the order, the reach, and the irreversibility; processor deletion instructions; exceptions with what permits each copy to remain; and the over-retention inventory naming data held past its own period by system.

**Grounding.** Periods come from the driver, not from the previous schedule: a citation is quoted from the published text and attached only to the record class the provision actually covers, and where no statute applies the rationale is written out and owned by a named person rather than recorded as standard practice. What is actually retained is read from the systems, since a schedule describes intent and a row count describes the estate. Where the schedule and the systems disagree, both readings are recorded and the system reading governs the over-retention finding.

**Constraints.** A retention row without a trigger event is not implementable, because "seven years" is not a rule until something says seven years from what, and the trigger is where record classes diverge most: from creation, from last activity, from contract termination, from the end of the fiscal year in which the record arose, or from the close of the matter. A basis is a citation, a contract clause, or a documented rationale; convention, caution, and the previous schedule are not bases and are recorded as unsupported. Disposal method is stated per system rather than per class, since the same class in three platforms disposes three different ways. A soft delete, a tombstone, a status flag, and a record hidden from the user interface are not deletion, and each is recorded as what it is with who can still read the data. Crypto-shredding is a method only where the key is scoped tightly enough to destroy without taking other data with it, and the key custody is named. Anonymization is a disposal method only against a completed re-identification assessment, because a label applied without one leaves personal data in scope while removing it from the schedule. Where deletion cannot reach into a backup, the position is recorded honestly as the data being put beyond use, with the expiry cycle that will eventually remove it, the commitment not to restore it into live use, and the suppression that runs if a restore happens. Legal hold outranks the schedule and outranks an erasure request, and a hold with no scope is not a hold that can be checked against. Verification is what a system returns: a zero-row query, a not-found response, a job log with counts, a vendor certificate. A closed ticket records that someone was asked.

**Ordered sequence for executing disposal.** This order is mandated because deletion is irreversible, because destroying data under hold converts a routine task into a spoliation problem, and because a confirmation collected before the downstream copies are handled records only part of an outcome:

1. Run the hold check across the exact scope and record its result, including holds that exist as preservation notices rather than as register entries.
2. Obtain the named approval for the disposal set, with its reach and the absence of rollback stated.
3. Execute in the systems that can confirm absence, and capture what confirmed it.
4. Instruct processors and downstream holders, and track each confirmation rather than assuming the instruction landed.
5. Record the backup and immutable-store position with the expiry cycle and the restore-time suppression.
6. Record the exceptions that remain with the basis permitting each, and close the disposal only then.

**Parallel surface.** Record classes, systems, per-system capability tests, and per-vendor deletion instructions are independent and fan out safely, as do the per-class citation checks. Three steps are aggregate and run once after the fan-out returns: the schedule itself, where one record class landing in eleven systems has to resolve to one period rather than eleven; the hold check, which is a question about the whole disposal scope and not about any single system; and the over-retention position across the estate, which is a coverage statement and cannot be produced from parts.

**Acceptance bar.** Every record class has a period, a trigger event, and a basis that names its source. Every class and system pair has a disposal method and a statement of what that system can confirm. The hold check is a documented step with a result rather than an assumption. Every exception names what permits the copy to remain. The over-retention list names systems and ages rather than reporting a percentage.

## Outputs

A complete run delivers this set:

- `retention-schedule.md`: per record class the period, the trigger event, the basis with its citation or written rationale and owner, the systems the class lands in, and the classes that currently have no defensible basis.
- `disposal-method-matrix.md`: per class and system the method, whether the platform deletes hard, what the deletion confirms, cascade behavior, retention locks, and the log or audit copy that survives.
- `legal-hold-position.md`: active holds with matter, scope, custodians, and issue date, the preservation notices not yet formalized, the record classes each hold freezes, and the check procedure that runs before any disposal.
- `deletion-execution-plan.md`: the disposal set, the reach across systems, backups, and processors, the approval required, the verification each system will return, the exceptions expected, and the explicit statement that there is no rollback.
- `processor-deletion-instructions.md`: per vendor the instruction, the clause it is issued under, the format and timing committed, the certificate available, and the retained copies the terms carve out.
- `over-retention-inventory.md`: data held past its own period by system, with the class, the age of the oldest record, the volume, why it is still there, and the data sitting in systems with no class assigned at all.
- `retention-downstream-handoff.md`: what `breach-assessment-desk` and the program record inherit, including which stores hold historic data that widens a breach population and which disposal actions are pending approval.

Depth standard: an artifact is complete when a platform owner could implement a lifecycle rule from it and a litigator could rely on the hold position. A schedule row without a trigger, or a disposal entry that names a method without saying what the system confirms, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the hold register, the backup inventory, or per-system retention configuration cannot be read, the run delivers `retention-connector-diagnostic.md` naming each unreachable source and the disposal decisions it blocks. No disposal is prepared for execution against an unread hold register, since the hold check is the one step whose absence is not recoverable after the fact.

Anti-fabrication guard: the field that invents itself here is the citation. Retention periods carry an air of legal authority, so a seven-year period acquires a tax provision and a five-year period acquires an anti-money-laundering one, and neither reference is ever checked again because the number looks right. Every citation in the schedule is quoted from the published text and attached only to the record class the provision actually covers; a period that came from precedent, from an industry norm, or from the previous schedule is recorded as a business rationale with the person who owns it, which is a legitimate basis honestly stated rather than a borrowed statute. The second invention is the deletion confirmation: a job that ran, a ticket that closed, and a vendor that acknowledged an instruction are three different things and none of them is a system confirming absence. Where a platform cannot confirm, the artifact says the platform cannot confirm, because a schedule that claims verified disposal it never observed is the document a regulator will test first.

## privacy_packet fields to update

- `retention[]` in full: `record_class`, `period`, `basis`, `trigger_event`, `systems_covered`, `backups_and_archives`, `exports_and_copies`, `disposal_method`, `legal_hold` with `active`, `matter`, `scope`, and `released_on`, and `state`
- `retention[].state` set to `undefined` for classes with no defensible basis and `blocked_by_hold` where a hold freezes disposal, rather than defaulting to `defined`
- `deletion_records[]` prepared with `covers`, `hold_check`, `systems_executed`, `systems_pending`, `processors_instructed`, `verification_basis`, and `exceptions`, held at the approval gate rather than marked complete
- `processing_activities[].retention_ref` linked so each activity carries a schedule row rather than a free-text period
- `data_inventory[].volume` updated where a row count was taken, with the date it was counted
- `source_facts` with the retention drivers and their citations separated from business rationale, `assumptions`, `open_questions`, `approvals` for every disposal set, `active_clocks` for hold reviews and erasure deadlines
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: executing deletion is irreversible and runs across systems, backups, and processors simultaneously. This desk prepares the set, the hold check, the verification each system will return, and the statement that there is no rollback, then stops.
- **Missing approval**: the disposal set, a shortened period, an extended period, a hold release, and an accepted over-retention each need a named owner, and a hold release needs the matter owner rather than the data owner.
- **Security or privacy**: a proposed disposal would destroy data under an open legal hold or under a preservation notice that was never formalized, which converts a retention task into a spoliation problem no privacy argument repairs.
- **Source conflict**: the schedule, the system configuration, and the statutory driver genuinely disagree about the period for a class. Preserve every reading; adopting the shortest one destroys records the organization needed and adopting the longest one keeps data with no basis.
- **Release integrity**: the schedule or a disposal record would state verified deletion, or a citation-backed period, on evidence that does not carry it.
- **Connector unreachable**: the hold register, the backup inventory, or per-system retention configuration exists and cannot be read. Disposal does not proceed on an unread hold register.

An unassigned record class in a low-volume store, a missing volume figure, and an unconfirmed backup tier are soft gaps. Label the assumption against the class and continue building the schedule.

## Downstream handoffs

`breach-assessment-desk` is next and needs the historic data footprint, since a store holding eight years of records because nothing ever expired is what turns a small incident into a large affected population. `rights-request-fulfillment-desk` needs the disposal methods and the per-system confirmation capability so an erasure response can state what was actually done. `processor-vendor-agreement-desk` receives the vendors whose contractual deletion commitment exceeds their technical capability. `data-inventory-mapping-desk` receives the copies and shadow stores found here that the map did not carry. `privacy-program-metrics-desk` needs schedule coverage against record classes and the share of systems with an implemented rule rather than a documented one.

## Quality bar

Good retention work is distinguishable from a policy document by three things. Every row has a trigger event, because a period without one cannot be implemented and most published schedules quietly lack them. Every basis names its source and the ones that came from habit say so, which is a stronger position than a citation that does not survive being read. And the schedule is reconciled against what the systems actually hold, so the artifact contains an over-retention list with names and ages rather than a statement that the organization retains data in accordance with its schedule. Beyond that, the tell of real work is the honesty about backups and soft deletes: an organization that writes down that its warehouse copy expires on a ninety day rotation and that its primary store only tombstones is in a defensible position, and one that reports both as deleted is one restore away from finding out otherwise.
