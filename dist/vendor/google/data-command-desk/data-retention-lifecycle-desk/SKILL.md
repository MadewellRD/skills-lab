---
name: data-retention-lifecycle-desk
description: design data retention and erasure covering retention schedules with their regulatory contractual or operational basis, deletion mechanisms that actually remove data given table format snapshots time travel and backups, the propagation map of every derived copy, data subject request location across copies, archival tiering, legal hold precedence over scheduled deletion, residual copies with expiry dates, and rules that were never enforced. use for retention schedules, erasure requests, purge design, and archival tiering.
---

# Data Retention Lifecycle Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the retention and erasure artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A retention period nobody has documented is a soft gap and is carried as undefined; declaring an erasure complete without confirmation across every enumerated copy is a release-integrity halt, because a false compliance record is worse than an open one and is discovered by the party least willing to accept it. Never invent retention periods, regulatory citations, deletion dates, snapshot windows, backup contents, legal hold status, or the fact that a rule has ever run.

## Role

Own how long data lives and how it actually goes away. This desk holds the retention schedule per dataset with the basis that establishes it, the deletion mechanism and whether it removes data given the table format and snapshot window, the propagation map of every derived copy, subject request location across those copies, archival tiering and what becomes unqueryable, legal hold and its precedence, the residual copies policy permits with their expiry, and the enforcement record naming the rules that have never actually run.

The defining property of this stage is that deletion is not a state, it is a set of operations across copies with different lifetimes, and the copies outlive the original. A row deleted from a table remains readable through time travel, remains in the snapshot the platform keeps for recovery, remains in last night's backup, remains in the aggregate that summarized it, remains in the extract inside a reporting tool, and remains in the file exported to a partner. The second property is that this domain fails toward paper: retention schedules are among the most reliably documented and least reliably executed artifacts in any organization, and the gap between the schedule and the enforcement record is the finding this desk exists to produce.

## Use when

- Retention needs setting or reviewing for a dataset, and the period needs a stated regulatory, contractual, or operational basis rather than a convention.
- A deletion or purge is being designed and it needs to actually remove data given the table format, its snapshot or time travel window, and the backup configuration.
- A data subject erasure or access request needs locating a single subject across every copy that holds them.
- A dataset is being tiered to archival storage and what becomes slow, expensive, or unqueryable needs stating before it moves.
- A legal hold is in force or arriving, and its precedence over scheduled deletion needs establishing across every affected copy.
- A retention rule exists on paper and nobody can say when it last ran, or whether any job implements it at all.
- Storage cost work has surfaced data nobody queries and the question is whether retention permits removing it.
- Residual copies persist after a deletion and their existence, justification, and expiry need recording rather than being left implicit.

## Do not use when

- The subject is who may read the data. That is `data-governance-access-desk`, whose classification and copy inventory this desk inherits.
- The subject is the snapshot and time travel window as a storage design choice. That is `warehouse-lakehouse-architecture-desk`; this desk consumes that window as the fact that bounds every deletion claim.
- The subject is the privacy program itself: lawful basis, consent, the intake and response clock for subject requests, or cross-border transfer. That is a labeled cross-suite handoff to the Privacy suite; this desk locates and removes the data those obligations require.
- The subject is reducing storage spend rather than meeting an obligation. That is `data-platform-cost-desk`, which this desk supplies with the retention constraint that bounds any deletion for cost reasons.
- The subject is retiring an asset because nobody reads it. That is `lineage-catalog-desk`; this desk decides whether retention permits its removal.

## Required evidence

- Classification per dataset and column, and the regulatory or contractual obligations bound to each, inherited from the governance stage.
- The retention schedule, records management policy, and any contractual clause that sets a period, read as documented intent.
- The lineage graph plus the export, extract, and reverse-ETL inventory, since the propagation map is a traversal over them.
- Table format and its transactional metadata: snapshot retention, time travel window, and the maintenance operation that expires them.
- Backup and disaster recovery configuration: what is backed up, at what frequency, with what retention, and whether a restore is selective or whole-cluster.
- The job inventory and run history for anything that currently implements a deletion, purge, or archival move, which is what distinguishes an enforced rule from a written one.
- Legal hold records: what is held, since when, by whose instruction, and over which datasets and date ranges.
- Storage tier configuration and the retrieval cost and latency of each tier the data may move to.
- The identifier that locates a subject, and the derived assets where that identifier has been dropped, hashed, or aggregated away.

## Workflow

**Outcome.** A retention schedule per dataset with its basis and source, a deletion mechanism per dataset that accounts for the table format and snapshot window, a propagation map naming every copy that holds the record, a subject request procedure that locates a person across those copies including where the identifier no longer exists, an archival tiering design with its retrieval consequences, a legal hold register with precedence stated, a residual copy register with expiry dates, and an enforcement record stating when each rule last actually ran.

**Grounding.** The period comes from the obligation that sets it, cited to the clause, contract, or policy, and where no obligation is identifiable the basis is recorded as operational or undefined rather than assigned a plausible number of years. Enforcement is established from job run history rather than from the existence of a policy, and a rule with no implementing job is recorded as never enforced, which is a finding rather than an omission. The propagation map is derived from lineage and the export inventory, and the paths lineage cannot see are carried in as gaps, since a copy the graph misses is a copy the deletion misses.

**Constraints.** Every retention rule names the dataset, the period, the basis with its source, the deletion mechanism, the derived copies, the legal hold state, and the date it was last enforced with the evidence. The deletion mechanism is assessed against the physics of the platform rather than accepted at face value: a row delete on a table with a thirty-day time travel window has not removed the data for thirty days, a partition drop does not touch the aggregates built from that partition, a full refresh does not remove rows whose source has stopped producing them, and crypto-shredding removes nothing while a copy of the key survives in a backup. Archival tiering states what becomes unqueryable, what a retrieval costs, and how long it takes, because a tier decision made on storage price alone is discovered later by whoever needs the data during an audit. Legal hold takes precedence over every scheduled deletion and is applied across all copies rather than to the primary table, and a hold released is recorded with its date because the scheduled deletion resumes from that moment. Residual copies that policy permits are named individually with their expiry, so an erasure record says what still exists rather than implying nothing does.

**Parallel surface.** Datasets under review, per-dataset basis research, per-copy enumeration, archival tier assessment, and the per-job enforcement check are independent units and fan out safely. The aggregate work runs once after the fan-out returns: composing the propagation map across the lineage graph, ordering the deletion across copies so derived assets are removed before their source, reconciling legal holds against the schedule to find the datasets where both apply, and assembling the subject request procedure that has to work across every copy at once. Deletion ordering is not parallelizable at all, because the order is the correctness property.

**Ordered gate: legal hold precedence.** Before any scheduled deletion, purge, archival move, or erasure execution, the hold check runs first and covers every dataset and date range in scope, not only the primary table. Deleting under an active hold is a spoliation event that no later remediation repairs, and the hold frequently covers a date range within a dataset rather than the dataset entire. Where a hold is active on any part of the scope, the deletion is bounded to exclude it and the exclusion is recorded, or the operation stops for the hold owner.

The execution order across copies, the suppression step, and the snapshot expiry step are mandated in `references/suite-workflow-contract.md` and are not restated or reordered here; this desk supplies the enumerated copy list that sequence operates over.

**Acceptance bar.** A reader could state, for each dataset in scope, how long it is kept and on what authority, what mechanism removes it, every place a copy survives, when the rule last actually ran, and what would still hold a record after a deletion is declared complete. Every rule with no implementing job is visible as never enforced.

## Outputs

A complete run delivers this set:

- `retention-schedule.md`: per dataset, the period, its regulatory, contractual, or operational basis with the source that establishes it, the owner, and the datasets whose basis is undefined.
- `deletion-mechanism.md`: per dataset, the mechanism, what it actually removes given the table format, the snapshot and time travel window that delays removal, the maintenance operation that closes that window, and the backup path that outlives both.
- `copy-propagation-map.md`: every derived model, aggregate, extract, feature table, reverse-ETL destination, file export, snapshot, and backup holding the record, with the lineage gaps that bound the map's completeness.
- `subject-request-procedure.md`: how one subject is located across every copy, the identifier used per copy, the assets where the identifier has been aggregated or hashed away and what that means for the request, the response path, and the record kept per request.
- `archival-tiering.md`: what moves, when, to which tier, what becomes unqueryable or slow, the retrieval cost and latency, and the obligations that require the data to remain producible.
- `legal-hold-register.md`: active holds with their scope, date range, instructing owner, the datasets and copies they cover, the scheduled deletions they suspend, and the release path.
- `enforcement-record.md`: per rule, when it last ran with the job and run evidence, the rules that have never run, and the residual copies that persist by policy with their expiry dates.
- `retention-downstream-handoff.md`: what `data-migration-desk` inherits, including obligations that must survive a platform move and the copies a migration would multiply.

Depth standard: an artifact is complete when a platform engineer could implement the purge and a compliance reader could accept the answer to where a record still lives. A retention entry with a period and no basis, a deletion mechanism that ignores the snapshot window, and a copy map that stops at the warehouse boundary are unfinished rather than draft.

When the table format metadata, backup configuration, job run history, or the export inventory exists and cannot be read, the run delivers `retention-connector-diagnostic.md` naming each unreachable source and the deletion and enforcement claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: the artifact this desk produces is the one an organization will later hand to a regulator, which makes an invented completion the most expensive sentence in the suite. The specific temptation is closure: a copy map that stops where the evidence stops feels finished, an erasure recorded as complete reads better than one recorded as complete except for a backup expiring in ninety days, and a retention period of seven years is such a common answer that it will pass review unchallenged whether or not any obligation says so. So a period is written with the clause, contract, or policy that sets it, or written as undefined, and a regulatory citation is never composed from what the obligation is likely to be. Deletion is described by what the mechanism actually removes on this platform, with the snapshot window and backup retention named as the interval during which the data is still readable. A copy map states the lineage gaps that bound it, since the copies most likely to be missed are the hand-scheduled ones with no metadata to find. And an enforcement date is quoted from a job run or written as never, because a rule assumed to be running because it exists is the exact condition this stage was created to expose.

## data_packet fields to update

- `retention_rules[]` with dataset, basis, period, deletion mechanism, derived copies, legal hold, and last enforced
- `retention_rules[].derived_copies` completed from the propagation map, with the lineage gaps that bound it
- `lineage.known_gaps` for copy paths discovered here that the graph does not carry
- `access_policies[].purpose_limitation` where an archival tier or export changes the audience
- `data_risks[]` for never-enforced rules, undeletable copies, holds that conflict with a schedule, and identifiers lost in derived assets
- `open_questions` for datasets with no identifiable retention basis and no owner
- `source_facts` with per-fact attribution, `decisions`, `assumptions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would delete rows or partitions, expire snapshots, drop a table, move data to a tier it cannot be retrieved from in time, or execute an erasure against a live dataset.
- **Missing approval**: deleting under a rule whose owner has not confirmed it, releasing or overriding a legal hold, accepting a residual copy as permanent, or tiering a dataset an obligation requires to remain producible needs a named owner who has not agreed.
- **Security or privacy**: an erasure would be recorded as complete while an enumerated copy still holds the records, a subject's identifiers would be carried into an artifact, or a deletion would be scoped from a copy map with known gaps on the path.
- **Source conflict**: the retention schedule, the contractual obligation, and the regulatory requirement genuinely disagree on a period, or a legal hold and a scheduled deletion both apply to the same date range.
- **Release integrity**: a rule would be recorded as enforced, an erasure as complete, or a dataset as compliant, without the run evidence and per-copy confirmation that establish it.
- **Connector unreachable**: table format metadata, backup configuration, job run history, the export inventory, or the legal hold register needed for this stage exists and cannot be read.

An undocumented period, an unnamed dataset owner, an unmeasured storage volume, and an archival tier whose retrieval cost is unpublished are soft gaps. Name them, label the assumption, and continue. Legal hold precedence, the requirement that erasure completion rest on per-copy confirmation, and the prohibition on inventing a regulatory basis are never relaxed to close a request faster.

## Downstream handoffs

`data-migration-desk` is next and needs the retention obligations that must survive the move, plus the warning that a dual run doubles every copy under an erasure obligation for the length of the run. `data-platform-cost-desk` inherits the retention floor that bounds any storage reduction, and receives the datasets retention permits removing. `data-governance-access-desk` receives the copies discovered here that sit outside their access control. `lineage-catalog-desk` receives the copy paths this stage found that the graph did not carry, and the tombstoning path for assets retention permits retiring. `data-incident-response-desk` inherits the snapshot and time travel window, since that window is also the recovery path every correction depends on. Send lawful basis, consent, the subject request intake clock, and cross-border transfer to the Privacy suite, and audit evidence packaging to the GRC suite, as labeled cross-suite handoffs.

## Quality bar

Good retention work is written from the copies inward rather than from the policy outward. It names every place a record survives before it discusses periods, because the period is the easy part and the propagation is where the obligation is actually met or missed. Each period cites the clause that sets it. Each mechanism is tested against the platform's own physics, so the snapshot window and the backup retention appear as intervals during which the data is still there. Legal holds are checked first and scoped to date ranges. Residual copies are named with expiry dates rather than left implied. And the enforcement record is the artifact a reviewer should read first, because a schedule with no run history is a document about deletion rather than evidence of it.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
