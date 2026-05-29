---
name: proposal-desk
description: create customer-facing proposal, scope, deck, docx, and pdf drafts with brand, pricing, and approval controls. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Proposal Desk

## Operating contract

Create customer-facing proposals, scopes, and commercial response packages from verified opportunity context and approved templates.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- opportunity context and customer objectives
- pricing inputs and commercial constraints
- required proposal sections
- brand or template rules
- target output format

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- proposal outline
- proposal draft
- artifact checklist
- approval notes
- open questions
- handoff-ready package

## Halt conditions

- pricing or scope inputs are missing
- template or brand requirement is unavailable
- external sharing is requested without approval
- proposal claims exceed verified opportunity evidence

## Downstream handoffs

- objection-handling-desk
- deal-review-desk
- crm-update-desk
- customer-handoff-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
