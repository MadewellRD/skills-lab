# Objection Handling Desk Stage Contract

## Purpose
Classify sales objections and draft evidence-backed responses, clarifying questions, and follow-up language for verbal or written use.

## Inputs
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

## Continuation rule
Continue to downstream desks only when the stage output is complete, source facts are preserved, and no approval gate blocks progress.

## Halt conditions
- approved proof points are missing
- requested claim is unsupported
- legal/security/pricing approval is required
- customer-facing send is requested without approval

## Downstream handoffs
- proposal-desk
- sales-call-prep-desk
- crm-update-desk
