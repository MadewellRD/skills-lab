---
name: ios-architecture-design-desk
description: design iOS app and game architecture, module boundaries, data flow, offline behavior, engine integration, services, APIs, migrations, and ADR-ready decisions.
---

# iOS Architecture Design Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing repo architecture, runtime constraints, service contracts, migration scope, or validation facts.

## Role

Define iOS architecture for app and game work: modules, layers, state, data flow, storage, networking, engine boundaries, native/plugin boundaries, background work, API contracts, migration impact, ADR decisions, and validation gates.

## Workflow

1. Start from accepted requirements and technical discovery facts.
2. Choose or validate architecture lane: modern native app, legacy migration, modularization, native/game engine, Unity/Unreal/Godot integration, or mixed.
3. Define module boundaries, data/state flow, threading/concurrency, storage, background work, service contracts, and engine/native boundaries.
4. Record decisions and rejected alternatives with risks and validation gates.
5. Continue to UI/UX, app engineering, or game engineering based on target outcome.

## Responsibilities

- Ground architecture in current repo structure and iOS app/game evidence.
- For app work, account for Swift, SwiftUI/UIKit, modularization, DI, data layer, offline/sync, Instruments profiling, and Baseline Profile implications.
- For game work, account for engine/runtime boundaries, native libraries, asset delivery, frame loop, input, and profiling constraints.
- Produce ADR-ready decisions before implementation handoff.

## Expected inputs

iOS PRD, discovery memo, repo facts, existing architecture docs, service contracts, design/game docs, performance/security constraints, and prior `ios_delivery_packet`.

## Expected outputs

Architecture brief, ADR notes, module/interface map, migration plan, risks, validation expectations, and packet update.

## Evidence packet additions

- architecture lane and rejected alternatives
- module boundaries and ownership
- data/state flow, storage, networking, and background work
- engine/native/plugin boundaries for game work
- ADR decisions, risks, and validation gates

## Packet fields to update

`architecture_lane`, `modules`, `interfaces`, `data_flow`, `state_management`, `storage`, `networking`, `background_work`, `engine_runtime`, `migrations`, `risks`, `validation_commands`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Accepted requirements or discovery facts are missing.
- Target framework, runtime, architecture lane, or migration scope is unresolved.
- API/service contracts are unknown and architecture depends on them.
- Validation gates cannot be tied to source evidence.

## Default output modes

- `ios-architecture-brief.md`
- `ios-adr.md`
- `ios-module-map.md`
- `ios-migration-plan.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-ui-ux-desk` for screen/interaction work, `ios-app-engineering-desk` for native implementation, or `ios-game-engineering-desk` for game runtime work.

## SDLC suite handoff

Use `architecture-design-desk` patterns for ADRs, interface contracts, migration planning, and architectural risks while preserving iOS-specific platform and runtime constraints.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
