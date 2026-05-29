---
name: qualification-desk
description: score opportunities against meddicc, bant, or local qualification frameworks with evidence-backed gaps and next actions. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Qualification Desk

## Operating contract

Evaluate whether an opportunity satisfies the team's qualification framework and identify evidence gaps before stage progression or proposal work.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- active opportunity record
- qualification methodology
- discovery notes and stakeholder evidence
- timeline, budget, pain, champion, and decision process evidence

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- qualification score
- criteria assessment
- missing evidence
- stage readiness recommendation
- next actions
- escalation flags

## Halt conditions

- qualification framework is missing
- required evidence is absent
- deal stage change is requested without approval
- budget, authority, or close plan is inferred without proof

## Downstream handoffs

- sales-call-prep-desk
- deal-review-desk
- proposal-desk
- crm-update-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
