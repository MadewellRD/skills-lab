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

1. Resolve target release/feature, telemetry stack, event schema, dashboards, alert owners, feature flags, and remote config controls.
2. Map product/release gates to observable signals: crashes, main-thread stalls, sessions, funnels, purchases, retention, performance, and game economy health.
3. Define rollout monitoring, alert thresholds, incident handoff, rollback triggers, and live-ops controls.
4. Update packet with operational evidence and continue to maintenance/growth after launch readiness.

## Responsibilities

- Make launch health observable before release claims.
- Separate app telemetry from game live-ops, economy, event, and content telemetry.
- Tie rollback and incident response to concrete signals.
- Avoid inventing dashboard, owner, alert, remote config, or production telemetry facts.

## Expected inputs

Release plan, analytics plan, crash/main-thread stall tooling, monitoring docs, feature flag/remote config docs, game live-ops docs, incident process, rollout plan, and prior `ios_delivery_packet`.

## Expected outputs

Observability plan, event/metric map, dashboard/alert checklist, live-ops plan, rollback triggers, incident handoff, halt conditions, and packet update.

## Evidence packet additions

- telemetry stack and owners
- events, metrics, dashboards, and alert thresholds
- crash/main-thread stall, release, funnel, purchase, retention, performance, and game economy signals
- feature flags, remote config, and live-ops controls
- rollback triggers and incident handoff

## Packet fields to update

`observability_requirements`, `analytics_events`, `crash_anr_monitoring`, `dashboards`, `alerts`, `feature_flags`, `remote_config`, `liveops_controls`, `incident_handoff`, `rollback_triggers`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Telemetry stack or owner is unknown.
- Required analytics, crash, main-thread stall, or rollout evidence is unavailable.
- Production rollout lacks monitoring or rollback triggers.
- Game live-ops, economy, content, or event controls are required but unresolved.

## Default output modes

- `ios-observability-plan.md`
- `ios-event-metric-map.md`
- `ios-liveops-plan.md`
- `ios-incident-handoff.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-maintenance-growth-desk` for post-launch iteration, debt, policy, and growth planning.

## SDLC suite handoff

Use `observability-readiness-desk`, `incident-response-desk`, `release-operations-desk`, and `maintenance-refactor-desk` when iOS observability or live-ops work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
