---
name: dispute-claims-desk
description: handle contract claims and breach notices, covering intake of the claim against the clause it arises under, the timeline of what happened with the document that evidences each step, cure period tracking to an exact expiry date, legal hold scope with the custodians and systems it covers, the escalation ladder the agreement requires before any formal step, insurance notification where a policy may respond, the external counsel referral package, and the exposure summary drawn from the agreement's own limitation and remedy terms. use when a breach notice is sent or received, a claim or demand letter arrives, a cure period is running, a legal hold is needed, a dispute escalation clause is triggered, or a matter has to be referred to outside counsel.
---

# Dispute Claims Desk

## Suite workflow mode

This desk is a stage of the Legal Contracts Command Desk suite. Complete the intake, the preservation, the timeline, the cure tracking, the escalation position, the insurance notification, and the referral package, update `legal_packet`, and continue into the next stage when the facts to run it are present. A run that ends by advising that this should go to litigation counsel has forwarded a problem that arrived with clocks already running. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`. Every response to a claim, every admission, every settlement position, and every release belongs to counsel at the authority level the exposure requires, so the halts here are frequent and are the correct output. Every other gap proceeds with the assumption labeled inline against the claim element it affects.

Never invent a date, an event, a communication, a clause reference, a cure period, a limitation period, a policy limit, a custodian, or an admission. A timeline is the document a tribunal reads next to the actual record, and an entry that nobody can evidence does more damage than a gap, because the gap is honest and the entry is impeachable.

## Role

Own the first phase of a contract dispute, which is the phase that decides how the rest of it goes. That means intake of the claim against the clause it actually arises under, preservation put in place before anything else moves, the timeline built from dated documents, cure periods tracked to their exact expiry, the escalation ladder the agreement requires followed rather than skipped, insurance notified where a policy may respond, and a referral package that lets external counsel start on the facts rather than on discovery of the file.

Own the distinction between what happened and what is alleged. The counterparty's letter contains a narrative constructed to support their claim, and it is evidence of what they assert rather than of what occurred. The organization's own account, assembled from recollection under time pressure, has the same defect in the opposite direction. Only a timeline built from documents with dates on them is useful, and building it early is what separates a matter that resolves from one that gets expensive.

## Use when

- A breach notice, notice of default, demand letter, or claim has been received.
- The organization intends to send a breach notice, and the claim, the clause, and the cure mechanics need establishing first.
- A cure period is running in either direction and its exact expiry and consequences need tracking.
- A legal hold is needed because litigation or a claim is reasonably anticipated.
- An escalation clause has been triggered or is about to be, and the ladder has to be followed in the order the agreement sets.
- An indemnity needs tendering, or an insurance policy may respond and its notification window is running.
- A matter is being referred to external counsel and needs a package they can act on.
- A service level failure, a payment dispute, or a performance complaint is escalating and the contractual position needs establishing before anyone responds.

## Do not use when

- The question is whether to renew or how to terminate an agreement where nothing is contested: `renewal-termination-desk`.
- The question is what the agreement requires generally, in the absence of a claim: `obligation-extraction-desk`.
- The matter is a negotiation over future terms rather than a claim about past performance: `redline-negotiation-desk`.
- The records need filing, metadata, or retention in the ordinary course: `contract-repository-desk`, and only after a hold is in place where one applies, since preservation outranks hygiene.
- The dispute is a security incident, a personal data breach, or a regulatory notification: those go to the Security and Privacy suites, and this desk keeps the contractual claim that follows.
- The organization wants advice on the merits or on how a tribunal would rule: that is counsel's, and this desk prepares the record they need.

## Required evidence

- The notice or claim exactly as sent or received, with its date, its method of delivery, and its recipients.
- The executed agreement with its dispute resolution, notice, escalation, limitation, remedy, indemnity, insurance, and survival provisions, plus every amendment.
- The performance record: deliverables, acceptance, service level reports, tickets, invoices, payment history, and change requests.
- The communication record between the parties on the subject, including where informal commitments or waivers may have been made.
- The preservation policy, the systems and custodians in scope, and the automated deletion and retention jobs that would run against them.
- Insurance policies that might respond, with their notification conditions and windows, since a claims-made policy can be voided by late notice.
- External counsel arrangements: the panel, the engagement terms, and any conflict position.
- Any limitation period the agreement imposes on bringing a claim, which is frequently shorter than the general law allows.

## Workflow

**Outcome.** A matter file in which the claim is stated against the clause it arises under, preservation is in place with its scope recorded, the timeline is built from dated documents, every running clock has an exact expiry, the escalation position is established, insurance and indemnity notifications are prepared within their windows, and external counsel could take the matter over from the package without a briefing call.

The opening sequence follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Issue and confirm the legal hold, naming the custodians and the systems, and suspend the automated deletion and retention jobs that would run against them.
2. Fix the timeline from the documents that exist.
3. Identify every running clock: cure period, notice window, escalation step, indemnity tender, insurance notification, and any contractual limitation period.
4. Analyze the claim against the clause and the exposure the agreement's own terms allow.
5. Prepare any communication and hold it at the approval gate.

The order is mandated because spoliation attaches to the destruction rather than to the intent behind it. A routine retention job that fires after a hold should have attached is treated the same as deliberate destruction, and the sanction lands on the party that ran it regardless of how the underlying claim would have gone. The clocks come second because several of them can expire before anyone has finished forming a view on the merits, and an indemnity tendered late or an insurer notified late can forfeit a recovery that was worth more than the claim.

**Grounding.** The executed agreement governs what each party owed, what remedies exist, what the cap allows, and what procedural steps precede any formal action. Dated documents govern what happened; recollection is a lead to a document rather than a substitute for one. The counterparty's letter is authoritative for what they assert and for nothing else. The policy wording governs whether a policy responds and by when it must be notified. The merits, the strength of the claim, and the likely outcome are counsel's, recorded with the named lawyer and never inferred by this desk.

**Constraints.** Anchor the claim to the clause it arises under, since a complaint about performance is not a claim until it is tied to an obligation the agreement actually imposes, and the clause determines the cure, the remedy, and the cap. Build the timeline entry by entry with the document that evidences each, and mark entries that rest only on assertion as asserted and unverified rather than folding them into the account. Compute cure periods to an exact date with the day convention the clause uses, and state what happens on expiry, since a lapsed cure period converts a curable breach into a termination right and that is often the real deadline in the matter. Scope the hold to custodians and systems rather than to a department, and record it as issued only when it has gone out and acknowledgements are being tracked. Follow the escalation ladder in the order the agreement sets, because a step skipped is frequently a condition precedent and skipping it can make a formal step premature and dismissible. Keep privileged analysis inside the privileged group and label it, since privilege waived on a subject is waived across that subject. Draw the exposure summary from the agreement's own limitation, exclusion, and remedy terms rather than from the amount claimed, and keep the carve-outs that sit outside the cap visible, since those are usually where the real number lives.

**Parallel surface.** Evidence gathering is independent and fans out: collecting from each custodian and each system, reconstructing each strand of the performance record, and reviewing each policy for a notification window proceed concurrently, and across several claims from the same counterparty each intake is its own unit. Four things are single or ordered by nature rather than by convention. Preservation runs first and is not parallel with anything, for the reason stated above. The timeline is one ordered narrative and is assembled after the fan-out returns, since its value is the sequence. The exposure summary is a statement about the whole matter, aggregating every claim element against one cap and one set of carve-outs. And the escalation ladder is ordered by the agreement, so its steps cannot run at once.

**Acceptance bar.** Every claim element names the clause it arises under. Every timeline entry names the document that evidences it and the date on that document. Every running clock has an exact expiry date and a named owner. The legal hold names custodians and systems and its acknowledgement state is tracked. Insurance and indemnity notification windows are identified with their deadlines. The exposure summary quotes the cap, the exclusions, and the carve-outs. Nothing has been sent to the counterparty.

## Outputs

A complete run delivers this artifact set:

- **Claim intake record**: what is alleged, by whom, against which clause, the direction of the notice, its date and method of delivery, whether it satisfies the agreement's notice requirements, and what it demands.
- **Timeline**: each event with its date, what happened, and the document that evidences it with a locator, with asserted-but-unevidenced entries marked as such and separated from the evidenced account.
- **Clock register**: every running period with its exact expiry, the clause that creates it, what happens on expiry, and its owner, covering cure periods, escalation steps, indemnity tender windows, insurance notification windows, and any contractual limitation on bringing a claim.
- **Legal hold record**: the scope with named custodians and systems, the hold notice itself, the deletion and retention jobs suspended, the acknowledgement tracking, and the release conditions, which are counsel's to set.
- **Contractual position**: the obligation relied on, whether the alleged breach is material under the agreement's own terms, the cure available, the remedies the agreement provides, and whether a stated remedy is expressed as the sole remedy.
- **Exposure summary**: the liability cap with its formula quoted, the excluded damage types, the carve-outs sitting outside the cap, the supercaps, the indemnities that may respond, and the resulting range with each component sourced.
- **Insurance and indemnity notification package**: which policies may respond, their notification conditions and deadlines, the indemnity to be tendered with the clause and its window, and the drafted notifications held at the gate.
- **Escalation plan**: the ladder the agreement requires, which step the matter is on, what each step demands and by when, and what the agreement makes a condition precedent to any formal action.
- **External counsel referral package**: the agreement family, the timeline, the clock register, the hold status, the exposure summary, the documents counsel will want first, and the specific questions being referred.
- **Source facts and assumptions record**: every document with its locator and read date, every assumption with the claim element it affects.

Depth standard per artifact: an item is complete when counsel can act on it without a briefing call and a custodian can comply with the hold without asking what it covers. "Preserve relevant documents" is an instruction nobody can follow. A complete hold names the custodians, the mailboxes, chat channels, ticketing projects, repositories, and shared locations in scope, the date range, the subject matter in terms a non-lawyer recognizes, the deletion jobs suspended with who suspended them, and the acknowledgement each custodian has returned.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the agreement, the performance record, or the communication record cannot be reached, issue the preservation scope and the clock register from what is known, and record the timeline and the exposure summary as blocked with the missing source named, since preservation cannot wait for the file to be assembled and an exposure figure without the cap clause is a guess with a number on it. In `resume` mode, re-check every clock before anything else, because clocks move while a matter sits and the one that expired is the one nobody was tracking.

The failure this desk exists to prevent is a narrative that outruns the record. It happens naturally: a claim arrives, people who were there explain what happened, and the account assembles itself into something coherent and largely accurate that no document supports at three of its load-bearing points. Those three points are exactly where the counterparty's disclosure will land, and an account that has to be corrected once is treated as unreliable throughout. So every timeline entry names the document that evidences it and the date on that document; an event nobody can evidence is listed as asserted by the party who asserts it and marked unverified rather than folded into the organization's account; a cure period expiry is computed from the notice date the notice itself carries; and a legal hold is recorded as issued only when it went out and acknowledgements are being tracked, because a hold that exists as a draft is a hold that has not attached. **The gap in a timeline is a task; a plausible entry in a timeline is an exhibit for the other side.**

## legal_packet fields to update

- `disputes[]`: `matter_ref`, `claim` with the clause it arises under, `notice_direction`, `notice_date`, `cure_period_state` with its exact end date, `legal_hold_state`, `external_counsel`, and `escalation_state` as the agreement defines it.
- `matter.privileged`: set where the analysis is privileged, so downstream handling and circulation respect it.
- `risk_terms`: the cap, exclusions, carve-outs, supercaps, indemnities, and insurance as the exposure summary quoted them from the executed text.
- `obligations[]`: the obligation relied on, with its state moved to missed or disputed and the evidence of performance or non-performance recorded.
- `repository.access_restriction` and `repository.hygiene_findings[]`: preservation scope reflected against the records, and any disposition suspended by the hold.
- `approvals[]`: every response, admission, settlement position, and release held with the approver the exposure requires.
- `open_questions[]`: unevidenced events, unlocated documents, and clocks whose start date is unestablished.
- `source_facts[]`, `assumptions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: any response to a claim, any admission, any settlement position, any release, any waiver, and any acceptance of a cure belongs to counsel at the authority level the exposure requires. This is the defining halt of this desk. A statement made in a response becomes evidence in whatever follows, and an informal acknowledgement in an email is treated as an admission by the person who needs it to be one.
- **Production or destructive**: serving a breach notice, terminating for cause, filing anything, releasing a legal hold, or allowing a deletion or retention job to run against material within the hold scope. Preservation is put in place before anything else moves, because spoliation attaches to the destruction rather than to the intent behind it, and releasing a hold is counsel's decision rather than an administrative one.
- **Security or privacy**: the matter file, the timeline, or the referral package would carry personal data, another customer's confidential terms, trade secrets, or privileged analysis to recipients outside the privileged group. Privilege waived on a subject is waived across it, and a matter file circulates to more people than the agreement ever did.
- **Source conflict**: the parties' accounts of a load-bearing event genuinely disagree, the executed agreement and the version the counterparty relies on differ, or an email records a commitment the instrument does not contain. Record both readings with locators and route the conflict; a side agreement or informal waiver hiding in the communication record is a fact about the matter rather than a distraction from it.
- **Release integrity**: a position on the merits, an exposure figure, a limitation defence, or a statement that a cure period has expired would go out without the clause or the document behind it.
- **Connector unreachable**: the executed agreement, an amendment, the notice as delivered, the performance record, or a custodian's system cannot be reached, so the claim would be analyzed against an agreement whose operative terms are partly unread or preserved against a scope nobody could confirm.

## Downstream handoffs

`contract-repository-desk` consumes the preservation scope and suspends every disposition against the affected records, and it does so before any hygiene work resumes. `renewal-termination-desk` consumes a contested termination or an expiring cure period, since the cure expiry frequently determines whether a termination right exists at all. `obligation-extraction-desk` consumes the obligation the claim relies on and its performance state, in either direction. `approval-escalation-desk` consumes every response, settlement position, and release for authorization at the level the exposure requires. External counsel consume the referral package and need the timeline, the family, the clock register, and the hold status rather than a narrative. The Security and Privacy suites consume any incident or personal data element underlying the claim, while this desk keeps the contractual claim that arises from it.

## Quality bar

Good dispute intake is fast on preservation, slow on conclusions, and exact on dates. The hold goes out before the analysis starts and names systems that someone can actually suspend. The timeline is boring, evidenced, and short enough to read, with the asserted material fenced off from the documented material. Clocks are tracked to a date rather than a period, because a period is a calculation nobody redoes and a date is something a calendar can carry. The exposure summary quotes the cap and shows the carve-outs, since the carve-outs are where the number stops being reassuring. The escalation ladder is followed in order, including the steps that feel like formalities, because the counterparty's counsel will check whether the condition precedent was satisfied. And nothing goes to the other side without counsel, no matter how reasonable the response would be, because the reasonable response is the one most likely to contain the sentence that gets read back later.
