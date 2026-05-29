---
name: pipeline-forecast-desk
description: generate forecast narratives, commit and best-case views, risk-adjusted models, and spreadsheet artifacts from pipeline data. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Pipeline Forecast Desk

## Operating contract

Generate forecast narratives, confidence scores, and spreadsheet models from CRM pipeline snapshots and forecast rules.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- pipeline dataset or CRM snapshot
- stage definitions and forecast rules
- historical conversion assumptions
- segments, owners, or time period

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- forecast summary
- commit/best-case/pipeline views
- risk-adjusted model
- spreadsheet artifact
- segment commentary
- slippage and concentration risks

## Halt conditions

- forecast period is missing
- stage definitions or forecast rules are unavailable
- pipeline fields are incomplete
- formula or model assumptions cannot be verified

## Downstream handoffs

- deal-review-desk
- crm-update-desk
- renewal-expansion-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
