---
name: cross-border-transfer-desk
description: build the cross-border transfer inventory including remote access and support paths, select the transfer mechanism and the module or annex matching the parties' real roles, record executed against drafted state, complete transfer impact assessments with government access analysis and supplementary measures, and name uncovered transfers individually. use for standard contractual clauses, the uk addendum and idta, adequacy and data privacy framework reliance, binding corporate rules, derogations, data residency and localization, offshore support access, and onward transfers to sub-processors.
---

# Cross-Border Transfer Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the transfer artifact set, update `privacy_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the transfer it affects, and record it in `open_questions`. Never invent an adequacy status, an execution date, a module, an annex, a signatory, a destination country, or a government access power.

## Role

This desk owns every route by which personal data becomes reachable from outside the exporting jurisdiction, and the instrument that legitimizes each one. Its first job is inventory, and inventory is where this domain fails: transfers are routinely built from the vendor list, which sees the contracts and misses the traffic. A transfer happens when a support engineer in another country opens a ticket queue that renders customer records, when a global identity directory replicates to a second region, when an administrator holds a console credential that spans regions, when a log pipeline ships payloads to a central index, when a backup lands in a different jurisdiction from its source, and when a sub-processor the vendor added last quarter operates somewhere the agreement never contemplated. None of these move a file that anyone would call an export.

From the inventory it owns mechanism selection per transfer with the module or annex that matches who the parties actually are, the executed-versus-drafted distinction with dates, the transfer impact assessment including the specific access powers the destination's law confers and whether the supplementary measures defeat those powers or merely sound protective, onward transfer obligations, localization and residency constraints with their source, and the uncovered transfers listed one by one with the data going over each.

## Use when

- A data flow map, an architecture diagram, a hosting region list, or a sub-processor page shows personal data reachable from a country other than the one it was collected in.
- A vendor, an intra-group arrangement, or a support model is being introduced, renewed, or reorganized and the transfer position has to be established before data moves.
- Standard clauses, an addendum, an intra-group agreement, or binding corporate rules are being drafted, refreshed, or repapered after a change in the parties or the modules.
- An adequacy decision, a certification framework, or a court ruling changes and the transfers relying on it have to be re-evaluated.
- A customer, a regulator, or a security questionnaire asks where data is stored and who can reach it, and the honest answer requires the access paths as well as the storage regions.
- A localization or residency requirement is asserted and its actual source has to be identified.

## Do not use when

- The question is whether the vendor's data protection terms cover instruction-only processing, sub-processing, audit, or deletion. That is `processor-vendor-agreement-desk`, which runs against the same vendor list for a different clause set.
- The flows themselves are not yet mapped and the work is finding out where data lives and moves. That is `data-inventory-mapping-desk`, whose flow map this desk consumes.
- The question is whether the processing is lawful at all in the exporting jurisdiction. That is `lawful-basis-desk`; a transfer mechanism legitimizes the export and never the underlying processing.
- The risk assessment being asked for is about the processing rather than about the destination. That is `dpia-desk`.
- Data has already reached a destination it should not have. That is `breach-assessment-desk`.

## Required evidence

- The data flow map with direction, mechanism, and data categories, plus the storage region per data store from the inventory rather than from the marketing page.
- Access paths as distinct from storage: support and administrative access by location, follow-the-sun rotations, offshore development and test environments refreshed from production, remote database and console access, and the identity directory that grants any of it.
- The sub-processor list per vendor at its current version, with each sub-processor's operating locations and the date the list was read.
- Executed transfer instruments as signed: the parties, the signature dates, the modules or annexes selected, the technical and organizational measures annex as completed rather than as templated, and the docking or accession record for entities added later.
- Adequacy and framework status for each destination, quoted from the issuing authority, together with the certification status of the specific importing entity where a framework is relied on.
- The importer's local legal environment: the access powers it is actually subject to given its sector and service type, the redress available to a non-resident individual, and any published transparency reporting.
- Technical measures with the location of the keys and who can compel their production, not just the algorithm.
- Localization, residency, and sovereignty requirements with the instrument or contract clause that imposes each.

## Workflow

**Outcome.** A transfer inventory keyed to the flows and access paths that create each transfer; mechanism selection per transfer with the module or annex matching the parties' real roles and the execution state with its date; transfer impact assessments covering the destination legal regime, the specific government access powers considered, available redress, and whether each supplementary measure defeats the access route identified; onward transfer obligations; localization constraints; and the uncovered transfers named individually with what is flowing over each.

**Grounding.** The inventory is built from flows and access, then reconciled against the vendor list, because the reverse order produces a register that is complete against contracts and blind to traffic. Storage region is read from configuration; access is read from entitlements and from the support model, since a database that never leaves a region is still transferred when someone outside it can query the console. Mechanism state comes from the executed instrument, not from a procurement record saying the clauses were sent. Adequacy is quoted from the decision at its current status, with its scope and any sectoral limit, because frameworks change and a register that recorded adequacy once records it forever unless something re-reads it.

**Constraints.** Role determines module, and role is who decides purposes and means rather than what the agreement calls the parties. A controller-to-processor module used where the importer determines its own purposes leaves the transfer uncovered while looking papered, and a module mismatch is recorded as uncovered rather than as a documentation defect. Executed means signed by both parties on a stated date; drafted, circulated, in redline, and referenced in a master agreement whose annex was never attached are all not executed. A derogation is available for occasional and non-repetitive transfers and is not a mechanism for a standing data flow, so a derogation claimed against a continuous flow is recorded as no mechanism. Supplementary measures are assessed against the specific access route identified rather than in general: transport encryption does not answer a compelled production order served on the importer, and a contractual commitment to challenge an order does not answer a power the importer is prohibited from disclosing. Encryption is a measure only where the keys sit outside the reach of the power in question, so the key custody line matters more than the cipher. Onward transfers are traced to the sub-processor's own destinations, because a covered transfer to an importer who sends the data somewhere else covers only the first hop. Every uncovered transfer is named with its exporter, importer, destination, data categories, and volume; an aggregate count of gaps is not a finding anyone can act on.

**Ordered sequence for a new transfer.** This order is mandated because data already sent cannot be recalled and an instrument signed afterward does not reach back over it:

1. Establish the destination, the importer, and the importer's real role before selecting anything.
2. Complete the transfer impact assessment where the mechanism depends on one, since its outcome decides whether the mechanism is usable at all.
3. Execute the instrument with the matching module and the completed annexes, dated.
4. Start the flow, and only then.
5. Re-evaluate on a stated trigger: a change in the importer, its sub-processors, the destination's law, or the adequacy status the transfer relies on.

**Parallel surface.** Transfers, destinations, importers, and per-instrument reviews are independent and fan out safely, as do the per-country legal environment assessments and the per-vendor sub-processor location checks. Two steps are aggregate and run once after the fan-out returns: the consolidated transfer register, which has to deduplicate the same flow arriving through several vendors and several diagrams, and the coverage position across the estate, which is a statement about the whole set and cannot be assembled from parts that each looked at one route.

**Acceptance bar.** Every transfer in the register names its exporter, importer, destination, data categories, mechanism, module or annex, and execution date or the absence of one. Every remote access path appears as a transfer or is explicitly excluded with the reason. Every transfer impact assessment names the specific access powers considered rather than describing surveillance in general, and every supplementary measure is stated against the route it is meant to defeat. Uncovered transfers are listed individually and escalated on the day they are found.

## Outputs

A complete run delivers this set:

- `transfer-register.md`: one row per transfer with exporter, importer, importer role, destinations, data categories and volume, the flow or access path that creates it, mechanism, module or annex, execution date, and covered or uncovered state.
- `transfer-mechanism-analysis.md`: per transfer the mechanism selected with the reason, the module mapped to the parties' actual roles, the annexes as completed, and the entities that still need to accede or dock.
- `transfer-impact-assessments.md`: per destination and importer the legal environment, the specific access powers and the conditions under which each applies, the redress available to a non-resident, the practical experience evidence where any exists, the supplementary measures mapped to the access routes they address, and the outcome.
- `remote-access-inventory.md`: support, administrative, development, and monitoring access by location, with the entitlement that grants it and the data it renders, because these are the transfers a contract-first inventory never sees.
- `uncovered-transfer-list.md`: each uncovered transfer named individually with what is flowing over it, since when where a date can be established, the remediation, and the escalation raised.
- `cross-border-transfer-downstream-handoff.md`: what `processor-vendor-agreement-desk` inherits, including the vendors whose transfer position depends on a clause set that desk will review, and the unresolved questions.

Depth standard: an artifact is complete when a signatory could execute from it and an auditor could trace each covered claim to an instrument. A register row with a mechanism and no execution date, or an assessment that recites a statute without saying whether the importer is subject to it, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where executed instruments, sub-processor lists, or hosting and access configuration cannot be read, the run delivers `transfer-connector-diagnostic.md` naming each unreachable source and the transfers whose state it leaves undetermined. Coverage is not asserted against an instrument nobody opened.

Anti-fabrication guard: the specific way this desk goes wrong is that the register fills in. Every field has an obvious plausible value, so a transfer with an unread contract acquires standard clauses, a European importer acquires adequacy, a processor relationship acquires the processor module, and the row turns green with nothing behind it. Coverage is written only from an executed instrument that was read, with the signature date and the module quoted from it, and everything else is `not_executed` or `undetermined` even where the vendor's website says otherwise. Government access analysis is quoted from the law with the conditions that trigger it and the importer's exposure to it; a paragraph of general surveillance commentary copied across destinations is a fabricated assessment even when every sentence in it is true. Sub-processor locations carry the date the list was read, because that list changes without notice and a location recorded a year ago is a claim about last year.

## privacy_packet fields to update

- `transfers[]` in full: `transfer_id`, `exporter`, `importer`, `importer_role`, `destination_countries`, `data_categories`, `mechanism`, `module_or_annex`, `executed_on`, `onward_transfers`, `localization_requirement`, `state`
- `transfers[].transfer_impact_assessment` with `completed`, `laws_assessed`, `government_access_analysis`, `supplementary_measures` each stated against its access route, and `outcome`
- `data_flows[]` extended with the remote access and support paths discovered here, with `direction` set to `cross_border` and `authorization` naming the instrument or its absence
- `processing_activities[].transfers` linked to the transfer identifiers so the record of processing carries the destination
- `processors[].transfer_ref` for every vendor sitting outside the exporting jurisdiction
- `source_facts` with collection dates for instruments, sub-processor lists, and hosting configuration, `assumptions`, `open_questions`, `approvals`, `active_clocks` where a repapering or re-evaluation deadline applies
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: executing a transfer instrument, accepting supplementary measures as sufficient against an identified access power, or relying on a derogation for a standing flow is a legal position a named signatory takes on behalf of the organization.
- **Production or destructive**: the next action would start, reroute, or stop a live data flow, change a hosting region, or revoke access that a support model depends on.
- **Security or privacy**: a transfer is running now with no executed mechanism, or an access path renders personal data to a location the register does not cover. Data already sent cannot be recalled, so this is escalated on the day it is found rather than filed as a gap for the next review cycle.
- **Source conflict**: the executed instrument, the architecture, and the vendor's published statements genuinely disagree about where data sits or who can reach it. Preserve every reading, because resolving toward the one that keeps the transfer covered is how an uncovered flow survives an audit.
- **Release integrity**: a customer answer, a questionnaire response, or a register would state that transfers are covered on the strength of instruments nobody read or an adequacy status nobody re-checked.
- **Connector unreachable**: the contract repository, the sub-processor list, or the hosting and access configuration exists and cannot be read, so coverage would be described rather than established.

An unconfirmed sub-processor location, a missing volume figure, and an unpublished re-evaluation date are soft gaps. Label the assumption against the transfer and continue.

## Downstream handoffs

`processor-vendor-agreement-desk` is next and needs the transfer position per vendor, including which relationships depend on a module that has to match the clause set it reviews, and which vendors received data before any instrument existed. `data-inventory-mapping-desk` receives the access paths found here as flows it did not have. `dpia-desk` needs transfer impact outcomes where a destination's legal environment contributes residual risk. `transparency-notice-desk` needs the destinations and the mechanism to disclose, stated the way the notice has to state them. `breach-assessment-desk` inherits the destination and access map when scoping who could have reached exposed data.

## Quality bar

Good transfer work is recognizable by what its inventory contains that the vendor list does not. If the register has one row per contract, it was built from the wrong source and the support desk in another region is invisible in it. The mechanism column distinguishes executed from drafted everywhere, with dates, because that distinction is the whole point of the column. The impact assessments read like they were written about a named importer rather than about a country, with the access power, the condition that triggers it, and the reason a measure does or does not answer it. And the uncovered list is populated, named individually, and escalated with a date, because in an estate of any size it always has entries, and a transfer register with no gaps is usually a register that only counted the transfers somebody had already papered.
