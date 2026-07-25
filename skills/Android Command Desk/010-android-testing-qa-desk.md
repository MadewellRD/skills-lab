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

**Outcome.** An Android QA strategy and evidence plan: requirement-to-test map; unit, integration, instrumented, UI, screenshot, benchmark, smoke, gameplay, Play pre-launch, and manual exploratory coverage; device and API matrix with emulator and physical coverage; local and CI validation sequence; defect triage rules; and release pass/fail gates with the evidence each requires.

**Grounding.** Work from the PRD, architecture, implementation scope, validation commands, CI status, test files, emulator and device availability, benchmark output, issue and bug history, and gameplay scope. Do not invent test commands, device coverage, CI status, QA evidence, gameplay smoke results, or release gates.

**Parallel surface.** Test cases, device and API matrix cells, locales, and app versus game surfaces are independent: design, assign, and execute across them in parallel. Two things are not parallel — the local and CI validation sequence has real ordering constraints (build before instrumented run, install before an adb-driven test), and the release pass/fail roll-up is aggregate and runs once, after the per-cell results exist.

**Acceptance bar.** The QA plan is complete when every acceptance criterion maps to at least one named test or an explicit manual check; every matrix cell states whether it is covered, uncovered, or waived with rationale; each validation command is runnable as written against the repo; defect triage rules define severity and the release-blocking threshold; and each release gate names the evidence artifact that satisfies it rather than the intent behind it.

Continue to release store ops when QA gates are explicit.

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

Proceed by default. Missing coverage is normally recorded as a named coverage gap, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — testing requires accounts, devices, paid test infrastructure, or environments the user has not authorized.
- **Production or destructive** — the plan would run tests against production services, real payment flows, or live player data.
- **Security or privacy** — tests require real credentials, personal data, or production secrets as fixtures.
- **Source conflict** — acceptance criteria, implementation scope, and existing tests genuinely disagree on expected behavior. Preserve the conflict rather than encoding one side as the assertion.
- **Release integrity** — a release gate would be reported as passed while its evidence is absent, unrunnable, or drawn from a different build than the one shipping.
- **Connector unreachable** — CI, test output, or repo test sources exist but cannot be read.

Otherwise proceed: an unavailable device or API level, an unidentified validation command, or an undefined gameplay smoke path becomes a labeled coverage gap naming the evidence needed to close it, and the plan covers what can be covered.

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
