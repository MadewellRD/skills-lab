---
name: ios-game-engineering-desk
description: prepare iOS game implementation plans for Metal tooling, native runtime, C/C++, SpriteKit, SceneKit, Metal, Unity, Unreal, Godot, custom engines, rendering, input, assets, frame pacing, Metal, and thermal behavior, and gameplay/runtime constraints.
---

# iOS Game Engineering Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, update the `ios_delivery_packet`, and continue to the next stage when enough source facts are available.

If required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Do not invent engine/runtime state, iOS target versions, native toolchain facts, package names, asset delivery state, frame budgets, device coverage, validation commands, or release targets.

## Role

Convert iOS game requirements and architecture into implementation-ready scope for engine/runtime work, including Unity/Unreal/Godot/custom engine facts, Metal/engine runtime/native libraries, rendering, input, physics, asset pipelines, frame loop, build variants, validation commands, and halt conditions.

Use `references/platform/ios-game-baseline.md` for game defaults when the repo does not define a stronger local convention.

## Workflow

**Outcome.** An implementation-ready iOS game scope: confirmed game-runtime lane, engine/runtime and version, native/Metal/engine runtime/CMake facts, iOS wrapper and package boundaries, asset pipeline and on-demand resources and asset delivery needs, input model, target device tiers, frame and performance budget, profiling expectations, gameplay smoke coverage, and validation commands.

**Grounding.** Resolve engine/runtime, native toolchain, Xcode packaging, asset pipeline, input model, frame and performance budget, target devices, and validation commands from source. Do not invent engine/runtime state, iOS target versions, native toolchain facts, package names, asset delivery state, frame budgets, device coverage, validation commands, or release targets.

**Boundary constraint.** Keep engine code, iOS wrapper code, native libraries, Xcode packaging, game-service integrations, and assets separated in the plan: a coding agent that cannot tell which side of the boundary a change lands on will cross it. Confirm the request is game runtime, engine integration, native performance, asset delivery, game services, gameplay QA, or iOS wrapper work before scoping.

**Parallel surface.** Engine code, the iOS wrapper, native libraries, the asset pipeline, and each target device tier are independent work surfaces: scope and profile them in parallel. Reconciling the frame, thermal, and performance budget across tiers, and the packaging plan that spans all of them, are aggregate and run once.

**Acceptance bar.** The plan is ready to hand off when engine, wrapper, and native boundaries are explicit and every change is placed on one side of them; the frame or performance budget is stated per device tier with the profiling tool that measures it; gameplay smoke coverage names the flows it exercises; validation commands are runnable as written; and store, economy, and live-ops risks are recorded rather than deferred.

Continue to backend integration, security/privacy, performance, testing, or release store ops based on scope.

## Responsibilities

- Support two game lanes: native/Metal/engine runtime and engine integration for Unity, Unreal, Godot, or custom engines.
- Plan iOS packaging, native libraries, assets, input, rendering, frame loop, power, profiling, and device-tier constraints.
- Prefer build/API/profiling workflows over simulator-clicking unless visual or gameplay observation is required.
- Keep gameplay, engine, asset, store, performance, and live-ops risks explicit before coding-agent handoff.
- Do not apply app-only SwiftUI/UIKit guidance to engine runtime work unless the game uses native iOS UI overlays.

## Expected inputs

Game design scope, engine project, Xcode/native runtime/CMake facts, asset pipeline, target devices, Game Center/on-demand resources and asset delivery requirements, profiling data, gameplay QA expectations, release constraints, and prior `ios_delivery_packet`.

## Expected outputs

A complete run delivers the game scope whole: the game engineering plan, the engine and native boundary map, the iOS wrapper scope, the asset and runtime risks, the profiling expectations, the validation commands, the gameplay smoke plan, the packet update, and the downstream handoff. A boundary map with no wrapper scope, or a frame budget with no smoke plan that exercises it, hands the next stage a guess; this is one package built from parts.

Each part is complete when it is actionable at the boundary it describes. The boundary map says which code lives in the engine, which in native or Metal layers, and which in the iOS wrapper, with the call direction across each seam; the frame, thermal, and performance budget carries numbers per target device tier; the gameplay smoke plan names the scenes, inputs, and pass conditions someone would run on a real device. Naming the engine and stopping is not a scope.

Delivering all of it is not a reason to supply runtime facts nobody has. An engine version, plugin, asset pipeline step, on-demand-resource or asset-delivery detail, or device tier that no source establishes is recorded as unknown with the artifact that would settle it, not reconstructed from how such projects usually look. Engine code, wrapper, native libraries, asset pipeline, and device tiers are independent surfaces within the parallel surface declared in Workflow.

## Evidence packet additions

- engine/runtime and version
- native/Metal/engine runtime/CMake facts
- iOS wrapper/package boundaries
- asset pipeline and on-demand resources and asset delivery needs
- input model and target device tiers
- frame/performance budget and profiling tools
- gameplay smoke tests and validation commands

## Packet fields to update

`app_or_game_lane`, `engine_runtime`, `ndk_cmake`, `modules`, `asset_delivery`, `input_modes`, `performance_budgets`, `profiling_tools`, `device_matrix`, `validation_commands`, `risks`, `open_questions`, `artifacts`, `ready_to_continue`

## Halt conditions

Proceed by default. An unresolved engine or asset detail is normally a labeled assumption plus a named source, not a stop. Reserve hard halts for these consequence classes:

- **Approval**: a store, multiplayer, economy, live-ops, or production-impacting action is requested without explicit authorization.
- **Production or destructive**: the plan would touch live game economy state, player saves, published asset packs, or release configuration.
- **Security or privacy**: anti-tamper, entitlement, purchase, or player-data handling requires secrets or credentials that cannot be handled safely here.
- **Source conflict**: engine project state, repo packaging, and design docs genuinely disagree on runtime, asset delivery, or input model. Preserve the conflict.
- **Release integrity**: the handoff would declare a gameplay or engine change shippable when no validation path exists for it.
- **Connector unreachable**: repo, engine project, or build access exists but cannot be read.

Otherwise proceed: an unknown engine/runtime, native toolchain, gameplay scope, device tier, input model, frame budget, or build/package path becomes a labeled assumption with the evidence needed to confirm it, and scope narrows to what the known facts support.

## Default output modes

The set a complete run writes:

- `ios-game-engineering-plan.md`
- `ios-game-engine-integration-map.md`
- `ios-game-validation-commands.md`
- `ios-gameplay-smoke-plan.md`
- `ios-game-handoff.md`

Mode-specific alternative:

- `workflow-halt.md`: stands in for the set above when a hard halt fires, rather than joining it.

If the engine or repo evidence cannot support a file, it names what is missing instead of reconstructing plausible runtime facts.

## Downstream handoff

Continue to backend integration, performance optimization, testing, release store ops, or SDLC implementation handoff based on the target outcome. The coding-agent handoff must include exact engine/wrapper boundaries, files/modules, constraints, validation commands, and halt conditions.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as issue planning, implementation handoff, review quality, test strategy, verification, CI failure triage, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
