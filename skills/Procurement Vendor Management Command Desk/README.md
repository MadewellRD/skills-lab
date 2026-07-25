# Procurement Vendor Management Command Desk

Source Markdown suite for procurement and vendor management. One orchestrator routes and runs; eighteen member desks own a real stage of the work.

The subject of this suite is the commitment: what the company has agreed to buy, from whom, on what terms, carrying what risk, for how long, and whether anyone can still change it.

The suite covers the function end to end: procurement policy and buying channels, intake and requisition, third-party risk tiering, category strategy, requirements and statements of work, supplier discovery, sourcing events including RFP, RFQ, and reverse auction, bid evaluation and weighted scoring, security and privacy review coordination, integrity and sanctions screening, should-cost modeling and negotiation, contract approval and signature routing, vendor onboarding and provisioning, supplier performance and service level review, relationship governance and concentration risk, spend analysis and savings realization, renewals and consolidation, and offboarding with data return and deletion.

This suite prepares, analyses, and recommends. It does not issue a sourcing document, communicate an award or a price to a supplier, sign an agreement, issue a purchase order, create or change a vendor's bank details, grant a vendor access to systems or data, waive a security requirement, serve a termination notice, or release a final payment. Those acts are prepared with their evidence, their amounts, and the authority each requires, and a named human authorizes them. Contract drafting and disputes go to the Legal Contracts suite, the substance of a security assessment to the Security suite, data protection assessments to the Privacy and Data Protection suite, the third-party risk program to GRC, purchase orders and savings recognition to Finance and Accounting, and cloud commitment portfolios to FinOps.

## Desks in workflow order

- `procurement-vendor-management-command-desk.md` (orchestrator)
- `procurement-policy-desk.md`
- `intake-triage-desk.md`
- `vendor-risk-tiering-desk.md`
- `category-strategy-desk.md`
- `requirements-specification-desk.md`
- `supplier-discovery-desk.md`
- `sourcing-event-desk.md`
- `bid-evaluation-desk.md`
- `security-privacy-review-desk.md`
- `supplier-integrity-screening-desk.md`
- `pricing-negotiation-desk.md`
- `contract-execution-routing-desk.md`
- `vendor-onboarding-provisioning-desk.md`
- `supplier-performance-sla-desk.md`
- `supplier-relationship-governance-desk.md`
- `spend-analysis-desk.md`
- `renewal-consolidation-desk.md`
- `vendor-offboarding-desk.md`

## How to start

Start at `procurement-vendor-management-command-desk` and give it the need, the value as both annual and total contract value, the data the supplier would touch, and where the request sits against the clock. That last part sets everything else: the same renewal conversation is a negotiation while the notice window is open and an invoice after it closes. The orchestrator classifies the request, enters at the right desk, and runs the stages the outcome requires rather than returning a routing note.

Enter a member desk directly when the stage is already known: a risk tier for a proposed tool, an evaluation scorecard for a bid set, a should-cost model before a negotiation, a security review status summary, a category spend baseline, a renewal position with its notice deadline, or an exit plan for a supplier being replaced.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `procurement_packet`, the operating modes, request types, commitment class and leverage window, the source hierarchy, procurement discipline, the action boundary, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Most requests run a subsequence. A renewal that just surfaced enters at renewals and pushes backward into performance and pricing, a cost reduction target enters at spend analysis and pushes forward into consolidation, and a tool a team already signed for enters at intake as a policy exception. Risk tiering sits early because the tier is a property of the use case rather than of the supplier, and it sets the diligence lead time the whole timeline has to accommodate. The diligence desks fan out over separate evidence and converge before negotiation, while bid comparison, consensus scoring, category fragmentation, supplier concentration, and the renewal calendar are single passes over the whole set.

Four orderings in this suite are not negotiable and are documented with their reasons in the orchestrator: publish the criteria before taking bids and score independently before consensus, tier before diligence before signature, compute the notice deadline from the executed document and act inside the window, and extract the data before deprovisioning before certifying deletion before final settlement.

Authoring convention: suite folders are human-readable product taxonomy, desk files are kebab-case and end in `.md`, and packaged {{AGENT}} skill folders are generated artifacts rather than the primary authoring structure.
