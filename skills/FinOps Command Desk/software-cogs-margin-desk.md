---
name: software-cogs-margin-desk
description: classify infrastructure and vendor spend into cost of revenue against research and internal cost, and compute software gross margin that ties to the ledger. covers the cost of revenue classification policy applied line by line, capitalized internal-use software development cost with its project basis, gross margin with its revenue basis stated, margin by product or service line, the variance between the cost dataset and the posted general ledger with its accrual timing and intercompany explanation, period state and who owns the close, and reclassification proposals prepared for the controller.
---

# Software Cogs Margin Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite and is the point where cost analysis meets the financial statements. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the line it affects and recorded in `open_questions`. Never invent revenue figures, margin percentages, ledger balances, capitalized amounts, classification rules, journal references, or the identity of the controller who owns a close.

## Role

Own the classification that decides which infrastructure and vendor spend is cost of revenue and which is not, and the margin that follows from it. This desk applies the organization's cost of revenue policy line by line with the rule behind each call, identifies capitalized internal-use software development cost against the project it belongs to, computes gross margin with its revenue basis stated, cuts margin by product or service line where the structure supports it, explains the variance between the cost dataset and the posted ledger through accrual timing, capitalization, and intercompany treatment, and prepares reclassification proposals for the controller rather than applying them.

The judgment that matters here is that the same charge can be cost of revenue or operating expense depending on what it serves, not on what service it is. A managed database serving production tenants is cost of revenue. The identical database in a research environment is not. A logging platform is split by which environments it observes. A charge that lands in a shared account serves both, and how it is split is an accounting position rather than an allocation preference. Moving a line between cost of revenue and research changes gross margin, which investors track, which makes it an accounting decision wearing an infrastructure costume.

## Use when

- Gross margin needs computing or explaining, and the cost side has to come from the cloud and vendor data.
- Cost of revenue classification is being built, revised, or challenged for infrastructure and vendor spend.
- The cost dataset and the posted ledger disagree and somebody needs the reconciliation before a close.
- Capitalized development cost needs identifying against projects, or the capitalization treatment of infrastructure used during development is in question.
- Margin by product line, service line, or plan tier is being asked for and the allocation has to support it.
- A funding, board, audit, or diligence process needs an infrastructure cost story that stands up to the ledger.
- A reclassification is being proposed and needs to reach the controller with its rule, its amount, and its margin effect attached.

## Do not use when

- The cost dataset does not reconcile to the invoice: that is `cost-data-ingestion-desk`, whose amortization and credit treatment this desk inherits rather than re-decides.
- The question is a unit cost or a per-tenant figure rather than a financial statement line: that is `unit-economics-desk`.
- Allocation coverage or shared splits are unsettled: those are `cost-allocation-tagging-desk` and `shared-cost-allocation-desk`, and a margin built on a large unexplained residual is a margin with an unquantified error.
- Cost centers need charging and statements issuing: that is `chargeback-invoicing-desk`.
- The question is next year's spend plan: that is `budget-planning-desk`.
- The close itself, revenue recognition, statutory reporting, or the journal entries: cross-suite handoff to the Finance and Accounting suite. This desk supplies the cost classification and the allocation evidence behind it.

## Required evidence

- The allocated cost dataset with its reconciliation state, cost basis, and amortization treatment.
- The revenue figure with its source and its recognition basis, from finance rather than from a dashboard.
- The cost of revenue classification policy as the organization actually applies it, including the treatment of support, delivery, and customer-facing infrastructure.
- The internal-use software capitalization policy and the projects currently being capitalized, with their phase.
- The general ledger extract for the period, at the account level the classification maps to.
- Period state and the controller who owns the close, since a closed period changes what is possible rather than merely what is convenient.
- Product and service line structure, and whether the allocation supports cutting margin by it.
- Prior period classifications, because consistency across periods is itself an accounting requirement and an unexplained change in treatment is an audit finding.

## Workflow

**Outcome.** A line-by-line classification of infrastructure and vendor spend into cost of revenue against research, internal, and sales-facing cost with the policy rule behind each call, capitalized development cost identified against its project and phase, gross margin computed with its revenue basis named, margin by product or service line where the structure supports it, a reconciliation of the cost dataset to the posted ledger with its accrual, timing, capitalization, and intercompany explanation, and reclassification proposals prepared with their margin effect quantified.

**Grounding.** The ledger is authoritative for what was recognized, in which period, against which account, and it is what an auditor reads. The cost dataset is authoritative for composition and granularity. These disagree routinely and legitimately through accrual timing, capitalization, credits recognized differently, and intercompany treatment, so the reconciliation explains the difference rather than adjusting one to match the other. The classification policy is authoritative for where a line lands; where the policy is silent, the line is unclassified and the question goes to the controller.

**Constraints.** One ordering is mandated and holds regardless of deadline pressure, because a posted period is audit-visible and unwinding one involves more people than the reclassification was worth:

1. Confirm the period state and the controller who owns it, before the analysis is designed rather than after it is finished.
2. Classify against the written policy, recording every line the policy does not decide as unclassified.
3. Quantify the margin effect of each proposed reclassification.
4. Take the proposal to the controller, who decides whether it posts and in which period.

Beyond that ordering: classification follows what the spend serves rather than what the service is called, and the rule that placed each line is recorded next to it. A line the policy does not decide stays unclassified with the question attached, never assigned to the side that produces a better margin. Consistency with prior periods is preserved, and any change in treatment is called out with its effect, because an unexplained classification change is exactly what a reviewer looks for. Capitalization follows the policy's phase criteria and is attributed to a named project; infrastructure consumed by capitalized development work is treated per policy rather than by analogy. Gross margin states its revenue basis, since a margin computed against recognized revenue, billed revenue, and annualized recurring revenue are three different numbers that are quoted interchangeably. Every figure carries its period state, and a margin computed on an open period says so.

**Parallel surface.** Product lines, service lines, individual cost categories, vendor spend items, and per-project capitalization analysis are independent units and fan out, as does connector preflight across the cost dataset, the ledger extract, the policy documents, and the revenue source.

The aggregate runs once after the fan-out returns. Gross margin is a whole-set figure and cannot be assembled from per-product margins, because shared and unallocated cost has to land somewhere before the total means anything. The ledger reconciliation is a statement about the full period, since the differences that break a tie-out are accruals and intercompany entries that exist only at the entity level. The residual from allocation is the same shape: it distorts every product margin proportionally and has to be sized once.

**Acceptance bar.** Every classified line names the policy rule that placed it, every unclassified line names the question and its amount, gross margin states its revenue basis and period state, and the difference between the cost dataset and the posted ledger is explained by named components or carried at its full size as unexplained.

## Outputs

A complete run delivers this artifact set:

- `cogs-classification.md`: each material cost line with its classification, the policy rule that placed it, the environment or workload evidence behind that call, and the lines the policy does not decide, listed as unclassified with their amounts.
- `capitalized-development-cost.md`: capitalized amounts by project and phase, the policy criteria applied, the infrastructure consumed by capitalized work, and the treatment questions the policy leaves open.
- `gross-margin-statement.md`: cost of revenue, the revenue figure with its basis and source, computed margin, period state, and the movement against the prior period with its drivers.
- `margin-by-product-line.md`: margin per product or service line where the allocation supports it, with the shared cost treatment stated and the lines the allocation cannot yet support named rather than estimated.
- `ledger-variance-reconciliation.md`: cost dataset against posted ledger, with the variance decomposed into accrual timing, capitalization, credit recognition, intercompany treatment, and anything unexplained carried at full size.
- `reclassification-proposals.md`: each proposal with the line, the current and proposed treatment, the policy basis, the amount, the margin effect, the period it would affect, and the controller it needs.

Depth standard per artifact: a classification entry cites the policy provision, not the intuition, and names the evidence that establishes what the spend serves. A capitalization entry names the project and the phase criterion. A margin figure shows cost of revenue, revenue, and the arithmetic between them. A variance entry gives an amount per component rather than a narrative about why the two systems differ. A proposal states its margin effect in basis points or currency, because that is the number the controller is actually deciding about.

In `diagnostic` mode, when the ledger extract, the revenue figure, or the classification policy exists and cannot be read, the run delivers `cogs-margin-connector-diagnostic.md` naming what was attempted and which classifications, margins, and reconciliations that leaves unavailable. A margin is not computed against a revenue figure taken from a dashboard when the finance source is unreachable.

The failure this desk exists to prevent is the classification that resolves an ambiguity in the direction of a better number. Cost of revenue judgments are genuinely hard at the edges, and every hard call has a version that improves gross margin. Once a line moves, the margin travels into a board pack, a diligence room, and eventually a statement an auditor tests, and by then the reasoning is a sentence nobody wrote down. A line the policy does not clearly place is recorded as unclassified with its amount and the specific question, and an unclassified pool of two percent presented honestly is a working paper the controller can close in an afternoon. A margin percentage that no ledger supports is not produced at all, and a variance nobody can compose stays visible at its full size with the word unexplained beside it, because a reconciliation that closes to zero through a plug is the single artifact in this suite most likely to become an audit finding.

## finops_packet fields to update

- `cogs.classification_policy_ref`, `cogs.cogs_lines`, `cogs.excluded_lines` with the rule behind each.
- `cogs.capitalization` with `policy_ref`, `capitalized_amount`, and `basis`.
- `cogs.cogs_amount`, `cogs.revenue_basis`, `cogs.gross_margin_pct`.
- `cogs.period_state`, `cogs.controller_owner`, `cogs.ledger_variance` with its explanation.
- `governance.approvals[]` for every reclassification, capitalization judgment, or restatement, with `required_approver`, `authority_basis`, and `state`.
- `source_facts[]` with `locator` and `as_of` for every ledger and revenue figure, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: a reclassification, a capitalization judgment, or any change touching a closed period. This is the defining halt for this stage. Cost of revenue and margin are reported externally, the controller owns the close, and a classification change is an accounting decision regardless of how clearly the infrastructure evidence points.
- Production or destructive: the next action would post a journal entry, edit a posted allocation, backdate a treatment, or restate a closed accounting period. The ledger is the record; a corrected copy finance never posted is a second set of books.
- Source conflict: the cost dataset and the ledger disagree materially on a closed period, or two revenue figures with different bases are in circulation for the same period. Record both readings with their locators.
- Release integrity: a margin, a cost of revenue figure, or a capitalized amount would leave the practice without the ledger behind it, without its revenue basis stated, or computed on an open period presented as final.
- Security or privacy: the analysis would place customer-level revenue, individual contract terms, or unreleased financial results into an artifact whose audience has not been cleared for them. Pre-release margin figures are material non-public information.
- Connector unreachable: the ledger extract, the revenue source, or the classification policy cannot be read. State whether the source was empty or unreachable.

An undocumented rationale for a prior period's classification, a missing project reference on a small capitalized item, or an unconfirmed product line mapping is a soft gap: proceed with it labeled against the line it affects and the question routed to the controller.

## Downstream handoffs

`budget-planning-desk` needs the classification, because a budget built without knowing which lines are cost of revenue cannot be reconciled to a margin plan. `forecasting-variance-desk` needs the margin sensitivity and the classification boundaries, so a spend forecast can be expressed as a margin trajectory. `unit-economics-desk` receives the classification boundary so that a per-unit cost and a cost of revenue figure use compatible scopes. `chargeback-invoicing-desk` needs the cost center mapping the ledger uses. The Finance and Accounting suite receives the reclassification proposals, the capitalization schedule, and the ledger variance for the close itself.

## Quality bar

Every classification cites a policy rule and the evidence about what the spend serves. Unclassified lines are visible with amounts and questions rather than resolved quietly. Capitalization names projects and phases. Margin states its revenue basis and its period state. The ledger variance is decomposed into named components with any remainder shown at full size. Reclassification proposals reach the controller with the margin effect quantified, ready to be decided rather than requiring the analysis to be redone.
