# CRM Update Desk Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `crm-update-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
- account, contact, opportunity, or task identifier
- source notes, transcript, email thread, or user instruction
- CRM field mapping rules
- write permission and approval state

## Outputs
- proposed CRM diff
- notes and tasks
- field update package
- approval request
- audit log
- write result when approved

## Halt conditions
- record ID cannot be resolved
- field mapping is unknown
- write permission is missing
- stage, amount, close date, owner, or external commitment changes lack approval

## Downstream handoffs
- sales-command-desk
- deal-review-desk
- pipeline-forecast-desk
- customer-handoff-desk
