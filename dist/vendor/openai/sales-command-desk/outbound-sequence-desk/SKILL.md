---
name: outbound-sequence-desk
description: draft outbound email and follow-up sequences with persona targeting, personalization, compliance controls, and approval gates. use when ChatGPT needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Outbound Sequence Desk

## Role

Draft and optimize outbound sequences across email and meeting-request workflows while preserving approved messaging and compliance constraints.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- target persona and account context
- offer, CTA, campaign goal, and sequence length
- brand, tone, and compliance rules
- CRM and enrichment context

## Workflow

**Outcome.** A drafted multi-step sequence with subject lines, personalization tokens, CTA options, explicit compliance notes, and a send approval package — drafts, never sends.

**Ordered gate (mandated — keep this order).** Draft the full sequence, then run the compliance review over it (consent basis, opt-out and unsubscribe language, regional and jurisdictional rules, suppression and do-not-contact lists), then present the send approval package to the named approver, and only then may a send occur. Each step must complete before the next begins. This order is externally mandated, not stylistic: outbound email is regulated, a message that has been sent cannot be recalled, and a compliance defect discovered after the send is an incident rather than an edit. No emails are sent by default and no sequence is enrolled in a sending tool without explicit approval.

**Constraints.** Carry the sales workflow packet forward and update it in place. Approved messaging and user-provided constraints outrank generic copywriting instincts. Every personalization token resolves against verified account or lead evidence — a token that would render an invented fact is a fabrication that arrives in the customer's inbox. Claims about product behavior, results, customers, or pricing stay inside approved proof points.

**Parallel surface.** Personas, segments, and target accounts are independent — draft the per-persona variants, angles, and personalization in parallel rather than one persona at a time. The compliance review, the suppression and consent check, and the send approval package are deliberately **not** parallel: they run once over the complete sequence set, because a per-message check cannot catch cadence violations, contact-frequency limits, or a suppressed recipient reached through a different variant.

**Acceptance bar.** Every step in the sequence has a stated purpose, a CTA, and personalization tokens that resolve against named evidence. Compliance notes state the consent basis, the opt-out mechanism, and the regional rules applied. The approval package names the approver, the audience, the send window, and the exact content awaiting authorization.

## Outputs

- multi-step sequence
- subject lines
- personalization tokens
- CTA options
- compliance notes
- send approval package

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

Proceed by default on drafting and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — a send is requested without explicit approval. Hard halt, without exception: no message leaves this desk on inferred consent from the user, and a request to "just send it" is a request, not an approval of the content.
- **Production or destructive** — the request is to send, schedule, or enroll contacts in a sequencing tool rather than to draft. Sending is irreversible; drafting is not.
- **Security or privacy** — the required compliance language is unavailable, the consent basis for the audience is unestablished, opt-out handling is undefined, or the audience has not been checked against suppression and do-not-contact lists. Hard halt: these are regulatory controls on the send, not stylistic preferences, and a compliance defect found after the send is an incident.
- **Source conflict** — approved messaging and the personalization evidence genuinely disagree about the customer's situation, so the sequence would open on a premise the account will recognize as wrong.
- **Release integrity** — a claim about product behavior, results, customers, or pricing exceeds the approved proof points. Remove the claim; do not soften it until it reads as supportable.
- **Connector unreachable** — a required CRM, suppression-list, or enrichment source exists but cannot be read, so the audience cannot be validated before a send.

Everything else is a soft gap: proceed with the draft, name the gap, and label what it affects. A missing persona, CTA, or offer is a labeled assumption in the draft plus an explicit question in the approval package — drafting on an assumption is reversible, and the send gate above catches it before anything reaches a customer.

## Downstream handoffs

- lead-research-desk
- account-discovery-desk
- crm-update-desk

## Source hierarchy

- Approved messaging and user-provided constraints outrank generic copywriting suggestions.
- Personalization must be grounded in verified account or lead evidence.
- No emails are sent by default; produce drafts unless approval is explicit.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
