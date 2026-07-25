---
name: warehouse-lakehouse-architecture-desk
description: design warehouse and lakehouse storage, covering zone and layer architecture, table format and its transactional guarantees, partitioning against real query predicates, clustering and sort order, file sizing and compaction, snapshot and time travel retention as the recovery window destructive operations depend on, workload isolation across ingest transform and query compute, and the catalog of record. use for medallion layering, table format selection, partition and cluster design, small file problems, and vacuum or retention decisions.
---

# Warehouse Lakehouse Architecture Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the architecture artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a table property, a partition specification, a snapshot retention window, a file count, a platform capability, or a compute configuration.

## Role

This desk decides the physical arrangement that every later stage is bound by. It owns the zone and layer architecture and what a table is permitted to do in each layer, the table format and the transactional guarantees it actually provides at the deployed version, partitioning chosen against predicates that are genuinely filtered on, clustering or sort order, file sizing and the compaction policy including the small-file problem the streaming path creates, snapshot and time travel retention, workload isolation across ingestion, transformation, and query compute, and the catalog of record that governs table metadata.

Snapshot retention deserves separate mention because it is not only a storage-cost setting. It is the recovery window that every destructive operation in this suite depends on. A backfill, a table replacement, a schema change that drops a column, and a correction after a bad load are all reversible exactly as far back as the snapshot window reaches, and that window expires on a clock nobody consults under pressure.

## Use when

- A new platform or a new zone architecture is being laid out and the rules for each layer have not been written.
- Queries scan far more than they should and the partition or cluster keys were chosen against predicates nobody actually filters on.
- A streaming or micro-batch path is producing thousands of small files and compaction is unmanaged.
- Time travel or snapshot retention is being set or reduced, which changes what a recovery can reach.
- Ingestion, transformation, and interactive queries contend on the same compute and one starves the others.
- Tables exist in more than one catalog and it is unclear which registration governs.

## Do not use when

- The logical shape and grain are still open. That is `data-modeling-desk`, and partitioning a table whose grain is undeclared is guesswork.
- The subject is the mechanics of landing data into the zone. That is `ingestion-pipeline-desk`.
- The subject is model materialization and incremental strategy in SQL rather than the physical layout underneath it. That is `transformation-layer-desk`.
- The work is attributing and reducing spend rather than designing the layout that constrains it. That is `data-platform-cost-desk`, which inherits the constraints set here.
- The work is moving to a different platform. That is `data-migration-desk`.

## Required evidence

- The logical model with declared grains and expected row counts and growth from the modeling stage.
- Actual query patterns: the predicates, joins, and aggregations that appear in query history, with their frequency and their scanned bytes, rather than the predicates a design document expects.
- Current table metadata where tables exist: format and format version, partition specification, sort or cluster keys, file counts and size distribution, snapshot count and age, and table properties as configured.
- Platform capabilities at the deployed version, including which transactional guarantees, maintenance operations, and catalog features are actually available rather than available in the newest release.
- Concurrency and workload evidence: peak query concurrency, queue or slot contention, and the schedule the transformation layer runs on.
- Retention and history requirements from the product definition and any regulatory basis that binds them.

## Workflow

**Outcome.** A physical design a platform engineer can implement: the zone and layer rules, the table format with the guarantees it provides and the ones it does not, partition and cluster specifications tied to the predicates that justify them, file sizing and compaction policy with its trigger, snapshot and time travel retention stated as the recovery window with its expiry behavior, workload isolation across compute, and the catalog of record with the registration path.

**Grounding.** Choose partition keys from observed predicates in query history rather than from the columns that feel natural, because the partition key that matches the reporting calendar and the one that matches the filter people actually type are frequently different columns. Read current partitioning, file sizes, snapshot age, and table properties from table metadata, not from the creation script, since maintenance jobs and manual interventions move them. Read the format's guarantees from the deployed version, because a capability the platform gained two releases ago is not a capability this deployment has.

**Constraints.** A partition key is judged by its cardinality against the data volume, so partitions that produce many tiny files or a handful of enormous ones are named as wrong rather than as a preference, and a high-cardinality key such as an identifier is rejected explicitly with its consequence. Clustering is specified with the predicate it serves and the maintenance it requires, since a sort order that is never re-applied decays. File sizing has a target and a compaction trigger, and the streaming path is addressed by name because it is the reliable source of small files. Concurrent writers are addressed explicitly: the isolation level the format provides, what happens when a compaction and a merge overlap, and which operations are safe to run alongside a scheduled load. Snapshot and time travel retention is written as a recovery window with a stated duration, and every layer's window is set against the longest destructive operation that layer must be able to reverse. Each layer states what a table there is allowed to do, including whether raw payloads are immutable, whether deletes are permitted, and which layer is the one a consumer may query.

**Parallel surface.** Independent tables, independent partition and clustering evaluations, independent file-size and compaction assessments, and independent metadata reads fan out safely. The aggregate runs once after the fan-out returns: the layer policy applied consistently across the estate, the workload isolation decision which is a shared-resource judgment by definition, and the retention window rolled up so that no layer's window is shorter than the recovery a downstream layer depends on. A per-table storage decision that never composes into a layer policy produces an estate where every table is individually defensible and collectively unmaintainable.

**Ordered sequence for reducing snapshot retention or expiring snapshots.** This order is mandated because expiry is irreversible and it destroys the evidence that every other rollback in this suite relies on:

1. Establish which operations currently depend on the window, including scheduled backfills, restatement policy, and any open incident whose correction is not yet reconciled.
2. Obtain the named approval from the owner of every data product whose recovery window would shorten.
3. Confirm an independent copy exists for anything whose required recovery reach exceeds the new window, and confirm its own retention outlasts the change.
4. Apply the change to one non-critical table first and confirm the reachable history matches the new window.
5. Apply across the estate, then record the new recovery reach per layer where the destructive-operation sequence in `references/suite-workflow-contract.md` will look for it.

**Acceptance bar.** A platform engineer can create the tables and the maintenance jobs from the artifact. Every partition and cluster key names the predicate that justifies it and the cardinality that makes it viable. Every layer states its permitted operations and its retention. Compaction has a trigger and a target size. The recovery window is a number, per layer, with the destructive operations it covers.

## Outputs

A complete run delivers this set:

- `storage-architecture.md`: the zone and layer model, what each layer holds, what a table there may do, who may read it, and the promotion rule between layers.
- `table-format-decision.md`: the format and version, the transactional and isolation guarantees it provides at the deployed version, the concurrent-writer behavior, the maintenance operations it requires, and the guarantees it does not provide stated explicitly.
- `partition-and-cluster-design.md`: per table the partition specification with the predicate and cardinality that justify it, the clustering or sort order, and the predicates that will not prune with the consequence of that.
- `file-and-compaction-policy.md`: target file size, compaction trigger and cadence, the small-file sources including the streaming path, and the interaction between compaction and concurrent writes.
- `retention-and-recovery-window.md`: snapshot and time travel retention per layer, what a recovery can reach, the expiry behavior, and the destructive operations each window is sized to cover.
- `workload-isolation.md`: the compute separation across ingestion, transformation, and interactive query, the concurrency limits, and the contention evidence behind the split.
- `catalog-of-record.md`: which catalog governs, how tables are registered, what happens to a table created outside it, and the reconciliation for objects registered in more than one place.
- `storage-architecture-downstream-handoff.md`: what `ingestion-pipeline-desk` inherits, including the landing layout, the file target, and the immutability rule for raw records.

Depth standard: an artifact is complete when the tables and maintenance jobs could be created from it without a follow-up round trip. A partition specification without a justifying predicate, or a retention setting without the recovery it is sized for, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when table metadata, query history, or the catalog cannot be read, the run delivers `storage-architecture-connector-diagnostic.md` naming each unreachable source and the layout claims that depend on it. Partitioning is not recommended against query patterns nobody observed.

Anti-fabrication guard: the risk that is specific to this desk is describing a platform that does not exist as deployed. Storage settings are quotable-sounding by nature, so a snapshot retention of seven days, a target file size, or a clustering key reads as read-from-metadata whether it was or not, and a recovery plan built on an assumed window fails at exactly the moment it is needed. So every partition specification, sort key, table property, file count, snapshot age, and retention window in the output is quoted from table metadata or from the platform configuration, and anything else is written as proposed with the setting that would have to be applied. Platform capabilities are established against the deployed version, since a design that relies on a feature this deployment does not have is not a design. Query predicates and scan volumes name the history query they came from; a predicate that was assumed rather than observed is labeled as assumed, because a partition key chosen for an imagined filter costs a full rewrite to correct. And a recovery window is never stated as adequate without the number and its source, since adequate is the word that turns an unread setting into a rollback plan nobody can execute.

## data_packet fields to update

- `storage_architecture.layout`, `table_format`, `partitioning`, `clustering`, `file_sizing`, `snapshot_retention`, `compute_isolation`, and `catalog_of_record`
- `models[].materialization` constrained where the layer policy restricts what a model may be
- `data_risks[]` for tables whose recovery window is shorter than the operations performed on them, and for high-cardinality partition keys already in place
- `cost.efficiency_findings` seeded with the pruning, file-sizing, and idle-compute observations this stage surfaces, left unpriced until the cost stage
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: reducing a retention or time travel window shortens the recovery reach for data products whose owners have not accepted it, or a layer policy change would restrict access a consumer currently relies on.
- **Production or destructive**: the next action would expire snapshots, run a vacuum or file-removal maintenance operation, repartition or rewrite an existing table, change a table property on a live table, or resize or suspend compute that a consumer depends on.
- **Security or privacy**: a layer or zone would place restricted data where the access model is broader than the source classification requires, or a lower-trust zone would receive personal, health, or cardholder data as a side effect of the layout.
- **Source conflict**: table metadata, the creation script, and the catalog registration genuinely disagree about partitioning, format, or ownership, and choosing one silently produces a maintenance job that operates on the wrong assumption.
- **Release integrity**: a recovery window, a transactional guarantee, or a pruning behavior would be recorded as established without the metadata or configuration evidence behind it.
- **Connector unreachable**: table metadata, query history, the catalog, or the platform configuration needed to establish current layout exists and cannot be read.

An unknown future growth rate, an unmeasured peak concurrency, and an undecided naming convention for zones are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`ingestion-pipeline-desk` is next and needs the landing layout, the raw-record immutability rule, the file target that bounds micro-batch sizing, and the layer the boundary writes into. `transformation-layer-desk` needs the materialization options each layer permits and the concurrent-writer behavior that decides whether a merge and a compaction can overlap. `streaming-pipeline-desk` needs the small-file consequence of its write cadence. `data-retention-lifecycle-desk` needs the snapshot window, because deletion is not complete while time travel still holds the rows. `data-platform-cost-desk` inherits the pruning, file-sizing, and isolation findings as the constraints its spend analysis works within.

## Quality bar

Good architecture work here is specific about physics. It states the cardinality that makes a partition key wrong, not a preference for daily partitions. It names the streaming path as the small-file source and gives the compaction trigger, rather than recommending compaction in general. It treats snapshot retention as a recovery contract with a number attached and says which destructive operations that number covers, because the alternative is discovering the window expired the day a backfill has to be reversed. It says what the format does not guarantee, since the gaps are what surprise people. And it separates the layer policy from the per-table decisions, so the estate stays coherent when the next twenty tables are added by somebody who never read this document.
