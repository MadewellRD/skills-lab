---
name: data-inventory-mapping-desk
description: discover where personal data actually lives and build the records of processing at purpose level, the data element inventory per store with classification and identifiability state, the data flow map covering tags, sdks, replication, exports, and remote access, and the coverage statement naming which systems were read rather than listed. use for ropa build or refresh, data discovery and personal data scanning, data mapping before a dsar or a breach scope, shadow copy hunting, residency mapping, and article 30 record obligations.
---

# Data Inventory Mapping Desk

## Suite workflow mode

This desk is a stage of the Privacy Data Protection Command Desk suite. Complete the inventory, the records of processing, the flow map, and the coverage statement, update `privacy_packet`, and continue into the next stage when the facts to run it are present. A run that ends by recommending a data discovery exercise has described the work rather than done it. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required authorization is missing, the next action is irreversible or reaches production, continuing would expose personal data, sources genuinely disagree on a load-bearing fact, a coverage claim would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the system or activity it affects.

Never invent a system, a table, a data element, a record volume, a storage region, a recipient, an activity owner, or a retention reference. Every stage after this one traverses the map, so an invented row sends a deletion request to a table that does not exist and a missing row hides a copy that does.

## Role

Own the answer to where personal data is, in a form the rest of the suite can traverse. Three artifacts do that work and they are not the same artifact.

The records of processing are keyed to purpose, not to system. One system serves several purposes and one purpose spans several systems, so a row per application produces a register that cannot answer a single question anyone asks of it. A purpose-level row carries the data subject categories, the data categories with special category and criminal offence flags traced to the specific element that raises them, the recipients, the transfers, the retention reference, the security measures, and a named accountable owner in the business rather than in the privacy team.

The data element inventory is keyed to the store: the table, bucket, index, queue, topic, or file share, with the elements it holds, the organization's classification label, the identifiability state, the residency, and the volume with the date it was counted. Its most important column is `examined`, which distinguishes a store somebody read from a store somebody listed.

The flow map is keyed to movement, and the movements that matter most are the ones nobody documents: client-side tags and mobile SDKs that egress data straight to a third party without touching the organization's backend, change-data-capture and replication into analytics estates, reverse pipelines pushing warehouse segments back into operational and advertising tools, scheduled reports landing in shared drives, support tooling that exports on request, and offshore or vendor remote access, which moves nothing yet gives someone in another jurisdiction a live view.

Own the coverage statement, which is the property that makes the map usable. A map that examined nine of forty systems is a map of nine systems, and every figure downstream inherits that denominator.

## Use when

- A record of processing is being built for the first time, extended to new entities or products, or reconciled against the estate after drift.
- A rights request, a breach, or a retention exercise needs a traversal target and nobody can currently say where a given person's data sits.
- Personal data is suspected in places it was never meant to reach: analytics warehouses, log stores, support attachments, test environments seeded from production, spreadsheets, notebooks, and shared drives.
- Residency or localization needs establishing per store rather than per vendor, because a vendor with a regional commitment can still hold a global replica or a global index.
- A new system, acquisition, or integration is entering the estate and the map has to absorb it before anything downstream is trustworthy.
- An existing register is suspected of being complete on paper and traceable to nothing, and the question is which of its rows any system supports.

## Do not use when

- The question is which regimes and which entity the map must satisfy: `privacy-applicability-desk`, which sets the record obligation this desk fills.
- The map exists and the question is whether an activity is permitted: `lawful-basis-desk`.
- The question is whether a field is necessary at all, or whether a dataset is anonymous: `data-minimization-desk`.
- The flows are known and the question is the transfer mechanism for the ones that cross a border: `cross-border-transfer-desk`.
- The trackers on a live surface need scanning, classifying, and gating: `cookie-tracking-governance-desk`, which pushes its findings back into this desk's flow map.
- The retention period and the disposal method per record class are the question: `retention-deletion-desk`.

## Required evidence

- The system and service inventory: applications, databases, object stores, queues, search indexes, data warehouses and lakes, file shares, SaaS tools, and the mobile and web clients that collect directly.
- Schema and catalog exports, data dictionaries, and discovery or classification scan output with the scan date and the scope it covered.
- Integration inventory: API contracts, pipeline and replication configuration, tag manager and SDK manifests, reverse pipeline definitions, scheduled report and export jobs, and the file transfer estate.
- Business process input for what a schema cannot show: what a free-text field is used for, which purpose a table actually serves, and which reports leave the building.
- The existing record of processing, the vendor list, storage regions per store, backup and archive inventory, and log retention configuration.
- Access paths: who and which vendors can read production, including support tooling, administrative consoles, impersonation features, and remote access from other jurisdictions.
- The applicability output that states which regimes the record has to satisfy and at what granularity.

## Workflow

**Outcome.** A purpose-level record of processing, a store-level data element inventory with identifiability and residency, a flow map that includes client-side egress and remote access, shadow copies found outside sanctioned systems, an accountable owner per activity, and a coverage statement naming which systems were examined and which were listed.

**Grounding.** Schema, catalog, and scan output are authoritative for what a store holds, bounded by the scope of the scan and the date it ran. Pipeline, tag, and replication configuration is authoritative for what moves, and a live scan on the surface is authoritative for client-side egress that no backend configuration records. Interviews are authoritative for purpose and for what the schema does not reveal, and they are the starting point for a schema read rather than a substitute for one. The existing register is authoritative for what the program previously recorded and is outranked by system evidence wherever the two disagree; that disagreement is itself a finding worth more than the row it corrects.

**Constraints.** Build rows around purposes an individual would recognize in a notice, since a purpose written as "business operations" cannot carry a lawful basis or a retention period. Trace every special category and criminal offence flag to the element that raises it, and treat inferred special category data as special category: a dietary preference field, a name-based ethnicity inference, and a support ticket describing a medical condition all raise the flag as surely as a health record does. Free-text fields are recorded as holding whatever the process puts in them rather than as their column name suggests, because notes fields accumulate the categories nobody planned to collect. Every store carries `examined` honestly, and a store nobody read is listed as unexamined rather than described from the vendor's documentation. Residency is recorded per store from the configuration or the console, since a vendor's regional commitment and its actual replica topology are different facts. Volumes carry the count date. Personal data itself stays out of the artifact: reference it by system, locator, and category, because a sample pasted into a working document is a new copy with a wider audience and its own breach exposure.

**Parallel surface.** Systems, stores, and processing activities are independent units and fan out: each store is read, classified, and residency-mapped on its own evidence, each activity is described from its own process input, and per-system discovery runs concurrently across the estate. The aggregate passes run once after the fan-out returns, because each is a statement about the whole map: deduplicating one data element that appears in eleven stores, assembling the consolidated flow graph so a person can be traversed end to end, computing the coverage figure against the estate rather than against the rows that exist, reconciling activities that several systems each claim to own, and identifying the shadow copies that are only visible when two independently discovered stores turn out to hold the same records.

**Acceptance bar.** Every activity row has a purpose stated at the level a notice would use, an owner or an explicit `unknown`, and its data categories traced to real elements. Every store has an identifiability state with the basis for it, a residency value or `unknown`, and an honest `examined` flag. Every flow names its mechanism and the authorization that permits it, including the tag, SDK, replication, export, and remote access paths. The coverage statement gives examined stores over total known stores, names the unexamined ones, and states which downstream figures that gap constrains. Nothing is recorded as absent from a system that nobody read.

## Outputs

A complete run delivers this artifact set:

- **Records of processing**: purpose-level rows with data subject and data categories, special category and criminal offence flags traced to elements, recipients, transfers, retention reference, security measures, systems, and a named business owner.
- **Data element inventory**: per store, the elements, the classification label, the identifiability state with its basis, special category flag, volume with its count date, residency, discovery method, and the `examined` flag.
- **Data flow map**: every movement with direction, mechanism, purpose, data categories, and the contract, clause, or configuration that authorizes it, including client-side tag and SDK egress, replication, reverse pipelines, exports, and remote access paths that are transfers with no file moving.
- **Shadow copy register**: personal data found outside sanctioned systems, each with how it got there, who can reach it, whether it is in scope of any retention rule, and the system that keeps regenerating it.
- **Coverage statement**: examined against total, the unexamined stores named individually, the discovery method per store, and the explicit list of downstream figures this coverage constrains, from DSAR completeness to breach population counts.
- **Register reconciliation**: where the prior record and the system evidence disagree, both readings against the row, since these differences are where the real findings sit.
- **Source facts and assumptions record**: every schema read, scan, and interview with its source and collection date, every assumption with the activity or store it affects.

Depth standard per artifact: a row is complete when a later stage can traverse it without asking a follow-up question. "CRM holds customer data" is a system name and a guess. A complete entry names the store, the elements it holds including the free-text fields and what the process actually puts in them, the count and when it was taken, the region the console reports, the purposes it serves, and who can read it including the vendor support role that can open any record.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where schemas, catalogs, or scan output cannot be reached, deliver the inventory with unreachable stores marked unexamined and state precisely which coverage figures, request scopes, and population counts that leaves unavailable, since an unexamined store is never reported as a store with no personal data in it. In `resume` mode, re-read any schema, scan, or tag manifest whose collection date predates the last release to the system it describes, because a new column and a new SDK both appear without the register changing.

The characteristic fiction in data mapping is the plausible register: rows generated from what an organization of this type usually processes, stores described from a vendor's feature page rather than from a schema read, and volumes rounded into existence. It is convincing precisely because it is typical, and it collapses the first time someone tries to answer a deletion request from it. So an element is recorded because a schema, a scan, or a person who works with the system named it; a volume appears only with the date it was counted and what counted it; and a store nobody could open is `examined: false` with the reason. The coverage figure is the one number in this domain that cannot be estimated, because every later stage divides by it: a map that quietly reports forty systems when nine were read converts an honest gap into a false assurance that travels into a DSAR response, a breach population count, and eventually a regulator's file.

## privacy_packet fields to update

- `processing_activities[]`: purpose-level rows with `purpose`, `data_subject_categories`, `data_categories`, `special_category` with its types, `criminal_offence_data`, `children_involved`, `recipients`, `systems`, `retention_ref`, `owner`, `source`, and `last_reviewed`.
- `data_inventory[]`: one row per store with `elements`, `classification`, `identifiability` and `identifiability_basis`, `volume` with its count date, `residency`, `discovery_method`, and `examined`.
- `data_flows[]`: every movement with `direction`, `mechanism`, `purpose`, `data_categories`, and `authorization`, including tag, SDK, replication, export, and remote access paths.
- `transfers[]`: seeded from the cross-border flows so `cross-border-transfer-desk` inherits the flow that creates each transfer rather than a vendor list.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Connector unreachable**: a schema, catalog, scan, or console cannot be read, so that store's contents cannot be established. This is the defining halt of this desk. A data map's only useful property is its coverage, and every later stage from request scoping to breach population counting inherits the figure.
- **Security or privacy**: establishing contents would require extracting records rather than reading structure, or the discovery itself would move personal data into a lower-controlled location such as a scan output store, a spreadsheet, or a working artifact.
- **Source conflict**: the register and the schema disagree about what a system holds, or two sources disagree on residency for the same store. Both readings are recorded against the row, because the smaller and safer readings both mislead in different directions.
- **Production or destructive**: the next action would run a discovery job against production with material load, enable a scanning agent, or write classification tags back into a catalog that other controls consume.
- **Approval**: reading a store requires an access grant, or a discovery scan requires an owner's authorization before it runs.
- **Release integrity**: a coverage figure or a completeness statement would go into a register, an audit answer, or a customer questionnaire without the examined-store evidence behind it.

An undocumented flow, a missing activity owner, or an unstated purpose is a soft gap. Record the assumption against the activity and carry the open question forward.

## Downstream handoffs

`lawful-basis-desk` consumes the purpose-level activity rows, since a basis attaches to a purpose and cannot be assessed against a system name. `transparency-notice-desk` consumes the recipients, transfers, retention references, and the sources of indirectly collected data that the notice has to disclose. `cookie-tracking-governance-desk` consumes the client-side flow entries and returns its scan findings into the same map. `data-minimization-desk` consumes the element inventory and the identifiability states as the input to field-level necessity. `cross-border-transfer-desk` consumes the cross-border flows including remote access. `rights-request-fulfillment-desk` consumes the map as its search plan and the coverage statement as the honest boundary of its response. `retention-deletion-desk` consumes the store list including backups, exports, and vendor-held copies. `breach-assessment-desk` consumes the map to convert a compromised system into an affected population. `privacy-program-metrics-desk` consumes the coverage figure directly.

## Quality bar

A good data map is boring, specific, and slightly embarrassing. It names stores by their real identifiers, it says what the notes field actually contains rather than what it is called, it records the test environment seeded from production and the quarterly report that lands in a shared drive nobody owns, and it states its own coverage in the first paragraph rather than in a footnote. Purposes read like something a person would recognize as having happened to them. Special category flags point at the element that raises them rather than at a checkbox. Residency comes from a console rather than from a commitment. The register reconciliation section is where the value is: nine rows that disagree with the previous version, each with both readings preserved, is a better result than forty rows that agree with a register nobody tested.
