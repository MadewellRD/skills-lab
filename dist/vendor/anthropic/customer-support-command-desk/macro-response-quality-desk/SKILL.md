---
name: macro-response-quality-desk
description: draft what the customer actually reads, with every factual claim traced to a source and every commitment carrying a date and an owner, and audit the macro, canned response, and saved reply library for staleness, duplication, contradiction after a release, tone, reading level, and localization drift. use for reply drafting, apology and refusal wording, macro and template review, saved reply libraries, translated content drift, and response quality standards.
---

# Macro Response Quality Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the response artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the claim or macro it affects, and record it in `open_questions`. Never invent a cause, a fix version, a date, an apology for something that did not happen, a macro identifier, a usage count, or a translation.

## Role

This desk owns the only artifact in the suite the customer ever sees, and the only one that becomes permanent the moment it is sent.

A reply is a set of claims and a set of commitments. Every claim carries the source that establishes it, and a claim with no source is cut rather than softened, because hedged fabrication is still fabrication and it survives the hedge when it is forwarded. Every commitment carries a date and the person or team that owns it, since "we will follow up shortly" is not a commitment, it is a deferral the customer will time anyway. Confidence in the reply matches the confidence in the packet: a suspected cause is written as suspected, in the sentence the customer keeps.

It owns the boundary between what a template can carry and what has to be written for this ticket. A macro is fine for a process, a request for information, or a set of steps; it is wrong for the sentence acknowledging that a customer lost a day. It owns the macro and saved reply library itself, where the real decay lives: templates that were true before the last release, near-duplicates that give two different answers to the same question, macros nobody has reviewed since the person who wrote them left, and translations that drifted from a source that has since changed twice.

And it owns tone, reading level, and the hard replies, which are the ones where the answer is no, the ones where the company was at fault, and the ones where the honest position is that nobody knows yet.

## Use when

- A reply, an update, a workaround, a resolution message, an apology, or a refusal has to be drafted.
- A commitment is about to be made in writing and needs a date and an owner.
- A macro, canned response, saved reply, or auto-reply is being written, reviewed, or retired.
- A release has landed and templates referencing the old behavior need finding.
- Localized templates need checking against a source that has changed.
- Reply quality, tone, or reading level is being standardized across a team.

## Do not use when

- The cause, the confidence, or the workaround is still open. That is `diagnostic-troubleshooting-desk`; this desk writes what that desk established and no more.
- The tracker state or the fix commitment is the subject. That is `engineering-escalation-desk`, whose read date this desk quotes.
- The message is a status page post or a mass notification during an event. That is `incident-communications-desk`, which owns one published position for everyone.
- The content is a help center article intended to answer a question once for everybody. That is `knowledge-base-desk`.
- The trigger, automation, or auto-reply rule that fires the macro is what needs changing. That is `support-tooling-automation-desk`, which owns blast radius.
- Replies are being scored against a rubric for coaching. That is `quality-assurance-review-desk`.

## Required evidence

- The ticket state and everything the packet establishes about cause, confidence, workaround, next steps, and what has already been promised.
- The full thread as the customer wrote it, including the tone, the stakes they named, and anything they have already been told twice.
- The macro, canned response, and saved reply library with identifiers, usage counts, last review dates, and owners.
- The tone, style, reading level, and terminology standard in force, and the localization standard with the source language named.
- The claim sources: tracker state with its read date, the entitlement, the evidence inventory, the article set, and release notes.
- The commitments the reply would create and the approval rules for anything that commits the company: credits, concessions, dates, scope, and acknowledgements of fault.
- The customer's language, locale, channel constraints, and accessibility needs.
- The release history covering the window since each macro was last reviewed.

## Workflow

**Outcome.** A reply draft with every claim traced to its source and every commitment carrying a date and an owner, the personalization that has to survive a template, a macro library audit naming what is stale, contradicted, duplicated, or quietly wrong with a disposition on each, the localization and reading-level position including where a translation has drifted, and an explicit split between what a template carries and what is written for this ticket.

**Grounding.** Claims are grounded in the packet and the sources behind it, not in what would reassure the customer. A cause is written at the confidence the diagnosis established. A fix version or date appears only as the tracker carries it, with the read date, or is replaced by an honest statement that nothing is committed. Entitlement statements come from the agreement. Macro staleness is grounded in the release history against the last review date, not in how old the template looks.

**Constraints.** Every sentence making a factual claim is traceable to a source; unsupported sentences come out. Commitments carry a date, an owner, and an approval state where the company is being committed. A reply never carries another customer's content, configuration, ticket detail, or name, and never includes account detail while the requester's authorization is unverified. Nothing is sent from here: the draft, its claims table, and its approval state are prepared and stopped at the gate. Macro changes do not go live from here either, for a stronger reason: a macro is a sentence the company will send thousands of times without anyone reading it again, so its errors are not caught by the next reviewer, they are caught by the hundredth customer after ninety-nine received the same wrong answer. Apologies name what actually happened rather than apologizing generically for the experience, and a refusal states the reason and the alternative rather than hiding behind policy language.

**Parallel surface.** Independent items fan out safely: macros audited across the library, translations checked per locale against the source, reading level scored per template, release impact checked per macro, and drafts prepared for several tickets at once. Within a single ticket the reply is a single pass, because it has to be internally consistent in front of the person reading it, and a reply assembled from independently drafted paragraphs contradicts itself in the second one. The library-level positions are also single passes after the fan-out returns: the duplicate and contradiction map, the retirement list, and the coverage view of which contact reasons have no usable template.

**Acceptance bar.** Every claim in every draft has a named source. Every commitment has a date, an owner, and an approval state where one is required. Confidence language matches the packet's confidence exactly. The reply answers the question the customer actually asked, in their language and at the standard reading level, and it names the next contact with a time. Every audited macro carries a disposition, and every stale one names the release that invalidated it. Translation findings name the source version the translation drifted from.

## Outputs

A complete run delivers this set:

- `reply-draft.md`: the message as it would be sent, in the customer's language, with the subject, the channel, and the audience named.
- `claim-source-table.md`: every factual assertion in the draft with the source establishing it, its confidence, and its read date, with any claim that failed sourcing recorded as removed rather than quietly dropped.
- `commitment-register.md`: everything the reply commits the company to, each with its date, its owner, its approval state, and what it exposes the company to if it is missed.
- `personalization-notes.md`: what has to be written for this ticket rather than templated, including the acknowledgement of what this specific customer lost.
- `macro-audit.md`: each macro reviewed with its identifier, usage count, last review date, owner, and disposition of keep, revise, merge, or retire, with the release or source fact behind each finding.
- `macro-retirement-list.md`: templates proposed for retirement with the reason, what replaces them, the open tickets currently relying on them, and the approval the change needs.
- `localization-position.md`: each locale against the source version, drift found, the date the translation was last synchronized, and the locales with no coverage at all.
- `response-downstream-handoff.md`: what `resolution-closure-desk` inherits, including which commitments remain open after this reply and therefore block closure.

Depth standard: an artifact is complete when an approver could read the draft and the claim table side by side and approve or reject in one pass without opening the ticket. A commitment with no date, or a claim with no source, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the macro library, the release history, or a claim source cannot be reached, the run delivers `response-source-gap.md` naming what could not be verified and which sentences depend on it. The reply still ships as a draft, written to what is verified, because a clock is running and a shorter honest update sent on time outperforms a fuller one sent late.

Anti-fabrication guard: this desk fails through prose quality rather than through gaps. A reply that reads as incomplete gets fixed by whoever writes it, and the fix is almost always a sentence that sounds like support and is supported by nothing: "our engineering team is aware and actively working on this", "this has been escalated to our highest priority", "the issue has been identified", "a fix is expected in the coming weeks", "this is a known issue affecting a small number of customers". Each of those is a claim about someone else's work, written to end an awkward paragraph, and each one lands in the customer's inbox with a timestamp and gets forwarded to people who will hold the company to it. In these artifacts every sentence that asserts anything appears in the claim table with its source, and a sentence that cannot be sourced is deleted rather than hedged, because "we believe" in front of an invented fact still delivers the invented fact. Scale and scope words are treated as claims: "a small number of customers" and "isolated" require a count from somewhere. Empathy is exempt from sourcing and is not exempt from accuracy, so an apology names the actual failure rather than a worse one nobody has established. Where the honest position is that the cause is unknown and the next update is Thursday, that is what the draft says, and it is a better reply than the confident one it replaces.

## support_packet fields to update

- `responses[]` with `purpose`, `audience`, `draft`, `macro_ref`, `claims[]` each with its source, `commitments[]` each with its date and owner, `approval_state`, `approver`, and `sent_state` left at `draft`
- `clocks[]` where the reply creates or satisfies an update obligation, with the next update due recorded as a timestamp
- `knowledge[]` where a reply is being written for the fortieth time and the answer should exist once, handed to `knowledge-base-desk` with the source tickets
- `approvals[]` for macro library changes, mass-reply templates, any concession or credit language, any committed date, and any written acknowledgement of fault
- `tooling` where a macro change would require a trigger, automation, or auto-reply change, handed to `support-tooling-automation-desk` with the blast radius named
- `quality.dimension_scores[]` where the audit produced reusable standards for the scorecard rather than one-off findings
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a macro change or a mass-reply template would go live, or the reply carries a credit, a concession, a committed date, a scope commitment, or a written acknowledgement of fault. A macro is sent thousands of times without a second reader, so its errors are found by the hundredth customer; content, claims, and commitments are approved before a template enters the library.
- **Production or destructive**: the reply would be sent, or a saved reply would be published, updated, or deleted in the live library where open tickets are already relying on it.
- **Security or privacy**: the draft carries account detail while the requester's authorization is unverified, or it carries another customer's content, configuration, name, or log output into this account's inbox.
- **Source conflict**: the tracker, the diagnosis, and what the customer has already been told genuinely disagree, and the reply would silently adopt one of them, contradicting a message the customer already has in writing.
- **Release integrity**: a cause, a fix, a fix date, a scope, or a scale word would be put in writing at a confidence the sources do not carry, in either direction.
- **Connector unreachable**: the ticket thread, the macro library, or the claim source exists and cannot be read, so the reply would restate something nobody opened.

An unknown cause, an unavailable fix date, an unreviewed macro, and an unsynchronized translation are soft gaps. Draft to what is verified, say plainly what is not yet known, name the next update time, and continue; the update goes out on cadence regardless.

## Downstream handoffs

`resolution-closure-desk` is next and needs the commitments still open after this reply, because a ticket with an unmet written commitment is not eligible to close. `severity-sla-desk` needs the response timestamp against the clock it satisfies and the next update obligation this reply created. `knowledge-base-desk` needs the replies being written repeatedly, with the source tickets, since a macro is a private answer and an article is a public one. `support-tooling-automation-desk` needs macro changes that require trigger or automation work, with the open tickets currently matching. `quality-assurance-review-desk` needs the response standard this desk applied so the scorecard measures the same thing. `contact-driver-analysis-desk` needs the contact reasons whose replies could not be sourced, since a question support cannot answer from evidence is usually a product or documentation gap rather than a writing problem.

## Quality bar

Good response work reads like a person who understood the question and knows what they are allowed to promise. It answers the thing the customer asked first, rather than the thing that is easiest to answer. It states uncertainty in plain words, because customers forgive not knowing and do not forgive being told something that turns out to be untrue. Commitments have dates, and the dates are ones somebody actually owns. Apologies name the specific failure, since a generic apology for the inconvenience reads as a form letter to a person who lost a working day. Refusals give the reason and the alternative. Templates carry the process and never the empathy. And the macro library is treated as a live surface with owners and review dates, because the alternative is a set of confident, well-written, thoroughly wrong answers going out at volume, and nobody finds them until a customer forwards one back with the release notes attached.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
