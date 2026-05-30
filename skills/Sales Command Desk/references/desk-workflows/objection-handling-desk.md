# Objection Handling Desk Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `objection-handling-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
- objection text or call note
- deal stage and customer context
- approved proof points and competitive claims
- product, security, legal, or pricing constraints

## Outputs
- objection classification
- core response
- follow-up questions
- supporting evidence list
- talk track
- email draft

## Halt conditions
- approved proof points are missing
- requested claim is unsupported
- legal/security/pricing approval is required
- customer-facing send is requested without approval

## Downstream handoffs
- proposal-desk
- sales-call-prep-desk
- crm-update-desk
