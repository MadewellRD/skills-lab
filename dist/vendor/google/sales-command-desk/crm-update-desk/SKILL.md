---
name: crm-update-desk
description: create safe crm note, task, field, and stage update packages with dry-run diffs, approvals, and audit logs. use when Gemini needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# CRM Update Desk

## Role

Create safe, auditable CRM updates from meetings, emails, files, and user instructions using dry-run diffs and approval gates.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- account, contact, opportunity, or task identifier
- source notes, transcript, email thread, or user instruction
- CRM field mapping rules
- write permission and approval state

## Workflow

**Outcome.** A CRM update package: the proposed diff against the current record, the notes and tasks to be created, the field update set, an approval request, an audit log, and — only once approved — the write result.

**Ordered gate (mandated — keep this order, every time).** Read the current record as the preimage, produce the dry-run diff against it, obtain explicit approval of that diff, execute the write, then record the audit entry. Every step precedes the next and none may be skipped or merged. This order is mandated because the CRM is a system of record: once a field is overwritten the preimage is gone and cannot be reconstructed from the artifact, an unapproved stage or amount change propagates into forecasts other people have already committed on, and a write with no audit entry cannot be traced or reversed. Never collapse the diff and the write into one action, never write ahead of approval, and never treat a user's request for an update as approval of a diff they have not seen.

**Constraints.** Carry the sales workflow packet forward and update it in place. The current CRM record is the preimage for every diff; meeting notes and emails are evidence for proposed values, not values in themselves. Never invent a record ID, a field name, a picklist value, an owner, or a date — an unresolved identifier or an unknown field mapping appears in the diff as a labeled assumption for the approver to confirm, and the write for that row stays blocked until it is confirmed. No destructive or material write happens without approval.

**Parallel surface.** Diff computation is parallel-safe across independent records — accounts, contacts, opportunities, notes, and tasks can each be read and diffed against their own preimage concurrently. The approval and the commit are deliberately **not** parallel: approval is requested once over the complete diff set so the approver sees the full blast radius before anything is written, and the audit log is a single record of what was approved and what was actually written.

**Acceptance bar.** Every proposed change shows the current value, the proposed value, and the evidence for it. Every material change — stage, amount, close date, owner, or anything creating an external commitment — is explicitly flagged as requiring approval. The audit log states what was approved, by whom, what was written, and what was not. A diff that a reviewer cannot evaluate without opening the CRM themselves has not met the bar.

## Outputs

A complete run produces the whole reviewable package, not one part of it:

- proposed CRM diff
- notes and tasks
- field update package
- approval request
- audit log

The diff shows what would change, the notes and tasks show what would be created, and the approval request is the thing a human actually authorizes. Producing them together is what lets an approver see the full blast radius at once.

One artifact is deliberately outside that set:

- write result when approved — produced only after the ordered gate in Workflow has cleared, and only for the rows that were approved. A complete draft package never advances the write; it is what the approver reads before authorizing, not evidence that authorization happened.

Depth is judged by whether an approver can decide without opening the CRM themselves. Every proposed change shows the current value, the proposed value, and the evidence for it; every material field — stage, amount, close date, owner, or anything creating an external commitment — is flagged as requiring approval; the audit log states what was approved, by whom, what was written, and what was not. A diff naming fields without showing values has not met the bar.

Completing the package is not permission to populate it. A record ID, field name, picklist value, owner, or date that no source establishes appears as a labelled assumption for the approver to confirm and that row's write stays blocked — never as a guessed value. A plausible-looking CRM write destroys a preimage nobody can reconstruct and propagates into forecasts other people have already committed on. Diff computation across independent records is part of the parallel surface declared in Workflow; the approval and the commit deliberately are not.

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

Proceed by default on the dry-run diff and label the assumption inline. Reserve hard halts for these consequence classes — all of which block the **write**, never the diff:

- **Approval** — a stage, amount, close date, owner, or any change creating an external commitment lacks explicit approval of the diff. Hard halt, always: material CRM fields are approved by a human who has seen the proposed values, not inferred from the request that prompted them.
- **Production or destructive** — any write to the system of record. This is the desk's core boundary: the write is gated behind the ordered sequence above and does not execute early because the change seems obviously correct. A missing write permission is the same class — hard halt on the write, produce the diff and the approval request instead.
- **Security or privacy** — the update would place personal data, customer-confidential material, or content the customer did not consent to record into a shared system of record.
- **Source conflict** — the current record and the source notes genuinely disagree on a material field. Show both in the diff, flag the field contested, and hard halt the write on that row; do not overwrite a disputed value.
- **Release integrity** — the diff cannot be shown against a real preimage, so the approver would be authorizing a change they cannot evaluate.
- **Connector unreachable** — the CRM cannot be read, so no preimage exists. Without a preimage there is no diff, and without a diff there is no write.

Everything else is a soft gap: proceed with the dry-run diff, name the gap, and label what it affects. An unresolved record ID or an unknown field mapping is a labeled assumption inside the diff for the approver to confirm — the row is still shown, the write for that row stays blocked, and no ID, field, or picklist value is ever guessed into a write.

## Downstream handoffs

- sales-command-desk
- deal-review-desk
- pipeline-forecast-desk
- customer-handoff-desk

## Source hierarchy

- Current CRM record is the preimage for all diffs.
- Meeting notes and emails provide evidence for proposed updates.
- No destructive or material write happens without approval.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
