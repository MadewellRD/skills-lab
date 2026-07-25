---
name: rights-request-fulfillment-desk
description: search every system the data map identifies and name those not searched, instruct processors and track responses, redact third-party and exempt content with a per-redaction basis, assemble the response package in the form the right requires including portability format and access supplementary information, deliver over an authenticated channel, and propagate erasure rectification restriction or objection downstream. use for dsar retrieval and disclosure, subject access packages, right to know responses, deletion propagation, suppression lists, portability exports, and appeal handling.
---

# Rights Request Fulfillment Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the fulfillment artifact set, update `privacy_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the request it affects, and record it in `open_questions`. Never invent a search result, a system's coverage, a redaction basis, a processor confirmation, or a delivery record.

The deadline this desk works under started before intake did. A halt states it on its own line with its start event and due date, and names who has to be told today.

## Role

This desk turns a verified, scoped request into an answer the organization can stand behind, and it owns the two things that decide whether that answer survives a complaint: coverage and the basis for every withholding.

Coverage means the response says which systems were searched and which were not, by name. A response that asserts completeness across an estate where nine of forty systems were opened is an inaccurate statement about the organization made under the same law the request was brought under. The systems not searched are named with the reason, including backups, archives, exports, analytics copies, mailboxes, ticket attachments, and processor-held copies.

Withholding means every redaction has a recorded basis at the level of the redaction rather than at the level of the document. It owns the third-party data question, where another person's personal data sits inside the requester's own records and the balance between the requester's right and the other person's has to be struck and written down. It owns the response package in the form the right actually requires, including the supplementary information an access response has to carry beyond the data itself, delivery over a channel the requester is authenticated on, and the propagation of erasure, rectification, restriction, and objection to every downstream copy with confirmations tracked.

## Use when

- A request has been classified, verified, and scoped, and the work is retrieval, review, packaging, and delivery.
- Erasure, rectification, restriction, or objection has to reach processors, warehouses, backups, marketing platforms, search indexes, and vendor-held copies rather than only the system of record.
- A portability request needs a structured machine-readable export, or a direct transmission to another controller.
- Third-party personal data or exempt content sits inside the records in scope and the redaction has to be justified per item.
- A response was delivered and an appeal, a follow-up, or a regulator complaint has arrived on it.
- A suppression record is needed after erasure so the individual is not re-added by the next import.

## Do not use when

- The request has not been classified, verified, or scoped. That is `rights-request-intake-desk`, and running retrieval ahead of it searches for the wrong thing under the wrong deadline.
- The deletion is driven by a retention schedule rather than by an individual's request. That is `retention-deletion-desk`, which owns the schedule and the disposal method this desk borrows.
- The systems that hold the person's data have never been mapped. That is `data-inventory-mapping-desk`; this desk can only search what the map identifies, and it reports the rest as not searched.
- The vendor has no assistance obligation and the question is what the contract requires. That is `processor-vendor-agreement-desk`.
- Handling the request has revealed an exposure of personal data. That is `breach-assessment-desk`, on its own clock.

## Required evidence

- The verified request with its right, regime, scope, deadline, exemptions, and the delivery form the right entitles the requester to.
- The data map and system inventory that says where to look, with its coverage statement, since that statement becomes the coverage statement of this response.
- The identifiers the individual is known by across systems, including the ones that differ: a customer number, a device or advertising identifier, a hashed email in a marketing platform, an internal person key, and any duplicate or merged records.
- The processor list filtered to those holding in-scope data, with the assistance clause and the response time each is contractually held to.
- Backup, archive, and export inventory with the retention cycle for each, and whether selective retrieval or selective deletion is possible.
- Third-party personal data appearing in the same records, and the exempt content identified at intake with its provision.
- The channel the requester is authenticated on and the secure delivery route available.
- Prior responses to the same individual, since a second response that contradicts the first is read as evidence about the first.

## Workflow

**Outcome.** A retrieval record naming every system searched with what was found and every system not searched with the reason; processor instructions issued with responses tracked; a redaction log with a basis per redaction; a response package in the required form carrying the supplementary information the right demands; a delivery record over an authenticated channel; and, for erasure, rectification, restriction, and objection, a propagation record with confirmations from each downstream holder.

**Grounding.** Search is executed against the data map rather than against recollection, and the identifier set is expanded before searching, because a person present in the CRM as an email address and in the event stream as a device identifier is one person and two searches. Results are recorded per system with the query or filter that produced them, so that "no records" is distinguishable from "not searched" and from "searched with the wrong identifier". Processor responses are recorded as received, and a processor that has not answered is recorded as outstanding rather than as having nothing, because silence from a vendor is not a negative search result.

**Constraints.** The response states its own coverage, and coverage is stated at the system level with names. Redaction carries a basis per redaction: the provision or the third-party balancing that justified it, the content type it covers, and who applied it, since a redaction log written per document cannot answer the one question a complaint asks, which is why a specific passage was withheld. Third-party personal data is not automatically withheld and is not automatically released; where the other person has not consented, the balance considers what the requester already knows, whether the other person is acting in a professional capacity, and whether the content can be released with the identifying part removed, and the reasoning is recorded. Exempt content is withheld at the narrowest level that achieves the exemption rather than by withholding the document that contains it. An access response carries more than the data: the purposes, the categories of data, the recipients including any in third countries, the retention period or the criteria used to set it, the source where the data was not collected from the individual, the rights available including complaint to a supervisory authority, and meaningful information about the logic of any automated decision. Portability is delivered in a structured, commonly used, machine-readable format that another controller could actually ingest, which a document rendering of the same data is not. Personal data is not copied into working artifacts, tickets, or the packet; the response package is assembled in a controlled location and referenced by locator. Delivery goes over the channel the requester is authenticated on, and where a package is sent out of band the access credential travels separately. Erasure propagation reaches processors, analytics and warehouse copies, search indexes, caches, marketing platforms, and exports, and where a backup cannot be selectively edited the data is put beyond use with the restore-time suppression recorded and the expiry cycle stated.

**Ordered sequence for erasure and its propagation.** This order is mandated because deletion is irreversible and because a record removed under a live hold converts a routine request into a spoliation problem:

1. Run the legal hold check across the scope and record its result before anything is deleted.
2. Execute in the systems that can confirm absence, and record what confirmed it.
3. Instruct processors and downstream holders, and track each confirmation rather than assuming the instruction landed.
4. Handle backups and immutable stores by the stated route, with the restore-time suppression in place before the deletion is called complete.
5. Create the minimal suppression record that prevents re-import, and record what permits that record to exist.

**Parallel surface.** Per-system searches within a single request are independent and fan out safely, as do the per-processor instructions, the per-system erasure executions, and the per-document redaction reviews. Several open requests also fan out. Three steps are aggregate and run once after the fan-out returns: deduplication of the same record surfacing from several systems, the coverage statement itself, which is a claim about the whole estate and cannot be assembled from parts that each looked at one system, and the assembly of the response package, which has to be internally consistent before it goes out.

**Acceptance bar.** Every system in the map appears in the retrieval record as searched or not searched, with the reason. Every redaction has a basis, a scope, and an author. The package carries the supplementary information the right requires, and a portability export opens in something other than the system that produced it. Delivery names the authenticated channel and the date. For erasure, every downstream holder has a confirmation or is recorded as outstanding by name.

## Outputs

A complete run delivers this set:

- `retrieval-record.md`: per system the identifiers and query used, the date searched, what was found in categories rather than in content, and per unsearched system the reason, so the coverage statement is auditable line by line.
- `processor-instruction-log.md`: the instruction sent to each processor, the clause it was issued under, the date, the response received or the outstanding state, and the escalation where a contractual response time has passed.
- `redaction-log.md`: one entry per redaction with the location, the content type, the basis with its provision or the third-party balancing performed, and the reviewer, at redaction level rather than document level.
- `response-package-manifest.md`: what the package contains, the format of each part, the supplementary information included with where each element sits, and the locator of the controlled location holding it, with no personal data reproduced in the manifest itself.
- `delivery-record.md`: the channel, the authentication that channel provides, the date, what was sent, how any access credential was transmitted separately, and the appeal and complaint routes stated in the response.
- `erasure-propagation-record.md`: per downstream holder the action, the confirmation and what confirmed it, the exceptions with the basis that keeps each copy, the backup treatment with its expiry cycle, and the suppression record created.
- `rights-request-fulfillment-downstream-handoff.md`: what `retention-deletion-desk` inherits, including the systems that could not delete and the exceptions that need a schedule position.

Depth standard: an artifact is complete when the response could be released and defended without a follow-up round trip, and when a regulator reading it alongside a complaint could reconstruct what was searched, what was withheld, and why. A retrieval record listing systems without dispositions, or a redaction log at document granularity, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where a system in scope cannot be searched or a processor cannot be reached, the run delivers `fulfillment-connector-diagnostic.md` naming each unreachable system, what the response can and cannot claim as a result, and the deadline still running. The response is not completed by treating an unreachable system as an empty one.

Anti-fabrication guard: the characteristic failure at this desk is that absence gets upgraded. A system nobody opened becomes a system with no records, a processor that never replied becomes a processor that confirmed, a soft delete becomes a deletion, and the response goes out saying the organization holds nothing further. Every one of those is a false statement to the individual, made in writing, under the law they invoked. In the artifacts here, "not searched", "no response received", "deleted in the primary store only", and "no records found for the identifier used" are each written as themselves and never collapse into a single reassuring sentence. The second failure is quieter: the response that reads as complete because it contains a lot of data while omitting the supplementary information the right actually requires, which makes a large package a non-compliant one. The manifest checks the required elements as elements rather than assuming the export covered them.

## privacy_packet fields to update

- `rights_requests[].scope.systems_searched` and `systems_not_searched`, the second populated with names and reasons rather than left blank
- `rights_requests[].scope.backups_and_archives` with how they were treated and on what basis, and `processors_instructed` with each response state
- `rights_requests[].third_party_data` with how other people's data in the same records was handled
- `rights_requests[].exemptions_applied[]` extended with the redactions each covers
- `rights_requests[].response_state`, `delivered_on`, `delivery_channel`, and `appeal` where one arrives
- `deletion_records[]` for erasure requests with `hold_check`, `systems_executed`, `systems_pending`, `processors_instructed` with confirmations, `verification_basis`, and `exceptions` each with what permits the copy to remain
- `active_clocks[]` updated with the response deadline and any appeal window the delivery starts
- `source_facts` with search dates, `assumptions`, `open_questions`, `approvals` for the release itself
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: the response would assert completeness across systems that were never searched, or carry redactions whose basis nobody recorded. This is the organization's answer on the record, a regulator reads it next to the complaint that follows, and a correction after delivery is a second disclosure event rather than an edit.
- **Missing approval**: releasing the package is an irreversible external act and needs the named owner who authorizes disclosure, as does a decision to withhold a whole category of content.
- **Production or destructive**: executing erasure, restriction, or rectification changes live records across systems and processors at once and has no rollback.
- **Security or privacy**: the package contains another individual's personal data with no completed balancing, the delivery channel is not one the requester is authenticated on, or the export would be sent to an address that does not match the verified identity.
- **Source conflict**: two systems genuinely disagree about the individual's records, or the map and the search results disagree about what a system holds. Preserve both readings; a response that silently picks one states something the organization cannot support.
- **Connector unreachable**: a system in scope or a processor holding in-scope data cannot be reached, so completeness cannot be claimed. The deadline continues and is stated on the halt.

An unconfirmed identifier in a low-volume system, an undocumented export, and an unclear record type are soft gaps. Search on the identifiers available, record the limitation in the coverage statement, and continue.

## Downstream handoffs

`retention-deletion-desk` is next and needs the systems that could not execute deletion, the exceptions with their retention basis, the suppression records created, and the backup expiry cycles this request now depends on. `processor-vendor-agreement-desk` receives the assistance failures found here, since a processor that missed its contractual response time is a clause finding as well as a delay. `breach-assessment-desk` takes over where fulfillment revealed data in a place it should not have been, or where a package went to the wrong person. `privacy-program-metrics-desk` needs delivery dates against deadlines and the coverage figures per request. `rights-request-intake-desk` handles any appeal that arrives on the delivered response.

## Quality bar

Good fulfillment work is judged on the two sentences the organization would least like to write and most needs to. The first names the systems that were not searched. The second gives the basis for a specific redaction. Everything else in a response package is retrieval mechanics. Beyond those, the marks of real work are an identifier set that caught the person in the platforms where they are not an email address, an erasure that reached the warehouse copy and the marketing platform rather than stopping at the system of record, a portability file another controller could load, and an access response that includes the purposes, recipients, retention, and source rather than a data dump that satisfies nobody. And where a backup could not be selectively edited, the honest answer with the expiry cycle and the restore-time suppression is a better artifact than a deletion confirmation that will be contradicted the first time someone restores.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
