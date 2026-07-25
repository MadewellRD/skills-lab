---
name: incident-command-desk
description: run a live production incident with severity declaration, incident commander and operations communications and scribe roles, evidence capture before any mitigating restart, reversible mitigation preferred over diagnosis, internal and customer communication cadence including the status page, a reconciled timeline, command handoff across shifts, and recovery confirmed against the journey sli rather than the symptom that paged.
---

# Incident Command Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the incident artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent timestamps, severities, customer impact figures, mitigation outcomes, role assignments, status page content, or the sequence of events between two observations.

## Role

Own production while it is broken. This desk runs the incident: it declares severity, names who holds each role, decides what stops user harm, keeps the outside world honestly informed, and produces a record the organization can learn from afterward.

The structure exists because incident response fails in predictable social ways rather than technical ones. Everyone investigates and nobody decides. Two responders independently restart the same component and the timeline becomes unreconstructable. The person deepest in the debugging is also the person answering executives, so both suffer. Twenty minutes pass with no external update and the support queue fills with customers who know less than they should. Command separates deciding from doing from communicating, and it does so before anyone is tired.

The single most consequential judgment here is mitigation over diagnosis. Understanding the cause is not a prerequisite for stopping user harm, and the reversible action almost always wins: roll back, flip the flag, drain the zone, shed the load, fail over to the healthy replica. The instinct to find the cause first is what turns a fifteen minute incident into a two hour one.

## Use when

- A user journey is degraded or unavailable now, whether a signal fired or a customer reported it.
- A page has been acknowledged and the responder needs command structure because the scope exceeds one person.
- Severity needs declaring, or an existing severity needs raising as scope becomes clear.
- Communication is required: internal stakeholders, the status page, support, or account teams.
- A mitigation decision carries risk and the reversible option needs choosing deliberately.
- An incident is crossing a shift boundary and command must transfer without losing state.
- Recovery looks complete on a dashboard and someone needs to confirm it against the journey the user actually performs.

## Do not use when

- The event is over and the question is what to learn: that is `postmortem-desk`, which starts from the timeline this desk preserves.
- Nothing is degraded and the concern is that a failure would go undetected: that is `alerting-quality-desk`.
- The responder is capable and the missing piece is the procedure: that is `runbook-engineering-desk`, whose output this desk consumes rather than authors.
- The incident is a planned change going badly and it can still be stopped before user impact: that is `change-safety-desk` and its abort criteria.
- The event is a security compromise, data exposure, or suspected breach: this desk continues to run the availability response, and the security response hands to the Security suite in parallel as an additive cross-suite handoff rather than a transfer of command.

## Required evidence

- The triggering signal or report with its timestamp and its detection source.
- Severity definitions and the declaration authority.
- The affected journey, its tier, its SLI, and its current measured state.
- Recent change history: deploys, flag flips, configuration pushes, migrations, certificate rotations, and infrastructure changes in the preceding window.
- The dependency graph along the affected journey, and the status of every hard dependency including third parties.
- Runbooks for the alerts that fired and for the failure modes in play.
- Escalation tiers and who is reachable at the current hour.
- Communication policy: internal cadence, status page authority, and the customer notification obligations that apply.

## Workflow

**Outcome.** User impact stopped, recovery confirmed against the journey SLI, an evidence set preserved that supports a real postmortem, a communication record that matches what actually happened, and a packet the review stages can act on without reconstructing the event from memory.

**Grounding.** The metrics backend, traces, logs, and synthetic probes state what the system is doing. The change history states what was done to it. The paging platform states when someone was told. The scribe log and incident channel state what responders believed at each moment, which is narrative rather than system state and stays labeled as such. Third-party status pages are claims by a vendor and are recorded with attribution, not adopted as fact. Where the dashboard and the customer report disagree, both are recorded per `references/suite-workflow-contract.md`, because a green dashboard during a real outage is a measurement finding.

**Constraints.** One incident commander at a time, holding the decision and not the keyboard. Roles are named explicitly rather than assumed: operations lead executing changes, communications lead owning internal and external updates, scribe holding the timeline. In a small incident one person may hold several roles, and saying which roles are merged is part of declaring the incident.

Every change made during an incident goes through one place and into the log, with who made it and when. Parallel investigation of hypotheses is expected and encouraged; parallel mutation is not, because two responders restarting components independently produce an incident nobody can reconstruct and a mitigation nobody can attribute.

The live incident order is mandated, and the reason is stated here so a future editor does not read it as ceremony: each step either preserves or destroys the evidence the next one needs, and a mitigation applied before impact is scoped can widen the blast radius rather than close it.

1. Declare severity and name the incident commander before parallel diagnostic work begins.
2. Capture the failing state before any restart, replacement, failover, scale action, or rollback: metric snapshots with their window, log and trace samples, heap and thread state where relevant, queue depths and saturation signals, and the list of changes in the preceding window.
3. Mitigate to restore the journey, preferring the reversible action over the diagnostic one.
4. Confirm recovery against the SLI that defines the journey, not against the symptom that paged.
5. Preserve the timeline, evidence, and change record before the incident channel closes.

Step 2 is the only opportunity to collect state a restart erases, and step 4 exists because a recovered dashboard and a recovered user are routinely different things. Destructive recovery actions such as failover, restore over live data, and snapshot deletion follow the separate ordered sequence in `references/suite-workflow-contract.md`.

Communication runs on a clock rather than on progress. An update at the stated cadence saying the cause is not yet known is a successful update; silence while responders work is the failure. External communication states impact and expected next update, and never states a cause that has not been established.

**Parallel surface.** Hypotheses, dependencies, services, and evidence collection tasks are independent and are parallel-safe: fanning out across dependency status checks, change history queries, log and trace sampling, per-service saturation reads, and third-party status verification is exactly the right use of responders and of connector access.

The aggregate is deliberately single-threaded and is the one place in this suite where that is the point: severity, the timeline, the mitigation decision, the record of what was changed, and every external communication reconcile through the incident commander and the scribe. An incident with two timelines has none.

**Acceptance bar.** Severity is declared with the definition it was declared under. Every role is held by a named person or explicitly merged. Evidence for the failing state exists before the first mutating action, or its absence is recorded as a gap in the timeline. Every change made during the incident appears in the log with its actor and timestamp. Recovery is confirmed against the journey SLI with the measurement, not against the alert clearing. Every external statement issued is in the record.

## Outputs

A complete run delivers this artifact set:

- `incident-record.md`: identifier, severity with its basis, affected journeys and services, detection source and time, current status, command roles as held, and the mitigation applied.
- `incident-timeline.md`: timestamped events from evidence, distinguishing system observations from responder actions from beliefs held at the time, with explicit gaps where nothing was recorded.
- `incident-evidence-index.md`: what was captured before mitigation, where it is stored, its retention expiry, and what was not captured because the action could not wait.
- `incident-communications-log.md`: every internal update and external statement with timestamp, audience, and author, including status page transitions and the next-update commitment made each time.
- `incident-impact-assessment.md`: journey degradation with the SLI measurement behind it, duration, error budget consumed, and the affected population as measured or as explicitly unquantified.
- `incident-handoff.md`: for a command transfer, the current hypothesis set, actions taken, actions in flight, what has been ruled out, outstanding approvals, and the communication commitments the incoming commander inherits.
- `incident-postmortem-seed.md`: what `postmortem-desk` needs while it is still recoverable, including evidence retention deadlines.

Depth standard per artifact: a timeline entry carries a timestamp, a source, and what was observed rather than what was concluded. An impact figure carries the query behind it. A communication entry carries what was actually said. "Investigated the database" is not a timeline entry; the query that was run, when, and what it returned is.

In `diagnostic` mode, when the metrics backend, logs, or change history exists and cannot be read, the run delivers `incident-connector-diagnostic.md` naming what was reachable and what access is required. The incident still proceeds; mitigation does not wait for a connector, and the artifact records that the response ran without that evidence.

Incidents fabricate through the timeline, and the damage is specific and lasting. Nobody logs the minutes between 02:14 and 02:47, and a fluent reconstruction of those minutes reads better than the truth, gets adopted into the postmortem, and becomes the organization's permanent memory of the outage, including the causal story it implies. So a timeline here is built only from timestamped evidence and stops where the evidence stops, with the gap marked as a gap. The same applies to the two other numbers this desk is asked for under pressure: customer impact is measured or written as unquantified, never estimated into a status update; and a cause is never stated externally, or internally as fact, until evidence supports it, because a retracted cause costs more trust than a slow one.

## reliability_packet fields to update

- `incidents[]` in full: `id`, `severity`, `status`, `detected_at`, `detection_source`, `time_to_mitigate`, `journey_impact`, `budget_impact`, and `commander`.
- `operating_posture` set to `active_incident`, then to `post_incident` on resolution.
- `slos[].error_budget_remaining` and `burn_rate` with the consumption this incident caused and the window.
- `failure_modes[]` with the mode observed, its actual propagation, and whether the expected detection worked.
- `resilience_controls[].evidence` where a control was proven or disproven under real load.
- `alerts[].signal_quality` where a rule caught the incident, fired late, or did not fire.
- `runbooks[].last_validated` and `gaps` where a runbook was used, and where it was wrong.
- `change_controls.rollback_tested` where a rollback was actually executed during the incident.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: declaring the incident resolved, publishing customer-facing communication or a status page update, initiating failover, or accepting a mitigation whose blast radius exceeds the commander's authority.
- Production or destructive: the next action would fail over, restore over live data, delete or truncate data, replace stateful nodes, remove capacity, or take an irreversible step whose recovery path is unproven. Mitigation is expected during an incident; the irreversible subset still requires its approval and the ordered sequence in `references/suite-workflow-contract.md`.
- Security or privacy: the incident shows signs of compromise, credential exposure, or unauthorized data access, or captured evidence contains personal data or secrets that would be distributed by attaching it. Hand to the Security suite in parallel while availability response continues.
- Source conflict: monitoring says recovered and customers say degraded, or the change history and the responder account disagree about what was changed. Declaring resolution on the convenient source ends the incident while users are still affected.
- Release integrity: recovery would be declared, or an all-clear communicated, without an SLI measurement supporting it.
- Connector unreachable: the metrics backend, change history, or paging platform needed to scope impact exists and cannot be read, and the scope claim would otherwise be asserted anyway.

Unknown root cause, an unquantified affected population, and missing evidence for a component that had to be restarted immediately are soft gaps. Proceed with each named in the timeline. Mitigation is never delayed for a soft gap, evidence capture is never skipped for speed on an action that can wait sixty seconds, and an incident is never downgraded in severity to reduce the communication obligation.

## Downstream handoffs

`postmortem-desk` needs the timeline, the evidence index with its retention deadlines, the impact assessment, the change correlation, and the actions taken with their outcomes. `alerting-quality-desk` needs the detection story: what fired, what fired late, and what should have fired. `runbook-engineering-desk` needs the steps that were wrong or missing. `change-safety-desk` needs the rollback outcome and any change that contributed. `oncall-escalation-desk` needs the escalation experience, including tiers that did not respond. Defect triage and the code fix hand to the SDLC suite as a labeled cross-suite handoff; a security dimension goes to the Security suite additively.

## Quality bar

User harm stopped early because someone chose a reversible action instead of waiting for understanding, one commander deciding and one timeline recording, external updates that arrived on the clock and said only what was known, recovery proven against the journey rather than the graph, and a postmortem that starts from preserved evidence instead of from what people remember three days later.
