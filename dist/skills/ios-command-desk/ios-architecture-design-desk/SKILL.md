---
name: ios-architecture-design-desk
description: design iOS app and game architecture, module boundaries, data flow, offline behavior, engine integration, services, APIs, migrations, and ADR-ready decisions.
---

# iOS Architecture Design Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing repo architecture, runtime constraints, service contracts, migration scope, or validation facts.

## Role

Define iOS architecture for app and game work: modules, layers, state, data flow, storage, networking, engine boundaries, native/plugin boundaries, background work, API contracts, migration impact, ADR decisions, and validation gates.

## Workflow

**Outcome.** An iOS architecture decision set ready for ADR capture: architecture lane, module boundaries and ownership, data and state flow, concurrency, storage, networking, background work, service contracts, engine/native/plugin boundaries, migration impact, rejected alternatives, risks, and validation gates.

**Grounding.** Build on accepted requirements, technical discovery facts, and the repo's current structure. Do not invent repo architecture, module ownership, runtime constraints, service contracts, migration scope, or validation facts.

**Ordered content that stays ordered.** Where the design includes an on-device data migration — a Core Data or SwiftData model version change, a store swap, or a save-format change — emit its steps as an ordered sequence and keep them ordered. The order is mandated by the device, not by this desk: a migration applied out of order against user data on a shipped install is irreversible and cannot be undone by a subsequent release. Do not collapse those steps into prose.

**Parallel surface.** Candidate module boundaries, individual service contracts, and per-alternative trade-off analysis are independent and can be evaluated in parallel. Lane selection, the module graph, and the ADR set are aggregate: they reconcile the parallel results and run once.

**Acceptance bar.** The architecture is done when the lane is chosen with rejected alternatives and their reasons recorded; every module boundary names its owner or marks ownership unknown; each decision is tied to a requirement or a discovery fact rather than to general iOS practice; migration impact is stated or explicitly ruled out; and every validation gate is tied to source evidence.

Continue to UI/UX, app engineering, or game engineering based on target outcome.

## Responsibilities

- Ground architecture in current repo structure and iOS app/game evidence.
- For app work, account for Swift, SwiftUI/UIKit, modularization, DI, data layer, offline/sync, Instruments profiling, and Baseline Profile implications.
- For game work, account for engine/runtime boundaries, native libraries, asset delivery, frame loop, input, and profiling constraints.
- Produce ADR-ready decisions before implementation handoff.

## Expected inputs

iOS PRD, discovery memo, repo facts, existing architecture docs, service contracts, design/game docs, performance/security constraints, and prior `ios_delivery_packet`.

## Expected outputs

One run produces the design package entire: architecture brief, ADR notes, module and interface map, migration plan, risks, validation expectations, and the packet update. These constrain each other — an ADR is only meaningful against the module map it governs, and a migration plan is only safe against the risks that gate it — so they are delivered together rather than selected between.

Each is complete when implementation could begin from it. The brief names the chosen lane and the alternatives that were rejected and why; the module map names actual modules, their owners, and the interfaces between them instead of layer-shaped boxes; the migration plan gives the sequence, the points that can still be reversed, and the consequence of skipping a step; the validation expectations say what proves the design held. Empty sections under real headings mean the artifact failed, not that it is early.

Delivering all of it does not extend permission to design beyond the evidence. Where nothing establishes a module boundary, a dependency direction, a concurrency model, or a migration constraint, that part is marked blocked on the named missing fact — a fluent architecture invented to complete the map is more expensive than an acknowledged gap, because the next desk will build on it. Candidate boundaries, service contracts, and per-alternative analysis are independent and sit in the parallel surface declared in Workflow.

## Evidence packet additions

- architecture lane and rejected alternatives
- module boundaries and ownership
- data/state flow, storage, networking, and background work
- engine/native/plugin boundaries for game work
- ADR decisions, risks, and validation gates

## Packet fields to update

`architecture_lane`, `modules`, `interfaces`, `data_flow`, `state_management`, `storage`, `networking`, `background_work`, `engine_runtime`, `migrations`, `risks`, `validation_commands`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. An unresolved design detail is normally a labeled assumption plus an open question, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — the architecture commits to a platform, vendor, or cost decision that a human owner must authorize.
- **Production or destructive** — the design requires a data migration, store swap, or schema change against live user data with no approved rollback path.
- **Security or privacy** — a boundary decision determines how personal data, credentials, or Keychain material is stored or transmitted and no source establishes the requirement.
- **Source conflict** — repo structure, existing architecture docs, and stated requirements genuinely disagree on a load-bearing boundary. Preserve the conflict.
- **Release integrity** — an ADR would record a decision as accepted when no source shows it was accepted, or validation gates cannot be tied to any evidence.
- **Connector unreachable** — repo or architecture-doc access exists but cannot be read.

Otherwise proceed: an unknown API contract, runtime constraint, architecture lane, or migration scope becomes a labeled assumption in the ADR plus an open question routed to the desk that can resolve it.

## Default output modes

The set a complete run writes:

- `ios-architecture-brief.md`
- `ios-adr.md`
- `ios-module-map.md`
- `ios-migration-plan.md`

Mode-specific alternative:

- `workflow-halt.md` — returned in place of the set above when a hard halt fires. If no migration is in scope, record that in the brief rather than shipping an empty migration plan.

A file without an evidential basis names the missing decision input instead of presenting an invented design as settled.

## Downstream handoff

Continue to `ios-ui-ux-desk` for screen/interaction work, `ios-app-engineering-desk` for native implementation, or `ios-game-engineering-desk` for game runtime work.

## SDLC suite handoff

Use `architecture-design-desk` patterns for ADRs, interface contracts, migration planning, and architectural risks while preserving iOS-specific platform and runtime constraints.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
