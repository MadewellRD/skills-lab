---
name: deal-review-desk
description: prepare internal deal reviews with risks, asks, commercial impact, approvals, and recommended decisions. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Deal Review Desk

## Operating contract

Prepare internal deal review artifacts with clear risks, asks, commercial impact, required decisions, and recommended next actions.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- opportunity record and forecast category
- stakeholder notes and open blockers
- commercial model or pricing context
- approval status and decision owner

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- deal review memo
- risk summary
- executive asks
- commercial impact
- decision log
- next actions

## Halt conditions

- deal amount, close date, or forecast category conflicts across sources
- approval owner is unknown
- commercial impact cannot be quantified but is required
- stage or forecast mutation is requested without approval

## Downstream handoffs

- qualification-desk
- pipeline-forecast-desk
- proposal-desk
- crm-update-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
