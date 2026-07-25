# Deal Review Desk Stage Contract

## Purpose
Prepare internal deal review artifacts with clear risks, asks, commercial impact, required decisions, and recommended next actions.

## Inputs
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

## Continuation rule
Continue to downstream desks only when the stage output is complete, source facts are preserved, and no approval gate blocks progress.

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
