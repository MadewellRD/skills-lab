# CRM Update Desk Stage Contract

## Purpose
Create safe, auditable CRM updates from meetings, emails, files, and user instructions using dry-run diffs and approval gates.

## Inputs
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

## Continuation rule
Continue to downstream desks only when the stage output is complete, source facts are preserved, and no approval gate blocks progress.

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
