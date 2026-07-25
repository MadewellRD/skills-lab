---
name: segmentation-coverage-desk
description: define customer segments and tiers with the criteria that place an account in each, assign the touch model across high touch low touch pooled digital and partner led, compute coverage ratios and csm capacity against what the motion actually requires, name unassigned accounts, and write the engagement contract stating what a customer in each tier is entitled to receive. use for book of business design, segmentation review, tiering, capacity and headcount modeling, coverage gaps, and scaled or digital customer success program builds.
---

# Segmentation Coverage Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the coverage artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the segment, account, or capacity figure it affects, and record it in `open_questions`. Never invent an account count, an ARR figure, a headcount, a tier entitlement, or an owner assignment.

## Role

This desk decides who gets what, and it is the only desk in the suite whose output is felt by every account at once. It owns segment definitions written as placement criteria rather than as descriptions: a segment is defined by the rule that puts an account into it, evaluated against fields that exist, so that an account can be placed without a judgment call and two people placing the same account agree. Descriptions of a segment are a communication artifact; criteria are the segment.

It owns motion assignment across high touch, low touch, pooled, digital, and partner led, and the honest statement of which motion each account actually receives rather than which one it is nominally in. It owns coverage ratios computed against what the motion requires, which is the arithmetic most coverage models skip: a high-touch motion with a quarterly business review, a monthly check-in, a success plan review, and an onboarding cycle has a per-account time cost, and a ratio is only a coverage claim when it is stated against that cost rather than against the number of accounts a spreadsheet fits on a page.

It owns capacity math naming where the model is oversubscribed and by how much, accounts with no owner listed by name rather than counted, the escalation path when the assigned owner is unavailable, and the engagement contract per tier: what a customer in that tier is entitled to receive, at what cadence, delivered by whom, on which surface.

## Use when

- A book of business is being designed, rebalanced, or split after a headcount change, an acquisition, or a segment redefinition.
- Coverage ratios are being quoted and nobody has stated what the motion actually requires per account.
- A tier's promised cadence is not being delivered and the question is whether the model or the execution is at fault.
- Accounts are arriving with no assigned owner, or a departure has left a set of accounts uncovered.
- A digital, pooled, or partner-led motion is being introduced and the boundary against one-to-one coverage has to be drawn.
- Retention performance differs sharply by segment and the coverage model is a candidate cause.

## Do not use when

- The subject is which named people sit inside one account rather than which accounts sit in which segment. That is `stakeholder-mapping-desk`.
- The work is designing the plays that run inside a motion. That is `playbook-design-desk`, which consumes segment and motion definitions from here.
- The subject is a single account's risk, health, or renewal. Those are `churn-risk-desk`, `health-scoring-desk`, and `renewal-preparation-desk`.
- The work is reporting retention, health distribution, or coverage performance to a forum. That is `retention-portfolio-reporting-desk`, which reads this model rather than setting it.
- The account has just closed and its own intake is the subject. That is `post-sale-handoff-desk`.

## Required evidence

- The account list with ARR and its as-of date, product mix, lifecycle stage, contract term dates, and growth potential where the org records it.
- Existing segment definitions and tier criteria as currently applied, plus the fields those criteria are evaluated against and their population rate.
- Team headcount and role mix, including CSM, onboarding, technical account management, support, and any pooled or digital function, with tenure and ramp state.
- Current book assignments per owner, including accounts assigned to someone on leave, in notice, or already over capacity.
- The engagement expectations already promised per tier, including cadence, named deliverables, and anything an order form or service schedule made contractual.
- Digital and in-product delivery capability: which surfaces exist, what they can address, and what they have actually reached.
- Partner-led coverage where it exists, with what the partner owns and what remains with the vendor.
- Retention performance by segment: gross and net retention, logo retention, and churn reasons, each with the population behind it.

## Workflow

**Outcome.** Segment definitions with placement criteria; motion assignment per segment with the accounts that receive a different motion in practice named; coverage ratios stated against the per-account cost the motion requires; capacity math naming where the model is oversubscribed and what that costs; the engagement contract per tier; unassigned and effectively unassigned accounts listed by name; and the escalation path when an owner is unavailable.

**Grounding.** Segment placement is computed from account fields that are actually populated, and the population rate travels with the segment: a criterion evaluated against a field that is empty on a third of the book is placing a third of the book by default rather than by rule. Capacity is computed from the engagement contract, not from a target ratio someone is comfortable defending. Delivered cadence is read from activity and meeting records rather than from the tier's promise, because the difference between the two is the finding. Where the CRM's segment field and the criteria disagree on an account, both readings are preserved and the account is listed, since a segment field maintained by hand drifts and the drift is invisible in aggregate.

**Constraints.** A segment is its criteria; a description without criteria is not a segment definition and is recorded as unspecified. Every account resolves to exactly one segment and one motion, and accounts that resolve to none or to several are named rather than absorbed. Coverage ratio is expressed with its numerator and denominator and the motion cost it is measured against; a bare accounts-per-CSM number is recorded as a headcount statistic and not as a coverage claim. Oversubscription is stated in the units that will actually be dropped, which is deliverables and cadence rather than percentage load. Unassigned accounts are named individually with their ARR and their renewal date, because a count of eleven unassigned accounts hides which one renews in six weeks. A tier entitlement is written as what the customer receives and can hold the company to, and anything already contractual is separated from anything that is a program norm.

**Parallel surface.** Independent items fan out safely: per-account segment placement, per-owner book composition, per-tier delivered-cadence measurement, and per-segment retention reads. The aggregate runs once after the fan-out returns, because coverage ratio, capacity math, book balance across owners, and the oversubscription judgment are statements about the whole population and cannot be assembled from parts. The engagement contract is also a single pass, since tiers are defined against each other and a promise added to one tier changes what the tier below it means.

**Acceptance bar.** An account can be placed into a segment by anyone reading the criteria, without asking. Every coverage ratio names its motion cost basis. Capacity math names the specific deliverables that will not be delivered at current headcount, rather than reporting a load percentage. Every unassigned account appears by name with its ARR and renewal date. Every tier entitlement states cadence, deliverable, owning role, and delivery surface, with contractual commitments marked as such. Accounts whose nominal motion and actual motion differ are listed.

## Outputs

A complete run delivers this set:

- `segment-definitions.md`: each segment with its placement criteria, the fields they evaluate and those fields' population rate, account count, ARR, and the accounts that resolve ambiguously.
- `coverage-model.md`: motion per segment, the per-account cost the motion requires with its components, the coverage ratio with numerator and denominator, and the nominal against actual motion per account where they differ.
- `capacity-analysis.md`: headcount against required capacity per motion, oversubscription stated in dropped deliverables and cadence, ramp state and leave factored in, and the point at which the next set of accounts stops receiving the tier's promise.
- `engagement-contract.md`: per tier, what the customer receives, at what cadence, from which role, on which surface, with contractual commitments separated from program norms and with the delivered-against-promised gap measured.
- `unassigned-and-at-risk-coverage.md`: accounts with no owner and accounts whose owner cannot cover them, each named with ARR, renewal date, and lifecycle stage, plus the escalation path when an owner is unavailable.
- `coverage-change-proposal.md`: the proposed model, what moves, which accounts change owner, what each affected customer will notice, and the approval this requires with the named authority level.
- `segmentation-coverage-downstream-handoff.md`: what `stakeholder-mapping-desk` and `playbook-design-desk` inherit, including the motion boundaries a play must respect.

Depth standard: an artifact is complete when a leader could approve or reject the model from it, and an operations owner could implement the assignment without a follow-up round trip. A ratio with no motion cost behind it, or a tier entitlement with no cadence and no owning role, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the account list, the assignment records, or the activity history cannot be reached, the run delivers `coverage-connector-diagnostic.md` naming each unreachable source and the specific ratios, capacity figures, and delivered-cadence measurements that remain unavailable. A coverage ratio is not published against a book nobody counted.

Anti-fabrication guard: this desk fails by publishing arithmetic that is internally consistent and externally untrue. Coverage models are made of round numbers, and round numbers are easy to produce: a ratio of one to forty, a tier promising quarterly reviews, a capacity model that balances. Each of those is a claim about work that either happens or does not, and the customers in the tier are the ones who find out. A tier entitlement goes into the engagement contract only where the delivery record shows it being delivered or where it is explicitly marked as a target the current headcount does not meet; a promised quarterly review that has occurred twice in eight quarters is written with that number next to it. A coverage ratio is published only with the motion cost it was computed against, and an assumed cost is labeled as assumed with what it was derived from. Account counts, ARR totals, and headcount come from the list and the roster that were actually read, with the as-of date, and a segment whose accounts nobody enumerated is reported as uncounted rather than estimated from the shape of the book. Unassigned accounts are named, never totaled, because the total is the number that gets reported and the names are the accounts that go unrenewed. Where the model does not balance, the artifact says which deliverables stop, because a capacity model that resolves to a comfortable number has resolved by dropping something silently, and the thing it dropped is already not happening.

## success_packet fields to update

- `coverage_model` in full: `segments[]` with segment, definition criteria, account count, ARR, motion, and ratio; `capacity` stated against what the motion requires; `unassigned_accounts` named rather than counted; and `escalation_path`
- `account.segment`, `account.tier`, `account.coverage_motion`, and `account.csm_owner` for each account placed, including the accounts placed by default because a criterion field was empty
- `approvals[]` with the coverage change as the action, the named approver, the authority level, and its state
- `risks[]` for accounts with no owner, oversubscribed owners carrying accounts at renewal, and tiers whose contractual entitlement is not being delivered
- `portfolio[]` for coverage ratio and any retention-by-segment figure computed here, each with its computed basis, population, and exclusions
- `source_facts` with collection dates, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a coverage model change reassigns accounts and relationships and sets what customers in each tier will and will not receive. Reassignment is felt by the customer whether or not it is announced, and it changes the retention number, so the model belongs to the leader who owns that number and the team it is drawn against.
- **Production or destructive**: the next action would write assignments into the CRM or success platform, change a customer's tier of record, or remove a coverage entitlement a service schedule made contractual.
- **Security or privacy**: the model would carry compensation data, performance ratings, or individual employee circumstances into an artifact whose audience is wider than the people entitled to see them.
- **Source conflict**: the account list, the assignment records, and the segment fields genuinely disagree on which accounts exist, what they are worth, or who owns them, and resolving it silently would produce a capacity model built on a book that does not exist.
- **Release integrity**: a coverage ratio, capacity figure, or retention-by-segment number would go to a forum making a headcount or investment decision with no computed basis, an undeclared population change, or an unstated exclusion.
- **Connector unreachable**: the account list, the assignment records, or the activity history exists and cannot be read, so a coverage claim would describe a book nobody enumerated.

An unrecorded growth-potential score, a partner's internal capacity, an unmeasured digital reach figure, and an unknown ramp curve for new hires are soft gaps. Record the gap, label the assumption against the figure it affects, and continue.

## Downstream handoffs

`stakeholder-mapping-desk` is next and needs the motion assigned to each account, because the depth of stakeholder coverage a pooled account can sustain is different from a high-touch one and mapping to a standard nobody can staff produces a map that ages immediately. `playbook-design-desk` needs segment and motion definitions with their boundaries, so a play built for high touch does not fire into a pooled book, and needs the delivery surfaces the model actually has. `health-scoring-desk` needs segment definitions, because a model calibrated on the enterprise cohort applied to the digital cohort produces a band distribution that means nothing. `onboarding-time-to-value-desk` needs the motion, since the onboarding path differs by tier. `retention-portfolio-reporting-desk` needs the segment definitions and their population as of a date, so retention by segment is computed on a cohort that can be reproduced.

## Quality bar

Good coverage work is uncomfortable to read. The segment definitions are criteria a person could apply blind, with the population rate of every field they depend on stated, and the accounts that fall between segments are listed rather than nudged. The capacity section names the deliverables that will not happen, in the tier where they will not happen, because a model that balances at the current headcount has almost always balanced by quietly assuming the reviews nobody has time for will occur. The engagement contract is measured against delivery, so a tier promising quarterly reviews reports how many were actually held. Unassigned accounts appear by name with their renewal dates, because that list is a to-do and a count is a footnote. And the proposal is honest about what customers will notice, since the accounts moving between owners include somebody's champion, and a relationship reset is a real cost that belongs in the model rather than in the following quarter's churn reasons.
