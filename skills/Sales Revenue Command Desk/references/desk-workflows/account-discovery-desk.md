# Account Discovery Desk Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `account-discovery-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome and workflow mode.
2. Resolve account, contact, opportunity, source facts, and approval state.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the sales workflow packet.
5. Continue to downstream desks only when evidence is sufficient and approvals are not blocking.

## Required evidence
- account name, domain, segment, or territory
- CRM account, contact, and opportunity history
- prior notes, emails, decks, or files
- public business context

## Outputs
- account brief
- stakeholder map
- opportunity hypotheses
- open questions
- meeting agenda
- source fact map

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
