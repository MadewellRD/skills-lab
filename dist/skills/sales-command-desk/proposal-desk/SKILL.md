---
name: proposal-desk
description: create customer-facing proposal, scope, deck, docx, and pdf drafts with brand, pricing, and approval controls. use when the assistant needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Proposal Desk

## Role

Create customer-facing proposals, scopes, and commercial response packages from verified opportunity context and approved templates.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- opportunity context and customer objectives
- pricing inputs and commercial constraints
- required proposal sections
- brand or template rules
- target output format

## Workflow

**Outcome.** A proposal outline and draft in the requested format, with an artifact checklist, approval notes, open questions, and a handoff-ready package — a draft awaiting approval, never a document that has been sent.

**Ordered gate (mandated — keep this order).** Confirm pricing and scope against approved commercial terms, then complete the internal pricing, legal, and brand review, then obtain the named approver's authorization, and only then may the proposal be shared externally. Each step precedes the next. This order is mandated because a proposal that reaches a customer is a commercial position: a price cannot be un-quoted, a scope statement becomes the thing the customer expects, and withdrawing either costs trust or money. Never share externally to save a round trip.

**Constraints.** Carry the sales workflow packet forward and update it in place. CRM and user-provided commercial terms define scope; approved templates and brand rules control presentation. Never write a price, discount, term, SLA, delivery date, or customer reference that no approved source states — an unresolved commercial value stays visibly unresolved in the draft rather than being filled with something plausible. Proposal claims stay within verified opportunity, product, and pricing evidence.

**Parallel surface.** Proposal sections are independent drafting units — problem framing, proposed approach, scope, timeline, team, references, and terms can be written in parallel rather than front to back. The pricing table, the total commercial summary, the internal consistency check, and the approval package are aggregate passes over the complete document, because a commercial total is defined by all of the scope at once and a contradiction between the scope section and the terms section is only visible when they are read together.

**Acceptance bar.** Every commercial figure traces to an approved source or is visibly marked unresolved; every scope statement matches what the opportunity record and the approved terms support; the artifact meets the requested format and brand rules; and the approval package names the approver, the reviews that apply, and exactly what is awaiting authorization.

## Outputs

A complete run produces the whole proposal package, not the outline alone:

- proposal outline
- proposal draft
- artifact checklist
- approval notes
- open questions
- handoff-ready package

The outline is the structure of the draft, not a substitute for it. A run that stops at the outline has produced a plan for the deliverable rather than the deliverable.

Each artifact is done when the approver could review it as the document that would actually go out. Every section is written in the voice and format the customer will receive; every commercial figure traces to an approved source or is visibly marked unresolved; every scope statement matches what the opportunity record and the approved terms support; the approval notes name the approver, the reviews that apply, and exactly what awaits authorization. Headings over filler text are a failure here, and in a customer-facing document it is a failure that can escape the building.

A complete draft is still a draft. Writing every section does not share it externally — the confirm-terms, internal-review, approval, then-share order in Workflow holds, and a finished package is not authorization to send it to save a round trip. Completeness also does not license invention: a price, discount, term, SLA, delivery date, headcount, or customer reference that no approved source states stays visibly unresolved in the draft. A plausible price becomes a quoted price the instant the document reaches the customer, and it cannot be un-quoted. Proposal sections are independent drafting units inside the parallel surface declared in Workflow.

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

Proceed by default on drafting and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — external sharing is requested without approval, or the draft commits pricing, discount, terms, or scope that its named approver has not cleared. Hard halt: a proposal is a commercial position and a shared price cannot be un-quoted.
- **Production or destructive** — the request is to send, share, or publish the proposal rather than to draft it.
- **Security or privacy** — the proposal would include another customer's confidential detail, an unapproved reference, or security and contractual material not cleared for this audience.
- **Source conflict** — the CRM, the approved commercial terms, and the user's instructions genuinely disagree on price, scope, or duration. Do not resolve a commercial conflict by choosing; surface it to the approver, because the wrong resolution ships as a quote.
- **Release integrity** — a proposal claim exceeds verified opportunity, product, or pricing evidence. Remove it or mark it unresolved; never let an unverifiable promise reach a customer document.
- **Connector unreachable** — a required CRM, pricing, or template source exists but cannot be read, so the commercial baseline cannot be established.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Missing pricing or scope inputs produce a draft with those sections visibly marked unresolved and listed in the approval notes — never filled with a plausible figure. An unavailable brand template means drafting in a clean neutral structure and flagging that the template must be applied before sharing.

## Downstream handoffs

- objection-handling-desk
- deal-review-desk
- crm-update-desk
- customer-handoff-desk

## Source hierarchy

- CRM and user-provided commercial terms define scope.
- Approved templates and brand rules control artifact presentation.
- Final customer sharing requires human approval.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
