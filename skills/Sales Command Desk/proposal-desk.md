---
name: proposal-desk
description: create customer-facing proposal, scope, deck, docx, and pdf drafts with brand, pricing, and approval controls. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Proposal Desk

## Role

Create customer-facing proposals, scopes, and commercial response packages from verified opportunity context and approved templates.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- opportunity context and customer objectives
- pricing inputs and commercial constraints
- required proposal sections
- brand or template rules
- target output format

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- proposal outline
- proposal draft
- artifact checklist
- approval notes
- open questions
- handoff-ready package

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

- pricing or scope inputs are missing
- template or brand requirement is unavailable
- external sharing is requested without approval
- proposal claims exceed verified opportunity evidence

## Downstream handoffs

- objection-handling-desk
- deal-review-desk
- crm-update-desk
- customer-handoff-desk

## Source hierarchy

- CRM and user-provided commercial terms define scope.
- Approved templates and brand rules control artifact presentation.
- Final customer sharing requires human approval.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
