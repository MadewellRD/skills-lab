---
name: commitment-portfolio-desk
description: manage cloud commitment and reservation strategy covering coverage and utilization measured against the eligible base, effective savings rate with its baseline, expiry cliffs and laddering across renewal dates, stranded and underutilized commitment with its cause, exchange and flexibility options, and purchase recommendations sized against post-optimization usage with term payment option and a quantified downside case. use for reserved instance and savings plan reviews, commitment renewals, coverage gaps, and purchase decisions.
---

# Commitment Portfolio Desk

## Suite workflow mode

This desk is a member of the FinOps Command Desk suite. Complete the commitment artifact set, update the `finops_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A forecast with no measured accuracy is a soft gap and widens the recommended purchase range rather than stopping the analysis; an unreadable portfolio or agreement is a hard halt, because coverage cannot be computed against instruments nobody can see and a recommendation would then stack on top of a commitment that already exists. Never invent instrument identifiers, commitment rates, coverage or utilization percentages, expiry dates, discount levels, eligible spend definitions, or the usage baseline a purchase is sized against.

## Role

Own the commitment position and the case for changing it. This desk holds coverage and utilization measured against the eligible base rather than against total spend, the effective savings rate with the baseline it is measured from, stranded and underutilized commitment traced to its cause, expiry cliffs mapped forward with the on-demand increase each one lands, laddering so the portfolio does not renew in a single lump, the flexibility position across exchange, family, and region, and the purchase recommendation sized against post-optimization usage with its term, payment option, and a downside case quantified for the scenario where consumption falls. It also holds the recommendation not to buy, where the data says so.

This is the only stage in the suite whose mistakes cannot be corrected by a later analysis. Every other finding here is reversible: a report can be reissued, a resize can be rolled back, an allocation rule can be changed. A commitment is generally non-cancellable and non-refundable for its full term, so an oversized purchase is not a bad recommendation, it is a monthly payment for one to three years against usage that no longer exists.

## Use when

- A commitment or reservation is expiring and the cliff, the renewal decision, and the replacement sizing need to exist before the term ends rather than after the first uncovered invoice.
- Coverage or utilization has drifted, on-demand charges have appeared on workloads that were supposed to be covered, or a commitment is showing unused hours.
- A purchase is being considered and the sizing needs an eligible base, a post-optimization baseline, a term and payment option chosen for the workload's stability, and a downside case.
- The effective savings rate needs stating for a report, a negotiation, or a board question, with the baseline it is measured against named rather than implied.
- A migration, decommission, region move, or instance family change is planned and its effect on existing commitments needs quantifying before it strands them.
- The portfolio renews unevenly and laddering needs designing so the organization is not making its largest commercial decision in one week every three years.
- An optimization pass has completed and the remaining usage now needs a rate lever applied to it, which is the correct order and the reason this stage sits downstream of the optimization lanes.

## Do not use when

- The usage itself has not been examined for waste, oversizing, scheduling, or architectural change. Run `rightsizing-desk`, `waste-elimination-desk`, and `cost-aware-architecture-desk` first; committing before optimizing locks the waste in at a discount and then penalizes every optimization that follows.
- The lever is a negotiated agreement, a discount structure, an eligible spend definition, or a contractual term rather than an instrument purchase. That is `cloud-commercial-negotiation-desk`, which this desk supplies with sizing options and shortfall exposure.
- The subject is software entitlement, seat counts, or a licence commitment. That is `licensing-saas-spend-desk`.
- The subject is whether a commitment charge is amortized, blended, or billed for reporting purposes. That is `cost-data-ingestion-desk`, whose cost basis declaration this desk consumes.
- The question is how commitment cost is split across teams who did not choose to buy it. That is `shared-cost-allocation-desk` and `chargeback-invoicing-desk`.

## Required evidence

- The current portfolio at instrument granularity: type, scope, term, payment option, commitment rate, start and end dates, exchangeability, cancellability, and the account or organization that holds it.
- Measured utilization per instrument and measured coverage per eligible workload, both with the period and the dataset that produced them, since the two are different numbers that are routinely quoted interchangeably.
- The eligible base: which usage a given instrument type can cover, which usage is excluded because it runs on interruptible capacity, is already covered, sits in a non-eligible service, or falls outside the instrument's scope.
- The post-optimization usage baseline with the specific optimization work that produced it and the state of that work, because a baseline that assumes changes nobody has scheduled is a forecast wearing a measurement's clothes.
- The forecast with its method, horizon, and measured prior accuracy, plus known step changes: migrations, launches, decommissions, region moves, and family or generation changes.
- The workload stability picture: which usage is a stable floor, which is elastic, and which is on a roadmap that would move or remove it inside the term.
- The commercial agreements governing rates, discount structures, eligible spend definitions, and any spend commitment the instrument purchases would draw against.
- The purchase authority matrix with the approval level each amount and term requires, and the named role at that level.
- Prior purchases with their outcome, since the most useful input to a sizing decision is the last one that was wrong and by how much.

## Workflow

**Outcome.** Coverage and utilization measured against the eligible base with the base stated; the effective savings rate with its named baseline; stranded and underutilized commitment with its cause; an expiry cliff map with the increase each cliff lands and the date it lands; a laddering design across terms and expiry dates; a purchase recommendation with instrument, quantity, term, payment option, the post-optimization baseline it was sized against, the projected saving with its baseline, and a quantified downside case; and the position that no purchase is justified, where that is what the data says.

**Grounding.** Coverage is a percentage of eligible usage and utilization is a percentage of purchased commitment, and every figure here states which one it is and what sits underneath it. A coverage figure quoted against total spend is not wrong so much as meaningless, because it moves whenever storage or transfer charges move and says nothing about the compute a commitment can actually cover. The savings baseline is named on every figure, since a saving against on-demand list, against the effective rate already achieved, and against the prior term's blended rate are three different numbers and the largest is the one that gets quoted when nobody says which is in use. Sizing rests on the usage that remains after optimization, with the optimization work identified by its state rather than by its existence on a list.

**Constraints.** The eligible base is computed and stated before any coverage percentage is published. Utilization below the stated floor is a value-destroying instrument and is reported as such with its cause rather than averaged into a portfolio figure that looks acceptable. Stranded commitment names its cause: a workload that moved region, a family change, a decommission, an autoscaling change, or a purchase sized against a peak that never repeated. Term and payment option follow the workload's stability rather than the discount table, because the deepest discount is on the longest term with the most cash upfront and that is exactly the wrong instrument for usage that is planned to move. Flexibility is priced: a convertible or family-flexible instrument gives up discount depth in exchange for the ability to survive a change, and the trade is stated with both numbers. Laddering spreads expiry across the horizon so a single quarter never carries the whole renewal, and the current expiry concentration is stated as a figure. The downside case is quantified rather than acknowledged: if usage falls by a stated percentage, the recommendation costs a named amount more than not buying, and that number appears next to the projected saving rather than in a footnote.

A purchase follows a mandated order, recorded here with its reason so a later editor does not read it as scaffolding: the commitment cannot be cancelled once made, so the approval is the last reversible moment in the sequence.

1. Establish the post-optimization usage baseline with the state of the optimization work behind it, and treat unscheduled work as usage that still exists.
2. Compute the eligible base and the coverage and utilization position against it, including every existing instrument, so the recommendation stacks on the real portfolio rather than on an empty one.
3. Size the instrument, term, and payment option against the stable floor of that baseline, and quantify the downside case at a stated fall in consumption.
4. Obtain the authorization the matrix names for that amount and term from the named human, then execute inside the purchase window.

**Parallel surface.** Individual instruments, accounts and organizations, providers, regions, instrument families, and workload stability assessments are independent analysis units and fan out safely, as do the per-instrument utilization read, the per-workload eligibility determination, and the expiry cliff calculation per instrument. Sizing is not part of that surface and never is. Commitments float across the estate, so two workstreams each sizing for their own scope will each produce a defensible recommendation against the same eligible usage, and the combined purchase over-commits the organization against consumption that exists once. The portfolio is sized in a single pass over the whole footprint, after the fan-out returns, and that constraint holds even when the engagement covers one team, because the instruments do not respect the engagement's boundaries.

**Acceptance bar.** Every percentage names its denominator, every saving names its baseline, and every recommendation names the post-optimization baseline it was sized against together with the state of the optimization work that baseline assumes. The downside case carries a figure. The expiry map carries dates and amounts. The authority the purchase requires is named with the provision that sets it. A recommendation to buy nothing is stated with the same rigor as a recommendation to buy.

## Outputs

A complete run delivers this set:

- `commitment-position.md`: the portfolio at instrument granularity with utilization, coverage against the stated eligible base, term, payment option, flexibility, expiry, and break-even, plus the eligible base calculation itself.
- `effective-savings-rate.md`: the blended saving with its baseline named, the components that produce it, and the reconciliation between the amortized commitment charges in the export and the invoice for the same period.
- `stranded-commitment.md`: unused and underutilized commitment with the cause traced to a specific change, the remaining exposure to term end, and the exchange, modification, or resale route where one exists.
- `expiry-cliff-map.md`: every instrument's expiry with the on-demand increase it lands, the date, the decision deadline that precedes it, and the concentration risk where several land together.
- `laddering-design.md`: the target expiry distribution, the term mix that produces it, and the transition path from the current concentration with the cost of getting there.
- `purchase-recommendation.md`: instrument, quantity, term, payment option, the post-optimization baseline it is sized against with the optimization work and its state named, projected saving with its baseline, break-even, the downside case quantified at a stated fall in consumption, and the approval the authority matrix requires.
- `no-purchase-positions.md`: the scopes where no commitment is justified, with the instability, roadmap change, or coverage position that makes buying wrong.
- `commitment-downstream-handoff.md`: what `licensing-saas-spend-desk`, `cloud-commercial-negotiation-desk`, and `optimization-backlog-desk` inherit, including the drawdown effect of any recommended purchase on an existing spend commitment.

Depth standard: an artifact is complete when the approver could sign the purchase from what is written and a finance partner could model it. A coverage percentage with no eligible base, a saving with no baseline, a recommendation with no downside figure, and a term chosen without reference to workload stability are unfinished rather than draft.

When the portfolio data, the utilization dataset, the eligible usage detail, or the agreement governing eligibility exists and cannot be read, the run delivers `commitment-connector-diagnostic.md` naming each unreachable source and the coverage, utilization, and sizing conclusions it makes unavailable, in place of the position that source would have grounded. A portfolio is never reconstructed from the discount visible in the billing data.

Anti-fabrication guard: the failure this desk exists to prevent is a purchase recommendation whose baseline is a wish. The arithmetic of commitment sizing is easy and the inputs are where it goes wrong, so a recommendation sized against usage that assumes rightsizing nobody has scheduled, a decommission nobody has dated, or a migration that has slipped twice will be internally consistent, well presented, and paid for monthly until the term ends. Every recommendation therefore names the optimization work its baseline depends on and that work's actual state, and unscheduled work is treated as usage that still exists rather than as usage that is about to disappear. Coverage and utilization figures come from the provider's own commitment reporting or the export with the period attached, never from a ratio computed over spend categories that happen to be at hand, and a percentage without its denominator is not published from this desk at all. Instrument identifiers, rates, expiry dates, and eligibility definitions are copied from the portfolio record and the executed agreement, since an eligibility assumption is the difference between a commitment that covers the workload and one that does not. And where the data supports no purchase, the artifact says so; a desk that has never recommended buying nothing is a desk that is sizing to a target rather than to a baseline.

## finops_packet fields to update

- `commitments.portfolio[]` with instrument_id, type, scope, term, payment_option, commitment_rate, start, end, utilization_pct, coverage_pct, exchangeable, cancellable, and break_even per instrument
- `commitments.targets` with the coverage target and the utilization floor, each carrying the basis that sets it
- `commitments.effective_savings_rate` with the baseline named
- `commitments.expiring_within_horizon[]` with the cliff each instrument creates and its date
- `commitments.stranded_commitment[]` with the cause and the remaining exposure
- `commitments.purchase_recommendations[]` with instrument, quantity, term, payment_option, assumed_baseline_usage, projected_saving with its baseline, downside_case quantified, approver_required, and approval_state
- `opportunities[]` with `lever: commitment`, and `overlaps_with` plus `net_of_overlap` against every rightsizing, scheduling, waste, and architecture opportunity that touches the same usage
- `forecast.commitment_trajectory` with agreement_ref, commit_amount, term_end, consumed_to_date, required_run_rate, and projected_position
- `governance.approvals[]` with the purchase as the item, the amount at stake over the term, the required approver, and the authority basis
- `source_facts[]` with locator and as-of for every portfolio, utilization, eligibility, and agreement reading, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: purchasing, exchanging, modifying, or selling a commitment spends real money on a term that generally cannot be cancelled or refunded. The purchase authority the matrix names approves the quantity, the term, and the payment option. This desk prepares the item and stops at the gate.
- **Production or destructive**: the next action would exchange or modify an existing instrument in a way that cannot be reversed, or would terminate resources currently absorbing a commitment and thereby strand it.
- **Release integrity**: a coverage, utilization, effective savings rate, or projected saving figure would leave the practice without its denominator, its baseline, or the eligible base behind it, or a recommendation would be presented without its downside case. Commitment figures travel into board packs and budget lines and are never re-derived by the people who quote them.
- **Source conflict**: the provider's commitment reporting, the billing export, and the executed agreement genuinely disagree on the commitment rate, the eligible spend definition, the expiry date, or the discount applied. Record both readings with locators and as-of dates and route the conflict; the agreement governs what happens when the commitment is not met, and only the agreement.
- **Connector unreachable**: the portfolio record, the utilization dataset, the eligible usage detail, or the agreement needed to establish eligibility exists and cannot be read, so a recommendation would stack on a position nobody can see.
- **Security or privacy**: the analysis would place unredacted negotiated rates, discount structures, or commercial terms into an artifact with an audience wider than the agreement permits.

An unmeasured forecast accuracy, an undated roadmap change, an unconfirmed decommission, and a workload with no stated stability are soft gaps. Name them, label the assumption against the recommendation it affects, widen the sizing range, and continue. Sizing against pre-optimization usage to make a coverage target reachable is never an acceptable way to keep the work moving.

## Downstream handoffs

`licensing-saas-spend-desk` is next in the default sequence and needs to know whether marketplace and licence spend draws down a provider commitment, because routing a purchase through a marketplace can change a shortfall position without anybody intending it. `cloud-commercial-negotiation-desk` receives the commit sizing options, the drawdown position, the shortfall exposure, and the flexibility asks that would be worth negotiating for. `optimization-backlog-desk` receives the commitment opportunities with their overlap markers, so a saving is not counted once for resizing an instance and again for reserving it. `forecasting-variance-desk` receives the trajectory and the expiry cliffs as known step changes. `chargeback-invoicing-desk` needs the amortization treatment and the question of who carries the cost of a commitment bought centrally for usage a team consumes. Send purchase execution and instrument management in the provider console to the Cloud Infrastructure suite, and send the paper on any negotiated arrangement to the Legal Contracts suite.

## Quality bar

Good commitment work is conservative in a way that shows its arithmetic. It states the eligible base before it states coverage, names the baseline on every saving, and puts the downside case next to the upside rather than at the end. It sizes against the floor rather than the average, because the average includes a peak that a three-year term will still be paying for. It knows the difference between a coverage gap and a coverage decision, and it says plainly when a workload should stay on demand because it is going to move. It ladders, so the organization is never making its largest commercial decision in one week under time pressure. It reports an instrument at low utilization as a loss with a cause rather than folding it into a portfolio average. And it is willing to recommend buying nothing, which is the clearest signal that the sizing came from the usage rather than from a target somebody set in a meeting.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
