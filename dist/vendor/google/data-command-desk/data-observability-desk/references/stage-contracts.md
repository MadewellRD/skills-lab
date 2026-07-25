# Data Stage Contracts

One entry per desk in the suite: what it requires on input, what it owns on output, and where it hands the `data_packet`. The orchestrator uses these contracts to route; each member desk uses its own entry as the acceptance boundary for "this stage is done."

## Default sequence

```text
data-product-definition
  -> source-system-profiling
  -> data-contract
  -> data-modeling
  -> warehouse-lakehouse-architecture
  -> ingestion-pipeline
  -> streaming-pipeline
  -> transformation-layer
  -> batch-orchestration
  -> data-quality
  -> data-observability
  -> lineage-catalog
  -> metric-semantic-layer
  -> analytics-enablement
  -> data-governance-access
  -> data-retention-lifecycle
  -> data-migration
  -> data-platform-cost
  -> data-incident-response
```

The chain is ordered by packet dependency, not by calendar. A request that starts mid-chain starts at the earliest desk whose inputs are already satisfied, and a live data incident enters at `data-incident-response-desk` regardless of what sits upstream of it.

Two dependencies are load-bearing rather than conventional. Everything downstream of modeling assumes a declared grain, because an undeclared grain double counts as soon as a second dimension joins. Everything in quality, observability, governance, retention, and incident response assumes lineage at some granularity, because blast radius is a graph traversal rather than a recollection.

## Stage completion rule

Every desk emits: source facts with attribution, decisions, its artifact set, the packet fields it updated, assumptions labeled where they were used, open questions, halt conditions, and next-stage readiness. Provenance travels with every number and every schema object. Unmeasured stays unmeasured in the packet, and a column that was inferred from a naming convention is recorded as inferred rather than as present.

---

## data-command-desk

- **Requires**: the user request, the target outcome, the operating posture, the blast radius the work reaches, and whatever connector access exists for warehouse metadata, catalog, orchestrator, schema registry, monitoring, BI usage, and billing.
- **Owns**: request classification across surface, posture, and blast radius; stage path selection; packet initialization and carriage; adjudication of conflicts between what the catalog says and what the warehouse contains; the workflow-level record; and the cross-suite handoff decision.
- **Hands to**: the earliest member desk whose inputs are satisfied, then each successive stage until the target outcome is reached or a hard halt applies.

## data-product-definition-desk

- **Requires**: the consuming question or decision, the named consumers and how they read the data, existing dashboards or reports that already answer part of it, service or contractual commitments the output feeds, and any tiering standard the organization already applies.
- **Owns**: the data product definition stated as the decision it serves rather than as the table it produces; the consumer inventory including downstream systems and external recipients; the output port and its interface; freshness, completeness, and accuracy targets with the consumer conversation that set them; criticality tier and owner; the regulatory or contractual use that raises the evidence bar; and the explicit statement of which existing assets already answer this question, so the run does not add a fourth table that computes the same thing.
- **Hands to**: `source-system-profiling-desk`.

## source-system-profiling-desk

- **Requires**: the candidate source systems, read access or an existing profile, the source schema, and the extraction constraints the owning team imposes.
- **Owns**: the profile per source, covering grain, candidate and actual primary keys, uniqueness violations, null rates and their distribution, cardinality, value ranges and outliers, encoding and type surprises, and the columns whose meaning the schema does not carry; the extraction pattern the source can actually support, including whether change data capture is available and whether deletes are hard, soft, or absent; arrival cadence, expected lateness, and out-of-order behavior; volume and growth against the extraction window; the load a full extract would place on the source and the constraint that bounds it; and the classification of every column carrying personal, health, cardholder, or otherwise restricted data, recorded here because every later stage inherits it.
- **Hands to**: `data-contract-desk`.

## data-contract-desk

- **Requires**: the profiled source shape, the consumer expectations from the data product definition, the producing team, the schema registry or repository holding the current schema, and the change history of that schema.
- **Owns**: the contract per producer-consumer pair, covering the field set, types, nullability, units, timezone, currency, enum meanings, and the semantics the schema cannot express; the compatibility mode and the enforcement point that actually rejects a violation, distinguished from the mode a document claims; the breaking change policy, notification path, and deprecation window; schema evolution rules for additive, widening, narrowing, rename, and drop, each with its downstream effect; the versioning and coexistence strategy while consumers migrate; and the honest list of contracts that are implied by habit rather than agreed with the producer.
- **Hands to**: `data-modeling-desk`.

## data-modeling-desk

- **Requires**: the profiled sources with keys and cardinality, the agreed contracts, the consuming questions and the dimensions those questions slice by, and the history requirements the consumers stated.
- **Owns**: the conceptual and logical model with entities, relationships, and cardinality; the declared grain of every fact, written as one row per something; the fact classification across transaction, periodic snapshot, and accumulating snapshot; dimension design including conformed dimensions, slowly changing type per attribute with its effective dating, degenerate dimensions, junk dimensions, and role-playing dates; natural key and surrogate key strategy including how a missing key is represented rather than silently dropped; bridge or factless bridge handling for many-to-many relationships; the late-arriving fact and late-arriving dimension policy; the additivity of every measure; and the modeling decisions that were rejected with the reason, so the next reader does not relitigate them.
- **Hands to**: `warehouse-lakehouse-architecture-desk`.

## warehouse-lakehouse-architecture-desk

- **Requires**: the logical model with grain and expected volumes, the query patterns and concurrency the consumers generate, the retention and history requirements, and the platform capabilities and constraints the organization already operates under.
- **Owns**: the zone or layer architecture and what a table is allowed to do in each layer; the table format and the transactional guarantees it provides; partitioning chosen against the predicates that are actually filtered on, with the cardinality that makes a partition key wrong; clustering or sort strategy; file sizing and compaction policy including the small file problem the streaming path creates; snapshot and time travel retention, which is also the recovery window every destructive operation depends on; workload isolation between ingestion, transformation, and query compute; the catalog of record and how table metadata is registered; and the physical decisions that constrain later cost work, stated as constraints rather than as preferences.
- **Hands to**: `ingestion-pipeline-desk`.

## ingestion-pipeline-desk

- **Requires**: the extraction pattern the source supports, the contract and its enforcement point, the landing zone design, the freshness target, and the backfill history the product needs.
- **Owns**: the ingestion design per source, covering extraction pattern and the watermark or high-water mark that bounds a run; change data capture handling including snapshot plus stream stitching, delete propagation, and out-of-order change records; idempotency and the deduplication key that makes a re-run safe; landing layout and the raw record preserved unmodified for replay; schema drift handling at the boundary, including whether an unexpected field lands, quarantines, or fails the run; error handling with dead letter and quarantine paths and who reads them; rate limits, pagination, and the extraction window the source owner allows; the historical backfill plan and its bounds; and the reconciliation that compares landed counts against the source.
- **Hands to**: `streaming-pipeline-desk`.

## streaming-pipeline-desk

- **Requires**: the event schemas and their contract state, the ordering and latency requirements, the topic or stream topology, and the downstream consumers of the stream including any that also read the batch path.
- **Owns**: event time versus processing time semantics and which one the business question actually needs; partition key selection and the ordering guarantee it buys or forfeits; windowing, watermarks, allowed lateness, and the explicit decision about what happens to data that arrives past it; delivery semantics stated as what the consumer observes rather than as a configuration flag, including the idempotency or transactional write that makes effectively-once real; state store design, keyed state size, checkpoint interval, and recovery time from checkpoint; consumer lag targets and the rebalancing behavior under scale changes; retention and compaction on the stream, which bounds how far a replay can go; the replay procedure and what a replay does to downstream state; and the reconciliation between the streaming path and the batch path where both exist.
- **Hands to**: `transformation-layer-desk`.

## transformation-layer-desk

- **Requires**: the landed data, the target model with its declared grain, the contract semantics, the materialization constraints from the storage architecture, and the freshness target the product carries.
- **Owns**: the layered transformation design from staging through intermediate to marts, with a stated responsibility per layer; materialization and incremental strategy per model, including the merge key, the update window, and why a re-run does not duplicate; deduplication and the record-selection rule where a source emits multiple versions of a key; slowly changing dimension implementation with the validity window logic; handling of late-arriving facts against dimensions that did not exist yet; null, unknown, and not-applicable representation kept distinct rather than collapsed; unit, timezone, and currency normalization stated once at the boundary rather than repeated per query; the dependency graph across models; the test hooks each model exposes to the quality stage; and the explicit statement of which models are safe to backfill in parallel and which must be reprocessed in event-time order.
- **Hands to**: `batch-orchestration-desk`.

## batch-orchestration-desk

- **Requires**: the transformation dependency graph, the ingestion schedules and their arrival variability, the freshness targets, the compute limits, and the run history where it exists.
- **Owns**: the schedule and trigger design, including data-aware triggering where a downstream job waits for data to exist rather than for a clock; the dependency graph as the orchestrator actually enforces it, distinguishing a task that succeeded from a task that produced data; sensors, arrival timeouts, and the behavior when a source is late; retry policy with backoff and the classes of failure that should not retry; concurrency pools and the queueing behavior at peak; SLA definition, the miss condition, and who it notifies; catch-up and backfill controls with partition bounds and a concurrency cap; run isolation so a backfill does not contend with the scheduled run; and the failure pattern from run history, separating chronic flakiness from real breakage.
- **Hands to**: `data-quality-desk`.

## data-quality-desk

- **Requires**: the models with their grain and keys, the contract expectations, the consumer quality targets, the reconciliation sources available, and any historical test results.
- **Owns**: the check set per asset with the actual assertion written out, covering freshness, volume, uniqueness at the declared grain, not-null, referential integrity, accepted values, distribution and drift, and business rules that encode what the consumer means by correct; thresholds with the derivation that justifies them rather than a round number; the blocking versus warning decision per check and what a blocking failure does to the pipeline and to the downstream consumer; quarantine design for rows that fail without failing the run; reconciliation against the system of record with its tolerance and the reason the tolerance is acceptable; the coverage map showing which assets and which columns have no check at all; and the separation between checks that have actually run and checks that exist only in a file.
- **Hands to**: `data-observability-desk`.

## data-observability-desk

- **Requires**: the check set and its severity routing, the pipeline and orchestration run history, the freshness targets from the data products, the lineage available, and the alerting destinations and their owners.
- **Owns**: the monitor set for freshness, volume, schema drift, distribution, job failure, and consumer lag, with the configured condition rather than the category; the routing decision per monitor across page, ticket, channel, and dashboard only, tied to whether a human action follows; lineage-aware grouping and suppression so one upstream failure produces one alert rather than forty downstream ones; detection coverage measured against how incidents were actually found, naming the incidents a consumer reported before any monitor fired; the noise review that names monitors firing without action and monitors that have never fired; time to detection and time to resolution where the history supports computing them; and the ownership record that says who receives each signal, with the unowned monitors named.
- **Hands to**: `lineage-catalog-desk`.

## lineage-catalog-desk

- **Requires**: the transformation code and its dependency graph, orchestrator metadata, query history, BI and export inventories, and the existing catalog or glossary state.
- **Owns**: the lineage graph at the granularity the evidence supports, with column-level edges where SQL parsing provides them and table-level where it does not, each edge attributed to how it was derived; the gaps the graph does not see, which in practice are hand-written jobs, notebooks, scheduled exports, spreadsheet extracts, and reverse-ETL destinations; impact analysis in both directions, upstream to find what a broken number depends on and downstream to find who consumes it; catalog registration with steward, description, and certification state; the business glossary and its mapping to physical columns; usage measured from query history rather than assumed from importance; deprecation and tombstoning of assets nobody reads; and the honest coverage figure stating what share of assets the graph actually covers.
- **Hands to**: `metric-semantic-layer-desk`.

## metric-semantic-layer-desk

- **Requires**: the marts and their grain, the existing metric definitions wherever they live including BI tools and ad-hoc queries, the owners who can adjudicate a definition, and the reports the metrics feed.
- **Owns**: the metric definition set with the actual expression including filters, exclusions, and denominator; the entity, dimension, and measure model that the semantic layer exposes; grain validity and the dimensions a metric may be sliced by without becoming wrong; additivity classification and the aggregation rule for semi-additive and non-additive measures; the time basis, timezone, and fiscal calendar the metric is measured on; the reconciliation of competing definitions of the same name, preserved as separate definitions with their sources until an owner adjudicates rather than merged into one; certification state and the owner who certified it; versioning and the restatement policy for a definition change that moves a published number; and the metrics whose current value depends on a definition nobody owns.
- **Hands to**: `analytics-enablement-desk`.

## analytics-enablement-desk

- **Requires**: the certified metrics and marts, the consumer personas and their tooling, existing dashboard and query usage, and the support load the analytics team currently carries.
- **Owns**: the consumption design per persona, covering which surface each audience uses and what they are trusted to build; the certified dataset and dashboard set with the questions each answers; self-serve boundaries stating what a consumer may join and what will produce a wrong number if they do; query patterns and the anti-patterns that break the grain; dashboard hygiene including duplicates, orphans, and the reports nobody has opened; the reverse-ETL and operational-analytics path where data returns to an operational system; onboarding material that explains the grain and the joins rather than the click path; the ad-hoc request intake and what converts a repeated request into a modeled asset; and the training and documentation gaps that generate the recurring questions.
- **Hands to**: `data-governance-access-desk`.

## data-governance-access-desk

- **Requires**: the column classifications recorded at profiling, the model and mart inventory, the consumer roles and their legitimate purposes, existing grants and policies, and the regulatory or contractual obligations that bind the data.
- **Owns**: the classification and sensitivity model applied to the physical assets; the access model with roles, groups, and the actual grants, predicates, and masks rather than a description of them; row-level and column-level policy expressions and where they are enforced; masking, tokenization, and pseudonymization decisions including which downstream copies inherit them and which silently do not; purpose limitation and the approved use per audience; the access review cadence, the joiners-movers-leavers path, and the standing grants nobody re-approves; sharing and egress controls covering exports, downloads, external shares, and non-production copies of production data; audit logging of access to restricted assets; and the enforcement evidence per policy, with policies confirmed live separated from policies asserted in a document.
- **Hands to**: `data-retention-lifecycle-desk`.

## data-retention-lifecycle-desk

- **Requires**: the classification and regulatory basis per dataset, the lineage graph including exports and extracts, the storage layout and snapshot retention, backup configuration, and any legal hold in force.
- **Owns**: the retention schedule per dataset with its regulatory, contractual, or operational basis and the source that establishes it; the deletion mechanism and whether it actually removes data given the table format and snapshot window; the propagation map of every derived copy that also holds the record, covering marts, aggregates, extracts, feature tables, exports, and backups; erasure and data subject request handling including how a single subject is located across the copies; archival tiering and what becomes unqueryable when data moves; legal hold and its precedence over scheduled deletion; the residual copies that policy permits to persist with their expiry dates; and the enforcement record stating when each rule was last actually executed, with never-enforced marked as such rather than assumed.
- **Hands to**: `data-migration-desk`.

## data-migration-desk

- **Requires**: the current platform inventory with models, pipelines, and consumers, the target platform and its constraints, the lineage graph, the consumer migration constraints, and the reconciliation sources for parity.
- **Owns**: the migration scope stating what moves, what is rebuilt, and what is deliberately retired instead of carried; the strategy and its sequencing, including the dual-run design where legacy and target produce the same figures side by side; the parity reconciliation that compares row counts, control totals, and metric values across platforms with a stated tolerance and the reason for any accepted variance; historical backfill of the target including how far back and why; the consumer migration plan naming who moves when and who is still on the legacy path; the query and transformation translation risks, particularly type coercion, null handling, timezone, and rounding differences that produce quiet numeric drift; the cutover sequence and its rollback; the freeze window and what changes are barred during it; and the decommission gate that must be satisfied before the legacy asset is retired.
- **Hands to**: `data-platform-cost-desk`.

## data-platform-cost-desk

- **Requires**: the billing or usage export, query history with attribution, the storage inventory, the workload and schedule design, and the freshness and concurrency requirements the spend is buying.
- **Owns**: the spend breakdown across compute, storage, and transfer with the export it came from; the top drivers named as specific workloads, queries, pipelines, or dashboards rather than as categories; attribution of spend to a team, product, or workload, and the share that is unattributable; the efficiency findings that actually move the number, covering partition pruning failures, full scans, exploding joins, over-frequent refresh, over-provisioned or idle compute, small file overhead, redundant materializations, and retained data nobody queries; the cost of freshness stated as what an hourly refresh costs against a daily one, so the trade is a business decision rather than a default; chargeback or showback design; the guardrails and quotas that prevent a single query from consuming a month of budget; and the separation between measured savings and estimated savings.
- **Hands to**: `data-incident-response-desk`.

## data-incident-response-desk

- **Requires**: the failing signal or consumer report, the lineage graph, run history and recent changes to code, schema, and configuration, the quality check results, and the consumer and communication path.
- **Owns**: severity classification based on consumer exposure rather than on how many rows are wrong; containment that stops the bad partition from propagating further, including pausing dependents and holding exports; evidence capture taken before any re-run, covering the affected partitions, the run logs, the failing check output, the upstream payload, and the code and configuration version that produced it; blast radius derived from lineage naming every dashboard, export, feature table, and external recipient that consumed it; the correction decision across backfill, restatement, and withdrawal, with the reconciliation that shows the correction landed; consumer notification including who acted on the wrong figure and what they were told; the restatement record for any published number that changed; and the postmortem with contributing factors, the detection gap that let it run undetected, and action items with named owners.
- **Hands to**: the orchestrator for workflow close, and to `data-quality-desk` or `data-observability-desk` when the incident shows the missing check or the missing monitor that would have caught it.

---

## Cross-suite boundary

These hand outward rather than to another desk in this suite: application code changes, repository work, issue planning, and implementation handoff go to the SDLC suite; service reliability, paging, and production incident command for the systems running the pipelines go to the SRE suite; cloud and warehouse spend policy, commitments, and chargeback governance go to the FinOps suite; privacy program obligations, lawful basis, consent, and data subject request process go to the Privacy suite; audit response and control evidence packaging go to the GRC suite; feature stores, training datasets, and evaluation data go to the AI Engineering suite; the underlying infrastructure goes to the Cloud Infrastructure suite. Label the handoff explicitly so nobody reads those desks as members of this one.
