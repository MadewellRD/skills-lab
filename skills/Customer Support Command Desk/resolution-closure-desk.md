---
name: resolution-closure-desk
description: decide how a ticket ends, with the resolution code from the scheme in force, the fix type separating a real fix from a workaround from a configuration change from expected behavior from not reproduced, customer confirmation before closure above the threshold, auto-close and pending-timeout exposure named, reopen analysis of what the first closure missed, and survey suppression decisions. use for resolution coding, closure eligibility, auto-close rules, pending-customer timeouts, reopen rates, and survey triggering.
---

# Resolution Closure Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the closure artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the ticket it affects, and record it in `open_questions`. Never invent a customer confirmation, a confirmation timestamp, a resolution code, a reopen reason, an auto-close rule, or a survey result.

## Role

This desk owns the end of a ticket, which is the point at which the record becomes permanent and the clock stops for good.

Closing is not a neutral administrative act. It stops the SLA clocks, fires the survey, releases the ticket from every view that would have surfaced it, and in most platforms cannot be undone. A customer who comes back gets a new ticket with a new clock and none of the history, which means the record of how long they actually waited is destroyed by the close rather than by the reopen. That asymmetry is why confirmation matters above the severity threshold the organization sets, and why silence is not confirmation.

It owns the resolution code, chosen for what actually happened rather than for how the code reports. It owns the fix type, which is a different field and the one that carries the truth: fixed, workaround, configuration change, documentation, expected behavior, not reproduced, no customer response, duplicate, or out of scope. A workaround is not a fix, and a ticket resolved by one stays attached to its defect, because closing it silently is exactly what makes a live defect look like it stopped affecting anyone.

It owns the exposure created by rules that close tickets without a human: auto-close after a pending timeout, solved-to-closed transitions, and inactivity rules that catch a customer who was waiting on the company rather than the other way around. And it owns reopen analysis, which is the cheapest quality signal support has, because every reopen is a specific statement about what the first closure got wrong.

## Use when

- A ticket is being resolved and needs a code, a fix type, and a closure decision.
- Closure eligibility has to be assessed, particularly above the confirmation threshold or where a defect is still open.
- Auto-close, pending-timeout, or inactivity rules are closing tickets and the exposure has to be named.
- Reopens are being analyzed, or a reopen rate is being explained.
- Survey triggering or suppression has to be decided for a ticket or a set.
- A batch of aged tickets is being cleared and the question is which are genuinely finished.

## Do not use when

- The commitments in the last reply are still open. That is `macro-response-quality-desk`, whose commitment register decides eligibility here.
- The defect is still with engineering and the subject is the status loop. That is `engineering-escalation-desk`.
- The backlog's shape, aging, and burn-down is the subject rather than individual closures. That is `queue-backlog-health-desk`, which must never be answered by mass-closing.
- The auto-close rule itself needs changing in the platform. That is `support-tooling-automation-desk`, which owns blast radius and the suppression path.
- Reopen or satisfaction figures are being reported to a forum. That is `support-metrics-reporting-desk`, which needs the definitions this desk applied.

## Required evidence

- What was actually done on the ticket and by whom, read from the thread rather than from the closing note.
- The resolution code scheme in force with the written definition of each code.
- The customer's last message, and whether they were asked a closed question they could answer.
- The reopen policy and what counts as a reopen, including whether a new ticket on the same issue counts.
- The auto-close, solved-to-closed, and pending-timeout rules configured on this queue, with their intervals and what notifications they fire.
- The survey trigger rules, the suppression policy, and any prior survey sent to this requester inside the throttle window.
- Any defect, known error, or incident the ticket remains attached to, with its current state.
- The confirmation threshold the organization sets, expressed by severity or entitlement, and the clocks still running.

## Workflow

**Outcome.** A resolution record with the code, what was done, and the fix type; the customer confirmation state with its timestamp and the message it came from; a closure decision per ticket including which are not eligible and why; the tickets that stay attached to an open defect; the reopen analysis naming what the first closure missed; the survey and suppression position; and the auto-close exposure where a rule would close tickets nobody resolved.

**Grounding.** Confirmation is grounded in a customer message that actually confirms, quoted with its timestamp. Fix type is grounded in what the diagnosis and reproduction established rather than in the resolution code chosen. Auto-close exposure is grounded in the configured rule read from the platform, applied against the actual set of tickets currently in the matching state. Reopen reasons are grounded in the reopening message rather than in the closing agent's account of it.

**Constraints.** Silence is not confirmation. A ticket closed after no response is coded as no customer response, which is a different outcome from resolved and reports differently on purpose. Above the confirmation threshold, closure waits for the customer. A ticket resolved by a workaround keeps its defect attachment and is not coded as fixed. A ticket answered by an article or a known error is coded for what it was, so the deflection shows up in the driver analysis. Nothing closes, merges, or bulk-transitions from here; the closure decision is prepared with its list and stopped at the gate. Surveys are not fired to a customer inside an unresolved escalation, inside an active incident, or where a suppression rule applies, and every suppression is recorded with its reason, because unrecorded suppression turns a satisfaction score into a measurement of who was allowed to answer.

**Mandated order, because closure is not reversible and it destroys the waiting record.** Above the severity or entitlement threshold the organization sets, confirmation precedes closure. Closing stops the clock, fires the survey, and in most platforms cannot be undone; the customer who returns gets a new ticket, a new clock, and none of the history:

1. Establish that the impact has actually ended, from the customer's own message or from system evidence where the customer cannot be reached.
2. Record the confirmation with the person, the timestamp, and the message it came from, or record explicitly that none was obtained and why.
3. Close, with the code and fix type set from what happened rather than from what closes cleanly.

**Parallel surface.** Independent items fan out safely: tickets in a closure batch assessed at once, resolution codes assigned per ticket, confirmation state read per thread, survey eligibility checked per requester, and reopen threads read in parallel. The aggregate positions are single passes after the fan-out returns: the auto-close exposure across the queue, the reopen rate with its definition, the miscoding pattern across the batch, and the burn-down implication of the closure set, because each is a statement about the whole population and none of them can be assembled from per-ticket answers.

**Acceptance bar.** Every ticket carries a resolution code and a separate fix type, both traceable to what the thread and the packet establish. Confirmation state names the message and timestamp it came from, or says none was obtained. Every ticket attached to an open defect is identified and stays attached. The auto-close exposure names the rule, the interval, the count of tickets currently in scope, and what the customer receives when it fires. Reopen entries name what the first closure missed. Every survey suppression carries its reason.

## Outputs

A complete run delivers this set:

- `resolution-record.md`: per ticket, the code with the scheme's definition, what was actually done, the fix type, the defect or known error it remains attached to, and the clocks it stops.
- `confirmation-position.md`: the customer confirmation with the person, the timestamp, and the quoted message, or the explicit statement that none was obtained with what was asked and when.
- `closure-eligibility.md`: which tickets may close now, which may not and why, and which are held by an open commitment, an open defect, or an unmet confirmation threshold.
- `auto-close-exposure.md`: each rule with its trigger, interval, and notification, the current count of tickets it would close, how many of those are waiting on the company rather than the customer, and the proposed suppression or exclusion.
- `reopen-analysis.md`: reopened tickets with the reopening message quoted, the reason class, what the first closure missed, and the pattern where several share one, distinguishing a premature close from a fix that did not hold.
- `survey-position.md`: which tickets trigger a survey, which are suppressed with the reason and the rule, throttle collisions, and the effect of the suppression set on any satisfaction figure computed from the remainder.
- `miscoding-findings.md`: resolutions coded as fixed that were workarounds, as user error against evidence of a defect, or as duplicate without a surviving record, each with the correction and the source.
- `closure-downstream-handoff.md`: what `incident-communications-desk` and `queue-backlog-health-desk` inherit, including tickets held open by an incident or a live defect.

Depth standard: an artifact is complete when a support leader could approve the closure set without reading the tickets, because every ineligible one names its blocker. A closure list with no confirmation column, or a code with no fix type beside it, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the ticket threads, the configured close rules, or the survey platform cannot be reached, the run delivers `closure-connector-diagnostic.md` naming each unreachable source and which eligibility, exposure, or reopen findings are unavailable. No ticket is proposed for closure on unread evidence, since closing is the one action in this suite that cannot be corrected afterward.

Anti-fabrication guard: the pressure at this desk points at the closed state, because open tickets are what the queue report is judged on and every aging ticket is somebody's uncomfortable number. The fabrications are quiet and they all look like tidiness: a confirmation recorded because the agent asked and heard nothing back, a resolution coded as fixed when a workaround is what the customer is running, a closing note written in the customer's voice, a ticket coded not reproduced when it was never attempted, a duplicate pointing at a surviving record nobody checked, and a satisfaction picture assembled from a population that had its unhappy half suppressed. Each closes a ticket and each destroys the evidence that would have explained the reopen, the credit claim, or the driver. In these artifacts confirmation exists only where a customer message says the impact ended, quoted with its timestamp and its sender; where nobody replied, the state is `not_asked` or the code is `no_customer_response`, and both are legitimate outcomes that report honestly. Fix type is set from the diagnosis rather than from the code, so a workaround stays a workaround in the record even where the ticket is closed and the customer is satisfied. And a survey suppression is written down with its rule, because an unrecorded suppression is indistinguishable from a customer who was never going to answer, and only one of those is a measurement.

## support_packet fields to update

- `resolution` with `code`, `summary` of what was actually done, `fix_type`, `customer_confirmed`, `confirmed_at`, `closed_at`, `auto_close_rule`, `reopen_count`, `reopen_reasons[]`, `survey_state` with its suppression reason, and `survey_result`
- `ticket.state` and `linked[]` where a ticket remains attached to a defect, a parent, or an incident rather than closing into it
- `defect.tickets_attached` maintained so a fix landing reaches every account waiting on it
- `clocks[]` marked `met` with the timestamp where a closure satisfies an obligation, and left running where it does not
- `approvals[]` for any bulk closure, any closure above the confirmation threshold without confirmation, and any change to the auto-close configuration
- `queue_health[].reopen_rate` with the reopen definition in force, and the counting rules applied to the closure set
- `metrics[]` where a resolution or satisfaction figure derives from this set, carrying its population and exclusions
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: closure would be applied, in bulk or above the confirmation threshold, without the customer confirming the impact ended. Closing stops the clock, fires the survey, and in most platforms cannot be undone; the customer who comes back gets a new ticket, a new clock, and none of the history, so the record of how long they actually waited is destroyed by the close rather than by the reopen.
- **Missing approval**: an auto-close rule would be suppressed, extended, or applied to a set outside its normal scope, or a batch of aged tickets would be cleared as a recovery action.
- **Release integrity**: a ticket would be coded as fixed while the defect behind it is open, or a satisfaction figure would be reported from a population whose suppressions are unrecorded.
- **Source conflict**: the closing note and the thread genuinely disagree about what was done or whether the customer confirmed, which is the exact discrepancy a credit claim or an escalation review is later argued over.
- **Security or privacy**: the closing message would carry account detail to an unverified requester, or another customer's content into this thread.
- **Connector unreachable**: the ticket threads, the configured close rules, or the survey platform exists and cannot be read, so an eligibility or exposure position would describe records nobody opened.

An unanswered confirmation request, an unknown reopen reason, a pending defect with no fix date, and an unmeasured survey response rate are soft gaps. Hold the ticket in its honest state, code it for what actually happened, label the assumption, and continue.

## Downstream handoffs

`incident-communications-desk` needs the tickets held open by an active incident, since the tickets an event generates outlive the incident record that would otherwise close them. `queue-backlog-health-desk` needs the closure set, the auto-close exposure, and the counting rules, because a backlog that improves through auto-close is not improving. `support-metrics-reporting-desk` needs the resolution codes, the reopen definition, and the survey suppression set with their reasons, or its resolution and satisfaction figures rest on an unstated population. `knowledge-base-desk` needs resolutions that answered a question worth publishing once. `contact-driver-analysis-desk` needs the fix types, because a driver resolved by workaround forty times is an unfixed defect wearing a healthy resolution rate. `quality-assurance-review-desk` needs the reopen analysis, which is the highest-yield sample it can draw.

## Quality bar

Good closure work leaves a record that still explains itself a year later. The code says what happened and the fix type says whether the problem is actually gone, and those two fields disagreeing is a normal, informative state rather than an error. Confirmation is quoted from the customer, with a timestamp, so nobody has to reconstruct it during a credit conversation. Tickets riding on an open defect stay visibly attached, because the alternative is a defect that appears to affect nobody until it appears in forty new tickets after the next release. Auto-close is treated as the significant automation it is, with its exposure counted and the tickets waiting on the company excluded. Reopens are read rather than tallied, since the reopening message usually names the exact sentence in the first reply that was wrong. And survey suppression is written down, because the fastest way to raise a satisfaction score is to stop surveying the people who are unhappy, and a team that does it accidentally cannot tell that from an improvement.
