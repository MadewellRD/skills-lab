---
name: data-migration-desk
description: plan data platform migration covering scope and what is deliberately retired rather than carried, dual-run design, parity reconciliation across row counts control totals and metric values with a stated tolerance, historical backfill depth, consumer cutover sequencing, query translation risk in type coercion null handling timezone and rounding, freeze windows, cutover and rollback, and the decommission gate for the legacy platform. use for warehouse migration, lakehouse moves, engine changes, and legacy retirement.
---

# Data Migration Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the migration artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. An unprofiled legacy object is a soft gap and is carried as unassessed; declaring parity from a reconciliation that was never run is a release-integrity halt, because the whole justification for cutting over is that the target produces the same numbers. Never invent row counts, control totals, variance figures, tolerance thresholds, consumer lists, cutover dates, or the state of a dual run.

## Role

Own the move. This desk holds the migration scope stating what moves, what is rebuilt, and what is deliberately retired rather than carried; the dual-run design; the parity reconciliation across row counts, control totals, and metric values with a stated tolerance and the reason for any accepted variance; the historical backfill depth and its justification; the consumer cutover sequence; the translation risks in type coercion, null handling, timezone, and rounding that produce quiet numeric drift; the freeze window; the cutover and its rollback; and the decommission gate.

Two properties separate a data migration from an application migration. The failure is silent and arithmetic: a translated query that runs and returns rows has not passed anything, because the difference between platforms shows up in the fifth decimal place, in the row that had a null, and in the aggregate that crossed a day boundary in a different timezone. And the migration is not finished when the data lands, it is finished when the last consumer stops reading the legacy path, which is a social problem with a technical gate rather than the reverse; the legacy warehouse that survives three years past its cutover is the standing shape of failure in this domain.

## Use when

- A warehouse, lakehouse, engine, or region move is being planned and the scope, sequence, and parity evidence need designing.
- A dual run is being designed or is already running and needs a reconciliation that would actually detect a difference.
- Parity needs establishing across row counts, control totals, and the metric values consumers care about, with a tolerance that has a reason attached.
- Historical data needs backfilling into a target and the depth needs deciding against what consumers actually query.
- Consumers need sequencing off a legacy path, including the ones reading through exports, extracts, and scheduled reports rather than through the warehouse.
- Query and transformation translation is producing numeric drift and the type, null, timezone, or rounding difference behind it needs isolating.
- A cutover and its rollback need designing, including the freeze window and what is barred during it.
- A legacy platform is due for decommission and the gate needs stating in terms someone can verify.

## Do not use when

- The subject is the target platform's zone design, table format, partitioning, or file sizing. That is `warehouse-lakehouse-architecture-desk`, whose output this desk consumes as the target's constraints.
- The subject is the transformation logic being rebuilt rather than translated. That is `transformation-layer-desk`.
- The subject is a backfill inside one platform to correct data rather than to populate a target. That is `data-incident-response-desk` when it corrects an incident and `ingestion-pipeline-desk` when it loads history.
- The subject is which consumers exist and what they read. That is `lineage-catalog-desk`, whose graph and usage measurement this desk consumes to sequence the cutover.
- The subject is the infrastructure, networking, or account structure the platform runs on. That is a labeled cross-suite handoff to the Cloud Infrastructure suite.

## Required evidence

- The current platform inventory: models, pipelines, schedules, views, stored procedures, semantic layer definitions, and the objects nobody can attribute to an owner.
- Consumer inventory from lineage and query history, including dashboards, exports, extracts, reverse-ETL destinations, external recipients, and the ad-hoc users who will find out at cutover.
- Measured usage per legacy object over a window spanning the longest reporting cycle, which is what separates what must move from what can be retired.
- The target platform's constraints: type system, null and sort semantics, timestamp and timezone handling, numeric precision and rounding behavior, collation, and function coverage.
- Reconciliation sources: the control totals, the system of record figures, and the certified metric values that parity will be measured against.
- Row counts and volumes per object with their collection date, since these move while the plan is written.
- The access policies, masking rules, row-level predicates, and retention obligations that must survive the move.
- Freeze constraints from the business calendar: close periods, regulatory filing dates, and peak trading windows.

## Workflow

**Outcome.** A migration scope naming what moves, what is rebuilt, and what is deliberately retired with the evidence behind each retirement; a dual-run design; a parity reconciliation across counts, control totals, and metric values with tolerances and their justifications; a backfill depth decision; a consumer cutover sequence; a translation risk register with the specific semantic differences that move numbers; a freeze window; a cutover sequence with rollback; and a decommission gate stated so someone can confirm it is met.

**Grounding.** Scope is decided from measured usage rather than from the object inventory, because a migration that carries everything carries the objects that should have died with the legacy platform, and each of them costs its own translation, reconciliation, and cutover. Parity is measured by comparing outputs, not by inspecting translated code; a query that compiles on the target is evidence of nothing. Tolerances come from a stated reason such as a known precision difference or a late-arriving window, and a tolerance chosen because the variance came out at that size is a finding rather than a threshold.

**Constraints.** Parity is reconciled at three levels because each catches a different failure: row counts catch missing or duplicated loads, control totals catch arithmetic and type differences, and metric values as the consumer computes them catch the semantic difference that survives both. Every accepted variance names its cause and its owner, and a variance with no explanation blocks the object rather than being averaged into a passing rate. The translation risk register is specific: decimal against floating point accumulation, integer division, rounding at the half, implicit casts that silently truncate, null propagation in aggregates and joins, empty string against null, null ordering in sorts and window functions, timestamp with and without timezone, session timezone defaults that move a day boundary, week and fiscal boundary functions that start on different days, collation and case sensitivity in join keys, and trailing whitespace in string comparisons. Each entry names where it applies and the reconciliation that would detect it. Backfill depth is justified against measured query history for old periods rather than set to all of it, and the periods not carried are recorded as unavailable with the legacy retention that covers them. Access policies, masks, and row-level predicates are migrated as first-class objects, since they are the controls most reliably lost in a platform move.

**Parallel surface.** Objects to translate, per-object reconciliation, per-consumer cutover preparation, translation risk assessment per pattern, and target backfill of partition-independent models are independent units and fan out safely. The aggregate work runs once after the fan-out returns: composing the parity picture across the whole dual run, ordering the consumer cutover along the dependency graph, deciding the freeze window against the business calendar, and evaluating the decommission gate. Backfill of slowly changing dimensions, accumulating snapshots, running totals, and sessionized models is reprocessed in event-time order rather than fanned out, because a parallel backfill of a type 2 dimension produces overlapping validity windows that no later run repairs.

**Ordered cutover gate.** Cutting a consumer, a pipeline, or the whole platform from legacy to target runs in this order, because the legacy path is the rollback and it stops being one the moment it is retired or stops receiving data:

1. Confirm parity for the objects in scope: counts, control totals, and metric values reconciled against the same period, with every variance either within a justified tolerance or explained and accepted by a named owner.
2. Confirm the rollback is real: the legacy path still loading, still current, and still readable, with the date its currency expires if the source stops feeding it.
3. Obtain the named approval for the blast radius, including the owner of every published metric and external or regulatory report the cutover touches.
4. Enter the freeze: bar schema changes, definition changes, and non-essential loads on both platforms for the window, and state what is exempt.
5. Cut the consumers in dependency order, downstream readers before the assets they read are retired, and hold exports and external deliveries across the switch so no recipient receives one figure from each platform.
6. Reconcile once more after the switch against the same control totals, then release the freeze and record the measured variance, the consumers moved, and the ones still on the legacy path.

Step 2 exists because a rollback nobody confirmed is a plan rather than an option, and the legacy platform commonly stops being current the moment ingestion is repointed. Step 5 is ordered because a mid-cutover consumer reading one figure from each platform produces a discrepancy nobody can attribute, and an external recipient who receives both will ask which one was wrong.

**Acceptance bar.** A reader could state which objects moved, which were retired and on what evidence, what parity was measured at and against which period, every accepted variance with its cause and owner, which consumers are cut and which remain on legacy, and what specifically must be true before the legacy platform is switched off. No object is recorded as at parity without its reconciliation result and date.

## Outputs

A complete run delivers this set:

- `migration-scope.md`: per object, move, rebuild, or retire, with the usage evidence behind each retirement and the owner who accepted it.
- `dual-run-design.md`: what runs on both platforms, for how long, how each side is fed, the cost of running both, and the comparison harness that produces the reconciliation.
- `parity-reconciliation.md`: per object, row counts, control totals, and metric values with the period compared, the measured variance, the tolerance and its justification, and the objects reconciled against nothing.
- `translation-risk-register.md`: each type, null, timezone, rounding, collation, or function semantic difference, where it applies, the numeric drift it produces, and the reconciliation that would detect it.
- `backfill-plan.md`: the history depth carried with its justification from query evidence, the bounds and ordering including which models must be reprocessed in event-time order, and the periods deliberately not carried.
- `consumer-cutover-plan.md`: consumers in dependency order with their owner, their notification, their switch date, and the ones reading through exports and extracts rather than through the warehouse.
- `cutover-and-rollback.md`: the freeze window and its exemptions, the cutover sequence, the rollback trigger and procedure, and the date the legacy path stops being a valid rollback.
- `decommission-gate.md`: what must be true before the legacy platform is retired, stated as checkable conditions, plus the objects and consumers currently failing each condition.
- `migration-downstream-handoff.md`: what `data-platform-cost-desk` inherits, including the dual-run spend and the target's cost shape.

Depth standard: an artifact is complete when an engineer could execute the cutover and an owner could sign the parity result. A parity claim without its period and variance, a retirement without usage evidence, and a rollback without the date it expires are unfinished rather than draft.

When the legacy inventory, query history, or the reconciliation sources exist and cannot be read, the run delivers `migration-connector-diagnostic.md` naming each unreachable source and the scope and parity claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: a migration plan is judged by its parity table, and a parity table is the easiest thing in this suite to write without running anything. Rows reading matched, variance zero, tolerance nought point one percent look like the output of a reconciliation and are indistinguishable from the output of an expectation, and the cutover approval that follows is granted against the appearance. So every parity row carries the period compared, the query or control total it was measured against, the measured variance, and the date it was run, or it reads not reconciled, which is an honest and common state early in a dual run. Tolerances are set from a named cause before the comparison rather than fitted to the result afterwards. Row counts and volumes carry their collection date, since a count taken three weeks ago and presented as current is how a target is declared complete while a month of history is missing. And the consumer list is built from lineage and query history rather than from who was in the kickoff meeting, because the consumer nobody enumerated is the one still reading legacy on the day it is switched off.

## data_packet fields to update

- `migration.scope`, `strategy`, and `dual_run_state`
- `migration.parity_evidence` with the reconciliation, its period, its variance, and its date
- `migration.consumer_migration` with who moved and who still reads the legacy path
- `migration.decommission_gate` stated as checkable conditions
- `reconciliations[]` for every control total and metric compared across platforms
- `backfills[]` for target history loads with bounds, ordering constraint, and approval state
- `data_risks[]` for translation differences, unenumerated consumers, and policies that did not survive the move
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would repoint ingestion, switch a consumer, drop or truncate a legacy object, run a backfill over live partitions, or retire a platform.
- **Missing approval**: cutting over a published metric, an external or regulatory report, or a tier-one data product; accepting a parity variance; or retiring an object a named consumer still reads, needs an owner who has not agreed.
- **Release integrity**: parity would be declared, a dual run reconciled, or a decommission gate satisfied without the reconciliation evidence and its date, or a rollback would be presented as available without confirming the legacy path is still current.
- **Security or privacy**: masking, row-level, or column-level policies would not survive the move, restricted data would land in a target zone with a wider reader set, or production data would be copied into a non-production target for testing.
- **Source conflict**: legacy and target genuinely disagree on a figure beyond tolerance and the cause is unresolved, which is the finding rather than an obstacle to routing around.
- **Connector unreachable**: the legacy inventory, query history, target metadata, or the reconciliation sources needed to establish scope or parity exist and cannot be read.

An unassessed legacy object, an unknown object owner, an unmeasured volume, and an undocumented historical schema change are soft gaps. Name them, label the assumption, and continue. The parity evidence requirement, the rollback confirmation, and the approval boundary on published and regulatory figures are never relaxed to hold a cutover date.

## Downstream handoffs

`data-platform-cost-desk` is next and needs the dual-run spend, the target's cost shape, and the retirement date that ends the double bill. `data-quality-desk` receives the checks that must exist on the target before it can carry a consumer. `data-observability-desk` receives the monitors that must be rebuilt on the target, since a migrated pipeline commonly arrives with none. `data-governance-access-desk` receives every policy that must be reapplied and any that did not survive translation. `metric-semantic-layer-desk` receives metric values as parity evidence and any definition that changed meaning through translation. `data-incident-response-desk` inherits the dual-run state, since an incident during a dual run has two candidate sources and one of them may be correct. Send infrastructure, networking, and account structure for the target platform to the Cloud Infrastructure suite as a labeled cross-suite handoff.

## Quality bar

Good migration work is opinionated about scope and rigorous about parity. It retires objects with usage evidence rather than carrying the whole inventory forward, and it says who accepted each retirement. Its parity table is a measurement record with periods, variances, and dates, and its tolerances have causes. The translation risk register names actual semantic differences rather than warning that platforms differ. The cutover sequence moves consumers in dependency order and holds external deliveries across the switch. The rollback has an expiry date, because the legacy path stops being a rollback long before anyone turns it off. And the decommission gate is written as conditions a person can check, so the legacy platform is retired on evidence rather than on the fact that everyone has stopped talking about it.
