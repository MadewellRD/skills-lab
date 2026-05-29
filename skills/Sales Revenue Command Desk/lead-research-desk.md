---
name: lead-research-desk
description: research and rank prospects using icp, crm, enrichment, and public evidence before outreach. use when chatgpt needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Lead Research Desk

## Role

Research named prospects or prospect lists and produce concise, source-backed lead briefs prioritized for sales outreach.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- ICP, target title, segment, geography, and exclusion rules
- existing CRM records and dedupe criteria
- prospecting or enrichment data
- public company and role evidence

## Workflow

- Classify the sales request and workflow mode.
- Create or update the sales workflow packet.
- Gather only the minimum additional evidence needed to complete the current stage.
- Produce the stage artifact with source-grounded facts and labeled assumptions.
- Continue to downstream desks when evidence is sufficient and no approval gate blocks progress.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- ranked lead list
- lead briefs
- fit score
- recommended angle
- missing data and risk notes
- next-step recommendation

## Workflow packet fields

- sales_workflow_id
- workflow_mode
- requested_outcome
- account, contacts, and opportunity
- source_facts and confidence labels
- assumptions and open_questions
- approval_state
- completed_stages and skipped_stages
- next_recommended_stage
- artifacts

## Halt conditions

- ICP or target audience is missing
- prospecting data cannot be verified
- requested contact details are unavailable or low confidence
- outbound send is requested without approval

## Downstream handoffs

- account-discovery-desk
- outbound-sequence-desk
- crm-update-desk

## Source hierarchy

- CRM records determine whether a lead already exists.
- Prospecting tools may enrich but low-confidence fields must be labeled.
- Do not fabricate contact data, reporting lines, or buying intent.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
