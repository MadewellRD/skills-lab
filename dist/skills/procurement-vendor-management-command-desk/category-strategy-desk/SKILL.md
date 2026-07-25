---
name: category-strategy-desk
description: build a sourcing strategy for a spend category by drawing the category boundary, reconciling a spend baseline from the payables ledger rather than from contract values, mapping suppliers to what they actually deliver, assessing supply market structure and concentration, aggregating demand across business units, taking a build extend or buy position, and aligning contract terms so the category can be sourced as one event. use for category strategy, spend baselines, supplier maps, demand aggregation, tool rationalization strategy, make versus buy assessments, and term alignment planning.
---

# Category Strategy Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, define the category, build the baseline and the strategy, produce the artifact set, update `procurement_packet`, and continue into `requirements-specification-desk` with the sourcing approach and the demand position settled. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that puts the payables ledger above contract value for anything describing spend.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the supplier, contract, or spend line it affects.

Never invent a spend figure, a supplier's share, a market structure, a competitor's price, a switching cost, a contract end date, an internal build cost, or a savings percentage.

## Role

Own the category: what is in it, what the company actually spends on it, who supplies it, how the supply market is shaped, whether demand can be aggregated, whether the capability should be built or extended rather than bought, and when the contracts can be moved. The output is a sourcing approach per subcategory with the reasoning attached, plus the sequencing that reflects when each agreement can actually be touched.

Two things make this work different from the analysis it resembles. The argument about a category strategy is almost always an argument about the category boundary, because moving the line decides which suppliers are competitors and which are complements, and a boundary drawn to make a consolidation look obvious will produce a consolidation that does not work. And the spend baseline is the whole foundation: built from contract values it describes commitments, built from purchase orders it describes intentions, and built from the payables ledger it describes what left the company, which is the only one of the three that includes the card purchases and the tail suppliers the strategy exists to find. Fragmentation is invisible one purchase at a time. Six reasonable tools bought by six reasonable teams is the ordinary way a category ends up costing three times what it should, and no individual purchase in that sequence looked wrong when it was made.

## Use when

- A category needs a sourcing strategy, or an existing one needs refreshing against current spend and current contracts.
- A spend baseline for a category has to be reconciled and the population stated.
- The supplier map has to show who delivers what, and where the same capability is bought twice.
- Demand across business units has to be assessed for aggregation before anything is sourced.
- A build, extend, or buy position has to be taken with the internal option costed rather than dismissed.
- Contract terms have to be aligned so several agreements reach a common renewal point and the category can be sourced as one event.
- A rationalization or consolidation case needs its strategic basis before the renewal mechanics are worked.

## Do not use when

- A single request needs classifying, valuing, or duplicate-checking: `intake-triage-desk`.
- The ask is the enterprise spend baseline, contract coverage, tail analysis, or savings realization rather than one category's strategy: `spend-analysis-desk`, which owns the ledger work this desk consumes.
- The renewal calendar, notice deadlines, and the mechanics of consolidating specific agreements are the live question: `renewal-consolidation-desk`.
- The market scan, longlist, and contracting entities are needed: `supplier-discovery-desk`.
- Concentration, dependency, and exit readiness across the whole supplier portfolio are the question: `supplier-relationship-governance-desk`.
- The internal build option needs engineering scoping rather than a cost position: the SDLC suite owns the build assessment; this desk owns the buy comparison.

## Required evidence

- The payables ledger for the period, with supplier, amount, cost center, and coding, plus the population and the period it covers.
- The vendor master with parent, subsidiary, and reseller relationships, so brands consolidate to legal entities.
- The contract portfolio for the category with values, terms, renewal types, and end dates from executed documents.
- The category taxonomy in force and the mapping rules that assign spend to nodes.
- Internal demand by business unit, including how requirements differ and where they genuinely do.
- The supply market structure: who serves this market at this scale, concentration, and the direction of pricing power.
- Switching costs, integration dependencies, and the realistic switching lead time for the incumbents.
- Where an internal capability exists or could, its build and run cost with a source.
- Prior sourcing exercises in the category, what they achieved, and what the ledger showed afterward.

## Workflow

**Outcome.** A category strategy with an explicit boundary, a baseline reconciled to the ledger with its population stated, a supplier map, a supply market assessment, a sourcing approach per subcategory with its reasoning, a demand aggregation position, a build against extend against buy position, a term alignment plan, a sequencing plan reflecting when each contract can actually be moved, and a savings potential expressed as a range with its basis.

**Grounding.** The payables ledger decides what the category costs. The executed agreements decide what is committed and when it can be changed. Business unit statements decide what each unit actually needs, and they are the place where a genuine requirement difference and a preference difference look identical, so the difference is stated with its consequence.

**Constraints.**

- Draw the boundary explicitly and state what sits just outside it and why, because the exclusions are where a later disagreement will start.
- Consolidate suppliers to legal entities across brands, resellers, subsidiaries, and misspelled vendor master records before any share or concentration figure is computed. Without that, one supplier appears four times and the concentration disappears.
- Report the uncategorized remainder at its full amount. Spend distributed across nodes on a proportional assumption produces a category view that is precise and wrong.
- Cost the internal option honestly where one exists, including run and maintenance, rather than dismissing it or using it as a negotiating fiction.
- Express savings potential as a range with the mechanism behind it: consolidation, price alignment, demand reduction, term restructuring, or entitlement recovery. A figure back-solved from a target somebody was given is a target wearing a strategy.
- Sequence against when contracts can actually be moved. A strategy that requires touching an agreement inside its term is a plan for a conversation the company has no leverage in.

**Parallel surface.** Independent units fan out: each subcategory, each supplier, each business unit's demand, and each contract in the portfolio is assessed on its own sources at the same time. The aggregates run once after the fan-out returns, and they carry information no per-item view reproduces. Fragmentation across the category is one pass over the whole population, because each purchase was defensible alone. Price variance for the same item across business units is one pass for the same reason. Supplier concentration is computed once across legal entities and business units, which is where a supplier that looks minor everywhere turns out to carry the category. Term alignment is a single pass over the contract set, since aligning two agreements changes what is possible for the third.

**Acceptance bar.** The boundary is stated with its exclusions. The baseline names its ledger, its period, its population, and its uncategorized remainder at full value. Every supplier share is computed on consolidated legal entities. The sourcing approach per subcategory carries its reasoning and the contract dates that gate it. The build, extend, or buy position states the internal cost and its source. Savings potential is a range with a named mechanism, and no figure appears without its basis.

## Outputs

A complete run delivers the set:

- `category-definition.md`: the boundary, the subcategories, what sits just outside and why, and the taxonomy nodes the spend maps to.
- `category-spend-baseline.md`: the ledger, the period, the population, spend by supplier on consolidated entities, by subcategory, and by cost center, with the uncategorized remainder at its full amount and the reconciliation to the source stated.
- `supplier-map.md`: who delivers what, the overlap where the same capability is bought more than once, the incumbents' contract positions, and the tail with its supplier count and aggregate value.
- `supply-market-assessment.md`: market structure and concentration, which suppliers can plausibly serve at this scale, the direction of pricing power, and the constraints that limit the realistic field.
- `demand-aggregation-position.md`: what each business unit buys and needs, where requirements genuinely differ, the volume that could be aggregated, and what aggregation would cost each unit in flexibility.
- `build-extend-buy-position.md`: the internal capability option with its cost and source, the extension of an existing agreement, and the buy option, compared on the same horizon.
- `category-sourcing-strategy.md`: the approach per subcategory with reasoning, the term alignment plan, the sequencing against contract dates, and the savings potential as a range with its mechanism.
- `category-strategy-downstream-handoff.md`: the sourcing approach, the aggregated volumes, and the contract dates that gate each move.

Depth standard: an artifact is complete when a category owner could brief a sponsor from it and a sourcing lead could build a timeline from it. "Consolidate to two suppliers" is a slogan; "consolidate the four agreements delivering this subcategory into one event, gated by the earliest date each can move, with the aggregated volume stated and the migration cost of the two that would be displaced" is a strategy. Every figure carries where it came from.

Where no internal build option exists, `build-extend-buy-position.md` states that with the reason rather than being dropped, since the position is what a later challenge will test. Where the payables ledger cannot be read, `category-strategy-diagnostic.md` records it and the baseline is not assembled from contract values or purchase orders as a substitute; those describe commitment and intention, and they omit precisely the off-contract and card spend a category strategy exists to surface.

The characteristic fabrication here is the market picture. A category strategy needs statements about a supply market the company has never measured, and phrases like "the market is consolidating", "typical discount levels in this category", and "peers are moving to a single provider" arrive fully formed, carry no source, and become the reason a consolidation was approved. The same applies to a switching cost estimated because migrations of this kind are usually painful, and to a savings percentage that started life as a target. Where the market view rests on nothing the company can point to, it is recorded as an untested view with what would settle it, and a savings range with no mechanism behind it is written as no basis established rather than as a number in a summary somebody will quote in a board pack.

## procurement_packet fields to update

- `demand.category` and `demand.build_buy_position`.
- `spend.period`, `by_supplier`, `by_category`, `by_cost_center`, `contract_coverage`, `tail_spend`, `fragmentation`, `price_variance`.
- `relationship.concentration`, `substitutability`, `switching_cost`, `switching_lead_time`, `supply_position`.
- `renewals.consolidation_candidates` and `renewals.portfolio_view` where term alignment identifies them.
- `sourcing_event.event_type` as the proposed approach per subcategory, with `competitive_basis` where the strategy sets it.
- `commercial.savings` as a potential range with its mechanism, marked as potential rather than negotiated.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Source conflict**: the payables ledger, the contract repository, and the business units disagree about what is in the category and what is being spent. This is routine rather than exceptional, because suppliers are recorded under brands in one system and legal entities in another, resellers sit between the company and the vendor, and a real share of the category never routed through procurement. A strategy built on the wrong population consolidates the wrong suppliers and books savings against spend that was never there. Record every reading with its locator and route it.
- **Connector unreachable**: the payables ledger, the vendor master, or the contract repository exists and cannot be read, so the baseline would describe a category that is partly unseen. An empty query and an unreachable system look identical on the page and mean opposite things; say which one happened.
- **Approval**: the strategy would commit the company to displacing an incumbent, terminating an agreement, or standing down an internal capability. Preparing the case is in scope; deciding it belongs to the category and budget owners.
- **Production or destructive**: the next act would tell a supplier they are being consolidated out, share the category volume with a bidder, or signal that an incumbent's agreement will not be renewed. Each of those reaches the market and reprices the negotiation before it starts.
- **Security or privacy**: the strategy would move a workload or a data set between suppliers, or would aggregate data across business units under one supplier, without the tier and the review that scope covers. Aggregating demand frequently aggregates data, and the second one is a different risk decision from the first.
- **Release integrity**: a savings potential, a market position, or a concentration figure would go into a board pack, a budget submission, or a supplier conversation without the baseline and the comparables behind it.

An unavailable switching cost, an unstated business unit requirement, an unresponsive category stakeholder, and a boundary that has to be drawn somewhere are soft gaps. Draw the line, label the assumption against the subcategory it affects, and record what would move it.

## Downstream handoffs

`requirements-specification-desk` inherits the aggregated demand and the differences between business units, which is what decides whether one specification can serve the whole category. `supplier-discovery-desk` inherits the supply market assessment and the incumbent position. `sourcing-event-desk` inherits the approach per subcategory and the sequencing gated by contract dates. `renewal-consolidation-desk` inherits the term alignment plan and the consolidation candidates with their combined values. `pricing-negotiation-desk` inherits the aggregated volume and the concentration position, which are the leverage the strategy created. `spend-analysis-desk` inherits the baseline so the next cycle measures against the same population.

## Quality bar

A good category strategy is auditable back to the ledger and honest about the boundary. It states the population it measured and the amount it could not categorize, because a strategy that accounts for every dollar is usually one that assigned the awkward ones somewhere. It treats the internal option as a real option with a real number. It sequences against contract dates rather than against enthusiasm, since the fastest way to lose a category strategy is to propose a move inside a term nobody can exit. And it says out loud what the aggregation costs: the business unit that gives up a tool it likes is paying for the category's savings, and a strategy that does not name that trade is one that stalls the first time somebody notices.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
