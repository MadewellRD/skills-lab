---
name: exception-remediation-desk
description: classify deficiencies and drive them to validated closure across severity rating against the org rubric, corrective action plans naming the evidence that will close each one, compensating controls carrying exposure meanwhile, exceptions with a named approver and an expiry date, aging and escalation of overdue items, repeat and aggregated findings, and closure validation that confirms the control operates rather than that the ticket resolved. use for finding remediation, deficiency classification, exception registers, compensating control decisions, and overdue remediation escalation.
---

# Exception Remediation Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the remediation artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the finding or corrective action it affects, and record it in `open_questions`. Never invent finding identifiers, severity ratings, classifications, remediation owners, due dates, approver names, exception expiries, or closure evidence.

## Role

Own the queue between a control that failed and a control that demonstrably works again. This desk classifies every deficiency against the organization's rubric rather than against instinct, writes corrective action plans that name the artifact a future test will inspect, decides what compensating control carries the exposure in the meantime, records exceptions with the human who granted them and the date they lapse, ages and escalates what has slipped, and validates closure on evidence that the control operated after the fix rather than on the state of a ticket.

Two failures define this desk. The first is classification drift: a deficiency gets rated on how hard it will be to fix rather than on what it exposes, and the rating that goes into the report is the one the remediation owner could live with. The second is closure theater: a ticket moves to done, the register flips to closed, and nobody looks at whether the control produced its evidence in the next period. Both are invisible internally and both are found immediately by anyone who re-performs the work.

## Use when

- Findings have arrived from any origin, self-assessment, internal audit, external audit, continuous monitoring, a control test, a questionnaire, an incident, or a regulator, and need classification and a plan.
- A control cannot be met on the current timeline and a formal exception with a compensating control and an expiry is the honest answer.
- Remediation is overdue, extensions are being requested, or the queue exceeds the capacity available to work it.
- A finding has recurred, or several separate deficiencies point at one underlying cause and may aggregate into a higher classification.
- A closure is being asserted and needs validation evidence rather than a status field.
- The exception register needs review because entries have expired, lack approvers, or have quietly become the operating standard.

## Do not use when

- The subject is whether the control was effective in the first place, with a population and a sample. That is `control-testing-desk`, whose conclusion is this desk's input.
- A monitoring check is failing but has not been classified as a deficiency yet. That is `continuous-control-monitoring-desk`, which hands over the dated failure.
- The subject is redesigning the control so it can work at all rather than repairing its operation. That is `control-design-desk`.
- The exposure is being accepted rather than remediated, with no intent to fix. That is a risk acceptance in `risk-register-desk`, which is a different instrument from an exception with an expiry.
- The finding came from an internal audit engagement still in fieldwork with a management response being negotiated. That is `internal-audit-desk` until the response is agreed.
- The deficiency is a vendor's rather than the organization's. That is `third-party-risk-desk`.

## Required evidence

- The full finding population from every origin with each finding's condition, the criterion it fails, its origin, and its date, since remediation prioritized from one source's list ignores the rest of the exposure.
- The organization's severity and classification rubric, including the thresholds separating an observation from a deficiency, a significant deficiency, a material weakness, or a nonconformity.
- Control and risk linkage per finding, so exposure is expressed in terms the risk register already uses.
- The exception policy with its authority levels, maximum durations, and renewal rules.
- Named remediation owners and a realistic view of their capacity, because a queue that exceeds capacity produces silent slippage rather than triage.
- Compensating control candidates with evidence they themselves operate, since an untested compensating control is a second unevidenced claim standing in for the first.
- Prior remediation history: closures, reopenings, extensions, and repeat findings.
- The evidence that would demonstrate closure per finding, identified before the work starts rather than assembled after it.

## Workflow

**Outcome.** A classified deficiency register, corrective action plans naming the closure evidence per finding, a compensating control record for exposure carried in the meantime, an exception register with approver, grant date and expiry per entry, an aging and escalation view against the rubric's timelines, and validated closures separated from asserted ones.

**Grounding.** The severity rubric is authoritative for classification and is applied to the condition as observed, not to the remediation's difficulty. The criterion the finding fails is quoted from its source, because a finding without criteria is a preference and gets negotiated away at the first management response. Closure rests on evidence that the control operated after the fix, from the system that produces that control's evidence, over a period long enough for the control's own frequency to have occurred at least once.

**Constraints.** Every finding carries condition, criteria reference, cause where a source establishes it, effect stated as exposure, severity with the rubric it came from, and classification. Every corrective action plan names the owner, the due date derived from a stated policy or an assessor deadline, the specific actions, and the artifact that will demonstrate closure, so remediation is defined by its evidence rather than by its intent. Compensating controls are named with the exposure they carry, their own evidence source, and the date the compensation ends; a compensating control with no evidence of its own operation is recorded as proposed. Exceptions carry a named human approver at the authority level the rubric requires, a grant date, and an expiry; an exception with no expiry is a silent policy change and is written as one. Aging is measured from the finding's original date rather than from its most recent extension, since resetting the clock on extension is how a nine-month overdue item reads as thirty days old. Repeat findings are marked as repeats with the prior finding referenced, and their classification is reconsidered upward because recurrence is evidence the first cause was never addressed. Several deficiencies sharing a cause are evaluated in aggregate against the rubric before each is rated in isolation.

**Mandated order, evidence before change.** For any finding inside an open observation period, this order holds and is not scaffolding: it is mandated because remediation destroys the record of how the control operated during the period the report will cover, and a period-of-time report opines on the whole period rather than its final state.

1. Capture and date the evidence of the control in its failing state, from the system of record.
2. Perform the remediation.
3. Capture the evidence of the corrected control operating, over at least one full operating cycle of that control.
4. Validate closure against that post-remediation evidence, by someone other than the owner who performed the fix.

Reversing steps one and two cannot be repaired afterward, because the underlying data has moved on and the period cannot be re-observed.

**Parallel surface.** Individual findings, individual corrective action plans, individual exception reviews, and individual closure validations fan out and are parallel-safe; each rests on its own control, criterion, and evidence. The deduplication of one underlying deficiency that fails several criteria, the aggregation assessment that decides whether related deficiencies rise to a higher classification, the ranking of the remediation queue against actual owner capacity, the aging rollup, and the residual exposure position after compensating controls are single passes over the whole set once the fan-out returns.

**Acceptance bar.** A remediation owner could start work from the plan without a scoping conversation, and a tester could confirm closure from the named evidence without asking what to look at. Every classification cites the rubric threshold it met, every exception has a named approver and a date it lapses, and every closure is either validated with dated post-remediation evidence or recorded as asserted and unvalidated.

## Outputs

A complete run delivers this set:

- `deficiency-register.md`: every finding with condition, criteria reference, cause, effect, severity with its rubric, classification, origin, owner, and current status, including repeats flagged against the prior finding.
- `corrective-action-plans.md`: per finding, the actions, owner, due date with the source that set it, dependencies, and the exact artifact that will demonstrate closure.
- `compensating-controls.md`: what carries each exposure meanwhile, its own evidence source and operating state, its coverage of the original control objective, and the date the compensation ends.
- `exception-register.md`: each exception with what it covers, the reason, the compensating control, the named approver and authority level, the grant date, and the expiry, with expired and unapproved entries listed first.
- `aging-and-escalation.md`: overdue items aged from their original date, extension history per item, the escalation triggered by the rubric, and the queue reconciled against owner capacity.
- `closure-validation.md`: per closed finding, the post-remediation evidence, its period, who validated it independently of the owner, and the closures that remain asserted rather than validated.
- `remediation-downstream-handoff.md`: what `third-party-risk-desk` and the reporting stages inherit, including unremediated exposure, exceptions expiring inside the next reporting period, and the classification aggregation position.

Depth standard: an artifact is complete when the owner could act on it and a later assessor could re-perform the closure decision from what it names. "Improve access provisioning" is a theme; a corrective action names who runs which review, at what frequency, against which system's export, and which artifact the next test will inspect.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the ticketing system, GRC platform, or the evidence source for a closure cannot be read, the run delivers `remediation-connector-diagnostic.md` naming each unreachable source, the findings whose current status is therefore unknown, and the closures that cannot be validated. Status is never inferred from the last state anyone remembers.

Anti-fabrication guard: this register is where optimism is laundered into fact, and it happens through the status field. "Closed" is the most expensive word in the program, because everything downstream stops looking at anything marked with it: the committee sees a burndown, the auditor samples elsewhere, and the exposure sits there dated and unowned until it recurs. So a closure is written as closed only where dated post-remediation evidence exists showing the control operating, validated by someone other than the person who fixed it, and every other closure is recorded as `remediated, validation pending` or `asserted, unvalidated`, which are the honest states and the ones that keep the item in view. Severity is never softened to fit remediation capacity, a due date is never invented to fill an empty field, an approver is never named because they hold the role that usually approves exceptions, and a compensating control is never credited until its own evidence exists. An overdue item stated plainly is a working queue; a closed item nobody validated is a finding that will be rediscovered by an outsider with a worse classification and a repeat flag.

## grc_packet fields to update

- `findings[]` with `condition`, `criteria_ref`, `cause`, `effect`, `severity` carrying its rubric, `classification`, `status`, `owner`, and `due`
- `remediation[]` with `cap_id`, `covers`, `actions`, `owner`, `due`, `compensating_control`, `validation_state` from `not_validated`, `evidence_pending`, or `validated`, and `validated_by`
- `exceptions[]` with `covers`, `reason`, `compensating_control`, named `approver`, `granted_on`, and `expires`
- `risks[]` where residual rating changes because an exception now carries exposure or a compensating control reduces it, with the scale named
- `risk_acceptances[]` where the honest instrument is acceptance rather than an exception, prepared for the approver at the authority level the rubric sets
- `control_library[]` where the design state changes because remediation redesigned the control
- `approvals[]` for every exception grant, extension, severity downgrade, and closure entry that would write to the system of record
- `evidence[]` for pre-remediation and post-remediation artifacts with their `period_covered` and `collected_on`
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would write a closure, a status change, a severity downgrade, or an extension into the system of record. That entry alters the audit trail an assessor will read, and a closure entered before validation cannot be removed, only annotated. Prepare the entry, its evidence, and its validation basis, and stop at the gate.
- **Missing approval**: granting or extending an exception, accepting a deficiency without remediation, or lowering a classification transfers exposure onto the business at an authority level the rubric sets. Confidence is not authority and a reporting deadline does not create one.
- **Release integrity**: a closure, a remediation status, or a residual exposure position would go to an assessor, a customer, or a committee on evidence that shows a ticket resolved rather than a control operating.
- **Security or privacy**: closure evidence would pull personal data, credentials, customer records, or regulated content into the remediation artifact or send it beyond the authorized recipient set. Reference it by locator.
- **Source conflict**: the ticket system, the GRC register, and the control's own evidence source genuinely disagree about whether a finding was remediated. Record every reading against the field rather than adopting the one that closes the queue.
- **Connector unreachable**: the evidence source needed to validate a closure exists and cannot be read, so validation would describe a control state nobody observed.

A missing cause, an unassigned owner, or an undocumented capacity constraint is a soft gap: name it, label the assumption inline against that finding, and continue with the plan drafted and the gap in `open_questions`.

## Downstream handoffs

`third-party-risk-desk` is next and needs findings whose remediation depends on a vendor, plus exceptions granted because a vendor cannot meet a requirement. `control-testing-desk` receives the post-remediation evidence and the operating window a re-test needs to cover. `risk-register-desk` receives residual exposure changes from exceptions and compensating controls, so the register reflects what is actually carried rather than what was planned. `audit-engagement-desk` receives the remediation position for exceptions likely to appear in the report, with management response material grounded in dated evidence. `committee-reporting-desk` receives the aging view, the escalations the rubric triggered, and the exceptions expiring inside the next period. Where remediation is engineering work, the SDLC suite receives the issues, milestones, and release gating, while the finding stays open here until its evidence returns.

## Quality bar

Good remediation work is boring to read and hard to argue with. Every finding names the criterion it fails, so nobody debates whether it is a finding. Every plan names the artifact that closes it, so closure is a fact rather than a negotiation. Exceptions are few, dated, approved by someone who exists, and reviewed before they expire rather than after. Aging is measured from the original date, so the queue tells the truth about how long exposure has been carried. Repeats are flagged and rated upward, because the second occurrence of the same condition is evidence about the program rather than about the control. The strongest sign of quality is a register that got worse before it got better: classifications held at their honest level, closures moved back to unvalidated when the evidence did not arrive, and the queue shortened by work rather than by status.
