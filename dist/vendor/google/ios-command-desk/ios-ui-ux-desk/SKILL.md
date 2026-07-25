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

**Outcome.** An implementation-ready iOS UI/UX scope: screen and flow inventory, navigation model, UI framework lane, UI state matrix, input modes and supported device classes, accessibility and localization gates, and the design-source facts and gaps behind them.

**Grounding.** Work from requirements, architecture, design files, screenshots, game design docs, existing UI code, and navigation files. Do not invent screens, flows, design sources, input models, accessibility targets, or localization requirements: label an assumption as an assumption and name the design artifact that would settle it.

**Coverage constraint.** Every screen carries its full state set — loading, empty, success, error, offline, permission denied, purchase failure, save conflict, and gameplay pause/resume where applicable. Choose the implementation-facing UI lane explicitly: SwiftUI, UIKit, hybrid, engine UI, native overlay, or store/listing asset workflow.

**Permission request flows stay ordered.** Where a screen or flow requests an iOS permission, emit the request sequence as ordered steps and keep it ordered: the Info.plist usage-description string must exist before the API call, the in-context rationale precedes the system prompt, the prompt precedes the protected call, and a defined denied path follows. iOS itself enforces this ordering — an app calling a protected API without its usage-description string is terminated, and the system permission alert is shown only once, after which the user must change the setting in Settings. Getting the order wrong is not recoverable in-session.

**Parallel surface.** Screens, user flows, device classes, and locales are independent items: build the state matrix, accessibility annotations, and localization notes across them in parallel rather than walking screen by screen. The navigation model and the UI framework lane are aggregate decisions that reconcile the per-screen results and are made once.

**Acceptance bar.** UI scope is implementation-ready when every screen in the inventory has a complete state row; accessibility and localization gates are stated as checkable conditions rather than aspirations; the UI lane is chosen and justified against repo evidence; input modes are enumerated for each supported device class; and every gap in design source is named alongside the artifact that would close it.

Continue to app or game engineering when UI scope is implementation-ready.

## Responsibilities

- Turn product and architecture facts into screen and interaction contracts.
- Make iOS accessibility, localization, adaptive layouts, and input modes testable.
- Separate app UI concerns from game HUD, menus, overlays, controller, keyboard, touch, and TV input concerns.
- Avoid inventing design source; label assumptions and halt when design facts are launch-critical.

## Expected inputs

Requirements, architecture, design files, screenshots, game design docs, existing UI code, navigation files, accessibility targets, localization scope, and prior `ios_delivery_packet`.

## Expected outputs

A complete run hands over the UI/UX scope in full: screen and flow inventory, UI state matrix, navigation notes, accessibility and localization gates, input requirements, risks, any halt conditions, and the packet update. Delivering the matrix without the navigation model, or the accessibility gates without the screens they attach to, leaves a SwiftUI or UIKit engineer unable to start — the package is the deliverable.

The depth bar: an engineer builds from it without asking what a state means. Every screen carries its real states — loading, empty, error, offline, permission-denied, and whatever content states exist — not just a name in a row; every accessibility and localization gate states the concrete requirement, including Dynamic Type, VoiceOver, and right-to-left behaviour where they apply, and how each is judged; every input requirement names the device classes and interaction modes it covers. An outline is not a scope.

None of this authorizes inventing design intent. A screen, flow, locale, or state that no design source, spec, or product decision establishes is logged as an open design gap with the owner who can decide it, rather than filled with something that looks like a reasonable screen. Screens, flows, device classes, and locales are independent and are part of the parallel surface declared in Workflow.

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

- **Approval** — a brand, Human Interface Guidelines, design-system, or accessibility-target decision requires a human owner to authorize it.
- **Production or destructive** — the request would publish or overwrite store listing assets, screenshots, or live UI copy.
- **Security or privacy** — a flow would surface personal data, request a sensitive permission, or present consent or usage-description wording that no source establishes.
- **Source conflict** — design files, product requirements, and existing UI code genuinely disagree on a screen, flow, or state. Preserve the conflict.
- **Release integrity** — accessibility or localization coverage would be reported as met when no evidence supports it.
- **Connector unreachable** — a design source exists but cannot be read. A design artifact that simply does not exist yet is a soft gap.

Otherwise proceed: unresolved screens, flows, input models, accessibility targets, localization scope, or HUD/menu/controller behavior become labeled assumptions in the brief plus open questions for the design owner.

## Default output modes

The set a complete run writes:

- `ios-ui-ux-brief.md`
- `ios-screen-state-matrix.md`
- `ios-accessibility-localization-gates.md`
- `ios-ui-handoff.md`

Mode-specific alternative:

- `workflow-halt.md` — returned instead of the set above when a hard halt fires; a finished scope does not carry it.

Where nothing establishes a file's content, it records the design gap and who owns the decision rather than inventing screens to populate it.

## Downstream handoff

Continue to `ios-app-engineering-desk` for native screens or `ios-game-engineering-desk` for engine/gameplay UI.

## SDLC suite handoff

Use SDLC requirement, architecture, implementation handoff, and verification gates when UI decisions need generic lifecycle support.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
