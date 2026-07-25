---
name: android-ui-ux-desk
description: plan Android UI/UX, Material design, navigation, responsive layouts, accessibility, input modes, localization, onboarding, and app or game interaction states.
---

# Android UI UX Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing screens, flows, design sources, input models, accessibility targets, or localization requirements.

## Role

Plan Android UI/UX for native apps and games: navigation, screen states, Compose/View strategy, Material alignment, responsive layouts, accessibility, gestures, controller/input support, localization, onboarding, empty/error/loading states, and gameplay HUD/menu flows.

## Workflow

**Outcome.** An implementation-ready Android UI/UX scope: screen and flow inventory, navigation model, UI framework lane, UI state matrix, input modes and supported device classes, accessibility and localization gates, and the design-source facts and gaps behind them.

**Grounding.** Work from requirements, architecture, design files, screenshots, game design docs, existing UI code, and navigation files. Do not invent screens, flows, design sources, input models, accessibility targets, or localization requirements: label an assumption as an assumption and name the design artifact that would settle it.

**Coverage constraint.** Every screen carries its full state set — loading, empty, success, error, offline, permission denied, purchase failure, save conflict, and gameplay pause/resume where applicable. Choose the implementation-facing UI lane explicitly: Compose, View/XML, hybrid, engine UI, native overlay, or store/listing asset workflow.

**Permission request flows stay ordered.** Where a screen or flow requests an Android runtime permission, emit the request sequence as ordered steps and keep it ordered: rationale before request, request before the protected call, and a defined denied and permanently-denied path. Android itself enforces this ordering, and a permission the user denies twice cannot be re-requested from inside the app, so getting the order wrong is not recoverable in-session.

**Parallel surface.** Screens, user flows, device classes, and locales are independent items: build the state matrix, accessibility annotations, and localization notes across them in parallel rather than walking screen by screen. The navigation model and the UI framework lane are aggregate decisions that reconcile the per-screen results and are made once.

**Acceptance bar.** UI scope is implementation-ready when every screen in the inventory has a complete state row; accessibility and localization gates are stated as checkable conditions rather than aspirations; the UI lane is chosen and justified against repo evidence; input modes are enumerated for each supported device class; and every gap in design source is named alongside the artifact that would close it.

Continue to app or game engineering when UI scope is implementation-ready.

## Responsibilities

- Turn product and architecture facts into screen and interaction contracts.
- Make Android accessibility, localization, adaptive layouts, and input modes testable.
- Separate app UI concerns from game HUD, menus, overlays, controller, keyboard, touch, and TV input concerns.
- Avoid inventing design source; label assumptions and halt when design facts are launch-critical.

## Expected inputs

Requirements, architecture, design files, screenshots, game design docs, existing UI code, navigation files, accessibility targets, localization scope, and prior `android_delivery_packet`.

## Expected outputs

Screen/flow inventory, UI state matrix, navigation notes, accessibility/localization gates, input requirements, risks, halt conditions, and packet update.

## Evidence packet additions

- screen and flow inventory
- navigation model and UI framework lane
- UI state matrix
- input modes and supported device classes
- accessibility and localization gates
- design-source facts and gaps

## Packet fields to update

`screens`, `user_flows`, `navigation`, `ui_framework`, `design_system_requirements`, `accessibility_standard`, `localization`, `input_modes`, `ui_states`, `risks`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. A missing design detail is normally a labeled assumption plus a named gap, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — a brand, design-system, or accessibility-target decision requires a human owner to authorize it.
- **Production or destructive** — the request would publish or overwrite store listing assets, screenshots, or live UI copy.
- **Security or privacy** — a flow would surface personal data, request a sensitive runtime permission, or present consent wording that no source establishes.
- **Source conflict** — design files, product requirements, and existing UI code genuinely disagree on a screen, flow, or state. Preserve the conflict.
- **Release integrity** — accessibility or localization coverage would be reported as met when no evidence supports it.
- **Connector unreachable** — a design source exists but cannot be read. A design artifact that simply does not exist yet is a soft gap.

Otherwise proceed: unresolved screens, flows, input models, accessibility targets, localization scope, or HUD/menu/controller behavior become labeled assumptions in the brief plus open questions for the design owner.

## Default output modes

- `android-ui-ux-brief.md`
- `android-screen-state-matrix.md`
- `android-accessibility-localization-gates.md`
- `android-ui-handoff.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `android-app-engineering-desk` for native screens or `android-game-engineering-desk` for engine/gameplay UI.

## SDLC suite handoff

Use SDLC requirement, architecture, implementation handoff, and verification gates when UI decisions need generic lifecycle support.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
