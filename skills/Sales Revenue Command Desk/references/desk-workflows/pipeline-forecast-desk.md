# Pipeline Forecast Desk Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `pipeline-forecast-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
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

## Halt conditions
- forecast period is missing
- stage definitions or forecast rules are unavailable
- pipeline fields are incomplete
- formula or model assumptions cannot be verified

## Downstream handoffs
- deal-review-desk
- crm-update-desk
- renewal-expansion-desk
