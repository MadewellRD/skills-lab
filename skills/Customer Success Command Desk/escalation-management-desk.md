---
name: escalation-management-desk
description: run the escalation record from the customer raised-at timestamp that starts every committed clock, with business impact in the customer's own words, severity assessed on customer impact rather than internal effort, named internal owner and executive sponsor at the severity the impact warrants, an action plan with an owner and date on every item, updates delivered on the committed cadence whether or not there is progress, relationship repair alongside the technical fix, and closure only on customer confirmation. use for red accounts, critical situations, executive escalations, service disruptions, and missed commitment recovery.
---

# Escalation Management Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the escalation artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the escalation item it affects, and record it in `open_questions`. Never invent a raised-at timestamp, an update that was not sent, an owner, an executive commitment, a root cause, or a customer confirmation of resolution.

## Role

This desk owns the record of a moment the customer will remember for the rest of the relationship, and it owns the clocks that moment started. It records the escalation as the customer raised it: the raised-at timestamp, which is when they raised it rather than when the internal team understood it, and the business impact in their own words rather than in the ticket's summary. Those two fields govern everything else, because every committed clock runs from the first and every severity judgment should be anchored to the second.

It owns severity assessed on customer impact rather than on internal effort, which is the inversion most escalation processes make: a small bug blocking a month-end close is a higher severity than a large defect nobody is waiting on. It owns the named internal owner and, at the severity the impact warrants, the executive sponsor, with what that executive is actually being asked to do rather than a name added to a distribution list.

It owns the action plan with an owner and a date on every item, the communication plan with the committed cadence and the next update due, and the updates themselves, delivered on cadence whether or not there is progress, because in an escalation the damage comes from silence more reliably than from the incident. It owns the relationship repair work that runs alongside the technical fix, and closure only on the customer confirming the impact has ended.

## Use when

- A customer has raised something as an escalation, a red account, or a critical situation, however informally.
- An executive on the customer side has been drawn in, or has asked for one on the company side.
- A commitment has been missed and the customer has said so.
- A service disruption, defect, or delivery failure has a business consequence the customer is now managing.
- An escalation is open and the update cadence is at risk of being missed.
- An escalation is being closed and the basis for closure has to be the customer's confirmation.

## Do not use when

- The problem is quiet and the work is naming and sizing it before the customer does. That is `churn-risk-desk`.
- The recovery plan carries a commercial concession as its core. That is `save-play-desk`, which this desk hands to.
- The subject is the technical incident, its root cause, and its engineering remediation. Route that to the support and engineering path; this desk keeps the relationship consequence and the committed cadence.
- The onboarding is late and the customer has not raised it. That is `onboarding-time-to-value-desk`.
- The subject is designing the plays that run when escalations occur. That is `playbook-design-desk`.

## Required evidence

- The escalation as the customer raised it, with the timestamp, the channel, the person who raised it, and their statement of impact verbatim.
- Affected products, environments, user populations, and the business process the customer runs on them.
- The support and incident record with its current state, severity, and the history of what has already been communicated.
- Prior escalations on this account, their outcomes, and whether previous commitments from them were honored.
- Contractual service commitments, service level terms, and any credit or remedy terms in the agreement.
- The executive relationship on both sides, including who has met whom and any prior executive contact.
- Internal owners for each contributing system and the queue each item actually sits in.
- The communication cadence already promised to the customer, and every update sent so far with its timestamp.

## Workflow

**Outcome.** An escalation record with the raised-at timestamp and impact in the customer's words; severity on customer impact; the internal owner and, where warranted, the executive sponsor with their specific role; an action plan with owners and dates; a communication plan with the committed cadence and the next update due; the update log; the relationship repair track; and a closure position that rests on the customer's confirmation.

**Grounding.** The raised-at timestamp comes from the customer's own message, ticket, or call record, not from when the internal team triaged it, because that difference is frequently days and every commitment is measured from the earlier moment. Impact is quoted from the customer, since the internal restatement of an impact reliably shrinks it. Update history is read from what was actually sent, with timestamps, rather than from what the plan said would be sent. Contractual remedies are read from the executed agreement rather than from what feels fair under pressure. Where the customer's account of the impact and the internal incident record genuinely disagree on scope or duration, both are preserved, because the customer's version is the one the relationship runs on and the internal version is the one the remediation runs on.

**Constraints.** Severity is set on customer impact and is stated with the business process affected and the population, so it can be argued with. The executive sponsor is assigned with a defined role, since an executive named without a job is a name in a status document. Every action item has a named owner and a date; an item owned by a team is unowned. The update cadence is committed to the customer explicitly and is met whether or not there is progress, and an update with no progress states that plainly rather than being delayed until there is something better to say. Anything the company offers under pressure, including credits, remedies, service commitments, and written acknowledgements of fault, waits for the authority that can grant it, and the clock does not pause while that is sought. Closure requires the customer to confirm the impact has ended; an internal resolution is a state of the fix, not a state of the escalation.

**Mandated order, which runs from when the customer raised it rather than from when the cause is understood.** This order is mandated because the relationship damage in an escalation is caused by silence rather than by the incident, and step 2 does not wait for steps 3 through 5 to reach certainty. A missed update is a second escalation stacked on the first:

1. Record the raised-at timestamp and the business impact in the customer's own words. Every committed clock runs from that moment.
2. Acknowledge to the customer and commit to an update cadence, before the internal diagnosis is complete.
3. Assign the internal owner and, at the severity the impact warrants, the executive sponsor.
4. Publish the action plan with an owner and a date on every item.
5. Update on the committed cadence whether or not there is progress to report.
6. Close only on the customer confirming the impact has ended.

**Parallel surface.** Independent items fan out safely: individual action items on separate systems, per-system diagnosis, evidence gathering across support, telemetry, and contract records, the contractual remedy analysis, and multiple open escalations across a book being assessed at once. The customer-facing sequence above is sequential by mandate and is not part of the parallel surface. The severity judgment, the communication plan, and the closure position are single passes, because each is a statement about the escalation as a whole and an escalation with two parallel narratives reaching the customer is a worse escalation.

**Acceptance bar.** The record carries a raised-at timestamp from the customer's own record and their impact statement verbatim. Severity names the business process and population affected. Every action item has a named owner and a date. The committed cadence is stated with the next update due as a timestamp. The update log shows what was sent and when, including the gaps. Closure is recorded only against a customer confirmation with the person and the date. Any concession appears with its approval state and named approver rather than as an intention.

## Outputs

A complete run delivers this set:

- `escalation-record.md`: raised-at timestamp with its source, the raising stakeholder, business impact verbatim, affected products and populations, severity with its basis, internal owner, executive sponsor and their role, and the current state.
- `action-plan.md`: every workstream item with a named owner, a date, its dependency, and its current state, with the items on the critical path to impact ending marked as such.
- `communication-plan.md`: the cadence committed to the customer, the next update due as a timestamp, the audience for each update, who delivers it, and the escalation path if an update will be missed.
- `update-log.md`: every update sent with its timestamp, audience, and content summary, and every committed update that was missed, recorded as missed rather than omitted.
- `commitment-and-remedy-position.md`: what has been committed to the customer so far and by whom, the contractual remedies that actually apply with the clause behind each, and any proposed concession with its value, its required authority, and its approval state.
- `relationship-repair-plan.md`: the trust damage separate from the technical fault, the stakeholders whose confidence changed, the executive engagement designed around what the executive is being asked to decide, and the follow-through after the fix lands.
- `closure-record.md`: the customer confirmation with the person and the date, the impact-ended statement in their words, the commitments left outstanding after closure, and the follow-up items with owners.
- `escalation-downstream-handoff.md`: what `churn-risk-desk` and `save-play-desk` inherit, including the risk this escalation created independent of whether the technical issue is fixed.

Depth standard: an artifact is complete when a new owner could take the escalation over mid-flight and know exactly what the customer was last told, what is due next, and by when. An action item with no owner, or a cadence with no next-update timestamp, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the support record, the communication history, or the contract terms cannot be reached, the run delivers `escalation-connector-diagnostic.md` naming each unreachable source and what cannot be established, while stating the running clocks and who must be told now. A running clock is never held pending evidence; the update goes out on cadence with what is known.

Anti-fabrication guard: the temptation here is to repair the record. An escalation is written up under pressure, often after the fact, by people who know how it should have gone, and the small corrections are the dangerous ones: the raised-at timestamp quietly moved to when the internal team picked it up, which makes a four-day silence look like one; an update logged as sent because it was drafted; the impact restated in the ticket's language, which narrows a month-end close failure into a report rendering issue; a root cause written before engineering has one; and closure recorded because the fix shipped rather than because the customer said the impact ended. Each of those makes the record read better and makes the account's history useless, which matters because this record is what the renewal conversation and the churn postmortem are read against, and the customer keeps their own version. In these artifacts the raised-at timestamp is quoted from the customer's own message with the channel named, impact is quoted verbatim, and an update appears in the log only if it was sent, with missed updates recorded as missed. An executive sponsor appears only where a named executive accepted the role. A remedy or credit appears with its approval state, never as a stated intention, since anything written in an escalation artifact tends to be read aloud to the customer by someone who assumed it was agreed. Closure names the person who confirmed and the date they confirmed it, and where nobody has, the state reads `resolved_pending_confirmation` for as long as that is true.

## success_packet fields to update

- `escalations[]` with `escalation_id`, `raised_by`, `raised_on` as the customer's timestamp, `severity`, `business_impact` in the customer's words, `systems_or_products[]`, `internal_owner`, `executive_sponsor`, `action_plan[]` with owners and dates, `update_cadence`, `next_update_due`, `updates_sent[]`, `state`, `customer_confirmed_resolution`, and `root_cause_ref`
- `active_clocks[]` for the next committed update and any contractual response or restoration commitment, each with its start event and due date
- `commitments[]` for everything committed to the customer during the escalation, with who made it, to whom, and its state
- `approvals[]` for executive engagement, service credits, contractual remedies, and any written acknowledgement of fault, each with the named approver and authority level
- `risks[]` for the relationship risk the escalation created, with ARR exposed, first detected date, and an owner, held open independently of the technical fix
- `stakeholders[]` updated where dispositions changed, a new executive entered, or the raising stakeholder's standing shifted
- `source_facts` with collection dates, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: executive engagement, a service credit, a contractual remedy, and any written acknowledgement of fault are commitments the company is held to afterward, in the moment where the pressure to concede something immediately is at its highest. The clock does not pause while approval is sought, so the update goes out on cadence with what is known and the concession waits for the person who can authorize it.
- **Production or destructive**: the next action would change the customer's live environment, roll back a release affecting them, or close the escalation record of record before the customer has confirmed the impact ended.
- **Security or privacy**: the escalation involves a data exposure, a breach notification obligation, or customer personal data, and the communication would go out before the path that owns those obligations has cleared it. A notification made incorrectly is itself a regulatory event.
- **Source conflict**: the customer's account of the impact and its duration and the internal incident record genuinely disagree, and adopting the internal version silently understates what the customer experienced and will be contradicted by them in the review that follows.
- **Release integrity**: a root cause, a remediation date, or a resolution would be stated to the customer without the evidence to support it. A date given in an escalation is planned against, and a second missed date costs more than the original fault.
- **Connector unreachable**: the support record, the communication history, or the contract terms exist and cannot be read, so the escalation's state or its remedy position would be asserted about a record nobody opened.

An unestablished root cause, an unknown fix date, an unconfirmed contributing system, and a pending engineering estimate are soft gaps and are never a reason to miss an update. Send the update on cadence, state what is not yet known, label the assumption, and continue.

## Downstream handoffs

`churn-risk-desk` is next and needs the escalation as a risk in its own right, with the ARR exposed and the first-detected date, because the relationship damage outlives the technical fix and an escalation closed cleanly still moves a renewal. `save-play-desk` needs the commitments made under pressure, the concession position with its approval state, and which relationships survived. `renewal-preparation-desk` needs the escalation history and any commitment still outstanding at the renewal, since an unresolved escalation inside the notice window changes the negotiation. `qbr-ebr-desk` needs the honest treatment of what happened, because the review that omits the escalation the customer lived through loses the room. `voice-of-customer-desk` needs the underlying cause where it recurs across accounts. `value-realization-desk` should know which period the impact covered, since an outage inside a measurement window affects the numbers.

## Quality bar

Good escalation work is timestamped throughout and written in the customer's language. The impact statement sounds like the customer, not like the ticket. Severity is argued from their business consequence, so a defect that blocks a regulated filing outranks a larger one nobody is waiting on. The action plan has names on it, not teams, and the communication plan has a specific next-update time that somebody is accountable for hitting, including the update that says there is nothing new. The record keeps missed updates visible, because they are the most diagnostic entries in it. The relationship track is treated as real work rather than as something that resolves itself when the fix ships, since the sponsor who spent a week explaining this internally has a longer memory than the incident. And closure waits for the customer, because the escalation belongs to them, and the only person who can say the impact has ended is the person who was living with it.
