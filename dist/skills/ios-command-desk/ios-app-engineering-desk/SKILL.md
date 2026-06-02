---
name: ios-app-engineering-desk
description: prepare iOS native app implementation plans for Swift, Objective-C, SwiftUI, View systems, modularization, storage, networking, background work, sensors, permissions, and platform APIs.
---

# iOS App Engineering Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, update the `ios_delivery_packet`, and continue to the next stage when enough source facts are available.

If required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Do not invent repo state, iOS target versions, module ownership, package names, permissions, validation commands, or release targets.

## Role

Convert iOS app requirements and architecture into implementation-ready scope for native app work, including target modules/files, Swift/Objective-C patterns, SwiftUI/UIKit choices, data layer, storage, networking, background work, sensors, permissions, validation commands, and halt conditions.

Use `references/platform/ios-app-baseline.md` for modern app defaults when the repo does not define a stronger local convention.

## Workflow

1. Confirm the request is native or hybrid app work, not game runtime work.
2. Resolve accepted requirements, architecture, target repo, branch, modules, UI framework, platform APIs, dependencies, permissions, and validation commands.
3. Build a source-fact map from Xcode, manifests, source modules, CI, tests, and existing architecture conventions.
4. Produce implementation boundaries with exact files/modules, expected changes, acceptance gates, validation commands, and forbidden scope.
5. Hand off to SDLC implementation only when iOS-specific ambiguity is low.

## Responsibilities

- Plan Swift/Objective-C and iOS platform implementation without broad unconstrained coding prompts.
- Prefer modern iOS patterns when repo facts permit: Swift, SwiftUI, modularization, dependency injection, clean data layer, screenshot/UI tests, Instruments profiling, and MetricKit and launch/runtime profiling.
- Respect legacy UIKit, Objective-C, or existing architecture when the repo requires it.
- Keep platform APIs, permissions, lifecycle behavior, offline/sync behavior, and validation commands explicit.
- Avoid asking coding agents to rediscover build, architecture, or test facts this desk should settle first.

## Expected inputs

Accepted requirements, architecture brief, UI/UX brief, technical discovery memo, repo files, Xcode facts, API contracts, permissions, validation expectations, and prior `ios_delivery_packet`.

## Expected outputs

App engineering plan, file/module change map, implementation constraints, validation commands, risks, halt conditions, packet update, and downstream SDLC implementation handoff when ready.

## Evidence packet additions

- target modules and files
- app implementation lane: Swift, Objective-C, Compose, UIKit, hybrid, or legacy
- platform APIs and permissions
- data/state/storage/networking decisions
- validation commands and expected evidence
- scope boundaries and forbidden changes

## Packet fields to update

`app_or_game_lane`, `modules`, `ui_framework`, `permissions`, `backend_integrations`, `api_contracts`, `validation_commands`, `acceptance_gates`, `source_facts`, `risks`, `open_questions`, `artifacts`, `ready_to_continue`

## Halt conditions

- No target repo, branch, module, or file scope for implementation.
- Accepted requirements or architecture are missing.
- Platform APIs, permissions, lifecycle behavior, or validation commands are unclear.
- Requested implementation depends on unresolved backend, policy, signing, or release facts.

## Default output modes

- `ios-app-engineering-plan.md`
- `ios-app-source-facts.md`
- `ios-app-validation-commands.md`
- `ios-app-implementation-handoff.md`
- `workflow-halt.md`

## Downstream handoff

Use `implementation-handoff-desk` only after this desk has reduced iOS-specific ambiguity. The handoff must include exact files/modules, constraints, acceptance gates, validation commands, source facts, open questions, and halt conditions.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as issue planning, implementation handoff, review quality, test strategy, verification, CI failure triage, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
