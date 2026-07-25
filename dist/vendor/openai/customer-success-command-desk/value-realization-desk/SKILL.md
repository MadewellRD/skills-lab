---
name: value-realization-desk
description: measure delivered customer value per outcome with the baseline and current value stated alongside the measurement method behind each, the attribution basis crediting the change to this product, monetization only where the customer accepts the conversion, and the named customer stakeholder who validated the figure. use for value assessment, roi and business case validation, outcome attainment, benefit quantification, executive value stories, and proving what the customer actually gained.
---

# Value Realization Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the value artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the outcome, the figure, or the attribution it affects, and record it in `open_questions`. Never invent a baseline, a current value, a measurement method, a conversion rate, a benchmark applied as if it were this customer's number, or a validation the customer did not give.

## Role

This desk answers the only question the person who approves the invoice actually asks: what did we get. It owns the value position per desired outcome, and a value position is four things held together. The baseline, with the method that produced it and the date it was taken. The current value, with its own method and date. The delta stated in the customer's unit before any money is attached to it. And the basis for attributing that delta to this product rather than to everything else that happened in the same period.

The methods matter as much as the numbers, and this is where most value work quietly fails. A baseline pulled from the customer's reporting and a current value pulled from product telemetry are not comparable, and presenting their difference as a result invites the customer's analyst to demonstrate that in one query. The desk states both methods, and where they differ it says so rather than averaging the discomfort away.

It owns monetization, and monetization is the customer's arithmetic, not the company's. Hours saved become money at the rate the customer's finance team uses, applied to headcount the customer agrees was actually redeployed, converted by an assumption the customer has seen and accepted. Where they have not accepted it, the delta stays in the customer's own unit, which is frequently more persuasive anyway: a claims team closing cases in four days instead of eleven does not need a dollar sign to be a result.

It owns the attribution basis, which is the part an executive audience tests first. Something else always changed too: a new process, a reorganization, a headcount change, a market shift, another vendor's tool arriving in the same quarter. The desk states what supports crediting the change here, whether that is a cohort comparison, a phased rollout with a control group, a timing correspondence tight enough to be evidence, or a stakeholder's own attribution on the record. And it owns the named customer stakeholder who validated each figure, with the date, because a number the customer has not seen is a hypothesis and one they have seen and disputed is a disagreement to record rather than a result to present.

## Mandated order for the baseline, and why it is ordered

The measurement of a business outcome is captured before the rollout meant to move it. The order is mandated because the pre-state is not recoverable once the change is live: a baseline reconstructed afterward from memory, from a vendor calculator, or from an industry benchmark is an estimate, is labeled as one here, and does not carry a business review in front of a finance function that can check it. Where the baseline was genuinely never taken, this desk says so and works with the honest alternatives, such as a comparable unrolled-out business unit or a period-over-period read the customer's own systems can produce, rather than manufacturing a number that makes the delta look clean.

## Use when

- A business review, renewal, or expansion conversation needs a defensible statement of what the customer has gained.
- The success plan has outcomes with baselines and the question is what has actually moved.
- A customer disputes the value they are getting, or their finance function has asked for a justification of the spend.
- A save play or renewal position rests on value that has never been measured or validated.
- An executive sponsor has changed and the value case has to be re-established for someone who did not buy it.
- A previously stated ROI figure needs re-examination before it is repeated.

## Do not use when

- The outcomes, metrics, baselines, and mutual plan are being set for the first time. That is `success-planning-desk`, which captures the baseline this desk measures against.
- The subject is what the product is being used for rather than what the usage produced. That is `usage-analysis-desk`; adoption is an input to value, not a substitute for it.
- The work is assembling and presenting the review itself. That is `qbr-ebr-desk`, which consumes validated figures from here.
- The question is why an outcome has not moved because the capability is unused. That is `adoption-enablement-desk`.
- The value being quantified is for a deal not yet closed. That is a sales business case; this desk measures delivered value on a live account.

## Required evidence

- The success plan outcomes in the customer's language, each with the metric they already report on, its baseline value, the method that produced it, and its as-of date.
- Current measurements from product telemetry, the customer's own systems, or a figure a named stakeholder has stated, each with its method and window.
- The customer's own valuation inputs: their cost assumptions, their loaded rates, their revenue or margin figures, and the conversion they use internally for this kind of benefit.
- Adoption and usage evidence linking the product to the change, with the instrumentation coverage that bounds it.
- What else changed in the customer's environment during the measurement period: processes, headcount, reorganizations, other tooling, seasonality, and market conditions.
- Prior value claims made to this account, with who made them, to whom, and whether they were accepted.
- The named stakeholder on the customer side who can validate a figure, and any figure their team has already produced independently.

## Workflow

**Outcome.** A value position per outcome, each stating baseline and current with both methods and dates, the delta in the customer's unit, monetization only where the customer accepts the conversion, the attribution basis, the named validator with the date, the confidence and what limits it, and an explicit statement for outcomes that did not move naming what got in the way.

**Grounding.** Baselines come from the success plan where one was captured before the change; where it was not, the reconstruction method is named and the figure is labeled an estimate throughout, including in anything downstream. Current values come from the highest source layer available and carry the coverage of that layer. The customer's own figure outranks the company's read of the same metric, and where the two differ both readings are recorded against the outcome, because the customer will use theirs in the room regardless. Monetization inputs come from the customer, quoted with who supplied them; a fully loaded hourly rate lifted from an industry report is not this customer's rate.

**Constraints.** The delta is stated in the customer's unit first, and money is added only as a second layer with the conversion visible. Any benchmark, multiplier, or model default is labeled as such and never presented as measured. Attribution is stated as a basis with its strength, not asserted; where the honest answer is that this product is one of several contributors, the claim is scoped to a contribution rather than inflated to a cause. A figure the customer has not seen is `not_validated`, and one they have seen and disputed is recorded with their objection intact. Confidence travels with every number, and the limits are specific: the instrumentation gap, the missing baseline, the unrepresentative period, the single business unit standing in for the enterprise. Outcomes that did not move are reported at the same level of detail as the ones that did.

**Parallel surface.** Independent items fan out safely: separate outcomes being measured, individual metrics being pulled and method-checked, individual business units or regions being measured against the same outcome, and prior claims being traced to their source. The aggregate is a single pass after the fan-out returns, because the total value position for the account, any blended ROI or payback figure, and the ranking of which outcomes carry the review are statements about the whole set. Validation with the customer is also a single pass, since a stakeholder validates a coherent position rather than a queue of separate numbers.

**Acceptance bar.** Every figure names its metric, its baseline with method and date, its current value with method and date, and its delta in the customer's unit. Every monetized figure shows the conversion and names who supplied it. Every claim carries an attribution basis with its strength stated. Every figure carries a validation state with the named stakeholder and date where validated. Reconstructed baselines are labeled as estimates everywhere they appear. Outcomes that did not move are present with what got in the way. Nothing is presented as measured that was modelled.

## Outputs

A complete run delivers this set:

- `value-position.md`: per outcome, the metric, baseline with method and date, current with method and date, delta in the customer's unit, monetization where accepted, confidence, and validation state.
- `measurement-methods.md`: for each figure, the source system, the query or report behind it, the population, the window, and the known limits, written so the customer's analyst can reproduce it.
- `attribution-analysis.md`: what supports crediting each change to this product, the competing explanations considered, what would strengthen the basis, and the claims deliberately scoped to a contribution rather than a cause.
- `monetization-model.md`: the conversion for each monetized outcome, the inputs with who supplied them, the arithmetic, and the sensitivity of the result to the one or two assumptions that carry it.
- `unrealized-outcomes.md`: outcomes that have not moved, each with what got in the way, whether the cause is adoption, configuration, a product gap, or a changed customer priority, and what would move it.
- `validation-record.md`: which figures a named customer stakeholder has agreed, on what date, in what forum, which are pending, and which they disputed with their objection recorded in their own terms.
- `value-realization-downstream-handoff.md`: what `qbr-ebr-desk`, `expansion-whitespace-desk`, `renewal-preparation-desk`, and `advocacy-reference-desk` inherit, with validation state and confidence limits attached to every figure rather than stripped.

Depth standard: an artifact is complete when the customer's own finance analyst could follow the arithmetic from source to claim and either agree with it or name the specific step they dispute. A figure with no method, a monetized benefit with no stated conversion, or an ROI percentage with no denominator is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when telemetry, the customer's own reporting, or the success plan baselines cannot be reached, the run delivers `value-connector-diagnostic.md` naming each unreachable source and stating exactly which outcomes cannot be measured and which claims therefore cannot be made. Where no pre-change baseline exists at all, the run delivers `baseline-reconstruction-options.md` setting out the honest alternatives with their weaknesses, rather than a value position resting on a number nobody took.

Anti-fabrication guard: the specific hazard here is the value calculator. Benchmark multipliers, industry-average savings percentages, hours-saved-times-a-loaded-rate, and payback periods derived from a model produce numbers that are internally consistent, professionally formatted, and about nobody. They are also the numbers most likely to be presented to the exact person who has the customer's real figures on the next screen. So every input is traced to the customer's own measurement or their own stated assumption, with the person who supplied it named; a modelled figure is labeled modelled in the artifact, in the packet, and in anything that leaves this desk, and it never loses that label by being copied into a deck. Percentage improvements are shown with both absolute numbers, since a fifty percent improvement over a base of six is a base of six. A baseline that was reconstructed after the change carries that word every time it appears. Validation is a recorded act by a named person on a date, so a stakeholder who nodded in a meeting is `not_validated`, and a figure produced by the account team and never shown to the customer is a hypothesis with a number in it. Where the customer's own systems produce a different figure from the company's, both go on the page, because the version presented as settled will be corrected in the room by the person the review was for, and every other claim in the same document loses its credibility in that moment.

## success_packet fields to update

- `value_realization[]` in full: `outcome_ref`, `baseline` with `value`, `method`, `as_of`, and `captured_before_change`, `current` with `value`, `method`, and `as_of`, `delta`, `monetized` with the accepted conversion or `not_monetized`, `attribution_basis`, `customer_validated_by`, `validated_on`, and `confidence` with what limits it
- `success_plan.desired_outcomes[]` updated with attainment against target, and outcomes recorded as not moved with the cause
- `risks[]` for outcomes categorized as value not realized, each with `arr_exposed` and `first_detected`
- `commitments[]` where a value figure was previously stated to the customer and is not supported by this measurement
- `stakeholders[]` updated where a validator's role or disposition was established during validation
- `assumptions[]` for every modelled input, reconstructed baseline, and scoped attribution, each naming the figure it affects
- `source_facts` with collection dates, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a value or ROI figure would go to a customer without a baseline captured before the change, without an attribution basis, or without customer validation. This number is presented to the person who approves the invoice, next to their own reporting, and a figure their finance team can disprove in one query costs the credibility of every other claim in the same review.
- **Source conflict**: the company's measurement and the customer's own figure for the same metric genuinely disagree, and presenting either alone would be contradicted by the other in the room.
- **Security or privacy**: the analysis would carry the customer's confidential financial data, headcount detail, or internal cost structure into an artifact whose audience is wider than they consented to, or would use their figures in another customer's material.
- **Missing approval**: a value claim is about to be published externally, used in a case study, or quoted in marketing material. That is an advocacy act with a customer approval requirement.
- **Production or destructive**: the next action would write value figures into the CRM or success platform as the record, or into a customer-facing system.
- **Connector unreachable**: telemetry, the data warehouse, or the customer's supplied reporting exists and cannot be read, so a delta would be asserted about a change nobody measured.

A missing loaded rate, an unconfirmed headcount redeployment, an unstated seasonality effect, and a validator who has not yet responded are soft gaps. Record the gap, label the assumption against the figure it affects, and continue with the delta in the customer's unit.

## Downstream handoffs

`qbr-ebr-desk` is next and needs each figure with its validation state and confidence limits intact, plus the unrealized outcomes, because a review that presents only what worked is the review that gets tested first. `expansion-whitespace-desk` needs to know whether the first outcome has actually been delivered, since an upsell into an undelivered commitment damages the renewal it was meant to grow. `renewal-preparation-desk` needs the validated value position, since that is what the renewal conversation is worth arguing from and what an uplift has to be justified against. `advocacy-reference-desk` needs figures the customer has validated and cleared for external use, which is a narrower set than the validated set. `churn-risk-desk` needs unrealized outcomes as risk evidence with dates. `voice-of-customer-desk` needs the product gaps that blocked outcomes, with the accounts and ARR behind each.

## Quality bar

Good value work survives contact with the customer's analyst. It shows its arithmetic, names its sources, and states its limits before anyone asks, which is what makes the numbers it does claim believable. It keeps the delta in the customer's unit and treats money as a second layer built on assumptions the customer supplied, so the conversation is about the outcome rather than about the multiplier. It is willing to report that two of five outcomes moved, one moved for reasons this product cannot claim, and two did not move at all, because that document builds more trust than a five-for-five story and it is the one the sponsor can defend internally without staking their own credibility. It names the person who agreed each figure and the date they agreed it. And it never lets a modelled number lose its label on the way into a slide, because the moment a benchmark is presented as a measurement, the company has told the customer something it cannot support about the customer's own business.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
