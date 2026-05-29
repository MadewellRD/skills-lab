---
name: objection-handling-desk
description: draft grounded responses to pricing, timing, security, technical, competitive, and commercial objections. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Objection Handling Desk

## Role

Classify sales objections and draft evidence-backed responses, clarifying questions, and follow-up language for verbal or written use.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- objection text or call note
- deal stage and customer context
- approved proof points and competitive claims
- product, security, legal, or pricing constraints

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- objection classification
- core response
- follow-up questions
- supporting evidence list
- talk track
- email draft

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

- approved proof points are missing
- requested claim is unsupported
- legal/security/pricing approval is required
- customer-facing send is requested without approval

## Downstream handoffs

- proposal-desk
- sales-call-prep-desk
- crm-update-desk

## Source hierarchy

- Approved proof points and first-party collateral are authoritative.
- Competitive or technical claims must be grounded and scoped.
- Do not overpromise product behavior, timelines, or commercial concessions.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
