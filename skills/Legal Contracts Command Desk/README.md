# Legal Contracts Command Desk

Source Markdown suite for commercial contracting. One orchestrator routes and runs; nineteen member desks own a real stage of the work.

The subject of this suite is enforceable text: what the organization has actually agreed to, on whose paper, under whose authority, against which legal entity, and what obligations that creates for as long as the agreement stays in force.

The suite covers the function end to end: intake and triage, counterparty entity diligence and signing authority, clause playbooks with fallback ladders and walk-away lines, NDAs, drafting on approved templates, MSA and SaaS commercial terms, risk allocation across caps, indemnities, warranties and insurance, data processing terms, security exhibits, IP and licensing, open source license review, regulatory flow-down, redlining and negotiation positions, approval routing under the delegation of authority, signature and execution, obligation extraction, repository and CLM hygiene, renewal and termination notices, and dispute intake with legal holds.

This suite prepares work for a lawyer and a business owner. It does not sign, send, waive, release, settle, or issue legal advice of record. Compliance obligations that a contract creates go to the GRC suite for control mapping and evidence. Privacy assessments and data subject rights go to the Privacy suite. Technical assessment of a counterparty's security posture goes to the Security suite. Sourcing, vendor selection, and spend go to the Procurement and Vendor Management suite.

## Desks in workflow order

- `legal-contracts-command-desk.md` (orchestrator)
- `contract-intake-triage-desk.md`
- `counterparty-diligence-desk.md`
- `clause-playbook-desk.md`
- `nda-confidentiality-desk.md`
- `contract-drafting-desk.md`
- `commercial-terms-desk.md`
- `risk-allocation-desk.md`
- `data-protection-terms-desk.md`
- `security-exhibit-desk.md`
- `ip-licensing-desk.md`
- `open-source-license-desk.md`
- `regulatory-flowdown-desk.md`
- `redline-negotiation-desk.md`
- `approval-escalation-desk.md`
- `signature-execution-desk.md`
- `obligation-extraction-desk.md`
- `contract-repository-desk.md`
- `renewal-termination-desk.md`
- `dispute-claims-desk.md`

## How to start

Start at `legal-contracts-command-desk` and give it the document, the counterparty, whose paper it is, whether the organization is the customer or the supplier, and the outcome you need. The orchestrator classifies the matter, enters at the right desk, and runs the stages the outcome requires rather than returning a routing note.

Enter a member desk directly when you already know the stage: an NDA turn before a first call, a liability position before an escalation, a subprocessor comparison for a security review, an obligation register from an agreement signed last year, or a notice window that closes in three weeks.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `legal_packet`, the operating modes, matter types, posture and paper, the source hierarchy, drafting and reading discipline, the action boundary, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Most matters run a subsequence of the chain. A signed agreement needing a summary enters at obligation extraction, an inbound vendor package enters at counterparty diligence, an auto-renewal enters at renewal and termination, a breach notice enters at dispute intake and pushes backward into the repository. The chain orders stages that consume each other's packet state. The seven review lanes between commercial terms and regulatory flow-down consume the same draft without consuming each other, so they run at once and converge into one issues list, while order of precedence across a family, the ranked issues list, the concession log, aggregate exposure across a counterparty, and the approval package are single passes over the whole set.
