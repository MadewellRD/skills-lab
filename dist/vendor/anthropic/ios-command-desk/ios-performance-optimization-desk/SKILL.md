---
name: ios-performance-optimization-desk
description: plan iOS performance for startup, memory, battery, main-thread stall and crash risk, rendering, frame pacing, Metal, and thermal behavior, asset loading, Instruments profiling, MetricKit and launch/runtime profiling, profiling, and device-tier budgets.
---

# iOS Performance Optimization Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing benchmarks, traces, device tiers, frame budgets, profiling output, or release-performance evidence.

## Role

Plan iOS performance work for app and game surfaces: startup, memory, battery, main-thread stall/crash risk, rendering, jank, frame pacing, Metal, and thermal behavior, asset loading, Instruments profiling, MetricKit and launch/runtime profiling, iOS GPU Inspector, profiling, and device-tier budgets.

## Workflow

**Outcome.** A measured iOS performance plan: performance lane, target devices and tiers, current measurements, workload and test scenario, available evidence, optimization hypotheses tied to that evidence, measurement plan and commands, success gates, and rollback criteria.

**Grounding.** Work from benchmark output, traces, Instruments and profiler results, CI reports, crash and main-thread-stall data, MetricKit payloads, the device matrix, requirements, performance budgets, and repo/build facts. Do not invent benchmarks, traces, device tiers, frame budgets, thermal behavior, profiling output, or release-performance evidence: an unmeasured value is stated as unmeasured.

**Constraints.** A bottleneck without evidence is a hypothesis and is labeled as one. Classify the performance lane explicitly: app startup or runtime, SwiftUI/UIKit rendering, background and battery, native or game rendering, asset loading, or release regression gate.

**Parallel surface.** Device tiers, test scenarios, and individual metrics are independent measurement axes: plan and collect across them in parallel. Comparison against the budget, regression classification against a baseline, and the ranked bottleneck list are aggregate and run once the measurements are in.

**Acceptance bar.** The plan is sound when every performance claim cites a measurement, a tool, and the device tier it was taken on; each hypothesis names the evidence that would confirm or kill it; success gates are numeric and tied to a runnable command; the device matrix states which tiers are covered and which are not; and rollback criteria are defined for any change shipping behind a performance gate.

Continue to testing or implementation handoff when measurement is sufficient.

## Responsibilities

- Require measurement before optimization claims.
- Use Instruments profiling and MetricKit and launch/runtime profiling for app startup/release readiness when relevant.
- Use Instruments/GPU/frame pacing, Metal, and thermal behavior and device-tier budgets for game performance when relevant.
- Keep performance handoffs focused on measured bottlenecks, not generic tuning.

## Expected inputs

Benchmark output, traces, profiler results, CI reports, crash/main-thread stall data, device matrix, app/game requirements, performance budgets, repo/build facts, and prior `ios_delivery_packet`.

## Expected outputs

Performance plan, measurement matrix, bottleneck hypotheses, validation commands, success gates, optimization handoff, halt conditions, and packet update.

## Evidence packet additions

- performance lane and workload
- device tiers and current measurements
- benchmark/profiling commands
- app startup/runtime or game frame budget
- success gates and rollback criteria
- optimization hypotheses tied to evidence

## Packet fields to update

`performance_budgets`, `benchmark_commands`, `profiling_tools`, `device_tiers`, `baseline_profiles`, `frame_budget`, `battery_constraints`, `bottlenecks`, `validation_commands`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. Absent measurement is normally recorded as a measurement gap plus the command that would close it, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — profiling or benchmarking requires running against a device, account, or environment the user has not authorized.
- **Production or destructive** — the work would profile against production traffic or real user data, or ship a change behind a performance gate with no rollback path.
- **Security or privacy** — traces, logs, MetricKit payloads, or profiler output would carry personal data or credentials.
- **Source conflict** — benchmark output, CI reports, and telemetry genuinely disagree about the current baseline. Preserve the conflict rather than averaging it away.
- **Release integrity** — a release gate depends on performance evidence that has not been collected, or an optimization would be reported as effective without a before-and-after measurement.
- **Connector unreachable** — a benchmark, CI, or profiler source exists but cannot be read.

Otherwise proceed: an unknown device tier, workload, or test scenario becomes a labeled assumption, and unavailable profiler or benchmark output becomes a named measurement gap in the plan.

## Default output modes

- `ios-performance-plan.md`
- `ios-benchmark-matrix.md`
- `ios-profile-summary.md`
- `ios-performance-handoff.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-testing-qa-desk` after performance gates and validation commands are clear.

## SDLC suite handoff

Use `test-strategy-desk`, `verification-desk`, `ci-failure-desk`, or `implementation-handoff-desk` when measured performance work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
