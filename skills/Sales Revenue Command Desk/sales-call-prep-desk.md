---
name: sales-call-prep-desk
description: prepare agendas, discovery questions, attendee context, objection watchlists, and follow-up scaffolds for sales meetings. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
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

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- call prep brief
- suggested agenda
- attendee map
- discovery questions
- objection watchlist
- follow-up checklist

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

- meeting or account cannot be resolved
- internal versus external attendees are ambiguous
- prior context is unavailable for a requested high-confidence prep brief
- booking or customer send is requested without approval

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
