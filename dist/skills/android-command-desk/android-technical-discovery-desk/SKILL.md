---
name: android-technical-discovery-desk
description: inspect Android repo, Gradle, SDK, NDK, dependency, manifest, device, emulator, engine, CI, feasibility, constraint, and unknown facts before implementation.
---

# Android Technical Discovery Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing repo, Gradle, SDK, NDK, engine, CI, device, or validation facts.

## Role

Collect Android source truth before design or implementation: repo layout, modules, Gradle state, Kotlin/Java versions, compile/min/target SDK, NDK/CMake use, game engine, dependencies, manifests, permissions, CI, tests, device assumptions, and unknowns.

## Workflow

1. Run connector preflight for repo, branch, issues, PRs, workflows, docs, and uploaded files.
2. Identify build system, modules, Gradle wrapper, Android Gradle Plugin, Kotlin/Java, SDK/NDK/CMake, dependency catalogs, manifests, and test commands.
3. Classify app/game stack: Compose/View/XML, Kotlin/Java, native/AGDK, Unity, Unreal, Godot, custom engine, or mixed.
4. Produce feasibility paths, risks, unknowns, validation commands, and missing evidence.
5. Continue to architecture when discovery evidence is sufficient.

## Responsibilities

- Build a source-fact inventory before proposing implementation.
- Prefer file paths and commands over generic Android advice.
- Identify repo-specific build, lint, test, benchmark, emulator, and CI gates.
- Surface missing SDK, signing, engine, Play Console, or validation facts as halt conditions.

## Expected inputs

Repo access, file tree, Gradle/settings/build files, AndroidManifest files, CI workflows, test output, engine config, NDK/CMake files, app/game docs, and prior `android_delivery_packet`.

## Expected outputs

Technical discovery memo, source-facts table, feasibility assessment, validation commands, unknowns, risks, halt conditions, and packet update.

## Evidence packet additions

- repo layout and module graph
- Gradle, AGP, Kotlin, Java, SDK, NDK, and CMake facts
- manifest, permissions, package/application ID, and build variants
- engine/runtime and asset pipeline facts for game work
- CI/test/benchmark commands and validation evidence

## Packet fields to update

`repo`, `modules`, `build_system`, `gradle`, `kotlin_java`, `min_sdk`, `target_sdk`, `compile_sdk`, `ndk_cmake`, `engine_runtime`, `permissions`, `dependencies`, `ci`, `validation_commands`, `source_facts`, `risks`, `open_questions`, `ready_to_continue`

## Halt conditions

- Repo access, branch, or source scope is unavailable.
- Gradle/build files cannot be found or parsed.
- Engine/runtime facts are missing for game work.
- Signing, package ID, Play track, or release state is required but unavailable.
- No validation command can be identified for the requested implementation.

## Default output modes

- `android-technical-discovery.md`
- `android-source-facts.md`
- `android-validation-commands.md`
- `android-feasibility-risks.md`
- `connector-diagnostic.md`

## Downstream handoff

Continue to `android-architecture-design-desk` when enough repo and platform facts are available.

## SDLC suite handoff

Use `technical-discovery-desk` patterns for feasibility, constraints, evidence, spikes, unknowns, and halt conditions while preserving Android-specific build and platform facts.
