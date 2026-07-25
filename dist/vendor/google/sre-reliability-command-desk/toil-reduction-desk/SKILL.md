---
name: toil-reduction-desk
description: account for operational toil with measured hours and how they were established, classify each recurring task as automatable partially automatable or inherent, define the elimination path per task through automation self-service or a design change that removes the work, and rank the backlog against the operational load budget with payback and auto-remediation safety.
---

# Toil Reduction Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the toil artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent hours, ticket volumes, page counts, task frequencies, automation effort estimates, or savings figures.

## Role

Own the operational load a team carries between incidents. Toil is the work that is manual, repetitive, automatable, tactical, produces no enduring improvement, and grows in proportion to the service rather than to its value: the access request that arrives fourteen times a month, the certificate rotated by hand, the quota bump, the stuck queue drained by the same command every Tuesday, the alert that requires a restart and always has.

Two distinctions carry this desk. The first is toil against operational work that is genuinely inherent: a judgment call, an approval, a customer conversation, an investigation with a real unknown. Both consume the same hours and only one is eliminable, and calling everything toil produces an automation backlog nobody can finish. The second is the fix against the cause. A task that exists because a service leaks connections is not an automation candidate; it is a defect whose manual workaround has been normalized, and automating the restart makes the defect permanent while hiding the signal that would have argued for fixing it.

The output is not a list of annoyances. It is an account of hours with a source, ranked against the load budget the team actually works to, with an elimination path per task and an honest payback for each.

## Use when

- Operational load is consuming the capacity a team needs for engineering work, or a load budget is being exceeded.
- Recurring pages, tickets, or requests need classifying and costing before an automation backlog is committed to.
- Postmortem action items are accumulating as manual procedures rather than as fixes.
- A runbook is executed the same way every time, which makes it a candidate for automation rather than for better documentation.
- A team is being asked to take on more services and needs to know what its current load actually is.
- Auto-remediation is being proposed and needs safety design before it is allowed to act on production.

## Do not use when

- The load is caused by unnecessary pages: that is `alerting-quality-desk`, and reducing noise is cheaper than automating a response to it.
- The load is real but the rotation is understaffed or badly shaped: that is `oncall-escalation-desk`.
- The manual work exists because a resilience control is missing, such as no retry budget, no load shedding, or no graceful degradation: that is `resilience-architecture-desk`.
- The recurring work is a self-service gap in the developer platform: cross-suite handoff to the Platform Engineering suite, which owns golden paths and self-service surfaces.
- The elimination path is a product or code change: this desk specifies and ranks it, then hands the implementation to the SDLC suite as a labeled cross-suite handoff.

## Required evidence

- Page history by rule and by responder, with timestamps and resolution actions.
- Ticket and request queue data with categories, volumes, and the age distribution of each class.
- The operational task inventory as it exists, including work that never generates a ticket, which is systematically the most under-counted category.
- Time evidence: tracked time, ticket handling durations, shift retrospectives, or a stated sampling method. The method matters more than the number.
- Runbooks that are executed manually and repeatedly, with their step counts and any approval steps inside them.
- Postmortem action items that are procedures rather than fixes.
- The operational load budget the team works to, and the current headcount and rotation shape it applies to.
- Existing automation, including the automation that has stopped working and is being compensated for by hand.

## Workflow

**Outcome.** A toil account with hours per task and the method that produced them, a classification of each task as automatable, partially automatable, or inherent, an elimination path per eliminable task, and a ranked backlog stated against the load budget with the payback for each item.

**Grounding.** Ticket queues and paging platforms state volume and timing. Time tracking, handling durations, and sampled measurement state hours. Team recollection states what feels heavy and is recorded as estimate rather than as measurement, because the gap between the two runs in both directions: teams overestimate the dramatic interrupt and badly underestimate the five minute task performed thirty times a month. Every hours figure in these artifacts carries how it was established, per `references/suite-workflow-contract.md`.

**Constraints.** Toil is counted per task with frequency and duration separately, so that the ranking is inspectable and a wrong assumption is visible rather than baked into a total. Work that generates no ticket is counted explicitly, since queue data alone systematically understates the load by exactly the amount of work the team does quietly.

Classification is honest about inherent work. A task requiring judgment, negotiation, or an approval that exists for a governance reason is inherent, and its improvement path is reduction in frequency or friction rather than automation. Partially automatable is the common and useful case: the diagnosis automates and the decision does not.

The elimination path names a mechanism rather than an aspiration. Automation removes the human from a task that already has a deterministic procedure. Self-service moves the task to the person who wants the outcome. A design change removes the task from existence, which is the highest-value path and the one most often skipped because it is someone else's backlog. Where the underlying cause is a defect, that is stated, and automating around it is recorded as a decision with its cost rather than as a solution.

Automation that acts on production follows a mandated order, and the reason is that a remediation loop is a production incident with a scheduler attached:

1. Run in observe mode, recording the action it would have taken, until its decisions have been reviewed against real occurrences.
2. Add a rate limit and a circuit breaker that stops the automation after a bounded number of actions in a window.
3. Enable it for the narrowest scope that still covers real cases.
4. Enable it broadly only once the observe record and the bounded run show it acts correctly, keeping the manual path available.

Steps 1 and 2 exist because an auto-remediation that is wrong in the same way every time will take that action every time, at machine speed, across the fleet, and the failure it causes will look exactly like the failure it was written to fix.

**Parallel surface.** Tasks, ticket categories, alert rules, runbooks, and services are independent units and are parallel-safe: per-task hour accounting, per-category queue analysis, per-runbook automatability assessment, per-task effort estimation, and connector preflight across the ticket queue, paging platform, and runbook repository all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: totaling load against the budget, ranking the backlog by payback and by risk reduction together, identifying tasks that share a root cause and should be eliminated once rather than automated separately, and judging whether the total is a toil problem or a reliability problem wearing a toil costume.

**Acceptance bar.** Every task carries frequency, duration, and the method behind both, or is marked unmeasured. Every task carries a classification. Every eliminable task carries a mechanism, an effort estimate with its basis, and a payback. The backlog is ranked and stated against the load budget, including the statement that the budget is unknown where nobody has set one. Tasks whose real cause is a defect are named as defects rather than as automation candidates.

## Outputs

A complete run delivers this artifact set:

- `toil-inventory.md`: each recurring task with its trigger, frequency, duration, hours per week, the measurement method, the responder it lands on, and whether it interrupts out-of-hours.
- `toil-classification.md`: automatable, partially automatable, or inherent per task, with the reasoning, the part that automates where it is partial, and the tasks whose real nature is a defect workaround.
- `toil-elimination-plan.md`: per eliminable task, the mechanism, the design of the automation or self-service surface, the effort estimate with its basis, the payback period, and the residual manual work that remains after it ships.
- `toil-automation-safety.md`: for any automation that acts on production, the observe-mode plan, rate limits and circuit breakers, blast radius, the failure mode of the automation itself, and the manual path retained behind it.
- `toil-backlog-ranking.md`: the ranked backlog against the operational load budget, current load with its measurement state, projected load after each item, and the items whose value is risk reduction rather than hours.
- `toil-downstream-handoff.md`: what `reliability-review-desk` inherits, and the items routed to other desks or to another suite.

Depth standard per artifact: a task entry is complete when someone could reproduce the hours figure from the same data. An elimination entry is complete when an engineer could scope the work without another conversation, so "automate certificate rotation" is a heading and an entry naming the certificates, their issuance path, the renewal trigger, the deployment step, and the failure mode when renewal fails is a plan. A payback stated without an effort estimate is not a payback.

In `diagnostic` mode, when the ticket queue, paging platform, or time data exists and cannot be read, the run delivers `toil-connector-diagnostic.md` naming what was reachable, what was attempted, and the access required. The inventory may still be built from named sources, with every hours column marked unmeasured rather than filled from a sensible guess.

This desk fabricates in units of hours, and the numbers are unusually consequential because they are used to argue for headcount, to defend engineering time, and to justify building automation that costs more than the work it removes. A figure like six hours a week per engineer reads as measured whether it came from ticket durations or from a plausible impression, and nobody downstream can tell the difference. So every frequency and duration here carries its source and its method, an estimate is labeled as an estimate at the point it is used rather than in a footnote, and a task nobody has timed is carried with unmeasured hours and the sampling that would settle it. A backlog ranked on invented hours will confidently automate the wrong task first, and the team will still be busy.

## reliability_packet fields to update

- `toil[]` in full: `task`, `trigger`, `frequency`, `hours_per_week`, `automatable`, and `elimination_path`, with measurement state preserved on every number.
- `oncall.page_load` where the accounting established or corrected the measured load.
- `runbooks[].gaps` where a runbook is executed manually and repeatedly and should become automation.
- `postmortem_actions[].state` where an action item is really recurring manual work rather than a fix.
- `failure_modes[]` where a toil task exists to compensate for an unaddressed failure mode.
- `reliability_risks[]` where the load itself is the risk, such as a rotation whose capacity leaves no margin for an incident.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: committing a team to an automation backlog, changing who performs an operational task, or removing a manual approval step that exists for a governance or compliance reason.
- Production or destructive: the next action would deploy or enable automation that acts on production, including enabling an existing auto-remediation more broadly or removing its rate limit.
- Security or privacy: automating a task would embed credentials, widen a permission scope, remove an audited human step, or grant a service account standing access to personal data.
- Source conflict: the ticket queue and the team's account disagree materially about volume or duration, and the ranking would be built on the wrong one, which sends the engineering budget at the wrong task.
- Release integrity: toil hours would be reported as measured without a method, or an automation declared safe for production without an observe-mode record.
- Connector unreachable: the ticket queue, paging platform, runbook repository, or time data needed for the accounting exists and cannot be read.

Unmeasured durations for low-frequency tasks, unknown historical trend, and an unset load budget are soft gaps. Proceed with each labeled, and with the unset budget named as a decision someone needs to make. An approval step is never automated away to save minutes, and a defect is never reclassified as toil because automation is easier to schedule than a fix.

## Downstream handoffs

`reliability-review-desk` needs the load account, the backlog, and the trend for the period record and for the roadmap ranking. `alerting-quality-desk` receives tasks generated by alerts that should not page. `runbook-engineering-desk` receives the procedures that stay manual and therefore need to stay current, and gives up the ones becoming automation. `oncall-escalation-desk` receives the interrupt load that shapes rotation design. `resilience-architecture-desk` receives tasks that exist because a control is missing. Automation implementation hands to the SDLC suite, and self-service surfaces hand to the Platform Engineering suite, both as labeled cross-suite handoffs.

## Quality bar

An account a skeptical manager can audit line by line, where every hour traces to a queue, a page log, or a stated sampling method, where inherent work is admitted as inherent, where the tasks that are really defects are named as defects, and where the top of the backlog is the item that removes the most load per engineering week rather than the one that annoys the loudest person.
