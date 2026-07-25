---
name: ingestion-pipeline-desk
description: design batch and change data capture ingestion, covering extraction pattern and watermark selection, snapshot plus stream stitching at a consistent log position, delete propagation, idempotency and deduplication keys, raw record preservation for replay, schema drift behavior at the boundary, dead letter and quarantine paths, extraction windows rate limits and pagination, historical backfill bounds, and landed count reconciliation against the source. use for elt extraction design, incremental loads, cdc setup, landing zone design, and duplicate or missing row investigations.
---

# Ingestion Pipeline Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the ingestion artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a watermark column, a log position, a deduplication key, a landed row count, a rate limit, or a backfill boundary.

## Role

This desk designs the boundary where data leaves a system that owns it and enters one that does not. It owns the extraction pattern per source and the watermark or high-water mark that bounds a run; change data capture handling including the stitching of an initial snapshot to the change stream, delete propagation, and out-of-order change records; idempotency and the deduplication key that makes a re-run safe rather than doubling; the landing layout and the raw record preserved unmodified so a replay is possible at all; schema drift behavior at the boundary, meaning whether an unexpected field lands, quarantines, or fails the run; dead-letter and quarantine paths together with the person who reads them; rate limits, pagination, and the extraction window the source owner permits; the historical backfill plan with its bounds; and the reconciliation that compares landed counts against the source.

Two of these decide whether the pipeline is trustworthy. The watermark decides whether rows are missed, and the deduplication key decides whether rows are counted twice. Everything else is recoverable.

## Use when

- A new source is being loaded and the extraction pattern, watermark, and dedup key have not been fixed.
- A load duplicates rows on retry, or misses rows that were modified during the extraction window.
- Deletes in the source are not reaching the target, or soft deletes are being read as live records.
- A change feed is being stood up and the snapshot and the stream have to be stitched without a gap or an overlap.
- The source changes shape and the boundary currently fails silently or drops the new field.
- History has to be loaded and nobody has bounded the backfill or checked whether the source retains that far back.

## Do not use when

- The source shape, keys, and delete behavior have not been established. That is `source-system-profiling-desk`, and an ingestion design on an unprofiled key is a duplicate generator.
- The subject is continuous stream processing semantics such as windowing, watermarks over event time, and state stores. That is `streaming-pipeline-desk`.
- The subject is what happens after landing, in staging and marts. That is `transformation-layer-desk`.
- The subject is scheduling, sensors, retries, and pool contention rather than the extraction itself. That is `batch-orchestration-desk`.
- Bad data already landed and reached consumers. That is `data-incident-response-desk`.

## Required evidence

- The profiled source with grain, real key, delete behavior, modification-timestamp trustworthiness, volume, and growth.
- The contract and its enforcement point, which decides what the boundary is permitted to accept.
- The change-feed configuration where one exists: log or write-ahead log retention, replication slot or change-tracking state, the position format, and the replica lag the reader operates behind.
- Extraction constraints from the source owner: batch window, rate limits, pagination and cursor expiry behavior, API quotas, and concurrency caps.
- The landing zone design and the raw-record immutability rule from the storage architecture stage.
- The freshness target the data product carries, since it bounds which extraction patterns are viable at all.
- Existing pipeline run history and any known duplicate, gap, or drift incidents.

## Workflow

**Outcome.** An ingestion design per source covering extraction pattern and watermark with its trust basis, the change-feed handling including snapshot stitching and delete propagation, the idempotency mechanism with its deduplication key, the landing layout with the raw record and its ingest metadata, the schema drift behavior with a defined outcome for each drift class, the error paths with an owner, the extraction window and rate limits, the backfill bounds, and the landed-count reconciliation.

**Grounding.** Take the watermark candidate and its trustworthiness from the profile, because a modification timestamp that a bulk job does not move produces a load that is silently incomplete rather than one that fails. Take log retention from the change-feed configuration, since it bounds how long a stalled consumer can be down before a snapshot is required again. Take rate limits and windows from the source owner rather than from observed behavior on a quiet day.

**Constraints.** Every run has an explicit boundary and every boundary has an overlap policy: a watermark read with a lookback window is stated with the lookback and the dedup that makes the overlap harmless. Idempotency is demonstrated rather than intended, which means the merge key is a real key from the profile, the record-selection rule for multiple versions of that key is written, and the behavior of a partial run followed by a re-run is stated. Deletes are handled explicitly by mechanism: tombstones from the change feed, a soft-delete flag carried through, or absence-based reconciliation against a periodic snapshot, and where the source hard deletes without a feed the design says so instead of implying deletes will arrive. The raw record lands unmodified with its ingest metadata, including the source, the extraction time, the file or offset, and the run identifier, because a replay is only possible against something that was not already interpreted. Schema drift has a defined outcome per class, covering a new field, a widened type, a narrowed type, a rename, and a drop, and silent success is not one of the permitted outcomes. Dead-letter and quarantine paths name the person who reads them and the cadence, since an unread quarantine is data loss with extra steps. Extraction never exceeds the window the source owner permits, and pagination handles cursor expiry mid-run.

**Parallel surface.** Independent sources, independent tables within a source, and independent connectivity and rate-limit checks fan out safely, and independent partitions of a bounded historical backfill parallelize where the load is append-only into landing. The aggregate runs once after the fan-out returns: the total load imposed on a shared source, the reconciliation of landed counts against source control totals, and the sequencing of backfill against the scheduled load. The snapshot-plus-stream stitch below is sequential by physics and does not fan out.

**Ordered sequence for standing up a change feed with an initial snapshot.** This order is mandated by the log itself, and getting it wrong loses changes permanently rather than visibly:

1. Start capturing the change stream and confirm it is retaining, before any snapshot is taken, so changes made during the snapshot are not lost.
2. Record the log position at which capture began, since it is the only anchor that makes the stitch reproducible.
3. Take the snapshot within the extraction window the source owner permits, using the read path agreed with them.
4. Apply the change stream from the recorded position forward, with the deduplication key resolving records the snapshot already contains.
5. Reconcile landed counts and a control total against the source before any consumer reads the result, and only then release the target.

The order is mandated because a snapshot taken before capture starts leaves an unrecoverable gap for every change in between, and a log position recorded after the fact is a guess that reprocesses or skips an unknown range. Do not compress these steps to save an outage window.

**Acceptance bar.** A re-run produces the same target rather than a second copy, and the reason it does is written down as a key rather than asserted. Every source names its watermark with its trust basis, its dedup key, and its delete mechanism. Every drift class has an outcome. Every backfill has bounds and a reconciliation. The raw layer is replayable.

## Outputs

A complete run delivers this set:

- `ingestion-design.md`: per source the extraction pattern, watermark and lookback, run boundary, schedule expectation, and the freshness the design can actually deliver against the target.
- `cdc-and-delete-handling.md`: the change-feed configuration, log retention and its implication for downtime, the snapshot stitching plan with the position anchor, out-of-order change handling, and the delete propagation mechanism.
- `idempotency-and-dedup.md`: the merge or deduplication key, the record-selection rule for multiple versions, the behavior of a partial run followed by a re-run, and the evidence that the key is actually unique.
- `landing-layout.md`: the raw record format, the ingest metadata columns, the immutability rule, the file or partition layout, and the replay procedure the layer enables.
- `schema-drift-policy.md`: the outcome per drift class at the boundary, where the check runs, what the alert says, and how a quarantined batch is released after a decision.
- `error-and-quarantine-paths.md`: dead-letter destination, quarantine table shape including the failure reason and run identifier, the named reader, the review cadence, and the reprocessing path.
- `backfill-plan.md`: the bounds, the source retention that limits how far back is possible, the ordering constraint, the concurrency cap, the control total, and the approval state.
- `ingestion-reconciliation.md`: the landed-count and control-total comparison against the source, its tolerance, the reason that tolerance is acceptable, and what a variance triggers.
- `ingestion-downstream-handoff.md`: what `streaming-pipeline-desk` and `transformation-layer-desk` inherit, including the dedup key and the ingest metadata available for incremental predicates.

Depth standard: an artifact is complete when the pipeline could be built and re-run safely from it. A watermark named without its trust basis, or a quarantine path without a reader, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the source, the change-feed configuration, or the pipeline run history cannot be read, the run delivers `ingestion-connector-diagnostic.md` naming each unreachable source and the design claims that depend on it. A stitching plan is not written against a log whose retention nobody read.

Anti-fabrication guard: the specific failure at this desk is asserting a safety property. Idempotent, exactly-once, and fully reconciled are all claims about a running system, and all three are cheap to type and expensive to discover as false, because the discovery happens in a downstream total that nobody was watching. So idempotency is recorded as unproven unless the merge key is a key the profile measured as unique and the record-selection rule is written out; intent is not proof. Watermark columns, log positions, offsets, and cursor semantics are quoted from the source and its configuration, never inferred from a naming convention, because a watermark on a column the source does not maintain produces a load that succeeds every night and is missing rows. Landed counts, source counts, and variances name the query and the run they came from, and a reconciliation that has not executed is written as not reconciled rather than as within tolerance. Rate limits and permitted windows are quoted from the source owner, since an assumed limit is discovered by exceeding it on someone else's production system.

## data_packet fields to update

- `pipelines[]` with `name`, `kind`, `trigger`, `watermark`, `idempotency`, `failure_handling`, `backfill_procedure`, and `runtime`
- `source_systems[].extraction_pattern` and `extraction_constraint` confirmed against what the design actually uses
- `backfills[]` with `target`, `bounds`, `reason`, `idempotency_basis`, `approval`, `reconciliation`, and `state` left at `planned` until an approver is named
- `reconciliations[]` for the landed-count comparison, with `result` left as not reconciled until a run produces one
- `data_risks[]` for untrustworthy watermarks, hard deletes with no feed, and unread quarantine paths
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a backfill over live partitions, an extraction outside the window the source owner permits, or enabling a change feed that changes the source's log retention needs the named owner.
- **Production or destructive**: the next action would write to or replace a production target, run a historical backfill, reset a replication slot or consumer position, truncate a landing location a replay depends on, or place read load on a source primary during a business window.
- **Security or privacy**: restricted columns would land in a zone whose access model is broader than the source classification, raw payloads containing personal, health, or cardholder data would be preserved beyond the retention their classification allows, or a quarantine table would hold restricted rows where the named reader is not entitled to them.
- **Source conflict**: the source count, the change feed, and the landed count genuinely disagree, or the profile and the live schema disagree about the key the merge depends on, and proceeding would silently choose which rows survive.
- **Release integrity**: a load would be recorded as idempotent, complete, or reconciled without the key evidence, the bounds, or the control total that establishes it.
- **Connector unreachable**: the source, its change-feed configuration, the landing zone, or the run history needed to design or bound the load exists and cannot be read.

An unknown historical growth rate, an unmeasured typical runtime, and an undecided alerting channel are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`streaming-pipeline-desk` is next where a stream exists and needs the stitching anchor, the delete semantics, and the dedup key that the streaming path has to agree with. `transformation-layer-desk` needs the dedup key, the ingest metadata columns available for incremental predicates, the landed grain, and the drift behavior it can rely on. `batch-orchestration-desk` needs the run boundary, the expected runtime, the arrival cadence, and the classes of failure that should not retry. `data-quality-desk` needs the reconciliation definition and its tolerance. `data-incident-response-desk` inherits the replay path and the raw layer that makes a correction possible.

## Quality bar

Good ingestion design is paranoid in specific, defensible places. It says why the watermark is trustworthy, or admits it is not and adds a lookback with a dedup that makes the overlap harmless. It states the delete mechanism rather than assuming deletes will show up, because the most common silent error in this domain is a target that accumulates records the source removed years ago. It preserves the raw payload unmodified, since every replay, every correction, and every argument about what the source actually sent depends on it. It names who reads the quarantine, because the design that routes bad rows somewhere nobody looks is indistinguishable from the design that drops them. And it reconciles counts against the source rather than trusting that the job exited zero, since an empty extract also exits zero.
