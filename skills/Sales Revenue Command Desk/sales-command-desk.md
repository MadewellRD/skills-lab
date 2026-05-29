---
name: sales-command-desk
description: route and run revenue workflow stages across sales research, discovery, outbound, call prep, qualification, proposals, crm updates, forecasting, renewals, and customer handoff. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Sales Command Desk

## Role

Act as the Sales Revenue workflow orchestrator. Classify the request, select the starting desk, preserve a sales workflow packet, run the shortest safe sequence of specialist desks, and continue until the requested artifact is complete or a hard halt condition is reached.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- account, contact, opportunity, segment, or ICP context
- CRM, calendar, email, file, or prospecting evidence
- deal stage, owner, requested outcome, and approval authority
- known compliance, brand, legal, pricing, or write-permission constraints

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- sales workflow plan
- stage sequence
- source fact summary
- decision and approval log
- deliverables or drafts
- downstream handoff packet

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

## Source hierarchy

- CRM records and user-provided constraints are authoritative for deal state.
- Calendar, email, notes, and files provide supporting context but must be cited as evidence, not assumed truth.
- Prospecting and public web sources support enrichment but must not override first-party CRM evidence.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
