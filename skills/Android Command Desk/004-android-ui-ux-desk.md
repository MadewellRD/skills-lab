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

1. Resolve target screens, user flows, navigation model, input model, and design source.
2. Map UI states: loading, empty, success, error, offline, permission denied, purchase failure, save conflict, and gameplay pause/resume where applicable.
3. Choose implementation-facing UI lane: Compose, View/XML, hybrid, engine UI, native overlay, or store/listing asset workflow.
4. Define accessibility, localization, adaptive layout, and device-class gates.
5. Continue to app or game engineering when UI scope is implementation-ready.

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

- Target screens, flows, or input model are missing.
- Design source is unavailable for visual implementation.
- Accessibility or localization target is required but unknown.
- Game HUD/menu/controller behavior is required but unresolved.

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
