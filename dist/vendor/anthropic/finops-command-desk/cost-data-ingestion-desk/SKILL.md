---
name: cost-data-ingestion-desk
description: establish the cost basis and reconcile the analysis dataset to the provider invoice across billing and usage exports, focus-conformed schemas, cost platform views, and vendor statements. covers amortized versus billed versus effective cost views, commitment fee and prepaid credit amortization, credit refund and adjustment treatment, tax support and marketplace charges, currency normalization with its rate source, refresh lag and export granularity, open closed and partial period state, and the questions the available billing data cannot answer.
---

# Cost Data Ingestion Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite and sits first in the dependency chain, because every figure every later desk produces inherits the basis, the period, and the datasets declared here. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the figure it moves and recorded in `open_questions`. Never invent invoice totals, dataset totals, variance amounts, credit or refund values, exchange rates, refresh timestamps, export schema versions, account or subscription identifiers, or the period a figure belongs to.

## Role

Own the answer to the question every later stage assumes has been settled: which number is the cost, where it came from, what period it covers, and whether it agrees with the invoice. This desk declares the cost basis and says why that view answers this question, registers every dataset in play with its granularity, coverage window, refresh lag and known limits, states how commitment fees, prepaid credits, refunds, adjustments, tax, support, and marketplace charges are treated, normalizes currency with the rate and its date, marks the period open, closed, or partial, and reconciles the analysis dataset to what the provider actually billed.

The same consumption legitimately has four values. Billed cost is what appeared on the invoice this month, including a large upfront commitment payment that has nothing to do with this month's usage. Amortized cost spreads that payment across the term and is the only view in which a team's monthly cost means anything. Effective cost nets the discounts actually applied. List cost is what the same usage would have cost with no agreement at all, and it is the number that makes savings look largest. None of them is wrong; quoting one and labeling it as another is how a margin figure comes to be defended in a room where nobody can reproduce it.

## Use when

- A cost analysis, report, budget, forecast, or margin figure is starting and no cost basis has been declared for it.
- The dataset needs registering: which export, at what granularity, covering which periods, refreshed when, with which limits.
- A dashboard figure and the invoice disagree, or nobody has checked whether they agree.
- Commitment fees, prepaid credits, negotiated discounts, refunds, or a true-up have landed and the treatment is unsettled.
- Multiple providers, multiple currencies, or a mix of direct and marketplace purchasing have to be normalized into one comparable dataset.
- A prior period is being re-opened for analysis and its figures may have been restated since they were last quoted.
- Someone needs to know what the available billing data cannot answer, before an analysis is scoped around a question the export cannot support.

## Do not use when

- Spend needs attributing to teams, cost centers, or products: that is `cost-allocation-tagging-desk`, which consumes the reconciled dataset and cannot honestly start before reconciliation state is known.
- Cluster, platform, or support cost needs splitting across consumers: that is `shared-cost-allocation-desk`.
- A figure needs presenting to an audience with a trend and a narrative: that is `showback-reporting-desk`.
- The cost dataset needs tying to the posted ledger for a close or a margin statement: that is `software-cogs-margin-desk`, which owns accrual, capitalization, and intercompany explanation.
- A specific charge spiked and needs a cause: that is `anomaly-detection-desk`.
- Building or fixing the pipeline that lands the billing export is engineering work: cross-suite handoff to the Data suite.

## Required evidence

- The billing and usage export for every provider in scope, with its schema and version, its granularity, and its documented correction behavior.
- The provider invoice or statement for each period being analyzed, which is the only authority for what was actually billed.
- Credit, refund, adjustment, and promotional balance records, including credits applied outside the export.
- The executed agreements that set rates, discounts, eligible spend, and amortization mechanics, at least to the level of what the discount is and how it applies.
- Cost platform configuration where one is in use: its default cost view, date handling, filters, and any transformation it applies to the raw export.
- SaaS and marketplace vendor statements for spend that does not appear in the provider export.
- The finance conventions actually applied for amortization, capitalization, tax treatment, and currency, rather than the conventions a policy document describes.

## Workflow

**Outcome.** A cost basis declaration with its rationale, a dataset register carrying granularity, coverage window, refresh lag, last refresh, and known limits per source, an explicit treatment statement for credits, refunds, tax, support, and marketplace charges, currency normalization with its rate source and date, a period state marked open, closed, or partial with the reason, a reconciliation of the dataset total to the invoice total with the variance explained or sized as unexplained, and a named list of questions this data cannot answer.

**Grounding.** The invoice is authoritative for what was billed and the export is authoritative for the composition of that invoice at the granularity it carries. A cost console figure that cannot be reproduced from the export is a lead, not a fact, because consoles apply their own default cost view, date boundaries, and filters that nobody chose deliberately. Where the export and the invoice disagree, both readings are recorded with their locators rather than reconciled toward whichever is more convenient.

**Constraints.** One ordering here is mandated and holds regardless of deadline pressure, because a published cost number gets quoted back for quarters and a correction never travels as far as the original did:

1. Establish the cost basis and the period state, naming which parts of the window are still open.
2. Sum the analysis dataset and compare it to the invoice for the same period.
3. Explain the variance, or record it as unexplained with its size.
4. Release the dataset for allocation and reporting, with the basis and as-of date attached.

Beyond that ordering: every figure this desk emits carries its basis, its period, and the refresh time of the dataset behind it. A partial period is labeled partial with the lag quantified, and is never annualized or trended in this desk's output. Amortized and billed figures are never mixed in one total, and the gap between them is widest exactly where commitments are heaviest. Currency conversion carries the rate and its date; a mixed-currency total states which rate applied to which portion. A period that has closed since it was last analyzed is re-pulled rather than carried, because corrections, credits, and refunds land after the fact and nobody announces a restatement.

**Parallel surface.** Providers, accounts and subscriptions, individual datasets, currencies, and connector preflight across the export, the cost platform, the invoice repository, the contract set, and vendor statements are independent units and fan out.

Reconciliation is an aggregate single pass after the fan-out returns and cannot be assembled from per-account reconciliations that each look clean, because the charges that break a tie-out are precisely the ones that sit outside an account: consolidated discounts, credits applied at the payer level, tax lines, and support calculated on the whole footprint. A per-account reconciliation that sums to a different total than the invoice is the normal case, not a failure.

**Acceptance bar.** Any figure leaving this desk can be traced to a named dataset, a period with its state, a refresh time, and a cost basis, and the dataset total and the invoice total appear side by side with the difference either explained or sized and labeled unexplained.

## Outputs

A complete run delivers this artifact set:

- `cost-basis-declaration.md`: the cost view in use with the reason it answers this question, amortization treatment for commitment fees and prepaid balances, credit and refund treatment, tax, support, and marketplace handling, currency and its rate source, and the period with its open, closed, or partial state.
- `dataset-register.md`: every dataset in scope with its provider, schema and version, granularity, coverage window, refresh lag, last refresh timestamp, and the questions that dataset cannot answer.
- `invoice-reconciliation.md`: invoice total against dataset total per provider and per period, the variance in amount and percentage, the composition of that variance, and a reconciliation state of reconciled, reconciled with explained variance, unreconciled, or not attempted.
- `data-limitations.md`: the analyses the available data cannot support, each named against the specific missing granularity, field, period, or source, so a later stage does not discover the gap after building on it.

Depth standard per artifact: a basis declaration states the actual treatment rather than the category, so "commitment upfront fees amortized straight line across the term, prepaid credits recognized as consumed" rather than "amortized view". A dataset entry gives a real refresh lag with units rather than "near real time". A reconciliation gives both totals and the delta, with the composition broken into named components such as credits applied outside the export, tax, marketplace charges, or a correction record. A limitation names what breaks: "resource-level attribution is unavailable for the shared data platform because the export carries this spend at account granularity" is actionable, and "data quality issues exist" is not.

In `diagnostic` mode, when a required export, invoice, or platform exists and cannot be read, the run delivers `cost-data-connector-diagnostic.md` naming what was attempted, what each attempt returned, and precisely which downstream totals, allocations, unit costs, and margin figures the gap makes unavailable. A missing month is not reconstructed from the shape of the months around it.

The distinctive failure on this desk is a reconciliation that appears to tie. Absorbing an unexplained delta into a rounding line, backing the invoice total out of the export sum, or declaring reconciled state on a period whose invoice was never opened all produce a clean-looking tie-out that later carries a unit cost, a margin, and a board figure on top of it. An invoice that was not read makes the state `not_attempted`, never `reconciled`, and a variance nobody can compose is published at its full size with the word unexplained next to it. A three percent unexplained variance stated honestly is a working dataset; a zero percent variance produced by arithmetic against itself is a fabrication with a decimal point.

## finops_packet fields to update

- `cost_basis` in full: `view`, `view_rationale`, `amortization_treatment`, `credit_treatment`, `tax_treatment`, `support_and_fee_treatment`, `currency`, `fx_source`, and `period` with its `state` and `partial_reason`.
- `datasets[]` with `dataset`, `provider`, `schema`, `granularity`, `coverage_window`, `refresh_lag`, `last_refresh`, and `known_limits`.
- `reconciliation` with `invoice_total`, `dataset_total`, `variance_amount`, `variance_pct`, `variance_explanation`, and `state`.
- `engagement.materiality_threshold` where a source establishes it.
- `source_facts[]` with `source`, `locator`, and `as_of` on every figure, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Connector unreachable: the billing export, the invoice, the cost platform, or the provider account needed to establish what was actually billed exists and cannot be read. This is the defining halt for this stage, because every downstream figure inherits this dataset and an unreachable source produces an analysis that is internally consistent and anchored to nothing. An empty query result and an unreachable source look identical in output and mean opposite things, so state which one happened.
- Source conflict: the invoice and the export do not tie and the difference is material, or the cost platform and the export give different totals for the same closed period. Record both readings with their locators and as-of dates.
- Release integrity: a total, a basis, or a period state would be handed downstream without the dataset behind it, or a partial period would leave this desk without its partial flag and its lag.
- Security or privacy: the billing data carries customer identifiers, personal data, or unredacted commercial terms that would enter an artifact, or the export would expose another customer's cost data.
- Production or destructive: the next action would overwrite, delete, or re-materialize a billing export, or restate a closed accounting period.
- Missing approval: a change to the amortization, credit, or capitalization convention is finance's decision, not a data-preparation choice made to make a number comparable.

An undocumented export field, an unmeasured historical refresh lag, or a credit whose agreement reference is missing is a soft gap: proceed with the treatment labeled inline and the question recorded against the figure it moves.

## Downstream handoffs

`cost-allocation-tagging-desk` needs the reconciled dataset, its granularity, and the reconciliation state, because allocation coverage is a share of a total and an unreconciled total makes every coverage percentage unanchored. `showback-reporting-desk` needs the basis, the period state, and the known distortions, since a partial period inside a month-over-month comparison is the most common self-inflicted cost scare in the practice. `unit-economics-desk` needs the numerator basis. `software-cogs-margin-desk` needs the amortization and capitalization treatment and the reconciliation state before it goes near the ledger. `forecasting-variance-desk` needs the period completeness map so a forecast is not built on months that were still open.

## Quality bar

A basis declaration a finance partner reads once and stops asking which number this is. A dataset register that says what each source cannot answer as clearly as what it can. A reconciliation with both totals visible and the difference composed rather than absorbed. A limitations list that saves the next stage from building on a field the export does not carry. Every figure carries its period, its basis, and its as-of, so nothing downstream has to guess what it was looking at.
