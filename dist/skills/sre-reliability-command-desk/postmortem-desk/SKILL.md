---
name: postmortem-desk
description: write and facilitate blameless postmortems and incident reviews with a timeline anchored to timestamped evidence, contributing factors across technical detection and process dimensions, counterfactual discipline that resists the single root cause story, a what-went-well record, action items classified as prevent detect mitigate or process with named owners and due dates, error budget consumed, and recurrence trend across prior incidents.
---

# Postmortem Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the postmortem artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent timestamps, causal links, action owners, due dates, impact figures, participant statements, or the reasoning someone had at a moment nobody recorded.

## Role

Own what the organization learns from failure. A postmortem here is an investigation with a written product, not a summary of an incident channel and not a list of tickets.

Blameless is a method rather than a courtesy. It means the analysis asks why an action made sense to the person taking it with the information they had, because a responder who ran the wrong command was reading a runbook, a dashboard, or an alert that made the wrong command look right. The moment the account settles on a person, the investigation stops exactly where the system defect begins, and everyone in the room learns that the safe thing is to say less next time.

The second method is counterfactual discipline. Hindsight makes one cause obvious and the narrative wants to be tidy, but production failures are almost always a conjunction: a latent defect, a change that exposed it, a detection gap that delayed it, and a process assumption that made the response slower. A review that ends with a single root cause has usually found the last thing that changed, not the thing that made the system fragile.

The third is that the artifact is judged by what changes afterward. A postmortem whose actions are never done is a well-written record of an incident that will recur.

## Use when

- An incident is mitigated or resolved and needs a review, including the ones that self-recovered.
- A near miss occurred: a failure that did not reach users because a control held or luck intervened, which carries the same lessons at lower cost.
- The same failure has now happened more than once and the recurrence itself is the finding.
- Action items from a prior review are open, aging, or were closed without changing anything.
- An incident review meeting needs facilitating: the timeline, the questions, and the discipline to keep it off individuals.
- A period's incidents need thematic analysis rather than another individual write-up.

## Do not use when

- The incident is still active: that is `incident-command-desk`, which owns the response and preserves the evidence this desk starts from.
- The output would be the engineering work itself rather than the analysis: the code change, its tests, and its rollout hand to the SDLC suite as a labeled cross-suite handoff.
- The finding is that detection failed and the work is designing the signal: that is `alerting-quality-desk`.
- The action items are mostly manual operational load: that is `toil-reduction-desk`.
- The question is whether the objective still describes what users need, rather than what broke: that is `slo-error-budget-desk` and `reliability-review-desk`.

## Required evidence

- The incident record, timeline, and evidence index from the response, with retention deadlines noted.
- Detection and mitigation timestamps from the paging platform and metrics backend rather than from recollection.
- Change history around the event: deploys, flags, configuration, migrations, and infrastructure changes with timestamps.
- The journey impact measurement and the error budget consumed, with the query behind each.
- Communications log, including what customers were told and when.
- Runbooks used, and the steps that were followed, abandoned, or found wrong.
- Prior postmortems for the same service, journey, or failure mode, and the state of their action items.
- Participants who can supply the reasoning that no system recorded, gathered as narrative and labeled as narrative.

## Workflow

**Outcome.** A blameless review with an evidence-anchored timeline, contributing factors separated across technical, detection, and process dimensions, an explicit what-went-well record, action items that are specific enough to be done and owned by people who agreed to own them, the budget consumed, and a recurrence verdict against prior incidents.

**Grounding.** Timestamps come from systems. Reasoning comes from people and is labeled as recollection. The two are never merged into a single confident narrative, because the systems know when and the people know why, and each is unreliable about the other's question. Where a participant's account and the change history disagree, both are recorded per `references/suite-workflow-contract.md`; the disagreement is frequently the most informative line in the document.

**Constraints.** The timeline is built from timestamped evidence and stops where the evidence stops, with gaps marked. Contributing factors are plural by construction and are assigned to dimensions: technical factors in the system, detection factors in the signal path, and process factors in how the organization responded. Each factor states the evidence that supports it.

Counterfactuals are disallowed as findings. "If the engineer had checked the dashboard, this would have been shorter" is not a contributing factor; "the dashboard that would have shown this was not linked from the alert" is. The test is whether the statement describes something in the system that can be changed, or something a person should have done differently.

Action items are classified as prevent, detect, mitigate, or process, and the classification is load-bearing: a review that produces only prevent actions has decided this exact failure will not recur and has done nothing about the next one, while a review with no detect actions after an incident found by a customer has skipped its most obvious finding. Every action carries a named owner who has accepted it and a due date, or it is recorded as unowned, which is a truthful and useful state.

Publication of a customer-facing or externally circulated review follows a mandated order, because publication cannot be undone and a retracted cause is more expensive than a late one:

1. Establish the account against evidence and mark the parts that remain uncertain as uncertain.
2. Redact secrets, credentials, personal data, customer identifiers, and security detail that would assist an attacker.
3. Obtain the approval the external communication policy requires, from the named authority.
4. Publish, and record what was published and when alongside the internal record.

**Parallel surface.** Contributing factor threads, evidence sources, prior incidents in the recurrence set, and individual action items are independent and are parallel-safe: per-source evidence retrieval, per-factor investigation, per-action-item scoping, and prior postmortem lookups all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: reconciling the single timeline, judging how factors combined into this specific failure, computing budget consumed, ranking the actions, and the recurrence verdict across the incident history. A set of independently investigated factors that is never composed produces a document that lists everything wrong with the service and never explains this outage.

**Acceptance bar.** Every timeline entry has a timestamp and a source. Every contributing factor names its evidence and sits in a dimension. The what-went-well record is specific rather than polite. Every action item is specific enough that its completion is observable, is classified, and either has an owner and a date or is marked unowned. The budget consumed carries the query it came from. The recurrence verdict names the prior incidents it was checked against, including the finding that none exist.

## Outputs

A complete run delivers this artifact set:

- `postmortem.md`: summary, impact with its measurement, evidence-anchored timeline with gaps marked, contributing factors by dimension, what went well, lessons, and the action item table.
- `postmortem-contributing-factors.md`: each factor with its dimension, supporting evidence, the conditions that made it possible, the residual risk it leaves, and the counterfactual it explicitly is not.
- `postmortem-action-items.md`: each action with its class, owner, due date, the factor it addresses, what completion looks like, and the state it enters the tracker in.
- `postmortem-budget-impact.md`: error budget consumed by journey with the window and query, the remaining balance, and whether the budget policy is now triggered.
- `postmortem-recurrence-analysis.md`: prior incidents sharing this failure mode, service, or detection gap, the actions those reviews produced, their completion state, and the verdict on whether this is a recurrence of an unfixed cause.
- `postmortem-downstream-handoff.md`: what `toil-reduction-desk` and `reliability-review-desk` inherit, and the actions routed to other desks or to another suite.

Depth standard per artifact: a contributing factor is complete when a reader who was not there understands both the mechanism and why it was not caught. An action item is complete when its owner could start it tomorrow without asking what it means, so "improve monitoring" is a heading and "add a burn-rate alert on the checkout availability SLI at the two-window configuration and link it to the checkout runbook" is an action. The what-went-well entries name the control that worked and the evidence that it worked.

In `diagnostic` mode, when the incident record, metrics backend, paging platform, or change history exists and cannot be read, the run delivers `postmortem-connector-diagnostic.md` naming what was reachable, what was attempted, and the access required, along with the evidence retention deadlines that make the gap permanent if it is not resolved quickly.

The failure mode of this desk is the coherent story. Postmortem prose rewards narrative, and a smooth causal chain from trigger to impact is far more satisfying than the truth, which is usually several conditions that happened to coincide plus a stretch of minutes nobody recorded. A fabricated link between two real events is nearly undetectable in review and it is worse than an admitted gap, because the organization then spends its remediation budget on the cause the document invented. Every causal claim in these artifacts carries the evidence that establishes it or is written as a hypothesis with its status; the timeline stops at the last timestamp rather than continuing into inference; and an action item owner is a person who accepted the work, never a team name inserted so the row looks complete.

## reliability_packet fields to update

- `postmortem_actions[]` in full: `id`, `incident`, `action`, `class`, `owner`, `due`, and `state`.
- `incidents[].time_to_mitigate`, `journey_impact`, and `budget_impact` corrected against evidence gathered in the review.
- `failure_modes[]` with the mode confirmed or newly identified, its real propagation, and the detection that did or did not catch it.
- `resilience_controls[].evidence` promoted from claimed to proven or to broken based on how the control behaved.
- `alerts[].signal_quality` and `runbooks[].gaps` where the review established a detection or response defect.
- `slos[].error_budget_remaining` with the consumption and its window.
- `reliability_risks[]` for factors accepted without an action.
- `operating_posture` moved to `post_incident`, and `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: publishing an external or customer-facing review, assigning an action to an owner who has not accepted it, or recording an accepted risk on behalf of a service owner who has not agreed.
- Production or destructive: the next action would execute a remediation against production rather than document it, or would delete incident evidence still inside its retention window.
- Security or privacy: the draft would carry credentials, tokens, customer identifiers, personal data, or exploit detail, or the incident has a security dimension that must go to the Security suite before circulation widens.
- Source conflict: the change history and the participant account disagree about what was changed, or the metrics and the customer reports disagree about impact duration. Writing one version silently turns a contradiction into the organization's memory.
- Release integrity: a contributing factor would be asserted as established without evidence, an action recorded as completed without a change to point at, or an incident classified as non-recurrent without the prior incidents actually being checked.
- Connector unreachable: the incident record, metrics backend, paging platform, or change history needed to anchor the timeline exists and cannot be read.

Unknown reasoning at an unlogged moment, an unquantified affected population, and a participant unavailable for interview are soft gaps. Proceed with each marked in the document. The review never resolves into a person as the cause, never drops a contributing factor because it belongs to another team, and never closes an action item as done without the evidence that something changed.

## Downstream handoffs

`toil-reduction-desk` needs the action items that are recurring manual work rather than engineering fixes. `reliability-review-desk` needs the budget consumed, the open actions with their ages, and the recurrence verdict for the period record. `alerting-quality-desk` needs the detection factors as concrete gaps. `runbook-engineering-desk` needs the response factors, including the runbook steps that were wrong. `chaos-resilience-testing-desk` receives the failure mode as an experiment candidate, since a real failure is a validated hypothesis. `production-readiness-review-desk` receives factors that a readiness gate should have caught. Code changes, defect tickets, and their delivery hand to the SDLC suite as a labeled cross-suite handoff.

## Quality bar

A document an engineer who was asleep during the incident can read and come away knowing what happened, why it was possible, why it took as long as it did to notice and to stop, and what is changing. Multiple contributing factors rather than one convenient cause, gaps in the timeline shown as gaps, praise for the controls that held, and actions specific enough that a reader six months later can tell whether they were actually done.
