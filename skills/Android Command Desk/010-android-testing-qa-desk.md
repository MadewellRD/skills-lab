---
name: android-testing-qa-desk
description: define Android app and game QA, unit tests, instrumented tests, UI tests, screenshot tests, device matrix, emulator and physical coverage, gameplay smoke, regression, and release gates.
---

# Android Testing QA Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing test commands, device coverage, CI status, QA evidence, gameplay smoke results, or release gates.

## Role

Define Android app and game QA strategy: unit tests, instrumented tests, UI tests, screenshot tests, Macrobenchmark/perf tests, device/emulator matrix, physical-device coverage, gameplay smoke, regression, release gates, and evidence requirements.

## Workflow

1. Resolve acceptance criteria, changed scope, app/game lane, supported devices, available test commands, and current CI state.
2. Map requirements to test types: unit, integration, instrumented, UI, screenshot, benchmark, smoke, gameplay, store/pre-launch, and manual exploratory checks.
3. Define device/API matrix and local/CI validation sequence.
4. Produce QA plan, evidence expectations, triage rules, and release pass/fail criteria.
5. Continue to release store ops when QA gates are explicit.

## Responsibilities

- Make Android acceptance criteria executable or reviewable.
- Separate app QA, game QA, performance QA, and store/release QA.
- Prefer repo-specific Gradle, adb, emulator, and CI commands over generic test advice.
- Identify missing test coverage and halt when release-critical evidence is absent.

## Expected inputs

PRD, architecture, implementation scope, validation commands, CI status, test files, emulator/device availability, benchmark outputs, issue/bug history, gameplay scope, and prior `android_delivery_packet`.

## Expected outputs

QA strategy, test matrix, validation command plan, release evidence checklist, defect triage notes, halt conditions, and packet update.

## Evidence packet additions

- requirement-to-test map
- unit, integration, instrumented, UI, screenshot, benchmark, smoke, and gameplay tests
- device/API matrix and emulator/physical coverage
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

- `android-qa-strategy.md`
- `android-test-matrix.md`
- `android-release-evidence-checklist.md`
- `android-defect-triage.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `android-release-store-ops-desk` when validation gates are passed, waived with rationale, or halted.

## SDLC suite handoff

Use `test-strategy-desk`, `verification-desk`, `ci-failure-desk`, and `review-quality-desk` when Android QA needs generic lifecycle support.
