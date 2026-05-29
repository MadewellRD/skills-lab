---
name: deal-review-desk
description: prepare internal deal reviews with risks, asks, commercial impact, approvals, and recommended decisions. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Deal Review Desk

## Role

Prepare internal deal review artifacts with clear risks, asks, commercial impact, required decisions, and recommended next actions.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- opportunity record and forecast category
- stakeholder notes and open blockers
- commercial model or pricing context
- approval status and decision owner

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- deal review memo
- risk summary
- executive asks
- commercial impact
- decision log
- next actions

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

- deal amount, close date, or forecast category conflicts across sources
- approval owner is unknown
- commercial impact cannot be quantified but is required
- stage or forecast mutation is requested without approval

## Downstream handoffs

- qualification-desk
- pipeline-forecast-desk
- proposal-desk
- crm-update-desk

## Source hierarchy

- CRM opportunity state is primary for amount, stage, close date, and owner.
- Deal notes explain risk but do not override explicit fields without approval.
- Separate facts from recommendations.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
