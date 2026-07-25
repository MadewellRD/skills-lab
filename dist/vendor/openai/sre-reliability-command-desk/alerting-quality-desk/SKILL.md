---
name: alerting-quality-desk
description: design and review production alerting including symptom-based paging on user impact, multi-window multi-burn-rate rules tied to error budget spend, page versus ticket versus dashboard routing, deduplication grouping inhibition and dependency-aware suppression, alert noise and page load review, flapping and self-resolving pages, alerts with no runbook, and detection gaps where a customer reported the outage before any signal fired.
---

# Alerting Quality Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the alerting artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent alert expressions, thresholds, firing counts, page volumes, routing destinations, silence rules, or the incidents an alert is claimed to have caught.

## Role

Own the layer between a system failing and a human being told about it. This desk decides what is worth waking someone for, what should become a ticket, what belongs on a dashboard and nowhere else, and what should not exist at all.

Two failures define the work and they pull in opposite directions. An alert set tuned only against noise stops paging for things that matter, and the outage arrives as a support ticket from a customer. An alert set tuned only against coverage produces a rotation that acknowledges pages reflexively and misses the one that counted. The resolution is not a middle setting; it is paging on user-visible symptoms and on error budget burn, ticketing the causes that predict future pain, and dashboarding everything else.

The material of this desk is the actual rule: the expression, the window, the `for` duration, the labels that group and route it, the inhibition that suppresses it when its upstream is already firing, and the runbook it links to.

## Use when

- SLIs and an error budget policy exist and the paging rules that defend them need designing or rewriting.
- The rotation reports too many pages, or the page load in `oncall.page_load` is over budget and the cause is the alert set rather than the system.
- An incident was detected by a customer, a dependency team, or a status page rather than by a signal, and the detection gap needs closing.
- The alert inventory has drifted: rules pointing at decommissioned services, thresholds nobody remembers setting, alerts that have never fired once.
- A single failure event produces a page storm and needs grouping, deduplication, and dependency-aware suppression.
- A new failure mode arrived from dependency analysis, chaos results, or a postmortem action item and needs a detection decision.

## Do not use when

- The user impact being alerted on is not defined yet: that is `sli-specification-desk`, because an alert cannot be called noisy until something states the impact it was written to protect.
- The objective, budget, or budget policy is the actual argument: that is `slo-error-budget-desk`, whose burn-rate windows this desk implements.
- The alert fires correctly and the problem is that nobody knows what to do next: that is `runbook-engineering-desk`.
- The pages are actionable and correctly routed but the rotation cannot absorb them: that is `oncall-escalation-desk`, which owns staffing and page load budget.
- An alert is firing right now and the service is degraded: that is `incident-command-desk`.

## Required evidence

- The SLI specifications with their measurement state, and the SLOs with windows and budget policy.
- The current alert rule source: rule files, monitor definitions, or the equivalent as configuration, read as configuration rather than described from a dashboard.
- Page history from the paging platform: which rules fired, how often, at what hour, acknowledged by whom, and how each was resolved.
- Notification routing and escalation policy, including grouping keys, inhibition or dependency suppression rules, and standing silences with their age.
- Incident records with their detection source, so detection gaps and their duration are visible rather than inferred.
- The failure mode inventory and dependency graph, since suppression and coverage both follow the graph.
- Runbook coverage per alert.

## Workflow

**Outcome.** An alert set where every page corresponds to user impact or budget burn, every rule carries its real expression and routing decision, every page has a runbook, the noise is named alert by alert with the evidence that made it noise, and the failure modes with no detection at all are listed as gaps rather than left implicit.

**Grounding.** The rule source states what is configured. The paging platform states what actually fired and what actually woke someone. The incident tracker states what was missed. These are three different sources and they disagree routinely: a rule that exists in the repository but is not loaded, a rule that fires nightly and is silenced by habit, an incident nobody was paged for. Record both sides with attribution per `references/suite-workflow-contract.md` rather than resolving to whichever is tidier.

**Constraints.** Page on symptoms the user experiences and on budget burn; route causes that predict future impact to tickets; leave the rest on dashboards. Burn-rate paging uses multiple windows so that a fast catastrophic burn and a slow persistent burn are both caught, with a short window as the reset condition so the page clears when the burn stops. Every threshold traces to the objective and window it defends rather than to a round number.

Suppression follows the dependency graph, not the alphabet: when a hard dependency is already paging, the dependents it takes down are grouped under it rather than paging independently. Grouping keys are chosen so that one failure event produces one notification, and so that two genuinely separate failures never collapse into one.

Signal quality is assigned from firing history, not from reading the expression. An alert with no firing record is `unproven` and stays that way; an alert that fires and closes itself without action is a candidate for a ticket, a longer `for` duration, or deletion; an alert that fires only alongside a broader page is a suppression candidate.

Cutting over a paging rule follows this order, and the order is mandated because deleting detection before proving its replacement leaves a window in which the failure mode is live and nothing watches it:

1. Deploy the replacement rule in ticket or dashboard routing alongside the incumbent, so both observe the same traffic.
2. Hold both until the replacement has observed the failure mode it targets, or until a stated observation window covering the failure mode's real recurrence interval has elapsed.
3. Promote the replacement to paging routing with its runbook attached.
4. Retire the incumbent, recording the retirement in the alert inventory rather than deleting it silently.

**Parallel surface.** Alert rules, failure modes, services, and incident detection records are independent units and are parallel-safe: per-rule expression review, per-rule firing history lookup, per-failure-mode coverage checks, and connector preflight across the metrics backend, paging platform, and incident tracker all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: composing page load across the whole rotation, deriving the suppression hierarchy from the dependency graph, ranking the noise list, and judging coverage across a journey where several services each look adequately alerted while the journey as a whole has no symptom-based signal.

**Acceptance bar.** Every paging rule states its expression, its window, what user impact or budget spend it corresponds to, its routing, and its runbook reference. Every rule carries a signal quality drawn from firing history or is marked unproven. Every failure mode in the packet maps to a detecting signal or is listed as undetected. Every incident whose detection source was not an alert appears in the detection gap list with what would have caught it.

## Outputs

A complete run delivers this artifact set:

- `alerting-rule-set.md`: the paging, ticketing, and dashboard-only rules with the actual expression, evaluation and `for` window, labels, routing destination, linked SLI, and runbook reference for each.
- `alerting-burn-rate-design.md`: the multi-window burn-rate rules per objective with the budget fraction each consumes before it fires, the short reset window, and the detection delay each configuration accepts.
- `alerting-noise-review.md`: per-rule firing counts, out-of-hours distribution, self-resolving share, actioned share, standing silences with their age, and a disposition for every rule that is keep, retune with the new value, demote to ticket, suppress under a parent, or delete.
- `alerting-detection-gaps.md`: failure modes with no signal, incidents found by customers or dependency teams with the time between impact and detection, and the proposed rule for each gap.
- `alerting-downstream-handoff.md`: what `runbook-engineering-desk` and `oncall-escalation-desk` inherit, including the alerts now paging without a runbook and the expected page load change.

Depth standard per artifact: a rule entry contains the expression a responder could read to understand why they were woken, not the category the alert belongs to. A noise entry contains the count and the window the count was taken over. A gap entry names the signal that would have caught the incident and the measurement point it would come from. "Alert on high error rate" is a category and is incomplete.

In `diagnostic` mode, when the rule source, paging platform, or incident tracker exists and cannot be read, the run delivers `alerting-connector-diagnostic.md` reporting what was reachable, the queries and exports attempted, and the exact access required. Noise dispositions are not assigned in that mode, because a disposition without firing history is an opinion about a rule nobody has watched.

The characteristic fabrication here is the confident verdict on an unread rule. Alert reviews read as authoritative whether or not anyone opened the rule file or the page log, and "this alert is noisy, delete it" is a sentence that removes production detection on the strength of a guess. Every disposition in these artifacts names the firing count and the window behind it, or the rule is recorded as unreviewed with the query that would review it. The two adjacent traps carry the same rule: an alert is described as covering a failure mode only when it has fired for that mode or a test has driven it, never because the expression looks like it would; and a threshold is quoted only from the rule source, never reconstructed from what a sensible threshold would be.

## reliability_packet fields to update

- `alerts[]` in full: `name`, `condition` with the real expression, `basis`, `slo_linked`, `routing`, `runbook_ref`, and `signal_quality`.
- `failure_modes[].detection` for every mode this review touched, including the modes now recorded as undetected.
- `incidents[].detection_source` where the review established how an incident was actually found.
- `slos[].burn_rate` and `slos[].budget_policy` where the burn-rate design changed what the policy triggers on.
- `runbooks[].covers` for alerts already carrying a runbook, and the alerts left without one.
- `oncall.page_load` with the measured page volume this review established, and its window.
- `reliability_risks[]` for detection gaps that remain open.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: retiring a paging rule, lowering a paging threshold on a tier 0 or tier 1 journey, or moving a page to ticket routing without the service owner who carries the consequence agreeing.
- Production or destructive: the next action would deploy, silence, reroute, or delete a live alerting rule, change escalation routing, or apply a maintenance window to a live rotation.
- Security or privacy: alert payloads, log samples, or notification templates would carry credentials, tokens, session identifiers, or personal data into a paging channel or a ticket queue.
- Source conflict: the rule source and the paging platform disagree about what is deployed, or the incident record and the page history disagree about whether an alert fired for an incident. Choosing one silently would delete detection based on the wrong picture.
- Release integrity: an alert would be recorded as covering a failure mode, or a rule set declared adequate for a launch gate, without firing evidence or a test that drove it.
- Connector unreachable: the metrics backend, rule repository, paging platform, or incident tracker needed for this review exists and cannot be read.

Absent page history for a recently created rule, unknown authorship of an old threshold, and an unmeasured out-of-hours split are soft gaps. Proceed with each named in the artifact and recorded in `open_questions`. Detection for a tier 0 journey is never removed to reduce a page count, and a rule is never described as tuned when it was only reworded.

## Downstream handoffs

`runbook-engineering-desk` needs the paging set with each alert's failure mode and first mitigating action candidate, plus the explicit list of pages with no runbook. `oncall-escalation-desk` needs the projected page load per rotation after the dispositions land, and the out-of-hours share. `production-readiness-review-desk` needs the alerting gate evidence: which user-impacting failure modes have a proven signal and which do not. `postmortem-desk` consumes the detection gap list when an incident's contributing factors include late detection. `slo-error-budget-desk` receives any objective whose burn-rate design showed the window cannot be defended by any alert that fires in time.

## Quality bar

A rotation that trusts its pager. Every page means a user is affected or the budget is burning fast enough to matter, every page has a first action, one failure produces one notification, and the alerts that were deleted were deleted with their firing history attached. The detection gap list is honest about the incidents customers found first, including the ones that are still uncovered.
