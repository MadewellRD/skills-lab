---
name: ios-ui-ux-desk
description: plan iOS UI/UX, Human Interface Guidelines, navigation, responsive layouts, accessibility, input modes, localization, onboarding, and app or game interaction states.
---

# iOS UI UX Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing screens, flows, design sources, input models, accessibility targets, or localization requirements.

## Role

Plan iOS UI/UX for native apps and games: navigation, screen states, SwiftUI/UIKit strategy, Human Interface Guidelines alignment, responsive layouts, accessibility, gestures, controller/input support, localization, onboarding, empty/error/loading states, and gameplay HUD/menu flows.

## Workflow

1. Resolve target screens, user flows, navigation model, input model, and design source.
2. Map UI states: loading, empty, success, error, offline, permission denied, purchase failure, save conflict, and gameplay pause/resume where applicable.
3. Choose implementation-facing UI lane: Compose, UIKit, hybrid, engine UI, native overlay, or store/listing asset workflow.
4. Define accessibility, localization, adaptive layout, and device-class gates.
5. Continue to app or game engineering when UI scope is implementation-ready.

## Responsibilities

- Turn product and architecture facts into screen and interaction contracts.
- Make iOS accessibility, localization, adaptive layouts, and input modes testable.
- Separate app UI concerns from game HUD, menus, overlays, controller, keyboard, touch, and TV input concerns.
- Avoid inventing design source; label assumptions and halt when design facts are launch-critical.

## Expected inputs

Requirements, architecture, design files, screenshots, game design docs, existing UI code, navigation files, accessibility targets, localization scope, and prior `ios_delivery_packet`.

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

- `ios-ui-ux-brief.md`
- `ios-screen-state-matrix.md`
- `ios-accessibility-localization-gates.md`
- `ios-ui-handoff.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-app-engineering-desk` for native screens or `ios-game-engineering-desk` for engine/gameplay UI.

## SDLC suite handoff

Use SDLC requirement, architecture, implementation handoff, and verification gates when UI decisions need generic lifecycle support.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
