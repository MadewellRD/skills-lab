---
name: renewal-expansion-desk
description: support renewal, upsell, and cross-sell motions with churn risk, expansion hypotheses, outreach, and forecast impact notes. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Renewal Expansion Desk

## Role

Support renewals, upsell, and cross-sell motions with risk analysis, expansion hypotheses, stakeholder plans, and follow-up drafts.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- renewal account and contract dates
- product usage, support, and customer-health context
- stakeholder history
- commercial targets and constraints

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- renewal risk memo
- expansion hypotheses
- stakeholder plan
- follow-up drafts
- forecast impact note
- open issue list

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

- contract dates or commercial terms are missing
- usage/support evidence is unavailable when required
- retention risk is asserted without evidence
- customer send or commit change lacks approval

## Downstream handoffs

- sales-call-prep-desk
- proposal-desk
- deal-review-desk
- crm-update-desk

## Source hierarchy

- CRM and contract records establish renewal timing and commercial facts.
- Usage and support evidence inform risk but must be labeled with freshness.
- Separate retention strategy from expansion strategy.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
