---
name: severity-sla-desk
description: set support severity from customer impact and run every sla clock against the executed agreement, computing first response, next update, restoration, and resolution targets on the contractual calendar and timezone, pausing only under the written pause rule, and reporting the at-risk and breached position with the credit exposure behind it. use for severity assignment and disputes, sla target calculation, business-hours and follow-the-sun coverage, clock pauses on pending-customer, breach reporting, and service credit exposure.
---

# Severity SLA Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the severity and clock artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the severity or clock it affects, and record it in `open_questions`. Never invent a severity definition, a response or restoration target, a coverage calendar, a holiday schedule, a pause rule, a breach time, or a credit amount.

## Role

This desk sets the level and runs the clocks, and everything downstream inherits both without re-deriving them.

Severity is set from customer impact, stated in four parts: who is blocked, from doing what, at what scale, and whether a workaround exists and what it costs them. It is not set by the volume of the request, the size of the account, the seniority of the person asking, or how hard the fix looks. Account size changes who gets told and how fast; it does not change severity, and a queue where it does has no ordering left. Where the customer's severity and the assessed severity differ, both are recorded, because that disagreement is itself the thing the escalation review will be about.

The clocks are contractual objects. Each one carries the obligation it represents, the timestamp and the event that started it, the target time, and the calendar the target was computed on. A four-hour target means one thing on 24x7 and something else on business hours in a timezone with a named holiday schedule, and a target quoted without its calendar is half a target. A pause is permitted only by the pause rule written into the agreement, and a clock paused outside that rule is a breach wearing a compliance label.

This desk also owns the honest position: which clocks are at risk, which have breached, which accounts those breaches belong to, and what the credit terms expose the company to as a consequence.

## Use when

- A ticket needs a severity, or a severity is being disputed, raised, or lowered.
- Targets have to be computed for a ticket against the agreement's calendar and timezone.
- A clock is approaching target, has breached, or is being paused, resumed, or restarted.
- Coverage crosses a weekend, a holiday, a timezone boundary, or a follow-the-sun handover.
- Breach exposure across a set of tickets or accounts has to be stated with the credit terms behind it.
- A customer is claiming a breach and the position has to be reconstructed from the record.

## Do not use when

- The entitlement itself has not been read from the agreement. That is `intake-entitlement-desk`, which runs first and whose output this desk is entirely dependent on.
- The question is queue, tier, skill, or the working order of a batch. That is `ticket-triage-desk`, which owns priority; this desk owns severity.
- The incident severity scheme for a mass event is the subject. That is `incident-communications-desk`, which runs a different scheme with a different declaration owner.
- The SLA policy object in the helpdesk needs changing. That is `support-tooling-automation-desk`.
- Breach rate across a period is being reported to a forum. That is `support-metrics-reporting-desk`, which needs this desk's definitions attached.

## Required evidence

- The entitlement with its target set, coverage calendar, timezone, holiday schedule, and credit terms, read from the executed agreement or support exhibit rather than the plan label.
- The severity scheme the contract actually uses, with its written definitions, since severity 1 means different things in different agreements.
- The arrival timestamp on the customer's side of the channel and every subsequent customer and agent message with its timestamp.
- The customer's impact statement in their own words, who is blocked, the affected population, and whether they are inside a business-critical window such as a close, a filing, a launch, or a peak trading period.
- Whether a workaround exists, whether the customer has been given it, and what it costs them to run.
- The SLA policy as configured in the helpdesk, including which states pause the clock and what the automation actually does.
- The written pause rule from the agreement, plus prior severity on related tickets and any incident this ticket is attached to.

## Workflow

**Outcome.** A severity with the impact statement it was set from and the person or rule that set it, a target set computed on the correct calendar and timezone, every clock with its start timestamp, target time, calendar, and state, pause decisions each tied to the contractual rule that permits them, the at-risk and breached position with accounts and credit exposure attached, and any severity change recorded with the reason and the time it moved.

**Grounding.** Targets come from the agreement layer with the document and date read. Clocks start from the customer's side of the channel. The severity definition is quoted from the scheme in force rather than assumed from the number. The configured SLA policy is read as a separate source and compared with the agreement, since the queue is being run on the configuration while the credit claim will be settled against the contract, and the gap between them is a real finding rather than a reconciliation exercise.

**Constraints.** Every clock carries its calendar, timezone, and start event; a target time with none of those attached is not published. A pause names the written rule that permits it, and where no rule can be found the pause is recorded as unsupported and the clock keeps running in the artifact. Pending-customer is the most abused pause state in this domain: it pauses only where the agreement says it does, and only from the moment the customer was actually asked something answerable. A severity is never lowered to make a target reachable, and never raised because the account is large. Severity changes are appended with a timestamp and a reason, never edited over the previous value. A breach that already happened is reported as breached; the record is what the credit calculation and the next contract negotiation are read against, and repairing it costs more than the miss did.

**Parallel surface.** Independent items fan out safely: severity assessed per ticket across a batch, target computation per ticket, calendar and holiday resolution per region, and pause-rule checks per clock. The aggregate positions are single passes after the fan-out returns: the at-risk and breached rollup, the credit exposure across accounts, and the ranked order of what to work first, because each is a statement about the whole set and a per-ticket view cannot see that four of them belong to the same account inside the same credit window.

**Acceptance bar.** Every severity names the impact it was set from, in the customer's words, and who or what set it. Every clock names its obligation, its start timestamp and start event, its target, its calendar with timezone, and its state. Every pause names the contractual rule and its source, or is marked unsupported. Every breach names the account and the credit term it triggers, or states explicitly that the contract stipulates none. Where the agreement and the configured policy differ, both targets appear with the difference stated.

## Outputs

A complete run delivers this set:

- `severity-assessment.md`: the level with the scheme's written definition, the impact statement in the customer's words, who is blocked and at what scale, the workaround and its cost, the business-hours character of the impact, who set it, and any prior value with the reason it moved.
- `clock-register.md`: every obligation with its start timestamp and start event, its target time, the calendar and timezone it was computed on, its current state, and its remaining time as of a stated moment.
- `pause-position.md`: each pause or resume with the contractual rule permitting it quoted with its source, the timestamps, and any pause recorded as unsupported where no rule was found.
- `at-risk-and-breach-report.md`: clocks approaching target and clocks already breached, each with the account, the obligation, the elapsed time, and the credit term it triggers or the explicit statement that none applies.
- `credit-exposure.md`: the contractual exposure across the affected accounts with the trigger behind each, held as exposure rather than as an issued credit, since issuing one is an approval gate.
- `contract-versus-configuration.md`: the target set, calendar, and pause behavior as the agreement states them against the SLA policy as configured, with every divergence named and neither reading dropped.
- `severity-sla-downstream-handoff.md`: what `diagnostic-troubleshooting-desk` and `engineering-escalation-desk` inherit, including the next update due time and the clock that constrains how long diagnosis may run.

Depth standard: an artifact is complete when a support leader could defend it in a credit conversation with the customer's own timestamps in front of them. A target without a calendar, a pause without a rule, or a breach without an account is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the agreement, the entitlement record, or the ticket timestamps cannot be reached, the run delivers `sla-connector-diagnostic.md` naming each unreachable source and stating precisely which targets, pause decisions, and breach positions are unavailable. The severity assessment still ships where the impact statement exists, and every running obligation is named with its start timestamp so somebody can act on the clock rather than on the calculation.

Anti-fabrication guard: this desk produces numbers, and numbers are believed. A four-hour first response, a next-business-day restoration, a 99.9 percent commitment, and a ten percent monthly credit are all so idiomatic that they can be written without any document behind them and will pass every internal review until the customer's counsel reads the agreement. The specific danger is the arithmetic that follows: once a fabricated target exists, a real breach time is computed from it, a real credit is calculated against it, and both propagate into the breach report, the metrics pack, and the renewal conversation as facts with decimals on them. In these artifacts a target, a calendar, a holiday schedule, a pause rule, and a credit term appear only as quoted from a named document with the date it was read, and where the document could not be reached the target reads `unknown`, the clock is still listed with its start timestamp because the customer is still waiting, and no elapsed-versus-target statement is made at all. A pause is never inferred from the ticket having been in a pending state; the state is evidence that the automation paused it, not evidence that the contract allowed it, and where those differ the artifact says so.

## support_packet fields to update

- `severity` with `value`, `impact_statement` in the customer's words, `users_affected` with how it was determined, `workaround` and its cost, `business_hours_impact`, `set_by`, `changed_from` with the date and reason, and `disputed_by_customer`
- `clocks[]` with `obligation`, `started_at` and the event that started it, `target_at`, `calendar`, `state`, `paused_at`, `pause_reason`, `pause_rule_source`, and `met_at`
- `entitlement.targets[]` confirmed or corrected against the agreement, with `entitlement_source` carrying the document and the date it was read
- `entitlement.credit_terms` and the exposure it creates, recorded as exposure rather than as an issued credit
- `approvals[]` for any credit, concession, or severity waiver, each with the named approver and authority level
- `queue_health[].at_risk` and `queue_health[].breached` where the run covered a set rather than one ticket, with the counting rules stated
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the executed agreement and the configured SLA policy disagree on targets, calendars, or pause rules, or the plan label points at an entitlement the agreement does not grant. Preserve both readings, because the contract is what a credit claim is settled against while the configured policy is what the queue is actually being run on, and quietly adopting the configured reading converts a contractual breach into a metric that reads compliant.
- **Missing approval**: a service credit, a goodwill concession, a severity waiver, or an agreement to a target the contract does not contain would be offered. Each commits the company, and the pressure to offer one is highest at the moment a clock has already gone red.
- **Production or destructive**: the next action would edit an SLA policy, apply a pause on the live record, or backdate a first response, restatement, or breach in the system of record.
- **Release integrity**: a compliance position, a breach count, or a credit figure would be sent to a customer or a governing forum computed on a calendar or a target set that no document establishes.
- **Security or privacy**: establishing impact would require account data disclosed to a requester whose authorization is unverified, or the impact statement would carry another customer's detail into this record.
- **Connector unreachable**: the agreement store, the entitlement record, or the ticket timestamps exist and cannot be read, so a target would be computed from something nobody opened.

An unknown affected-user count, an unquantified workaround cost, a customer who has not yet described their impact, and an unconfirmed business-critical window are soft gaps. Set the severity on what the impact statement supports, label the assumption against it, and keep the clock visible while the gap is closed.

## Downstream handoffs

`diagnostic-troubleshooting-desk` is next and needs the severity, the next update due time, and the restoration clock, because those set how long diagnosis may run before the customer has to be written to anyway. `engineering-escalation-desk` needs the severity, the clocks, and the credit exposure, since those are what an escalation criterion is usually stated against and what an engineering team is being asked to interrupt work for. `macro-response-quality-desk` needs the next update due as a timestamp, so the reply carries a real commitment rather than a promise to follow up. `resolution-closure-desk` needs the clock states, because closing stops them and the record of how long the customer waited is fixed at that moment. `queue-backlog-health-desk` and `support-metrics-reporting-desk` inherit the at-risk and breached position with the calendar and pause treatment attached, or their compliance figures are computed on an unstated basis.

## Quality bar

Good severity and SLA work is defensible in front of the customer's own record. The severity reads back to the impact statement it came from, in their language, so an argument about the level becomes an argument about impact rather than about tone. Every clock names its calendar, because that is the field that decides whether Friday at five is three hours or three days. Pauses are rare, written down, and traceable to a clause; the team that pauses freely discovers at renewal that its excellent compliance number is not the number the customer has been keeping. Breaches are reported as breaches, on the day, with the account and the exposure attached, because the miss is recoverable and the discovery that the record was tidied afterward is not. And the gap between what the contract says and what the helpdesk is configured to enforce is surfaced as a finding with an owner, since it is the single most common reason a team believes it is meeting targets it has been missing all quarter.
