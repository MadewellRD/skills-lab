---
name: rights-request-intake-desk
description: classify a data subject rights request into the specific right under the specific regime, establish requester authority for agents and guardians, verify identity at an assurance level proportionate to what will be disclosed, compute the statutory deadline and any extension basis, define scope, and assess exemptions with the provision each rests on. use for dsar and subject access intake, right to know, delete, correct, opt out of sale or share, limit sensitive data use, portability, objection, restriction, authorized agent requests, appeals, and manifestly unfounded or excessive determinations.
---

# Rights Request Intake Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the intake artifact set, update `privacy_packet`, and continue to `rights-request-fulfillment-desk` whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the request it affects, and record it in `open_questions`. Never invent a receipt date, a verification outcome, an exemption, a provision reference, or a deadline.

A clock is already running when this desk starts. It began on the day the request arrived, not on the day someone recognized it as a request, and no halt anywhere in this suite pauses it.

## Role

This desk owns everything that happens between a request arriving and anyone searching for data. It classifies the request into the specific right under the specific regime, because "delete my data" is a different obligation with a different deadline, a different scope, and a different exemption set depending on which law the person can invoke and what relationship they have with the organization. It establishes who is asking and on what authority: the individual themselves, an agent with written permission, a parent or guardian, an executor, or an employee whose request runs through a different exemption catalogue than a customer's.

It owns identity verification at an assurance level proportionate to what will be disclosed, which cuts in both directions: releasing to the wrong person is a breach committed while answering a request made under the same law, and demanding an identity document for a request that a session re-authentication would settle is excessive collection performed in the name of protection.

It owns the deadline, computed from the recorded receipt date under the regime that set it, the extension where one is available with the ground the regime allows, the scope in records and period, and the exemptions that may apply, each attached to the provision it rests on rather than to a category name.

## Use when

- Anything arrives that a reasonable reader would treat as an exercise of a right, in any channel, whether or not it uses the word access, delete, or opt out, and whether or not it came through the request form.
- A request arrives from an agent, a guardian, a representative, or a rights-request platform acting for someone else and the authority has to be established.
- A single message asks for several things at once, or asks under a regime the requester may or may not be able to invoke.
- An extension, a refusal, a fee, or a manifestly unfounded or excessive determination is being considered.
- An appeal or a regulator referral arrives on a request that was already answered.
- The request log has to reflect a receipt date, a deadline, and a verification state that will be read back in a complaint.

## Do not use when

- The request is classified and verified and the work is searching, redacting, packaging, and delivering. That is `rights-request-fulfillment-desk`.
- The subject is a bulk retention or disposal question rather than an individual exercising a right. That is `retention-deletion-desk`.
- The subject is an opt-out signal arriving through a browser or platform mechanism rather than as an individual request. That is `consent-preference-desk`, which owns universal signal handling.
- The requester is asking a question about the notice rather than exercising a right. That is `transparency-notice-desk`.
- A parent's authority over a child's account depends on an age determination that has not been made. That is `childrens-data-desk`, whose guardian rules this desk applies.

## Required evidence

- The request as received in full, with the channel, the exact wording, any attachments, and the timestamp the organization first received it rather than the timestamp it reached the privacy team.
- The identity signals that arrived with it: the account or session it came from, the email address and whether it matches an account, prior correspondence, and anything the requester volunteered.
- Agent, guardian, executor, or representative documentation where someone acts for another, including the permission itself and whether the regime also requires confirming with the individual directly.
- The requester's location and relationship to the organization, since both decide which regimes they can invoke and whether an employment, patient, or financial-services carve-out applies.
- The identity verification policy with the assurance levels it defines and the evidence each accepts, including the account re-authentication route.
- The existing request log for this individual, including prior requests, prior responses, and any appeal.
- The exemption catalogue with citations, and any standing counsel position on how a specific exemption applies here.
- Whether a legal hold, an active investigation, or ongoing litigation touches the records in scope, which changes what can be deleted rather than whether the request is valid.

## Workflow

**Outcome.** A classification into the specific right under the specific regime with the requester type and authority established; a verification determination at a proportionate assurance level with the method recorded; the statutory deadline computed from the receipt date with the regime that set it, plus any extension with its ground and the new date; a defined scope in records, systems, and period; and the exemptions that may apply, each with the provision it rests on and the content it would cover.

**Grounding.** The receipt date is the date the organization received the request in any channel, taken from the message metadata rather than from the ticket creation time, because a request that sat in a shared mailbox for nine days consumed nine days of the deadline. Regime eligibility is established from the requester's location and relationship, and where several regimes reach the same request, the most protective deadline and the broadest scope govern the handling rather than the organization choosing among them. Motive is not a ground for refusal: a request made in the middle of a dispute, or one that is obviously preparation for litigation, is still a valid request and is handled as one.

**Constraints.** A request is not required to use any particular words, form, or channel, and telling a requester to resubmit through a portal does not restart the clock. Verification is proportionate to the sensitivity of what will be disclosed: an opt-out of sale or share needs less than an access response containing health or financial records, and the assurance level is set against the disclosure rather than against the effort. Where verification would require collecting more personal data than the organization already holds about the requester, that is recorded as a constraint on what can be answered rather than as a reason to demand documents. A failed verification is not silence: the refusal, its basis, and the appeal route go back to the requester inside the same deadline. Extensions are available only on the ground the regime allows, and where the regime requires the requester to be told of the extension and its reason within the original period, that notification is part of the extension being available at all rather than a courtesy. Exemptions attach to content rather than to requests: an exemption that covers legal advice in three documents does not exempt the response. Every exemption carries the provision it rests on, quoted from the published text, and an exemption asserted without one is recorded as not established. A fee or a refusal on manifestly unfounded or excessive grounds carries the burden of demonstrating it, and the reasoning is written at intake because it will be read later by someone deciding a complaint.

**Ordered sequence for intake.** This order is mandated because a disclosure cannot be withdrawn and because an extension the requester was never told about is not an extension:

1. Record the receipt date and start the clock, before classification and before verification.
2. Verify identity to the assurance level the disclosure requires, and release nothing before it resolves.
3. Where an extension is taken, notify the requester of the extension and its reason inside the original period.

**Parallel surface.** Where several requests are open, each is an independent unit and they fan out safely, as do the per-regime eligibility checks and the per-exemption assessments within a single request. Two steps are aggregate and run once after the fan-out returns: the multi-regime resolution for a single request, which decides which deadline and which scope govern when more than one law reaches it, and the linkage of a new request to prior requests from the same individual, since a pattern across requests is what a manifestly excessive determination has to be built on and no single request shows it.

**Acceptance bar.** Every request has a right, a regime, a requester type, a receipt date, and a deadline traceable to that date and that regime. Verification has a method, an assurance level, and a state, and the level is justified against what will be disclosed. Scope names the record types and the period. Every exemption names its provision and the content it covers. The acknowledgement that went back to the requester is recorded with what it said and when it was sent.

## Outputs

A complete run delivers this set:

- `rights-request-classification.md`: per request the right, the regime and why the requester can invoke it, the requester type and authority, everything the message asked for including the parts that are separate rights, and the regimes considered and ruled out with the reason.
- `identity-verification-record.md`: the assurance level required with the disclosure it is set against, the method used, the evidence accepted, the outcome, the date, and where verification failed the refusal wording and the appeal route sent back.
- `deadline-and-extension-calculation.md`: the receipt date with its source, the regime's period, the computed due date, the extension ground where one is taken with the notification sent inside the original period, and every other clock the request starts such as an acknowledgement window or an appeal period.
- `request-scope-definition.md`: the record types, systems, and period in scope, what is excluded and on what basis, the treatment of backups and archives, and the processors likely to hold in-scope data.
- `exemption-assessment.md`: per candidate exemption the provision, the content it would cover, whether it is established or arguable, the third-party data present in the same records, and the balancing where the regime requires one.
- `requester-acknowledgement.md`: the acknowledgement prepared for the requester in plain language, stating what was received, what will happen, the deadline, and how to escalate, held at the approval gate rather than sent.
- `rights-request-intake-downstream-handoff.md`: what `rights-request-fulfillment-desk` inherits, including the verified scope, the deadline, the exemptions to apply, and the systems the map says to search.

Depth standard: an artifact is complete when a fulfillment analyst could execute from it without re-reading the original message and a regulator could follow the reasoning from receipt to deadline. A classification naming a right without a regime, or an exemption named without a provision, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the request log, the account record, or the verification evidence cannot be read, the run delivers `rights-request-connector-diagnostic.md` naming each unreachable source and what it blocks, and it states the deadline anyway with its start event, because the clock does not depend on the connector.

Anti-fabrication guard: two fields at this desk fabricate more easily than anything else in the suite, and both are dates. The receipt date acquires a plausible value from the ticket rather than from the message that actually arrived, which quietly moves a deadline by days and turns a late response into an on-time one in the log. The deadline acquires the number the analyst remembers rather than the one the invoked regime sets, which is how a forty-five day answer gets given to a thirty-day obligation. Both are computed from a source that is named in the artifact, and where the original message cannot be located the request is recorded with the receipt date undetermined and escalated rather than dated from the ticket. The third fabrication is the exemption with no provision under it: an exemption is written with the text it rests on, and one that cannot be cited is recorded as not established, because the organization will have to produce that citation to the requester or to a regulator and a borrowed reference will not survive being read.

## privacy_packet fields to update

- `rights_requests[]` created or updated with `request_id`, `regime`, `right`, `requester_type`, `received_on`, `deadline`, `extension` with `taken`, `basis`, and `new_deadline`, and `response_state`
- `rights_requests[].identity_verification` with `method`, `assurance_level`, `state`, and `verified_on`
- `rights_requests[].scope` with the record types and period, and the processors expected to hold in-scope data
- `rights_requests[].exemptions_applied[]` each with `exemption`, `citation`, and `applied_to`
- `rights_requests[].fee_or_refusal` with the basis where either is proposed
- `active_clocks[]` for the statutory deadline, the acknowledgement window, the extension notification window, and any appeal period, each with its start event and start date
- `source_facts` with collection dates, `assumptions`, `open_questions`, `approvals` where a refusal or a fee needs authorization
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: proceeding past unresolved identity would disclose personal data to someone who is not the individual. That is a breach committed while answering a request made under the same law, and the disclosure cannot be recalled. Going quiet is not the alternative: the refusal and its appeal route go back inside the deadline.
- **Missing approval**: a refusal, a fee, a manifestly unfounded or excessive determination, or a decision to treat a regime as unavailable to this requester is a position the organization defends to a regulator and needs a named owner.
- **Production or destructive**: the next action would execute an erasure, a restriction flag, or an opt-out that changes live records or live processing.
- **Source conflict**: the channel record, the ticket, and the requester genuinely disagree about when the request arrived or what it asked for. Both readings are preserved and the earlier receipt date governs the clock while the conflict is resolved, because a deadline computed from the later one is a deadline the organization set for itself.
- **Release integrity**: an acknowledgement or a refusal would go out asserting a deadline, a scope, or an exemption that no source establishes.
- **Connector unreachable**: the request record, the account, or the verification evidence exists and cannot be read. The deadline is still stated with its start event, and the person who owns the clock is told now.

An unconfirmed requester location, an unclear record type, and an ambiguous phrase in the request are soft gaps. Interpret in the requester's favor, label the interpretation, and continue; the cost of over-scoping an intake is work, and the cost of under-scoping it is an incomplete response on the record.

## Downstream handoffs

`rights-request-fulfillment-desk` is next and needs the verified scope, the deadline with its start event, the exemptions with their provisions, the third-party data flagged at intake, the delivery form the right requires, and the channel the requester is authenticated on. `retention-deletion-desk` needs erasure requests with the hold question already raised. `processor-vendor-agreement-desk` supplies the assistance clauses the processors are held to. `breach-assessment-desk` receives any request that turns out to be an individual reporting an exposure, which arrives as a rights request more often than as an incident report. `privacy-program-metrics-desk` needs the receipt and deadline data as the population its attainment metric is computed over.

## Quality bar

Good intake work is the part of a rights request that decides whether the rest of it can succeed, and it is judged on dates and on provisions. The receipt date is sourced from the message rather than from the ticket. The deadline names the regime that set it, so a reader can check the arithmetic. Verification is argued from what will be disclosed, and an intake that demands a passport scan for an opt-out is a finding against the program rather than diligence. The classification catches every right buried in a single sentence, because "send me everything you have and then delete it" is two rights with two outcomes and organizations routinely answer only the first. And the exemption section reads like something written to be quoted back, with the provision and the specific content it covers, because that is exactly what happens to it.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
