---
name: account-discovery-desk
description: build account briefs, stakeholder maps, whitespace hypotheses, and meeting agendas from crm, files, and public account evidence. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Account Discovery Desk

## Operating contract

Create account briefs, stakeholder maps, whitespace analysis, and opportunity hypotheses for target or active accounts.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- account name, domain, segment, or territory
- CRM account, contact, and opportunity history
- prior notes, emails, decks, or files
- public business context

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- account brief
- stakeholder map
- opportunity hypotheses
- open questions
- meeting agenda
- source fact map

## Halt conditions

- account identity cannot be resolved
- CRM and user-provided account facts conflict
- stakeholder claims lack evidence
- customer-facing output is requested before fact validation

## Downstream handoffs

- sales-call-prep-desk
- qualification-desk
- proposal-desk
- crm-update-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
