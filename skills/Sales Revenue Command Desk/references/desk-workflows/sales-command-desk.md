# Sales Command Desk Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `sales-command-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
- account, contact, opportunity, segment, or ICP context
- CRM, calendar, email, file, or prospecting evidence
- deal stage, owner, requested outcome, and approval authority
- known compliance, brand, legal, pricing, or write-permission constraints

## Outputs
- sales workflow plan
- stage sequence
- source fact summary
- decision and approval log
- deliverables or drafts
- downstream handoff packet

## Halt conditions
- account, opportunity, target persona, or requested deliverable cannot be resolved
- required connector access is missing
- sources conflict on deal stage, owner, amount, close date, or customer commitment
- a write, send, external share, stage change, booking, or commercial commitment requires approval

## Downstream handoffs
- lead-research-desk
- account-discovery-desk
- outbound-sequence-desk
- sales-call-prep-desk
- qualification-desk
- objection-handling-desk
- proposal-desk
- deal-review-desk
- crm-update-desk
- pipeline-forecast-desk
- renewal-expansion-desk
- customer-handoff-desk
