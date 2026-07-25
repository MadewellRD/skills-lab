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

**Outcome.** An iOS source-fact inventory sufficient to design against: repo layout and module graph, build system state, Xcode and toolchain versions, Swift/Objective-C versions, compile/min/target SDK, native runtime and CMake use, engine/runtime, dependencies, manifests, permissions, CI, tests, device assumptions, feasibility paths, risks, unknowns, and validation commands.

**Grounding.** Start from a connector preflight over repo, branch, issues, PRs, workflows, docs, and uploaded files. Do not invent repo, Xcode, SDK, native runtime, engine, CI, device, or validation facts: a fact that cannot be read is recorded as unknown.

**Stack classification.** Classify the app/game stack explicitly, SwiftUI, UIKit, Swift or Objective-C, native/Metal tooling, Unity, Unreal, Godot, custom engine, or mixed, because every downstream desk branches on it.

**Parallel surface.** Build and settings files, module manifests, dependency catalogs, CI workflow definitions, and test targets are independent artifacts; inspect them in parallel rather than walking the tree serially. The module graph, feasibility assessment, and risk list are aggregate and assemble after the per-artifact reads.

**Acceptance bar.** Discovery is done when every fact in the memo is traceable to a file path, command output, or named source; the app/game stack is classified; at least one runnable validation command is identified or its absence is recorded as a blocker; and unknowns are listed as unknowns rather than filled with plausible iOS defaults.

Continue to architecture when discovery evidence is sufficient.

## Responsibilities

- Build a source-fact inventory before proposing implementation.
- Prefer file paths and commands over generic iOS advice.
- Identify repo-specific build, lint, test, benchmark, simulator, and CI gates.
- Surface missing SDK, signing, engine, App Store Connect, or validation facts as halt conditions.

## Expected inputs

Repo access, file tree, Xcode/settings/build files, iOSManifest files, CI workflows, test output, engine config, native runtime/CMake files, app/game docs, and prior `ios_delivery_packet`.

## Expected outputs

A run that finishes hands over the discovery set whole: the technical discovery memo, the source-facts table, the feasibility assessment, the validation commands, the unknowns, the risks, any halt conditions that apply, and the `ios_delivery_packet` update. The memo on its own cannot be designed against; what makes it usable is the facts behind it, the commands that demonstrate them, and the explicit boundary of what is still unknown.

The standard is that the architecture desk should not need to reopen the repo. Each fact traces to a file path, a command's output, or a named source; each validation command runs against this project as written, with the scheme, destination, or target it needs; each unknown states which downstream decision it holds up. A memo that lists categories and leaves the values blank has not finished.

That standard is not met by inference. An Xcode version, toolchain, deployment target, Swift or Objective-C detail, dependency, signing fact, or CI setting that cannot be read stays an unknown, never a plausible iOS default, which would read as evidence and be treated as one. Build and settings files, manifests, dependency catalogs, CI definitions, and test targets are independent reads and belong to the parallel surface declared in Workflow.

## Evidence packet additions

- repo layout and module graph
- Xcode, AGP, Swift, Objective-C, SDK, native runtime, and CMake facts
- manifest, permissions, bundle ID, and build variants
- engine/runtime and asset pipeline facts for game work
- CI/test/benchmark commands and validation evidence

## Packet fields to update

`repo`, `modules`, `build_system`, `xcode`, `swift_objc`, `min_ios_version`, `target_sdk`, `deployment_target`, `xcframework_cmake`, `engine_runtime`, `permissions`, `dependencies`, `ci`, `validation_commands`, `source_facts`, `risks`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. A missing build fact is normally recorded as an unknown with its downstream impact named, not a stop. Reserve hard halts for these consequence classes:

- **Approval**: discovery would require running commands, writing to the repo, or touching App Store Connect state that has not been authorized.
- **Production or destructive**: inspecting or reproducing the build would mutate a shared branch, a release artifact, or signing and provisioning material.
- **Security or privacy**: discovery surfaces secrets, signing certificates, provisioning profiles, or credentials that cannot be handled safely in this context.
- **Source conflict**: repo state and documentation genuinely disagree on build system, SDK level, engine, or module ownership. Preserve the conflict.
- **Release integrity**: the memo would declare a build reproducible or a change feasible when no validation command supports it.
- **Connector unreachable**: repo, branch, or workflow access exists but cannot be read. A file that is merely absent is a soft gap: record it as unknown and continue.

Otherwise proceed: missing Xcode, SDK, native runtime, engine, signing, bundle ID, or TestFlight and App Store release-state facts are logged as unknowns, each with the downstream decision it blocks.

## Default output modes

The set a complete run writes:

- `ios-technical-discovery.md`
- `ios-source-facts.md`
- `ios-validation-commands.md`
- `ios-feasibility-risks.md`

Mode-specific alternative:

- `connector-diagnostic.md`: takes the place of the set above when required repo, branch, or workflow access exists but cannot be read, leaving no source facts to establish.

Where the evidence could not be read, the file says exactly that. It is never completed with iOS defaults so the set appears finished.

## Downstream handoff

Continue to `ios-architecture-design-desk` when enough repo and platform facts are available.

## SDLC suite handoff

Use `technical-discovery-desk` patterns for feasibility, constraints, evidence, spikes, unknowns, and halt conditions while preserving iOS-specific build and platform facts.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
