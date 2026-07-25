---
name: load-performance-testing-desk
description: derive a workload model from production traffic, design load stress soak spike and breakpoint profiles with what each proves, state environment fidelity gaps and what they invalidate, measure the saturation point and the behavior past it, and define the performance regression gate that ties results back to the objective. use for load testing, stress and soak testing, capacity validation, tail latency analysis, and performance regression gating.
---

# Load Performance Testing Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the load and performance artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent test results, saturation points, latency figures, throughput numbers, or the date a test was run.

## Role

Own the empirical answer to what the system does under load, as distinct from the modeled answer the capacity stage produced. That means a workload model derived from real traffic rather than from an endpoint list, a set of test profiles each of which is asked to prove one specific thing, an honest account of how the test environment differs from production and what those differences invalidate, the measured saturation point, and the behavior past it.

The behavior past the knee is the part most often skipped and most often decisive. A system that sheds cleanly past saturation degrades; a system that queues past saturation collapses and stays collapsed after load returns to normal. Both look identical at 80 percent of capacity, which is where most testing stops.

## Use when

- A capacity model has saturation hypotheses that need measuring rather than asserting.
- A launch, campaign, migration, or seasonal peak needs validation against a workload that resembles the real one.
- Tail latency is the complaint and the latency distribution under load needs establishing at the threshold the objective uses.
- Resilience controls have concrete values and their behavior at and past those values needs observing under load.
- A performance regression gate is needed in the delivery path, or the existing gate passes changes that later degrade production.
- Soak behavior is unknown: leaks, descriptor exhaustion, disk fill from logs, connection churn, or slow degradation over days.

## Do not use when

- The demand model, binding signal, or ceilings are not established: start at `capacity-planning-desk`, whose hypotheses this desk tests.
- The question is behavior under an injected fault rather than under load: that is `chaos-resilience-testing-desk`. Load asks how much; chaos asks what if this breaks.
- The question is what value a timeout, breaker, or shed threshold should take: that is `resilience-architecture-desk`. This desk measures whether the chosen value behaves as intended.
- The question is functional correctness or a product acceptance test: cross-suite handoff to the SDLC suite's testing desks.
- The work is a code-level optimization: measure and hand the finding to the SDLC suite rather than performing the change here.

## Required evidence

- Production traffic composition: request mix by endpoint and operation, arrival rate over time including the burst shape, payload size distribution, cache hit ratio, authentication mix, tenant or cohort skew, and the read-to-write ratio.
- The saturation hypotheses, binding signals, and peak targets from the capacity stage.
- The objective and its latency threshold and measurement point from the indicator stage, so the test measures the same thing production is judged on.
- The resilience control values that the test is expected to exercise: timeouts, retry budgets, breaker thresholds, concurrency limits, shed thresholds, and queue bounds.
- The test environment's actual specification: instance types and counts, dataset size and shape, dependency posture (real, stubbed, or recorded), network path, cache state at start, and whether the CDN and edge are in the path.
- The load generator's configuration, including whether it drives an open arrival model or a closed concurrency model, and its own capacity limits.
- Prior test reports with their dates, so a result is never quoted without knowing which build it described.

## Workflow

**Outcome.** A workload model with a documented derivation from production telemetry, a profile set covering load, stress, soak, spike, and breakpoint with a stated question per profile, an environment fidelity statement naming what each gap invalidates, the measured saturation point with the signal that saturated, the observed behavior past that point, the latency distribution at and beyond the target, and a regression gate expressed against the objective.

**Grounding.** The workload model comes from production telemetry with the query and window named; the environment specification comes from the infrastructure definition rather than from what the environment was intended to be; results come from a dated run with the build or version identified, per `references/suite-workflow-contract.md`.

**Constraints.** Derive the workload from real traffic and show the derivation. A test that hits the cheapest endpoint at high rate proves the load generator works. The mix, the payload distribution, the cache hit ratio, and the tenant skew are what make the test predictive, and skew matters disproportionately because one large tenant frequently generates a traffic shape no average describes.

Drive load by arrival rate rather than by fixed concurrency wherever the production traffic is open-loop, which is almost always true for user-facing systems. A closed-loop generator cannot send more than the system can serve, so it hides saturation by slowing down alongside the system and reports a latency distribution that omits precisely the delayed requests that define the failure. State how the generator handles that omission, and check that the generator is not itself the bottleneck before any result is attributed to the system.

Give each profile a question. Load establishes behavior at expected peak; stress finds where it breaks; breakpoint ramps until the knee and records where it is; spike tests the step change with cold caches, autoscaler lag, and reconnect storms included; soak runs long enough for leaks, descriptor exhaustion, log volume, fragmentation, and slow drift to appear, which means hours to days rather than minutes. A profile without a question produces a graph nobody acts on.

Write the fidelity gaps before the results, and state what each one invalidates rather than listing them as caveats. A dataset an order of magnitude smaller than production invalidates conclusions about index and query behavior; stubbed dependencies invalidate conclusions about timeout, retry, and breaker behavior; a warm cache from a prior run invalidates spike results; a missing CDN invalidates edge and bandwidth conclusions; a single-tenant test invalidates conclusions about contention. A result whose fidelity gap invalidates it is reported as inapplicable rather than quietly used.

Measure the latency distribution at the threshold the objective uses and past it, since a mean under load is the least informative number the test can produce. Record what happens beyond saturation explicitly: whether shedding engaged and at what point, whether errors were returned quickly or requests queued, whether latency degraded proportionally or exploded, and whether the system recovered on its own when load fell back or required intervention. The last one determines whether an overload is an incident or an outage.

Testing against production or a shared environment is a production-affecting action and follows the ordered destructive-action sequence in `references/suite-workflow-contract.md` rather than being treated as an ordinary test run.

**Parallel surface.** Test scenarios, profiles, per-endpoint workload derivation, environment specification reads, and prior-report collection are independent units and are parallel-safe.

The aggregate work runs once after the fan-out returns: composing per-endpoint mixes into the journey-level workload model, reconciling results across profiles into a single saturation verdict, comparing the measured knee against the modeled one from the capacity stage, and setting the regression gate from the combined distribution rather than from one profile.

**Acceptance bar.** The workload model names its derivation source and window. Every profile states the question it answers. Fidelity gaps state what they invalidate. The saturation point names the signal that saturated and the run that measured it, or is recorded as not reached. Behavior past saturation is described from observation or marked as untested. Every result carries a date and a build. The regression gate is expressed against the objective threshold rather than against a raw number with no owner.

## Outputs

A complete run delivers this artifact set:

- `workload-model.md`: the traffic mix, arrival pattern and burst shape, payload distribution, cache hit ratio, tenant skew, and read-write ratio, each with the production query and window it was derived from, plus the simplifications made and their expected effect.
- `load-test-plan.md`: per profile, the question it answers, the ramp and duration, the target rates, the success criteria expressed against the objective, the abort criteria, and the resilience controls it is expected to exercise.
- `environment-fidelity-statement.md`: every difference between the test target and production, and for each, the specific conclusions it invalidates, ranked by how much of the plan it undermines.
- `load-test-results.md`: per run, the date, build, profile, measured throughput and latency distribution at and past target, the saturation point with the signal that bound, the errors and shedding observed, resource behavior, and the recovery behavior after load was removed.
- `saturation-and-overload-behavior.md`: the knee with its binding signal, the behavior past it, whether the system self-recovered, and the comparison against the capacity model's prediction with the discrepancy explained or left open.
- `performance-regression-gate.md`: the gated metric, its threshold tied to the objective, where the gate runs in the delivery path, the workload it runs, its sensitivity, and what a failure blocks.
- `load-testing-downstream-handoff.md`: the controls confirmed or contradicted for `chaos-resilience-testing-desk`, and the corrections `capacity-planning-desk` should apply to its model.

Depth standard per artifact: a result entry another engineer could reproduce, which means the profile, the environment, the build, and the generator configuration are all present. A saturation entry that names the resource that bound, since "it fell over at 4000 requests per second" without the binding signal gives nobody a fix. A gate entry with a threshold traceable to the objective rather than to whatever the last good run happened to produce.

In `diagnostic` mode, when production telemetry for the workload derivation, the test environment specification, or prior reports exist and cannot be read, the run delivers `load-testing-connector-diagnostic.md` reporting reachability, what was attempted, and the access needed. A workload model is not derived from an endpoint inventory alone in that mode.

The failure specific to this desk is the confident result from a test that was never run at that scale. Load numbers are unusually seductive because they come in the vocabulary of measurement (throughput, percentiles, a knee) and because a plausible saturation point can be back-computed from a capacity model in seconds. Two rules keep the record honest. First, a number appears only if a dated run produced it, with the build and profile attached, and a run that stopped at its target records the saturation point as not reached rather than estimating where it would have been. Second, a result inherits the fidelity of the environment that produced it, so a figure from a stubbed-dependency environment is never reported as system behavior, and a soak conclusion is never drawn from a run shorter than the phenomenon it was looking for. "The knee was never reached because the generator saturated first" is a real finding that leads to a better test next week; an invented knee becomes the number the capacity plan is built on and the launch is approved against.

## reliability_packet fields to update

- `load_tests[]`: `profile`, `workload_model`, `environment_fidelity`, `saturation_point`, `result`, `date`.
- `capacity.saturation_signals` and `capacity.current_headroom` corrected where measurement contradicted the model, with the correction attributed.
- `resilience_controls[]` evidence advanced to exercised for controls a dated run actually engaged.
- `failure_modes[]` extended with overload behavior the test exposed, including non-self-recovering collapse.
- `readiness_gates[]` for the load and performance gate with the evidence behind its state.
- `reliability_surface` set to `load_test`.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: running load against production, a shared environment, or a third-party dependency, or exceeding a rate a vendor agreement bounds, requires the named owner of that system.
- Production or destructive: the next action would generate load against a live system, consume shared quota, fill a production queue or datastore, or trigger real downstream side effects such as payments, messages, or provisioning.
- Security or privacy: the workload model or fixtures would carry production personal data, credentials, or payment details into a test environment or a report.
- Source conflict: the measured saturation point and the capacity model disagree materially, and adopting one silently would misstate readiness for a peak that is already scheduled.
- Release integrity: a system would be recorded as validated at a target rate, or a control declared effective under load, without a dated run establishing it.
- Connector unreachable: the production telemetry needed to derive the workload, the environment specification, or the test result store exists and cannot be read.

Absent prior test history, a low-fidelity environment, and an unmeasured cache hit ratio are soft gaps: run what the environment supports, state what the gap invalidates, and record the assumption where it was used. A result is never generalized past the fidelity of the environment that produced it in order to close a readiness gate.

## Downstream handoffs

`chaos-resilience-testing-desk` needs the confirmed control behavior and the saturation point, since injecting a fault near the knee is a different experiment from injecting one at idle. `capacity-planning-desk` needs the measured knee to correct its model and its binding-signal choice. `resilience-architecture-desk` needs the observed overload behavior to revisit shed thresholds and queue bounds. `change-safety-desk` needs the regression gate definition and its position in the delivery path. `production-readiness-review-desk` needs the dated results as the evidence behind the performance gate. Cross-suite: code-level performance fixes and gate implementation in the pipeline go to the SDLC suite.

## Quality bar

A workload a traffic engineer would recognize as their system, including the awkward tenant skew. Profiles that each answer a question someone asked. Fidelity gaps stated as invalidations rather than as apologies. A knee that was actually reached, or an honest statement that it was not and why. Behavior past saturation described from observation, because that is the part that decides whether a peak becomes an incident or an outage.
