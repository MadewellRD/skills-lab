---
name: lineage-catalog-desk
description: build data lineage and metadata covering column-level and table-level lineage from sql parsing, orchestrator metadata and query history, upstream and downstream impact analysis, blast radius, catalog registration and stewardship, business glossary mapping, asset usage from query logs, lineage gaps in notebooks and hand-scheduled exports, and deprecation of unread tables. use when tracing what a change breaks, finding who consumes a dataset, registering assets, or retiring tables nobody reads.
---

# Lineage Catalog Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the lineage and catalog artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A path the graph cannot see is a soft gap and is recorded as a named gap; a query history or catalog that exists and cannot be read is a hard halt, because every impact answer downstream would be an assertion about consumers nobody looked for. Never invent lineage edges, column mappings, steward names, certification state, query counts, last-queried dates, or the existence of a consumer.

## Role

Own the graph and the metadata over it: lineage at the granularity the evidence supports with every edge attributed to how it was derived, the paths the graph cannot see, impact analysis in both directions, catalog registration with stewardship and certification, the glossary mapped to physical columns, usage measured from query history, and the deprecation of assets nobody reads.

Two properties make lineage work different from drawing a diagram. First, an edge is a claim about execution, and the plausible edge and the parsed edge are indistinguishable on the page; a staging model that obviously feeds a mart may in fact feed nothing, because the mart was rewritten against the raw table during an incident and never moved back. Second, the value of the graph is concentrated entirely in its edges, so a graph that covers the warehouse and misses the scheduled export feeding a regulatory return is not partially useful; it is confidently wrong at the one point where the answer mattered.

## Use when

- A schema change, a metric redefinition, a deprecation, or an incident needs its blast radius derived rather than recalled.
- A number is wrong and the upstream path that produced it needs tracing back to a source column.
- Assets need registering in the catalog with a steward, a description, and a certification state, or the catalog has drifted from what the warehouse contains.
- Business terms need mapping to physical columns, because a glossary that defines a term without naming the column it lives in cannot settle an argument.
- Usage needs measuring from query history, to distinguish assets that are read from assets that are merely present.
- Tables, views, or extracts nobody reads are candidates for deprecation and the retirement path needs evidence and a sequence.
- Alert fan-out cannot be grouped because the dependency path between two assets is not in the graph.
- Column-level lineage is needed for a personal-data mapping, so the classification recorded at profiling can be traced to every derived copy.

## Do not use when

- The subject is the transformation logic itself, its materialization, or its dependency structure as code. That is `transformation-layer-desk`; this desk reads that structure and records what it implies about execution.
- The subject is monitor conditions, routing, or detection coverage. That is `data-observability-desk`, which consumes this graph for grouping.
- The subject is what a metric means or which definition is correct. That is `metric-semantic-layer-desk`; this desk supplies which dashboards a definition change would move.
- The subject is dashboard hygiene, certified datasets per persona, or self-serve boundaries. That is `analytics-enablement-desk`, which consumes the usage measurement produced here.
- The subject is retention, erasure, or which copies must be deleted. That is `data-retention-lifecycle-desk`, which consumes the propagation paths this desk traces.

## Required evidence

- The transformation code and its dependency graph, which is the primary source of parsed column-level edges.
- Orchestrator metadata: task dependencies, asset materializations, and run history, which supplies job-level edges where SQL parsing does not reach.
- Query history over a window long enough to include monthly and quarterly workloads, which is the only honest measure of usage and the source of edges that exist only in ad-hoc queries.
- The information schema and catalog state: what tables, views, and columns actually exist, against which the catalog's registration is compared.
- BI tool metadata: dashboards, their underlying datasets, extract schedules, and view counts by user.
- The export and reverse-ETL inventory, including file drops, scheduled reports, and operational destinations that read from the warehouse and leave it.
- The existing catalog, glossary, and data dictionary entries, read as documented intent rather than as state.
- The column classifications recorded at profiling, so restricted data can be traced through the graph.

## Workflow

**Outcome.** A lineage graph at the granularity the evidence supports with each edge attributed to its derivation, an explicit gap register for the paths the graph cannot see, bidirectional impact analysis usable for a real change, catalog registration with steward, description, and certification state per asset, a glossary mapped to physical columns, usage measured per asset from query history, and a deprecation list with the evidence behind each candidate.

**Grounding.** Every edge carries how it was derived: parsed from SQL, read from orchestrator metadata, observed in query history, or asserted by a person. These are not equivalent, and an asserted edge that no parse or run confirms is recorded as asserted. Coverage is stated as a real fraction with its denominator, so a graph covering the modeled warehouse and none of the ingestion path says so rather than reporting a single confident percentage. Usage comes from query and view logs; an asset described as critical by its owner and never queried in the window is recorded with both facts intact, because that disagreement is the finding.

**Constraints.** The gap register is a first-class artifact rather than a caveat, and it names the specific paths this domain always loses: notebooks scheduled outside the orchestrator, hand-written jobs on a server nobody inventories, spreadsheet extracts pulled on a schedule by a person, BI extracts that materialize a copy inside the reporting tool, reverse-ETL syncs that write back into operational systems, and file exports to external recipients. Impact analysis runs in both directions and states which one it is answering, since upstream traversal finds what a broken number depends on and downstream traversal finds who is exposed, and confusing them produces a notification list that omits the people who were harmed. Column-level edges are used where parsing supplies them and table-level is recorded where it does not, rather than presenting a table-level graph as if it resolved columns. Certification is a claim about an owner having accepted the asset, so an asset with no named steward is uncertified regardless of how well it is documented.

**Parallel surface.** Assets, models, dashboards, and export destinations are independent units for extraction, catalog registration, description drafting, and usage measurement, and per-asset parsing fans out safely. The graph composition itself is not parallel and runs once after the fan-out returns, along with the transitive impact analysis over it, the coverage computation, the deduplication of edges arriving from different derivations, and the deprecation ranking. A per-asset metadata sweep that is never composed into a traversable graph produces a catalog that answers what a table is and cannot answer what breaks if it changes, which is the question the stage exists for.

**Ordered gate for retiring an asset.** Deprecating and dropping a table, view, extract, or dashboard runs in this order, because a drop is irreversible past the snapshot window and the reader who needed it is usually the one who queries quarterly:

1. Establish non-use from query history over a window that spans the asset's longest plausible cycle, including month-end, quarter-end, and annual reporting, and check the export and BI inventories separately since those paths often bypass query logs.
2. Announce the deprecation to the identified consumers and to the channel where unidentified consumers would notice, with a date, and record who was told.
3. Tombstone rather than drop: mark deprecated in the catalog, and where the platform supports it, revoke read access or rename so a remaining consumer fails loudly instead of silently reading stale rows.
4. Observe through the announced window, and treat any access attempt as a consumer the evidence missed.
5. Drop only after the window closes with the recovery path confirmed, and record the snapshot or export that could restore it and the date that recovery expires.

Step 3 exists because a silent drop and a silent freeze are indistinguishable to a consumer until a report is already wrong, and step 1 must span the long cycle because the annual reader has no representation in a thirty-day query log.

**Acceptance bar.** A reader could answer, from these artifacts alone, what breaks if a named column changes, who currently consumes a named table including outside the warehouse, what share of assets the graph actually covers and at what granularity, and which assets are candidates for retirement with the evidence behind each. Every edge names its derivation and every usage figure names the log and window it was measured over.

## Outputs

A complete run delivers this set:

- `lineage-graph.md`: the edges with granularity and derivation per edge, the traversal entry points, and the sections of the estate covered at column level against those covered only at table or job level.
- `lineage-gap-register.md`: every path the graph cannot see, what it connects, how it was discovered, and what impact answer is unreliable while it remains unmapped.
- `impact-analysis.md`: bidirectional traversal for the changes actually in scope, naming downstream models, dashboards, exports, feature tables, and external recipients, with the direction stated per answer.
- `catalog-registration.md`: per asset, registration state, steward, description state, certification, and the difference between what the catalog holds and what the information schema contains.
- `glossary-mapping.md`: business terms mapped to physical columns and models, with the terms that map to more than one physical source preserved as ambiguous rather than resolved.
- `asset-usage-and-deprecation.md`: measured usage per asset with its window, the unread and duplicate assets ranked as retirement candidates, and the deprecation sequence and announcement state for each.
- `lineage-downstream-handoff.md`: what `metric-semantic-layer-desk` and the governance, retention, and incident stages inherit, including the coverage figure and the gaps that bound every impact claim.

Depth standard: an artifact is complete when an engineer could run the impact analysis for a real schema change and a steward could accept ownership without asking what the asset contains. A graph with edges and no derivations, a usage figure with no window, and a deprecation candidate with no non-use evidence are unfinished rather than draft.

When query history, orchestrator metadata, the catalog, or BI metadata exists and cannot be read, the run delivers `lineage-connector-diagnostic.md` naming each unreachable source and the edges, usage figures, and impact answers that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: the failure mode here is the obvious edge. A naming convention makes a dependency look established, and a graph drawn from what a warehouse ought to look like reads exactly like one parsed from its code, with the difference surfacing only when a deprecation drops a table an unmapped export still reads. Every edge therefore carries its derivation and inferred edges stay marked as inferred, however plainly true they seem. Coverage is never rounded upward to make a graph look finished, because the number's only job is to bound the confidence of the impact answers built on it. Absence of an edge is reported as absence of evidence rather than as evidence of no consumer, since the paths this graph misses are precisely the ones with no metadata to miss. And an asset is never declared unused on the strength of query history alone while the export and BI extract inventories are unread, because the reader who does not appear in a query log is usually the reader whose report leaves the organization.

## data_packet fields to update

- `lineage.coverage`, `lineage.granularity`, and `lineage.derivation` per edge class
- `lineage.known_gaps[]` with each unmapped path and what it connects
- `catalog[]` with registration, steward, description state, certification, and measured usage
- `data_products[].consumers` corrected from traced consumption rather than from the intake list
- `models[].column_basis` where the catalog or parse establishes columns that were previously inferred
- `data_risks[]` for unowned, uncatalogued, or widely joined assets with no steward
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: query history, orchestrator metadata, the catalog, transformation code, or BI metadata needed to derive edges exists and cannot be read, so any impact answer would be an assertion about consumers nobody searched for.
- **Production or destructive**: the next action would drop, rename, revoke access to, or tombstone an asset, or delete a catalog entry that a downstream process reads.
- **Missing approval**: retiring an asset a named consumer still reads, deprecating a certified dataset, or reassigning stewardship needs the current owner, who has not agreed.
- **Security or privacy**: tracing would copy restricted column values into the graph or a description, or a classification would be carried into a lower-trust catalog audience than the data it describes.
- **Source conflict**: the catalog owner, the repository ownership record, and the query history genuinely disagree about who owns or consumes an asset, and picking one silently would send a deprecation notice to the wrong people.
- **Release integrity**: lineage coverage, an impact analysis, or a non-use finding would be declared complete when a known gap sits directly on the path the answer traverses.

An unregistered asset, a missing description, an unnamed steward, and a table-level edge where column-level was wanted are soft gaps. Name them, label the assumption, and continue. The requirement that a deprecation rest on measured non-use across query, export, and BI paths is never relaxed to clear a backlog of unread tables.

## Downstream handoffs

`metric-semantic-layer-desk` is next and needs the dashboard and query paths a definition change would move, plus the physical columns each business term maps to. `analytics-enablement-desk` inherits usage and the orphan and duplicate list. `data-governance-access-desk` inherits the traced propagation of every classified column into derived assets. `data-retention-lifecycle-desk` inherits the copy map, since a deletion plan is a lineage traversal with an expiry attached. `data-incident-response-desk` inherits the graph as its blast-radius instrument and the gap register as the bound on it. `data-observability-desk` receives the newly mapped paths that let fan-out alerts be grouped. `data-migration-desk` inherits the consumer inventory that determines cutover order.

## Quality bar

Good lineage work is honest about its edges before it is impressive about its coverage. It states granularity per region of the estate rather than as one number, attributes every edge, and puts the gap register in front of the graph, because the reader's real question is how much of the answer to trust. Impact analysis names actual dashboards, exports, and recipients rather than counting downstream objects. Usage is measured over a window long enough to contain the quarterly reader. Stewardship names a person who has accepted the asset rather than a team that inherited it in a spreadsheet. And the deprecation list is ordered by evidence strength, so the assets retired first are the ones whose non-use is provable across every path, not the ones whose names look obsolete.
