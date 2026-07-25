---
name: committee-reporting-desk
description: build governance forum reporting for a risk committee audit committee or board across metrics carrying value computed basis and as-of date, risk and control health presented against appetite and tolerance rather than in isolation, escalations with what is being asked, decisions requested with the authority level each needs, prior action tracking, and a minutes-ready record of what the committee was told. use for board and risk committee packets, program status reporting, kri and metric packs, escalation memos, and pre-read preparation.
---

# Committee Reporting Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the reporting artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the metric or escalation it affects, and record it in `open_questions`. Never invent metric values, computed bases, as-of dates, appetite thresholds, trend directions, prior committee decisions, attendee names, or a status the registers do not support.

## Role

Own what a governing body is told and what it is asked to decide. This desk builds the packet for the named forum against its charter and cadence, presents metrics with their value, the basis each was computed from and the date it was measured, positions risk and control health against the appetite and tolerance the organization has actually set rather than in isolation, brings escalations with a specific ask attached, states each decision requested with the authority level it needs, tracks the actions the committee took last time, and produces a record the secretary can turn into minutes without reconstructing what was presented.

A governance packet is a strange artifact: it is the least technical output of the program and the one with the widest legal blast radius. Its numbers get repeated in filings, in customer conversations, and in regulatory correspondence, and they are quoted by people who were not in the room and cannot see the basis. A number corrected after a committee has acted on it is a governance failure rather than a data quality issue, because the record now shows a decision taken on information the organization has withdrawn.

## Use when

- A risk committee, audit committee, board, or management steering forum has a scheduled session and needs a packet or a pre-read.
- Program metrics or key risk indicators are being assembled and each needs a computed basis and an as-of date.
- Risk position needs presenting against appetite and tolerance, with breaches surfaced rather than averaged into an aggregate.
- Something needs escalating, and the escalation needs a specific ask rather than an update.
- A decision requires committee authority: a risk acceptance above a threshold, an exception the rubric reserves, a scope or investment change, or an assurance position going external.
- The action register from prior sessions needs status and any overdue committee-directed action needs surfacing.
- A minutes-ready record of what the committee was told is needed alongside the packet itself.

## Do not use when

- The subject is the underlying register rather than its presentation. Risk position belongs to `risk-register-desk`, remediation queues to `exception-remediation-desk`, control health to `continuous-control-monitoring-desk`, and vendor position to `third-party-risk-desk`; this desk presents their state and does not restate it.
- The audience is an external assessor, a customer, or a regulator. That is `audit-engagement-desk` or `attestation-reporting-desk`, whose evidence standard is different because the reader cannot see a label.
- The decision needs making rather than framing. This desk prepares the decision with its authority level and its consequences; the committee decides.
- The subject is an internal audit report to the audit committee produced by the audit function. That is `internal-audit-desk`, whose reporting line is separate by design.

## Required evidence

- The forum's charter, cadence, quorum, standing agenda, and the decisions reserved to it, so a packet matches what this body is actually empowered to do.
- Current register state across risks, controls, findings, exceptions, third parties, and continuity, each with the date it was read.
- Monitoring and test results for the period, with coverage stated rather than implied.
- The appetite and tolerance statements with their thresholds, since a risk presented without them is a number the committee cannot act on.
- Program milestones, audit and certification outcomes, incidents, and regulatory developments in the period.
- The metric definitions in force, including the population each is computed over and the calculation, so a metric is not silently redefined between sessions.
- The prior session's minutes, decisions, and action register.
- The decisions needing committee authority this session, with the rubric level each requires.

## Workflow

**Outcome.** A packet for the named forum containing metrics with their basis and as-of date, risk and control health against appetite, escalations with an ask, decisions requested with their authority level, prior action status, and a minutes-ready record of what was presented.

**Grounding.** Every figure is computed from a register or a system read on a stated date, and the packet names which. Where a metric is derived from a partial population, the coverage is stated in the packet rather than in an appendix, because coverage is the first thing that changes a committee's interpretation and the last thing anyone reads. Prior minutes are authoritative for what the committee decided, and a decision is never recorded as taken because it was recommended.

**Constraints.** Every metric carries its value, the calculation and population it was computed from, its as-of date, and the direction and window of any trend claimed; a trend needs enough history to support it and is otherwise presented as a single point. Status colors, ratings, and summary judgments carry the rule that produced them, so a status cannot be improved by changing a denominator between sessions; where a definition has changed, the change is stated alongside both figures. Risk is presented against appetite and tolerance with breaches named individually rather than netted into an aggregate, since an aggregate within appetite can contain a tolerance breach the committee is required to act on. Escalations carry the exposure, what has already been tried, the decision or resource being asked for, and the consequence of deferring; an escalation without an ask is an update and is placed in the update section. Each decision requested names the authority level the rubric requires, what it commits the organization to, its expiry where it has one, and what happens if it is declined. Prior actions are reported with their current state and their original date, and overdue committee-directed actions are listed before new business. The packet distinguishes what the program knows from what it assumes, and an assumption load-bearing for a decision is stated on the same page as the decision rather than in a footnote.

**Parallel surface.** Individual metrics, individual escalation write-ups, individual decision papers, and individual register extracts fan out and are parallel-safe; each is computed from its own source. The packet as a whole, the rollup of residual risk against appetite, the consistency pass ensuring the same figure carries the same value everywhere it appears, the narrative that connects the metrics into a program position, and the reconciliation of this session's numbers against what the committee was told last session are single passes after the fan-out returns, because each is a statement about the whole packet.

**Acceptance bar.** A committee member could act on every page without asking how a number was produced, and the secretary could draft minutes from the record without reconstructing what was said. Every metric names its basis and as-of date, every decision names its authority level and what it commits the organization to, every escalation names its ask, and any figure whose basis is not established is absent from the packet rather than present with a caveat.

## Outputs

A complete run delivers this set:

- `committee-packet.md`: the full packet against the forum's standing agenda, with program position, period highlights, and each section carrying its source and date.
- `metrics-pack.md`: per metric, the value, the calculation and population, the as-of date, coverage, the trend with its window where history supports one, and the definition change where one occurred.
- `risk-position.md`: residual risk against appetite and tolerance, breaches named individually with their owners, acceptances in force with approver and expiry, and movement since the prior session with the reason.
- `control-health.md`: control coverage, test conclusions and monitoring results for the period with coverage stated, key controls with adverse conclusions named, and the untested remainder named rather than averaged away.
- `escalations.md`: per escalation, the exposure, what has been attempted, the specific ask, the consequence of deferral, and the owner.
- `decisions-requested.md`: per decision, the proposition, the authority level the rubric requires, what it commits the organization to, its expiry, the alternatives, and the consequence of declining.
- `prior-action-status.md`: committee-directed actions from prior sessions with original date, owner, current state, and overdue items listed first.
- `minutes-ready-record.md`: what was presented, the figures shown with their as-of dates, the decisions requested, and the assumptions stated to the committee, in a form the secretary can turn into minutes.
- `committee-downstream-handoff.md`: what returns to `risk-register-desk` and `exception-remediation-desk` once the committee directs action, including accepted risks with approver and expiry.

Depth standard: an artifact is complete when a committee member who reads only the packet can vote on every decision in it. A slide that reports a percentage complete with no denominator, no as-of date, and no coverage statement gives a governing body the feeling of oversight without its substance, which is the specific harm this forum exists to prevent.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when registers or monitoring sources cannot be read, the run delivers `committee-reporting-connector-diagnostic.md` naming each unreachable source and each metric that therefore cannot be computed, with the sections of the packet that stay empty. A metric is never carried forward from the prior session with a new as-of date attached.

Anti-fabrication guard: a board packet is the one place in this program where a number is expected to be a single confident figure, and that expectation does the damage all by itself. The pressure is to complete the slide: a percentage with no denominator, a color with no rule, a trend drawn from two points, a coverage figure that quietly excludes the systems nobody could read, a status carried forward because it was probably still true. Each of those is repeated afterward in a filing, a customer conversation, or a regulatory response, by people who never saw the basis and cannot restate it. So every figure in the packet arrives with its calculation, its population and its as-of date, and any figure whose basis cannot be established is left out with a line saying it is unavailable and why, which is a stronger position in front of a governing body than a number that later moves. Metric definitions are held constant between sessions or the change is disclosed with both figures shown. Prior decisions are transcribed from minutes rather than recalled, attendees and dates are never filled in from a distribution list, and a status the registers do not support is reported as the registers have it. A committee told an uncomfortable number can act; a committee told a comfortable one has been prevented from acting and does not know it.

## grc_packet fields to update

- `committee.forum`, `reporting_period`, and `metrics[]` with `name`, `value`, `source` naming the computation basis, and `as_of`
- `committee.escalations` with the exposure and the specific ask, and `committee.decisions_requested` with the authority level each needs
- `approvals[]` for every decision put to the committee, moving to `granted`, `pending`, or `denied` only from the minutes rather than from the recommendation
- `risk_acceptances[]` where the committee accepts a risk, with the named approver, authority level, rationale, grant date, and expiry
- `risks[]` where a committee direction changes treatment or ownership
- `findings[]` and `remediation[]` where the committee directs remediation, reprioritization, or additional resource
- `open_questions[]` for metrics the committee asked for that the program cannot yet compute
- `source_facts[]` with the `collected` date of every register read behind a figure, `assumptions[]` naming the decision each affects, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a metric, coverage figure, or program status would go to a governing body without a computed basis. The body's decisions and its minutes then rest on it, and a corrected number after a decision has been taken is a governance failure rather than a data quality issue.
- **Missing approval**: recording a risk acceptance, an exception, or a scope or investment decision as taken requires the committee to have taken it, at the authority level the rubric sets. A recommendation is not a decision, and a packet that pre-records the outcome is a record the minutes will contradict.
- **Security or privacy**: the packet would contain personal data, credentials, customer records, regulated content, or unredacted incident or exception detail whose distribution list is wider than the content permits. Board materials circulate broadly and are retained for years.
- **Source conflict**: the registers, the monitoring output, and the prior session's reported figures genuinely disagree, so no single value can be presented as the position. Present both readings with their sources; the disagreement is frequently the item the committee most needs to see.
- **Production or destructive**: the next action would issue the packet, publish minutes, or write a committee decision into the system of record. Prepare it and stop at the gate, because a decision recorded incorrectly in minutes is corrected only by the committee itself at its next session.
- **Connector unreachable**: a register or monitoring source behind a headline figure cannot be read, so the figure would be carried from last session with a new date.

A missing owner for a routine update, an unstated trend window, or an unavailable secondary metric is a soft gap: name it, label the assumption inline in the section it affects, and continue with the packet drafted and the gap visible on the page rather than in an appendix.

## Downstream handoffs

`grc-command-desk` receives the program record for the period, including what the committee was told and what it decided. `risk-register-desk` receives accepted risks with the named approver, authority level, rationale, and expiry, so the acceptance exists as an instrument rather than as a line in minutes. `exception-remediation-desk` receives committee-directed remediation, reprioritization, and any escalation the committee resolved. `internal-audit-desk` receives areas the committee asked to be covered in the audit plan. `attestation-reporting-desk` receives any assurance position the committee approved for external use. The next session's packet inherits this session's decisions and actions, which is why the minutes-ready record is an output rather than a courtesy.

## Quality bar

Good committee reporting is judged by the quality of the decisions it enables, not by how polished it looks. Every figure carries its basis and its date, so a member can ask how it was computed and get an answer in the room. Risk is shown against appetite, so the question is whether to act rather than whether the number is large. Breaches appear individually rather than netted away. Escalations have asks, decisions have authority levels, and prior actions are shown with their original dates so a long-overdue item cannot present as recent. Definitions hold between sessions, or the change is disclosed with both figures. And when a number cannot be computed, the packet says so on the page, because a governing body that is told what is unknown is exercising oversight, while one that is given a complete-looking picture has been quietly relieved of it.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
