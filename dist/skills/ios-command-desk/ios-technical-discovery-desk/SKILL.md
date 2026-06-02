---
name: ios-technical-discovery-desk
description: inspect iOS repo, Xcode, SDK, native runtime, dependency, manifest, device, simulator, engine, CI, feasibility, constraint, and unknown facts before implementation.
---

# iOS Technical Discovery Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing repo, Xcode, SDK, native runtime, engine, CI, device, or validation facts.

## Role

Collect iOS source truth before design or implementation: repo layout, modules, Xcode state, Swift/Objective-C versions, compile/min/target SDK, native runtime/CMake use, game engine, dependencies, manifests, permissions, CI, tests, device assumptions, and unknowns.

## Workflow

1. Run connector preflight for repo, branch, issues, PRs, workflows, docs, and uploaded files.
2. Identify build system, modules, Xcode wrapper, iOS Xcode Plugin, Swift/Objective-C, SDK/native runtime/CMake, dependency catalogs, manifests, and test commands.
3. Classify app/game stack: SwiftUI/UIKit/XML, Swift/Objective-C, native/Metal tooling, Unity, Unreal, Godot, custom engine, or mixed.
4. Produce feasibility paths, risks, unknowns, validation commands, and missing evidence.
5. Continue to architecture when discovery evidence is sufficient.

## Responsibilities

- Build a source-fact inventory before proposing implementation.
- Prefer file paths and commands over generic iOS advice.
- Identify repo-specific build, lint, test, benchmark, simulator, and CI gates.
- Surface missing SDK, signing, engine, App Store Connect, or validation facts as halt conditions.

## Expected inputs

Repo access, file tree, Xcode/settings/build files, iOSManifest files, CI workflows, test output, engine config, native runtime/CMake files, app/game docs, and prior `ios_delivery_packet`.

## Expected outputs

Technical discovery memo, source-facts table, feasibility assessment, validation commands, unknowns, risks, halt conditions, and packet update.

## Evidence packet additions

- repo layout and module graph
- Xcode, AGP, Swift, Objective-C, SDK, native runtime, and CMake facts
- manifest, permissions, bundle ID, and build variants
- engine/runtime and asset pipeline facts for game work
- CI/test/benchmark commands and validation evidence

## Packet fields to update

`repo`, `modules`, `build_system`, `xcode`, `kotlin_java`, `min_sdk`, `target_sdk`, `compile_sdk`, `ndk_cmake`, `engine_runtime`, `permissions`, `dependencies`, `ci`, `validation_commands`, `source_facts`, `risks`, `open_questions`, `ready_to_continue`

## Halt conditions

- Repo access, branch, or source scope is unavailable.
- Xcode/build files cannot be found or parsed.
- Engine/runtime facts are missing for game work.
- Signing, bundle ID, TestFlight group or App Store release state, or release state is required but unavailable.
- No validation command can be identified for the requested implementation.

## Default output modes

- `ios-technical-discovery.md`
- `ios-source-facts.md`
- `ios-validation-commands.md`
- `ios-feasibility-risks.md`
- `connector-diagnostic.md`

## Downstream handoff

Continue to `ios-architecture-design-desk` when enough repo and platform facts are available.

## SDLC suite handoff

Use `technical-discovery-desk` patterns for feasibility, constraints, evidence, spikes, unknowns, and halt conditions while preserving iOS-specific build and platform facts.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
