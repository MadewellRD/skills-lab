---
name: spend-analysis-desk
description: build the spend baseline from the accounts payable ledger rather than from contract values, consolidate suppliers across brands resellers subsidiaries and duplicate vendor master records, apply the category taxonomy and report the uncategorized remainder at full value, separate spend under an agreement from spend with nothing behind it, quantify tail and off-contract and card spend, expose price variance for the same item across business units, and test negotiated savings against what the ledger actually shows. use for spend cube and baseline analysis, supplier rationalization, maverick and off contract spend, tail spend management, contract coverage, price variance, savings realization, and cost reduction targets.
---

# Spend Analysis Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, build the baseline, produce the artifact set, update `procurement_packet`, and continue into `renewal-consolidation-desk`, since the consolidation case is only worth making once the ledger has said what each overlapping tool actually costs. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that makes the payables ledger authoritative for what was paid.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the supplier, category, or spend line it affects.

Never invent a spend figure, a supplier parent relationship, a category assignment, a cost center, a contract coverage status, a unit price, a utilization rate, a savings figure, a baseline, or a budget line finance has not agreed to.

## Role

Own what the company actually paid, as distinct from what it committed to, intended to, or was invoiced for. Contract value is a commitment, a purchase order is an intention, and a supplier's account statement is their record; only the payables ledger says what left the company. A spend analysis built on any of the other three describes something other than spend, and it goes wrong in a specific direction: it is cleanest exactly where the problem is worst, because the card purchases, the reimbursed subscriptions, and the reseller invoices that never touched a requisition are the ones the other systems never saw.

The analytical work here is consolidation, not arithmetic. The same supplier arrives as a brand, a legal entity, a reseller, a marketplace intermediary, an acquired product still billing under its old name, and two misspelled vendor master records, and until those are collapsed the concentration is invisible and the negotiation leverage does not exist. Everything else this desk produces, contract coverage, tail, fragmentation, price variance, savings realization, is downstream of getting the population and the supplier identity right.

## Use when

- A spend baseline is needed for a category, a business unit, a supplier, or the whole portfolio.
- A cost reduction or savings target has landed and nobody has established what is currently being spent or on what.
- Suppliers have to be consolidated across brands, resellers, subsidiaries, and duplicate vendor master entries before any concentration or leverage claim is made.
- Contract coverage has to be established: what is spent under an agreement against what is spent with nothing behind it.
- Off-contract, off-channel, card, and expense-reimbursed spend has to be quantified and attributed to a buying unit.
- Tail spend needs sizing, with its supplier count and its aggregate value, before anyone decides what to do about it.
- The same item or service is suspected of being bought at different prices across business units.
- A savings claim has to be tested against the ledger and separated into realized saving and avoided cost before finance is asked to recognize it.
- Several tools appear to deliver one capability and the overlap argument needs a factual basis.

## Do not use when

- The question is one supplier's utilization against its entitlement rather than spend across the portfolio: `supplier-performance-sla-desk`.
- The question is portfolio concentration, dependency, and exit readiness rather than the spend baseline: `supplier-relationship-governance-desk`.
- The renewal calendar, notice deadlines, and the consolidation decision are the work: `renewal-consolidation-desk`, which consumes this baseline.
- The commercial position, benchmarks, and negotiation plan for a specific deal are the work: `pricing-negotiation-desk`.
- The category boundary, supply market structure, and sourcing approach are the question: `category-strategy-desk`.
- The ask is purchase order processing, three-way match, accruals, or the recognition of a saving against a budget line: the Finance and Accounting suite.
- The ask is a data pipeline, a spend cube build, or reporting infrastructure rather than category judgment: route the engineering to the Data suite with the model and the acceptance criteria attached.

## Required evidence

- The payables ledger for the period at invoice level, with supplier, amount, currency, date basis, cost center, and general ledger coding.
- The period definition and the date basis it uses, since invoice date, posting date, and payment date produce different baselines from the same ledger.
- The vendor master with parent and subsidiary relationships, duplicate records, and inactive entries.
- The contract portfolio with values, terms, and the entity each agreement is with, for coverage matching.
- Purchase order data and the buying channels used, including no-purchase-order exceptions.
- Corporate card and expense reimbursement data, which is where subscriptions bought around the requisition process live.
- The category taxonomy and the mapping rules, including how unmapped spend is to be treated.
- Credit memos, refunds, rebates, intercompany and pass-through entries, tax and freight lines, and prepayments or accruals that distort the period.
- Foreign exchange rates and the restatement basis where the ledger spans currencies.
- Prior savings claims with their baselines, and how finance treated each.

## Workflow

**Outcome.** A spend baseline reconciled to the ledger with its population and period stated, a supplier consolidation with the mapping rules and the unconfirmed mappings flagged, a category view with the uncategorized remainder reported at full value, a contract coverage position, an off-contract and off-channel view attributed to buying units, a tail analysis, a price variance view, a fragmentation view, and a savings realization test separating realized saving from avoided cost.

**Grounding.** The ledger is the population. Every figure reconciles to a stated control total, and every exclusion is named with its value rather than dropped. Contract values, purchase orders, and supplier statements are cross-references used to explain the ledger, never substitutes for it.

**Constraints.**

- State the population, the period, the date basis, the currency treatment, and the exclusions before any figure. A baseline without those is a number that cannot be reproduced or defended.
- Consolidate suppliers to the legal entity and record the rule used. Where a parent relationship is inferred rather than confirmed from the vendor master or a filing, flag it, because the concentration figure depends entirely on it.
- Trace reseller and marketplace spend through to the actual vendor where the invoice allows, and record where it does not, since a reseller-mediated category looks fragmented and is not.
- Report the uncategorized remainder at its full amount. Distributing unmapped spend proportionally across categories produces a tidy view that is wrong everywhere.
- Match contract coverage on the entity and the period, not on the supplier name. Spend against an expired agreement is uncovered spend.
- Quantify card and expense spend separately even where it is small, because that is the channel through which unreviewed suppliers enter and where duplicate subscriptions accumulate.
- Compare unit prices only where the item, the volume band, and the term are genuinely the same, and state the comparison basis. A price variance built on unlike units is an argument the business unit will win.
- Test savings against the ledger. A negotiated reduction that does not appear as a lower payment is an avoided cost at best, and the artifact says which one it is and names the budget line where finance recognized it.

**Parallel surface.** Independent items fan out and are parallel safe: categories, cost centers, business units, legal entities, and periods can each be analyzed at once, and the coverage match per supplier runs independently. The findings that give this desk its value are single passes over the whole population and cannot be assembled from the fan-out: supplier consolidation, because the same vendor appears in several partitions and only a whole-population pass collapses it; concentration, for the same reason; fragmentation, since several suppliers delivering one capability sit in different cost centers by definition; price variance, which exists only across business units; tail analysis, which is a property of the distribution; and the reconciliation to the control total, which is the step that proves the partitions add up to the ledger.

**Acceptance bar.** The baseline reconciles to a stated control total with every exclusion named and valued. Supplier consolidation states its rules and flags inferred mappings. The category view reports uncategorized spend at full value. Contract coverage is matched on entity and period. Off-contract spend names the buying unit where the data allows and states where it does not. Price variance states the comparison basis. Every savings figure names its baseline, its type, and whether finance has agreed to recognize it. Unattributable spend appears at full value as unattributed.

## Outputs

A complete run delivers the set:

- `spend-baseline.md`: total spend with population, period, date basis, currency treatment, exclusions with their values, and the reconciliation to the ledger control total.
- `supplier-consolidation.md`: the consolidated supplier view with the mapping rules applied, the brands, resellers, subsidiaries, and duplicate records collapsed into each entity, and every inferred mapping flagged as unconfirmed.
- `category-view.md`: spend by category with the taxonomy applied, the mapping coverage rate, and the uncategorized remainder at full value with its largest constituents named.
- `contract-coverage.md`: spend under a current agreement against spend with no agreement or an expired one, matched on entity and period, with the largest uncovered suppliers listed.
- `off-contract-and-channel-analysis.md`: spend that bypassed the required channel, split by card, expense, and no-purchase-order invoice, attributed to buying units where the data allows, with the unattributable portion stated.
- `tail-spend-analysis.md`: the tail definition used, its supplier count, its aggregate value, its category composition, and the share of it that is unreviewed and uncontracted.
- `price-variance.md`: the same item or service bought at different prices across the company, with the comparison basis, the volume and term differences, and the value of aligning to the best price.
- `fragmentation-view.md`: capabilities delivered by more than one supplier, what each costs, which business units use which, and the combined value.
- `savings-realization.md`: negotiated savings against what the ledger shows, realized saving and avoided cost separated, the baseline for each, and the budget line where finance recognized it or the note that it has not been.
- `spend-analysis-downstream-handoff.md`: the baseline, the consolidated entities, the fragmentation candidates, and the coverage gaps the renewal, consolidation, and category stages inherit.

Depth standard: an artifact is complete when a category owner could open a negotiation from it and a controller could reconcile it. "Around a certain amount with this supplier" is a recollection; "consolidated spend for the entity across four vendor master records and one reseller, for a stated period on a stated date basis, of which a stated share sits under a current agreement, reconciling to the ledger control total with the named exclusions" is a baseline.

Where a category is genuinely clean, the artifact says so with the evidence rather than manufacturing a finding, because a spend analysis that reports an opportunity in every category is not read twice. Where the payables ledger cannot be read at all, this run does not produce a baseline: `spend-analysis-diagnostic.md` states what was reachable, what was not, and which conclusions are unavailable, and no baseline is assembled from contract values, purchase orders, or supplier statements in its place.

A spend analysis comes with its own false proof of correctness, and that is what has to be guarded against here. The output is a set of tables whose parts sum to a total, and a table that adds up looks reconciled whether or not it is: an inferred parent-subsidiary mapping, a proportional allocation of unmapped spend, a supplier name matched by similarity, a period assembled on one date basis and compared to a period assembled on another, and a currency restated at a rate nobody recorded all produce arithmetic that balances perfectly and a picture that is wrong. Downstream, three stages treat that picture as the population: the consolidation case, the concentration view, and the savings claim that goes to finance. So the mapping rules are stated and inferred mappings are flagged rather than absorbed, unattributed spend is reported at its full amount rather than distributed, the reconciliation to the ledger control total is shown rather than asserted, and where the ledger is incomplete for a period that gap is stated with its value rather than left to be read as a smaller number.

## procurement_packet fields to update

- `spend.period`, `by_supplier`, `by_category`, `by_cost_center`, `contract_coverage`, `tail_spend`, `off_contract_spend`, `fragmentation`, `price_variance`, `savings_realization`.
- `relationship.concentration` where the consolidated view changes the portfolio picture, since concentration computed on unconsolidated names is systematically understated.
- `renewals.consolidation_candidates` seeded from the fragmentation view with the combined value attached.
- `demand.duplicate_candidates` and `existing_coverage` where the analysis shows the company already pays for a requested capability.
- `commercial.savings` updated with the realized and avoided split and the recognition state.
- `approvals` where a savings figure is going to be reported into a management result or a budget line.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Connector unreachable**: the payables ledger cannot be read and the analysis would be assembled from the contract repository, purchase orders, or supplier statements instead. Each of those describes intention rather than payment, and all three systematically omit exactly the off-contract and card spend the analysis exists to find, so the resulting picture is cleanest where the problem is worst. A ledger that is merely incomplete for a period is a stated gap; a ledger that cannot be reached is this halt.
- **Source conflict**: the ledger, the contract repository, and the business units disagree about what is in the category or what is being spent. This happens routinely because suppliers are recorded under brands in one system and entities in another, resellers sit between the company and the vendor, and a meaningful share of the category never routed through procurement. Record both readings with their locators rather than adopting the one that supports the conclusion.
- **Release integrity**: a savings figure would be reported to finance, an executive review, or an external result without its baseline, or an avoided cost would be presented as a realized saving. This number reaches an audited statement and does not come back.
- **Security or privacy**: the ledger extract contains personal data, payroll, legal settlement, or medical payment detail and would be circulated beyond the people entitled to see it, or supplier pricing held under confidentiality would be shared across business units in a way the agreements prohibit.
- **Approval**: acting on the analysis by cancelling a supplier, stopping a payment, reallocating a budget line, or committing a savings target. Analysis is reversible; each of those is not.
- **Production or destructive**: any part of the analysis that reaches a supplier, including telling a vendor what the company spends with it in aggregate, which is information the supplier does not have and will price against.

An incomplete card data feed, an unmapped cost center, a supplier whose parent relationship cannot be confirmed, and a period with a known posting lag are soft gaps. State each with its value, keep it visible in the totals as unattributed or unconfirmed, and continue.

## Downstream handoffs

`renewal-consolidation-desk` inherits the fragmentation view, the consolidated supplier entities, and the coverage gaps, which is what turns a consolidation opinion into a case with a number. `pricing-negotiation-desk` inherits the current paid price, which is the only defensible baseline for a saving, and the aggregate volume that creates leverage. `supplier-relationship-governance-desk` inherits the consolidated concentration figures. `intake-triage-desk` inherits the duplicate and existing coverage evidence, so the next request for a capability the company already buys is answered in the first minute. `category-strategy-desk` inherits the baseline and the population definition. `vendor-onboarding-provisioning-desk` receives the coding gaps that made spend unattributable, since that is where the next baseline gets fixed.

## Quality bar

A good spend analysis is reproducible by someone else from the stated population, period, and rules, and it reconciles. It collapses the same supplier into one line even when the ledger spells it four ways, and it says which of those mappings it confirmed and which it inferred. It reports the ugly remainder rather than smoothing it. It distinguishes a saving that reduced a payment from a saving that reduced a proposal, and it names the budget line for the first. And it earns its place by finding the things no single purchase could reveal: the capability bought six times, the price one business unit pays and another does not, and the tail of unreviewed suppliers that is larger in aggregate than the contract everyone is arguing about.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
