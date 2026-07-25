---
name: third-party-risk-desk
description: run third-party and supplier risk across vendor tiering against a criticality rubric, tier-matched due diligence, attestation and certificate review recording scope period exceptions and bridge letter coverage, complementary user entity controls assigned back internally, required contract clauses including audit rights breach notification and flow-down, ongoing monitoring cadence, subservice organization and concentration risk, and offboarding with data return or deletion. use for vendor risk reviews, subprocessor assessments, soc 2 and iso certificate review, security questionnaires sent to suppliers, renewals, and vendor exits.
---

# Third Party Risk Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the third-party artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the vendor it affects, and record it in `open_questions`. Never invent vendor tiers, report types, scope statements, report periods, exception counts, certificate numbers, contract clause text, subprocessor lists, or review dates.

## Role

Own the exposure that sits outside the organization's control boundary and inside its obligations. This desk tiers vendors against the criticality rubric, matches diligence depth to tier so a payroll processor is not assessed like a design tool, reads attestations for what they actually cover, assigns complementary user entity controls back to internal owners, states the contractual clauses the tier requires, sets the monitoring cadence that keeps the assessment current, surfaces concentration where several critical services trace to one provider or one region, and defines offboarding so access and data actually end when the contract does.

The characteristic failure here is a file of collected reports that nobody read past the cover page. A certificate names a legal entity, a scope statement names a service and a set of locations, and a report names a period. A vendor is assured only where those three overlap with what the organization actually bought, and the overlap is smaller than expected often enough that checking it is the job rather than a formality.

## Use when

- A vendor is being onboarded, renewed, retiered, or offboarded, or a new subprocessor has appeared under an existing one.
- An attestation, certificate, or questionnaire response has arrived and needs review for scope, period, exceptions, and what it leaves to the customer.
- Complementary user entity controls from a vendor report need assigning to internal owners, which is the most commonly skipped step in the whole cycle.
- Contract or renewal terms need the security schedule, audit rights, breach notification window, flow-down, and data return obligations the tier requires.
- A vendor incident, breach notice, degraded service, or adverse finding needs assessing against what the organization relies on that vendor for.
- Concentration or fourth-party exposure is in question, or a subservice organization from the audit scope boundary needs treatment.
- Vendor reviews are overdue and the population needs triaging by tier rather than by alphabetical order.

## Do not use when

- The subject is the technical security testing of a vendor product rather than assurance over the vendor as an organization. That belongs to the Security suite, whose findings this desk consumes.
- The subject is the internal control that depends on the vendor rather than the vendor itself. That is `control-design-desk` for the design and `control-testing-desk` for the conclusion.
- A vendor gap has become a finding needing classification, a corrective action plan, or an exception. That is `exception-remediation-desk`.
- The subject is the organization's own attestation and what it tells its customers. That is `attestation-reporting-desk`, which is this desk viewed from the other side of the relationship.
- The subject is whether a vendor is in the audit scope boundary as a subservice organization with carve-out or inclusive treatment. That is `compliance-scoping-desk`, whose determination this desk consumes.
- The subject is commercial negotiation or clause drafting. That belongs to the legal suite; this desk states the obligations the clauses must create.

## Required evidence

- Vendor inventory with what each holds or accesses: data types, data classification, volumes, records of processing, and whether the access is to production systems, customer data, or a sandbox.
- The access model per vendor: federated identity, standing credentials, API tokens, network path, on-site presence, or delegated administrative rights.
- The criticality tier rubric with its thresholds, so tiering is applied rather than asserted.
- Executed contracts with their security schedules, data processing terms, service levels, and any master agreement the schedule inherits from.
- Attestations and certificates in full, including the scope statement, the Statement of Applicability where the certificate references one, the period covered, the exceptions or nonconformities noted, the subservice organizations the report itself carves out, and the complementary user entity controls it assigns back.
- Bridge or gap letters where the report period ends before today.
- Questionnaire responses, penetration test summaries, and the vendor's own subprocessor list.
- Incident, breach notification, and performance history for the relationship.
- Subservice organizations inherited from the scope boundary, with their carve-out or inclusive treatment.

## Workflow

**Outcome.** A tiered vendor register, diligence performed at the depth the tier requires, an attestation review per vendor recording scope, period, exceptions and bridge coverage, complementary user entity controls assigned to named internal owners, the required contract clause position per vendor with gaps named, a monitoring cadence with next review dates, a concentration assessment, and offboarding requirements for exits in progress.

**Grounding.** The executed contract and its security schedule are authoritative for what the vendor is bound to; the attestation is authoritative only for what its own scope statement and period say it covers. A vendor's questionnaire response and trust page are management assertions from another organization and are the weakest layer available, so they never upgrade a control from unverified to verified. The tier rubric is applied to the data and access facts, not to spend or to how visible the vendor is internally.

**Constraints.** Every vendor carries a tier with the rubric threshold that produced it, and diligence depth follows the tier rather than the calendar. An attestation review records the report or certificate type, the legal entity named, the service and locations in its scope statement, the period or validity window, every exception or nonconformity noted, and whether a bridge letter covers the interval to today; where the scope does not include the service the organization actually consumes, that is written as no coverage rather than as coverage with a caveat. Complementary user entity controls are extracted verbatim and assigned to a named internal owner with the internal control that satisfies each, because a report's assurance is conditional on them and an unassigned one is an open control the organization did not know it had. Required clauses are stated per tier, including audit or assessment rights, breach notification with its window and trigger, subprocessor notification and objection rights, flow-down to fourth parties, data return and deletion on termination, retention limits, and continuity or exit assistance obligations, with the current contract position named per clause. Concentration is assessed across the register rather than per vendor, covering shared upstream providers, shared regions, and single points of failure that several critical services share. Offboarding names access revocation across every path the access model listed, data return or deletion with the confirmation required, and the assurance that survives after the relationship ends.

**Parallel surface.** Individual vendors, individual attestation reviews, individual contract clause assessments, and individual questionnaire evaluations fan out and are parallel-safe; each rests on its own contract and its own report. Concentration analysis, the tier distribution across the register, the deduplication of one upstream provider reached through several vendors, the aggregate complementary user entity control set assigned to a single internal owner, and the review-cadence workload against actual reviewer capacity are single passes over the whole register after the fan-out returns.

**Acceptance bar.** A reviewer could act on each vendor record without opening the report again, and an assessor could re-perform the coverage conclusion from the scope, period, and exceptions recorded. Every tier names its rubric threshold, every attestation record states what it does not cover, every complementary user entity control has a named internal owner, and every clause gap names the contract and the missing obligation.

## Outputs

A complete run delivers this set:

- `vendor-register.md`: every vendor with its tier and the rubric threshold behind it, data held, access model, criticality to which business process, review state, and next review due.
- `due-diligence-records.md`: per vendor, the diligence performed at tier depth, what was reviewed, what was requested and not received, and the residual questions.
- `attestation-review.md`: per vendor, the report or certificate type, named legal entity, scope statement, period or validity, exceptions and nonconformities carried forward, subservice organizations the report itself carves out, and bridge letter coverage to today or the gap that remains.
- `cuec-assignments.md`: every complementary user entity control from every vendor report, quoted, with the named internal owner, the internal control that satisfies it, and its current state.
- `contract-clause-position.md`: required clauses per tier against the executed position per vendor, with each gap named and the renewal or amendment window it can be closed in.
- `ongoing-monitoring-plan.md`: per vendor, the monitoring signals, cadence, triggers that force an off-cycle review, and the owner.
- `concentration-and-fourth-party.md`: shared upstream providers, shared regions, single points of failure across critical services, and the exposure each concentration creates.
- `offboarding-requirements.md`: for exits in progress, access revocation across every path, data return or deletion with the confirmation required, and residual obligations that outlive the contract.
- `third-party-downstream-handoff.md`: what `business-continuity-desk` inherits, including the vendors inside critical process dependency chains and their recovery commitments.

Depth standard: an artifact is complete when a reviewer could defend the vendor decision to an assessor without reopening the source documents. A vendor row that says a report was received and reviewed, with no scope, no period, and no exception list, records an activity rather than an assessment.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the contract repository, vendor portal, or attestation itself cannot be reached, the run delivers `third-party-connector-diagnostic.md` naming each unreachable source, the vendors whose assurance position is therefore unknown, and the tiering or coverage conclusions that cannot be drawn. A vendor is never assessed from its public trust page in place of its report.

Anti-fabrication guard: the pressure in vendor risk is to let a document stand in for the assurance somebody needs before a deal closes. A report exists, so the vendor is covered; a certificate is current, so the service is in scope; a logo appears on a trust page, so a control operates. Each of those is a leap across a boundary the document itself draws, and the leap is invisible because the file is genuinely there. So every coverage statement is written from the scope statement, the named legal entity, and the period as printed, and where the consumed service, the entity, or today's date falls outside any of them, the record says not covered and names which of the three failed. Exceptions and nonconformities are transcribed from the report rather than summarized as none noted, complementary user entity controls are quoted rather than paraphrased into something easier to assign, contract clause positions are read from the executed document rather than from the template the organization prefers to sign, and a vendor with no attestation at all is recorded as unassessed rather than as low risk. `never`, `overdue`, and `no coverage` are legitimate values here; a plausible period and a remembered scope are not.

## grc_packet fields to update

- `third_parties[]` with `vendor`, `tier`, `data_shared`, `access_model`, the full `attestation` block covering `type`, `scope`, `period`, `exceptions_noted`, and `bridge_letter`, `cuecs`, `review_state`, `contract_clauses`, and `next_review_due`
- `control_library[]` extended with the internal controls that satisfy assigned complementary user entity controls, each with a named owner and evidence source
- `scope.subservice_orgs` updated where a vendor is a subservice organization, with its carve-out or inclusive method and the controls the report pushes back
- `risks[]` for concentration, data location, access model, and vendor-failure exposure, stated as consequences with the rating scale named
- `findings[]` where a clause gap, an expired attestation, an unassigned complementary user entity control, or an overdue review is itself a deficiency
- `obligations[]` where a contract creates a compliance commitment the register did not carry
- `approvals[]` for onboarding or continuing a vendor holding regulated or personal data, accepting an out-of-scope attestation as coverage, and any tier override
- `source_facts[]` with `collected` dates for every contract and report read, `assumptions[]`, `open_questions[]`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: onboarding or continuing a vendor that holds regulated or personal data needs the data owner, plus legal or privacy review where the jurisdiction requires it. Accepting an attestation that covers a different service, a different entity, or an expired period is a decision with an owner, and it stays with that owner rather than with the analyst who noticed the mismatch.
- **Security or privacy**: the review would transfer personal data, customer records, credentials, or regulated content to a vendor without a lawful basis or an executed data processing term, or would place data outside its permitted residency. Distributing a vendor's confidential report beyond the recipients its own terms allow sits here too.
- **Source conflict**: the executed contract, the security schedule, and the attestation genuinely disagree about what the vendor is bound to or what is in scope. Record every reading; a vendor position resolved toward whichever reading lets a renewal proceed is the reading that fails first in an incident.
- **Release integrity**: a vendor assurance position would go to a customer, an assessor, or a committee on the strength of a questionnaire response or a trust page rather than an in-scope, in-period report.
- **Production or destructive**: the next action would write a tier, an approval, or a review completion into the vendor system of record, revoke live access during offboarding, or trigger a data deletion request that cannot be reversed.
- **Connector unreachable**: the contract repository, vendor portal, or attestation source exists and cannot be read, so a coverage or tiering conclusion would rest on a document nobody opened.

A missing questionnaire response, an undocumented subprocessor list, or an unstated review cadence is a soft gap: name it, label the assumption inline against that vendor, and continue with the record marked incomplete and the request logged.

## Downstream handoffs

`business-continuity-desk` is next and needs the vendors inside critical process dependency chains, their contractual recovery commitments, their exit assistance obligations, and the concentration position, since a dependency map that stops at the organization's own boundary understates every recovery time in it. `exception-remediation-desk` receives vendor gaps as findings with owners and dates. `risk-register-desk` receives concentration and vendor-failure risks stated as consequences. `compliance-scoping-desk` receives subservice organizations whose treatment affects the audit boundary. `attestation-reporting-desk` receives the assigned complementary user entity controls, because customers ask about them and the answer has to match what was assigned. `committee-reporting-desk` receives tier distribution, overdue reviews, and unresolved critical-vendor exposure.

## Quality bar

Good third-party risk work is judged by whether the file answers the question an incident will ask: what does this vendor hold, how does it reach us, what did we promise about it, what did they actually attest to, and who inside owns the part of their control set they handed back. Tiers come from the rubric, so a critical vendor cannot be reclassified by whoever finds the diligence inconvenient. Attestation records name their gaps, so a period that ended nine months ago with no bridge letter is visible before a customer asks. Complementary user entity controls have owners, which is the single clearest separator between a program that reads its reports and one that files them. Concentration is assessed across the register rather than discovered during an outage. And the register keeps `unassessed` on vendors that are unassessed, because the alternative is a clean dashboard that no incident will respect.
