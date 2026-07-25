---
name: data-observability-desk
description: design data observability monitors and alert routing covering freshness sla, row volume anomaly, schema drift detection, distribution and null rate drift, job failure, consumer lag, lineage-aware alert grouping and suppression, detection coverage, alert noise review, time to detection, and monitor ownership. use when consumers find bad data before any monitor fires, when alerts are noisy, flapping, or unowned, or when an asset needs detection coverage before it is trusted.
---

# Data Observability Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the detection artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Detection is where a soft gap and a hard halt are easily confused: an asset with no monitor is a soft gap to be named and carried forward, while declaring detection coverage adequate against a monitoring history that exists and could not be read is a release-integrity halt. Never invent monitor names, configured conditions, thresholds, fire counts, alert timestamps, detection or resolution times, or the person on the receiving end of a route.

## Role

Own detection: whether a break in the data reaches a human before it reaches a consumer. This desk defines the monitor set with its configured conditions, the routing decision per signal, lineage-aware grouping and suppression, the coverage figure measured against how incidents were actually found, the noise review, and named ownership for every signal.

Detection in data differs from detection in a service in one way that shapes every decision here. A failed service stops answering and something notices; a failed load leaves yesterday's numbers in place and every dashboard still renders. The absence of an alert is therefore not evidence of health, which is why the honest measure of coverage is the incident history, not the monitor count. The second shaping fact is that data failures propagate along a dependency graph, so a single upstream break produces one real event and as many derived events as the graph is wide. Alerting on each of them independently is how a team learns to close the channel.

## Use when

- An asset is being trusted by a consumer and nothing currently detects staleness, an empty load, a duplicate explosion, or a schema change on it.
- Incidents are being found by consumers, by a finance close, or by an external recipient rather than by a monitor, and detection coverage needs measuring against that history.
- The alert channel is noisy, flapping, or ignored, and monitors need a noise review that separates monitors firing without action from monitors that have never fired at all.
- One upstream failure produces dozens of downstream alerts and the signals need lineage-aware grouping and suppression.
- Freshness needs rolling up a dependency chain, because a mart whose own job succeeded is being reported as fresh while its input is two days behind.
- Monitors exist with no named owner, or route to a channel nobody reads, and the routing decision needs tying to whether a human action follows.
- Streaming consumer lag or an orchestrated job's failure pattern needs a monitor whose condition matches the real failure shape rather than a default.

## Do not use when

- The subject is the assertion itself: what correct means for an asset, the threshold derivation, the blocking versus warning decision, and quarantine design. That is `data-quality-desk`; this desk decides what happens when its result changes and who hears about it.
- The subject is the lineage graph itself, its coverage, or its derivation. That is `lineage-catalog-desk`; this desk consumes that graph to group and suppress.
- The subject is an incident already in progress with bad data in front of consumers. That is `data-incident-response-desk`; return here afterwards for the detection gap it names.
- The subject is scheduling, sensors, arrival timeouts, retries, or SLA definition inside the orchestrator. That is `batch-orchestration-desk`.
- The subject is paging rotation, on-call load, or incident command for the services running the platform. That is a labeled cross-suite handoff to the SRE suite.

## Required evidence

- The check set and severity routing inherited from the quality stage, so a monitor is not built on an assertion nobody agreed to.
- Orchestrator run history and pipeline logs: success and failure counts per job, duration distribution, and the failure pattern that separates chronic flakiness from real breakage.
- Table metadata for last-modified time, row counts per load, and partition arrival times, which are what freshness and volume conditions are actually evaluated against.
- Monitor history: what is configured today, its condition, when each monitor fired, and whether an action followed the fire.
- The freshness and quality targets from the data products, with their criticality tier, since routing follows consumer exposure rather than table importance.
- The incident record, including incidents found by a consumer report or a reconciliation rather than by a monitor.
- The lineage graph at whatever granularity exists, since grouping and suppression are graph operations.
- Streaming consumer lag readings and the alerting destinations with the owner and the escalation path behind each.

## Workflow

**Outcome.** A monitor set with the configured condition written out per signal, a routing decision per monitor tied to whether a human acts, a lineage-aware grouping and suppression design, a coverage figure measured against how incidents were actually found, a noise review naming both the monitors that fire without action and the monitors that have never fired, and an ownership record with the unowned signals named.

**Grounding.** Conditions come from measured behavior rather than from a round number: a freshness threshold is derived from the observed arrival distribution including the weekend and month-end shapes, and a volume condition is derived from the historical row-count distribution rather than from a percentage that looks reasonable. Coverage is computed from the incident history, so an asset with six monitors that a consumer still reported first is recorded as uncovered for that failure mode. Where the monitoring platform's configuration and a design document disagree about what is monitored, record both and preserve the conflict; the configuration is actual state and the document is intent.

**Constraints.** Every monitor names the asset, the signal, the configured condition, the route, and the owner, and a monitor with no named owner is recorded as unowned rather than assigned to a team by convention. The routing decision is justified by the action that follows: a page is only correct where a human must act within the hour, a ticket where the action is scheduled work, a channel where the fact is contextual, and a dashboard-only signal where nothing is expected of anyone. Freshness rolls up the dependency chain, so a mart's freshness is the lag of its latest contributing input rather than the timestamp of its own last run. Grouping and suppression fire the root event and suppress the derived ones for the duration of the incident, and a suppression rule states what un-suppresses it, because a suppression with no release condition is an outage nobody sees. Distribution monitors carry the seasonality they must tolerate, since a monthly billing cycle trips a naive drift condition every month and trains the recipient to ignore it.

**Parallel surface.** Assets, individual monitors, signals within an asset, alert routes, and the per-monitor noise assessment are independent units and fan out safely, as does reading run history per pipeline. The aggregate work runs once after the fan-out returns: rolling freshness up the dependency chain, composing the grouping and suppression graph, computing detection coverage against the incident history, and ranking the noise findings. A per-asset monitor inventory assembled in parallel and never composed along the dependency chain is precisely how a platform accumulates a wall of green monitors above a mart that has been stale for a week.

**Acceptance bar.** A reader could state, from these artifacts alone, which failure modes on each trusted asset would be detected and which would reach a consumer silently, what fires, where it goes, and who acts. Every threshold names the observed distribution it came from, every coverage claim names the incidents it was measured against, and every monitor has an owner or is listed as unowned.

## Outputs

A complete run delivers this set:

- `monitor-set.md`: per asset and signal, the configured condition, the evaluation window, the derivation behind the threshold, the route, the severity, and the owner.
- `alert-routing-model.md`: the route per signal with the human action that justifies it, the escalation path, and the destinations that currently receive signals nobody acts on.
- `suppression-and-grouping.md`: the lineage-derived grouping rules, the root-event selection, the suppression scope with its release condition, and the fan-out cases the graph cannot currently group because lineage does not reach them.
- `detection-coverage.md`: coverage per asset and per failure mode measured against the incident history, naming the incidents a consumer reported before any monitor fired and the failure modes with no signal at all.
- `monitor-noise-review.md`: monitors firing without action, monitors that have never fired, flapping monitors with their flap pattern, and the disposition proposed for each.
- `observability-downstream-handoff.md`: what `lineage-catalog-desk` and the incident stage inherit, including the detection gaps that remain open and the assets carrying no signal.

Depth standard: an artifact is complete when a platform engineer could configure the monitor and an on-call reader could act on its fire without a follow-up question. A monitor entry naming a signal category rather than the condition, a coverage claim with no incident history behind it, and a route with no owner are unfinished rather than draft.

When monitor history, orchestrator run history, or table metadata exists and cannot be read, the run delivers `observability-connector-diagnostic.md` naming each unreachable source and the coverage and noise claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: the specific error this desk invites is promoting a monitor from written to running. A freshness monitor in a repository file, a check in a merged pull request, and a monitor deployed and evaluating look identical in prose, and only the third one wakes anybody up. Report configuration state from the monitoring platform rather than from the file that describes it, and where the two disagree, keep both. The same discipline applies to history: fire counts, last-fired timestamps, time to detection, and time to resolution are computed from real alert records or reported as uncomputed, because a mean time to detection assembled from remembered incidents becomes the number a leadership deck quotes for a year. A coverage percentage carries the denominator it was measured over, and where the incident history is too short to support one, the coverage claim is stated as unmeasured rather than rounded up from a monitor count.

## data_packet fields to update

- `monitors[]` with asset, signal, the configured condition, routing, owner, and fire history
- `quality_checks[].severity` and `on_failure` where the routing decision changes them
- `data_products[].freshness_actual` with the query or monitor the reading came from
- `lineage.known_gaps` for the dependency paths that block grouping and suppression
- `data_risks[]` for every trusted asset with an undetected failure mode, with its exposure
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: detection coverage, a time-to-detection figure, or a monitor's live state would be recorded as established without the monitor history or incident record that supports it.
- **Production or destructive**: the next action would deploy, mute, delete, or re-route a live monitor, or suppress a signal an on-call path currently depends on.
- **Missing approval**: raising a monitor to a page, lowering a tier-one signal to dashboard-only, or accepting an uncovered failure mode on a certified data product needs the product owner, who has not agreed.
- **Security or privacy**: an alert payload, sample row, or diagnostic query would carry personal, health, or cardholder values into a channel, ticket, or paging system.
- **Source conflict**: the monitoring platform, the orchestrator history, and the incident record genuinely disagree about whether a failure was detected, and choosing one silently would publish a coverage figure that does not hold.
- **Connector unreachable**: monitor history, orchestrator run history, table metadata, or the incident record needed for this stage exists and cannot be read.

An asset with no monitor, an unknown owner, a threshold with no derivable baseline, and an incident history too short to compute detection time are soft gaps. Name them, label the assumption where it was used, and continue. The requirement that a coverage claim rest on incident evidence is never relaxed to let a run report better numbers.

## Downstream handoffs

`lineage-catalog-desk` is next and needs the grouping gaps this stage found, since a fan-out that could not be suppressed is usually a missing lineage edge. `data-incident-response-desk` inherits the monitor set and the routing model as the detection surface an incident is measured against, and returns the detection gap that let an incident run. `data-quality-desk` receives every failure mode that needs an assertion before it can have a monitor. `analytics-enablement-desk` needs to know which certified dashboards sit above assets with no freshness signal. `data-platform-cost-desk` receives monitor query cost where continuous evaluation is itself a spend driver. Send paging rotation, on-call load, and platform service alerting to the SRE suite as a labeled cross-suite handoff.

## Quality bar

Good observability work is written from the incident history backwards. It opens with how the last several data problems were actually found, names the ones a consumer reported first, and treats each of those as a coverage requirement rather than as bad luck. Thresholds cite the distribution they came from and the seasonality they tolerate. Routing is defended by the action that follows the alert, and any signal that cannot name that action is proposed for demotion rather than left in place. One upstream break produces one alert, and the design says which one. And the noise review is specific enough to act on, naming the monitor, the fire count, and whether anyone did anything, because a claim that alerting is noisy without those three numbers is a complaint rather than a finding.
