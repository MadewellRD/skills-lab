# Deal Review Desk Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `deal-review-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
- opportunity record and forecast category
- stakeholder notes and open blockers
- commercial model or pricing context
- approval status and decision owner

## Outputs
- deal review memo
- risk summary
- executive asks
- commercial impact
- decision log
- next actions

## Halt conditions
- deal amount, close date, or forecast category conflicts across sources
- approval owner is unknown
- commercial impact cannot be quantified but is required
- stage or forecast mutation is requested without approval

## Downstream handoffs
- qualification-desk
- pipeline-forecast-desk
- proposal-desk
- crm-update-desk
