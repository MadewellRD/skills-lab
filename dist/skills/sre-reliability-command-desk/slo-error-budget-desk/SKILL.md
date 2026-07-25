---
name: slo-error-budget-desk
description: set service level objectives with windows, define and compute the error budget and its balance, account for burn rate over multiple windows, write an error budget policy with consequences that bind someone, and separate objectives agreed with the owner from proposed and aspirational ones. use for slo target setting, error budget accounting, burn rate analysis, budget policy design, and freeze adjudication.
---

# SLO Error Budget Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the objective and budget artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent attainment figures, budget balances, burn rates, contractual commitments, or an owner's agreement to a target.

## Role

Own how much unreliability the business has agreed to spend, over what window, and what actually changes when it is spent. An objective here is a target on a specified indicator over a stated window; the error budget is the arithmetic complement of that target expressed in the same events the indicator counts; the budget policy is what makes the two consequential.

Three states must stay separated and never collapse into one another: an objective that is computed and agreed, an objective that is computed but only proposed, and an objective that exists in a document with nothing computing it. All three are written as a percentage and look identical in a review deck. Only the first can be missed, defended, or enforced.

## Use when

- Indicators exist with a known measurement state and the question is what target they should hold and over what window.
- An error budget needs defining, computing, or reconciling against what teams believe the balance is.
- Burn rate accounting is needed, whether for a current burn, a retrospective analysis of a period, or the thresholds that alerting will be built on.
- An error budget policy needs writing, or the existing one has no consequence, no named owner, and has never changed a decision.
- The organization is deciding whether a freeze applies, or whether budget exhaustion should stop feature work.
- Existing objectives need auditing for the gap between what is published, what is agreed, and what is computed.

## Do not use when

- The indicator, its event definitions, or its measurement point are not settled: that is `sli-specification-desk`, whose measurement state gates what this desk may call an objective.
- The question is which alert fires at which burn rate and how it routes: that is `alerting-quality-desk`. This desk sets the budget arithmetic; that desk builds the paging rules on it.
- The question is why the objective is missed, which dependency causes it, or what the composed ceiling is: that is `dependency-failure-analysis-desk`.
- The question is whether a rollout may proceed given the current budget: that is `change-safety-desk`, which consumes the budget state as a promotion gate.
- The question is the periodic adjudication across many services and the reliability roadmap: that is `reliability-review-desk`.

## Required evidence

- The indicator set with measurement state, implementation query, and window from the upstream stage.
- Historical attainment computed over the candidate window, with the query and date range that produced it, where it exists at all.
- Service tier and journey criticality, which bound what target is defensible.
- Contractual and regulatory commitments: service agreements with customers, uptime credits, regulatory availability or data-freshness obligations, and internal commitments made to dependent teams.
- The composed availability ceiling implied by the journey's dependencies, where the dependency stage has produced one.
- Existing objective documents, the dates they were agreed, and whoever is recorded as agreeing.
- Any existing budget policy, and evidence of whether it has ever been invoked.

## Workflow

**Outcome.** An objective per indicator with its window and agreement state, an error budget defined in the indicator's own events with its current balance and the window that balance was computed over, burn rate accounting across a fast and a slow window, a budget policy whose consequences name a bound party and an override path, and an explicit separation of agreed objectives from proposed and aspirational ones.

**Grounding.** Attainment comes from the indicator's implementation query over a named date range; commitments come from the agreement or regulation itself; agreement state comes from a person or a record, never from the fact that a number appears in a document. Where a published objective and a computed attainment disagree with a commitment, all three are recorded with attribution and the conflict is preserved per `references/suite-workflow-contract.md`.

**Constraints.** Every objective states its window explicitly and the window type is a deliberate choice: a rolling window measures a continuously moving user experience and never grants an amnesty, while a calendar window aligns to reporting and hands back a full budget on a date, which is why the last week of a calendar month is where risky changes accumulate. Say which was chosen and why.

Set the target against what the journey's users need and what the tier obligates, not against the number the last quarter happened to produce. Fitting the target to observed performance produces an objective that can never be missed and therefore never informs a decision. An objective the service currently misses is a valid and useful output. An objective above the composed ceiling its dependencies allow is a promise the architecture cannot keep, and it is recorded as such rather than quietly rounded down.

Define the budget in the same events the indicator counts, so it is expressible as failed requests, delayed records, or unavailable minutes rather than only as a percentage; a budget stated in events is one an engineer can reason about during an incident. Burn rate is the multiple of the budget being consumed relative to even consumption: a burn rate of one exhausts the budget exactly at the end of the window, and a burn rate of n exhausts it in one nth of the window. Account for it over both a short window that catches an acute event and a long window that catches a slow drain, because a burn visible only at one time scale is the reason a service can pass every daily check and end the month exhausted.

The budget policy is where objectives acquire teeth. It names what changes at each threshold, who is bound by that change, who may override it, and what evidence closes the override. A policy stating that the team will "prioritize reliability" binds nobody. Objectives on unmeasured indicators are labeled aspirational and are not permitted to carry a budget balance, since a balance derived from an uncomputed attainment is a number the organization will act on.

**Parallel surface.** Indicators, journeys, candidate objectives, attainment computations, and commitment lookups are independent units and are parallel-safe; per-objective drafting and per-window burn computation fan out.

The aggregate work runs once after the fan-out returns: rolling per-service budgets up to the journey the user actually experiences, reconciling objectives against the composed dependency ceiling, adjudicating the single budget policy that governs all objectives together, ranking objectives by the gap between target and attainment, and deciding whether the portfolio state triggers a freeze.

**Acceptance bar.** Every objective states an indicator, a target, a window, and an agreement state. Every attainment and budget balance names the query and the date range that produced it, or is written as unmeasured. Burn is accounted over at least a short and a long window. The policy names a bound party and an override approver. No objective is stated as a bare percentage.

## Outputs

A complete run delivers this artifact set:

- `slo-definitions.md`: per indicator, the target, the window and its type, the rationale tying the target to tier and user need, the agreement state with who agreed and when, and the measurement state inherited from the indicator.
- `error-budget-accounting.md`: the budget expressed in the indicator's own events and as a percentage, the current balance with the query and date range behind it, consumption attributed to incidents and changes where the record supports it, and the unattributed remainder stated as unattributed.
- `burn-rate-analysis.md`: burn computed over a short and a long window with the arithmetic shown, the thresholds that alerting will use with the fraction of budget each represents, and the burn history over the window where data exists.
- `error-budget-policy.md`: thresholds, the consequence at each one, the party bound by it, the override path with its named approver and expiry, the reset boundary, and whether the policy has ever actually been invoked.
- `slo-downstream-handoff.md`: the budget state, thresholds, and policy consequences that `alerting-quality-desk` and `change-safety-desk` inherit, with the aspirational objectives flagged as unusable for gating.

Depth standard per artifact: an objective entry a service owner could dispute on the merits, because the rationale is present and the tier link is explicit. A budget entry expressed in events, so "the budget is 43 minutes of full unavailability, or 1.2 million failed requests at current volume" replaces a bare percentage. A policy entry with a named role, not "engineering leadership". A burn entry showing the computation, since a burn multiple with no arithmetic behind it cannot be checked against a different window.

In `diagnostic` mode, when the metrics backend or the recording rules behind an indicator exist and cannot be read, the run delivers `slo-connector-diagnostic.md` reporting reachability, the queries attempted, and the access needed. Objectives may be proposed in that mode; no balance, attainment, or burn figure is stated.

The specific danger in this desk is the budget balance, because it is the one number in the suite that people act on immediately. A stated remaining balance changes whether a team ships on Friday, whether a migration is approved, whether a freeze lifts. It is also trivially derivable from an attainment figure that was never computed: pick a plausible attainment, subtract, and the arithmetic is flawless while the input is invented. So a balance appears only when the attainment behind it names its query and date range, an objective with no computing rule carries no balance at all and is labeled aspirational, an attainment is never quoted without the window it was computed over, and consumption is attributed to an incident only when the incident record supports the attribution, with the remainder left explicitly unattributed. "We cannot compute this budget until the indicator is instrumented" is a finding a team can act on this week; a confident balance built on an imagined attainment quietly authorizes the release that spends what is left.

## reliability_packet fields to update

- `slos[]`: `sli_id`, `objective`, `window`, `current_attainment`, `error_budget_remaining`, `burn_rate`, `budget_policy`, `agreement_state`.
- `operating_posture` set to `budget_exhausted` or `freeze` where the accounting establishes it.
- `readiness_gates[]` for the objective and budget gate, with the evidence behind its state.
- `reliability_risks[]` for objectives above the composed dependency ceiling and for tier 0 journeys carrying only aspirational objectives.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: setting, lowering, or retiring an objective, activating a budget consequence that stops feature work, or declaring a freeze, without the service owner or accountable leader who must agree.
- Production or destructive: the next action would change live recording rules, budget dashboards, burn-rate alerting, or a release gate that blocks deploys.
- Security or privacy: a commitment document that would ground the objective carries customer-identifying or contractual terms that do not belong in the artifact.
- Source conflict: the customer agreement, the internal objective document, and the computed attainment disagree on the commitment or the achieved level, and resolving it silently would misstate what the business owes.
- Release integrity: an objective would be recorded as met, agreed, or measured, or a budget declared healthy, without a computation or an agreement record behind it.
- Connector unreachable: the metrics backend, recording rules, or the agreement repository exists and cannot be read, so attainment or commitment cannot be established.

Absent history, short retention, an unmeasured indicator, and an unrecorded agreement date are soft gaps: state the objective as proposed or aspirational, name the missing input, and record the assumption where it was used. An objective is never promoted to agreed, and a balance never stated, to let a downstream gate close.

## Downstream handoffs

`dependency-failure-analysis-desk` needs the objective per journey to compare against the composed availability the dependency graph allows. `alerting-quality-desk` needs the budget definition and burn thresholds, since burn-rate paging is computed from them directly. `change-safety-desk` needs the current budget state and the policy consequences as its promotion and freeze gates. `production-readiness-review-desk` needs the agreement state per objective, because an aspirational objective cannot pass an objective gate. `reliability-review-desk` needs the accounting and policy invocation history. Cross-suite: customer-facing commitment language and credit terms go to the Legal Contracts suite, and contractual reporting to the GRC suite.

## Quality bar

Objectives that describe the user experience closely enough that missing one produces a complaint and meeting one produces silence. Windows chosen for a reason that is written down. A budget expressed in events an on-call engineer can count during an incident. A policy someone has actually been bound by, or an honest note that it has never been invoked. Aspirational objectives labeled without defensiveness, because that label is what makes the agreed ones worth defending.
