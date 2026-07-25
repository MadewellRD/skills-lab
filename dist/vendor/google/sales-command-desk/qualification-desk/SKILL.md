---
name: qualification-desk
description: score opportunities against meddicc, bant, or local qualification frameworks with evidence-backed gaps and next actions. use when Gemini needs to perform or continue sales revenue command desk work involving accounts, leads, opportunities, crm, calendar, email, files, prospecting, proposals, forecasts, renewals, or customer handoffs.
---

# Qualification Desk

## Role

Evaluate whether an opportunity satisfies the team's qualification framework and identify evidence gaps before stage progression or proposal work.

## Use when

- A user asks for sales, revenue, account, lead, opportunity, renewal, forecast, proposal, or CRM workflow support.
- The work needs connector-grounded source facts, approval gates, or downstream continuation across Sales Revenue desks.
- A preserved sales workflow packet or prior sales artifact needs continuation.

## Do not use when

- The request is only generic copywriting with no sales workflow context.
- The task requires legal, tax, security, or pricing approval that has not been granted.
- The request asks to send customer communications, change CRM material fields, or create external commitments without explicit approval.

## Required evidence

- active opportunity record
- qualification methodology
- discovery notes and stakeholder evidence
- timeline, budget, pain, champion, and decision process evidence

## Workflow

**Outcome.** A qualification assessment against the team's framework: a per-criterion score with its evidence, the missing evidence named, a stage-readiness recommendation, next actions, and any escalation flags.

**Ordered gate (mandated — keep this order).** A stage-readiness recommendation is produced first and a CRM stage change happens only after explicit approval — assessment, then approval, then write, never a write that follows from the score automatically. The order is mandated because deal stage drives forecast, reporting, and process gates downstream; a stage advanced on an inferred score corrupts the pipeline for everyone reading it.

**Constraints.** Carry the sales workflow packet forward and update it in place. Score only what is evidenced. Unknowns remain unknowns — budget, authority, decision process, and close plan are never inferred from deal momentum, seniority, or enthusiasm, and an unscored criterion is reported as unscored rather than given a middling value to complete the matrix.

**Parallel surface.** The framework criteria are independent assessments against their own evidence, and where several opportunities are in scope each opportunity is independent — evaluate them in parallel rather than walking the framework in order. The composite score, the stage-readiness recommendation, and the escalation flags are a single aggregate pass once every criterion is assessed, because readiness is defined over the complete criterion set.

**Acceptance bar.** Every criterion carries a score or an explicit `unknown`, and every score names the note, email, meeting, or record that supports it. The missing-evidence list is specific enough to act on — who to ask and what to ask for. The stage recommendation follows from the criterion set rather than from overall impression.

## Outputs

- qualification score
- criteria assessment
- missing evidence
- stage readiness recommendation
- next actions
- escalation flags

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

- **Approval** — a deal stage change, forecast category change, or CRM write is requested without explicit approval. Hard halt: stage drives forecast and process gates that other people rely on.
- **Production or destructive** — the request is to advance the opportunity in the CRM rather than to assess whether it should advance.
- **Security or privacy** — the assessment would expose confidential customer commercial detail or personal data in the artifact.
- **Source conflict** — CRM fields, discovery notes, and stakeholder evidence genuinely disagree on budget, authority, timeline, or decision process. Record both readings against the criterion and mark it contested; a qualification score that averages a conflict hides the thing the review needs to see.
- **Release integrity** — a qualified verdict or stage-readiness recommendation would rest on inferred budget, authority, or close plan rather than on evidence. Report the criterion as `unknown` instead — an honest gap is this desk's product.
- **Connector unreachable** — a required CRM, email, or notes source exists but cannot be read, so the evidence base cannot be assembled at all.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A missing qualification framework means adopting a named standard one, stating which and why, and scoring against it. Absent evidence for a criterion is scored `unknown` with the specific missing evidence named — that gap list is the most useful part of the output, not a reason to withhold it.

## Downstream handoffs

- sales-call-prep-desk
- deal-review-desk
- proposal-desk
- crm-update-desk

## Source hierarchy

- Score only what is evidenced.
- Unknowns remain unknowns; do not inflate confidence.
- CRM stage changes require explicit approval.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, hypotheses, decisions, and open questions.
- Preserve the workflow packet in every handoff.
- Use dry-run diffs for CRM changes before any write.
- Keep customer-facing claims within verified deal, product, pricing, and approval evidence.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
