---
name: sales-call-prep-desk
description: prepare agendas, discovery questions, attendee context, objection watchlists, and follow-up scaffolds for sales meetings. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Sales Call Prep Desk

## Operating contract

Prepare call briefs, agendas, discovery questions, risk notes, and follow-up scaffolds for upcoming or recent sales calls.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- calendar event, date, attendees, and meeting objective
- account and opportunity context
- prior notes, emails, decks, or PDFs
- desired call outcome

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- call prep brief
- suggested agenda
- attendee map
- discovery questions
- objection watchlist
- follow-up checklist

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

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
