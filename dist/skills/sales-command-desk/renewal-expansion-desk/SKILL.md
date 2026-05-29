---
name: renewal-expansion-desk
description: support renewal, upsell, and cross-sell motions with churn risk, expansion hypotheses, outreach, and forecast impact notes. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Renewal Expansion Desk

## Operating contract

Support renewals, upsell, and cross-sell motions with risk analysis, expansion hypotheses, stakeholder plans, and follow-up drafts.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- renewal account and contract dates
- product usage, support, and customer-health context
- stakeholder history
- commercial targets and constraints

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- renewal risk memo
- expansion hypotheses
- stakeholder plan
- follow-up drafts
- forecast impact note
- open issue list

## Halt conditions

- contract dates or commercial terms are missing
- usage/support evidence is unavailable when required
- retention risk is asserted without evidence
- customer send or commit change lacks approval

## Downstream handoffs

- sales-call-prep-desk
- proposal-desk
- deal-review-desk
- crm-update-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
