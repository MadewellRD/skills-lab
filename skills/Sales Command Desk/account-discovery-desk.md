---
name: account-discovery-desk
description: build account briefs, stakeholder maps, whitespace hypotheses, and meeting agendas from crm, files, and public account evidence. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Account Discovery Desk

## Role

Create account briefs, stakeholder maps, whitespace analysis, and opportunity hypotheses for target or active accounts.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- account name, domain, segment, or territory
- CRM account, contact, and opportunity history
- prior notes, emails, decks, or files
- public business context

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- account brief
- stakeholder map
- opportunity hypotheses
- open questions
- meeting agenda
- source fact map

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

- account identity cannot be resolved
- CRM and user-provided account facts conflict
- stakeholder claims lack evidence
- customer-facing output is requested before fact validation

## Downstream handoffs

- sales-call-prep-desk
- qualification-desk
- proposal-desk
- crm-update-desk

## Source hierarchy

- CRM and first-party notes are primary account evidence.
- Public web research supports business context and must be dated when freshness matters.
- Separate verified account facts from hypotheses.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
