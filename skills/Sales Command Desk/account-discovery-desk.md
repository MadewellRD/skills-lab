---
name: account-discovery-desk
description: build account briefs, stakeholder maps, whitespace hypotheses, and meeting agendas from crm, files, and public account evidence. use when {{AGENT}} needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Account Discovery Desk

## Role

Create account briefs, stakeholder maps, whitespace analysis, and opportunity hypotheses for target or active accounts.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- account name, domain, segment, or territory
- CRM account, contact, and opportunity history
- prior notes, emails, decks, or files
- public business context

## Workflow

**Outcome.** An account brief with a stakeholder map, whitespace and opportunity hypotheses, open questions, a meeting agenda, and a source fact map that shows where each claim came from.

**Constraints.** Carry the sales workflow packet forward and update it in place rather than re-deriving state already recorded. CRM and first-party notes are the primary account evidence; public research adds business context and is dated when freshness matters. Keep verified account facts strictly separate from hypotheses — a stakeholder's role, influence, or position on the deal is a claim that needs evidence, and an org chart assembled from inference is labeled as inferred. Nothing produced here goes to the customer without approval.

**Parallel surface.** Accounts are independent, and within an account the individual stakeholders are independent research units — profile them in parallel rather than one contact at a time. The stakeholder map's relationships, the whitespace hypotheses, and the meeting agenda are aggregate passes once the profiles are in, because influence, coverage gaps, and agenda priority are properties of the full stakeholder set.

**Acceptance bar.** Every account and stakeholder fact names its source and is marked verified or hypothesis; every whitespace hypothesis names the evidence that suggests it and what would confirm it; every open question names who could answer it. A stakeholder whose role could not be sourced appears as an open question rather than as an assumed title.

## Outputs

- account brief
- stakeholder map
- opportunity hypotheses
- open questions
- meeting agenda
- source fact map

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

Proceed by default on reversible work and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — customer-facing output is requested from this brief before its facts have been validated and approved. Hard halt: an account brief is internal working material and its hypotheses are not customer-ready by default.
- **Production or destructive** — the request is to write the discovery back into the CRM or contact the stakeholders rather than to produce the brief.
- **Security or privacy** — the brief would collect or expose personal data beyond the business context needed, or would carry confidential material from another account into this one.
- **Source conflict** — CRM records and user-provided account facts genuinely disagree on identity, ownership, hierarchy, or relationship state. Record both and name the owner who can resolve it; an account brief built on the wrong entity is wrong throughout.
- **Release integrity** — a hypothesis about a stakeholder's role, influence, or position is about to leave this desk labeled as a verified fact.
- **Connector unreachable** — a required CRM, file, or email source exists but cannot be read, so first-party account evidence is unavailable entirely.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. An ambiguous account identity is resolved to the most likely entity with the assumption stated and the alternatives listed. A stakeholder claim without evidence is not a halt and is not a fact either — it is recorded as a hypothesis with the question that would confirm it.

## Downstream handoffs

- sales-call-prep-desk
- qualification-desk
- proposal-desk
- crm-update-desk

## Source hierarchy

- CRM and first-party notes are primary account evidence.
- Public web research supports business context and must be dated when freshness matters.
- Separate verified account facts from hypotheses.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.
