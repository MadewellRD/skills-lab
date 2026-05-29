# Customer Handoff Desk Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `customer-handoff-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
- closed-won opportunity
- account and stakeholder context
- scope and commercial terms
- proposal/order-form files
- risks, dependencies, and timeline

## Outputs
- handoff brief
- customer summary
- open risks
- promised deliverables
- owner/action list
- DOCX/PDF-ready package

## Halt conditions
- opportunity is not closed-won or handoff trigger is unclear
- scope or promised deliverables conflict across sources
- required handoff owner is missing
- CRM note/task write lacks approval

## Downstream handoffs
- crm-update-desk
- renewal-expansion-desk
- customer-success handoff if available
