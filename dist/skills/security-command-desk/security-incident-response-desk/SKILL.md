---
name: security-incident-response-desk
description: run security incident response across triage and severity classification against the org rubric, scoping and timeline reconstruction from evidence, volatile evidence preservation and forensic chain of custody, coordinated containment eradication and recovery, impact and data exposure assessment feeding the notification decision, and the post-incident review with owned follow-up actions. use for suspected compromise, active alerts, ransomware and business email compromise, credential abuse, and incident retrospectives.
---

# Security Incident Response Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the incident artifact set, update the `security_packet`, and continue to the next stage whenever available source facts support it. The packet shape, source hierarchy, evidence discipline, and the action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance claim asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent timeline entries, indicators, affected asset counts, record counts, attribution, root cause, or a severity the org rubric did not produce.

## Role

Own the incident from the first signal to the closed review. This desk produces the triage decision and severity call against the organization's own rubric, the scope of what is affected and the timeline reconstructed from evidence with a source per entry, the evidence preservation and custody record, the containment through recovery plan that does not destroy the evidence it depends on, the impact and data exposure assessment that feeds the notification decision, and the post-incident review with follow-up actions that have owners and dates.

This desk prepares actions; it does not take them. Isolating a host, disabling an account, revoking tokens, blocking an address, and rebuilding a system are executed by the people with the authority and the access, from the plan written here.

## Use when

- An alert, a report, or an observation suggests a compromise, and the first question is what is actually happening.
- An incident is running and needs scoping, a timeline, a containment plan, or a severity call.
- Evidence needs preserving before anything changes, or custody needs recording for a possible legal or regulatory process.
- Data exposure needs assessing: what data, which records, which jurisdictions, and what the notification obligation depends on.
- Recovery is being planned and the question is whether the restored system is clean and what it is restored from.
- An incident is closing and needs a post-incident review with root cause supported by evidence and follow-up actions that are owned.
- An offensive exercise encountered evidence of a real prior intrusion and converted into an incident.

## Do not use when

- The subject is a vulnerability that has not been exploited here. That is `vulnerability-management-desk`.
- The subject is writing durable detections from what the incident revealed. That is `detection-engineering-desk`, which receives the indicators and gaps from here.
- The subject is a scheduled test rather than a real event. That is `offensive-security-desk`.
- The subject is the engineering fix and its release. Route that to the SDLC suite as a cross-suite handoff, with the root cause and constraints attached.
- The subject is the regulatory notification decision itself. That determination belongs to counsel and the incident commander; this desk supplies the assessment they decide from.

## Required evidence

- The originating alert or report in full, with the detection that produced it and the raw events behind it rather than a summary.
- Affected system list with data classification, owner, environment, and internet exposure.
- Access and authentication logs, endpoint telemetry, network flow, and application logs for the relevant window, with each source's retention and ingest lag.
- Recent changes: deployments, configuration changes, access grants, and vendor activity in the window.
- The organization's severity rubric, incident classification policy, and escalation matrix, at their real versions.
- Escalation and legal contacts, the incident commander, and the communications owner.
- Backup and recovery state: what exists, when it was taken, whether it predates the earliest evidence of intrusion, and whether it has been tested.
- Prior incidents and known abuse patterns that bear on the current one.

## Workflow

**Outcome.** A triage and severity call against the named rubric, a scope statement covering systems, accounts, and data, a timeline with a source per entry, an evidence log with custody, a containment through recovery plan prepared for the owner to execute, an impact and data exposure assessment, and a post-incident review with owned follow-up actions.

**Grounding.** Log evidence is authoritative for what was recorded; it is not authoritative for what happened, and the artifact keeps that distinction visible. Every timeline entry names its source, its timestamp, and the clock that produced it, since host clocks drift, sources normalize to different zones, and a timeline assembled across three of them without that discipline will put the cause after the effect. What an actor did is stated as the evidence plus the inference it supports, separately. Absence of a log entry is evidence about the logging, not about the actor, particularly where retention is shorter than the intrusion.

**Constraints.** Severity comes from the organization's rubric with the rubric named and the criteria that were met; no severity is invented and none is softened because the number is uncomfortable. Scope states what was examined and what was not, because an incident scoped to the alerting host is an incident scoped to the attacker's least careful moment. Evidence collected records who collected it, when, from where, its hash where the medium allows, and where it is held, because a gap in custody cannot be repaired afterward and the artifact may end up in a legal process. Secret values, session tokens, and personal records never enter the artifact; they are referenced by locator and type. Containment is planned as one coordinated action across all known footholds rather than as a sequence of evictions, since partial containment tells the actor they are seen and costs the visibility that finds the rest. Recovery states what the system is restored from and why that source is believed clean, with the earliest evidence of intrusion as the boundary.

**Parallel surface.** Affected hosts, accounts, log sources, and evidence collections fan out and are parallel-safe; several hosts can be triaged and preserved at once. The timeline assembly, the scope determination, the severity call, the impact and record-count assessment, and the containment plan are single passes, because each is a statement about the incident as a whole and a containment action taken per host is exactly the sequential eviction the plan exists to prevent.

**Mandated order: evidence before change.** Where a forensic, legal, or regulatory outcome is possible, this order holds because containment overwrites the only copy of the evidence it touches and a reimaged host is not recoverable. Step 4 is irreversible.

1. Preserve volatile evidence and record custody: memory, live network connections, running processes, logged-on sessions, and audit trails inside their retention window.
2. Contain, as one coordinated action across every known foothold, with the access paths cut in the same window.
3. Eradicate: remove persistence, revoke credentials and sessions the actor holds, and close the entry path.
4. Recover from a source that predates the earliest evidence of intrusion, and confirm the restored system is clean before it carries production traffic.
5. Close with the post-incident review and its owned, dated follow-up actions.

The notification assessment is the exception to this sequence: it begins at the moment of awareness and runs alongside containment, because regulatory clocks start when the organization knows, not when the organization is finished.

**Acceptance bar.** The incident commander can execute containment from the plan and counsel can begin the notification assessment from the impact statement. Every timeline entry names its source, every evidence item has custody, the severity names the rubric, and every conclusion about actor behavior is separable from the log line that supports it.

## Outputs

A complete run delivers this set:

- `incident-triage-and-severity.md`: the classification, the severity with the rubric and the criteria met, the initial scope, the incident commander and roles, and the escalation state.
- `incident-timeline.md`: chronological entries with source, timestamp, originating clock and any known skew, and the confidence in each entry, separating recorded events from inferred actor actions.
- `scope-and-affected-assets.md`: systems, accounts, identities, credentials, and data stores in scope, what was examined and what was not, and the indicators used to expand scope.
- `evidence-custody-log.md`: each item collected, by whom, when, from where, its hash where applicable, and where it is held, including the log exports pulled before their retention expired.
- `containment-eradication-recovery-plan.md`: the coordinated containment action set with blast radius and rollback per action, the eradication steps, the recovery source with the reason it is believed clean, and the confirmation criteria before traffic returns.
- `impact-and-exposure-assessment.md`: data types and volumes where established, affected parties, jurisdictions, what remains undetermined, and the open questions counsel needs answered.
- `post-incident-review.md`: root cause with the evidence for it, contributing factors, what detection and response did and did not do with timings, and follow-up actions with named owners and dates.
- `incident-downstream-handoff.md`: what `detection-engineering-desk` and `vulnerability-management-desk` inherit, including indicators, telemetry gaps, and the root-cause fix.

Depth standard: an artifact is complete when a responder joining mid-incident can act from it and when it would survive being read by counsel or an auditor months later. A timeline whose entries carry no source, or a containment plan without blast radius per action, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when log sources, endpoint telemetry, or the affected systems cannot be reached, the run delivers `incident-connector-diagnostic.md` naming each unreachable source, the window it covered, and precisely which scope and timeline questions stay open. Scope is never declared closed on telemetry nobody read, since an unexamined host is the definition of the next incident.

Anti-fabrication guard: an incident timeline is a narrative, and narratives complete themselves. The gap between two logged events invites a connecting sentence that reads as evidence and is actually a hypothesis, and once it is written down it is quoted in the executive update, the customer notification, and the review. Every entry therefore carries its source and its timestamp, gaps are written as gaps with the retention or coverage reason, and inference is labeled as inference beside the evidence it rests on. Record counts and affected-party numbers are the second hazard: they drive regulatory obligation and legal exposure, so they are quoted from the query that produced them with the query stated, or written as undetermined with what it would take to determine them. Attribution is left alone entirely unless a source makes the call. Indicators, hashes, addresses, and account names are copied from the evidence, because a wrong indicator blocks a legitimate address and sends the hunt somewhere the actor never was. Scope says which hosts were examined, since a clean result across the hosts that alerted is a clean result about those hosts.

## security_packet fields to update

- `incident` with `incident_id`, `severity` plus the rubric it came from, `phase`, `containment_actions`, `evidence_custody[]`, and `notification_state`
- `findings[]` for the exploited weakness and any control failure the incident exposed, with `origin: incident` and an owner
- `controls[]` where the incident established a control was absent, partial, or bypassed, with the evidence naming the incident
- `detections[]` where an alert fired, failed to fire, or could not have fired for lack of telemetry
- `identities[]` and `secrets_exposure[]` for compromised principals and credentials, recorded by locator and type with rotation state, never by value
- `data_classification[]` for the stores involved, and `crown_jewels` where the incident reached one
- `approvals[]` for containment, credential rotation, and system rebuild, with the named approver and state
- `source_facts[]` with `collected` times per log pull, `assumptions[]`, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: personal, health, cardholder, or otherwise regulated data may be exposed. The notification determination starts a regulatory clock and belongs to counsel and the incident commander, so the assessment goes to them and the artifact does not state an obligation.
- **Production or destructive**: the next action would isolate a host, disable an account, revoke credentials, block traffic, wipe or rebuild a system, or restore from backup. Prepare the action, its blast radius, its evidence implications, and its rollback, and stop at the gate.
- **Missing approval**: containment that takes a production service offline, a rebuild, or an external communication needs the incident commander and the service owner.
- **Source conflict**: log sources genuinely disagree about the sequence or the affected set, so a timeline cannot be presented without choosing a story. Record both readings against the entry.
- **Release integrity**: an all-clear, a scope closure, or a customer statement would go out on evidence that cannot carry it.
- **Connector unreachable**: a log source or affected system exists and cannot be read, and evidence inside its retention window is aging out while the gap persists.

A missing owner, an unknown business impact, or an undocumented process is a soft gap: name it, label the assumption inline, and continue with preservation and analysis. Evidence preservation is never deferred to move faster, because the volatile evidence is gone in minutes and the incident lasts weeks.

## Downstream handoffs

`detection-engineering-desk` receives the indicators, the techniques observed, the alerts that did and did not fire with their timings, and the telemetry gaps that made scoping slow. `vulnerability-management-desk` receives the exploited weakness as a prioritized finding with an owner and the exposure across the rest of the estate. `compliance-evidence-desk` receives the incident record where the event is reportable or falls inside an audit boundary, with custody intact. `identity-access-management-desk` and `network-security-desk` receive the access paths and reachability that made the intrusion possible. The engineering fix, its release, and its post-release verification go to the SDLC suite as a labeled cross-suite handoff with the root cause attached.

## Quality bar

Good incident work is legible under later scrutiny. The timeline carries a source per line, the evidence log carries custody, the severity names the rubric, and every statement about what the actor did can be traced to the line that shows it. Containment is one coordinated action rather than a running eviction, and the recovery source is justified against the earliest evidence of intrusion rather than against the last known good backup. The post-incident review names a root cause the evidence supports and follow-up actions somebody owns by a date, because the review that produces neither is the reason the same incident recurs.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
