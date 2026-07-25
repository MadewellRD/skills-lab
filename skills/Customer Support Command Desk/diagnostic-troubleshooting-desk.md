---
name: diagnostic-troubleshooting-desk
description: take a support symptom to a cause by carrying hypotheses with the observation that would confirm or eliminate each, building an evidence inventory from logs, traces, har captures, configuration exports, and diagnostic bundles with collection times and retention limits, separating product defect from configuration from integration from customer environment from expected behavior, and stating the cause at the confidence it was established. use for troubleshooting, log and trace analysis, known error matching, workarounds, and root cause isolation on a live ticket.
---

# Diagnostic Troubleshooting Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the diagnostic artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the hypothesis or evidence item it affects, and record it in `open_questions`. Never invent a log line, an error code, a trace identifier, a configuration value, a timestamp, a known error record, or a cause.

## Role

This desk owns the distance between a symptom and a cause, and it owns being honest about how far along that distance the ticket actually is.

The work is carried as hypotheses, each paired with the observation that would confirm or eliminate it, because that pairing is what separates diagnosis from pattern matching. A symptom that resembles a known failure is a hypothesis, not a finding. The evidence inventory records what was actually collected: from which system, at what time, covering which window, and where the source truncated it, since telemetry has a retention window and a log that aged out is unavailable rather than clean.

It owns the fault domain, which is the decision that determines who fixes this: product defect, configuration, integration, customer environment, data, third party, capacity, expected behavior, or an enablement gap where the product works and the customer was never shown how. It owns the cause stated at the confidence it was established, suspected, isolated, or confirmed by engineering, rather than at the confidence the customer would prefer. It owns the workaround with its real cost to the customer, since "export it manually each morning" is a different answer at four records than at forty thousand. And it owns the failed lines of inquiry, written down, so the next person starts further along instead of repeating three days of work.

## Use when

- A symptom is present and the cause is not isolated.
- Logs, traces, error records, configuration exports, HAR captures, or diagnostic bundles need collecting, reading, and correlating against a window.
- A symptom needs matching against the known error database or against prior tickets with the same signature.
- Something changed on either side and the change history has to be lined up against when the symptom started.
- A workaround has to be found, and its cost to the customer stated.
- A ticket is being resolved as user error, working as designed, or not a bug, and the evidence for that has to hold.

## Do not use when

- The severity, the targets, or a clock about to breach is the subject. That is `severity-sla-desk`, whose next update time constrains how long this desk may run in silence.
- The cause is understood and the work is making it reproducible for engineering. That is `reproduction-bug-intake-desk`.
- The case is leaving support and the package is the subject. That is `engineering-escalation-desk`.
- Many customers are affected at once and the scope has to be established from system evidence. That is `incident-communications-desk`.
- The recurring cause across many contacts is the subject rather than this one ticket. That is `contact-driver-analysis-desk`.

## Required evidence

- The symptom as reported, with the exact version or build, edition, deployment model, region, and configuration the customer is actually on rather than what the account record says they bought.
- Application and platform logs, traces, spans, and error records for the affected tenant across the window the symptom covers, with the retention window of each source stated.
- Tenant configuration state and the configuration audit history, including who changed what and when.
- Authentication, permission, and entitlement state where the symptom touches access.
- Recent change on both sides: releases, feature flag changes, migrations, and infrastructure events on the company side; upgrades, integrations, network changes, policy changes, and new users on the customer side.
- The known error database, prior tickets with the same signature, and the release notes covering the window.
- Client-side evidence where the symptom is in the browser or the app: HAR capture, console output, device and client version, and network path.
- The diagnostic collection the customer can reasonably be asked to run, and what it costs them to produce it.

## Workflow

**Outcome.** A diagnosis carried as hypotheses with their tests and results, an evidence inventory with collection times, windows, and retention limits, a fault domain assignment, a cause stated at the confidence it was established, a workaround with its cost, and the failed lines of inquiry recorded.

**Grounding.** System evidence is authoritative for what happened, bounded by retention and instrumentation coverage. The engineering record is authoritative for defect state. Documentation is authoritative for documented expected behavior against a stated version, and a mismatch between documentation and observed product behavior is a finding to route rather than a resolution to send. Agent notes and the team's working belief are evidence of what someone thought at the time, not evidence of what happened, and the distance between those two layers is where most real findings in this domain live: the ticket resolved as user error against logs showing a server-side timeout, the "known issue" that was never matched to a known error record.

**Constraints.** Every hypothesis names the observation that would eliminate it, and an untested hypothesis stays untested rather than becoming a conclusion by elimination of the others. A cause carries its confidence label in the same sentence, and "known issue" is a specific claim that this symptom matched a specific known error record, travelling with that record's identifier or it is not that claim. Absence of evidence inside a covered window is a finding; absence outside the retention window is a statement about retention and is written that way. Evidence is redacted before it leaves the ticket, and the redaction is recorded. Nothing runs in the customer's production environment from here: enabling verbose logging, restarting a service, clearing a cache, rerunning a job, and querying live data are prepared with their expected impact and stopped at the gate. Not reproduced and working as designed are different findings, and neither one is a cause.

**Parallel surface.** Independent items fan out safely: hypotheses tested against different evidence sources at once, log, trace, configuration, and audit pulls run in parallel for the same window, client-side and server-side evidence collected simultaneously, known error matching against several signatures, and several tickets with the same symptom investigated concurrently. The correlation pass is a single pass after the fan-out returns: lining the change history up against the symptom onset, reconciling client and server timestamps into one timeline, and assigning the fault domain are each statements about the whole evidence set, and a fault domain assigned per source produces four different answers.

**Acceptance bar.** Every hypothesis carries its test and a result of confirmed, eliminated, or untested. Every evidence item names its system, its collection time, the window it covers, where retention truncated it, and its redaction state. The fault domain is assigned with the evidence that separates it from the neighbouring domain. The cause carries its confidence, and where the cause is unconfirmed the artifact says so in the same place the customer-facing answer will be drafted from. Every workaround states what it costs the customer to run.

## Outputs

A complete run delivers this set:

- `diagnosis.md`: symptom as reported against symptom as observed, the hypothesis set with each test and result, the fault domain with the evidence that assigned it, the cause with its confidence, and what remains unexplained.
- `evidence-inventory.md`: every item collected with its source system, scope, collection timestamp, the window it covers, the retention limit that truncated it, and its redaction state.
- `timeline.md`: symptom onset against change history on both sides, with client and server timestamps reconciled to one timezone and the skew named where it exists.
- `known-error-match.md`: the known error record or prior ticket signature this symptom matched with its identifier, or an explicit statement that no match was found and what was searched.
- `workaround.md`: the workaround, the exact steps, the versions and editions it holds for, what it costs the customer to run, and how long it is expected to be needed.
- `customer-diagnostic-request.md`: the collection to ask the customer for, written so a non-specialist can run it, with what each item will establish and what it will not.
- `production-action-request.md`: any step that would run in the customer's environment, with its expected impact, its reversibility, and the approval it needs, prepared rather than performed.
- `diagnostic-downstream-handoff.md`: what `reproduction-bug-intake-desk` and `engineering-escalation-desk` inherit, including the hypotheses still open and the evidence that could not be collected.

Depth standard: an artifact is complete when another engineer could take the ticket over and know what has been ruled out and why. A hypothesis list with no tests, or a cause with no confidence label, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where logs, traces, or configuration state for the affected tenant and window cannot be reached, or the window has aged past retention, the run delivers `diagnostic-evidence-gap.md` naming each unreachable source, the window it would have covered, and precisely which hypotheses are untestable as a result. The hypothesis set, the timeline from what is reachable, and the customer collection request still ship, because those are what make the next attempt cheaper.

Anti-fabrication guard: the failure mode here is fluency. A support engineer who has seen this symptom shape forty times can write a cause that is grammatical, technically specific, and entirely uncollected, and it is indistinguishable from a real diagnosis right up until the customer hits the same fault again with the ticket closed. The tells are small: an error code that fits the product's format but appears in no log that was pulled, a timestamp with no source, a configuration value quoted from what the default usually is, "the logs show" where no log was reachable, and "known issue" attached to no record identifier. In these artifacts every observation is quoted from a named source with its collection time, an error string appears only where it was read, and a hypothesis that could not be tested is written as untested and stays in the hypothesis section rather than migrating into the cause line. Where the window aged out, the artifact says the window aged out; it never says nothing was found, because those are different sentences and only one of them is true. A cause established by resemblance is `suspected`, and it stays `suspected` in every downstream artifact until an observation moves it, including in the reply the customer will keep.

## support_packet fields to update

- `diagnosis` with `symptom_reported`, `symptom_observed`, `fault_domain`, `hypotheses[]` each with its `test` and `result`, `evidence[]` each with `collected_from`, `collected_at`, `covers_window`, `retention_limit`, and `redaction_state`, `known_error_ref`, `workaround_given`, `cause`, and `cause_confidence`
- `ticket.version_or_build`, `deployment`, `environment`, and `product_area` corrected where the evidence contradicts what intake recorded
- `severity` where the observed impact differs from the reported impact, handed back to `severity-sla-desk` with the evidence rather than restated here
- `approvals[]` for any step that would run in the customer's production environment, with the expected impact and its reversibility
- `clocks[]` where the next update obligation is affected by how long collection will take
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: logs, traces, or configuration state for the affected tenant and window cannot be read, or the window has aged past retention. A cause asserted without them describes something nobody observed. Evidence that is merely absent is a soft gap; evidence that cannot be reached is this halt.
- **Production or destructive**: the next step would run in the customer's environment, including enabling verbose logging, restarting a service, clearing a cache, failing over, rerunning a job, or executing a query against live data. Prepare it with its expected impact and stop at the gate.
- **Security or privacy**: the evidence carries credentials, session tokens, API keys, connection strings, or personal data and would leave the ticket unredacted, or the investigation has turned into a suspected vulnerability, account compromise, or abuse case, which stops being handled in the open immediately.
- **Source conflict**: the customer's account of what they did and the audit log genuinely disagree, or documented behavior and observed behavior diverge on a load-bearing point. Record both readings; the documentation mismatch is a finding to route, not a resolution to send.
- **Release integrity**: a cause would be stated to the customer at a confidence the evidence does not carry, in either direction. Overstating consumes engineering capacity another ticket needed; understating leaves a live defect looking like user error.
- **Missing approval**: the diagnosis requires access to another tenant's data, a production database, or a customer's environment beyond what the agreement grants.

An untestable hypothesis, an unavailable client-side capture, a customer who has not yet run the collection, and a version the customer cannot confirm are soft gaps. Continue with what is reachable, label the assumption against the hypothesis it affects, and send the update the clock requires regardless of whether the cause has moved.

## Downstream handoffs

`reproduction-bug-intake-desk` is next where the fault domain is a product defect, and it needs the evidence inventory, the exact build and configuration, and the hypotheses that survived, because a reproduction attempt that starts from the symptom rather than from the isolated conditions repeats the work. `engineering-escalation-desk` needs the cause with its confidence, the failed lines of inquiry, and the evidence already redacted, since those are the difference between a package an engineer accepts and one that comes back for more information. `macro-response-quality-desk` needs the cause at its stated confidence and the workaround with its cost, so the reply commits to nothing the evidence cannot hold. `resolution-closure-desk` needs the fault domain, because it determines the resolution code and whether the ticket stays attached to a defect. `knowledge-base-desk` needs the workaround and the versions it holds for. `contact-driver-analysis-desk` needs the underlying cause separated from the symptom the code recorded.

## Quality bar

Good diagnostic work is legible about its own uncertainty. The hypothesis list shows what was ruled out and by what observation, so the next person can disagree with the reasoning rather than starting over. Evidence carries its collection time and its window, because a log pulled for the wrong hour is worse than no log. The fault domain is argued rather than assumed, since the difference between a configuration issue and a defect is the difference between the customer's afternoon and an engineering sprint. The cause wears its confidence in public, and `suspected` survives all the way into the customer reply rather than firming up somewhere in the handoff. The workaround is written for the person who has to run it and priced in their time. And the failed attempts are recorded, because in this domain the most expensive thing on a long-running ticket is the third engineer independently trying the first engineer's idea.
