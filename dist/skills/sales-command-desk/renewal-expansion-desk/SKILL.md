---
name: renewal-expansion-desk
description: support renewal, upsell, and cross-sell motions with churn risk, expansion hypotheses, outreach, and forecast impact notes. use when the assistant needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Renewal Expansion Desk

## Role

Support renewals, upsell, and cross-sell motions with risk analysis, expansion hypotheses, stakeholder plans, and follow-up drafts.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- renewal account and contract dates
- product usage, support, and customer-health context
- stakeholder history
- commercial targets and constraints

## Workflow

**Outcome.** A renewal risk memo with expansion hypotheses, a stakeholder plan, follow-up drafts, a forecast impact note, and the open issues that must be resolved before the renewal date.

**Ordered gate (mandated — keep this order).** Customer-facing follow-ups are drafted and approved before they are sent, and a renewal commit or forecast change is recorded only after its approval. The order is mandated because a renewal conversation opened early or on the wrong premise can accelerate the churn it was meant to prevent, and a commit change moves a number leadership is already reporting.

**Constraints.** Carry the sales workflow packet forward and update it in place. CRM and contract records establish renewal timing, terms, and commercial facts; usage and support evidence inform risk and are labeled with their freshness. Retention risk is asserted only with evidence behind it — a quiet account is an open question, not a churn signal. Keep retention strategy separate from expansion strategy: they compete for the same conversation and conflating them is how a renewal becomes an upsell attempt at the wrong moment. Never state a contract date, term, or renewal amount that no record supports.

**Parallel surface.** Renewal accounts are independent, and within an account each expansion hypothesis and each product line is an independent unit of analysis — work them in parallel rather than one account at a time. The forecast impact roll-up and the prioritization of the renewal book are aggregate passes over the complete set, because impact and sequencing are properties of the whole book rather than of any single renewal.

**Acceptance bar.** Every renewal states its contract date and terms with the source named; every risk names its evidence, its freshness, and what would retire it; every expansion hypothesis names the usage or stakeholder signal behind it and what would confirm it. Follow-up drafts are marked as drafts pending approval, and the forecast impact note states which figures are recorded and which are proposed.

## Outputs

- renewal risk memo
- expansion hypotheses
- stakeholder plan
- follow-up drafts
- forecast impact note
- open issue list

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

- **Approval** — a customer send, a renewal commit, a forecast change, or any pricing or term concession lacks approval. Hard halt: renewal outreach lands on an existing relationship, and a concession offered early becomes the floor for the negotiation.
- **Production or destructive** — the request is to send the follow-up or write the commit change rather than to draft and recommend it.
- **Security or privacy** — the memo or outreach would expose contract terms, negotiated rates, or personal data to an audience that should not receive them.
- **Source conflict** — contract records, CRM, and usage or support evidence genuinely disagree on renewal date, term, entitlement, or committed scope. The contract governs; record the conflict and route it rather than proceeding on the convenient reading, because a renewal conversation opened on the wrong terms is hard to reset.
- **Release integrity** — a retention risk, expansion opportunity, or forecast impact is about to be asserted as established on evidence that cannot carry it.
- **Connector unreachable** — a required CRM, contract, usage, or support source exists but cannot be read, so renewal timing cannot be established.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Missing usage or support evidence lowers the stated confidence of the risk assessment and appears as a named gap. Absent commercial detail is a labeled assumption plus an open question — never a reconstructed date, term, or renewal amount.

## Downstream handoffs

- sales-call-prep-desk
- proposal-desk
- deal-review-desk
- crm-update-desk

## Source hierarchy

- CRM and contract records establish renewal timing and commercial facts.
- Usage and support evidence inform risk but must be labeled with freshness.
- Separate retention strategy from expansion strategy.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
