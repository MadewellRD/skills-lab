# Data Command Desk

Source Markdown suite for data engineering and analytics engineering. The subject is the path a fact takes from the system that records it to the decision that consumes it: how it is sourced, what the producer committed to, how it is modeled, where it lands, how it is transformed and scheduled, what establishes that it is correct, who is permitted to see it, what it costs to keep, and what happens when it turns out to be wrong.

Application code and repository work belong to the SDLC suite. Service reliability and paging for the systems running the pipelines belong to the SRE suite. Feature stores, training sets, and evaluation data belong to the AI Engineering suite. This suite owns the data itself.

## Desks in workflow order

- `data-command-desk.md` (orchestrator)
- `data-product-definition-desk.md`
- `source-system-profiling-desk.md`
- `data-contract-desk.md`
- `data-modeling-desk.md`
- `warehouse-lakehouse-architecture-desk.md`
- `ingestion-pipeline-desk.md`
- `streaming-pipeline-desk.md`
- `transformation-layer-desk.md`
- `batch-orchestration-desk.md`
- `data-quality-desk.md`
- `data-observability-desk.md`
- `lineage-catalog-desk.md`
- `metric-semantic-layer-desk.md`
- `analytics-enablement-desk.md`
- `data-governance-access-desk.md`
- `data-retention-lifecycle-desk.md`
- `data-migration-desk.md`
- `data-platform-cost-desk.md`
- `data-incident-response-desk.md`

## Workflow backbone

```text
data product definition
  -> source system profiling
  -> data contract
  -> data modeling
  -> warehouse and lakehouse architecture
  -> ingestion pipeline
  -> streaming pipeline
  -> transformation layer
  -> batch orchestration
  -> data quality
  -> data observability
  -> lineage and catalog
  -> metric and semantic layer
  -> analytics enablement
  -> governance and access
  -> retention and lifecycle
  -> migration
  -> platform cost
  -> data incident response
```

The chain is ordered by packet dependency, not by calendar. Few workflows need every stage: a metric dispute does not need a storage architecture stage, and a cost review does not need a contract stage. One entry point ignores the order entirely, because bad data already reaching consumers enters at data incident response wherever it started. The orchestrator selects the stage path, carries the `data_packet`, and records every skip with its reason.

Two dependencies are load-bearing rather than conventional. Everything downstream of modeling assumes a declared grain, because an undeclared grain double counts the moment a second dimension joins. Everything in quality, observability, governance, retention, and incident response assumes lineage at some granularity, because blast radius is a graph traversal rather than a recollection.

## How to start

Ask the command desk for the outcome, not the stage. Name the dataset, pipeline, or metric, say what state the platform is in (greenfield, steady, mid-backfill, mid-migration, schema change in flight, or a live bad-data incident), and say how far the change reaches (one model, the marts below it, a published metric, an external report, a feature table, or the whole platform). The orchestrator classifies the request, starts at the earliest desk whose inputs are satisfied, and continues through the stages the outcome needs.

Examples: "model a subscription revenue mart and tell me which measures are non-additive", "our nightly load duplicates rows whenever it retries, make it idempotent and reconcile it against the source", "finance and growth report different active user counts, work out which definitions are in play and who owns each", "we need to delete one customer everywhere, find every copy including exports and snapshots", "warehouse spend doubled last month, name the workloads that caused it", "the revenue dashboard has been wrong since Tuesday, scope who consumed it".

This suite designs, models, plans, and reconciles. It does not execute a write against production data, run a backfill, alter a live schema, grant access, or publish a restated figure; it prepares the exact change with its blast radius, reconciliation, and rollback, and stops at the gate.

## Suite references

- `references/suite-workflow-contract.md`: continuity rule, action boundary, operating modes, the full `data_packet` field set, source discipline, the ordered sequences for destructive operations and for deletion under retention, halt format, parallel surface, and cross-suite boundaries.
- `references/stage-contracts.md`: per-desk inputs, owned outputs, and handoff target.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.
