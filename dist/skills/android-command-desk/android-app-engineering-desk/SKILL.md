---
name: android-app-engineering-desk
description: prepare Android native app implementation plans for Kotlin, Java, Jetpack Compose, View systems, modularization, storage, networking, background work, sensors, permissions, and platform APIs.
---

# Android App Engineering Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, update the `android_delivery_packet`, and continue to the next stage when enough source facts are available.

If required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Do not invent repo state, Android target versions, module ownership, package names, permissions, validation commands, or release targets.

## Role

Convert Android app requirements and architecture into implementation-ready scope for native app work, including target modules/files, Kotlin/Java patterns, Compose/View choices, data layer, storage, networking, background work, sensors, permissions, validation commands, and halt conditions.

Use `references/platform/android-app-baseline.md` for modern app defaults when the repo does not define a stronger local convention.

## Workflow

1. Confirm the request is native or hybrid app work, not game runtime work.
2. Resolve accepted requirements, architecture, target repo, branch, modules, UI framework, platform APIs, dependencies, permissions, and validation commands.
3. Build a source-fact map from Gradle, manifests, source modules, CI, tests, and existing architecture conventions.
4. Produce implementation boundaries with exact files/modules, expected changes, acceptance gates, validation commands, and forbidden scope.
5. Hand off to SDLC implementation only when Android-specific ambiguity is low.

## Responsibilities

- Plan Kotlin/Java and Android platform implementation without broad unconstrained coding prompts.
- Prefer modern Android patterns when repo facts permit: Kotlin, Jetpack Compose, modularization, dependency injection, clean data layer, screenshot/UI tests, Macrobenchmark, and Baseline Profiles.
- Respect legacy View/XML, Java, or existing architecture when the repo requires it.
- Keep platform APIs, permissions, lifecycle behavior, offline/sync behavior, and validation commands explicit.
- Avoid asking coding agents to rediscover build, architecture, or test facts this desk should settle first.

## Expected inputs

Accepted requirements, architecture brief, UI/UX brief, technical discovery memo, repo files, Gradle facts, API contracts, permissions, validation expectations, and prior `android_delivery_packet`.

## Expected outputs

App engineering plan, file/module change map, implementation constraints, validation commands, risks, halt conditions, packet update, and downstream SDLC implementation handoff when ready.

## Evidence packet additions

- target modules and files
- app implementation lane: Kotlin, Java, Compose, View/XML, hybrid, or legacy
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

- `android-app-engineering-plan.md`
- `android-app-source-facts.md`
- `android-app-validation-commands.md`
- `android-app-implementation-handoff.md`
- `workflow-halt.md`

## Downstream handoff

Use `implementation-handoff-desk` only after this desk has reduced Android-specific ambiguity. The handoff must include exact files/modules, constraints, acceptance gates, validation commands, source facts, open questions, and halt conditions.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as issue planning, implementation handoff, review quality, test strategy, verification, CI failure triage, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
