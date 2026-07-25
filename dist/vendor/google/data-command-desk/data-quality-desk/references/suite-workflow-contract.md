# Data Suite Workflow Contract

## Purpose

This reference defines how the Data Command Desk suite runs as one continuous workflow instead of a set of isolated prompts. Every desk in the suite reads it, updates the `data_packet`, and hands that packet to the next stage.

The subject of this suite is the path a fact takes from the system that records it to the decision that consumes it: how it is sourced, what the producer committed to, how it is modeled, where it lands, how it is transformed and scheduled, what establishes that it is correct, who is permitted to see it, what it costs to keep, and what happens when it turns out to be wrong.

The packet therefore carries schema state and measurement state side by side, because the two things this domain fabricates most easily are a number nobody computed and a column nobody has. Both look identical to a real one on the page.

## Continuity rule

Do not stop with a bare next-desk recommendation when the next stage can be completed from available source facts. Complete the current stage, update the `data_packet`, and continue until the target outcome is reached or a hard halt applies.

A stage is complete when the next desk can act on its output without rediscovering the grain, the keys, the owner, the thresholds, or the evidence behind a number. A stage that emitted headings and deferred their contents is incomplete, because every later stage trusts the packet rather than re-reading the warehouse.

## Operating modes

- `single_stage`: run one desk because the user asked for one specific data artifact, such as a dimensional model, a contract, or a quality check set.
- `workflow_run`: default. Run the stage path the target outcome needs, carrying the packet through each stage.
- `resume`: continue from a prior `data_packet` or a halt-resume prompt, treating `completed_stages` as done rather than redoing them. Re-read any profile, row count, freshness reading, or cost figure whose collection date is stale, because warehouse state moves between readings while the packet does not.
- `halt`: stop on a hard-halt class from `references/halt-taxonomy.md` and emit the halt format below.
- `diagnostic`: the warehouse metadata, catalog, orchestrator run history, schema registry, monitoring history, or billing export cannot be reached, so the run reports reachability and evidence gaps instead of asserting schema, volume, lineage, quality, or cost state.

## Action boundary

This suite produces models, contracts, pipeline and orchestration designs, check sets, policies, retention rules, migration and backfill plans, cost findings, and incident records. It does not execute a write against a production dataset, run a backfill, drop or replace a table, alter a schema, change a schedule, grant access, delete under a retention rule, or publish a restated number. For those, the desk prepares the exact change, its blast radius derived from lineage, its reconciliation, and its rollback, then stops at the gate. The person holding the authority executes.

## Data packet

Every desk preserves and updates this packet. Unknown, unmeasured, unprofiled, and never-reconciled are legitimate values; a plausible number and a guessed column name are not. A field with no source basis stays empty rather than being filled with something that fits the pattern.

```yaml
data_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  current_stage: "stage-name"
  completed_stages:
    - "stage-name"
  skipped_stages:
    - stage: "stage-name"
      reason: "why it was not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  data_surface: "data_product | source_profiling | data_contract | modeling | storage_architecture | ingestion | streaming | transformation | orchestration | quality | observability | lineage_catalog | metric_semantics | analytics_enablement | governance_access | retention_lifecycle | migration | cost | data_incident | unknown"
  operating_posture: "greenfield | steady_state | backfill_in_flight | schema_change_in_flight | migration_dual_run | active_data_incident | post_incident | audit_or_review | freeze | unknown"
  blast_radius: "single_model | one_pipeline | downstream_marts | published_metric | external_or_regulatory_report | ml_feature_store | whole_platform | unknown"
  environment: "development | staging | production | unknown"

  data_products:
    - name: ""
      decision_supported: "what a consumer actually does with it"
      consumers: []                  # named teams, services, dashboards, or external recipients
      output_port: "table | view | topic | file_export | api | bi_model | feature_table | reverse_etl_destination"
      owner: "source-backed owner or unknown"
      criticality: "tier1 | tier2 | tier3 | untiered | unknown"
      freshness_target: "source-backed target or unset"
      freshness_actual: "measured lag with the query or monitor it came from, or unmeasured"
      quality_target: "source-backed target or unset"
      regulatory_use: "financial_report | regulatory_filing | safety | contractual | none | unknown"

  source_systems:
    - name: ""
      kind: "oltp_database | saas_api | event_stream | file_drop | third_party_feed | operational_export | spreadsheet | unknown"
      extraction_pattern: "full_snapshot | incremental_watermark | log_based_cdc | api_pagination | webhook | file_delivery | unknown"
      grain: "what one record represents in the source system"
      primary_key: "declared key, or none declared"
      volume: "measured row count and growth rate with its source, or unmeasured"
      arrival: "cadence, expected lateness, and out-of-order behavior, or unprofiled"
      delete_behavior: "hard_delete | soft_delete | no_deletes | unknown"
      profiling_state: "profiled | partially_profiled | unprofiled"
      classification: "public | internal | confidential | pii | phi | pci | unclassified"
      extraction_constraint: "load window, rate limit, replica lag, licence limit, or none known"

  data_contracts:
    - id: ""
      producer: "team or system that owns the shape"
      consumers: []
      schema_ref: "registry subject, repo path, or none"
      compatibility_mode: "backward | forward | full | none | unenforced"
      enforcement_point: "producer_ci | schema_registry | ingestion_gate | transformation_test | none"
      breaking_change_policy: "source-backed policy or unknown"
      deprecation_window: "source-backed window or unset"
      semantics: "units, timezone, currency, null meaning, and enum meaning that the schema itself does not carry"
      state: "agreed | proposed | implied | violated | unknown"

  models:
    - name: ""
      layer: "landing | bronze | staging | silver | intermediate | gold | mart | semantic"
      pattern: "fact | dimension_scd1 | dimension_scd2 | bridge | periodic_snapshot | accumulating_snapshot | aggregate | normalized | wide_table | data_vault_hub | data_vault_link | data_vault_satellite"
      grain: "one row per <entity per period>, or undeclared"
      keys: "natural key and surrogate key strategy, or unknown"
      materialization: "view | table | incremental | snapshot | materialized_view | streaming_table"
      incremental_strategy: "append | merge | insert_overwrite | delete_insert | none"
      late_arriving_policy: "how late facts and late-arriving dimensions are handled, or undefined"
      idempotent_rerun: "yes | no | unproven"
      column_basis: "catalog, information schema, DDL, or inferred"

  storage_architecture:
    layout: "medallion | layered_warehouse | data_vault | lakehouse_zones | mixed | unknown"
    table_format: "source-backed format or unknown"
    partitioning: "partition keys and the predicate they serve, or none"
    clustering: "clustering or sort keys, or none"
    file_sizing: "target file size and compaction policy, or unmanaged"
    snapshot_retention: "time travel or snapshot window with its source, or unknown"
    compute_isolation: "how ingest, transform, and query workloads are separated, or shared"
    catalog_of_record: "metastore or catalog that governs the tables, or unknown"

  pipelines:
    - name: ""
      kind: "batch_ingest | cdc | streaming | transformation | export | reverse_etl"
      trigger: "schedule, sensor, upstream asset, or event"
      watermark: "the column and boundary that defines a run's scope, or none"
      idempotency: "how a re-run avoids duplicates and partial state, or unproven"
      failure_handling: "retry policy, dead letter, quarantine, or none"
      backfill_procedure: "documented procedure, or none"
      runtime: "measured typical and worst-case duration with its source, or unmeasured"

  streams:
    - topic: ""
      key: "partition key and the ordering guarantee it buys"
      delivery: "at_least_once | at_most_once | effectively_once | unknown"
      time_semantics: "event_time | processing_time | ingestion_time"
      lateness_policy: "allowed lateness and what happens to data past it, or undefined"
      state_store: "keyed state, its size, and its checkpoint interval, or stateless"
      consumer_lag: "measured lag with its source, or unmeasured"
      retention: "topic retention and compaction setting, or unknown"
      replay_safety: "what a replay from an earlier offset does to downstream state"

  orchestration:
    dependency_basis: "how a downstream task learns its upstream produced data, not merely that a task exited zero"
    schedule: "source-backed schedule or unknown"
    sla_definition: "the miss condition and who it notifies, or none"
    concurrency_limits: "pools, slots, or none"
    retry_policy: "attempts and backoff, or platform default"
    backfill_controls: "partition bounds, catch-up behavior, and concurrency cap"
    run_history: "success rate and failure pattern with its source, or unmeasured"

  quality_checks:
    - asset: ""
      check: "freshness | volume | uniqueness | not_null | referential_integrity | accepted_values | distribution | schema_drift | reconciliation | business_rule"
      expression: "the actual assertion, not the category it belongs to"
      threshold: "the value that separates pass from fail, and how it was derived"
      severity: "blocking | warn | observe"
      on_failure: "halt_pipeline | quarantine_rows | alert_only | none"
      last_result: "measured result with the run it came from, or never_run"

  reconciliations:
    - target: "the dataset or figure being reconciled"
      against: "the control total or system of record it is compared to"
      tolerance: "accepted variance and the reason it is accepted"
      result: "measured variance with its date, or not_reconciled"

  monitors:
    - asset: ""
      signal: "freshness | volume | schema | distribution | job_failure | consumer_lag | cost"
      condition: "the threshold or anomaly rule actually configured"
      routing: "page | ticket | channel | dashboard_only"
      owner: "named owner or unknown"
      history: "times fired and whether action followed, or never_fired"

  lineage:
    coverage: "assets with traced lineage over total assets, or untraced"
    granularity: "column_level | table_level | job_level | none"
    derivation: "parsed SQL, orchestrator metadata, query history, or manual assertion"
    known_gaps: []                   # hand-written jobs, notebooks, exports, and BI extracts the graph does not see

  catalog:
    - asset: ""
      registered: "yes | no"
      steward: "named steward or unowned"
      description_state: "documented | stub | absent"
      certification: "certified | uncertified | deprecated"
      usage: "measured query or dashboard usage with its source, or unmeasured"

  metrics:
    - name: ""
      definition: "the actual expression including filters, exclusions, and denominator"
      grain: "the dimensional grain the metric is valid at"
      additivity: "additive | semi_additive | non_additive"
      time_basis: "the date field and timezone the metric is measured on"
      owner: "named owner or unknown"
      certification: "certified | proposed | contested | unknown"
      competing_definitions: "other places the same name is computed differently, with each source"

  access_policies:
    - asset_or_domain: ""
      model: "rbac | abac | row_level | column_level | masking | tokenization | view_only"
      rule: "the actual predicate, mask, or grant"
      subjects: "roles or groups the rule applies to"
      purpose_limitation: "approved use, or none stated"
      enforcement_evidence: "how the rule was confirmed live, or unverified"

  retention_rules:
    - dataset: ""
      basis: "regulatory | contractual | operational | undefined"
      period: "source-backed period or unset"
      deletion_mechanism: "partition_drop | row_delete | crypto_shred | archive_tier | none"
      derived_copies: "downstream tables, exports, BI extracts, feature tables, and backups that also hold it"
      legal_hold: "active | none | unknown"
      last_enforced: "date with its evidence, or never"

  migration:
    scope: "what is moving and what is deliberately staying"
    strategy: "lift_and_shift | rebuild | strangler | dual_run | unknown"
    dual_run_state: "not_started | running | reconciled | cut_over | rolled_back"
    parity_evidence: "the reconciliation that shows legacy and target agree, with its date, or none"
    consumer_migration: "which consumers moved and which still read the legacy path"
    decommission_gate: "what must be true before the legacy asset is retired"

  cost:
    spend_source: "billing export, usage view, or unmeasured"
    compute_vs_storage: "measured split with its source, or unmeasured"
    top_drivers: "the workloads, queries, or pipelines that account for the spend, each with its source"
    attribution: "how spend maps to a team, product, or workload, or unattributed"
    efficiency_findings: "partition pruning, file sizing, materialization choice, idle compute, or unassessed"

  data_incidents:
    - id: ""
      detected_at: "source-backed timestamp"
      detection_source: "monitor | quality_check | consumer_report | reconciliation | manual"
      symptom: "what was wrong with the data, stated as a consumer would see it"
      affected_assets: []
      affected_partitions: "the exact bounds, or unknown"
      downstream_exposure: "dashboards, exports, feature tables, and external recipients that consumed it"
      correction: "backfill, restatement, withdrawal, or none yet"
      consumer_notification: "who was told and when, or none"
      status: "detected | contained | corrected | closed"

  backfills:
    - target: ""
      bounds: "the partition, key, or time range"
      reason: ""
      idempotency_basis: "why re-running is safe for this model, or unproven"
      approval: "named approver, or not obtained"
      reconciliation: "the control total the result is compared to, or none"
      state: "planned | approved | running | reconciled | rolled_back"

  data_risks:
    - risk: ""
      assets_affected: []
      exposure: "what a consumer experiences if it lands"
      current_control: "the control that exists today, or none"
      owner: "named owner or unknown"

  source_facts:
    - fact: "source-backed fact"
      source: "information_schema | table_metadata | query_history | data_profile | catalog | lineage_graph | schema_registry | source_system_schema | orchestrator_run_history | pipeline_logs | test_results | monitor_history | bi_usage_logs | access_logs | billing_export | git_repo | ticket_queue | docs | user | connector | uploaded_file | unknown"
  decisions:
    - "decision made at this stage"
  assumptions:
    - "assumption made to continue, labeled where it was used"
  open_questions:
    - "question blocking later work"
  artifacts:
    - "artifact name or path"
  halt_conditions:
    - "condition that requires stopping"
  ready_to_continue: true
```

## Stage advancement

Advance when the current desk's output would survive being handed to the next desk without a follow-up round trip. `references/stage-contracts.md` states what each desk requires on input and owns on output.

Run only the stages the target outcome needs. A metric definition dispute does not need a storage architecture stage; a cost review does not need a contract stage. Record every skip in `skipped_stages` with its reason, so a later reader can tell a deliberate skip from an omission.

Two dependencies in this chain are load-bearing rather than conventional. Nothing downstream of the modeling stage is meaningful until the grain is declared, because a fact table with an undeclared grain silently double counts the moment a second dimension joins to it. And nothing in the quality, observability, or incident stages is meaningful until lineage exists at some granularity, because blast radius is a graph traversal, not a recollection.

## Source discipline

Read the system's actual state and its documented intent from different places and keep them labeled as such.

Actual state: the information schema, table metadata, and catalog state what columns and tables exist. Data profiles state what the values actually look like, including the null rate and cardinality that the documentation rounds off. Query history states what is actually read and by whom, and it is the honest measure of whether an asset is used. Orchestrator run history and pipeline logs state what actually ran, when, and how often it failed. Test results and monitor history state what was actually checked. The schema registry states what shape a producer actually publishes. Access logs state who actually reads a restricted dataset. The billing or usage export states what is actually spent.

Documented intent: design documents, model specifications, contract documents, runbooks, data dictionaries, glossary entries, retention schedules, and policy documents state what is supposed to exist and who is supposed to own it. Tickets and chat threads are decision context and history, never schema or volume state.

The gap between the two is usually the finding. A data dictionary describing a column that was dropped two quarters ago, a contract with a compatibility mode nothing enforces, a retention schedule that no job implements, a certified metric that three dashboards compute three ways, and a lineage diagram drawn by hand that omits the export feeding the finance spreadsheet are the recurring shape of this domain. Record both sides, attribute both, and preserve the conflict rather than resolving it into whichever source is easier to reach.

Keep source facts separate from assumptions and from inference in every artifact. Never invent table names, column names, data types, join keys, row counts, null rates, freshness lags, partition bounds, test results, lineage edges, metric definitions, owners, retention periods, access grants, or cost figures.

## Halt behavior

The default posture is to proceed with the assumption labeled inline where it was used. Hard halts are justified by consequence, never by uncertainty, and belong to the six classes in `references/halt-taxonomy.md`. Evidence that is merely absent is a soft gap; evidence that exists and cannot be read is a hard halt.

### Ordered sequence for destructive data operations

Backfills over live partitions, restatements of a published figure, table replacement, schema changes that drop or retype a column, hard deletion under a retention or erasure rule, topic replay from an earlier offset, and migration cutover run in this sequence:

1. Establish that the recovery path exists and covers the operation: a snapshot, time travel window, or exported copy whose retention outlasts the change, confirmed before any write.
2. Derive the blast radius from lineage rather than from memory, and obtain the named approval for that radius from the owner of every affected data product, published metric, and external report.
3. Pause the downstream dependents so partial or intermediate state cannot be read, exported, or published while the operation is in flight.
4. Execute against one bounded partition or key range first and reconcile that result against a control total captured before the change.
5. Complete the operation, reconcile the full result against the same control total, then release the pause and record the measured variance, the bounds actually processed, and the consumers notified.

This order is mandated because step 1 is the only evidence that the operation is reversible, snapshot and time travel windows expire on a clock nobody consults under pressure, and step 4 is the only cheap place to discover that the transformation is not idempotent. A number that reaches an external recipient cannot be recalled, only restated, and a restatement costs more credibility than the delay of doing step 2 properly. Do not compress these steps to save a run, and do not reorder them if a later edit makes the list look redundant.

### Ordered sequence for deletion under retention or erasure

Deletion propagates in a specific direction because the copies outlive the original:

1. Enumerate every copy from lineage and from the export inventory: derived models, aggregates, BI extracts, feature tables, reverse-ETL destinations, file exports, and backups or snapshots that still contain the rows.
2. Suppress at the serving layer so nothing further reads the data while deletion is in progress.
3. Delete from the derived assets, then from the system of record.
4. Expire the snapshots, time travel windows, and backups that still hold the deleted rows, and record which of them retain the data until their own expiry.
5. Confirm the absence with a query against each enumerated copy, and record the residual copies that policy allows to persist along with their expiry date.

The direction is mandated because deleting the system of record first orphans the derived copies, a full refresh will not remove rows whose source no longer produces them, and time travel silently resurrects deleted records for the length of its window. An erasure declared complete while a snapshot still holds the rows is a false compliance record, which is worse than an open one.

### Halt format

```markdown
## Workflow Halt

Halt class: <one of the six hard classes>
Current stage: <stage>
Completed stages: <list>
Blocked next stage: <stage>
Consequence if we proceeded: <what would be irreversible, unapproved, exposed, published, or asserted without evidence>
Missing fact or access: <the exact table, column, grant, export, approval, or connector>
Already attempted: <queries run, catalog reads, connectors tried, and what each returned>
Proceeding meanwhile: <reversible work that does not depend on the blocked fact>
Required to resume:
- <specific fact, access grant, or approval, with the owner who can supply it>
Resume prompt:
<copy-paste prompt carrying the current data_packet>
```

A halt that only reports being stuck is incomplete. Name the exact query, catalog entry, permission, export, or approver that unblocks it.

## Parallel surface

Source systems, tables and columns during profiling, models within a layer, pipelines, quality checks, monitors, catalog entries, dashboards, metric definitions under review, access policies, datasets under retention review, and consumers to notify are independent units and are parallel-safe. Connector preflight across warehouse metadata, catalog, orchestrator, schema registry, monitoring, BI usage, and billing is likewise parallel-safe.

The aggregate work is not parallel and runs once, after the fan-out returns: composing the end-to-end lineage graph and the impact analysis over it, rolling freshness up a dependency chain where a mart is only as fresh as its latest input, reconciling competing definitions of the same metric, ranking data risks, attributing cost across shared compute, and deciding the deletion order across copies. A per-table picture assembled in parallel and never composed along the dependency chain is how this domain produces a suite of green tests above a dashboard that has been quietly wrong for a month.

Two carve-outs are physical rather than stylistic. Transformation execution follows the dependency graph, so a model with upstream references cannot be built before them regardless of how independent the files look. And backfill across partitions parallelizes only for transformations that are partition-independent and idempotent; slowly changing dimensions, accumulating snapshots, running totals, sessionization, and any model whose output depends on the previously processed partition must be reprocessed in event-time order, because a parallel backfill of an SCD2 table produces overlapping validity windows that no later run repairs.

## Cross-suite handoffs

Label cross-suite work explicitly rather than implying those desks belong to this suite. Send application code changes, repository work, issue planning, and implementation handoff to the SDLC suite. Send service reliability, paging, on-call, and production incident command for the systems that run the pipelines to the SRE suite. Send warehouse and cloud spend policy, commitments, and chargeback governance beyond the platform findings this suite produces to the FinOps suite. Send privacy program obligations, lawful basis, consent, cross-border transfer, and data subject request process to the Privacy suite. Send audit response, control evidence packaging, and framework mapping to the GRC suite. Send feature stores, training datasets, embeddings, and model evaluation data to the AI Engineering suite. Send the infrastructure the platform runs on to the Cloud Infrastructure suite.

A data incident with a privacy or security dimension belongs to this suite and the Security or Privacy suite at the same time, and the handoff is additive rather than a transfer of command.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model, including context budget, native self-verification, long-horizon continuation, and parallel fan-out, along with the governance invariants that do not relax as models improve.
