# Pipeline Forecast Desk Stage Contract

## Purpose
Generate forecast narratives, confidence scores, and spreadsheet models from CRM pipeline snapshots and forecast rules.

## Inputs
- pipeline dataset or CRM snapshot
- stage definitions and forecast rules
- historical conversion assumptions
- segments, owners, or time period

## Outputs
- forecast summary
- commit/best-case/pipeline views
- risk-adjusted model
- spreadsheet artifact
- segment commentary
- slippage and concentration risks

## Continuation rule
Continue to downstream desks only when the stage output is complete, source facts are preserved, and no approval gate blocks progress.

## Halt conditions
- forecast period is missing
- stage definitions or forecast rules are unavailable
- pipeline fields are incomplete
- formula or model assumptions cannot be verified

## Downstream handoffs
- deal-review-desk
- crm-update-desk
- renewal-expansion-desk
