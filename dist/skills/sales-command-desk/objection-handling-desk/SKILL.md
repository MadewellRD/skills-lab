---
name: objection-handling-desk
description: draft grounded responses to pricing, timing, security, technical, competitive, and commercial objections. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Objection Handling Desk

## Operating contract

Classify sales objections and draft evidence-backed responses, clarifying questions, and follow-up language for verbal or written use.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- objection text or call note
- deal stage and customer context
- approved proof points and competitive claims
- product, security, legal, or pricing constraints

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- objection classification
- core response
- follow-up questions
- supporting evidence list
- talk track
- email draft

## Halt conditions

- approved proof points are missing
- requested claim is unsupported
- legal/security/pricing approval is required
- customer-facing send is requested without approval

## Downstream handoffs

- proposal-desk
- sales-call-prep-desk
- crm-update-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
