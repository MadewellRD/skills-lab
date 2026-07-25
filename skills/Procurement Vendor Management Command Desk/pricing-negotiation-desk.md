---
name: pricing-negotiation-desk
description: build the commercial position for a supplier deal with a should-cost model, sourced benchmarks carrying provider date and scope, total cost of ownership across the full horizon, term structure covering initial term renewal mechanics uplift caps and price protection, commitment mechanics covering minimums true-up true-down and overage rates, and a negotiation plan with ranked objectives tradeables a concession sequence and a credible walk-away. use for price benchmarking, should-cost modeling, tco analysis, discount and net effective rate assessment, renewal uplift negotiation, minimum commitment and shelfware exposure, and negotiation planning before a supplier conversation.
---

# Pricing Negotiation Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, build the commercial position, produce the artifact set, update `procurement_packet`, and continue into `contract-execution-routing-desk` once the position is agreed internally. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet, the commitment class, and the leverage window that decide what this desk can still change.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the price line, cost component, or term it affects.

Never invent a list price, a discount, a market rate, a benchmark, a comparable, a peer price, a unit cost, an implementation estimate, a switching cost, a supplier's cost base, a competitor's quote, a fiscal quarter motivation, a savings figure, or a walk-away alternative that does not exist.

## Role

Own the commercial position: what this should cost, what it will actually cost over its whole life, which terms decide the next three negotiations, and what the company is prepared to do if the supplier declines. The output is not a target price. It is a defensible position with a model behind it, a set of ranked objectives, a sequence in which concessions are exchanged rather than given, and an alternative credible enough that the supplier prices against it.

Three things separate a commercial position from a wish. A should-cost model built from cost drivers says what the thing is worth independent of what the supplier asked for, which is the only way to argue about a price that has no published list. Total cost across the full horizon includes implementation, integration, migration, training, support, internal effort, and exit, which is where the cheapest bid routinely stops being the cheapest. And the term structure carries more long-run value than the headline discount: an uplift cap, a price hold, a co-termination right, and a true-down right cost nothing to obtain while the deal is open and are unobtainable once it is signed. The negotiator who wins twenty percent on year one and leaves renewal uncapped has given the discount back with interest, on a date somebody else chose.

## Use when

- A price has been quoted and there is no basis yet for saying whether it is reasonable.
- Bids have been evaluated and normalized and the commercial position for the preferred supplier has to be built before terms are discussed.
- A renewal is approaching and the uplift, the consumption position, and the term structure need a position before the notice window closes.
- A minimum commitment, a consumption commitment, a ramp, or a true-up is on the table and the exposure needs modeling against realistic usage.
- The company needs a walk-away position and an honest assessment of the alternative behind it, including what switching would actually cost and how long it would take.
- Diligence findings are unremediated and have to be converted into contract terms while signature is still ahead.
- A savings figure is going to be claimed and its baseline, its type, and its recognition need establishing before anyone reports it.

## Do not use when

- Bids still have to be scored against published criteria, normalized against each other, and recommended: `bid-evaluation-desk`, whose normalized totals this desk consumes.
- The spend baseline, price variance across business units, or savings realization against the ledger is the question: `spend-analysis-desk`.
- The renewal calendar, the notice deadline, and the decision date have to be established first: `renewal-consolidation-desk`, which decides whether this negotiation is still open.
- Consumption against entitlement has never been measured and the real question is shelfware rather than discount: `supplier-performance-sla-desk`.
- The clause language, enforceability, or liability position is the question rather than the commercial position: the Legal Contracts suite.
- The signature routing, approval chain, and document set are the question: `contract-execution-routing-desk`.

## Required evidence

- The evaluated bids with their normalized totals, the normalization basis, and the assumptions every bidder priced against.
- The current agreement where one exists: price paid, unit structure, term, uplift mechanics, and what the last negotiation achieved.
- The supplier's quote with its structure, its validity period, and everything excluded from it.
- The published list price where one genuinely exists, and an explicit note where the list is set by the supplier and never charged.
- Benchmarks and comparables with provider, date, scope, volume, and why each is comparable to this engagement.
- Should-cost inputs: the cost drivers for this category, unit economics, and the components a supplier of this kind actually incurs.
- Consumption against entitlement for any renewal or expansion, since the seats nobody uses are a larger reduction than the discount nobody offered.
- The full cost picture beyond licence: implementation, integration, data migration, training, support tiers, internal effort, and exit and egress costs.
- The diligence findings and the terms the security, privacy, and integrity reviews require the contract to carry.
- The alternative: the realistic second choice, its cost, its switching cost, and its switching lead time.
- The authority levels this value engages, and the leverage window with what closes on which date.

## Workflow

**Outcome.** A should-cost model with its method and inputs stated, a benchmark set where genuine comparables exist, a total cost position across the full horizon, a term structure position, a commitment mechanics position, a negotiation plan with ranked objectives, tradeables, and a concession sequence, a walk-away position with the alternative behind it, and the leverage assessment stating what is open, what closes when, and what has already been said to the supplier.

**Grounding.** A benchmark is a comparable with a source, a date, a scope, and a volume. An impression of what things cost is not a benchmark, and it is the number that becomes the negotiation target, then the concession the supplier tests, then the savings figure in a report finance is asked to recognize. A discount is stated against what it discounts; a discount off a list price the supplier sets and never charges describes the supplier's pricing practice rather than the value obtained. Net effective unit price after ramp, credits, and bundled items is the comparable figure, not the headline.

**Constraints.**

- Model the full horizon, not the first year. Ramps, uplifts, and expiring price protection move the average unit price materially, and a three year deal is compared as a three year deal.
- Price the term structure explicitly. Uplift cap, renewal mechanics, price hold duration, benchmarking or most favored terms, co-termination, and the right to reduce at renewal each carry a number, and each is unobtainable after signature.
- Model commitment mechanics against realistic consumption rather than the sponsor's forecast, and state the exposure at the low case. Unused entitlement is the most common and least visible cost in this domain.
- Rank objectives before the conversation and identify what the company would genuinely give up. A plan with eleven priorities has none, and the supplier discovers that faster than the negotiator does.
- Sequence concessions as exchanges. Each concession names what is received for it; a concession given to build goodwill is priced by the supplier as the new starting point.
- State the walk-away with the alternative behind it, including its switching cost and lead time. A walk-away with nothing behind it is a bluff, and an incumbent knows the company's switching cost better than the company does.
- Convert unremediated diligence findings into terms now. Before signature a finding is a commercial position with a supplier motivated to fix it; after signature it is an issue with no deadline and no consequence.
- Separate realized saving from avoided cost everywhere. A reduction against a price the company was actually paying reaches a budget line; a reduction against a proposal reaches a slide.

**Parallel surface.** Independent workstreams fan out: the should-cost build, benchmark gathering per comparable, each cost component in the total cost model, the term structure position, the commitment mechanics model, and the switching cost estimate for the alternative each draw on different sources and are parallel safe. Where several suppliers are still live, each supplier's commercial position is built independently. Two steps are single passes after the fan-out returns. The negotiation plan is assembled once across the whole position, because ranking objectives and sequencing concessions is meaningless per component and the whole point is what gets traded against what. The leverage assessment is also one pass, since it depends on the total picture of what has been said, what has been committed, and which dates close.

**Acceptance bar.** Every price position states its basis and separates modeled from sourced. Each benchmark carries provider, date, scope, and volume, or the position states that no comparable was found. The total cost model shows every component including internal effort and exit, over a stated horizon, with the net effective unit price. The term structure position states the cap, the hold, and the renewal mechanics being sought and what each is worth. The commitment model shows the low, expected, and high consumption cases and the exposure at each. The negotiation plan names the ranked objectives, the tradeables, the concession sequence, and the walk-away with its alternative costed.

## Outputs

A complete run delivers the set:

- `should-cost-model.md`: the cost drivers, the inputs, the method, the resulting range, and the sensitivity to the two or three assumptions that move it most.
- `benchmark-set.md`: every comparable with provider, date, scope, volume, and the reason it is comparable, plus the positions where no comparable was found, stated as such.
- `total-cost-of-ownership.md`: the horizon, every component from licence to exit including internal effort, the year by year profile, and the net effective unit price after ramp and credits.
- `term-structure-position.md`: initial term, renewal mechanics, uplift cap, price protection and its expiry, co-termination, benchmarking rights, and reduction rights, each with the position sought, the fallback, and what it is worth.
- `commitment-mechanics-model.md`: minimums, ramps, true-up and true-down rights, overage rates, carryover of unused entitlement, and the exposure modeled at low, expected, and high consumption.
- `negotiation-plan.md`: ranked objectives with the consequence of missing each, tradeables, the concession sequence with what is received for each, the anticipated supplier positions, and the questions that establish them.
- `walk-away-position.md`: the point at which the company declines, the alternative, its cost, its switching cost, and its lead time, with an honest statement where the alternative is weak.
- `leverage-assessment.md`: the leverage window, what has already been communicated to the supplier and by whom, what closes on which date, and what the position becomes after each date.
- `savings-position.md`: the figure, the baseline behind it, whether it is realized saving or avoided cost, and what finance would need to recognize it.
- `pricing-negotiation-downstream-handoff.md`: the agreed commercial position, the terms the diligence findings require, and the open positions the contract stage inherits with their risk owners.

Depth standard: an artifact is complete when the person delivering the negotiation could walk into the conversation with it and answer the supplier's first three questions without leaving the room. "Push for a better discount" is an intention; "the net effective unit price sought over three years with the uplift capped, the fallback if the cap is refused, the two comparables that support the number with their dates, and the reduction right traded for the longer term" is a position.

Where a genuine list price does not exist, `benchmark-set.md` says so and the discount discussion is replaced by unit economics rather than dropped. Where the alternative is genuinely weak and the company has no realistic walk-away, `walk-away-position.md` states that plainly, because a negotiator who believes in a walk-away that does not exist negotiates worse than one who knows the position is thin. Where the supplier's quote, the current agreement, or the consumption data cannot be reached, `pricing-negotiation-diagnostic.md` names the gap and the positions it makes unavailable.

This desk produces documents made almost entirely of numbers, and a number carries no visible trace of where it came from. A figure computed from a should-cost model, a figure read off a competitor's quote, a figure a peer mentioned on a call, and a figure someone remembered all render as the same digits in the same column, and by the time the position reaches the supplier nobody can tell them apart, including the person who wrote it. That is why every figure here travels with its origin attached and the model separates modeled from sourced rather than blending them into a single view. A price position with no comparable behind it is recorded as no comparable found and argued from unit economics instead; a supplier's motivation nobody established is written as an assumption rather than as intelligence; and a savings figure is not written until its baseline is named, because that number does not stop at this artifact, it travels to a quarterly report and finance is asked to book it.

## procurement_packet fields to update

- `commercial.price_structure`, `quoted_price`, `list_price`, `discount_claimed`, `benchmark`, `should_cost`, `tco_model`, `term_structure`, `payment_terms`, `commitment_mechanics`, `negotiation_plan`, `concessions`, `savings`.
- `contract.open_positions` for every term the negotiation has not closed, each with the company position, the supplier position, and a named risk owner.
- `policy.required_terms` where a mandatory position has to survive the negotiation intact.
- `approvals` for the value band this deal engages, with the amount at stake, the authority basis, and the state, including approval to communicate a number.
- `relationship.switching_cost` and `switching_lead_time` where the walk-away analysis established them.
- `leverage_window` and `commitment_class` where this stage changes them.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Production or destructive**: any number, target, budget figure, deadline, or indication of intent that reaches the supplier. This is irreversible for a reason that has nothing to do with systems: the counterparty heard it and repriced against it. The most expensive sentence in this domain is a sponsor telling a supplier they have essentially won before terms are agreed, because every concession available before that sentence is gone after it and nothing recovers it. Prepare the number and the script; the person with authority delivers it.
- **Approval**: committing to a price, a term length, a minimum commitment, or a payment schedule that engages an authority level, and accepting a risk in exchange for a commercial concession. A negotiator cannot approve the deal they negotiated.
- **Security or privacy**: a required security, privacy, or data protection term is being traded away for price. Those positions are obligations rather than tradeables, and a discount bought with a waived control is a cost recorded in the wrong column.
- **Source conflict**: the quote, the order form, the current agreement, and the ledger disagree about what the company is paying today, which makes every saving figure downstream unverifiable. Record both readings with their locators and route the conflict rather than adopting the one that produces the better number.
- **Release integrity**: a benchmark with no comparable behind it would be quoted to the supplier, or a savings figure with no baseline would be reported to finance or into a quarterly result. Both are claims the company cannot support when asked, and the second one reaches an audited number.
- **Connector unreachable**: the executed agreement, the payables history, or the consumption data exists and cannot be read, so the current price and the entitlement position would be assumed rather than established.

An unanswered question about the supplier's cost base, an unavailable peer comparable, an implementation estimate with a wide range, and an unconfirmed usage forecast are soft gaps. Label them inline against the line they affect, model the range rather than a point, and continue.

## Downstream handoffs

`contract-execution-routing-desk` inherits the agreed commercial position, the term structure, the commitment mechanics, and every open position with its risk owner, so legal negotiates a defined list rather than discovering positions in the redlines. `supplier-integrity-screening-desk` findings arrive here and leave as contract terms, which is the only stage at which that conversion is free. `vendor-onboarding-provisioning-desk` inherits the entitlement counts and the invoicing structure the pricing assumes. `supplier-performance-sla-desk` inherits the service levels and remedies that were priced, and the consumption baseline the commitment was set against. `spend-analysis-desk` inherits the savings claim with its baseline and its type, because that is where realized saving is tested against what the ledger shows. `renewal-consolidation-desk` inherits the uplift cap, the price hold expiry, and the reduction rights, which are the terms that decide the next negotiation.

## Quality bar

A good commercial position is one the supplier's own deal desk would recognize as informed. It argues from unit economics rather than from a percentage, it knows which terms carry value beyond the current term, and it is candid internally about where the company is weak. Every number shows its origin. The concession sequence reads as a series of exchanges rather than a list of hopes. The walk-away is either real and costed, or explicitly described as thin so nobody negotiates as though it were real. And the position holds up on the worst day: the supplier asks where the benchmark came from, and the answer is a comparable with a provider, a date, and a scope, rather than a pause.
