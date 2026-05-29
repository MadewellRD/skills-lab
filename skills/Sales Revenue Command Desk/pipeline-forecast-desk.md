---
name: pipeline-forecast-desk
description: generate forecast narratives, commit and best-case views, risk-adjusted models, and spreadsheet artifacts from pipeline data. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Pipeline Forecast Desk

## Role

Generate forecast narratives, confidence scores, and spreadsheet models from CRM pipeline snapshots and forecast rules.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- pipeline dataset or CRM snapshot
- stage definitions and forecast rules
- historical conversion assumptions
- segments, owners, or time period

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- forecast summary
- commit/best-case/pipeline views
- risk-adjusted model
- spreadsheet artifact
- segment commentary
- slippage and concentration risks

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

- forecast period is missing
- stage definitions or forecast rules are unavailable
- pipeline fields are incomplete
- formula or model assumptions cannot be verified

## Downstream handoffs

- deal-review-desk
- crm-update-desk
- renewal-expansion-desk

## Source hierarchy

- CRM snapshot defines pipeline state.
- Forecast rules must be explicit and preserved in outputs.
- Keep spreadsheet formulas dynamic where spreadsheet artifacts are generated.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
