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

1. Resolve performance goal, target devices, current measurements, workload, and validation commands.
2. Classify performance lane: app startup/runtime, SwiftUI/UIKit rendering, background/battery, native/game rendering, asset loading, or release regression gate.
3. Identify available evidence: benchmark reports, traces, CI results, main-thread stalls/crashes, profiler output, telemetry, or user-observed symptoms.
4. Define optimization hypotheses, measurement plan, device matrix, success gates, and rollback criteria.
5. Continue to testing or implementation handoff when measurement is sufficient.

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

- No performance target or current measurement exists for optimization claims.
- Device tier, workload, or test scenario is unknown.
- Required profiler/benchmark output is unavailable.
- Release gate depends on performance evidence that has not been collected.

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

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
