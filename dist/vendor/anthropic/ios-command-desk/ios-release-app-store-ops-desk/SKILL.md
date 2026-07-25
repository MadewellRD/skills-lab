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

**Outcome.** An iOS release and App Store operations package: release target and version, bundle ID and build artifacts, signing and provisioning state, TestFlight group or App Store release state, store listing and asset delivery readiness, release notes, staged rollout plan, rollback plan, and the gate evidence and approvals behind any go decision.

**Grounding.** Work from QA evidence, release scope, versioning plan, CI and build output, signing policy, App Store Connect notes, listing assets, policy review, and the rollout and rollback plan. Do not invent signing state, bundle ID, App Store Connect state, release track, rollout percentages, rollback commands, or policy evidence.

**Ordered release sequence, keep this ordered.** The steps below are ordered because Apple's signing chain and App Review mandate the order, not because the executing model needs the decomposition. Signing and provisioning precede archive and upload because App Store Connect rejects an artifact whose certificate, profile, entitlements, or bundle ID do not match, and the bundle ID cannot be changed after first submission. Gate verification precedes submission because App Review is an external gate on a queue this desk does not control, and a rejected submission costs a full review cycle. Approval precedes release, and phased release percentages only advance on Apple's schedule, pausing a phased release does not recall the builds already delivered to users. A future editor must not reorder, renumber, or collapse these into prose:

1. Resolve release target, version, branch/commit, bundle ID, signing state, artifacts, track, and rollout plan.
2. Verify product, technical discovery, architecture, security/privacy, performance, QA, observability, and policy gates.
3. Define build/package commands, release notes, store listing changes, asset delivery, staged rollout, monitoring, and rollback criteria.
4. Separate repo/package readiness from App Store Connect actions that require explicit approval.
5. Continue to observability/live ops for launch monitoring.

**Parallel surface.** Evidence collection for the individual gates in step 2, and readiness checks for individual store listing assets and locales, are independent of one another and can be gathered in parallel. The sequence above and the go/no-go roll-up are explicitly not parallel: they run once, in order, once the evidence exists.

**Acceptance bar.** The release package is ready when the release is bounded by a specific version, branch, and commit; every gate is classified pass, fail, blocked, unknown, or not applicable together with the evidence supporting that classification; signing state and bundle ID are sourced rather than assumed; rollback steps are marked verified or unverified rather than presented uniformly; staged rollout has defined phases, monitoring windows, and halt criteria; and any go decision traces to gate evidence rather than to the absence of known problems.

## Responsibilities

- Treat release as gated operations, not just a build command.
- Require signing, versioning, bundle ID, artifact, track, rollout, and rollback facts before release-ready claims.
- Cover game-specific packaging such as on-demand resources and asset delivery when relevant.
- Never perform external publish actions without explicit approval.

## Expected inputs

QA evidence, release scope, versioning plan, CI/build output, signing policy, App Store Connect notes, listing assets, release notes, policy review, rollout/rollback plan, and prior `ios_delivery_packet`.

## Expected outputs

A complete run delivers the entire release package: the readiness report, the build and package checklist, the TestFlight group or App Store release state plan, the staged rollout plan, the release notes draft, the rollback plan, any halt conditions, and the packet update. No single one of these carries a go decision on its own, which is why they are produced together rather than one per turn.

These are prepared artifacts, not performed actions. Having the full package does not upload a build, distribute to a TestFlight group, submit for App Review, change release state, or advance a phased release percentage; every App Store Connect action stays behind the ordered release sequence and the explicit approval it requires, exactly as Workflow specifies. A complete package is what a human approves from; it is not itself the approval.

Each artifact is done when the release could be executed from it. The readiness report classifies every gate pass, fail, blocked, unknown, or not applicable with its evidence; the rollout plan names phases, monitoring windows, and halt criteria; the rollback plan gives concrete steps, each marked verified or unverified rather than presented uniformly; the release notes are the text that would actually ship. A page of headings is not a release package.

No part of the set is completed by assumption. Signing and provisioning state, bundle ID, App Store Connect state, track, rollout phases, rollback commands, and policy evidence are sourced or recorded as unknown against the gate they block; an assumed provisioning state reads as readiness and fails at upload, and an unverified rollback step fails when it is the only thing left. Per-gate evidence and per-asset and per-locale listing checks are independent and part of the parallel surface declared in Workflow.

## Evidence packet additions

- release target and version
- bundle ID and build artifacts
- signing state and TestFlight group or App Store release state
- store listing and asset delivery readiness
- release gates, approvals, rollout, and rollback plan

## Packet fields to update

`release_target`, `versioning`, `application_id`, `build_artifacts`, `signing_state`, `testflight_group`, `store_listing`, `asset_delivery`, `release_notes`, `rollout_plan`, `rollback_plan`, `approvals`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default when drafting checklists, notes, and readiness reports: an unknown gate is classified `unknown` with its missing evidence named. Release decisions are different; a go decision and any App Store Connect write are consequence-bearing acts. Reserve hard halts for these consequence classes:

- **Approval**: a requested App Store Connect submit, publish, release, phased-release advance, or listing-change action lacks explicit approval. This desk prepares release decisions; it does not execute them.
- **Production or destructive**: the action reaches production users irreversibly: releasing an approved build, advancing a phased release, publishing a listing change, or rotating signing or provisioning material.
- **Security or privacy**: the release depends on unresolved security, privacy, privacy-label, or App Review policy risk.
- **Source conflict**: repo state, CI output, and App Store Connect notes genuinely disagree on version, artifact, release state, or signing state. Preserve the conflict rather than picking one and shipping.
- **Release integrity**: signing or bundle ID facts are missing; QA, security/privacy, performance, policy, or observability gates are unresolved; or a rollback plan and staged rollout criteria are missing for a production release.
- **Connector unreachable**: repo, CI, or App Store Connect evidence exists but cannot be read.

Otherwise proceed: missing listing copy, asset, or release-note detail is drafted with the assumption labeled inline and flagged for the owner before submission.

## Default output modes

The set a complete run writes:

- `ios-release-readiness.md`
- `ios-build-package-checklist.md`
- `ios-testflight-phased-release-plan.md`
- `ios-release-notes.md`
- `ios-rollback-plan.md`

Mode-specific alternative:

- `workflow-halt.md`: returned instead of the set above when a hard halt fires. A failed or blocked gate is recorded in the readiness report as a no-go and does not need a halt to be visible.

## Downstream handoff

Continue to `ios-observability-liveops-desk` for launch monitoring and live-ops readiness.

## SDLC suite handoff

Use `release-operations-desk`, `deployment-desk`, `verification-desk`, and `observability-readiness-desk` when iOS release work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
