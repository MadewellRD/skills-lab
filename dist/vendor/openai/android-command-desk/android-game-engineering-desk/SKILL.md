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

**Outcome.** An implementation-ready Android game scope: confirmed game-runtime lane, engine/runtime and version, native/AGDK/NDK/CMake facts, Android wrapper and package boundaries, asset pipeline and Play Asset Delivery needs, input model, target device tiers, frame and performance budget, profiling expectations, gameplay smoke coverage, and validation commands.

**Grounding.** Resolve engine/runtime, native toolchain, Gradle packaging, asset pipeline, input model, frame and performance budget, target devices, and validation commands from source. Do not invent engine/runtime state, Android target versions, native toolchain facts, package names, asset delivery state, frame budgets, device coverage, validation commands, or release targets.

**Boundary constraint.** Keep engine code, Android wrapper code, native libraries, Gradle packaging, Play-service integrations, and assets separated in the plan: a coding agent that cannot tell which side of the boundary a change lands on will cross it. Confirm the request is game runtime, engine integration, native performance, asset delivery, Play Games services, gameplay QA, or Android wrapper work before scoping.

**Parallel surface.** Engine code, the Android wrapper, native libraries, the asset pipeline, and each target device tier are independent work surfaces: scope and profile them in parallel. Reconciling the frame and performance budget across tiers, and the packaging plan that spans all of them, are aggregate and run once.

**Acceptance bar.** The plan is ready to hand off when engine, wrapper, and native boundaries are explicit and every change is placed on one side of them; the frame or performance budget is stated per device tier with the profiling tool that measures it; gameplay smoke coverage names the flows it exercises; validation commands are runnable as written; and store, economy, and live-ops risks are recorded rather than deferred.

Continue to backend integration, security/privacy, performance, testing, or release store ops based on scope.

## Responsibilities

- Support two game lanes: native/AGDK/NDK and engine integration for Unity, Unreal, Godot, or custom engines.
- Plan Android packaging, native libraries, assets, input, rendering, frame loop, power, profiling, and device-tier constraints.
- Prefer build/API/profiling workflows over emulator-clicking unless visual or gameplay observation is required.
- Keep gameplay, engine, asset, store, performance, and live-ops risks explicit before coding-agent handoff.
- Do not apply app-only Compose/View guidance to engine runtime work unless the game uses native Android UI overlays.

## Expected inputs

Game design scope, engine project, Gradle/NDK/CMake facts, asset pipeline, target devices, Play Games/Play Asset Delivery requirements, profiling data, gameplay QA expectations, release constraints, and prior `android_delivery_packet`.

## Expected outputs

A complete run delivers the whole game scope together: the game engineering plan, the engine and native boundary map, the Android wrapper scope, the asset and runtime risks, the profiling expectations, the validation commands, the gameplay smoke plan, the packet update, and the downstream handoff. A boundary map without the wrapper scope, or a frame budget without the smoke plan that exercises it, leaves the next stage guessing — this is one deliverable assembled from parts, not a set of options.

Each part is complete when it is actionable at the engine boundary. The boundary map names which code lives in the engine, which in native libraries, and which in the Android wrapper, with the call direction across each boundary; the frame and performance budget states numbers per target device tier; the gameplay smoke plan names the scenes, inputs, and pass conditions someone would actually run on a device. Naming an engine and stopping there is not a scope.

Delivering all of it is never a reason to invent runtime facts. An engine version, plugin, asset pipeline step, AGDK or NDK detail, or device tier that no source establishes is recorded as unknown with the artifact that would settle it — never filled in from how such projects usually look. Engine code, wrapper, native libraries, asset pipeline, and device tiers are independent surfaces and are part of the parallel surface declared in Workflow.

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

Proceed by default. An unresolved engine or asset detail is normally a labeled assumption plus a named source, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — a Play, multiplayer, economy, live-ops, or production-impacting action is requested without explicit authorization.
- **Production or destructive** — the plan would touch live game economy state, player saves, published asset packs, or release configuration.
- **Security or privacy** — anti-tamper, entitlement, purchase, or player-data handling requires secrets or credentials that cannot be handled safely here.
- **Source conflict** — engine project state, repo packaging, and design docs genuinely disagree on runtime, asset delivery, or input model. Preserve the conflict.
- **Release integrity** — the handoff would declare a gameplay or engine change shippable when no validation path exists for it.
- **Connector unreachable** — repo, engine project, or build access exists but cannot be read.

Otherwise proceed: an unknown engine/runtime, native toolchain, gameplay scope, device tier, input model, frame budget, or build/package path becomes a labeled assumption with the evidence needed to confirm it, and scope narrows to what the known facts support.

## Default output modes

A complete run writes all of these:

- `android-game-engineering-plan.md`
- `android-game-engine-integration-map.md`
- `android-game-validation-commands.md`
- `android-gameplay-smoke-plan.md`
- `android-game-handoff.md`

Mode-specific alternative:

- `workflow-halt.md` — takes the place of the set above when a hard halt fires, rather than joining it.

A file the engine and repo evidence cannot support states what is missing instead of being written from how such projects usually look.

## Downstream handoff

Continue to backend integration, performance optimization, testing, release store ops, or SDLC implementation handoff based on the target outcome. The coding-agent handoff must include exact engine/wrapper boundaries, files/modules, constraints, validation commands, and halt conditions.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as issue planning, implementation handoff, review quality, test strategy, verification, CI failure triage, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
