---
name: success-planning-desk
description: define desired business outcomes in the customer's own metrics, capture baselines before the change with the method and date behind each, set targets and success criteria stated as what must be observably true, and build the mutual action plan with owners and dates on both sides that a named customer stakeholder has actually agreed. use for success plan creation and refresh, joint success planning, outcome and baseline definition, mutual action plans, and qbr preparation that needs a measurable outcome underneath it.
---

# Success Planning Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the success plan artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the outcome, baseline, or milestone it affects, and record it in `open_questions`. Never invent a customer metric, a baseline value, a target, a customer-side owner, or an agreement that has not been given.

## Role

This desk owns the document both sides measure the relationship against. It writes desired business outcomes in the customer's language, against the metric the customer already reports on internally, because an outcome expressed in the vendor's vocabulary cannot be checked by the customer's finance team and will not be recognized by the executive who approves the invoice. Time saved, tickets deflected, cycle time reduced, revenue per rep, days to close, and cost per unit are the customer's units; product adoption and platform usage are not outcomes, they are the mechanism.

It owns baselines, which is the load-bearing part of this desk and the part most often skipped. A baseline is the value of the customer's metric before the change that is supposed to move it, captured with the method that produced it and the date it was taken. It owns targets with dates and named owners on both sides, and success criteria written as what has to be observably true rather than as an aspiration, so the outcome can be judged rather than argued.

It owns the mutual action plan with an owner and a due date on every item including the customer-side ones, the named customer stakeholder who agreed the plan and when, the review cadence, and, importantly, the outcomes this product cannot move, stated as out of scope rather than quietly dropped so they resurface as a disappointment at the renewal.

## Use when

- A new account is being planned after handoff, or an existing account has no plan that anyone at the customer has agreed to.
- A business review is being prepared and the value story has no measured baseline underneath it.
- A rollout, expansion, or new module is about to begin and the pre-change measurement has not been taken.
- The customer's priorities have changed, a sponsor has changed, or the original business case no longer describes what they want.
- The plan exists, has not been reviewed in a period, and its milestones have quietly slipped.
- A renewal is approaching and the question is what the customer got against what they said they wanted.

## Do not use when

- The subject is the implementation sequence, dependencies, and go-live rather than the outcomes. That is `onboarding-time-to-value-desk`, which delivers against this plan.
- The change has already happened and the question is what moved. That is `value-realization-desk`, which cannot work without the baselines set here.
- The work is which named people can agree the plan. That is `stakeholder-mapping-desk`.
- The subject is why a capability is not being used. That is `adoption-enablement-desk`.
- The plan is being presented to an executive audience with a narrative. That is `qbr-ebr-desk`.

## Required evidence

- The customer's stated business outcomes in their own words, with the metric names they use internally, from discovery, the business case, or a stakeholder statement with a date.
- The business case the deal was bought against, carried from handoff, including the numbers the customer used to justify the purchase.
- Current-state measurements available before any rollout: the customer's own reporting, their system exports, or a measurement the product can take at day zero.
- Executive and champion priorities with dates, and any change in the customer's own business that moved them.
- The entitlements and product capability that could plausibly move each metric, so an outcome is not adopted that nothing purchased can affect.
- The customer's internal milestones, constraints, budget cycle, and change-management capacity.
- Prior success plans with what was agreed, what was delivered, and what was quietly abandoned.

## Workflow

**Outcome.** Desired business outcomes in the customer's language and metrics; a baseline per outcome with its value, method, and date, flagged for whether it was captured before the change; targets with dates and owners on both sides; success criteria stated observably; the mutual action plan with owners and dates including the customer-side items; the named stakeholder who agreed the plan and the date; the review cadence; and outcomes stated as out of scope with the reason.

**Grounding.** Outcomes come from statements by named customer stakeholders with dates, not from the product's value proposition and not from what accounts in this segment usually want. The metric is the one the customer already reports on, named as they name it, because a metric invented for the plan has no owner inside their organization and no history to compare against. Baselines come from the customer's own system or from a measurement taken at a stated point, with the method written down; a figure supplied by a value calculator, a benchmark, or an industry average is an estimate and carries that label permanently. Where the customer's stated priority and the business case in the deal record disagree, both readings are preserved and the customer's current statement is the one the plan is built on, with the difference recorded.

**Constraints.** Every outcome carries a metric, a baseline, a target, a date, and an owner on each side, or it is recorded as incomplete with the missing element named. Success criteria are observable: a criterion that cannot be checked from a system, a report, or a named person's confirmation is rewritten or removed. Customer-side actions carry customer-side owners by name, since a mutual action plan where every owner is internal is a delivery plan the customer has not committed to. Outcomes the purchased capability cannot move are stated as out of scope with the reason, rather than left in to be aspirational. Targets are set against the customer's own cycle, not against the vendor's fiscal calendar. The plan is agreed with a named person and a date, and until it is, `agreed_with` reads `not_agreed` regardless of how confident the account team is that the customer is on board.

**Mandated order: the baseline is captured before the change it will measure.** This order is externally mandated by the arithmetic of measurement rather than by process preference, and it does not compress: the pre-change state cannot be recovered once the rollout is live, so a baseline assembled afterward from memory, from a benchmark, or from a reconstruction is an estimate that the customer's own finance team will discount at exactly the moment the value claim matters.

1. Name the metric as the customer names it and confirm which of their systems is the system of record for it.
2. Capture the baseline value from that system, with the method, the population, the window, and the date, before the rollout, configuration change, or enablement that is meant to move it begins.
3. Have the named customer stakeholder confirm the baseline figure and the method, because a baseline they did not see is one they can reject later when the delta is inconvenient.
4. Record the target and the measurement date against that same method, so the later comparison is like for like.
5. Only then begin the change, and record its start date as the boundary the comparison is drawn around.

Where a rollout has already started, the baseline is recorded as reconstructed with its method and its limits stated, rather than presented as a measurement.

**Parallel surface.** Independent items fan out safely: individual outcomes being defined, individual baselines being captured, individual milestone owners being confirmed, and accounts in a book having their plans refreshed at once. The plan itself is a single pass after the fan-out returns, because outcomes compete for the same customer-side capacity and the same milestones, and a plan assembled from independently written outcomes over-commits the two or three people at the customer who own all of them. Agreement is also a single act, taken on the whole plan.

**Acceptance bar.** Every outcome is stated in the customer's metric with a baseline carrying its value, method, and date, and a flag for whether it predates the change. Every target has a date and an owner on both sides. Every success criterion is checkable. Every mutual action plan item has a named owner, and customer-side items have customer-side names. The plan records who agreed it and when, or records `not_agreed`. Outcomes the product cannot move appear as out of scope rather than being absent.

## Outputs

A complete run delivers this set:

- `success-plan.md`: outcomes in the customer's language with metric, baseline, target, dates, and owners on both sides, plus the out-of-scope outcomes with their reasons.
- `baseline-register.md`: per outcome the baseline value, the system it came from, the method, the population, the window, the date, and whether it was captured before the change, with reconstructed baselines labeled and their limits stated.
- `success-criteria.md`: what has to be observably true for each outcome to count as met, with the source that would show it and the person who would confirm it.
- `mutual-action-plan.md`: milestones with owner, due date, state, dependency, and blocker, with customer-side items named and their owners identified by person rather than by team.
- `plan-agreement-record.md`: who agreed, when, on what version, what they changed during agreement, and the review cadence with the next review date.
- `success-planning-downstream-handoff.md`: what `onboarding-time-to-value-desk` and `value-realization-desk` inherit, particularly the first outcome, its baseline, and the measurement method the later comparison has to match.

Depth standard: an artifact is complete when the customer could sign it and the CSM could run the next twelve months from it without a follow-up round trip. An outcome with no baseline, a milestone with no owner, or a criterion nobody could check is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the customer's measurement systems, their stated outcomes, or the business case cannot be reached, the run delivers `success-plan-connector-diagnostic.md` naming each unreachable source, the outcomes that cannot be baselined, and the value claims that will therefore be unavailable later. A baseline is not supplied from a benchmark to complete the table.

Anti-fabrication guard: the characteristic failure here is a plan that reads beautifully and belongs to nobody. Success plan templates invite completion, and a blank baseline cell is uncomfortable, so numbers arrive from somewhere: an industry benchmark, the value calculator used in the sales cycle, the customer's aspiration restated as their current state, or a round figure that makes the target arithmetic work. Every one of those becomes the denominator of an ROI claim presented to the person who approves the invoice, next to their own reporting, and a baseline they can disprove in one query costs the credibility of the entire review. A baseline appears only where a measurement was taken from a named system with a stated method, or it is written as `not_measured` with what would have to be measured. An outcome appears only where a named customer stakeholder stated it, with the date; outcomes inferred from the product's value proposition are labeled as proposed and are not counted as the customer's. `agreed_with` carries a person's name and a date or reads `not_agreed`, and enthusiasm on a call is not agreement to a document nobody has seen. Customer-side owners are named people the customer nominated, never a team name standing in for a commitment nobody made. A plan with two measured outcomes and three marked as unbaselined is a working plan; a complete plan with invented baselines is a value claim already scheduled to fail.

## success_packet fields to update

- `success_plan.desired_outcomes[]` with `outcome`, `metric`, `baseline` including `method`, `as_of`, and `captured_before_change`, `target` with value and date, `owner_customer`, `owner_internal`, and `source`
- `success_plan.success_criteria[]` stated observably with the evidence that would show each met
- `success_plan.mutual_action_plan[]` with `milestone`, named `owner`, `due`, `state`, and `blocker`
- `success_plan.agreed_with`, `agreed_on`, and `last_reviewed`
- `stakeholders[]` where an outcome owner or plan approver was newly identified or confirmed
- `active_clocks[]` for any milestone with a customer-committed date and for the next plan review
- `risks[]` where an outcome has no baseline and a value claim will later be required, or where the plan is unagreed
- `source_facts` with collection dates, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a success plan is a joint commitment carrying dates and customer-side obligations, and it becomes the document both sides measure the relationship against. It is agreed with the named customer owner rather than written for them, and a plan nobody at the customer accepted will still be quoted back as a promise the company made.
- **Release integrity**: a target, a baseline, or a success criterion would be committed to a customer-facing plan without a measurement or a stated method behind it, which sets up a value claim with nothing underneath it.
- **Source conflict**: the customer's stated priorities, the business case in the deal record, and the executive's stated objectives genuinely disagree, and building the plan on whichever is most achievable hides a difference the renewal will surface.
- **Security or privacy**: capturing a baseline would require the customer's internal financial, personal, or confidential operating data to be moved into an artifact or a system that is not entitled to hold it.
- **Production or destructive**: the next action would write the plan into the success platform as the record of agreement, or begin the rollout that closes the window for capturing a baseline.
- **Connector unreachable**: the customer's measurement system, the business case, or the stakeholder statements needed to establish an outcome exist and cannot be read.

An unconfirmed review cadence, an unnamed secondary owner, an unquantified target for a secondary outcome, and an undocumented customer constraint are soft gaps. Record the gap, label the assumption against the outcome it affects, and continue.

## Downstream handoffs

`onboarding-time-to-value-desk` is next and needs the first outcome, its baseline, and the definition of what would count as first value against it, plus the customer-side owners who will carry milestones. `value-realization-desk` needs the baseline register with the exact method behind each figure, because the later measurement has to be taken the same way or the delta is not comparable. `adoption-enablement-desk` needs which capabilities serve which outcome, so adoption work is aimed at the capability the outcome depends on. `qbr-ebr-desk` needs the plan and its attainment, including the outcomes that did not move. `renewal-preparation-desk` needs the plan against actual attainment, since the renewal conversation is the customer's own assessment of it. `health-scoring-desk` needs outcome attainment where the model uses it as a component.

## Quality bar

Good success planning is written in the customer's vocabulary and could be read aloud in their operating review without translation. The metrics are ones their systems already produce, the baselines carry methods a skeptical analyst could reproduce, and the dates line up with their fiscal and operational cycle rather than the vendor's quarter. The mutual action plan has customer names on customer items, which is the difference between a joint plan and a delivery plan with a friendly title. It is explicit about what the product will not do, because the outcome nobody scoped out is the one the customer remembers wanting. And it records agreement as an event with a person and a date, since the plan's whole function is to be the thing both sides point at later, and a document only one side ever saw cannot perform that function.
