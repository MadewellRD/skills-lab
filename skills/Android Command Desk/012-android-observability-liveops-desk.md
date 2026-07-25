---
name: android-observability-liveops-desk
description: define Android observability and live ops for crash reporting, logs, metrics, analytics events, alerts, feature flags, remote config, game economy/events, rollout monitoring, and incident response.
---

# Android Observability Liveops Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing telemetry stacks, dashboards, alert owners, remote config, production signals, game economy controls, or incident hooks.

## Role

Define Android observability and live ops for app/game launches and operations: crash reporting, ANR monitoring, logs, metrics, analytics events, alerts, feature flags, remote config, rollout monitoring, game economy/events, live content, and incident response hooks.

## Workflow

**Outcome.** An Android observability and live-ops plan: telemetry stack and owners; event schema, metrics, dashboards, and alert thresholds; crash, ANR, session, funnel, purchase, retention, performance, and game economy signals; feature flags, remote config, and live-ops controls; rollout monitoring; rollback triggers; and incident handoff.

**Grounding.** Work from the release plan, analytics plan, crash and ANR tooling, monitoring docs, feature flag and remote config docs, game live-ops docs, the incident process, and the rollout plan. Do not invent telemetry stacks, dashboards, alert owners, remote config, production signals, game economy controls, or incident hooks.

**Parallel surface.** Individual events, metrics, dashboards, and alert definitions are independent: specify them in parallel. Threshold coherence across the alert set, the rollout monitoring plan, and the rollback trigger set are aggregate — they must not contradict one another, so reconcile them once after the per-signal work.

**Acceptance bar.** The plan is complete when every release gate maps to at least one observable signal; each alert names a threshold, a window, and an owner or marks the owner unknown; each rollback trigger names the signal and value that fires it; instrumentation that does not yet exist is listed as an instrumentation gap rather than assumed present; and the incident handoff states who receives it and with what context.

Update the packet with operational evidence and continue to maintenance/growth after launch readiness.

## Responsibilities

- Make launch health observable before release claims.
- Separate app telemetry from game live-ops, economy, event, and content telemetry.
- Tie rollback and incident response to concrete signals.
- Avoid inventing dashboard, owner, alert, remote config, or production telemetry facts.

## Expected inputs

Release plan, analytics plan, crash/ANR tooling, monitoring docs, feature flag/remote config docs, game live-ops docs, incident process, rollout plan, and prior `android_delivery_packet`.

## Expected outputs

A complete run delivers the whole operating picture: the observability plan, the event and metric map, the dashboard and alert checklist, the live-ops plan, the rollback triggers, the incident handoff, the halt conditions that apply, and the packet update. An alert set without the rollback triggers it should fire, or a live-ops plan without the signals that tell you it is working, is not an operable release — these are produced as one package.

Depth is judged by whether an on-call engineer could act at 3am without asking what an alert means. Every event carries its schema and the question it answers; every metric names its owner, its source, and its threshold; every alert states what it fires on, who it pages, and what the first response is; every rollback trigger states the concrete signal and the action it authorizes. A dashboard named but not specified is not a deliverable.

Completing the set is never a licence to invent telemetry. An event, metric, threshold, or dashboard that no instrumentation or telemetry plan supports is recorded as a gap with the instrumentation work it needs — a threshold picked because the row looked empty produces either an alert nobody trusts or silence where there should be a page. Individual events, metrics, dashboards, and alert definitions are independent and part of the parallel surface declared in Workflow.

## Evidence packet additions

- telemetry stack and owners
- events, metrics, dashboards, and alert thresholds
- crash/ANR, release, funnel, purchase, retention, performance, and game economy signals
- feature flags, remote config, and live-ops controls
- rollback triggers and incident handoff

## Packet fields to update

`observability_requirements`, `analytics_events`, `crash_anr_monitoring`, `dashboards`, `alerts`, `feature_flags`, `remote_config`, `liveops_controls`, `incident_handoff`, `rollback_triggers`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. An unknown telemetry detail is normally an instrumentation gap plus the fact needed to close it, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — changing alerting, remote config, feature flags, or live-ops controls in a real environment requires authorization.
- **Production or destructive** — the request would flip a production flag, push remote config, alter a live game economy or event, or silence a production alert.
- **Security or privacy** — proposed telemetry would capture personal data, credentials, or content whose collection no source establishes.
- **Source conflict** — monitoring docs, the analytics plan, and observed production signals genuinely disagree on what is instrumented. Preserve the conflict.
- **Release integrity** — a production rollout would proceed with no monitoring coverage or rollback triggers, or launch health would be reported as observable when the instrumentation does not exist.
- **Connector unreachable** — a monitoring, analytics, or crash-reporting source exists but cannot be read.

Otherwise proceed: an unknown telemetry stack, owner, dashboard, or live-ops control becomes a labeled assumption plus an open question, and the plan states what becomes observable once the gap is closed.

## Default output modes

A complete run writes all of these:

- `android-observability-plan.md`
- `android-event-metric-map.md`
- `android-liveops-plan.md`
- `android-incident-handoff.md`

Mode-specific alternative:

- `workflow-halt.md` — produced instead of the set above when a hard halt fires, not alongside it.

A file the telemetry plan cannot support names the instrumentation gap rather than listing signals and thresholds nobody chose.

## Downstream handoff

Continue to `android-maintenance-growth-desk` for post-launch iteration, debt, policy, and growth planning.

## SDLC suite handoff

Use `observability-readiness-desk`, `incident-response-desk`, `release-operations-desk`, and `maintenance-refactor-desk` when Android observability or live-ops work needs generic lifecycle support.
