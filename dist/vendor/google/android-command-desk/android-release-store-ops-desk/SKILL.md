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

**Outcome.** An Android release and Play Store operations package: release target and version, package/application ID and build artifacts, signing state, Play track, store listing and asset delivery readiness, release notes, staged rollout plan, rollback plan, and the gate evidence and approvals behind any go decision.

**Grounding.** Work from QA evidence, release scope, versioning plan, CI and build output, signing policy, Play Console notes, listing assets, policy review, and the rollout and rollback plan. Do not invent signing state, package/application ID, Play Console state, release track, rollout percentages, rollback commands, or policy evidence.

**Ordered release sequence — keep this ordered.** The steps below are ordered because Google Play and the signing chain mandate the order, not because the executing model needs the decomposition. Signing precedes upload because Play rejects an artifact signed with the wrong key, and neither the application ID nor the app signing key can be changed after first publish. Gate verification precedes track promotion because a promoted build cannot be recalled from users who already installed it. Staged rollout percentages only move upward, and halting a rollout does not un-ship the builds already delivered. A future editor must not reorder, renumber, or collapse these into prose:

1. Resolve release target, version, branch/commit, package/application ID, signing state, artifacts, track, and rollout plan.
2. Verify product, technical discovery, architecture, security/privacy, performance, QA, observability, and policy gates.
3. Define build/package commands, release notes, store listing changes, asset delivery, staged rollout, monitoring, and rollback criteria.
4. Separate repo/package readiness from Play Console actions that require explicit approval.
5. Continue to observability/live ops for launch monitoring.

**Parallel surface.** Evidence collection for the individual gates in step 2, and readiness checks for individual store listing assets and locales, are independent of one another and can be gathered in parallel. The sequence above and the go/no-go roll-up are explicitly not parallel: they run once, in order, once the evidence exists.

**Acceptance bar.** The release package is ready when the release is bounded by a specific version, branch, and commit; every gate is classified pass, fail, blocked, unknown, or not applicable together with the evidence supporting that classification; signing state and application ID are sourced rather than assumed; rollback steps are marked verified or unverified rather than presented uniformly; staged rollout has defined percentages, monitoring windows, and halt criteria; and any go decision traces to gate evidence rather than to the absence of known problems.

## Responsibilities

- Treat release as gated operations, not just a build command.
- Require signing, versioning, package ID, artifact, track, rollout, and rollback facts before release-ready claims.
- Cover game-specific packaging such as Play Asset Delivery when relevant.
- Never perform external publish actions without explicit approval.

## Expected inputs

QA evidence, release scope, versioning plan, CI/build output, signing policy, Play Console notes, listing assets, release notes, policy review, rollout/rollback plan, and prior `android_delivery_packet`.

## Expected outputs

A complete run delivers the entire release package: the readiness report, the build and package checklist, the Play track plan, the staged rollout plan, the release notes draft, the rollback plan, the halt conditions that apply, and the packet update. A go decision cannot be read out of any one of these alone, which is why they are produced together rather than one per turn.

These are prepared artifacts, not executed actions. Producing the full package does not promote a track, upload an artifact, move a rollout percentage, or change store listing state — every Play Console action stays behind the ordered release sequence and the explicit approval it requires, exactly as specified in Workflow. A complete package is what a human approves from; it is not the approval.

Each artifact is done when the release could be run from it. The readiness report classifies every gate as pass, fail, blocked, unknown, or not applicable with its evidence; the rollout plan names percentages, monitoring windows, and halt criteria; the rollback plan states the concrete steps and marks each verified or unverified rather than presenting them uniformly; the release notes are the text that would actually ship. A checklist of headings is not a release package.

Nothing in the set is filled by assumption. Signing state, application ID, Play Console state, track, rollout percentages, rollback commands, and policy evidence are sourced or recorded as unknown with the blocked gate named — an invented signing state or an unverified rollback step reads as readiness and fails at the moment it is needed. Per-gate evidence and per-asset and per-locale listing checks are independent and part of the parallel surface declared in Workflow.

## Evidence packet additions

- release target and version
- package/application ID and build artifacts
- signing state and Play track
- store listing and asset delivery readiness
- release gates, approvals, rollout, and rollback plan

## Packet fields to update

`release_target`, `versioning`, `application_id`, `build_artifacts`, `signing_state`, `play_track`, `store_listing`, `asset_delivery`, `release_notes`, `rollout_plan`, `rollback_plan`, `approvals`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default when drafting checklists, notes, and readiness reports: an unknown gate is classified `unknown` with its missing evidence named. Release decisions are different — a go decision and any Play Console write are consequence-bearing acts. Reserve hard halts for these consequence classes:

- **Approval** — a requested Play Console publish, promote, rollout-increase, or listing-change action lacks explicit approval. This desk prepares release decisions; it does not execute them.
- **Production or destructive** — the action reaches production users irreversibly: promoting to the production track, increasing a staged rollout, publishing a listing change, or rotating signing material.
- **Security or privacy** — the release depends on unresolved security, privacy, data-safety, or Play policy risk.
- **Source conflict** — repo state, CI output, and Play Console notes genuinely disagree on version, artifact, track, or signing state. Preserve the conflict rather than picking one and shipping.
- **Release integrity** — signing or package/application ID facts are missing; QA, security/privacy, performance, policy, or observability gates are unresolved; or a rollback plan and staged rollout criteria are missing for a production release.
- **Connector unreachable** — repo, CI, or Play Console evidence exists but cannot be read.

Otherwise proceed: missing listing copy, asset, or release-note detail is drafted with the assumption labeled inline and flagged for the owner before publish.

## Default output modes

A complete run writes all of these:

- `android-release-readiness.md`
- `android-build-package-checklist.md`
- `android-play-track-plan.md`
- `android-release-notes.md`
- `android-rollback-plan.md`

Mode-specific alternative:

- `workflow-halt.md` — replaces the set above when a hard halt fires. A failed or blocked gate is recorded in the readiness report as a no-go; it does not need a halt to be visible.

## Downstream handoff

Continue to `android-observability-liveops-desk` for launch monitoring and live-ops readiness.

## SDLC suite handoff

Use `release-operations-desk`, `deployment-desk`, `verification-desk`, and `observability-readiness-desk` when Android release work needs generic lifecycle support.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
