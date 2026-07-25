---
name: ios-observability-liveops-desk
description: define iOS observability and live ops for crash reporting, logs, metrics, analytics events, alerts, feature flags, remote config, game economy/events, rollout monitoring, and incident response.
---

# iOS Observability Liveops Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing telemetry stacks, dashboards, alert owners, remote config, production signals, game economy controls, or incident hooks.

## Role

Define iOS observability and live ops for app/game launches and operations: crash reporting, main-thread stall monitoring, logs, metrics, analytics events, alerts, feature flags, remote config, rollout monitoring, game economy/events, live content, and incident response hooks.

## Workflow

**Outcome.** An iOS observability and live-ops plan: telemetry stack and owners; event schema, metrics, dashboards, and alert thresholds; crash, main-thread stall, session, funnel, purchase, retention, performance, and game economy signals; feature flags, remote config, and live-ops controls; rollout monitoring; rollback triggers; and incident handoff.

**Grounding.** Work from the release plan, analytics plan, crash and main-thread-stall tooling, monitoring docs, feature flag and remote config docs, game live-ops docs, the incident process, and the rollout plan. Do not invent telemetry stacks, dashboards, alert owners, remote config, production signals, game economy controls, or incident hooks.

**Parallel surface.** Individual events, metrics, dashboards, and alert definitions are independent: specify them in parallel. Threshold coherence across the alert set, the rollout monitoring plan, and the rollback trigger set are aggregate, they must not contradict one another, so reconcile them once after the per-signal work.

**Acceptance bar.** The plan is complete when every release gate maps to at least one observable signal; each alert names a threshold, a window, and an owner or marks the owner unknown; each rollback trigger names the signal and value that fires it; instrumentation that does not yet exist is listed as an instrumentation gap rather than assumed present; and the incident handoff states who receives it and with what context.

Update the packet with operational evidence and continue to maintenance/growth after launch readiness.

## Responsibilities

- Make launch health observable before release claims.
- Separate app telemetry from game live-ops, economy, event, and content telemetry.
- Tie rollback and incident response to concrete signals.
- Avoid inventing dashboard, owner, alert, remote config, or production telemetry facts.

## Expected inputs

Release plan, analytics plan, crash/main-thread stall tooling, monitoring docs, feature flag/remote config docs, game live-ops docs, incident process, rollout plan, and prior `ios_delivery_packet`.

## Expected outputs

A complete run delivers the operating picture in full: the observability plan, the event and metric map, the dashboard and alert checklist, the live-ops plan, the rollback triggers, the incident handoff, any halt conditions, and the packet update. Alerts with no rollback triggers behind them, or a live-ops plan with no signals to say whether it is working, is not an operable release; these ship as one package.

The bar is that an on-call engineer can act at 3am without asking what an alert means. Each event carries its schema and the question it answers; each metric names its owner, its source, and its threshold; each alert states its firing condition, who it pages, and the first response; each rollback trigger names the concrete signal and the action it authorizes. A dashboard mentioned but not specified is not a deliverable.

Completing the set is never a licence to invent telemetry. An event, metric, threshold, or dashboard that no instrumentation or telemetry plan supports is recorded as a gap with the instrumentation it needs; a threshold chosen to fill a row yields either an alert nobody trusts or silence where a page belonged. Individual events, metrics, dashboards, and alert definitions are independent and part of the parallel surface declared in Workflow.

## Evidence packet additions

- telemetry stack and owners
- events, metrics, dashboards, and alert thresholds
- crash/main-thread stall, release, funnel, purchase, retention, performance, and game economy signals
- feature flags, remote config, and live-ops controls
- rollback triggers and incident handoff

## Packet fields to update

`observability_requirements`, `analytics_events`, `crash_anr_monitoring`, `dashboards`, `alerts`, `feature_flags`, `remote_config`, `liveops_controls`, `incident_handoff`, `rollback_triggers`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. An unknown telemetry detail is normally an instrumentation gap plus the fact needed to close it, not a stop. Reserve hard halts for these consequence classes:

- **Approval**: changing alerting, remote config, feature flags, or live-ops controls in a real environment requires authorization.
- **Production or destructive**: the request would flip a production flag, push remote config, alter a live game economy or event, or silence a production alert.
- **Security or privacy**: proposed telemetry would capture personal data, credentials, or content whose collection no source establishes, or would exceed what the privacy label and privacy manifest declare.
- **Source conflict**: monitoring docs, the analytics plan, and observed production signals genuinely disagree on what is instrumented. Preserve the conflict.
- **Release integrity**: a production rollout would proceed with no monitoring coverage or rollback triggers, or launch health would be reported as observable when the instrumentation does not exist.
- **Connector unreachable**: a monitoring, analytics, or crash-reporting source exists but cannot be read.

Otherwise proceed: an unknown telemetry stack, owner, dashboard, or live-ops control becomes a labeled assumption plus an open question, and the plan states what becomes observable once the gap is closed.

## Default output modes

The set a complete run writes:

- `ios-observability-plan.md`
- `ios-event-metric-map.md`
- `ios-liveops-plan.md`
- `ios-incident-handoff.md`

Mode-specific alternative:

- `workflow-halt.md`: produced in place of the set above when a hard halt fires, not alongside it.

Where the telemetry plan cannot support a file, it names the instrumentation gap instead of listing signals and thresholds nobody set.

## Downstream handoff

Continue to `ios-maintenance-growth-desk` for post-launch iteration, debt, policy, and growth planning.

## SDLC suite handoff

Use `observability-readiness-desk`, `incident-response-desk`, `release-operations-desk`, and `maintenance-refactor-desk` when iOS observability or live-ops work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
