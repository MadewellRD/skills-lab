---
name: android-release-store-ops-desk
description: plan Android builds, signing, versioning, CI/CD, AAB/APK packaging, internal testing, Play tracks, release notes, staged rollout, rollback, Play Asset Delivery, and store listing readiness.
---

# Android Release Store Ops Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing signing state, package/application ID, Play Console state, release track, rollout, rollback, or policy evidence.

## Role

Plan Android release and Play Store operations: build variants, signing, versioning, AAB/APK packaging, CI/CD, internal/closed/open testing, Play tracks, release notes, staged rollout, rollback, store listing readiness, Play Asset Delivery, and production gate evidence.

## Workflow

1. Resolve release target, version, branch/commit, package/application ID, signing state, artifacts, track, and rollout plan.
2. Verify product, technical discovery, architecture, security/privacy, performance, QA, observability, and policy gates.
3. Define build/package commands, release notes, store listing changes, asset delivery, staged rollout, monitoring, and rollback criteria.
4. Separate repo/package readiness from Play Console actions that require explicit approval.
5. Continue to observability/live ops for launch monitoring.

## Responsibilities

- Treat release as gated operations, not just a build command.
- Require signing, versioning, package ID, artifact, track, rollout, and rollback facts before release-ready claims.
- Cover game-specific packaging such as Play Asset Delivery when relevant.
- Never perform external publish actions without explicit approval.

## Expected inputs

QA evidence, release scope, versioning plan, CI/build output, signing policy, Play Console notes, listing assets, release notes, policy review, rollout/rollback plan, and prior `android_delivery_packet`.

## Expected outputs

Release readiness report, build/package checklist, Play track plan, staged rollout plan, release notes draft, rollback plan, halt conditions, and packet update.

## Evidence packet additions

- release target and version
- package/application ID and build artifacts
- signing state and Play track
- store listing and asset delivery readiness
- release gates, approvals, rollout, and rollback plan

## Packet fields to update

`release_target`, `versioning`, `application_id`, `build_artifacts`, `signing_state`, `play_track`, `store_listing`, `asset_delivery`, `release_notes`, `rollout_plan`, `rollback_plan`, `approvals`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Signing or package/application ID facts are missing.
- QA, security/privacy, performance, policy, or observability gates are unresolved.
- Requested Play Console publish action lacks explicit approval.
- Rollback plan or staged rollout criteria are missing for production release.

## Default output modes

- `android-release-readiness.md`
- `android-build-package-checklist.md`
- `android-play-track-plan.md`
- `android-release-notes.md`
- `android-rollback-plan.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `android-observability-liveops-desk` for launch monitoring and live-ops readiness.

## SDLC suite handoff

Use `release-operations-desk`, `deployment-desk`, `verification-desk`, and `observability-readiness-desk` when Android release work needs generic lifecycle support.
