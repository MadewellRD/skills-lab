---
name: deal-review-desk
description: prepare internal deal reviews with risks, asks, commercial impact, approvals, and recommended decisions. use when {{AGENT}} needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Deal Review Desk

## Role

Prepare internal deal review artifacts with clear risks, asks, commercial impact, required decisions, and recommended next actions.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- opportunity record and forecast category
- stakeholder notes and open blockers
- commercial model or pricing context
- approval status and decision owner

## Workflow

**Outcome.** A deal review memo: the current deal state, the risks with their evidence, the specific executive asks, the commercial impact, a decision log, and the recommended next actions.

**Ordered gate (mandated — keep this order).** A stage, amount, close-date, or forecast-category change is recommended in the memo and executed only after the approval it requires — recommendation, then approval, then mutation. The order is mandated because these fields drive the forecast that leadership commits on; a field changed ahead of its approval silently rewrites a number other people have already reported.

**Constraints.** Carry the sales workflow packet forward and update it in place. The CRM opportunity record is primary for amount, stage, close date, and owner; deal notes explain risk but do not override explicit fields. Keep facts separate from recommendations throughout — an executive ask is only actionable if the reader can see which part is evidence and which is judgment. Never state a commercial impact figure that no source supports.

**Parallel surface.** Deals in the review set are independent — assemble the state, risks, asks, and commercial impact for each in parallel rather than one deal at a time. The portfolio roll-up, cross-deal risk themes, and the prioritization of executive asks are a single aggregate pass once every deal is assembled, because concentration risk and ask prioritization are properties of the whole set.

**Acceptance bar.** Every deal fact names its source and its recency, every risk names the evidence behind it and what would retire it, every ask names the decision owner and what is being asked for, and every recommendation is distinguishable from the facts it rests on. A commercial impact that cannot be quantified is stated as unquantified with the missing input named.

## Outputs

- deal review memo
- risk summary
- executive asks
- commercial impact
- decision log
- next actions

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

- **Approval** — a stage, amount, close-date, or forecast-category mutation is requested without approval, or an executive ask would commit discount, resources, or terms. Hard halt: these fields feed a forecast other people have already reported.
- **Production or destructive** — the request is to execute the field changes rather than to recommend them.
- **Security or privacy** — the memo would expose customer-confidential commercial terms or personal data to an audience beyond the review.
- **Source conflict** — deal amount, close date, forecast category, or owner genuinely conflicts across sources. Hard halt on mutating the field; present both readings in the memo with their sources and let the review resolve it. Do not reconcile a forecast-bearing field on your own judgment.
- **Release integrity** — a commercial impact figure or a deal verdict would be stated as established when the evidence cannot carry it.
- **Connector unreachable** — a required CRM, notes, or pricing source exists but cannot be read, so deal state cannot be established.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. An unknown approval owner is recorded as an open question naming the decision that needs one — the memo is still produced, and nothing requiring that approval is executed. A commercial impact that cannot be quantified is stated as unquantified with the missing input named, rather than estimated into the memo.

## Downstream handoffs

- qualification-desk
- pipeline-forecast-desk
- proposal-desk
- crm-update-desk

## Source hierarchy

- CRM opportunity state is primary for amount, stage, close date, and owner.
- Deal notes explain risk but do not override explicit fields without approval.
- Separate facts from recommendations.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
