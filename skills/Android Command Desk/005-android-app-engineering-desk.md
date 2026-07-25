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

**Outcome.** An implementation-ready native Android app scope: confirmed app rather than game-runtime lane, exact target modules and files, expected changes, implementation constraints, platform APIs and permissions, data/state/storage/networking decisions, validation commands, acceptance gates, and forbidden scope.

**Grounding.** Resolve accepted requirements, architecture, target repo and branch, modules, UI framework, platform APIs, dependencies, permissions, and validation commands from source. Build the source-fact map from Gradle files, manifests, source modules, CI, tests, and existing architecture conventions. Do not invent repo state, Android target versions, module ownership, package names, permissions, validation commands, or release targets.

**Constraints.** Express scope as boundaries, exact files and modules, expected changes, and what must not be touched. Every permission in scope names the code path that requires it.

**Parallel surface.** Target modules and files are independent units of scope: map changes, constraints, and validation per module in parallel. Cross-module contracts, the shared dependency and permission set, and the forbidden-scope boundary are aggregate and settle once, after the per-module maps exist.

**Acceptance bar.** The plan is ready to hand off when every change is anchored to a module or file path that exists in the repo; each acceptance gate has a validation command that can actually be run as written; permissions and platform APIs are listed with the code path that requires them; forbidden scope is explicit so the coding agent does not widen the change; and no fact in the plan is unattributed. Hand off to SDLC implementation only when Android-specific ambiguity is low.

## Responsibilities

- Plan Kotlin/Java and Android platform implementation without broad unconstrained coding prompts.
- Prefer modern Android patterns when repo facts permit: Kotlin, Jetpack Compose, modularization, dependency injection, clean data layer, screenshot/UI tests, Macrobenchmark, and Baseline Profiles.
- Respect legacy View/XML, Java, or existing architecture when the repo requires it.
- Keep platform APIs, permissions, lifecycle behavior, offline/sync behavior, and validation commands explicit.
- Avoid asking coding agents to rediscover build, architecture, or test facts this desk should settle first.

## Expected inputs

Accepted requirements, architecture brief, UI/UX brief, technical discovery memo, repo files, Gradle facts, API contracts, permissions, validation expectations, and prior `android_delivery_packet`.

## Expected outputs

A complete run delivers the engineering scope as a set: the app engineering plan, the file and module change map, the implementation constraints, the validation commands, the risks, the halt conditions that apply, the packet update, and the downstream SDLC implementation handoff. The handoff is part of the set whenever the implementation readiness facts are present; when they are not, it is emitted as an explicit not-ready note listing exactly which facts are missing, rather than silently omitted or padded out.

Depth is judged by whether a coding agent could start without a clarifying round trip. The change map names real modules and file paths with the expected change per file, not a module list; the constraints state what must not change as well as what must; every validation command is runnable against this repo as written. A plan that describes the work in the abstract has not met the bar.

Producing the full set is not permission to invent the repo. A module, file path, API, permission, or command that no source establishes is recorded as unknown with the discovery step that would resolve it, never guessed into a change map, where a wrong path costs an agent a whole run. Per-module scoping is independent work and belongs to the parallel surface declared in Workflow.

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

Proceed by default. A missing implementation detail is normally a labeled assumption plus a named source, not a stop. Reserve hard halts for these consequence classes:

- **Approval**: the change requires authorization to act on a repo, branch, or release surface the user has not granted.
- **Production or destructive**: the plan would modify a shared branch, delete code, migrate on-device user data, or alter signing or release configuration.
- **Security or privacy**: implementation requires handling secrets, credentials, or personal data without safe instructions, or adds a permission whose justification no source establishes.
- **Source conflict**: requirements, architecture, and repo state genuinely disagree on target module, ownership, or intended behavior. Preserve the conflict.
- **Release integrity**: the handoff would declare work implementable and validated when no validation command exists for it.
- **Connector unreachable**: repo or branch access exists but cannot be read.

Otherwise proceed: an unclear platform API, lifecycle behavior, backend dependency, policy detail, or file scope becomes a labeled assumption in the plan plus an open question, and the scope boundary is tightened rather than the work stopped.

## Default output modes

A complete run writes all of these:

- `android-app-engineering-plan.md`
- `android-app-source-facts.md`
- `android-app-validation-commands.md`
- `android-app-implementation-handoff.md`

Mode-specific alternative:

- `workflow-halt.md`: produced instead of the set above when a hard halt fires, not appended to it.

If a file has no source basis, it says so and names the discovery step that would close it. An invented change map costs more than a missing one.

## Downstream handoff

Use `implementation-handoff-desk` only after this desk has reduced Android-specific ambiguity. The handoff must include exact files/modules, constraints, acceptance gates, validation commands, source facts, open questions, and halt conditions.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as issue planning, implementation handoff, review quality, test strategy, verification, CI failure triage, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.
