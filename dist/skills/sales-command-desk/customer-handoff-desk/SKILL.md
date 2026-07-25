---
name: customer-handoff-desk
description: prepare post-sale handoff packages for onboarding, customer success, support, or implementation teams. use when the assistant needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Customer Handoff Desk

## Role

Prepare complete post-sale handoff packages that preserve customer goals, promised outcomes, scope, risks, owners, and next actions.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- closed-won opportunity
- account and stakeholder context
- scope and commercial terms
- proposal/order-form files
- risks, dependencies, and timeline

## Workflow

**Outcome.** A post-sale handoff package: the customer summary and their goals, the committed scope, the promised deliverables, the open risks, the owner and action list, and a DOCX/PDF-ready artifact the receiving team can work from.

**Ordered gate (mandated — keep this order).** Confirm closed-won state against the signed commercial artifact before the package asserts any committed scope, and route any CRM note or task write through the dry-run diff and approval sequence before it is written. The order is mandated because a handoff package is the document onboarding, support, and delivery plan against: committed scope stated ahead of the signature triggers real spend against a deal that may still change, and it hands the customer expectations nobody agreed to.

**Constraints.** Carry the sales workflow packet forward and update it in place. Signed commercial artifacts and the CRM define committed scope; proposal files and meeting notes provide context and do not alter commitments. A promise made in a call but absent from the signed artifact is surfaced as an unresolved commitment with its source, never quietly promoted into scope or quietly dropped. Never invent a deliverable, date, owner, or contractual term.

**Parallel surface.** Where several accounts are being handed off, each is independent, and within a package the individual promised deliverables, open risks, and workstreams are independently assembled — work them in parallel. Reconciling the promised-deliverable set against the signed commercial artifact is deliberately an aggregate pass over the complete set, because the failure it catches — a commitment that appears in notes or the proposal but not in the contract — is a gap between two lists and cannot be detected one item at a time.

**Acceptance bar.** Every committed deliverable cites the signed artifact or contract clause that carries it; every unresolved commitment is listed separately with its source and its status; every risk and action names an owner and a date or an explicit gap. The package states the deal state it was built from, and a reader in onboarding can tell what was sold apart from what was discussed without going back to the seller.

## Outputs

- handoff brief
- customer summary
- open risks
- promised deliverables
- owner/action list
- DOCX/PDF-ready package

## Workflow packet fields

- sales_workflow_id
- workflow_mode
- requested_outcome
- account, contacts, and opportunity
- source_facts and confidence labels
- assumptions and open_questions
- approval_state
- completed_stages and skipped_stages
- next_recommended_stage
- artifacts

## Halt conditions

Proceed by default on reversible work and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — a CRM note or task write, or any customer-facing send of the handoff material, lacks approval.
- **Production or destructive** — the request is to write to the CRM, notify the customer, or trigger onboarding rather than to prepare the package.
- **Security or privacy** — the package would carry contract terms, pricing detail, or personal data to a receiving team that should not have them.
- **Source conflict** — the signed commercial artifact, the proposal, and the meeting notes genuinely disagree on scope or promised deliverables. Hard halt: the signed artifact governs, and a conflict here is exactly what the handoff exists to surface. List both versions with their sources and route the discrepancy; never reconcile a commitment conflict silently in either direction.
- **Release integrity** — the package would assert committed scope for an opportunity that is not closed-won. Hard halt: a handoff read as final triggers real onboarding spend and sets customer expectations against a deal that may still change. Where a provisional package is genuinely wanted, mark the deal state on every page and label the scope as not yet committed.
- **Connector unreachable** — a required CRM, contract, or proposal source exists but cannot be read, so committed scope cannot be established.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A missing handoff owner is an open question at the top of the package naming the role that must be assigned — the package is still produced so the receiving team is not waiting on an org decision. Missing risk or timeline detail is a named gap, never a reconstructed commitment.

## Downstream handoffs

- crm-update-desk
- renewal-expansion-desk
- customer-success handoff if available

## Source hierarchy

- Signed commercial artifacts and CRM define committed scope.
- Proposal files and notes support context but must not alter commitments.
- Surface unresolved commercial, technical, or onboarding risks.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
