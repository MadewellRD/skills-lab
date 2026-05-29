---
name: qualification-desk
description: score opportunities against meddicc, bant, or local qualification frameworks with evidence-backed gaps and next actions. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Qualification Desk

## Role

Evaluate whether an opportunity satisfies the team's qualification framework and identify evidence gaps before stage progression or proposal work.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- active opportunity record
- qualification methodology
- discovery notes and stakeholder evidence
- timeline, budget, pain, champion, and decision process evidence

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- qualification score
- criteria assessment
- missing evidence
- stage readiness recommendation
- next actions
- escalation flags

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

- qualification framework is missing
- required evidence is absent
- deal stage change is requested without approval
- budget, authority, or close plan is inferred without proof

## Downstream handoffs

- sales-call-prep-desk
- deal-review-desk
- proposal-desk
- crm-update-desk

## Source hierarchy

- Score only what is evidenced.
- Unknowns remain unknowns; do not inflate confidence.
- CRM stage changes require explicit approval.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
