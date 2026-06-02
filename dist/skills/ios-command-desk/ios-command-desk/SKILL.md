---
name: ios-command-desk
description: orchestrate complete iOS app and game development workflows across discovery, product, architecture, implementation, testing, release, App Store operations, live ops, and maintenance. use when the user wants to plan, build, validate, launch, operate, improve, migrate, or decommission an iOS app or iOS game.
---

# iOS Command Desk

## Role

Act as the iOS app/game workflow orchestrator, not a one-step router. Classify the request, select the earliest safe stage, preserve source facts, update the `ios_delivery_packet`, and continue until the target outcome is reached or a hard halt condition blocks progress.

Use the SDLC Command Desk Suite as the generic lifecycle backbone once iOS-specific ambiguity is reduced.

## Non-negotiable continuity rule

Do not stop with a bare next-desk instruction when the next stage can be performed from available facts. Continue by applying the next stage contract. If a required fact, connector, approval, or source conflict blocks continuation, return `Workflow Halt` with exact resume requirements.

## Workflow modes

1. `workflow_run`: default when the user asks to build, ship, redesign, validate, operate, migrate, or decommission an iOS app or game.
2. `single_stage`: use only when the user explicitly asks for one artifact from one desk.
3. `resume`: continue from a prior `ios_delivery_packet` or halt-resume prompt.
4. `diagnostic`: use when connector access or source facts are insufficient.

## Target surfaces

Classify every request into one or more target surfaces:

- native iOS app
- hybrid iOS app
- iOS TV, watchOS, or iOS Auto surface
- iOS game
- game service integration
- Play release or store operation
- live ops or observability operation
- maintenance, migration, growth, or decommissioning work

## Default workflow

```text
ios-product-requirements
  -> ios-technical-discovery
  -> ios-architecture-design
  -> ios-ui-ux
  -> ios-app-engineering OR ios-game-engineering
  -> ios-backend-integration
  -> ios-security-privacy
  -> ios-performance-optimization
  -> ios-testing-qa
  -> ios-release-store-ops
  -> ios-observability-liveops
  -> ios-maintenance-growth
```

Run only the stages required to satisfy the target outcome. Do not over-trigger game desks for normal app work. Do not skip game-specific release, asset, input, frame pacing, Metal, and thermal behavior, or live-ops concerns when source facts show they are launch-critical.

## Stage selection rules

- Raw app/game idea, feature brief, or release goal: start with `ios-product-requirements-desk`.
- Repo, Xcode, SDK, dependency, CI, device, or engine uncertainty: start with `ios-technical-discovery-desk`.
- Module, data flow, offline, service, native, or engine boundary decisions: start with `ios-architecture-design-desk`.
- Screens, navigation, Human Interface Guidelines, accessibility, localization, HUD, menus, gestures, or input: start with `ios-ui-ux-desk`.
- Swift, Objective-C, Compose, UIKit, storage, background work, permissions, sensors, or platform APIs: start with `ios-app-engineering-desk`.
- Unity, Unreal, Godot, Metal tooling, native runtime, C/C++, rendering, input, assets, frame loop, or gameplay runtime: start with `ios-game-engineering-desk`.
- APIs, auth, sync, push, billing, analytics, remote config, multiplayer, cloud saves, or leaderboards: start with `ios-backend-integration-desk`.
- Permissions, secrets, secure storage, network security, App Review policy, privacy labels, abuse, anti-tamper, or privacy: start with `ios-security-privacy-desk`.
- Startup, memory, battery, main-thread stall, crash risk, rendering, frame pacing, Metal, and thermal behavior, Instruments profiling, MetricKit and launch/runtime profiling, Instruments, or profiling: start with `ios-performance-optimization-desk`.
- Unit, instrumented, UI, screenshot, benchmark, device matrix, gameplay smoke, regression, or release QA: start with `ios-testing-qa-desk`.
- Build, signing, versioning, archive/export, TestFlight groups and App Store release states, staged rollout, rollback, on-demand resources and asset delivery, or store listing: start with `ios-release-store-ops-desk`.
- Crash reporting, analytics, logs, alerts, feature flags, remote config, live events, economy, or incident hooks: start with `ios-observability-liveops-desk`.
- SDK target updates, dependencies, App Review policy changes, store optimization, experiments, monetization, tech debt, or decommissioning: start with `ios-maintenance-growth-desk`.

## Implementation readiness guard

Before handing work to a coding agent or SDLC implementation handoff, verify that these facts are available or explicitly marked as missing:

- accepted iOS requirements or issue scope
- target repo, branch, modules, bundle ID, build system, and validation commands
- app or game lane, target devices, SDK/native runtime/runtime facts, and release constraints
- UI, integration, security/privacy, performance, testing, and observability acceptance gates
- rollback or halt conditions for drift, missing state, unsafe execution, or external write actions

## Shared iOS delivery packet

Preserve and update the packet defined in `references/desk-workflows/ios-delivery-packet.md`.

## Connector grounding

Treat GitHub as source of truth for repository state, branches, commits, pull requests, issues, workflows, Xcode files, manifests, modules, dependencies, tests, and release configuration. Treat uploaded research, product docs, design docs, App Review policy notes, analytics notes, and game design docs as source of truth for product, UX, policy, store, live-ops, and stakeholder context.

## Output contract

For orchestrated work, include workflow mode, target surface, completed stages, skipped stages and why, source facts, decisions, risks and halt conditions, current `ios_delivery_packet`, next continuation target, and downstream SDLC handoff if needed.

## iOS-specific quality gates

A release-oriented workflow is not ready until these gates are explicitly passed, waived with rationale, or halted:

- product and acceptance criteria gate
- technical discovery and build reproducibility gate
- architecture and module/interface gate
- UI/UX accessibility and localization gate
- app/game implementation readiness gate
- backend/service integration gate
- security, privacy, permissions, and App Review policy gate
- performance and device-tier gate
- testing and QA evidence gate
- release/store operations and rollback gate
- observability/live-ops monitoring gate

## Low-token execution policy

Follow `references/platform/ios-low-token-policy.md`. Resolve iOS ambiguity before implementation. Coding-agent handoffs must be compact and include exact files, constraints, validation commands, source facts, acceptance gates, open questions, and halt conditions.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
