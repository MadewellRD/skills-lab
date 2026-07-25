---
name: ios-app-engineering-desk
description: prepare iOS native app implementation plans for Swift, Objective-C, SwiftUI, View systems, modularization, storage, networking, background work, sensors, permissions, and platform APIs.
---

# iOS App Engineering Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, update the `ios_delivery_packet`, and continue to the next stage when enough source facts are available.

If required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Do not invent repo state, iOS target versions, module ownership, package names, permissions, validation commands, or release targets.

## Role

Convert iOS app requirements and architecture into implementation-ready scope for native app work, including target modules/files, Swift/Objective-C patterns, SwiftUI/UIKit choices, data layer, storage, networking, background work, sensors, permissions, validation commands, and halt conditions.

Use `references/platform/ios-app-baseline.md` for modern app defaults when the repo does not define a stronger local convention.

## Workflow

**Outcome.** An implementation-ready native iOS app scope: confirmed app rather than game-runtime lane, exact target modules and files, expected changes, implementation constraints, platform APIs and permissions, data/state/storage/networking decisions, validation commands, acceptance gates, and forbidden scope.

**Grounding.** Resolve accepted requirements, architecture, target repo and branch, modules, UI framework, platform APIs, dependencies, permissions, and validation commands from source. Build the source-fact map from Xcode project and settings files, manifests, source modules, CI, tests, and existing architecture conventions. Do not invent repo state, iOS target versions, module ownership, package names, permissions, validation commands, or release targets.

**Constraints.** Express scope as boundaries, exact files and modules, expected changes, and what must not be touched. Every permission in scope names its Info.plist usage-description string and the code path that requires it.

**Parallel surface.** Target modules and files are independent units of scope: map changes, constraints, and validation per module in parallel. Cross-module contracts, the shared dependency and permission set, and the forbidden-scope boundary are aggregate and settle once, after the per-module maps exist.

**Acceptance bar.** The plan is ready to hand off when every change is anchored to a module or file path that exists in the repo; each acceptance gate has a validation command that can actually be run as written; permissions and platform APIs are listed with the code path that requires them; forbidden scope is explicit so the coding agent does not widen the change; and no fact in the plan is unattributed. Hand off to SDLC implementation only when iOS-specific ambiguity is low.

## Responsibilities

- Plan Swift/Objective-C and iOS platform implementation without broad unconstrained coding prompts.
- Prefer modern iOS patterns when repo facts permit: Swift, SwiftUI, modularization, dependency injection, clean data layer, screenshot/UI tests, Instruments profiling, and MetricKit and launch/runtime profiling.
- Respect legacy UIKit, Objective-C, or existing architecture when the repo requires it.
- Keep platform APIs, permissions, lifecycle behavior, offline/sync behavior, and validation commands explicit.
- Avoid asking coding agents to rediscover build, architecture, or test facts this desk should settle first.

## Expected inputs

Accepted requirements, architecture brief, UI/UX brief, technical discovery memo, repo files, Xcode facts, API contracts, permissions, validation expectations, and prior `ios_delivery_packet`.

## Expected outputs

A complete run produces the engineering scope as a set: the app engineering plan, the file and module change map, the implementation constraints, the validation commands, the risks, any halt conditions, the packet update, and the downstream SDLC implementation handoff. The handoff belongs to the set whenever the implementation readiness facts are present; where they are not, it is emitted as an explicit not-ready note naming the missing facts, which is different from quietly dropping it or writing a generic one.

The bar is that a coding agent can start without a clarifying exchange. The change map gives real modules and file paths with the expected change per file rather than a list of targets; the constraints say what must not change as well as what must; every validation command runs against this project as written, with its scheme and destination. A plan that describes the work in general terms has not cleared the bar.

Producing the whole set is not licence to invent the project. A module, path, API, entitlement, permission, or command that no source establishes is recorded as unknown next to the discovery step that would settle it; a fabricated file path costs a coding agent an entire run before anyone notices. Per-module scoping is independent work inside the parallel surface declared in Workflow.

## Evidence packet additions

- target modules and files
- app implementation lane: Swift, Objective-C, Compose, UIKit, hybrid, or legacy
- platform APIs and permissions
- data/state/storage/networking decisions
- validation commands and expected evidence
- scope boundaries and forbidden changes

## Packet fields to update

`app_or_game_lane`, `modules`, `ui_framework`, `permissions`, `backend_integrations`, `api_contracts`, `validation_commands`, `acceptance_gates`, `source_facts`, `risks`, `open_questions`, `artifacts`, `ready_to_continue`

## Halt conditions

Proceed by default. A missing implementation detail is normally a labeled assumption plus a named source, not a stop. Reserve hard halts for these consequence classes:

- **Approval**: the change requires authorization to act on a repo, branch, or release surface the user has not granted.
- **Production or destructive**: the plan would modify a shared branch, delete code, migrate on-device user data, or alter signing, provisioning, or release configuration.
- **Security or privacy**: implementation requires handling secrets, credentials, Keychain material, or personal data without safe instructions, or adds a permission or required-reason API whose justification no source establishes.
- **Source conflict**: requirements, architecture, and repo state genuinely disagree on target module, ownership, or intended behavior. Preserve the conflict.
- **Release integrity**: the handoff would declare work implementable and validated when no validation command exists for it.
- **Connector unreachable**: repo or branch access exists but cannot be read.

Otherwise proceed: an unclear platform API, lifecycle behavior, backend dependency, policy detail, or file scope becomes a labeled assumption in the plan plus an open question, and the scope boundary is tightened rather than the work stopped.

## Default output modes

The set a complete run writes:

- `ios-app-engineering-plan.md`
- `ios-app-source-facts.md`
- `ios-app-validation-commands.md`
- `ios-app-implementation-handoff.md`

Mode-specific alternative:

- `workflow-halt.md`: returned in place of the set above when a hard halt fires, not added to it.

A file with no source basis states that and names the discovery step that would close it. A fabricated path is worse than an absent one.

## Downstream handoff

Use `implementation-handoff-desk` only after this desk has reduced iOS-specific ambiguity. The handoff must include exact files/modules, constraints, acceptance gates, validation commands, source facts, open questions, and halt conditions.

## SDLC suite handoff

Use the SDLC Command Desk Suite when this stage needs generic lifecycle support such as issue planning, implementation handoff, review quality, test strategy, verification, CI failure triage, release operations, deployment, observability readiness, incident response, maintenance/refactor, retrospective, or decommissioning.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
