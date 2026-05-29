---
name: outbound-sequence-desk
description: draft outbound email and follow-up sequences with persona targeting, personalization, compliance controls, and approval gates. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Outbound Sequence Desk

## Role

Draft and optimize outbound sequences across email and meeting-request workflows while preserving approved messaging and compliance constraints.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- target persona and account context
- offer, CTA, campaign goal, and sequence length
- brand, tone, and compliance rules
- CRM and enrichment context

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- multi-step sequence
- subject lines
- personalization tokens
- CTA options
- compliance notes
- send approval package

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

- persona, CTA, or offer is missing
- compliance language is required but unavailable
- claims cannot be supported
- user asks to send without explicit approval

## Downstream handoffs

- lead-research-desk
- account-discovery-desk
- crm-update-desk

## Source hierarchy

- Approved messaging and user-provided constraints outrank generic copywriting suggestions.
- Personalization must be grounded in verified account or lead evidence.
- No emails are sent by default; produce drafts unless approval is explicit.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
