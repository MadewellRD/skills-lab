---
name: reliability-review-desk
description: run the recurring service reliability review covering error budget attainment and burn across the period, error budget policy adjudication including whether a freeze applies and its exception path, incident page and toil trends, open postmortem actions and expiring waivers, the reliability risk register with exposure and owner, objective revision proposals, and a roadmap that ranks reliability debt by journey impact rather than by the loudest incident.
---

# Reliability Review Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the review artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent attainment figures, budget balances, trends, incident counts, action item states, waiver decisions, or agreement from a service owner who has not given it.

## Role

Own the periodic moment where reliability stops being a set of individual artifacts and becomes a decision about where engineering time goes. This is the review a service owner and a director attend together: what the budget did, what broke, what the team carried, what remains open, and what changes next period.

The review has a specific job that no other desk in the suite performs, which is adjudication. An error budget policy that is written but never applied is a document; the policy becomes real at exactly the moment someone looks at an exhausted budget and says the freeze applies, or grants an exception with a name attached to it. A review that reports the budget without adjudicating it has held a meeting.

Its second job is resisting recency. Reliability roadmaps drift toward whatever failed most recently and most visibly, and the loudest incident is frequently not the largest risk. Ranking by journey impact, by budget consumption, and by the exposure in the risk register produces a different order than ranking by memory, and the difference is the value of doing this on a cadence rather than after each outage.

## Use when

- The weekly, monthly, or quarterly service reliability review is due.
- An error budget is exhausted, nearly exhausted, or has been exhausted long enough that the policy consequence is overdue.
- A freeze is being proposed, is in force and needs an exit decision, or is being contested.
- Postmortem action items are aging, and their completion state needs adjudicating rather than reporting.
- Readiness waivers are approaching expiry and need renewal, closure, or escalation.
- The reliability roadmap for the next period needs setting, or a reliability investment case needs the evidence behind it.
- An objective no longer matches what users need, in either direction, and the revision needs evidence and agreement.

## Do not use when

- The objective itself is being defined or first computed: that is `slo-error-budget-desk`. This desk adjudicates against an existing objective and proposes revisions; it does not set one from scratch.
- A specific incident needs analysis: that is `postmortem-desk`, whose output this review consumes.
- The service is being launched, accepted for support, or gated: that is `production-readiness-review-desk`.
- The freeze question is really about how a specific change reaches production safely: that is `change-safety-desk`.
- The review is of the platform, its golden paths, or its adoption: cross-suite handoff to the Platform Engineering suite. Spend and commitment review goes to the FinOps suite.

## Required evidence

- Attainment per objective across the review period, with the window and the query behind each figure.
- Error budget consumed and remaining, and the burn events that consumed it, attributable to incidents, rollouts, or steady-state degradation.
- The error budget policy as written, with its stated consequence and its exception authority.
- Incident records for the period with severity, duration, detection source, and journey impact.
- Page load per rotation with its out-of-hours share, and the toil account with its measurement state.
- Open postmortem actions with owners, due dates, and ages, including actions from prior periods.
- Readiness waivers with owners and expiry dates.
- The reliability risk register carried from upstream stages, and the change failure rate for the period.
- The prior review record, so the period is a comparison rather than a snapshot.

## Workflow

**Outcome.** A review record a service owner and an executive can both act on: attainment and budget with their sources, the policy adjudication and its consequence, trends over enough periods to be a trend, open actions and waivers with states, the risk register with exposure and owners, and a ranked roadmap with the reason each item sits where it does.

**Grounding.** The metrics backend states attainment. The incident tracker states what broke. The paging platform states what the rotation carried. The action tracker states what was actually completed. Meeting notes and team accounts state intent and are labeled as such. Where the objective document and the computed attainment disagree, both are recorded per `references/suite-workflow-contract.md`, and the disagreement is escalated rather than reconciled by preferring the document.

**Constraints.** Every figure carries the query, dashboard, or export that produced it and the window it covers. A trend requires enough periods to be one; two points are a comparison and are described as a comparison.

Budget adjudication follows a mandated order, because negotiating the exception before applying the policy is precisely how a budget policy becomes advisory:

1. State the budget position against the policy as written, with the figure and its source.
2. State the consequence the policy specifies, whether that is a freeze, a reprioritization, a hand-back of support, or an escalation.
3. Take the exception, if one is sought, from the authority named in the policy, recorded with its rationale and an expiry.

An objective is never revised to match observed attainment as a way of clearing a budget deficit. A revision proposal carries evidence about what users actually need, names the journey and the measurement, and requires the owner's agreement; without that agreement it is recorded as proposed and the objective stands.

The roadmap ranks by journey impact, budget consumption, and risk exposure, and states its ranking basis explicitly so a reader can disagree with the order rather than only with the contents. An item promoted for a reason outside that basis, such as an executive commitment or a customer escalation, is recorded with that reason visible.

**Parallel surface.** Services, objectives, journeys, incidents, action items, waivers, and risk register entries are independent units and are parallel-safe: per-objective attainment retrieval, per-incident summarization, per-action status lookups, per-waiver expiry checks, and connector preflight across metrics, incident tracker, paging platform, and action tracker all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: the policy adjudication, the roadmap ranking, composing budget across the journey rather than per service, judging whether several separately acceptable services combine into an unacceptable journey, and reading trends across the period set. Ranking is inherently aggregate, since the whole point is a single order across items that were assessed independently.

**Acceptance bar.** Every number carries its source and window or is written as unmeasured. The budget position for every objective is stated and adjudicated against the policy, including the objectives where the policy is silent. Every open action and waiver has a state, an age, and an owner. The roadmap is ordered with its ranking basis stated. The review names what changed since the last one, including the things that did not change and were supposed to.

## Outputs

A complete run delivers this artifact set:

- `reliability-review-record.md`: the period under review, attainment per objective with sources, budget consumed and remaining, incidents by severity with journey impact, page load and toil, change failure rate, and the deltas against the prior period.
- `reliability-budget-adjudication.md`: the budget position per objective, the policy consequence that applies, the decision taken, any exception with its authority rationale and expiry, and the freeze status with its entry and exit conditions.
- `reliability-risk-register.md`: each risk with the journeys affected, the exposure a user would experience, the current control, the owner, and its movement since the last review.
- `reliability-action-and-waiver-status.md`: open postmortem actions and readiness waivers with owner, age, due or expiry date, current state, and the adjudication for each overdue item.
- `reliability-roadmap.md`: the ranked reliability work for the next period with the ranking basis, the journey each item protects, the debt it closes, the effort where it is known, and the items explicitly not being taken with the reason.
- `reliability-objective-revisions.md`: proposed changes to objectives with the evidence and the agreement state, or the explicit statement that no revision is proposed.
- `reliability-review-downstream-handoff.md`: what returns to `slo-error-budget-desk`, what goes to the orchestrator for workflow close, and what hands to another suite.

Depth standard per artifact: an attainment row carries the objective, the measured value, the window, and the query. A risk entry states what a user experiences if it lands, not a category name. A roadmap item states the journey it protects and the debt it closes, since a list of engineering tasks without that linkage is a backlog rather than a reliability roadmap. An adjudication that reports a budget position without stating the consequence is incomplete.

In `diagnostic` mode, when the metrics backend, incident tracker, paging platform, or action tracker exists and cannot be read, the run delivers `reliability-review-connector-diagnostic.md` naming what was reachable, what was attempted, and the access required. No budget adjudication is issued in that mode, because a freeze decision made without the budget figure is an opinion with consequences.

The specific way this review goes wrong is the manufactured trajectory. Executive-facing reliability reporting wants a direction: improving, stable, degrading. That sentence is easy to write from three incidents and a feeling, it is what the audience is listening for, and once it is said the roadmap gets ranked to match it. So every trend in these artifacts names the periods it spans and the figures at each, a comparison across two periods is called a comparison, and a direction is asserted only where the series supports it. The adjacent trap carries the same rule: an action item is reported as done only when the tracker or the change record says so, never because its due date has passed, and a waiver is reported as closed only when someone closed it.

## reliability_packet fields to update

- `slos[].current_attainment`, `error_budget_remaining`, `burn_rate`, `budget_policy`, and `agreement_state` for the period, each with its window.
- `reliability_risks[]` in full: risk, journeys affected, exposure, current control, and owner.
- `postmortem_actions[].state` and `due` as adjudicated in the review.
- `readiness_gates[].state` and `expiry` where a waiver was renewed, closed, or escalated.
- `operating_posture` set to `freeze` or `budget_exhausted` where the adjudication puts it there.
- `oncall.page_load` and `toil[]` trend state for the period.
- `change_controls.change_failure_rate` for the period, with its source.
- `decisions` with the adjudication and the roadmap order, `assumptions` where a figure rests on one.
- `source_facts` with attribution, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: declaring or lifting a freeze, granting a budget policy exception, revising an objective, closing a waiver, or reassigning a risk to an owner who has not accepted it.
- Production or destructive: the next action would enforce a freeze in the deployment system, disable a pipeline, remove support for a service, or otherwise change a live control rather than record the decision.
- Security or privacy: the review would restate incident detail containing personal data, customer identifiers, or security specifics in a document circulated more widely than that content allows.
- Source conflict: the objective document and the computed attainment disagree, the action tracker and the team's account disagree about completion, or the incident record and the budget consumption disagree about what was spent. Adopting one silently launders a guess into a freeze decision or a roadmap.
- Release integrity: an objective would be reported as met, a risk reported as controlled, or an action reported as complete without the evidence that supports it.
- Connector unreachable: the metrics backend, incident tracker, paging platform, or action tracker needed for the period figures exists and cannot be read.

An unmeasured toil figure, an absent prior review, and an unknown effort estimate for a roadmap item are soft gaps. Proceed with each named. The budget policy is applied as written before any exception is discussed, an objective is never lowered to make a period look better, and an overdue action is never quietly re-dated to keep the list short.

## Downstream handoffs

The orchestrator receives the review record for workflow close. `slo-error-budget-desk` receives objective revision proposals and the evidence behind them when the review concludes an objective no longer describes what users need. `production-readiness-review-desk` receives waiver adjudications and the debt that remains open. `change-safety-desk` receives the freeze decision and its exit conditions. `toil-reduction-desk` and `alerting-quality-desk` receive the roadmap items that belong to them. Engineering delivery of roadmap items hands to the SDLC suite, and spend implications hand to the FinOps suite, both as labeled cross-suite handoffs.

## Quality bar

A review where the budget position produced an actual decision rather than a slide, where every figure can be traced to a query in front of the room, where the risk register describes what a user would experience rather than a category, and where the top of the roadmap is defensible against someone who only remembers last month's outage.
