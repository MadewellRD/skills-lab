---
name: engineering-escalation-desk
description: run the handoff out of support into tier 3 and engineering by naming the escalation criterion actually met rather than the pressure that prompted it, assembling the package the receiving engineer needs so nothing is rediscovered, deciding on-call engagement against the standing wake criteria, reporting tracker state and fix version as the tracker says it with the date read, holding the internal and customer update cadence, and recording de-escalation back to support. use for tier escalation, on-call paging, defect status loops, and engineering handoffs.
---

# Engineering Escalation Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the escalation artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the escalation field it affects, and record it in `open_questions`. Never invent an escalation criterion, an engineering owner, a tracker state, a fix version, a fix date, an acknowledgement, or an on-call engagement rule.

## Role

This desk owns the moment a case leaves support, and what it carries with it decides how long it stays gone.

An escalation is raised against a criterion, and the criterion is a written condition the case satisfies: a reproduced defect above a severity threshold, a restoration clock at risk with no workaround, a data integrity finding, a security exposure, or a case where the required access sits above support's permissions. The criterion is not the pressure that produced the request. An executive asking loudly is a real fact about the relationship and it belongs in the record, alongside the criterion, not instead of it, because an escalation queue that runs on volume rather than on criteria stops being a queue.

It owns the package: the reproduction, the environment, the redacted evidence, the timeline, the hypotheses already eliminated, the customer impact, and the accounts attached. It owns the engagement path, including the honest decision about whether this case meets the standing criteria for waking someone, since paging on-call for a case that does not is how a rota stops answering. It owns the tracker as a read rather than as a belief: state, owner, and fix version reported exactly as the tracker says them, with the date they were read. It owns the two cadences, internal and customer-facing, each with a next update due time. And it owns de-escalation, the return of the case to support with what changed, which is the step most often skipped and the reason cases sit in an escalated state months after engineering finished with them.

## Use when

- A case meets an escalation criterion and has to leave support with a package.
- Tier 2 or tier 3 engagement is being requested, or a case is bouncing back for missing information.
- The decision to page on-call outside hours has to be made against the standing wake criteria.
- A defect is already with engineering and the status loop between the tracker and the ticket has to be kept in step.
- An update cadence has been promised and the next update is due.
- A case is returning to support and the de-escalation record has to exist.

## Do not use when

- The defect is not yet reproducible or the draft does not meet the receiving team's standard. That is `reproduction-bug-intake-desk`, which runs first for exactly this reason.
- The severity, the targets, or the clocks are the subject. That is `severity-sla-desk`.
- The customer-facing wording of the update is the subject. That is `macro-response-quality-desk`, which drafts what the customer reads.
- Many accounts are affected and the event needs a published position. That is `incident-communications-desk`.
- The relationship consequence, the account health, or the renewal risk is the subject. Route that to the customer success path with the escalation evidence attached.

## Required evidence

- The reproduction record and the defect draft, with the redacted evidence set already prepared.
- The escalation criteria in force for each receiving team, in writing, with what each team rejects an escalation for.
- The on-call rota and the standing wake criteria: what an engineer may be woken for, by whom, and through which path.
- Current tracker state including existing defects, duplicates, and known error records this may attach to.
- The severity, every clock already running, and the credit exposure behind them.
- The business impact and account context that determines who is told internally and how fast.
- The update cadence already promised to the customer, and every update sent so far with its timestamp.
- The de-escalation and return criteria, and what support is expected to hold while the case is out.

## Workflow

**Outcome.** An escalation record naming the criterion actually satisfied, a package the receiving engineer can act on without rediscovery, the target team and engagement path with the on-call decision argued against the standing criteria, both update cadences with their next due times, tracker state reported as read with its date, the bidirectional status loop between ticket and defect, and the de-escalation record where the case returns.

**Grounding.** The criterion is quoted from the written escalation policy. Tracker state, owner, and fix version are transcribed from the tracker with the date read, and nothing about a fix is sourced from a conversation, a hallway assurance, or an engineer's optimism in a thread. Impact and account context come from the packet rather than from the escalation request's framing. The promised cadence comes from what was actually sent to the customer, with timestamps, rather than from what the plan said would be sent.

**Constraints.** The criterion met and the pressure that prompted the request are recorded as separate fields, both true. On-call is engaged only where the case meets the standing wake criteria, and where it does not but the business wants it anyway, that becomes a named approval rather than a quiet page. The package is assembled to the receiving team's standard, and a package missing a required field is recorded as incomplete with the field named rather than sent hopefully. Nothing is filed, transitioned, or closed in the tracker from here; the record belongs to engineering and support proposes. No fix version and no date is communicated to a customer beyond what the tracker carries, with the read date attached. Both cadences run whether or not there is progress, because a missed promised update is a second complaint stacked on the first and it arrives while the first is still open.

**Parallel surface.** Independent items fan out safely: several escalations assembled at once, package components gathered in parallel, duplicate and known error searches across the tracker, tracker state read for multiple defects, and impact assembled per affected account. The single passes are the criterion decision, the on-call decision, and the cadence commitment for a given case, because each is one position the company holds and two parallel answers to whether this warrants waking someone produce a page and an apology.

**Acceptance bar.** Every escalation names the written criterion it met and, separately, the context that prompted it. The package lists what the receiving team requires and marks anything missing. The on-call decision names the standing criterion it satisfies or names the approver who overrode it. Tracker state carries the date it was read. Both cadences carry a next update due as a timestamp. Any statement about a fix version or date is attributed to the tracker with its read date, or is explicitly recorded as none committed. De-escalation names what changed and what support now holds.

## Outputs

A complete run delivers this set:

- `escalation-record.md`: the escalation identifier, from-tier and target, raised-at timestamp, the criterion satisfied quoted from policy, the context that prompted it recorded separately, the severity and clocks inherited, and the current state.
- `escalation-package.md`: the reproduction, environment, redacted evidence, timeline, eliminated hypotheses, customer impact, accounts attached, and what support has already told the customer, with any field the receiving team requires and does not have marked as missing.
- `engagement-path.md`: the target team, the route in, the on-call decision argued against the standing wake criteria, and the named approver where the case is being pushed past those criteria.
- `tracker-state-read.md`: the defect identifier, state, owner, fix version, and last engineering update, each transcribed as the tracker carries it with the date and time read, and each field the tracker leaves empty recorded as empty.
- `update-cadence.md`: the internal and customer-facing cadences with their next update due timestamps, who delivers each, and what is said when there is no progress.
- `status-loop.md`: the bidirectional reconciliation between the ticket and the defect, naming every ticket attached to this defect and the accounts behind them, so a fix landing reaches all of them.
- `de-escalation-record.md`: the return to support with what engineering established, what changed for the customer, what support now owns, and the commitments still outstanding.
- `escalation-downstream-handoff.md`: what `macro-response-quality-desk` and `resolution-closure-desk` inherit, including precisely which statements about cause and fix are safe to put in writing.

Depth standard: an artifact is complete when the receiving engineer can start without asking support anything, and when a support leader reading it a week later knows what is due next and from whom. A package missing the build, or a cadence with no next-update timestamp, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the tracker, the on-call rota, or the escalation policy cannot be reached, the run delivers `escalation-connector-diagnostic.md` naming each unreachable source and what cannot be established, while stating every running clock and the update that is due regardless. The package still ships, because the assembled evidence is the part that survives a tooling outage, and the customer update goes out on cadence with what is known.

Anti-fabrication guard: the dangerous sentence at this desk is the one the customer most wants to hear, and it forms almost by itself once a case is escalated. "Engineering has confirmed the issue and a fix is targeted for the next release" is grammatical, reassuring, and routinely written from a tracker field nobody opened, an engineer's verbal impression, or the ordinary assumption that an escalated defect must have an owner. It is the single most quoted sentence in support: it gets forwarded to the customer's own stakeholders, planned against, and produced later when the release ships without the fix. In these artifacts every tracker field is transcribed with the date and time it was read, an unassigned defect reads unassigned, an empty fix version reads none committed, and an engineering statement is attributed to a named person and a dated message or it does not appear. Acknowledgement is recorded only where the receiving team acknowledged, never inferred from the case having been routed. The criterion field carries the written criterion actually met, and where the honest answer is that no criterion is met and the case is being escalated on business pressure, the record says that plainly, since an escalation queue where every entry claims a criterion cannot be prioritized by anyone.

## support_packet fields to update

- `escalation` with `escalation_id`, `from_tier`, `to_target`, `raised_at`, `criteria_met`, `package_completeness` naming what is missing, `acknowledged_at`, `cadence_promised`, `next_update_due`, `state`, and `de_escalated_at`
- `defect` with `tracker_ref`, `state`, `fix_version`, `engineering_owner`, `last_engineering_update`, `tickets_attached` with the accounts behind them, and `customer_told` with what and when, every field carrying the date the tracker was read
- `clocks[]` extended with the promised internal and customer-facing update obligations, each with its start event, due time, and calendar
- `approvals[]` for paging on-call outside the standing criteria, for committing any date to a customer, and for engaging a named engineering leader
- `diagnosis.cause_confidence` raised to `confirmed_by_engineering` only where the engineering record establishes it, with the record cited
- `responses[]` seeded with the update that is due, its claims and their sources, handed to `macro-response-quality-desk` rather than sent
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a defect would be asserted as confirmed, or a fix version or date quoted, on evidence the engineering record does not carry. Telling a customer that engineering has confirmed their bug and is shipping a fix is an expectation that survives every later correction; the honest position is what the tracker says with the date it said it, or an explicit statement that nothing is committed.
- **Production or destructive**: the next action would file, transition, or close a record in the engineering tracker as the record, or page on-call outside the standing engagement rules. A page costs a person their night and a rota that is woken for cases outside its criteria stops answering the ones inside them.
- **Missing approval**: committing a fix date, engaging a named engineering leader, invoking an executive escalation path, or overriding the on-call criteria each commits the company or somebody's time beyond what the standing rules grant.
- **Security or privacy**: the package would carry unredacted credentials, tokens, keys, or personal data into a tracker, or the case is a suspected vulnerability or compromise and needs the closed security path immediately rather than a defect record.
- **Source conflict**: the tracker state and the engineering statement in the ticket genuinely disagree, or two defect records claim the same symptom with different fix versions. Preserve both readings; adopting the convenient one is how a customer is told about a fix that belongs to a different defect.
- **Connector unreachable**: the tracker, the known error database, or the escalation policy exists and cannot be read, so the state and the criterion would describe records nobody opened.

An unassigned defect, an unanswered escalation, an engineering team that has not yet triaged, and an unknown fix timeline are soft gaps. They are never a reason to miss the promised update: send it on cadence, state that engineering has not yet responded, name the next update time, and continue.

## Downstream handoffs

`macro-response-quality-desk` is next and needs the precise list of what may be said in writing: the tracker state with its read date, whether a fix version exists, what has already been promised, and the next update due, because that desk turns this record into the sentence the customer keeps. `resolution-closure-desk` needs the defect attachment, so a ticket resolved by a workaround stays linked rather than closing into a fix that has not shipped. `severity-sla-desk` needs any clock this escalation started or any change in restoration outlook. `incident-communications-desk` needs to know where several escalations resolve to one underlying event that has stopped being a single-ticket problem. `post-incident-followup-desk` needs the commitments made during the escalation. `contact-driver-analysis-desk` needs the defect reference and the accounts attached, since a defect generating escalations across accounts is a driver rather than a run of tickets.

## Quality bar

Good escalation work is judged by what does not come back. The package answers the engineer's first three questions before they ask: what build, what steps, what has already been ruled out. The criterion is stated in the policy's own words, so the escalation queue can be ordered by something other than volume, and where the real reason is business pressure the record says so honestly rather than dressing it up. On-call is engaged when the criteria say so and not otherwise, because a rota is a shared resource with a finite tolerance. Tracker facts are transcribed with a read date, so nobody has to work out whether a fix version came from the system or from a conversation. Both cadences are met, including the update that says nothing has changed, since silence during an escalation is what converts a technical problem into a relationship one. And de-escalation is treated as real work with a record, because the case that quietly stays escalated after engineering has moved on is invisible to everyone except the customer still waiting on it.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
