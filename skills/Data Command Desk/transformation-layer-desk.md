---
name: transformation-layer-desk
description: design the layered sql transformation stack from staging through intermediate to marts, covering materialization and incremental strategy with merge keys and lookback windows, deduplication and record selection, slowly changing dimension implementation with validity windows, late arriving fact handling, unit timezone and currency normalization, null versus unknown versus not applicable, the model dependency graph, and which models are safe to backfill in parallel. use for elt model design, incremental model strategy, scd2 implementation, and transformation refactors.
---

# Transformation Layer Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the transformation artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a model name, a column, a merge key, a lookback window, a row count, or a dependency edge.

## Role

This desk turns landed data into the modeled shape, and it owns the design of that path rather than the individual statement. It covers the layered stack with a stated responsibility per layer, typically a staging layer that renames, casts, and does nothing else, an intermediate layer that carries joins and business logic, and marts that expose a declared grain; materialization and incremental strategy per model including the merge key, the update window, and the reason a re-run does not duplicate; deduplication and the record-selection rule where a source emits several versions of a key; slowly changing dimension implementation with its validity window logic; handling of facts that arrive for dimension members that did not exist yet; unit, timezone, and currency normalization performed once at a boundary rather than repeated in every query; null, unknown, and not-applicable kept distinct rather than collapsed into one another; the dependency graph across models; the test hooks each model exposes to the quality stage; and the explicit statement of which models are safe to backfill in parallel and which must be reprocessed in event-time order.

That last item is not a performance note. A parallel backfill of a type two dimension produces overlapping validity windows that no later run repairs.

## Use when

- A new layer of models is being designed, or an existing stack has no stated responsibility per layer and business logic has spread into staging.
- An incremental model is duplicating rows, missing late updates, or diverging from what a full refresh would produce.
- A slowly changing dimension needs implementing and the validity window convention has not been fixed.
- Facts arrive before their dimension members and are currently being dropped by an inner join or assigned to a null key.
- Currency, timezone, or unit conversion is being repeated in dashboards and giving different answers in different places.
- A backfill is planned and nobody has established which models are order dependent.

## Do not use when

- The target grain, keys, and slowly changing type per attribute have not been decided. That is `data-modeling-desk`, and implementing an undeclared grain is how a fan-out ships.
- The subject is landing raw data and the boundary behavior. That is `ingestion-pipeline-desk`.
- The subject is scheduling, sensors, retries, and pool contention. That is `batch-orchestration-desk`.
- The subject is the assertions that validate the output rather than the logic that produces it. That is `data-quality-desk`.
- The subject is the metric expression exposed to consumers on top of the marts. That is `metric-semantic-layer-desk`.

## Required evidence

- The landed data with its ingest metadata, dedup key, and drift behavior from the ingestion stage, including whether duplicates are visible to this layer.
- The target model with its declared grain, keys, per-attribute slowly changing type, and late-arriving policy from the modeling stage.
- The contract semantics that must survive the transformation: units, timezone convention, currency basis, null meaning, and enum domains.
- The materialization options and concurrent-writer behavior the storage architecture permits, plus the layer policy for what a table may do.
- The freshness target the product carries, which bounds how much a model may reprocess per run.
- The existing model code and its dependency graph where a stack already exists, along with the run durations and any known full-refresh divergence.

## Workflow

**Outcome.** A transformation design a builder can implement: the layer responsibilities and the promotion rules between them, per model a materialization and incremental strategy with merge key, incremental predicate, and lookback window, the deduplication and record-selection rule, the slowly changing dimension implementation with its validity convention, the late-arriving handling, the normalization boundary for units, timezone, and currency, the null semantics, the dependency graph, the test hooks each model exposes, and the parallel-safety classification for backfill.

**Grounding.** Every column referenced comes from the information schema, the landed layout, or an agreed contract. Incremental predicates use a column the ingestion stage actually populates, since an incremental filter on a timestamp the source does not maintain produces a model that succeeds nightly and quietly stops picking up updates. Where a full refresh and the incremental path are already known to disagree, record the divergence and its size rather than assuming the incremental path is correct because it is the one that runs.

**Constraints.** Each layer states what it may and may not do, because business logic in staging is the reason nobody can tell where a number is computed. Every incremental model states its merge key, the predicate that bounds a run, the lookback that absorbs late updates, and the reason a re-run converges on the same rows rather than adding to them; a model whose incremental output can differ from its full refresh states the divergence and its cause instead of hiding it. Deduplication states the ordering that selects the surviving record, and the tie-break when the ordering column ties, since a nondeterministic selection makes the model irreproducible. Slowly changing dimensions use a half-open validity interval so adjacent versions neither overlap nor leave a gap, with a stated current-row indicator and a stated behavior for a late correction that lands inside an existing window. Late-arriving facts are handled by an explicit rule, generally an inferred dimension member with unknown attributes to be enriched later, and never by an inner join that silently discards the fact. Units, timezone, and currency are normalized once at a named boundary, with the source value retained alongside the normalized one and, for currency, the rate and the rate date carried so a figure can be reproduced. Null, unknown, and not-applicable are represented distinctly, because collapsing them makes a coverage question unanswerable afterwards. Order-dependent models are named explicitly: slowly changing dimensions, accumulating snapshots, running totals, sessionization, and anything whose output depends on the previously processed partition.

**Parallel surface.** Independent models within a layer, independent staging models across sources, and independent normalization and semantic reviews fan out safely for authoring. Two carve-outs are physical rather than stylistic and are stated in `references/suite-workflow-contract.md`. Execution follows the dependency graph, so a model with upstream references cannot be built before them no matter how independent the files look. And backfill across partitions parallelizes only for models this desk has classified as partition-independent and idempotent; the order-dependent set is reprocessed in event-time order. The aggregate runs once after the fan-out returns: the dependency graph itself, the cross-model grain review that catches two models at different grains being joined downstream, and the parallel-safety classification, which is a property of the set rather than of any one model.

**Acceptance bar.** A builder can implement each model without asking what a row means or which key merges. Every incremental model states its merge key, lookback, and convergence reason. Every slowly changing dimension states its validity convention and its late-correction behavior. Every model carries the test hooks the quality stage will attach to. The backfill classification names the order-dependent models explicitly rather than declaring the set safe.

## Outputs

A complete run delivers this set:

- `transformation-architecture.md`: layer responsibilities, promotion rules, naming and placement conventions, and what is explicitly not allowed in each layer.
- `model-specifications.md`: per model the purpose, declared grain, source references, materialization, incremental strategy with merge key, incremental predicate, and lookback, plus the full-refresh divergence where one exists.
- `dedup-and-record-selection.md`: per source the version-selection rule, the ordering and tie-break, and the evidence that the key is unique at the stated grain.
- `scd-implementation.md`: the validity window convention, current-row indicator, change-detection basis, late-correction behavior, and the hash or comparison that decides a new version is warranted.
- `late-arriving-policy.md`: the inferred-member rule for facts ahead of dimensions, the enrichment path when the real member arrives, and whether prior facts are restated or left as recorded.
- `normalization-rules.md`: the unit, timezone, and currency boundary with the retained source values, the rate and rate-date carriage, and the null, unknown, and not-applicable representation.
- `model-dependency-graph.md`: the edges with their basis, the critical path to the freshness target, and the models with no downstream consumer.
- `backfill-parallel-safety.md`: the partition-independent and idempotent set, the order-dependent set with the reason for each, and the reprocessing order the second set requires.
- `transformation-downstream-handoff.md`: what `batch-orchestration-desk` inherits, including the dependency graph, expected runtimes, and the completeness signal each model can emit.

Depth standard: an artifact is complete when a builder or {{CODING_AGENT}} could implement the model set from it without a follow-up round trip. An incremental model without a merge key, or a slowly changing dimension without a validity convention, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the landed schema, the existing model code, or the catalog cannot be read, the run delivers `transformation-connector-diagnostic.md` naming each unreachable source and the model claims that depend on it. SQL is not written against a schema nobody read.

Anti-fabrication guard: this desk produces the artifact with the worst failure economics in the suite, which is a query that references a column that does not exist under a name that looks exactly like one that would. It does not error usefully; in the common case it errors immediately, and in the expensive case a plausible column really does exist, holds something else, and the model runs green for a quarter. So every table and column in every expression is taken from the information schema, the landed layout, or an agreed contract, and a model built on a column that is only proposed is marked as blocked on that column rather than written speculatively. Merge keys are keys the profile measured as unique at the stated grain, not columns whose name suggests identity. Row counts, runtimes, and full-refresh divergences name the run or query that produced them, and an unmeasured runtime is written as unmeasured. Sample rows are not fabricated to demonstrate a transformation, because a fabricated row copied into a fixture becomes an expectation, and the expectation then fails against real data while looking authoritative. And a model is classified as safe to backfill in parallel only after its order dependence was actually considered; the default classification is order dependent, since that error is recoverable and the reverse one is not.

## data_packet fields to update

- `models[]` with `name`, `layer`, `pattern`, `grain`, `keys`, `materialization`, `incremental_strategy`, `late_arriving_policy`, `idempotent_rerun`, and `column_basis`
- `models[].idempotent_rerun` left as `unproven` where convergence rests on intent rather than on a measured key
- `pipelines[]` entries of kind `transformation` with their dependency basis and expected runtime
- `quality_checks[]` seeded as test hooks per model, with `expression` and `threshold` left for `data-quality-desk` to derive
- `data_risks[]` for full-refresh divergence, nondeterministic dedup ordering, and order-dependent models currently backfilled in parallel
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a logic change would restate figures a consumer already published, a grain would change on a model with named downstream dependents, or a historical rebuild would rewrite validity windows over reported periods.
- **Production or destructive**: the next action would run a full refresh over a live table, replace a model's target, rebuild a slowly changing dimension's history, or execute a backfill over partitions consumers are reading.
- **Security or privacy**: a transformation would carry a restricted column into a broader-access layer, denormalize a personal identifier into a mart with wider entitlements, or produce a sample or test fixture containing real restricted records.
- **Source conflict**: the landed data, the contract, and the model's expectations genuinely disagree about a key or a unit, and resolving it silently would bake a wrong conversion into every figure the model produces.
- **Release integrity**: a model would be recorded as idempotent, as grain-conformant, or as agreeing with its full refresh without the key evidence or the comparison that establishes it.
- **Connector unreachable**: the landed schema, the existing model code, or the run history needed to design the incremental strategy exists and cannot be read.

An unmeasured typical runtime, an undecided naming convention, and an unenriched inferred member are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`batch-orchestration-desk` is next and needs the dependency graph, the expected runtimes, the completeness signal per model, and the backfill parallel-safety classification that bounds catch-up concurrency. `data-quality-desk` needs the test hooks, the declared grain for uniqueness assertions, the enum domains for accepted values, and the normalization boundary so a distribution check is written against the normalized value. `metric-semantic-layer-desk` needs the mart grain and the normalized units and time basis the metric is measured on. `lineage-catalog-desk` needs the model references from which column-level lineage is parsed. `data-incident-response-desk` inherits the backfill classification, since a correction under time pressure is exactly where an order-dependent model gets reprocessed in parallel.

## Quality bar

Good transformation design reads like it has been burned before. Staging does nothing but rename and cast, so there is one place to look when a number is wrong. Every incremental model can say why re-running it converges, in terms of a key rather than of intent, and says how far its lookback reaches for late updates. Slowly changing dimensions use half-open intervals, and the document says what happens when a correction lands inside an existing window, because that is the case that produces overlaps. Currency carries its rate and rate date, so a figure can be reproduced a year later when the rate table has moved. Null, unknown, and not-applicable stay distinct, since collapsing them is irreversible and the question that needs them always arrives later. And the parallel-safety list names the order-dependent models explicitly, because the day someone needs that list is the day they are backfilling under pressure and will otherwise assume the whole set is safe.
