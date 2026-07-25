---
name: source-system-profiling-desk
description: profile source systems before extraction, establishing record grain, candidate and actual primary keys, uniqueness violations, null rates, cardinality, value ranges, encoding and type surprises, arrival cadence and lateness, hard versus soft delete behavior, change data capture feasibility, source load and rate limits, and the column level pii phi and pci classification every later stage inherits. use for source discovery, data profiling, key analysis, extraction feasibility, and cdc assessment.
---

# Source System Profiling Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the profile artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a table name, a column name, a data type, a row count, a null rate, a cardinality, an arrival cadence, or a classification.

## Role

This desk establishes what a source actually contains and what it will actually give up, as opposed to what its schema and its owning team say. It owns the record grain, the candidate keys and the key that is actually unique, the uniqueness violations that disqualify the declared one, null rates and how they move over time, cardinality and value ranges, the encoding and type surprises that survive into every downstream cast, arrival cadence with expected lateness and out-of-order behavior, delete behavior, the extraction pattern the source can support including whether change data capture is available at all, the load a full extract places on the system and the window its owner will allow, and the column-level classification of personal, health, cardholder, and otherwise restricted data.

That classification is recorded here because every later stage inherits it and none of them can rediscover it cheaply. A free-text notes column carrying customer names is a governance problem in the mart, a retention problem in the archive, and an exposure problem in the non-production copy, and all three inherit the profiling call.

## Use when

- A source is a candidate for a new pipeline and nobody has established its grain, its real key, or its volume.
- A declared primary key is about to be trusted as a join key or a merge key downstream.
- The extraction pattern is undecided and the answer depends on whether an incrementing column is trustworthy, whether a log-based feed exists, and what the source owner will permit.
- Loads are duplicating or dropping rows and the cause is suspected to be in the source shape rather than the transformation.
- Deletes are disappearing from the target silently, or reappearing.
- Restricted data may be present in columns the schema does not label as sensitive.

## Do not use when

- The shape is understood and the work is committing the producer to it. That is `data-contract-desk`.
- The work is designing the extraction mechanics, watermarks, and dedup keys against a profile that already exists. That is `ingestion-pipeline-desk`.
- The subject is the target model rather than the source. That is `data-modeling-desk`.
- The source is a stream and the questions are ordering, windowing, and lateness semantics. That is `streaming-pipeline-desk`.
- A load is failing right now and consumers already have bad data. That is `data-incident-response-desk`.

## Required evidence

- Read access to the source or an existing profile, with the snapshot date and the row scope each statistic was computed over.
- The source schema as the system reports it: information schema or catalog, constraints, indexes, defaults, and collation, rather than an entity diagram.
- Change-feed capability evidence where relevant: transaction log or write-ahead log availability, its retention, replication slot or change-tracking configuration, and the replica lag the extract would read behind.
- The extraction constraints the owning team imposes: batch window, rate limits and pagination behavior, API quotas and cursor expiry, replica availability, and licence or seat limits.
- Application behavior the schema does not carry: whether records are updated in place, whether deletes are physical, whether a bulk job touches rows without moving the modification timestamp.
- Existing data dictionaries and dictionaries' disagreements with the live schema, kept as two separate readings.

## Workflow

**Outcome.** A profile per source that a downstream designer can build on: declared grain, the key that is actually unique with the violations that disqualify alternatives, null rates and cardinality per column with their measurement basis, type and encoding surprises named, arrival cadence with lateness and out-of-order behavior, delete behavior, the feasible extraction patterns with the constraint that bounds each, and a column-level classification covering restricted data.

**Grounding.** Profile the source, do not read about it. A declared primary key is a constraint in a schema; uniqueness is a measurement, and the two disagree often enough that the measurement is the finding. Cardinality and null rate come from a query with a stated scope and date, never from a data dictionary. Change-feed feasibility comes from the log configuration and its retention, not from a vendor capability page. Where the dictionary and the information schema disagree about a column, record both readings with attribution and preserve the conflict.

**Constraints.** Grain is stated as what one record represents, in words, before any key analysis, because a key that is unique at the wrong grain is the standard route to a silent fan-out downstream. Uniqueness is tested at the stated grain and over history rather than over a recent slice, since soft deletes, reactivations, and merges produce duplicates that a fresh partition never shows. Null rate is reported with its trend, because a column that is ninety percent null today and was zero percent null last year has a semantic change hiding in it. Type surprises are named concretely, covering numerics held as text, epoch values whose unit is ambiguous, booleans encoded as a mix of flags and nulls, timestamps with no timezone and no stated convention, precision and scale that will not survive the target type, and encodings or collations that change sort and equality. Delete behavior is established by observation rather than by assertion, because a source that "never deletes" and a source whose deletes are simply invisible to the extract look identical from the target. Profiling reads run against a replica or an approved window, never against a production primary outside the load the owner permits. Sample values are described by shape and never reproduced when the column carries restricted data.

**Parallel surface.** Independent source systems, independent tables within a source, and independent columns within a table fan out safely, as do the classification pass and the constraint interviews. The aggregate runs once after the fan-out returns: reconciling keys across sources so the same entity can be joined, judging whether a single extraction window fits the whole set against the source's total load budget, and rolling the column classifications up into a source-level sensitivity finding, because one restricted column changes the handling of every table that carries its key.

**Acceptance bar.** A pipeline designer can choose an extraction pattern and a deduplication key from this profile without opening the source. Every statistic names the query and the snapshot it came from. Every restricted column is classified or explicitly marked as unreviewed. The key section says which key is actually unique and shows the violation count for the ones that are not.

## Outputs

A complete run delivers this set:

- `source-profile.md`: one section per source with grain, volume and growth, arrival cadence, lateness, out-of-order behavior, and delete behavior, each with its measurement basis.
- `key-and-cardinality-analysis.md`: candidate keys, the actual unique key, duplicate counts per candidate with example key values redacted where restricted, orphan and referential-integrity findings against related tables, and the fan-out risk each many-to-many relationship creates.
- `column-profile.md`: per column type, null rate and its trend, distinct count, value range or top values by share, and the type, encoding, precision, and timezone surprises that will affect the cast.
- `extraction-feasibility.md`: the patterns the source supports, the change-feed configuration and its log retention where one exists, the watermark candidates with the reason each is or is not trustworthy, the load a full extract imposes, and the window and rate limits the owner permits.
- `column-classification.md`: the restricted-data call per column including free-text columns that carry personal data incidentally, with the basis for each call and the columns that were not reviewed.
- `source-profiling-downstream-handoff.md`: what `data-contract-desk` inherits, including the semantics the schema does not carry and the fields whose meaning is disputed.

Depth standard: an artifact is complete when the next desk can act on it without re-querying the source. A column entry with a type and no null rate, or an extraction section that names a pattern without the constraint that bounds it, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the source, its replica, or its catalog cannot be read, the run delivers `source-profiling-connector-diagnostic.md` naming each unreachable source, what was attempted, and the profile claims that depend on it. A key is not declared unique against a table nobody queried.

Anti-fabrication guard: a profile is a page of numbers, and a computed number and a reasonable-sounding one are typographically identical. That is this desk's specific exposure. So every count, null rate, distinct count, range, duplicate count, and growth figure carries the query and the snapshot date that produced it, and a statistic that was not computed is written as unprofiled rather than estimated from the column name or the table's apparent purpose. Column names and data types are taken from the live schema; a column the dictionary describes and the schema does not contain is recorded as a dictionary claim, not as a column. Change-feed availability is read from the source configuration, because a feed assumed to exist collapses the whole ingestion design that was built on top of it. Illustrative rows are not manufactured to show a pattern, and real rows are not copied out of a restricted column to prove one, so the finding describes the shape and cites the count instead.

## data_packet fields to update

- `source_systems[]` with `name`, `kind`, `extraction_pattern`, `grain`, `primary_key`, `volume`, `arrival`, `delete_behavior`, `profiling_state`, `classification`, and `extraction_constraint`
- `data_risks[]` for keys that are not unique, columns whose null rate is moving, and restricted data found where the schema does not label it
- `open_questions` for every semantic that the source owner has to answer rather than the schema
- `source_facts` with per-fact attribution split between the live schema and the documented dictionary, `decisions`, `assumptions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: profiling would exceed the extraction window or rate limit the source owner set, or enabling a change feed would require a configuration change on a system this suite does not own.
- **Production or destructive**: the next action would run a full scan against a production primary during a business window, hold locks, consume a replication slot that backs up the source log, or alter source configuration.
- **Security or privacy**: profiling output would carry real values from a personal, health, or cardholder column, restricted data would be copied into a lower-trust environment to be profiled, or a column's sensitivity cannot be established and it is about to be treated as unrestricted.
- **Source conflict**: the live schema and the data dictionary disagree about a column a decision depends on, or two systems report different totals for the same entity, and silently preferring the reachable one launders a guess into a join key.
- **Release integrity**: a key would be recorded as unique, a source as change-feed capable, or a column as non-sensitive without the query, configuration, or review that establishes it.
- **Connector unreachable**: the source, its replica, its catalog, or its change-feed configuration exists and cannot be read.

An unknown historical growth rate, an unprofiled low-traffic table, and an unanswered semantic question are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`data-contract-desk` is next and needs the field set with real types, the semantics the schema does not carry, and the list of behaviors that are habit rather than commitment. `ingestion-pipeline-desk` needs the watermark candidates with their trustworthiness, the deduplication key, the delete behavior, and the extraction window. `data-modeling-desk` needs the grain, the natural key, and the cardinality that decides where a fan-out will occur. `data-quality-desk` needs the observed null rates and ranges as the derivation basis for thresholds. `data-governance-access-desk` and `data-retention-lifecycle-desk` both inherit the column classification, and neither will re-derive it.

## Quality bar

Good profiling is uncomfortable reading. It says the declared primary key has duplicates, gives the count, and names the reactivation pattern that produces them. It says the modification timestamp does not move when the nightly bulk job runs, so it is not a safe watermark, and it says how that was established. It separates what the source will support from what the source team is willing to allow, because those are different constraints with different owners. It classifies the free-text column that carries customer names even though nothing in the schema hints at it. And it is honest about scope: a profile computed over one recent partition says so, because a uniqueness result from a single day is not a uniqueness result.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
