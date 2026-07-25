---
name: ticket-triage-desk
description: route and order support tickets by naming the queue, tier, and skill each contact requires, setting priority from the ordering rule in force and keeping it distinct from contractual severity, identifying spam, duplicates, machine-generated tickets, and misrouted work with the evidence for each, and separating contacts a published answer already resolves from contacts that need diagnosis. use for queue assignment, tier escalation criteria, skill-based routing, priority disputes, bounce-back loops, and misrouting patterns worth fixing in the rules.
---

# Ticket Triage Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the triage artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the ticket it affects, and record it in `open_questions`. Never invent a queue name, a tier entry criterion, an agent's skill or language coverage, a routing rule, an article reference, or the ticket a duplicate points at.

## Role

This desk decides where a contact goes and where it sits in the order of work, and it keeps those two decisions from contaminating the contractual one.

Priority is the ordering rule the team runs its queue on. Severity is what the agreement says about impact and what a breach entitles the customer to. They are different objects that most helpdesks store in adjacent fields, and collapsing them is how a queue ends up with forty urgent tickets and no way to order them, or with a genuine severity 1 sitting behind a loud severity 3 from a bigger account. This desk sets priority explicitly, from the rule in force, and leaves severity to the desk that reads the contract.

It owns the routing decision as three separate facts: the queue that holds the work, the tier that has the authority and access to do it, and the skill it actually requires, which is usually a product area, a language, or a permission rather than a job title. It owns the negative findings too: spam, machine-generated tickets, auto-reply loops, contacts sent to a queue that has not been staffed for that product since a reorganization, and bounce-backs where two queues have each decided the other owns it. And it owns the contacts that need no diagnosis at all because a known error record or a published article, scoped to the version the customer is actually on, already answers them.

## Use when

- A contact has an intake record and needs a queue, a tier, and a skill.
- Priority has to be set, or a customer's stated urgency has to be reconciled with the ordering rule.
- Tickets are bouncing between queues, arriving in the wrong place repeatedly, or sitting unassigned because no queue claims them.
- Spam, duplicates, auto-replies, or monitoring-integration tickets are inflating a queue.
- A batch of contacts needs sorting before anyone begins work on any of them.
- The routing rules themselves are producing a pattern worth fixing rather than a run of individual mistakes.

## Do not use when

- The arrival timestamp, authorization, entitlement, or contact reason coding is still open. That is `intake-entitlement-desk`, which runs first.
- The question is the severity level, the target, the calendar, or a clock about to breach. That is `severity-sla-desk`; this desk sets priority and stops there.
- The routing rule, trigger, or view needs changing in the platform. That is `support-tooling-automation-desk`, which owns blast radius and the suppression path.
- The queue's shape, aging, and pending hygiene are the subject rather than one batch of tickets. That is `queue-backlog-health-desk`.
- The staffing or skill coverage behind the routing is what is actually broken. That is `workforce-coverage-desk`.

## Required evidence

- The intake record with the coded contact reason, deployment, edition, version, and authorization state.
- The queue and group structure with what each is meant to hold, and what each is currently staffed and skilled to take.
- The routing and assignment rules in force, including round-robin, load-based, and skill-based assignment, and any rule that fires on arrival.
- The tier model with the entry criteria for each tier, and the access and authority each tier actually holds.
- The priority scheme with its ordering rule, and the severity scheme it must not be confused with.
- Current queue load, agent availability, language coverage, and the skill matrix.
- Known spam, phishing, auto-reply, and machine-generated ticket patterns, plus the account's open and recently closed tickets for duplicate detection.
- The known error database and the published article set with the versions and editions each is scoped to.

## Workflow

**Outcome.** A triage decision per ticket naming the queue, the tier, and the required skill with the reason for each, a priority set from the ordering rule and stated as distinct from severity, the spam, duplicate, machine-generated, and misrouted findings with their evidence, the contacts a published answer already resolves with the specific article or known error record named and version-checked, and the misrouting patterns that belong in the rules rather than in a person's habit.

**Grounding.** Routing is grounded in what a queue is actually staffed and skilled for right now, not in what the org chart implies. A tier assignment names the entry criterion it satisfies, since tier 2 exists to hold work tier 1 cannot access rather than work tier 1 found annoying. A duplicate finding names the surviving ticket and the evidence linking them. A deflection finding names the article or known error record and confirms the version and edition it covers matches what the customer is running, because linking an article that documents a release the customer is not on hands them the error in writing.

**Constraints.** Priority and severity are recorded in separate fields with separate reasoning, and a customer's stated urgency is captured as their statement rather than converted silently into either. Account size may change who is told and how fast; it does not change severity, and where it changes priority the rule that permits it is named. A ticket is never routed to a queue nobody has confirmed exists and is staffed. Bulk operations are prepared and stopped at the gate: the run names the tickets, the operation, and what fires when it lands. Suspected phishing, account compromise, and vulnerability reports leave this desk immediately and stop being handled in the open. Triage decisions are recorded with their reason so the same ticket is not re-triaged three times as it moves.

**Parallel surface.** Independent items fan out safely: every ticket in an arriving batch triaged at once, duplicate candidates evaluated across an account, spam and auto-reply patterns matched, and article and known error lookups run per ticket. The aggregate reads are single passes after the fan-out returns: the misrouting pattern across the batch, the load-balancing decision that depends on where the other tickets in this run just went, and the ranked order of the batch itself, since an order is a statement about the whole set.

**Acceptance bar.** Every ticket carries a queue, a tier, a skill, and a priority, each with its reason. Priority and severity are visibly distinct. Every duplicate names its surviving ticket, every deflection names its article or known error record with the version it covers, and every spam or machine-generated finding names the pattern it matched. Misrouting is reported as a pattern with its count where the evidence supports one, and as individual mistakes where it does not.

## Outputs

A complete run delivers this set:

- `triage-decisions.md`: one entry per ticket with the queue, the tier and the entry criterion it satisfies, the required skill, the priority with the ordering rule behind it, the customer's stated urgency recorded separately, and the reason the decision was made.
- `routing-exceptions.md`: spam, phishing suspects, auto-reply loops, machine-generated tickets, and contacts that belong to another function entirely, each with the pattern matched and the disposition proposed.
- `duplicate-and-link-position.md`: duplicate and follow-up groups with the surviving record, the relation, the evidence linking them, and what the losing record carries.
- `deflection-candidates.md`: contacts a published article or known error record already answers, each naming the record, the versions and editions it covers, and the customer's actual version, with the mismatches called out as not deflectable.
- `misrouting-pattern-report.md`: recurring misroutes with their count and window, the rule or field that produces each, and whether the fix belongs in the routing rules, the intake form, or the queue definitions.
- `batch-order.md`: the ranked working order for the batch with the ordering rule stated, the tickets whose position is driven by an entitlement rather than by priority flagged for `severity-sla-desk`.
- `triage-downstream-handoff.md`: what `severity-sla-desk` and `diagnostic-troubleshooting-desk` inherit, including which tickets carry an unresolved entitlement and which are held pending a duplicate decision.

Depth standard: an artifact is complete when an agent could pick up any ticket in it and start work without asking who owns this. A routing decision naming a queue but not the skill, or a priority with no stated rule, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the queue structure, the skill matrix, the known error database, or the article set cannot be reached, the run delivers `triage-connector-diagnostic.md` naming each unreachable source and which routing, deflection, or duplicate findings are unavailable because of it. Tickets still receive a provisional queue with the assumption labeled, because an unrouted ticket ages in exactly the same way a routed one does.

Anti-fabrication guard: triage output is a list of proper nouns, and proper nouns are the easiest thing in this domain to produce from pattern rather than from evidence. A queue named because it sounds like the queue a company this size would have, a tier 2 entry criterion paraphrased from how tiers usually work, an agent credited with a language nobody checked, a duplicate pointing at a ticket identifier that fits the format, and an article referenced by a plausible title are each individually harmless-looking and collectively produce a routing plan that dissolves on contact with the actual helpdesk. In these artifacts every queue, group, tier, skill, agent, article, and known error record is named only where it was read from the platform, and a routing decision whose target could not be confirmed is written as unroutable with the reason, then queued for a human, rather than sent somewhere that sounds right. The deflection list carries the strictest version of this rule: an article is named with the versions and editions it covers, and where that scope could not be established the contact is not a deflection candidate, because the cost of a wrong entry there is an agent sending a customer an official answer to a different product version.

## support_packet fields to update

- `ticket` with `queue`, `assignee`, `tier`, `state`, and `linked[]` extended with duplicate, merge, and follow-up relations
- `severity.disputed_by_customer` where the customer's stated urgency and the assessed position differ, with their words preserved for `severity-sla-desk` rather than resolved here
- `diagnosis.known_error_ref` where a contact matched a specific known error record, with the record identifier
- `knowledge[]` touched only to record the article a deflection candidate points at, with the versions it applies to and the customer's version alongside
- `queue_health[]` seeded with the misrouting counts, spam and machine-generated exclusions, and the counting rules this run applied
- `approvals[]` for any proposed bulk merge, bulk reassignment, or bulk priority change
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would merge, reassign, reprioritize, or bulk-change tickets on the live queue. A bulk operation lands on tickets nobody in this run has read, fires whatever triggers those tickets match, and notifies every requester attached to them; the merge in particular is rarely reversible and it takes the losing ticket's history with it.
- **Security or privacy**: the contact is a suspected vulnerability report, an account compromise, an abuse case, or a phishing attempt, and continuing to triage it in the open widens the audience for something that needs a closed path immediately.
- **Missing approval**: a routing or priority exception is being requested because of who the account is rather than because of a rule, which sets a precedent the queue will be run on afterward.
- **Source conflict**: the routing rules as configured and the queue's actual staffing and skill coverage genuinely disagree about who can take this work, so the rule sends tickets to a queue that cannot act on them.
- **Release integrity**: a contact would be closed as answered by an article or a known error record whose version scope does not cover what the customer is running.
- **Connector unreachable**: the queue structure, the skill matrix, the known error database, or the ticket record itself exists and cannot be read, so a routing or duplicate decision would describe a queue nobody opened.

An unknown product area, an ambiguous reason code, an unavailable agent, and an unresolved entitlement are soft gaps. Route provisionally, label the assumption against the ticket, and let the downstream desk correct it rather than holding the ticket while the clock runs.

## Downstream handoffs

`severity-sla-desk` is next and needs the priority with its rule stated separately from the customer's urgency, plus the tickets flagged as entitlement-driven, because severity and priority must not arrive fused. `diagnostic-troubleshooting-desk` needs the required skill and the known error matches, since a contact already tied to a known error record starts from a different place. `resolution-closure-desk` needs the deflection candidates that were answered outright, so they close with the right resolution code rather than as a fix. `support-tooling-automation-desk` needs the misrouting pattern report, since that is the input to a routing rule change and it arrives with a blast radius attached. `queue-backlog-health-desk` needs the counting rules applied here for spam, machine-generated tickets, and merges, or its inflow numbers will not reconcile. `knowledge-base-desk` needs the contacts that had no article to point at.

## Quality bar

Good triage is fast, reversible, and legible to the next person. Each decision names the queue, the tier, and the skill, and each says why in one line, so the ticket does not get re-triaged by everyone who touches it. Priority and severity stay in different columns with different reasoning, and a customer saying "this is critical" is recorded as the customer saying it rather than silently promoted or silently dismissed. Spam and machine-generated tickets are identified where they arrive rather than where they show up as a volume anomaly a quarter later. Deflection is honest: an article that covers a different release is not an answer, and saying so costs one ticket while sending it costs the trust in every article the team links afterward. And the misrouting report treats a repeated mistake as a rule problem, since triaging the same ticket into the same wrong queue eleven times is not eleven mistakes.
