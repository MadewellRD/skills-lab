---
name: outbound-sequence-desk
description: draft outbound email and follow-up sequences with persona targeting, personalization, compliance controls, and approval gates. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Outbound Sequence Desk

## Operating contract

Draft and optimize outbound sequences across email and meeting-request workflows while preserving approved messaging and compliance constraints.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- target persona and account context
- offer, CTA, campaign goal, and sequence length
- brand, tone, and compliance rules
- CRM and enrichment context

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- multi-step sequence
- subject lines
- personalization tokens
- CTA options
- compliance notes
- send approval package

## Halt conditions

- persona, CTA, or offer is missing
- compliance language is required but unavailable
- claims cannot be supported
- user asks to send without explicit approval

## Downstream handoffs

- lead-research-desk
- account-discovery-desk
- crm-update-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
