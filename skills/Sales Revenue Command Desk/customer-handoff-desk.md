---
name: customer-handoff-desk
description: prepare post-sale handoff packages for onboarding, customer success, support, or implementation teams. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Customer Handoff Desk

## Role

Prepare complete post-sale handoff packages that preserve customer goals, promised outcomes, scope, risks, owners, and next actions.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- closed-won opportunity
- account and stakeholder context
- scope and commercial terms
- proposal/order-form files
- risks, dependencies, and timeline

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- handoff brief
- customer summary
- open risks
- promised deliverables
- owner/action list
- DOCX/PDF-ready package

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

- opportunity is not closed-won or handoff trigger is unclear
- scope or promised deliverables conflict across sources
- required handoff owner is missing
- CRM note/task write lacks approval

## Downstream handoffs

- crm-update-desk
- renewal-expansion-desk
- customer-success handoff if available

## Source hierarchy

- Signed commercial artifacts and CRM define committed scope.
- Proposal files and notes support context but must not alter commitments.
- Surface unresolved commercial, technical, or onboarding risks.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
