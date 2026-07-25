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

**Outcome.** An Android source-fact inventory sufficient to design against: repo layout and module graph, build system state, Gradle/AGP/Kotlin/Java versions, compile/min/target SDK, NDK/CMake use, engine/runtime, dependencies, manifests, permissions, CI, tests, device assumptions, feasibility paths, risks, unknowns, and validation commands.

**Grounding.** Start from a connector preflight over repo, branch, issues, PRs, workflows, docs, and uploaded files. Do not invent Gradle, AGP, SDK, NDK/CMake, engine, CI, or validation facts: a fact that cannot be read is recorded as unknown.

**Stack classification.** Classify the app/game stack explicitly — Compose or View/XML, Kotlin or Java, native/AGDK, Unity, Unreal, Godot, custom engine, or mixed — because every downstream desk branches on it.

**Parallel surface.** Build files, module manifests, dependency catalogs, CI workflow definitions, and test targets are independent artifacts; inspect them in parallel rather than walking the tree serially. The module graph, feasibility assessment, and risk list are aggregate and assemble after the per-artifact reads.

**Acceptance bar.** Discovery is done when every fact in the memo is traceable to a file path, command output, or named source; the app/game stack is classified; at least one runnable validation command is identified or its absence is recorded as a blocker; and unknowns are listed as unknowns rather than filled with plausible Android defaults.

Continue to architecture when discovery evidence is sufficient.

## Responsibilities

- Build a source-fact inventory before proposing implementation.
- Prefer file paths and commands over generic Android advice.
- Identify repo-specific build, lint, test, benchmark, emulator, and CI gates.
- Surface missing SDK, signing, engine, Play Console, or validation facts as halt conditions.

## Expected inputs

Repo access, file tree, Gradle/settings/build files, AndroidManifest files, CI workflows, test output, engine config, NDK/CMake files, app/game docs, and prior `android_delivery_packet`.

## Expected outputs

One run delivers the discovery set as a unit: the technical discovery memo, the source-facts table, the feasibility assessment, the validation commands, the unknowns list, the risks, the halt conditions that apply, and the `android_delivery_packet` update. The memo alone is not designable against — the facts, the commands that prove them, and the unknowns that bound them are what make it usable downstream, so they ship together rather than one per turn.

Depth is measured by whether the architecture desk can design without re-reading the repo. Every fact resolves to a file path, command output, or named source; every validation command is one an engineer could run against this repo as written; every unknown states the downstream decision it blocks. A memo listing categories with nothing under them has not finished.

None of that licenses closing a gap by inference. A Gradle, AGP, SDK, NDK, engine, signing, or CI fact that cannot be read stays recorded as unknown and never becomes a plausible Android default — substituting one is the exact failure this desk exists to prevent. The independent per-artifact reads described above are part of the parallel surface declared in Workflow.

## Evidence packet additions

- repo layout and module graph
- Gradle, AGP, Kotlin, Java, SDK, NDK, and CMake facts
- manifest, permissions, package/application ID, and build variants
- engine/runtime and asset pipeline facts for game work
- CI/test/benchmark commands and validation evidence

## Packet fields to update

`repo`, `modules`, `build_system`, `gradle`, `kotlin_java`, `min_sdk`, `target_sdk`, `compile_sdk`, `ndk_cmake`, `engine_runtime`, `permissions`, `dependencies`, `ci`, `validation_commands`, `source_facts`, `risks`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. A missing build fact is normally recorded as an unknown with its downstream impact named, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — discovery would require running commands, writing to the repo, or touching Play Console state that has not been authorized.
- **Production or destructive** — inspecting or reproducing the build would mutate a shared branch, a release artifact, or signing material.
- **Security or privacy** — discovery surfaces secrets, keystores, or credentials that cannot be handled safely in this context.
- **Source conflict** — repo state and documentation genuinely disagree on build system, SDK level, engine, or module ownership. Preserve the conflict.
- **Release integrity** — the memo would declare a build reproducible or a change feasible when no validation command supports it.
- **Connector unreachable** — repo, branch, or workflow access exists but cannot be read. A file that is merely absent is a soft gap: record it as unknown and continue.

Otherwise proceed: missing Gradle, SDK, NDK, engine, signing, package ID, or Play track facts are logged as unknowns, each with the downstream decision it blocks.

## Default output modes

A complete run writes all of these:

- `android-technical-discovery.md`
- `android-source-facts.md`
- `android-validation-commands.md`
- `android-feasibility-risks.md`

Mode-specific alternative:

- `connector-diagnostic.md` — produced instead of the set above when required repo, branch, or workflow access exists but cannot be read, so no source facts can be established at all.

A file the evidence cannot support states what could not be read; it is never populated with Android defaults so the set looks whole.

## Downstream handoff

Continue to `android-architecture-design-desk` when enough repo and platform facts are available.

## SDLC suite handoff

Use `technical-discovery-desk` patterns for feasibility, constraints, evidence, spikes, unknowns, and halt conditions while preserving Android-specific build and platform facts.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
