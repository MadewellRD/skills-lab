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

A complete run delivers the QA package together: the strategy, the test matrix, the validation command plan, the release evidence checklist, the defect triage notes, the halt conditions that apply, and the packet update. A matrix without the commands that execute it, or a release evidence checklist without the triage rules that decide what a failure means, leaves QA unable to sign anything — so the set is the unit of work, not a choice of one.

Each artifact is done when a QA engineer could run it without interpreting intent. The requirement-to-test map connects each requirement ID to the specific cases that cover it or marks it uncovered; the device and API matrix names real emulator and physical coverage per cell rather than a device family; the validation plan states runnable commands in the order the build system actually requires; the triage rules state severity thresholds and what blocks a release. Device testing, Play pre-launch coverage, and manual exploratory passes are deliverables of this desk and stay in the plan.

The set never gets completed by inventing coverage. A test that does not exist is listed as a gap with the requirement it would cover; a result nobody produced is reported as not-run, not as passing. Claiming coverage that was never executed is how an untested build reaches a staged rollout. Test cases, matrix cells, locales, and app-versus-game surfaces are independent and belong to the parallel surface declared in Workflow.

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

A complete run writes all of these:

- `android-qa-strategy.md`
- `android-test-matrix.md`
- `android-release-evidence-checklist.md`
- `android-defect-triage.md`

Mode-specific alternative:

- `workflow-halt.md` — issued instead of the set above when a hard halt fires. Known defects go in the triage notes; they are not a reason to halt the QA package.

A file with no evidence behind it records what was not run. It never presents coverage that does not exist in order to complete the set.

## Downstream handoff

Continue to `android-release-store-ops-desk` when validation gates are passed, waived with rationale, or halted.

## SDLC suite handoff

Use `test-strategy-desk`, `verification-desk`, `ci-failure-desk`, and `review-quality-desk` when Android QA needs generic lifecycle support.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
