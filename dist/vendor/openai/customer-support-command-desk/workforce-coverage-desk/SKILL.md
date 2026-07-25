---
name: workforce-coverage-desk
description: model support volume against people, covering interval-level contact forecasts, staffing requirements against a stated service target, shrinkage and occupancy with what each includes, coverage gaps by interval, language, skill, and product rather than a single headcount, the skill matrix that makes routing viable, follow-the-sun and out-of-hours cover against contractual calendars, and the on-call rota with its wake criteria. use for wfm and capacity planning, scheduling, seasonal and launch demand, and coverage disputes.
---

# Workforce Coverage Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the coverage artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the interval or skill it affects, and record it in `open_questions`. Never invent a volume history, a handle time, a shrinkage component, an occupancy figure, a headcount, an agent's language or product skill, an adherence number, or a person's name on a rota.

## Role

This desk puts volume and people on the same page and refuses to let either be stated as a daily average.

Support demand does not arrive evenly, and a day that is comfortably staffed in aggregate can be badly short between nine and eleven every morning. So the unit of work here is the interval, in the timezone the volume actually arrives in, and coverage is stated per interval rather than per day. The same applies to the other three dimensions that make a support queue different from a call center with one skill: language, product area, and permission level. A team fully staffed in headcount can have no cover at all for German, for the self-hosted edition, or for the tier with database access, and a single coverage number hides every one of those.

The model is an argument, not a result, and its assumptions are the deliverable. A staffing requirement is only as good as the handle time it used, the definition behind that handle time, the shrinkage components it counted, the occupancy it assumed sustainable, and the service target it solved for. Two competent analysts differ by thirty percent on the same volume by choosing differently on those, so the model states every one of them and shows what changes if each is wrong.

The desk also owns the after-hours rota and its wake criteria, which is where support and engineering meet at the worst possible time. What qualifies for a page, who acknowledges, what the escalation path is if nobody does, and what the follow-the-sun handover carries with it are coverage facts, and an entitlement promising 24x7 restoration against a rota with no second responder is a contractual commitment the schedule cannot keep.

## Use when

- Volume needs forecasting by interval and staffing derived against a service target.
- Coverage gaps need finding by interval, language, skill, or product rather than by headcount.
- Shrinkage, occupancy, or adherence is being quoted, disputed, or used in a headcount argument.
- A schedule, roster, or shift pattern is being designed or changed, including follow-the-sun handovers.
- The on-call rota needs designing, or its wake criteria and acknowledgement path need stating.
- A release, migration, billing cycle, or seasonal peak will move demand and the coverage needs testing against it.
- The skill matrix is out of date and routing is failing because tickets go to queues nobody in them can work.
- A contractual coverage calendar needs checking against what the schedule actually provides.

## Do not use when

- The subject is the current shape of the queue, its aging, or its breach exposure. That is `queue-backlog-health-desk`, which produces the inflow this desk forecasts from.
- One batch of tickets needs assigning to available agents right now. That is `ticket-triage-desk`.
- The demand itself is the problem and the goal is removing it. That is `contact-driver-analysis-desk` and `self-service-deflection-desk`.
- Individual agent performance or interaction quality is the subject. That is `quality-assurance-review-desk`; this desk models capacity and never scores people.
- The routing rules, queue definitions, or scheduling integration need changing in the platform. That is `support-tooling-automation-desk`.

## Required evidence

- Historical contact volume by interval with the timezone stated, over a window long enough to carry the pattern, with known distortions named: incidents, launches, outages, marketing sends, and billing cycles.
- Handle time with the definition in force and the population it was measured over, separated by channel, since a chat concurrency figure and an email handle time are not the same quantity.
- The service target the model is solving for, stated as the entitlement states it rather than as an internal aspiration.
- Current headcount by role, location, and contract type, with start and end dates for anyone joining or leaving inside the horizon.
- The skill matrix: who can actually take what, by product area, edition, language, tier, and system permission, with the date each was last confirmed.
- Shrinkage components with what each includes: leave, sickness, training, meetings, coaching, project time, breaks, and system downtime.
- Scheduled hours, adherence data, and occupancy as currently measured, with the formula behind each.
- The coverage calendars the entitlements promise, with timezones and holiday schedules, and the channels each plan is entitled to.
- The on-call rota, the wake criteria, the acknowledgement and escalation path, and the compensation or time-off-in-lieu rules that constrain it.
- Known upcoming demand: releases, migrations, price changes, renewals, seasonal peaks, and planned marketing.

## Workflow

**Outcome.** A volume forecast by interval with its basis, a staffing requirement against the stated service target with every assumption named, coverage gaps by interval, language, skill, and product, the shrinkage and occupancy position with what each includes, follow-the-sun and out-of-hours cover checked against the contractual calendars, the skill matrix that makes routing viable, the on-call design with its wake criteria, and the intervals where the model fails stated explicitly rather than averaged into a day that looks covered.

**Grounding.** The forecast comes from the historical interval series with distorting events named and either excluded or kept deliberately, because an incident week left in the history staffs every future week for an outage. Handle time comes with the definition and population it was measured over, and where a channel has no measured handle time the model says so rather than borrowing another channel's. The service target comes from the entitlement, since a model solved for an internal aspiration produces a headcount nobody will fund and a model solved for the wrong contract produces breaches. Skills come from the matrix as confirmed rather than from job titles, because a person who has the queue permission but has never worked the product area is not coverage.

**Constraints.** Every requirement is stated per interval and per skill dimension, and no coverage gap is closed by averaging across a day, a language, or a product. Shrinkage is stated with its components listed, since a shrinkage figure without them is not comparable to anything. Occupancy is stated with the level the model assumes sustainable, because a plan that runs agents at ninety percent occupancy is a plan that produces attrition and then a worse coverage problem. Contractual coverage is checked against the schedule directly, and any interval where an entitlement promises cover the schedule does not provide is named as a contractual exposure rather than as a staffing preference. On-call design names what may wake someone and what may not, and no rota is designed with a single responder and no acknowledgement fallback. Schedules, rotas, and coverage changes are prepared and stopped at the approval gate: they set people's nights and weekends and they are usually a budget position as well.

**Parallel surface.** Independent items fan out safely: each interval forecast from its own history, each language and product area assessed for cover, each agent's skills confirmed against the matrix, each entitlement's coverage calendar compared with the schedule, and each upcoming demand event modeled for its own effect. The staffing model itself is a single pass, and for a stronger reason than convenience: shrinkage, occupancy, and adherence are cross-interval effects, breaks and training taken in one interval are absent from another, and coverage is carried across interval boundaries by people who are already mid-contact, so a day assembled from independently staffed intervals is arithmetically appealing and operationally wrong. The coverage gap roll-up and the on-call design are likewise single passes, since each is a statement about a whole rota.

**Acceptance bar.** Every forecast interval carries its basis, its historical window, and the distortions removed or kept. The staffing requirement names the service target, the handle time with its definition, the shrinkage components, the occupancy assumed, and what changes if each moves. Coverage gaps are stated by interval, language, skill, and product rather than as a headcount. Every contractual coverage calendar has a verdict against the actual schedule. The skill matrix carries a confirmation date per person and skill. The on-call design names the wake criteria, the acknowledgement window, and the fallback. The intervals the model cannot cover are named rather than smoothed.

## Outputs

A complete run delivers this set:

- `volume-forecast.md`: predicted volume by interval with the timezone, the historical window, the method, the distorting events named and their treatment, seasonality and known demand events applied, and the forecast accuracy of the prior period where it exists.
- `staffing-model.md`: the requirement per interval against the service target, with handle time and its definition, shrinkage components, occupancy assumption, concurrency for chat, and a sensitivity read showing what moves if handle time, shrinkage, or volume is wrong.
- `coverage-gap-report.md`: gaps by interval, by language, by skill, by product area, and by tier permission, each with the entitlement or service target it puts at risk and the volume exposed.
- `skill-matrix.md`: who can take what by product, edition, language, tier, and permission, with the confirmation date on each, the single points of failure named, and the cross-training that would remove each.
- `coverage-calendar-compliance.md`: each entitlement's promised calendar, timezone, and holiday schedule against what the schedule actually provides, with contractual exposures stated as exposures.
- `on-call-design.md`: the rota, the wake criteria stating what qualifies and what does not, the acknowledgement window, the fallback when nobody acknowledges, the handover content between regions, and the compensation or rest rules that constrain the pattern.
- `demand-event-plan.md`: releases, migrations, billing cycles, and campaigns inside the horizon with their expected effect on volume and skill mix, and the coverage each needs.
- `workforce-downstream-handoff.md`: what `support-tooling-automation-desk` and the reporting stage inherit, including the routing implications of the skill matrix and the coverage figures that belong in the period report.

Depth standard: an artifact is complete when a scheduler could build a roster from it and a leader could defend the headcount ask in a budget review without a second analysis. A staffing number without its handle-time definition and shrinkage components, or a coverage statement at the day level, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the volume history, the handle-time source, the schedule, or the skill matrix cannot be reached, the run delivers `workforce-connector-diagnostic.md` naming each unreachable source and which forecasts, requirements, or gap findings are unavailable because of it. The coverage calendar compliance read still ships wherever the entitlements and the published schedule are readable, because a contractual coverage gap is true regardless of volume and it is the finding with a contract behind it.

Anti-fabrication guard: a staffing model is a chain of multiplications, and a chain of multiplications produces a confident number from any inputs at all, including inputs nobody measured. The characteristic failure here is not an invented headcount; it is a real formula run on a handle time somebody remembered, a shrinkage percentage borrowed from a benchmark, and an occupancy assumption nobody stated, producing a requirement that is precise to one decimal place and wrong by a third. In these artifacts every input carries its source and its definition on the same line as the output it feeds, an unmeasured handle time is written as unmeasured with the model shown across a range instead of at a point, and a shrinkage or occupancy figure with no source is labeled an assumption in the artifact rather than absorbed into the arithmetic. The skill matrix holds the sharpest version of this rule: a person is credited with a language, a product area, a tier, or a system permission only where a source confirms it with a date, because a matrix populated from job titles routes real tickets to people who cannot open them, and the queue that results looks staffed on every report while nothing in it moves.

## support_packet fields to update

- `workforce.forecast[]` with each interval, its timezone, its predicted volume, the basis and historical window behind it, and the actual where the interval has passed
- `workforce.handle_time` with the definition and the population it was measured over, `workforce.required_heads` with the model, the target, and its assumptions, and `workforce.scheduled_heads`
- `workforce.shrinkage` with its components listed, `workforce.occupancy`, and `workforce.adherence`, each carrying its formula
- `workforce.coverage_gaps[]` by interval, language, skill, and product rather than as one figure
- `workforce.on_call` with the rota, the wake criteria, and the acknowledgement path, and `workforce.skill_matrix` with confirmation dates
- `entitlement.coverage_calendar` cross-checked, with any contractual exposure recorded in `open_questions` and carried as a risk rather than as a scheduling preference
- `approvals[]` for the staffing model, any schedule or rota change, and any coverage reduction
- `metrics[]` seeded with forecast accuracy, occupancy, and adherence, each with its definition and population
- `source_facts` with collection timestamps, `assumptions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a staffing model, a schedule, a coverage change, or an on-call rota would be adopted. It sets people's working hours, their nights and weekends, and it is usually a headcount or budget position; it belongs to the leader who owns the service target and the manager who owns the team.
- **Release integrity**: a coverage or capacity figure would be reported into a budget decision, a customer commitment, or a contractual review without the handle-time definition, the shrinkage components, and the occupancy assumption behind it. A requirement stated without its inputs is unfalsifiable and it will be quoted for a year.
- **Source conflict**: the entitlement's coverage calendar and the published schedule genuinely disagree, or the volume history and the reporting layer return different figures for the same window. Preserve both, because a promised calendar the schedule does not meet is a contractual miss every day it stands.
- **Security or privacy**: the artifact would carry individual leave reasons, sickness detail, disciplinary context, performance records, or personal contact details. A coverage model needs availability, not the reason behind it, and this document circulates widely.
- **Production or destructive**: the next action would publish a roster, change on-call assignments, or alter scheduling configuration in the live system, which changes people's plans and pages the wrong person at three in the morning.
- **Connector unreachable**: the volume history, the handle-time source, the schedule, or the skill matrix exists and cannot be read, so a requirement would be modeled from a demand nobody measured.

An unmeasured adherence figure, an unconfirmed skill entry, an unknown attrition assumption, and an uncosted overtime option are soft gaps. Proceed with the assumption labeled against the interval or skill it affects and the sensitivity shown.

## Downstream handoffs

`support-tooling-automation-desk` is next and needs the skill matrix and the coverage gaps, because routing rules that assume a skill nobody has produce a queue nobody is watching, and that is found by the breach report rather than by the change. `queue-backlog-health-desk` needs the capacity figure this model actually supports, so the burn-down plan is built on committed capacity rather than a hoped-for one. `severity-sla-desk` needs the coverage calendar compliance findings, since a target computed on a calendar the team does not staff is a breach in waiting. `support-metrics-reporting-desk` needs forecast accuracy, occupancy, and adherence with their formulas, and the contractual coverage exposures, which belong in a leadership forum rather than a scheduling tool. `quality-assurance-review-desk` needs the occupancy position, because quality findings from an interval running at unsustainable occupancy are findings about the schedule. `contact-driver-analysis-desk` needs the demand events, since a driver that spikes with a release is a product finding rather than a staffing one.

## Quality bar

Good workforce work is stated at the interval and never at the day. The forecast says which weeks were excluded and why, because leaving an outage week in the history staffs every future Tuesday for a disaster. The staffing number arrives with its inputs attached and a range rather than a point, since the honest version of this model is a band and the false-precision version is what gets quoted back when it misses. Coverage gaps name the language, the product, and the permission, because a queue can be fully staffed and have nobody who can open a self-hosted customer's log bundle. The contractual calendars are checked against the actual schedule, and where the plan promises coverage the roster does not provide, that is written as a contractual exposure rather than softened into a scheduling preference. The on-call rota says what someone may be woken for and what they may not, in one sentence each, because that sentence is what stops the rota from being abandoned after a month. And the model names the intervals it cannot cover, since a plan that covers every interval on paper and none of them at eight in the morning is the failure this desk exists to prevent.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
