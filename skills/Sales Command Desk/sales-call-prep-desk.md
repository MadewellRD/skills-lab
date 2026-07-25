---
name: sales-call-prep-desk
description: prepare agendas, discovery questions, attendee context, objection watchlists, and follow-up scaffolds for sales meetings. use when {{AGENT}} needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Sales Call Prep Desk

## Role

Prepare call briefs, agendas, discovery questions, risk notes, and follow-up scaffolds for upcoming or recent sales calls.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- calendar event, date, attendees, and meeting objective
- account and opportunity context
- prior notes, emails, decks, or PDFs
- desired call outcome

## Workflow

**Outcome.** A call prep brief: agenda, attendee map, discovery questions tied to the gaps that matter, an objection watchlist, and a follow-up checklist ready to complete after the call.

**Constraints.** Carry the sales workflow packet forward and update it in place. The calendar invite establishes logistics; CRM and prior notes establish deal context; files and decks are supporting content and must not create commitments nobody made. Mark every attendee as internal or external before any content is assembled, and keep internal-only assessments — deal risk, forecast commentary, competitive positioning, pricing latitude — out of anything that could be shared in the meeting. Discovery questions target the specific evidence gaps in the deal rather than a generic list.

**Parallel surface.** Attendees are independent research units, and where several meetings are in scope each meeting is independent — prepare them in parallel rather than sequentially. The agenda, the objection watchlist ordering, and the internal/external content split are aggregate passes over the complete attendee set, because agenda time is allocated across the whole meeting and the sharing boundary is defined by who is in the room.

**Acceptance bar.** Every attendee is classified internal or external and carries the context sourced for them; every agenda item has a purpose and an owner; every discovery question names the gap it closes; and the brief states clearly which sections are internal-only. Context that could not be retrieved is named as a gap rather than filled with a plausible reconstruction.

## Outputs

A complete run delivers the whole prep package before the call, not one section of it:

- call prep brief
- suggested agenda
- attendee map
- discovery questions
- objection watchlist
- follow-up checklist

The follow-up checklist belongs to the prep rather than to a later stage — it is what the rep completes in the ten minutes after the call, and it is written before the call happens.

Each artifact is done when the rep could walk in on it. Every attendee is classified internal or external and carries the context sourced for them; every agenda item has a purpose and an owner; every discovery question names the specific gap it closes instead of being a generic list; the watchlist names the objections this account is likely to raise and where the response lives. A brief that recaps the CRM record is not preparation.

Producing all of it does not authorize filling in the people. An attendee's role, seniority, priorities, or history that could not be retrieved is named as a gap rather than reconstructed into something plausible — being wrong about someone's job in front of that person is a credibility loss the meeting does not recover from. The internal/external split stays a hard boundary: deal risk, forecast commentary, competitive positioning, and pricing latitude live in the internal-only sections and out of anything shareable in the room, and a complete package never makes internal assessment shareable. Attendees, and each meeting where several are in scope, are independent research units inside the parallel surface declared in Workflow.

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

- **Approval** — a meeting booking, invite, reschedule, or customer-facing send is requested without approval. Hard halt: calendar actions and customer messages reach people outside the company.
- **Production or destructive** — the request is to book, send, or write back to the CRM rather than to prepare.
- **Security or privacy** — internal and external attendees are ambiguous, or internal-only material (deal risk, forecast commentary, pricing latitude, competitive assessment) would be placed in a document that could be shared in the meeting. Hard halt: the sharing boundary must be established before content is assembled, because this exposure cannot be walked back once the screen is shared.
- **Source conflict** — CRM, calendar, and prior notes genuinely disagree on the meeting purpose, the attendees, or the deal state the meeting is premised on.
- **Release integrity** — a brief is about to assert customer commitments, prior agreements, or product promises that the prior context does not support.
- **Connector unreachable** — a required calendar, CRM, email, or file source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. An ambiguous meeting or account is resolved to the most likely match with the assumption stated. Missing prior context lowers the brief's stated confidence and appears as a named gap with the question to ask on the call — a thinner brief delivered before the meeting beats a complete one delivered after it.

## Downstream handoffs

- qualification-desk
- objection-handling-desk
- proposal-desk
- crm-update-desk

## Source hierarchy

- Calendar invite establishes meeting logistics.
- CRM and prior notes establish deal context.
- Files and decks provide supporting content but must not create unsupported customer commitments.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
