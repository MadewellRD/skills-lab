---
name: android-game-engineering-desk
description: prepare Android game implementation plans for AGDK, NDK, C/C++, Unity, Unreal, Godot, custom engines, rendering, input, assets, frame pacing, and gameplay/runtime constraints.
---

# Android Game Engineering Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, update the `android_delivery_packet`, and continue to the next stage when enough source facts are available.

If required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Do not invent engine/runtime state, Android target versions, native toolchain facts, package names, asset delivery state, frame budgets, device coverage, validation commands, or release targets.

## Role

Convert Android game requirements and architecture into implementation-ready scope for engine/runtime work, including Unity/Unreal/Godot/custom engine facts, AGDK/NDK/native libraries, rendering, input, physics, asset pipelines, frame loop, build variants, validation commands, and halt conditions.

Use `references/platform/android-game-baseline.md` for game defaults when the repo does not define a stronger local convention.

## Workflow

1. Confirm the request is game runtime, engine integration, native performance, asset delivery, Play Games services, gameplay QA, or Android wrapper work.
2. Resolve engine/runtime, native toolchain, Gradle packaging, asset pipeline, input model, frame/performance budget, target devices, and validation commands.
3. Separate engine code, Android wrapper code, native libraries, Gradle packaging, Play-service integrations, and assets.
4. Produce implementation boundaries, gameplay smoke coverage, profiling expectations, and validation commands.
5. Continue to backend integration, security/privacy, performance, testing, or release store ops based on scope.

## Responsibilities

- Support two game lanes: native/AGDK/NDK and engine integration for Unity, Unreal, Godot, or custom engines.
- Plan Android packaging, native libraries, assets, input, rendering, frame loop, power, profiling, and device-tier constraints.
- Prefer build/API/profiling workflows over emulator-clicking unless visual or gameplay observation is required.
- Keep gameplay, engine, asset, store, performance, and live-ops risks explicit before coding-agent handoff.
- Do not apply app-only Compose/View guidance to engine runtime work unless the game uses native Android UI overlays.

## Expected inputs

Game design scope, engine project, Gradle/NDK/CMake facts, asset pipeline, target devices, Play Games/Play Asset Delivery requirements, profiling data, gameplay QA expectations, release constraints, and prior `android_delivery_packet`.

## Expected outputs

Game engineering plan, engine/native boundary map, Android wrapper scope, asset/runtime risks, profiling expectations, validation commands, gameplay smoke plan, packet update, and downstream handoff.

## Evidence packet additions

- engine/runtime and version
- native/AGDK/NDK/CMake facts
- Android wrapper/package boundaries
- asset pipeline and Play Asset Delivery needs
- input model and target device tiers
- frame/performance budget and profiling tools
- gameplay smoke tests and validation commands

## Packet fields to update

`app_or_game_lane`, `engine_runtime`, `ndk_cmake`, `modules`, `asset_delivery`, `input_modes`, `performance_budgets`, `profiling_tools`, `device_matrix`, `validation_commands`, `risks`, `open_questions`, `artifacts`, `ready_to_continue`

## Halt conditions

- Engine/runtime or native toolchain is unknown.
- Gameplay scope, target devices, input model, or frame budget is missing.
- Build/package/release path is unknown.
- Requested Play, multiplayer, economy, live-ops, or production-impacting action lacks approval.
- No validation path exists for the requested gameplay or engine change.

## Default output modes

- `android-game-engineering-plan.md`
- `android-game-engine-integration-map.md`
- `android-game-validation-commands.md`
- `android-gameplay-smoke-plan.md`
- `android-game-handoff.md`
- `workflow-halt.md`

## Downstream handoff

Continue to backend integration, performance optimization, testing, release store ops, or SDLC implementation handoff based on the target outcome. The coding-agent handoff must include exact engine/wrapper boundaries, files/modules, constraints, validation commands, and halt conditions.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as issue planning, implementation handoff, review quality, test strategy, verification, CI failure triage, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
