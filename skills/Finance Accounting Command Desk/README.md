# Finance Accounting Command Desk

Source Markdown suite for accounting operations and financial planning. One orchestrator routes and runs; nineteen member desks own a real stage of the work.

The subject of this suite is the record of what the business actually did: what it earned, what it owes, what it holds, what it committed to, and what it expects next.

The suite covers the function end to end: chart of accounts and accounting policy, revenue recognition and deferred revenue, billing and order to cash, receivables and collections, spend approval and delegation of authority, payables and three way match, expense management, equity and cap table hygiene with stock compensation, month-end close, balance sheet reconciliations, tax provision and filings coordination, financial statements and board reporting, cash flow forecasting and runway, SaaS metrics such as ARR, retention, and burn, budgeting, reforecasting and scenarios, variance and flux analysis, internal controls, and audit support.

This suite prepares, analyses, and recommends. It does not post to the ledger, close or reopen a period, release a payment, issue a credit memo, write off a receivable, grant equity, file a return, or send statements outside the company. Those acts are prepared with their support, their amounts, and the authority each requires, and a named human authorizes them. Contract drafting goes to the Legal Contracts suite, sourcing to Procurement and Vendor Management, cloud cost modeling to FinOps, compensation structure to People and Talent, and system implementation to the SDLC suite.

## Desks in workflow order

- `finance-accounting-command-desk.md` (orchestrator)
- `accounting-policy-coa-desk.md`
- `revenue-recognition-desk.md`
- `billing-order-to-cash-desk.md`
- `accounts-receivable-collections-desk.md`
- `spend-approval-authority-desk.md`
- `accounts-payable-desk.md`
- `expense-management-desk.md`
- `equity-cap-table-desk.md`
- `month-end-close-desk.md`
- `account-reconciliation-desk.md`
- `tax-coordination-desk.md`
- `financial-reporting-desk.md`
- `cash-flow-treasury-desk.md`
- `saas-metrics-reporting-desk.md`
- `budget-planning-desk.md`
- `forecast-scenario-desk.md`
- `variance-analysis-desk.md`
- `internal-controls-desk.md`
- `audit-support-desk.md`

## How to start

Start at `finance-accounting-command-desk` and give it the question, the period and its status, the entities in scope, and where the answer is going. That last part sets the evidence bar: a management estimate and a figure headed for a lender certificate are the same schedule at two very different standards. The orchestrator classifies the request, enters at the right desk, and runs the stages the outcome requires rather than returning a routing note.

Enter a member desk directly when the stage is already known: a revenue memo for one non-standard order form, an aging with a collections plan, a bank reconciliation, a departmental variance explanation, a thirteen week cash forecast, an ARR bridge before a diligence request, or a support package for one audit sample.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `finance_packet`, the operating modes, request types, figure destination and period status, the source hierarchy, accounting discipline, the action boundary, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Most requests run a subsequence. A non-standard order form enters at revenue recognition, a customer who stopped paying enters at receivables, a board deadline enters at financial reporting and pushes backward into close, and an auditor request enters at audit support and pushes backward into whichever account it touches. The chain orders stages that consume each other's packet state. The transaction cycle desks work separate populations in separate subledgers and converge at close, while the consolidated trial balance, intercompany eliminations, the deferred revenue waterfall, the ARR bridge, the consolidated cash forecast, and materiality are single passes over the whole set.

Four orderings in this suite are not negotiable and are documented with their reasons in the orchestrator: the close sequence from cutoff through distribution, approval before commitment before receipt before match before payment, contract before billing before recognition, and board consent before grant before expense.
