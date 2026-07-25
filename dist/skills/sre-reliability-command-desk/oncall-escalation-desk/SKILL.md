---
name: oncall-escalation-desk
description: design and review on-call rotations and escalation including coverage and follow-the-sun arrangements, primary and secondary tiers with acknowledgement and response expectations, shift handoff and transfer of open state, page load budget and out-of-hours burden, responder onboarding and shadowing, override and holiday gaps, and the hours or services where a page would reach nobody.
---

# Oncall Escalation Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the on-call artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent responder names, rotation membership, schedule coverage, acknowledgement times, page counts, escalation contacts, contact methods, or compensation arrangements.

## Role

Own the human side of production response: whether a page reaches a person who is awake, authorized, and capable, and whether that person can hand what they know to the next one.

An on-call program has three failure surfaces and they are usually confused with each other. The first is coverage: a rotation with a hole, an override that expired, a service whose escalation policy terminates in an empty schedule, a holiday nobody staffed. The second is load: a rotation that is fully covered and steadily burning the people in it, which shows up as slow acknowledgement, then as attrition, then as an outage where the page was acknowledged and nothing happened. The third is capability: a responder who receives the page, has no context, and lacks the access to act, where the escalation path is the actual mitigation.

This desk works from the paging platform's schedules and escalation policies as configured, not from an org chart or a wiki page. Those two disagree more often than any other pair of sources in this suite, and the gap between them is where the unanswered page lives.

## Use when

- A rotation is being designed, split, merged, or extended to a new service, region, or time zone.
- Page load is over the operational budget, or out-of-hours pages are concentrated on a small number of people.
- An escalation policy needs tiers, acknowledgement timeouts, and response expectations that match severity.
- A page went unacknowledged, escalated to an empty tier, or reached someone who could not act.
- Shift handoff loses open state, and incidents restart their investigation every rotation change.
- A service is being accepted for support, or handed from its owning team to a shared rotation, and the staffing question is real.
- New responders are joining and pager readiness needs defining rather than assumed.

## Do not use when

- The pages are unnecessary and the fix is the alert set: that is `alerting-quality-desk`. Staffing a rotation to absorb noise is the expensive way to solve an alerting problem.
- The responder is reachable and capable but has no procedure to follow: that is `runbook-engineering-desk`.
- Ownership and pager attribution for a service are not established yet: that is `service-tiering-desk`, which assigns the rotation this desk then staffs.
- The manual work between pages is the burden rather than the pages themselves: that is `toil-reduction-desk`.
- Command roles during a live incident, such as who is incident commander and who runs communications: that is `incident-command-desk`. This desk decides who is reachable; that desk decides who is in charge once they answer.

## Required evidence

- Paging platform configuration read as configuration: schedules with their layers and rotation cadence, escalation policies with tiers and acknowledgement timeouts, overrides, and contact methods per responder.
- Page history with timestamps, acknowledgement latency, escalation events, and out-of-hours distribution per person and per rotation.
- The service to rotation mapping, including services whose escalation policy resolves to no schedule.
- Severity definitions and the response expectation attached to each.
- Runbook coverage and the access preconditions responders need, since capability gaps present as escalation volume.
- Team roster, time zones, and leave calendar as they bear on coverage, along with any working-hours, labor, or compensation constraint that binds the schedule.
- Incident records showing where response was delayed and why.

## Workflow

**Outcome.** A rotation and escalation design where every tier resolves to a person who can act, response expectations match severity, page load per responder is stated against a budget, shift handoff transfers open state, onboarding produces pager readiness rather than a calendar entry, and every hour or service where a page would reach nobody is named.

**Grounding.** The paging platform states who is actually on the schedule and who a page actually reaches. Page history states what the rotation actually carries. The roster, leave calendar, and org records state intent and are treated as intent. When the catalog says one team owns a service and the escalation policy routes it elsewhere, both are recorded and the conflict is preserved per `references/suite-workflow-contract.md`, because that gap is the finding rather than a data quality nuisance.

**Constraints.** Every escalation policy terminates in a tier that resolves to a reachable human, with a stated acknowledgement timeout at each step. A policy whose final tier is a schedule with no one on it, a distribution list, or a person who has left is a coverage gap regardless of how many tiers precede it.

Page load is measured and stated per responder per shift, split by in-hours and out-of-hours, because the sleep-interrupting subset is what determines whether a rotation is sustainable. A rotation over budget is reported as over budget with the number, and the remedy is routed to the desk that owns the cause: alert noise to alerting quality, repetitive manual work to toil reduction, an unstable service to resilience or change safety. Adding bodies to absorb a load nobody has diagnosed is recorded as a decision with its cost, not as a fix.

Shift handoff follows a mandated order, and the reason is that the alternative has a specific and repeated failure: the outgoing responder releases the pager and the incoming one discovers an open incident from a customer.

1. The outgoing responder assembles open state before the shift boundary: active incidents with their current mitigation, degraded but unpaged conditions, standing silences and their expiry, changes in flight, and anything deliberately deferred.
2. The incoming responder acknowledges receipt of that state explicitly, in the channel of record rather than verbally.
3. The pager transfers only after that acknowledgement, and the transfer is recorded.
4. Anything unacknowledged at the boundary stays with the outgoing responder until a named person takes it.

**Parallel surface.** Rotations, services, escalation policies, and responders are independent units and are parallel-safe: per-rotation coverage analysis, per-policy tier resolution, per-responder page load computation, per-service escalation mapping, and connector preflight across the paging platform, incident tracker, and service catalog all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: composing coverage across the calendar so overlapping leave, holidays, and time zone boundaries are seen together, ranking coverage gaps by the tier of the journeys behind them, and judging total load across responders who sit on several rotations at once, which is the case that per-rotation analysis always reports as healthy.

**Acceptance bar.** Every service maps to a rotation or appears as unrouted. Every escalation policy resolves to named, reachable tiers with acknowledgement timeouts. Page load is stated per rotation and per responder with the window it was measured over, or stated as unmeasured. Every coverage gap names the hours, the services, and the journeys exposed. Onboarding states what a responder must be able to do before taking the pager, not how long they should shadow.

## Outputs

A complete run delivers this artifact set:

- `oncall-rotation-design.md`: rotations with cadence, layers, participants drawn from the schedule, time zone and follow-the-sun arrangement, primary and secondary responsibilities, and the services each rotation carries.
- `oncall-escalation-policy.md`: tiers with named targets, acknowledgement timeouts, auto-escalation behavior, severity-specific response expectations, the subject matter expert and management escalation paths, and the terminal tier for each policy.
- `oncall-load-report.md`: pages per shift and per responder, out-of-hours and sleep-interrupting share, acknowledgement latency distribution, escalation rate, the load budget in force, and the rotations over it with the driver identified.
- `oncall-coverage-gaps.md`: unstaffed hours, expired overrides, single-responder rotations with no secondary, services routing to empty schedules, contact methods that failed, and the journeys exposed behind each gap.
- `oncall-onboarding-plan.md`: the pager readiness bar as capabilities, the access grants required before a first shift, shadow and reverse-shadow arrangement, and the escalation safety net for a new responder.
- `oncall-downstream-handoff.md`: what `production-readiness-review-desk` and `incident-command-desk` inherit, including whether the rotation can accept a new service and the response expectations command can rely on.

Depth standard per artifact: an escalation entry states the target, the timeout, and what happens on no acknowledgement, not the concept of escalation. A load figure carries the window it was computed over and the query or export it came from. A coverage gap names the specific hours and the specific services, since "weekend coverage is thin" is an impression and "no primary is scheduled between 02:00 and 08:00 UTC on Sundays for the payments rotation" is a finding.

In `diagnostic` mode, when the paging platform, schedule export, or page history exists and cannot be read, the run delivers `oncall-connector-diagnostic.md` naming what was reachable, what was attempted, and the exact access required. Rotation membership and load figures are not composed in that mode.

The fabrication risk here is unusually personal. Every artifact in this desk contains people: who is on the schedule, who answered, who escalated, who is carrying too much. A plausible roster reads perfectly and is wrong in the way that matters, because a rotation assembled from team membership rather than from the paging schedule produces a coverage report that certifies hours nobody is actually watching, and an invented escalation contact is a page that rings out. Every person, schedule entry, override, contact method, and acknowledgement figure in these artifacts comes from the paging platform or is written as unknown with the export that would resolve it. The load numbers carry the same rule and the stakes are the same in the other direction: an estimated page count used to argue a rotation is sustainable is how a team gets told its burnout is not real.

## reliability_packet fields to update

- `oncall.rotations` with cadence, layers, participants, and covered services as configured.
- `oncall.escalation_path` with tiers, timeouts, and terminal targets.
- `oncall.page_load` with pages per shift, out-of-hours share, and the measurement window, or as unmeasured.
- `oncall.handoff` with the transfer ritual and what open state it carries.
- `oncall.coverage_gaps` with the exposed hours, services, and journeys.
- `services[].pager_rotation` and `services[].support_model`, corrected where the escalation policy contradicts the catalog.
- `readiness_gates[]` for the on-call gate, with its state and evidence.
- `reliability_risks[]` for gaps that remain open, with the journeys affected and an owner.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: changing who carries a pager, adding a service to a rotation, extending out-of-hours obligations, or accepting support for a service the receiving team has not agreed to take.
- Production or destructive: the next action would modify a live schedule, escalation policy, override, or notification routing, including a change intended as a correction.
- Security or privacy: the artifact would carry personal contact details, home addresses, medical or leave reasons, or performance judgments about named individuals beyond what the operational record supports.
- Source conflict: the service catalog and the escalation policy disagree about who owns a service, or the schedule and the page history disagree about who was actually on call. Choosing one silently assigns responsibility to a team that has not accepted it.
- Release integrity: an on-call gate would be recorded as passed, or a rotation declared able to absorb a new service, without schedule and load evidence.
- Connector unreachable: the paging platform, schedule export, page history, or service catalog needed for coverage analysis exists and cannot be read.

Unknown individual time zones, an unmeasured acknowledgement distribution, and missing historical override records are soft gaps. Proceed with each named. Coverage is never reported as complete on the strength of a roster, and a load figure is never rounded down to keep a rotation inside its budget.

## Downstream handoffs

`production-readiness-review-desk` needs the on-call gate evidence: whether a staffed rotation with a resolving escalation path exists for the service, and whether the current load leaves room to accept it. `incident-command-desk` needs the escalation tiers, response expectations, and who is reachable now, since command depends on knowing which roles can actually be filled at the current hour. `alerting-quality-desk` receives the load evidence that argues for a page-to-ticket disposition. `toil-reduction-desk` receives the recurring page and ticket classes that consume shift time. `reliability-review-desk` receives page load trend and coverage gaps for the period record.

## Quality bar

Every page reaches someone awake, authorized, and equipped, and every escalation step has a person behind it. The load each rotation carries is a number with a source, the gaps are stated as specific hours against specific journeys, and the handoff means the incoming responder starts the shift knowing what is already broken.
