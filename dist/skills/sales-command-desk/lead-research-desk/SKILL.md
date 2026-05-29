---
name: lead-research-desk
description: research and rank prospects using icp, crm, enrichment, and public evidence before outreach. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Lead Research Desk

## Operating contract

Research named prospects or prospect lists and produce concise, source-backed lead briefs prioritized for sales outreach.

Read `references/suite-workflow-contract.md` for cross-desk continuation rules, `references/workflow-packet-schema.md` for packet fields, and `references/stage-contract.md` for this desk's stage contract.

## Execution rules

- Start by resolving the requested outcome, account/contact/opportunity context, evidence sources, and approval state.
- Maintain a sales workflow packet throughout the response.
- Prefer completing the requested stage over giving a bare recommendation to use another desk.
- Continue to a downstream desk only when required facts are present and no approval gate blocks progress.
- Halt with the suite halt format when connector access, required facts, source conflicts, or approval gates block safe continuation.
- Do not send emails, book external meetings, write CRM fields, change stages, alter amount or close date, or share customer-facing artifacts without explicit approval.

## Required evidence

- ICP, target title, segment, geography, and exclusion rules
- existing CRM records and dedupe criteria
- prospecting or enrichment data
- public company and role evidence

## Stage workflow

- Classify the stage mode.
- Gather and normalize source facts.
- Produce the requested artifact or decision output.
- Record assumptions, open questions, and approval requirements.
- Preserve completed stage state and downstream handoff targets.

## Outputs

- ranked lead list
- lead briefs
- fit score
- recommended angle
- missing data and risk notes
- next-step recommendation

## Halt conditions

- ICP or target audience is missing
- prospecting data cannot be verified
- requested contact details are unavailable or low confidence
- outbound send is requested without approval

## Downstream handoffs

- account-discovery-desk
- outbound-sequence-desk
- crm-update-desk

## Observability hooks

- Log selected desk, workflow mode, sources consulted, confidence labels, approval gates, and any blocked write/send/share action.
- Record dry-run CRM diffs before writes.
- Record artifact names and source facts used to support customer-facing claims.
