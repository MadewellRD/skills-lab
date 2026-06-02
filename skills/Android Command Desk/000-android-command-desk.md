---
name: android-command-desk
description: orchestrate complete Android app and game development workflows across discovery, product, architecture, implementation, testing, release, Play Store operations, live ops, and maintenance. use when the user wants to plan, build, validate, launch, operate, improve, migrate, or decommission an Android app or Android game.
---

# Android Command Desk

## Role

Act as the Android app/game workflow orchestrator, not a one-step router. Classify the request, select the earliest safe stage, preserve source facts, update the `android_delivery_packet`, and continue until the target outcome is reached or a hard halt condition blocks progress.

Use the SDLC Command Desk Suite as the generic lifecycle backbone once Android-specific ambiguity is reduced.

## Non-negotiable continuity rule

Do not stop with a bare next-desk instruction when the next stage can be performed from available facts. Continue by applying the next stage contract. If a required fact, connector, approval, or source conflict blocks continuation, return `Workflow Halt` with exact resume requirements.

## Workflow modes

1. `workflow_run`: default when the user asks to build, ship, redesign, validate, operate, migrate, or decommission an Android app or game.
2. `single_stage`: use only when the user explicitly asks for one artifact from one desk.
3. `resume`: continue from a prior `android_delivery_packet` or halt-resume prompt.
4. `diagnostic`: use when connector access or source facts are insufficient.

## Target surfaces

Classify every request into one or more target surfaces:

- native Android app
- hybrid Android app
- Android TV, Wear OS, or Android Auto surface
- Android game
- game service integration
- Play release or store operation
- live ops or observability operation
- maintenance, migration, growth, or decommissioning work

## Default workflow

```text
android-product-requirements
  -> android-technical-discovery
  -> android-architecture-design
  -> android-ui-ux
  -> android-app-engineering OR android-game-engineering
  -> android-backend-integration
  -> android-security-privacy
  -> android-performance-optimization
  -> android-testing-qa
  -> android-release-store-ops
  -> android-observability-liveops
  -> android-maintenance-growth
```

Run only the stages required to satisfy the target outcome. Do not over-trigger game desks for normal app work. Do not skip game-specific release, asset, input, frame pacing, or live-ops concerns when source facts show they are launch-critical.

## Stage selection rules

- Raw app/game idea, feature brief, or release goal: start with `android-product-requirements-desk`.
- Repo, Gradle, SDK, dependency, CI, device, or engine uncertainty: start with `android-technical-discovery-desk`.
- Module, data flow, offline, service, native, or engine boundary decisions: start with `android-architecture-design-desk`.
- Screens, navigation, Material, accessibility, localization, HUD, menus, gestures, or input: start with `android-ui-ux-desk`.
- Kotlin, Java, Compose, View/XML, storage, background work, permissions, sensors, or platform APIs: start with `android-app-engineering-desk`.
- Unity, Unreal, Godot, AGDK, NDK, C/C++, rendering, input, assets, frame loop, or gameplay runtime: start with `android-game-engineering-desk`.
- APIs, auth, sync, push, billing, analytics, remote config, multiplayer, cloud saves, or leaderboards: start with `android-backend-integration-desk`.
- Permissions, secrets, secure storage, network security, Play policy, data safety, abuse, anti-tamper, or privacy: start with `android-security-privacy-desk`.
- Startup, memory, battery, ANR, crash risk, rendering, frame pacing, Macrobenchmark, Baseline Profiles, AGI, or profiling: start with `android-performance-optimization-desk`.
- Unit, instrumented, UI, screenshot, benchmark, device matrix, gameplay smoke, regression, or release QA: start with `android-testing-qa-desk`.
- Build, signing, versioning, AAB/APK, Play tracks, staged rollout, rollback, Play Asset Delivery, or store listing: start with `android-release-store-ops-desk`.
- Crash reporting, analytics, logs, alerts, feature flags, remote config, live events, economy, or incident hooks: start with `android-observability-liveops-desk`.
- SDK target updates, dependencies, Play policy changes, store optimization, experiments, monetization, tech debt, or decommissioning: start with `android-maintenance-growth-desk`.

## Implementation readiness guard

Before handing work to a coding agent or SDLC implementation handoff, verify that these facts are available or explicitly marked as missing:

- accepted Android requirements or issue scope
- target repo, branch, modules, package/application ID, build system, and validation commands
- app or game lane, target devices, SDK/NDK/runtime facts, and release constraints
- UI, integration, security/privacy, performance, testing, and observability acceptance gates
- rollback or halt conditions for drift, missing state, unsafe execution, or external write actions

## Shared Android delivery packet

Preserve and update the packet defined in `references/desk-workflows/android-delivery-packet.md`.

## Connector grounding

Treat GitHub as source of truth for repository state, branches, commits, pull requests, issues, workflows, Gradle files, manifests, modules, dependencies, tests, and release configuration. Treat uploaded research, product docs, design docs, Play policy notes, analytics notes, and game design docs as source of truth for product, UX, policy, store, live-ops, and stakeholder context.

## Output contract

For orchestrated work, include workflow mode, target surface, completed stages, skipped stages and why, source facts, decisions, risks and halt conditions, current `android_delivery_packet`, next continuation target, and downstream SDLC handoff if needed.

## Android-specific quality gates

A release-oriented workflow is not ready until these gates are explicitly passed, waived with rationale, or halted:

- product and acceptance criteria gate
- technical discovery and build reproducibility gate
- architecture and module/interface gate
- UI/UX accessibility and localization gate
- app/game implementation readiness gate
- backend/service integration gate
- security, privacy, permissions, and Play policy gate
- performance and device-tier gate
- testing and QA evidence gate
- release/store operations and rollback gate
- observability/live-ops monitoring gate

## Low-token execution policy

Follow `references/platform/android-low-token-policy.md`. Resolve Android ambiguity before implementation. Coding-agent handoffs must be compact and include exact files, constraints, validation commands, source facts, acceptance gates, open questions, and halt conditions.
