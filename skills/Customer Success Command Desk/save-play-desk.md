---
name: save-play-desk
description: build the recovery plan for an at-risk account matched to the root cause rather than the symptom, with the concession stated at its value with a named approver and authority level, executive engagement designed around a decision, checkpoints testing observable customer signals, explicit abandonment criteria, and a managed off-ramp where wind-down is the honest outcome. use for save campaigns, red account recovery, retention plays, discount and credit requests, downgrade negotiation, and deciding when a save has failed.
---

# Save Play Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the save artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the play, the checkpoint, or the concession it affects, and record it in `open_questions`. Never invent an approver, an authority level, a concession the company has agreed to, a customer commitment, or an outcome from a comparable save.

## Role

This desk owns the plan that tries to keep the account, and it owns the honesty about whether the plan is working. A save play is built against the root cause carried in from the risk register, not against the symptom that made the account visible. Enablement sessions do not fix a workflow that moved into another tool. A discount does not fix an integration that has been broken since a release in the spring. An executive dinner does not fix an unresolved escalation. Matching the play to the cause is most of the difference between a save and a delayed churn, and the desk states its hypothesis explicitly: why this play addresses this cause, and what would have to be observed for the hypothesis to be wrong.

It owns the commercial component with the discipline that component requires. A concession is written with what it is, what it is worth, who has to authorize it at the org's required level for that value, and its current approval state. Discount, credit, term extension, ramped pricing, a service commitment, professional services at no charge, and a contractual remedy are all concessions, and a service commitment is frequently the most expensive of them because it binds the company's people for the length of the term.

It owns the sequence of moves with customer-facing steps separated from internal ones, executive engagement designed around a specific decision the executive is being asked to make rather than around presence, checkpoints that test observable customer behaviour on a date, the abandonment criteria that say this save has failed, and the managed off-ramp for the cases where the honest outcome is a wind-down. The off-ramp is real work: a customer who leaves well is a future win-back, a reference-safe departure, and a churn record with a usable reason. A customer who leaves after three months of unanswered optimism is a public account of what working with the company is like.

## Mandated order for the concession, and why it is ordered

The commercial part of a save runs in this order, and the order is externally mandated because an offer cannot be unoffered: the number the customer sees becomes the floor for this negotiation and the anchor for the next renewal, no matter what was authorized afterward.

1. Size the concession against the exposure and the cause, with the value computed.
2. Obtain authorization at the level the org requires for that value, from a named approver.
3. Only then place the concession in anything the customer can see, including a draft shared for feedback and a verbal indication on a call.

Steps 1 and 2 do not wait for each other to be comfortable, and step 3 does not begin early because the customer is on the phone and the moment feels right. Everything else in the play, including the diagnosis, the executive engagement, and the relationship repair, proceeds while authorization is pending.

## Use when

- A risk has a root cause, an owner, and an ARR exposure, and the question is what the company actually does about it.
- An escalation has stabilized technically and the relationship consequence still has to be worked.
- A customer has signalled non-renewal, a downgrade, or a competitive evaluation and there is still time to act.
- A commercial concession is being contemplated and its value, authority level, and consequences need stating before anyone speaks to the customer.
- A save already in flight has reached a checkpoint and the question is whether to continue, change the play, or stop.
- The honest position is that the account is leaving and the departure needs to be managed rather than denied.

## Do not use when

- The risk itself has not been evidenced, sized, or traced to a cause. That is `churn-risk-desk`, whose register this desk consumes.
- The customer has just raised something and the committed update clock is the live issue. That is `escalation-management-desk`; a save runs alongside it, not instead of it.
- The work is defining a reusable play with a trigger and a threshold for a whole segment. That is `playbook-design-desk`; this desk runs a play against one named account.
- The subject is the renewal timeline, forecast category, and close plan. That is `renewal-preparation-desk`, which inherits the save outcome.
- The commercial negotiation, quote construction, and contract paper are the subject. Those belong to the sales suite; this desk prepares the position and the approval request.

## Required evidence

- The risk or escalation with its root cause, its evidence, its ARR exposure, and its owner.
- The stakeholder map with who can still be reached, who decides, who has gone dormant, and where the relationship survives the current dissatisfaction.
- The value position: what has actually been delivered and validated, and what was promised and has not been.
- Contract facts including term end, notice deadline, auto-renewal behaviour, termination rights on both sides, and any remedy the agreement already provides.
- The concession catalogue available to this account with the authority level each value band requires, plus any pricing or discount policy in force.
- The commitment register, since an outstanding sales-cycle promise is frequently both the cause and the cheapest concession.
- Capacity of the people the play needs: the CSM, the technical resource, the executive, and any professional services time it assumes.
- Outcomes of comparable saves with what was tried, what it cost, and what happened.

## Workflow

**Outcome.** A save plan per risk, stating the hypothesis linking play to cause, the sequence of moves with owners and dates and customer-facing steps separated from internal ones, the concession with its value, required authority level, named approver, and approval state, the executive engagement with the decision being asked for, checkpoints with the observable signal each tests and the date it is tested, the abandonment criteria, and the managed off-ramp position.

**Grounding.** The play is grounded in the cause the risk register established, and where the cause is recorded as not established, the first move of the play is the diagnosis rather than a concession. Concession authority comes from the policy in force, quoted; an authority level assumed from what feels proportionate is the fastest way to have a save unwound by the person who actually owns the number. What the customer values is taken from what a named stakeholder said, with the date, rather than from what would be convenient to offer. Comparable saves inform the play only where the comparison is genuine in cause, segment, and size.

**Constraints.** Every checkpoint tests something the customer does, not something the company does: a delivered training session is an activity, while thirty of the forty licensed users completing the reconciliation workflow in the two weeks after it is the signal. Every checkpoint has a date, and reaching it without the signal is a result rather than an occasion to extend. Abandonment criteria are written before the play starts, because they are unwritable once the sunk cost exists. A concession is priced at what it costs across the term, including the renewal it anchors, not at this year's delta. Relationship repair runs alongside the technical or commercial fix rather than after it. Where the play depends on a product change, the dependency is named with its state, and a roadmap item is carried at the confidence the company can stand behind rather than at the confidence the customer needs to hear.

**Parallel surface.** Independent items fan out safely: separate risks each getting their own play, individual concession options being priced and traced to their authority level, individual stakeholder outreach threads, and comparable saves being mined for outcome. The aggregate is a single pass after the fan-out returns, because ranking the save queue against the capacity that actually exists, and deciding which accounts get an executive when there are four executives and eleven candidates, are statements about the whole set. Within one account the plan is also a single pass, since the moves interact: a concession changes what the executive conversation is about, and an off-ramp assessment changes how much is worth spending on the play.

**Acceptance bar.** Every play names the cause it addresses and states why it addresses that cause. Every concession carries its value, its required authority level, its named approver, and its state, and no concession is present in customer-facing material without approval recorded. Every checkpoint names an observable customer signal and a date. Abandonment criteria exist and are specific. The off-ramp position exists even where the play is expected to succeed. Capacity is named, so the plan is one the assigned people can actually run.

## Outputs

A complete run delivers this set:

- `save-plan.md`: per risk, the hypothesis, the sequence with owners and dates, customer-facing moves separated from internal ones, and the dependencies each move carries.
- `concession-request.md`: the concession, its value computed across the term, the exposure it is set against, the required authority level with the policy it comes from, the named approver, the approval state, and the precedent it sets for this account and this segment.
- `executive-engagement-brief.md`: who is being asked to engage, with whom on the customer side, the specific decision being sought, the three facts that executive needs, and what the company is prepared to commit in the room.
- `checkpoint-schedule.md`: each checkpoint with its date, the observable customer signal it tests, the source that will show it, the owner, and the action if the signal is absent.
- `abandonment-criteria.md`: the conditions under which this save is declared failed, written before the play starts, with the person who makes that call.
- `off-ramp-plan.md`: the managed wind-down position covering data export, transition support, contractual end state, what is said and by whom, and the win-back conditions worth recording.
- `save-play-downstream-handoff.md`: what `value-realization-desk`, `renewal-preparation-desk`, and `retention-portfolio-reporting-desk` inherit, including the concession precedent and the play's measured effect.

Depth standard: an artifact is complete when the named owner could execute the next move tomorrow and an approver could grant or deny the concession from the request without asking a question. A checkpoint without a signal, a concession without an authority level, or a play whose hypothesis is "increase engagement" is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the contract, the concession policy, or the usage evidence cannot be reached, the run delivers `save-connector-diagnostic.md` naming each unreachable source and stating which concessions cannot be authorized, which checkpoints cannot be measured, and which contractual leverage cannot be established. Termination rights and notice windows are not inferred from the shape of a standard agreement.

Anti-fabrication guard: this desk fails by producing a plan that is full of motion and empty of consequence. Save plans are easy to write because activity is easy to invent: a workshop, an executive touch, a health check, a roadmap session, a revised success plan. Any account can be given that list, which is exactly why it saves nothing. So each move is tied to the cause it addresses or it does not go in the plan, and a move whose only justification is that it demonstrates attention is labeled as relationship maintenance rather than counted as the save. The second failure is the phantom concession. A discount percentage typed into a draft, a credit mentioned as a possibility, or an extension floated to test the reaction is an offer the moment the customer reads it, and writing an approver's name into the approval field before that person has said yes converts an assumption into an authorization on the page. `approval_state` is `granted` only where a source records the grant, with the person and the date; `pending` and `not_required` are the honest states and neither of them is a soft form of yes. The third failure is optimistic checkpoint language. Checkpoints exist to make a failing save visible early, so a signal is written as a countable observation with its source system named, and a checkpoint that passes because the meeting happened has tested nothing. Where the evidence says the account is leaving, the off-ramp is written plainly rather than softened into a save with an unlikely hypothesis, because a save forecast that nobody believed cost the renewal team the quarter it needed to plan for the loss.

## success_packet fields to update

- `save_plays[]` in full: `covers` referencing the risk or escalation, `play`, `hypothesis`, `concession_requested`, `concession_value`, `approval_state`, `approver` with authority level, `owner`, `checkpoints[]` each with its date and observable signal, and `outcome`
- `approvals[]` with the concession as the action, the named approver, the authority level the org requires for that value, and its state
- `risks[]` updated with `mitigation` set to the play in flight and `state` moved to `mitigating`, with closure still owned by `churn-risk-desk`
- `commitments[]` for anything the play commits the company to, including service commitments, executive involvement, and dated deliverables
- `active_clocks[]` for each checkpoint date and for any commitment the play makes to the customer
- `renewal.forecast_category` flagged for reassessment where the save outcome changes it, with the change made by `renewal-preparation-desk`
- `source_facts` with collection dates, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a concession is authorized before it is visible to the customer, including in a draft shared for feedback. An offer cannot be unoffered; a save bought with an unapproved discount is a revenue decision taken by whoever typed it, and it sets the floor for the next renewal too.
- **Missing approval**: committing an executive, a service level, professional services time, or a contractual remedy binds people and money that belong to someone else.
- **Production or destructive**: the next action would send the save outreach, deliver the offer, change entitlements, extend a term in the billing system, or write the play into the CRM as the record.
- **Security or privacy**: the play would carry another customer's terms, pricing, or situation into this account as comparative evidence, or would expose the customer's internal circumstances beyond the people running the save.
- **Source conflict**: the contract, the concession policy, and the account team's understanding of what has already been offered genuinely disagree, so the company would risk offering something twice or contradicting a position the customer already holds.
- **Release integrity**: a save outcome would be reported as in flight or succeeding to a forecast forum on evidence that cannot carry it, which removes the account from the attention the loss will need.
- **Connector unreachable**: the contract, the concession policy, or the usage evidence exists and cannot be read, so leverage and checkpoints would be built on terms nobody opened.

An unknown executive availability, an unconfirmed comparable outcome, an unpriced professional services option, and an unstated customer preference between two remedies are soft gaps. Record the gap, label the assumption against the move it affects, and continue.

## Downstream handoffs

`value-realization-desk` is next and needs what the play committed to delivering and by when, because a save promised on future value becomes a value claim with a date attached. `renewal-preparation-desk` needs the concession granted with its term consequences, the uplift position it now makes possible or impossible, and the checkpoint results, since a save concluded in the notice window is the renewal position. `churn-risk-desk` needs the checkpoint results as closure evidence or as confirmation the risk is unchanged. `qbr-ebr-desk` needs anything the play committed the company to in front of an executive. `escalation-management-desk` needs any remedy that touches an open escalation so a single account is not given two answers. `retention-portfolio-reporting-desk` needs the outcome and the concession value, because saves bought with discount are a different retention story from saves earned with delivery.

## Quality bar

Good save work is specific about cost and specific about failure. It names what the company is spending, in money and in the time of named people, against an exposure it has computed, so a leader can compare this save with the other three competing for the same executive. Its hypothesis is falsifiable and its checkpoints are observations the customer generates. It contains the sentence nobody wants to write: the date at which this is abandoned, and who says so. It treats the off-ramp as a deliverable rather than a failure, because how a customer leaves determines what they say about the company for years and whether they can be won back. And it is honest in the register: an in-flight save is `in_flight`, a save the customer has not yet agreed to is not `saved`, and a downgrade recorded as a save is the kind of accounting that makes the next quarter's retention number a surprise.
