---
name: crm-update-desk
description: create safe crm note, task, field, and stage update packages with dry-run diffs, approvals, and audit logs. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# CRM Update Desk

## Operating contract

Create safe, auditable CRM updates from meetings, emails, files, and user instructions using dry-run diffs and approval gates.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- account, contact, opportunity, or task identifier
- source notes, transcript, email thread, or user instruction
- CRM field mapping rules
- write permission and approval state

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

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

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
