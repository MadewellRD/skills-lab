---
name: ios-release-app-store-ops-desk
description: plan iOS builds, signing, versioning, CI/CD, archive/export packaging, internal testing, TestFlight groups and App Store release states, release notes, staged rollout, rollback, on-demand resources and asset delivery, and store listing readiness.
---

# iOS Release App Store Ops Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing signing state, bundle ID, App Store Connect state, release track, rollout, rollback, or policy evidence.

## Role

Plan iOS release and App Store operations: build variants, signing, versioning, archive/export packaging, CI/CD, internal/closed/open testing, TestFlight groups and App Store release states, release notes, staged rollout, rollback, store listing readiness, on-demand resources and asset delivery, and production gate evidence.

## Workflow

1. Resolve release target, version, branch/commit, bundle ID, signing state, artifacts, track, and rollout plan.
2. Verify product, technical discovery, architecture, security/privacy, performance, QA, observability, and policy gates.
3. Define build/package commands, release notes, store listing changes, asset delivery, staged rollout, monitoring, and rollback criteria.
4. Separate repo/package readiness from App Store Connect actions that require explicit approval.
5. Continue to observability/live ops for launch monitoring.

## Responsibilities

- Treat release as gated operations, not just a build command.
- Require signing, versioning, bundle ID, artifact, track, rollout, and rollback facts before release-ready claims.
- Cover game-specific packaging such as on-demand resources and asset delivery when relevant.
- Never perform external publish actions without explicit approval.

## Expected inputs

QA evidence, release scope, versioning plan, CI/build output, signing policy, App Store Connect notes, listing assets, release notes, policy review, rollout/rollback plan, and prior `ios_delivery_packet`.

## Expected outputs

Release readiness report, build/package checklist, TestFlight group or App Store release state plan, staged rollout plan, release notes draft, rollback plan, halt conditions, and packet update.

## Evidence packet additions

- release target and version
- bundle ID and build artifacts
- signing state and TestFlight group or App Store release state
- store listing and asset delivery readiness
- release gates, approvals, rollout, and rollback plan

## Packet fields to update

`release_target`, `versioning`, `application_id`, `build_artifacts`, `signing_state`, `play_track`, `store_listing`, `asset_delivery`, `release_notes`, `rollout_plan`, `rollback_plan`, `approvals`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Signing or bundle ID facts are missing.
- QA, security/privacy, performance, policy, or observability gates are unresolved.
- Requested App Store Connect publish action lacks explicit approval.
- Rollback plan or staged rollout criteria are missing for production release.

## Default output modes

- `ios-release-readiness.md`
- `ios-build-package-checklist.md`
- `ios-play-track-plan.md`
- `ios-release-notes.md`
- `ios-rollback-plan.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-observability-liveops-desk` for launch monitoring and live-ops readiness.

## SDLC suite handoff

Use `release-operations-desk`, `deployment-desk`, `verification-desk`, and `observability-readiness-desk` when iOS release work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
