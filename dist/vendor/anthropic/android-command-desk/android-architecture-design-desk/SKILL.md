---
name: android-architecture-design-desk
description: design Android app and game architecture, module boundaries, data flow, offline behavior, engine integration, services, APIs, migrations, and ADR-ready decisions.
---

# Android Architecture Design Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing repo architecture, runtime constraints, service contracts, migration scope, or validation facts.

## Role

Define Android architecture for app and game work: modules, layers, state, data flow, storage, networking, engine boundaries, native/plugin boundaries, background work, API contracts, migration impact, ADR decisions, and validation gates.

## Workflow

**Outcome.** An Android architecture decision set ready for ADR capture: architecture lane, module boundaries and ownership, data and state flow, threading and concurrency, storage, networking, background work, service contracts, engine/native/plugin boundaries, migration impact, rejected alternatives, risks, and validation gates.

**Grounding.** Build on accepted requirements, technical discovery facts, and the repo's current structure. Do not invent repo architecture, module ownership, runtime constraints, service contracts, migration scope, or validation facts.

**Ordered content that stays ordered.** Where the design includes an on-device data migration — a schema change, a storage-engine swap, or a save-format change — emit its steps as an ordered sequence and keep them ordered. The order is mandated by the device, not by this desk: a migration applied out of order against user data on a shipped install is irreversible and cannot be undone by a subsequent release. Do not collapse those steps into prose.

**Parallel surface.** Candidate module boundaries, individual service contracts, and per-alternative trade-off analysis are independent and can be evaluated in parallel. Lane selection, the module graph, and the ADR set are aggregate: they reconcile the parallel results and run once.

**Acceptance bar.** The architecture is done when the lane is chosen with rejected alternatives and their reasons recorded; every module boundary names its owner or marks ownership unknown; each decision is tied to a requirement or a discovery fact rather than to general Android practice; migration impact is stated or explicitly ruled out; and every validation gate is tied to source evidence.

Continue to UI/UX, app engineering, or game engineering based on target outcome.

## Responsibilities

- Ground architecture in current repo structure and Android app/game evidence.
- For app work, account for Kotlin, Compose/View, modularization, DI, data layer, offline/sync, Macrobenchmark, and Baseline Profile implications.
- For game work, account for engine/runtime boundaries, native libraries, asset delivery, frame loop, input, and profiling constraints.
- Produce ADR-ready decisions before implementation handoff.

## Expected inputs

Android PRD, discovery memo, repo facts, existing architecture docs, service contracts, design/game docs, performance/security constraints, and prior `android_delivery_packet`.

## Expected outputs

A complete run produces the full design package in one pass: the architecture brief, the ADR notes, the module and interface map, the migration plan, the risks, the validation expectations, and the packet update. They interlock — an ADR without the module map it constrains, or a migration plan without the risks that gate it, is not something an engineer can build against, so treat them as one deliverable rather than a list to choose from.

Each artifact is done when implementation could start from it. The brief names the selected lane and the alternatives that lost and why; the module map names real modules, real ownership, and the interfaces between them rather than boxes labelled by layer; the migration plan states the sequence, the reversible points, and what breaks if a step is skipped. Section headings with nothing decided underneath are a failed artifact, not a first draft.

Producing everything is not licence to design past the evidence. Where no source establishes a module boundary, a dependency direction, a concurrency constraint, or a migration dependency, mark that part blocked on the named missing fact — a convincing architecture invented to fill the gap is worse than an acknowledged hole. Independent per-boundary and per-contract work is part of the parallel surface declared in Workflow.

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
- **Production or destructive** — the design requires a data migration, storage swap, or schema change against live user data with no approved rollback path.
- **Security or privacy** — a boundary decision determines how personal data, credentials, or keys are stored or transmitted and no source establishes the requirement.
- **Source conflict** — repo structure, existing architecture docs, and stated requirements genuinely disagree on a load-bearing boundary. Preserve the conflict.
- **Release integrity** — an ADR would record a decision as accepted when no source shows it was accepted, or validation gates cannot be tied to any evidence.
- **Connector unreachable** — repo or architecture-doc access exists but cannot be read.

Otherwise proceed: an unknown API contract, runtime constraint, architecture lane, or migration scope becomes a labeled assumption in the ADR plus an open question routed to the desk that can resolve it.

## Default output modes

A complete run writes all of these:

- `android-architecture-brief.md`
- `android-adr.md`
- `android-module-map.md`
- `android-migration-plan.md`

Mode-specific alternative:

- `workflow-halt.md` — stands in place of the set above when a hard halt fires, rather than accompanying a finished design. Where no migration is in scope, say so in the brief instead of writing an empty migration plan.

Where a file has no evidential basis, it names what is missing. A design document is never padded out to fill its slot in the list.

## Downstream handoff

Continue to `android-ui-ux-desk` for screen/interaction work, `android-app-engineering-desk` for native implementation, or `android-game-engineering-desk` for game runtime work.

## SDLC suite handoff

Use `architecture-design-desk` patterns for ADRs, interface contracts, migration planning, and architectural risks while preserving Android-specific platform and runtime constraints.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
