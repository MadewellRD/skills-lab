---
name: queue-backlog-health-desk
description: read the shape of a support queue by reporting backlog in age cohorts with untouched, pending-customer, and pending-engineering states held apart, inflow against outflow, at-risk and breached counts with credit exposure, reopen rate against its definition in force, pending-state hygiene, and a burn-down plan against real capacity. use for backlog reviews, queue aging, wip and workload distribution, sla breach exposure, ticket counting rules, and backlog recovery planning.
---

# Queue Backlog Health Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the queue health artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the queue or cohort it affects, and record it in `open_questions`. Never invent a ticket count, an age cohort figure, an inflow or outflow rate, a breach count, a credit exposure, a reopen rate, an agent's workload, or a capacity figure nobody committed.

## Role

A single open-ticket count is the least informative number a support organization produces. It contains this morning's arrivals and a ticket nobody has read since March, and it moves for reasons that have nothing to do with whether the operation is keeping up. This desk replaces that number with the shape of the queue.

The shape has four parts. Backlog by age cohort, so the tail is visible instead of averaged. States held apart, because a ticket in pending-customer is waiting and a ticket in pending-engineering is blocked and an untouched ticket is a failure, and merging them produces a number that describes nothing. Inflow against outflow over the same window, which is the only reading that says which direction the backlog is actually moving; a queue that shrank while inflow collapsed did not improve. And the SLA position across the queue, with the at-risk and breached counts carrying the accounts and the credit exposure behind them, because that is the part of the backlog that has money attached.

The desk owns two findings nobody volunteers for. Pending-state hygiene, meaning the tickets parked in a waiting state that no rule and no person will ever return to, which is where a queue hides its real age. And the counting rules, stated explicitly for merges, duplicates, spam, machine-generated tickets, and internal tickets, because the same month moves by a fifth on those rules alone and a backlog figure that cannot be compared with the last one is not a measurement.

The burn-down plan is the output leaders want and the one most often produced dishonestly. It is arithmetic against capacity somebody has actually committed, and where that capacity does not exist the honest plan says the backlog does not clear.

## Use when

- The backlog is growing, or a leader has asked what is actually in it.
- Aged tickets need reading by cohort rather than as a single open count.
- SLA breach exposure across a queue needs quantifying, with the accounts and credit terms behind it.
- Tickets are parked in pending states and nobody is sure which of them are alive.
- Inflow and outflow need comparing to establish whether the operation is keeping up.
- A backlog recovery plan is needed, or a proposed one needs testing against real capacity.
- Reopen rate is being quoted and its definition has never been written down.
- Queue counting rules differ between two reports of the same period.

## Do not use when

- One batch of tickets needs routing, priority, and duplicate decisions. That is `ticket-triage-desk`.
- The severity, target, calendar, or clock on an individual ticket is the question. That is `severity-sla-desk`, which owns the entitlement math this desk aggregates.
- The finding is that there are not enough people, or the wrong skills, at the wrong hours. That is `workforce-coverage-desk`, which owns forecast, shrinkage, and coverage.
- The fix is a view, a trigger, an SLA policy, or an auto-close rule in the platform. That is `support-tooling-automation-desk`.
- The question is what is generating the volume rather than how the queue is absorbing it. That is `contact-driver-analysis-desk`.
- The numbers are going to a leadership forum and need definitions, populations, and exclusions attached for the record. That is `support-metrics-reporting-desk`.

## Required evidence

- The queue and view definitions with what each is meant to hold, and whether any ticket can appear in more than one.
- Open tickets with created timestamp, first-touch timestamp, last public reply timestamp, last internal update timestamp, current state, assignee, and severity.
- Inflow and outflow counts over the same window on the same counting rules, with solved and closed distinguished.
- The full age distribution rather than an average or a median, with the cohort boundaries the team already uses.
- Ticket states with pending-customer and pending-engineering separable, plus the pending-timeout and auto-close rules configured on each queue.
- SLA position per ticket: target, elapsed, remaining, paused time with the pause rule invoked, at-risk threshold, and breached state, with the entitlement behind each.
- Reopen data with the reopen definition actually in force, including whether a customer reply on a solved ticket counts.
- Agent assignment counts, work in progress per agent, and unassigned tickets.
- The counting rules for merges, duplicates, spam, machine-generated tickets, internal tickets, and tickets created by automation.

## Workflow

**Outcome.** A queue health read stating backlog by age cohort with untouched, pending-customer, and pending-engineering held apart, inflow against outflow with the direction the backlog is moving, the untouched set with its oldest ticket named, the at-risk and breached position with accounts and credit exposure, the pending-state hygiene findings, the reopen rate with its definition, the counting rules applied, and a burn-down plan against capacity that has been committed rather than assumed.

**Grounding.** Age runs from the arrival timestamp on the customer's side of the channel, so a ticket created from a forwarded thread ages from the original message. Untouched means no response has reached the customer, not that no internal note exists, since an internal comment is not an answer. SLA positions are inherited from the entitlement read upstream rather than recomputed from the configured policy, and where the two differ both are carried. Inflow and outflow are pulled over the same window on the same rules; comparing a raw arrival count with a filtered solved count is how a queue is shown to be improving while it grows.

**Constraints.** Every count carries its window, its queue, and its counting rules, and the same rules apply to both sides of any comparison. No aggregate merges pending-customer with working tickets. A ticket in pending-engineering carries its defect reference or is reported as parked without one, which is itself the finding. Bulk operations are prepared and stopped at the gate, with the tickets named, the operation stated, the triggers that will fire listed, and the notifications each will send counted. Closing aged tickets is never presented as backlog recovery: the backlog is the record of what the operation did not do, and a mass close notifies every one of those customers that their unresolved problem is solved. Where a burn-down plan needs capacity nobody has committed, the plan says the backlog does not clear at current capacity rather than assuming overtime, borrowed staff, or a deflection improvement that has not happened.

**Parallel surface.** Independent items fan out safely: each queue read separately, each ticket's SLA position computed, each pending ticket assessed for whether anything will actually return it, each account's breach exposure resolved against its own credit terms, and each agent's work in progress counted. The aggregates are single passes after the fan-out returns, because each is a statement about a whole set: the age distribution and its cohort boundaries, inflow against outflow, the reopen rate over the window, the total credit exposure, and the burn-down arithmetic, which depends on the whole cohort structure and on one capacity figure rather than on per-queue guesses.

**Acceptance bar.** Every figure carries its window, its queue, and its counting rules. Backlog appears as cohorts with untouched, pending-customer, and pending-engineering separate, never as one open count. The oldest untouched ticket is named with its age and its account. Every breached and at-risk ticket carries its entitlement source and its credit exposure. The reopen rate is stated with the definition it was computed on. The burn-down plan names the capacity it assumes and the source of that commitment, and states plainly where the arithmetic does not close.

## Outputs

A complete run delivers this set:

- `queue-health-summary.md`: per queue, the window, the counting rules, open total, inflow, outflow, net movement, and the one-line reading of which direction the queue is going and why.
- `backlog-age-cohorts.md`: the full age distribution per queue with cohort boundaries stated, split by state, with untouched, pending-customer, and pending-engineering as separate series rather than as footnotes.
- `untouched-and-aging-set.md`: every open ticket with no customer-facing response, ranked by age, with the account, the severity, the entitlement, and the oldest named explicitly.
- `sla-exposure-position.md`: at-risk and breached counts per queue and per account, each breach with its target, its entitlement source, its elapsed time, the pause treatment applied, and the credit exposure the terms attach to it.
- `pending-state-hygiene.md`: tickets parked in a waiting state with nothing that will return them, the pending-timeout and auto-close rules in force on each queue, the tickets an auto-close rule would close that nobody resolved, and the pending-engineering tickets with no defect reference.
- `reopen-analysis.md`: the reopen rate with the definition in force, the reopen reasons grouped, and the queues, macros, or resolution codes the reopens cluster around.
- `burn-down-plan.md`: the arithmetic per cohort, the capacity assumed with the source of that commitment, the sequence that protects the entitlements with the most exposure, what is deliberately not being worked, and the honest statement where the backlog does not clear.
- `queue-health-downstream-handoff.md`: what `workforce-coverage-desk` and `contact-driver-analysis-desk` inherit, including the sustained inflow rate, the coverage gaps the aging implies, and the drivers the aged tickets cluster into.

Depth standard: an artifact is complete when a support manager could run tomorrow's stand-up from it and a leader could see the shape of the queue without asking a follow-up question. A cohort table without state separation, or a breach count without the accounts behind it, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the reporting layer, the ticket record, or the SLA policy configuration cannot be reached, the run delivers `queue-connector-diagnostic.md` naming each unreachable source and precisely which cohorts, breach counts, or rates are unavailable because of it. Partial reads still ship with their coverage stated, because a queue read over four of six queues is useful when it says which four, and a breach clock does not pause while a connector is down.

Anti-fabrication guard: queue reporting is arithmetic, and arithmetic is the most persuasive thing to produce without data, because a table of counts that sums correctly, cohorts that taper the way backlogs usually taper, and a burn-down that lands neatly at zero on a Friday all look exactly like the output of a real query. In these artifacts every count, cohort, rate, and exposure figure comes from a query against a named source over a stated window with its counting rules attached, no total is completed by subtraction to make a table balance, and no cohort is populated because the distribution looked implausible without it. Where a queue could not be read, it is listed as unread rather than estimated from the queues that could, since a backlog figure's entire value is that the next one can be compared with it. The burn-down carries the strictest form of this rule: it uses only capacity somebody has committed with a name attached, never a headcount that might be freed or a deflection gain that has not landed, because a plan built on borrowed capacity is a plan that returns as a breach report in three weeks.

## support_packet fields to update

- `queue_health[]` with one entry per queue carrying `window`, `inflow`, `outflow`, `open_total`, `age_cohorts[]` as cohorts rather than an aggregate, `untouched` with the oldest, `pending_customer` and `pending_engineering` held separately, `at_risk`, `breached` with accounts and credit exposure, `reopen_rate` with its definition, `wip_per_agent`, and `counting_rules`
- `clocks[]` for every at-risk and breached obligation surfaced by the sweep, each with its start, target, calendar, and pause treatment
- `approvals[]` for any bulk close, bulk merge, bulk reassignment, or bulk state change the recovery plan proposes
- `metrics[]` seeded with backlog age, breach rate, and reopen rate, each carrying its definition, population, exclusions, and window
- `workforce.coverage_gaps[]` seeded where the aging pattern points at an interval, language, skill, or product with no cover
- `drivers[]` seeded where aged tickets cluster into a single driver or a single open defect
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: a recovery step would mass-close, mass-merge, bulk-reassign, or bulk-change state on the live queue. Closing a thousand aged tickets clears the metric and notifies a thousand customers that their unresolved problem is solved, fires every trigger and survey those tickets match, and destroys the record of how long each person actually waited.
- **Release integrity**: a backlog, breach, or reopen figure would be reported without its window, its counting rules, or its state separation, into a decision about headcount, a customer commitment, or a contractual review. Two figures on different counting rules are both defensible and produce opposite conclusions.
- **Missing approval**: the plan proposes deprioritizing a queue, an account tier, or a severity band, or accepting breaches on a set of tickets. That is a decision about which customers wait, and it belongs to the leader who owns the service target.
- **Source conflict**: the reporting layer and the raw ticket record return different counts for the same window, or the configured SLA policy and the executed entitlement disagree on which tickets are breached. Preserve both readings; the contract is what a credit claim settles against.
- **Security or privacy**: the artifact would carry ticket content, customer identities, or account detail beyond what the audience needs, since a queue report circulates far more widely than a ticket does.
- **Connector unreachable**: the ticket record, the reporting layer, or the SLA configuration exists and cannot be read, so the queue position would describe counts nobody pulled.

An unknown agent capacity, a missing reopen definition, an unclassified pending ticket, and an uncosted credit exposure are soft gaps. Proceed with the assumption labeled against the cohort it affects, and state which figures it moves.

## Downstream handoffs

`workforce-coverage-desk` is next and needs the sustained inflow rate with its window, the handle-time population behind any capacity claim, and the intervals where the aging concentrates, because that is the input to a staffing model rather than a headcount request. `contact-driver-analysis-desk` needs the drivers the aged and reopened tickets cluster into, since an aging tail is usually two or three unresolved causes rather than a general slowness. `support-tooling-automation-desk` needs the pending-timeout, auto-close, and view definitions this run found to be wrong, each arriving with the tickets it would act on. `severity-sla-desk` needs the tickets whose SLA position could not be resolved. `engineering-escalation-desk` needs the pending-engineering set with the oldest and its defect reference, since that cohort ages outside support's control and needs pushing rather than sorting. `support-metrics-reporting-desk` needs the counting rules verbatim so the period report reconciles with this read.

## Quality bar

Good queue work makes the tail visible and refuses to average it away. The report opens with the counting rules, so the next one can be compared with it, and it says whether spam and machine-generated tickets are in or out before anyone finds the discrepancy. Pending-customer tickets sit in their own column, because two hundred of them parked forever is a different problem from two hundred tickets being worked, and calling both backlog hides the one that is fixable. The oldest untouched ticket is named, with its account and its age, since that single line does more to move a queue than any distribution. Breaches carry the accounts and the credit terms, because that converts a queue problem into a number the business already understands. And the burn-down is honest about capacity: a plan that clears the backlog using people nobody has assigned is a plan that has already failed, and saying so in the artifact is the useful version of that finding.
