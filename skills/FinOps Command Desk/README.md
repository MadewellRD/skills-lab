# FinOps Command Desk

Source Markdown suite for cloud financial management. One orchestrator routes and runs; nineteen member desks own a real stage of the work.

The subject of this suite is what the technology estate costs, who consumed it, what the organization got for the money, and which of those costs can be reduced without breaking something that earns revenue.

The suite covers the function end to end: billing data ingestion and invoice reconciliation, tagging and cost allocation, shared and container cost splits, showback reporting, unit economics, software cost of revenue and gross margin, budgets, forecasting and variance analysis, anomaly detection and root cause, rightsizing, waste elimination, cost-aware architecture, commitment and reservation strategy, SaaS and license spend, provider negotiation inputs, the optimization backlog with savings realization, engineering cost reviews, chargeback and internal billing, and practice maturity assessment.

This suite analyses, models, and recommends. It does not purchase a commitment, terminate or resize a running resource, post to the ledger, publish a chargeback, set a budget of record, or send anything to a vendor. Those acts are prepared with their evidence and their downside, and a named human authorizes them. Changes to the estate itself go to the Cloud Infrastructure suite, the paper on a provider agreement goes to the Legal Contracts suite, sourcing goes to Procurement and Vendor Management, and the financial close goes to Finance and Accounting.

## Desks in workflow order

- `finops-command-desk.md` (orchestrator)
- `cost-data-ingestion-desk.md`
- `cost-allocation-tagging-desk.md`
- `shared-cost-allocation-desk.md`
- `showback-reporting-desk.md`
- `unit-economics-desk.md`
- `software-cogs-margin-desk.md`
- `budget-planning-desk.md`
- `forecasting-variance-desk.md`
- `anomaly-detection-desk.md`
- `rightsizing-desk.md`
- `waste-elimination-desk.md`
- `cost-aware-architecture-desk.md`
- `commitment-portfolio-desk.md`
- `licensing-saas-spend-desk.md`
- `cloud-commercial-negotiation-desk.md`
- `optimization-backlog-desk.md`
- `engineering-cost-review-desk.md`
- `chargeback-invoicing-desk.md`
- `finops-maturity-desk.md`

## How to start

Start at `finops-command-desk` and give it the question, the period, the providers and accounts in scope, and what the answer is for. That last part sets the evidence bar: an exploratory figure and a figure that goes in a board pack are the same analysis at two different standards. The orchestrator classifies the request, enters at the right desk, and runs the stages the outcome requires rather than returning a routing note.

Enter a member desk directly when the stage is already known: a tag coverage report before an allocation project, a rightsizing candidate list for one service, a commitment coverage snapshot before a renewal, one anomaly that needs a root cause, or a unit cost for a pricing conversation.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `finops_packet`, the operating modes, request types, decision class and period state, the source hierarchy, measurement discipline, the action boundary, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Most engagements run a subsequence. A bill that jumped overnight enters at anomaly detection, a margin question enters at cost of revenue and margin, an expiring commitment enters at the commitment portfolio, a chargeback dispute enters at chargeback and pushes backward into allocation. The chain orders stages that consume each other's packet state. Rightsizing, waste, architecture, and licensing consume the same data without consuming each other, so they run at once and converge into one deduplicated opportunity set, while reconciliation to the invoice, allocation coverage, net savings after overlap, the chargeback ledger, and commitment sizing are single passes over the whole estate.

Two orderings in this suite are not negotiable and are documented with their reasons in the orchestrator: reconcile before publishing a figure, and optimize before sizing a commitment. The second exists because commitments generally cannot be cancelled, so committing against unoptimized usage locks the waste in for the full term and penalizes every optimization that follows.
