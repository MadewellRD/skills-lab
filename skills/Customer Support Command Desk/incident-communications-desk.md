---
name: incident-communications-desk
description: run the customer-facing side of a mass event by establishing affected scope from system evidence with an explicit statement of what is not affected, recording the impact start timestamp every credit and outage letter runs from, publishing one holding position with the next update time before the cause is known, holding the update cadence, pointing every reply and channel at that position, and building the proactive notification list from a query rather than an estimate. use for outages, degradations, status page updates, mass notifications, and incident ticket surges.
---

# Incident Communications Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the incident communications artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the scope or update it affects, and record it in `open_questions`. Never invent an affected-account list, an account count, an impact start timestamp, a cause, a restoration estimate, or a status page update that was not published.

## Role

This desk owns what customers are told while something is broken for many of them at once, which is the point where the one-contact model stops working and forty agents start writing forty different explanations of the same event inside the same hour.

It owns the affected scope, determined from system evidence, and it owns the harder half of that sentence: an explicit statement of what is not affected. Customers make decisions on the negative claim, so it carries more risk than the positive one and it is the one most often written from inference. The method that produced the scope is recorded alongside it, because a scope from a tenant query and a scope from a plausible guess look identical once they are in a status post.

It owns the impact start timestamp, taken from system evidence rather than from when the alert fired or the incident was declared. That single field is what every credit calculation, every contractual notification window, and the eventual outage letter run from, and it is routinely off by the length of time it took someone to notice.

It owns one published holding position, naming impact, non-impact, and the time of the next update, published before the cause is known. It owns the update cadence, met whether or not there is progress. It owns the instruction that points every reply and every channel at that published position rather than restating it, since restatements diverge and get screenshotted next to each other. It owns the proactive notification list produced by a query with the query recorded. And it owns recovery confirmation from both system evidence and at least one affected customer before resolution is declared.

## Use when

- Multiple accounts are affected by the same event and a published position is needed.
- Tickets are arriving about the same symptom faster than they can be individually answered.
- A status page post, a mass notification, or a customer-facing statement about an event has to be drafted.
- An update is due on a committed cadence during an ongoing event.
- Affected accounts have to be identified for proactive notification or for a contractual obligation.
- Recovery has to be confirmed and the event declared resolved to customers.

## Do not use when

- The event affects one account and the work is a single ticket's severity and clocks. That is `severity-sla-desk`.
- The subject is the internal incident command, the technical mitigation, or the engineering root cause. Route those to the reliability and engineering path; this desk owns only what customers are told.
- The event has ended and the obligations it created are the subject: outage letters, credits, and incident-generated tickets. That is `post-incident-followup-desk`.
- The message is one customer's reply rather than the published position. That is `macro-response-quality-desk`, which points replies at what this desk publishes.
- The surge of tickets needs routing and ordering. That is `ticket-triage-desk`, which attaches them to the incident reference this desk establishes.

## Required evidence

- System evidence establishing what is affected and what is not: error rates, availability and latency by service, region, shard, cluster, tenant cohort, edition, and client version.
- The impact start timestamp from telemetry, with the detection time recorded separately so the gap between them is visible.
- The incident severity scheme, which is not the ticket severity scheme, and the named owner of the declaration.
- The account and tenant identification query behind any affected-customer list, with the query itself and the time it was run.
- The status page and notification surfaces with their subscriber populations, their component structure, and who may publish to each.
- Contractual notification obligations for affected accounts, including any window in which notification is owed.
- The tickets already arriving about the event, and the reference they will be attached to.
- The approval path for a public statement and the standing pre-approved holding language where it exists.

## Workflow

**Outcome.** The affected scope with the method that determined it and an explicit non-impact statement, the impact start timestamp, one published holding position naming impact, non-impact, and the next update time, the update cadence with each update timestamped and each due time recorded, the instruction pointing every reply and channel at the published position, the proactive notification list with the query behind it, and recovery confirmation from both system evidence and an affected customer before resolution is declared.

**Grounding.** Scope comes from telemetry and tenant queries, with the query text and run time recorded, and the scope method is written as system evidence, inferred, or undetermined so a reader knows which they are holding. The impact start timestamp comes from the first system signal, not from the declaration. Subscriber populations come from the notification platform, since a status page reaches only those subscribed to it and treating it as reaching everyone is how an account learns about an outage from a competitor. Every published update is recorded as published with its timestamp and its text.

**Constraints.** Nothing is published from here; the position is drafted with its approval named and stopped at the gate, and where pre-approved holding language exists that is the fastest correct path. A holding statement needs no cause: impact, non-impact, and the next update time are sufficient and are the right thing to publish while approval is sought. No estimate of restoration is published unless an owner has committed to it. The affected list is a query result, and where the query could not be run the scope is recorded as undetermined rather than described with a scale word. One customer's name, configuration, or detail never appears in a communication to another. Updates go out on cadence whether or not there is progress, and an update with nothing new says so rather than being delayed until it can say something better.

**Mandated order, which runs from when impact started rather than from when the cause is understood.** Steps 2 and 4 do not wait for certainty. An event with no published position produces a queue of agents each explaining it differently, in writing, inside the same hour, and those replies get compared with each other in public:

1. Determine the affected scope from system evidence and record the impact start timestamp. Every clock, every credit calculation, and the outage letter run from that moment.
2. Publish one holding position naming what is affected, what is not, and when the next update comes, before the cause is known.
3. Point every reply and every channel at that published position rather than restating it in their own words.
4. Update on the committed cadence whether or not there is progress.
5. Confirm recovery from system evidence and from at least one affected customer before declaring resolution.
6. Close the customer-facing incident only once the follow-up owed to each affected account is recorded, because the tickets an event generates outlive the incident record that would otherwise close them.

**Parallel surface.** Independent items fan out safely: accounts identified as affected across tenants and regions, evidence pulled per service and per cohort, notification lists assembled per channel and per locale, arriving tickets attached to the incident reference, and translations of an approved update prepared per locale. The scope determination and the single published position are single passes by design, because the entire value of them is that only one exists, and two parallel scope reads produce two different non-impact claims that customers will place side by side.

**Acceptance bar.** Scope names what is affected, what is not, and the method behind both. The impact start timestamp names the system signal it came from, with detection time recorded separately. The holding position names impact, non-impact, and a next update time, and needs no cause to be correct. Every update carries its timestamp and its due time was met or the miss is recorded. The notification list carries the query and its run time. Recovery confirmation names both the system evidence and the affected customer who confirmed.

## Outputs

A complete run delivers this set:

- `affected-scope.md`: what is affected and what is not, by service, region, tenant cohort, edition, and client version, with the scope method stated as system evidence, inferred, or undetermined for each claim.
- `impact-timeline.md`: the impact start timestamp with its system signal, detection time, declaration time, mitigation and recovery times as they land, all in one stated timezone.
- `holding-position.md`: the single published statement naming impact, non-impact, and the next update time, with its approval state and approver named.
- `update-log.md`: every update with its timestamp, the surface it went to, its text, and the next due time it committed to, with any missed update recorded as missed rather than omitted.
- `channel-alignment.md`: the instruction pointing replies, chat, phone greeting, in-product notice, and social responses at the published position, with the exact wording agents may use and what they must not add.
- `notification-list.md`: the accounts to be proactively notified, the query that produced them with its run time, the contractual notification obligations that apply, and the accounts that could not be identified.
- `recovery-confirmation.md`: the system evidence showing recovery, the affected customer who confirmed it, the timestamp of each, and the residual impact still outstanding.
- `incident-comms-downstream-handoff.md`: what `post-incident-followup-desk` inherits, including the confirmed scope, the impact window, every commitment made publicly, and the accounts owed a written explanation.

Depth standard: an artifact is complete when an agent taking a call mid-event can answer from it without improvising and a support leader can see what has been said publicly and what is due next. A scope with no method, or an update log with no next-due times, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where telemetry, the tenant query path, or the status page cannot be reached, the run delivers `incident-scope-gap.md` naming each unreachable source and stating that scope is undetermined. A holding position still ships for approval, written to impact reported by customers with that attribution stated, because publishing nothing during an event is itself a decision and it is the worse one.

Anti-fabrication guard: an outage compresses time, and under time pressure scope gets written from inference and phrased as fact. The specific failure is the negative claim: "customers on other regions are unaffected", "this is limited to a subset of accounts", "the API is not impacted", each written because nobody had contrary evidence rather than because anybody ran a query. Customers act on those sentences, they stop investigating their own systems, and every one that turns out to be wrong converts a technical outage into a credibility event that outlasts it. Scale words carry the same weight as numbers here: "a small number of customers" is a count claim, and it is quoted back with the actual number attached. In these artifacts every scope claim carries its method, an affected list is a query result recorded with its query and run time, and where nobody ran a query the scope reads undetermined and the published position says impact is still being assessed, which is an honest and entirely publishable sentence. The impact start timestamp is taken from the first system signal, never from the declaration, since setting it to the declaration silently shortens every credit window and understates every outage letter. And an update appears in the log only if it was published; a drafted update that never went out is recorded as a missed commitment, because the customers waiting on it experienced silence regardless of what exists in the drafts folder.

## support_packet fields to update

- `incident` with `incident_id`, `impact_started_at` from system evidence, `declared_at`, `severity` on the incident scheme, `affected_scope`, `scope_method`, `accounts_identified` with the query behind it, `published_position`, `status_page_state`, `updates_published[]`, `next_update_due`, `mitigated_at`, `resolved_at`, `recovery_confirmed_by`, `rfo_committed`, `rfo_due`, and `credits_triggered`
- `clocks[]` extended with the next status update obligation and any contractual notification window, each with its start event and due time
- `ticket.incident_ref` on every ticket attached to the event, so none of them closes because the incident closed
- `responses[]` for the holding position and each update, with claims and their sources, commitments, approval state, and approver
- `approvals[]` for the status page post, the mass notification, any public statement about cause or scope, and any restoration estimate
- `severity` left on the ticket scheme and kept distinct from the incident severity, which uses a different scheme and a different declaration owner
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a status page post, a mass notification, or a public statement about cause or scope would go out. It reaches every subscriber at once, it is archived, screenshotted, and quoted, and it is read by press, competitors, and the customer's own security team as the company's position. A holding statement naming impact and the next update time needs no cause and is the correct thing to publish while approval is sought.
- **Production or destructive**: the next action would publish, edit, or resolve a status page component, send a mass notification, or bulk-update the tickets attached to the event.
- **Security or privacy**: the event is or may be a security incident, a data exposure, or a compromise, where notification content and timing carry regulatory consequence and belong to the path that owns those obligations; or the notification list would expose one customer's identity to another.
- **Source conflict**: telemetry and customer reports genuinely disagree about who is affected, which is the situation where a confident non-impact claim does the most damage. Publish the impact claim, state the assessment as ongoing, and preserve both readings.
- **Release integrity**: a cause, a scope, or a restoration estimate would be published on evidence that cannot carry it. Understating scope leaves affected customers uncontacted and unpaid; overstating it triggers credits and escalations the event did not warrant.
- **Connector unreachable**: telemetry, the tenant identification path, or the status page exists and cannot be read, so scope or publication state would describe something nobody observed.

An unknown cause, an unavailable restoration estimate, an incomplete account list, and an unquantified user impact are soft gaps and never a reason to miss an update. Publish on cadence with what is established, say plainly what is still being assessed, name the next update time, and continue.

## Downstream handoffs

`post-incident-followup-desk` is next and needs the confirmed scope, the impact window with its start timestamp, every public commitment made during the event, and the accounts owed a written explanation, because the outage letter and the credit calculation both run off those fields. `macro-response-quality-desk` needs the published position and the exact reply wording agents may use, so forty replies say one thing. `ticket-triage-desk` needs the incident reference so arriving contacts attach rather than each entering diagnosis separately. `resolution-closure-desk` needs the tickets held open by the event, since an incident closing does not resolve the individual problems raised during it. `severity-sla-desk` needs the clocks the event started, including any contractual notification window. `queue-backlog-health-desk` needs the volume the event generated flagged, or the week's inflow reads as a trend.

## Quality bar

Good incident communication is fast, singular, and boring in exactly the right way. One position exists, everybody points at it, and no agent is left improvising an explanation in writing to a customer who will compare it with a colleague's. The first post goes out before the cause is known, because impact and a next update time are enough and waiting for certainty is what produces the twenty-minute silence customers remember. The non-impact statement is treated as the highest-risk sentence in the post and is written only from a query. The impact start timestamp comes from telemetry, since it is what credits and outage letters are computed from and nobody argues about it later if it was right at the time. Updates land on the committed cadence including the ones that say nothing has changed. Recovery is confirmed by a customer as well as by a graph, because the graph recovering and the customer's queue draining are different events. And every ticket the event generated is still visible after the incident is closed, because those customers did not stop having a problem when the status page went green.
