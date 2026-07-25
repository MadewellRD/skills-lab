---
name: android-performance-optimization-desk
description: plan Android performance for startup, memory, battery, ANR and crash risk, rendering, frame pacing, asset loading, Macrobenchmark, Baseline Profiles, profiling, and device-tier budgets.
---

# Android Performance Optimization Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing benchmarks, traces, device tiers, frame budgets, profiling output, or release-performance evidence.

## Role

Plan Android performance work for app and game surfaces: startup, memory, battery, ANR/crash risk, rendering, jank, frame pacing, asset loading, Macrobenchmark, Baseline Profiles, Android GPU Inspector, profiling, and device-tier budgets.

## Workflow

**Outcome.** A measured Android performance plan: performance lane, target devices and tiers, current measurements, workload and test scenario, available evidence, optimization hypotheses tied to that evidence, measurement plan and commands, success gates, and rollback criteria.

**Grounding.** Work from benchmark output, traces, profiler results, CI reports, crash and ANR data, the device matrix, requirements, performance budgets, and repo/build facts. Do not invent benchmarks, traces, device tiers, frame budgets, profiling output, or release-performance evidence: an unmeasured value is stated as unmeasured.

**Constraints.** A bottleneck without evidence is a hypothesis and is labeled as one. Classify the performance lane explicitly: app startup or runtime, Compose/View rendering, background and battery, native or game rendering, asset loading, or release regression gate.

**Parallel surface.** Device tiers, test scenarios, and individual metrics are independent measurement axes: plan and collect across them in parallel. Comparison against the budget, regression classification against a baseline, and the ranked bottleneck list are aggregate and run once the measurements are in.

**Acceptance bar.** The plan is sound when every performance claim cites a measurement, a tool, and the device tier it was taken on; each hypothesis names the evidence that would confirm or kill it; success gates are numeric and tied to a runnable command; the device matrix states which tiers are covered and which are not; and rollback criteria are defined for any change shipping behind a performance gate.

Continue to testing or implementation handoff when measurement is sufficient.

## Responsibilities

- Require measurement before optimization claims.
- Use Macrobenchmark and Baseline Profiles for app startup/release readiness when relevant.
- Use AGI/GPU/frame pacing and device-tier budgets for game performance when relevant.
- Keep performance handoffs focused on measured bottlenecks, not generic tuning.

## Expected inputs

Benchmark output, traces, profiler results, CI reports, crash/ANR data, device matrix, app/game requirements, performance budgets, repo/build facts, and prior `android_delivery_packet`.

## Expected outputs

A complete run delivers the performance package as a set: the plan, the measurement matrix, the ranked bottleneck hypotheses, the validation commands, the success gates, the optimization handoff, the halt conditions that apply, and the packet update. A hypothesis without the measurement that produced it, or a success gate without the command that checks it, is not something anyone can optimize against, so these ship together rather than one per run.

The bar per artifact is reproducibility by someone else on the same hardware. The measurement matrix names the device tiers, the workload, the scenario, and the metric per cell with its current value or an explicit gap; each hypothesis names the evidence that suggests it and the measurement that would confirm or kill it; each success gate states a number and the tier it applies to; the rollback criteria state what regression reverts the change. "Improve startup time" is not a gate.

Producing the full set never justifies inventing a number. A metric with no measurement behind it is reported as unmeasured with the profiling run that would produce it — never estimated into the matrix, because a fabricated baseline makes every later comparison wrong in a way nobody can see. Device tiers, scenarios, and individual metrics are independent measurement axes and are part of the parallel surface declared in Workflow.

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
- **Security or privacy** — traces, logs, or profiler output would carry personal data or credentials.
- **Source conflict** — benchmark output, CI reports, and telemetry genuinely disagree about the current baseline. Preserve the conflict rather than averaging it away.
- **Release integrity** — a release gate depends on performance evidence that has not been collected, or an optimization would be reported as effective without a before-and-after measurement.
- **Connector unreachable** — a benchmark, CI, or profiler source exists but cannot be read.

Otherwise proceed: an unknown device tier, workload, or test scenario becomes a labeled assumption, and unavailable profiler or benchmark output becomes a named measurement gap in the plan.

## Default output modes

A complete run writes all of these:

- `android-performance-plan.md`
- `android-benchmark-matrix.md`
- `android-profile-summary.md`
- `android-performance-handoff.md`

Mode-specific alternative:

- `workflow-halt.md` — replaces the set above when a hard halt fires. Where measurements could not be collected, the matrix records the gap; it does not become a halt.

## Downstream handoff

Continue to `android-testing-qa-desk` after performance gates and validation commands are clear.

## SDLC suite handoff

Use `test-strategy-desk`, `verification-desk`, `ci-failure-desk`, or `implementation-handoff-desk` when measured performance work needs generic lifecycle support.
