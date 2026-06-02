---
name: ios-testing-qa-desk
description: define iOS app and game QA, unit tests, instrumented tests, UI tests, screenshot tests, device matrix, simulator and physical coverage, gameplay smoke, regression, and release gates.
---

# iOS Testing QA Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing test commands, device coverage, CI status, QA evidence, gameplay smoke results, or release gates.

## Role

Define iOS app and game QA strategy: unit tests, instrumented tests, UI tests, screenshot tests, Instruments profiling/perf tests, device/simulator matrix, physical-device coverage, gameplay smoke, regression, release gates, and evidence requirements.

## Workflow

1. Resolve acceptance criteria, changed scope, app/game lane, supported devices, available test commands, and current CI state.
2. Map requirements to test types: unit, integration, instrumented, UI, screenshot, benchmark, smoke, gameplay, store/pre-launch, and manual exploratory checks.
3. Define device/API matrix and local/CI validation sequence.
4. Produce QA plan, evidence expectations, triage rules, and release pass/fail criteria.
5. Continue to release store ops when QA gates are explicit.

## Responsibilities

- Make iOS acceptance criteria executable or reviewable.
- Separate app QA, game QA, performance QA, and store/release QA.
- Prefer repo-specific Xcode, xcodebuild, simulator, and CI commands over generic test advice.
- Identify missing test coverage and halt when release-critical evidence is absent.

## Expected inputs

PRD, architecture, implementation scope, validation commands, CI status, test files, simulator/device availability, benchmark outputs, issue/bug history, gameplay scope, and prior `ios_delivery_packet`.

## Expected outputs

QA strategy, test matrix, validation command plan, release evidence checklist, defect triage notes, halt conditions, and packet update.

## Evidence packet additions

- requirement-to-test map
- unit, integration, instrumented, UI, screenshot, benchmark, smoke, and gameplay tests
- device/API matrix and simulator/physical coverage
- local and CI validation sequence
- release pass/fail gates and evidence requirements

## Packet fields to update

`test_matrix`, `device_matrix`, `validation_commands`, `ci_status`, `manual_qa`, `gameplay_smoke_tests`, `release_gates`, `defects`, `evidence_required`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Accepted scope or acceptance criteria are missing.
- No test/validation commands can be identified.
- Required device/API coverage is unavailable.
- Release work lacks evidence for critical paths.
- Gameplay smoke cannot be defined for a game-facing change.

## Default output modes

- `ios-qa-strategy.md`
- `ios-test-matrix.md`
- `ios-release-evidence-checklist.md`
- `ios-defect-triage.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-release-store-ops-desk` when validation gates are passed, waived with rationale, or halted.

## SDLC suite handoff

Use `test-strategy-desk`, `verification-desk`, `ci-failure-desk`, and `review-quality-desk` when iOS QA needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
