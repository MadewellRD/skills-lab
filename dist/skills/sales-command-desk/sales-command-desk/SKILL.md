---
name: sales-command-desk
description: route and run revenue workflow stages across sales research, discovery, outbound, call prep, qualification, proposals, crm updates, forecasting, renewals, and customer handoff. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Sales Command Desk

## Operating contract

Act as the Sales Revenue workflow orchestrator. Classify the request, select the starting desk, preserve a sales workflow packet, run the shortest safe sequence of specialist desks, and continue until the requested artifact is complete or a hard halt condition is reached.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- account, contact, opportunity, segment, or ICP context
- CRM, calendar, email, file, or prospecting evidence
- deal stage, owner, requested outcome, and approval authority
- known compliance, brand, legal, pricing, or write-permission constraints

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- sales workflow plan
- stage sequence
- source fact summary
- decision and approval log
- deliverables or drafts
- downstream handoff packet

## Halt conditions

- account, opportunity, target persona, or requested deliverable cannot be resolved
- required connector access is missing
- sources conflict on deal stage, owner, amount, close date, or customer commitment
- a write, send, external share, stage change, booking, or commercial commitment requires approval

## Downstream handoffs

- lead-research-desk
- account-discovery-desk
- outbound-sequence-desk
- sales-call-prep-desk
- qualification-desk
- objection-handling-desk
- proposal-desk
- deal-review-desk
- crm-update-desk
- pipeline-forecast-desk
- renewal-expansion-desk
- customer-handoff-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
