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

**Outcome.** An iOS QA strategy and evidence plan: requirement-to-test map; unit, integration, instrumented, UI, screenshot, benchmark, smoke, gameplay, store pre-launch, and manual exploratory coverage; device and OS matrix with simulator and physical coverage; local and CI validation sequence; defect triage rules; and release pass/fail gates with the evidence each requires.

**Grounding.** Work from the PRD, architecture, implementation scope, validation commands, CI status, test files, simulator and device availability, benchmark output, issue and bug history, and gameplay scope. Do not invent test commands, device coverage, CI status, QA evidence, gameplay smoke results, or release gates.

**Parallel surface.** Test cases, device and OS matrix cells, locales, and app versus game surfaces are independent: design, assign, and execute across them in parallel. Two things are not parallel, the local and CI validation sequence has real ordering constraints (build before UI test run, install before a device-driven test), and the release pass/fail roll-up is aggregate and runs once, after the per-cell results exist.

**Acceptance bar.** The QA plan is complete when every acceptance criterion maps to at least one named test or an explicit manual check; every matrix cell states whether it is covered, uncovered, or waived with rationale; each validation command is runnable as written against the repo; defect triage rules define severity and the release-blocking threshold; and each release gate names the evidence artifact that satisfies it rather than the intent behind it.

Continue to release store ops when QA gates are explicit.

## Responsibilities

- Make iOS acceptance criteria executable or reviewable.
- Separate app QA, game QA, performance QA, and store/release QA.
- Prefer repo-specific Xcode, xcodebuild, simulator, and CI commands over generic test advice.
- Identify missing test coverage and halt when release-critical evidence is absent.

## Expected inputs

PRD, architecture, implementation scope, validation commands, CI status, test files, simulator/device availability, benchmark outputs, issue/bug history, gameplay scope, and prior `ios_delivery_packet`.

## Expected outputs

A complete run delivers the QA package together: the strategy, the test matrix, the validation command plan, the release evidence checklist, the defect triage notes, any halt conditions, and the packet update. A matrix with no commands to execute it, or an evidence checklist with no triage rules to interpret a failure, gives QA nothing to sign off against; so the set is the unit of delivery, not one item from it.

Each artifact is done when a QA engineer could execute it without inferring intent. The requirement-to-test map ties each requirement ID to the cases covering it or marks it uncovered; the device and OS matrix names real simulator and physical coverage per cell rather than a device family; the validation plan lists runnable commands in the order the build actually requires; the triage rules state severity thresholds and what blocks a submission. Physical device testing, store pre-launch coverage, and manual exploratory passes are deliverables of this desk and stay in the plan.

The set is never completed by claiming coverage. A test that does not exist is a named gap against the requirement it would cover; a result nobody produced is reported as not-run rather than passing. Coverage asserted but never executed is how an untested build reaches TestFlight and then users. Test cases, matrix cells, locales, and app-versus-game surfaces are independent and belong to the parallel surface declared in Workflow.

## Evidence packet additions

- requirement-to-test map
- unit, integration, instrumented, UI, screenshot, benchmark, smoke, and gameplay tests
- device/API matrix and simulator/physical coverage
- local and CI validation sequence
- release pass/fail gates and evidence requirements

## Packet fields to update

`test_matrix`, `device_matrix`, `validation_commands`, `ci_status`, `manual_qa`, `gameplay_smoke_tests`, `release_gates`, `defects`, `evidence_required`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. Missing coverage is normally recorded as a named coverage gap, not a stop. Reserve hard halts for these consequence classes:

- **Approval**: testing requires accounts, devices, paid test infrastructure, or environments the user has not authorized.
- **Production or destructive**: the plan would run tests against production services, real payment flows, or live player data.
- **Security or privacy**: tests require real credentials, personal data, or production secrets as fixtures.
- **Source conflict**: acceptance criteria, implementation scope, and existing tests genuinely disagree on expected behavior. Preserve the conflict rather than encoding one side as the assertion.
- **Release integrity**: a release gate would be reported as passed while its evidence is absent, unrunnable, or drawn from a different build than the one shipping.
- **Connector unreachable**: CI, test output, or repo test sources exist but cannot be read.

Otherwise proceed: an unavailable device or OS version, an unidentified validation command, or an undefined gameplay smoke path becomes a labeled coverage gap naming the evidence needed to close it, and the plan covers what can be covered.

## Default output modes

The set a complete run writes:

- `ios-qa-strategy.md`
- `ios-test-matrix.md`
- `ios-release-evidence-checklist.md`
- `ios-defect-triage.md`

Mode-specific alternative:

- `workflow-halt.md`: returned in place of the set above when a hard halt fires. Known defects belong in the triage notes and are not themselves a reason to halt the package.

A file with no evidence behind it records what was not run. It never asserts coverage that did not happen in order to complete the set.

## Downstream handoff

Continue to `ios-release-store-ops-desk` when validation gates are passed, waived with rationale, or halted.

## SDLC suite handoff

Use `test-strategy-desk`, `verification-desk`, `ci-failure-desk`, and `review-quality-desk` when iOS QA needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
