---
name: lead-research-desk
description: research and rank prospects using icp, crm, enrichment, and public evidence before outreach. use when Gemini needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
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

**Outcome.** A ranked lead list with per-lead briefs: fit against the stated ICP, the evidence behind that fit, a recommended angle, the missing data, and a next-step recommendation — ready for outreach that this desk does not itself send.

**Constraints.** Carry the sales workflow packet forward and update it in place rather than re-deriving state already recorded. Every contact detail, title, reporting line, company fact, and buying signal is either sourced or absent — never fabricate contact data, org structure, or intent, and label any enrichment field whose confidence is low. Respect exclusion rules, suppression lists, and regional data-protection constraints on personal data at research time, not later at send time. This desk produces drafts and lists; it does not write to the CRM and does not send outbound.

**Parallel surface.** Leads and prospect accounts are independent research units — enrich, source, and score each in parallel rather than working down the list. Dedupe against existing CRM records, cross-lead ranking, and account-level roll-up are aggregate passes over the complete set, because a duplicate is a relationship between records and a ranking is a property of the whole list.

**Acceptance bar.** Every lead carries a fit score against the stated ICP criteria, every asserted fact names its source, every low-confidence field is labeled, and every lead is marked as new or already present in the CRM. A lead whose contact data could not be sourced appears with the gap named rather than with a plausible guess in the field.

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

Proceed by default on reversible work and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — an outbound send, a sequence enrollment, or a customer-facing action is requested without explicit approval. Hard halt: this desk researches and ranks, it does not contact.
- **Production or destructive** — the request is to write leads into the CRM, enrich existing records in place, or import a list rather than to produce one.
- **Security or privacy** — sourcing or storing the requested personal data would breach consent, regional data-protection rules, or a suppression or do-not-contact instruction. This applies at research time, not only at send time.
- **Source conflict** — CRM records and enrichment sources genuinely disagree on identity, employment, or ownership such that the lead may be a duplicate of an existing relationship. Flag the collision; do not create a second record path.
- **Release integrity** — a lead brief is about to present unverified contact data, reporting lines, or buying intent as established fact.
- **Connector unreachable** — a required CRM or enrichment source exists but cannot be read, so dedupe against existing records is impossible.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A missing ICP means proposing one from the accounts already in the CRM, labeling it as proposed, and ranking against it. Unavailable or low-confidence contact detail is reported as missing or labeled low confidence — never filled with a plausible address, title, or reporting line.

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

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
