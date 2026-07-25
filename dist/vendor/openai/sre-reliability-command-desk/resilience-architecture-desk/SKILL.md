---
name: resilience-architecture-desk
description: design timeout and retry budgets, circuit breakers, bulkheads, load shedding and admission control, backpressure, cache and stale-serve fallbacks, idempotency and replay safety, and graceful degradation modes, and record whether each control is configured, tested, proven in an incident, or unproven. use for resilience design, failure absorption, deadline propagation, retry amplification control, and degradation mode specification.
---

# Resilience Architecture Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the resilience control set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent configured values, control placements, degradation behavior, or evidence that a control has held.

## Role

Own what absorbs the failures the dependency stage found. Each failure mode either has a control that stops it reaching the user, or it is accepted as residual risk with a named owner. This desk assigns concrete values to those controls, places them at the layer where they actually work, specifies what the user sees when the system degrades, and records how each control's state was established.

The state matters as much as the value. A control moves through four states and they are not interchangeable: designed, configured in a running system, exercised under injected or real failure, and proven in a production incident. Most reliability postmortems turn on a control that had reached state two and was believed to be at state four.

## Use when

- The failure-mode inventory exists and each mode needs a control assigned, a value chosen, or an explicit acceptance as residual risk.
- Timeouts and retries need a coherent budget across a call chain rather than per-service defaults chosen independently.
- Circuit breakers, bulkheads, load shedding, admission control, or backpressure need placing, sizing, or reviewing.
- Degradation behavior needs specifying: what a user can still do while a dependency is unavailable, and what they see.
- Retry amplification, metastable failure, or overload collapse showed up in the dependency analysis or in a real incident.
- Idempotency and replay safety need establishing before retries or a failover can be made safe.

## Do not use when

- The failure modes and coupling are not yet established: start at `dependency-failure-analysis-desk`, whose inventory is this desk's work list.
- The question is whether the control holds when the fault is actually injected: that is `chaos-resilience-testing-desk`, which promotes a control from claimed to proven or to broken.
- The question is how much capacity the system needs: that is `capacity-planning-desk`. Shedding decides what happens past the limit; capacity decides where the limit sits.
- The question is where the saturation knee is and how the system behaves past it under a real workload: that is `load-performance-testing-desk`.
- The change is a code change to implement a control: specify it here with its value and acceptance bar, then label the implementation as a cross-suite handoff to the SDLC suite.

## Required evidence

- The failure-mode inventory with coupling, propagation, and residual risk from the upstream stage, and the objective each journey carries.
- Current configuration read from source: client and server timeouts, retry counts and backoff parameters, connection and thread pool sizes, breaker thresholds and windows, queue bounds, concurrency limits, and rate limits.
- The latency distribution per dependency, because a timeout is only meaningful relative to the served distribution rather than to a round number.
- Deadline and context propagation behavior across the call chain, including whether a deadline is passed at all.
- Product decisions about acceptable degradation: what may be stale, what may be omitted, what must never be approximated, and what must fail closed rather than open.
- Cache topology, freshness semantics, and whether stale-on-error serving exists today.
- Idempotency mechanisms already in place: keys, deduplication windows, and the write paths that lack them.
- Evidence of controls behaving under stress: incident records, load test results, and chaos experiment outcomes.

## Workflow

**Outcome.** A control specification per failure mode with a concrete value, its enforcement layer, its interaction with the other controls on the same path, a stated degradation mode per journey with the user-visible behavior in each, and an evidence state per control that distinguishes designed from configured from exercised from proven.

**Grounding.** Configuration in the repository or the running system states what is set; design documents state what was intended. Where they disagree, both are recorded with attribution and the conflict is preserved per `references/suite-workflow-contract.md`. A breaker described in an architecture document and absent from the client configuration is recorded as designed, not as configured.

**Constraints.** Timeouts are derived from the observed latency distribution of the dependency and from the caller's own deadline, and they are set as a budget along the chain rather than per hop in isolation. The invariant that must hold: a callee's timeout is shorter than its caller's remaining deadline, and the deadline is propagated so work is abandoned when nobody is waiting for it. The common inversion, where a downstream timeout exceeds the upstream one, means the caller has already returned an error while the callee continues consuming capacity on a result nobody will read.

Retries are governed by a budget, not by a count. A retry budget caps retries as a fraction of total requests so amplification is bounded when a dependency degrades, which a fixed retry count cannot do because the count multiplies exactly when the dependency is weakest. Retries use exponential backoff with jitter to avoid synchronizing the herd, are attempted only on errors that are actually retryable, and are permitted only on operations that are idempotent or carry a deduplication key that survives the retry. Retry at one layer only where the chain allows it; retries at three layers compose into the product of their counts.

Circuit breakers state their error threshold, their evaluation window, their minimum request volume, and their half-open probe behavior, because a breaker that never trips and a breaker that flaps both look configured. Bulkheads isolate resources per dependency, and the isolation is verified down to the resource that actually saturates: two logical pools sharing one connection pool, one thread pool, or one event loop are one bulkhead.

Load shedding and admission control state what is shed first and what is protected, which requires request criticality to be expressed in the request itself rather than inferred; health checks, retries of already-accepted work, and control-plane traffic are named explicitly on the protected side. Backpressure is preferred over unbounded queueing: a bounded queue that rejects is recoverable, while an unbounded one converts an overload into a latency collapse that persists after load returns to normal.

Degradation modes are specified in terms of what the user can still accomplish and what they see, with the switch that activates each mode named and its activation path stated. A degradation mode with no flag, no automatic trigger, and no tested activation is a description of a capability rather than a capability. Fail-open and fail-closed are decided per control and stated explicitly, and authorization, payment, and safety paths fail closed regardless of the availability cost.

**Parallel surface.** Failure modes, dependencies, control specifications, and configuration reads are independent units and are parallel-safe; per-dependency timeout derivation, per-control configuration reads, and evidence lookups across incidents, load tests, and chaos results all fan out.

The aggregate work runs once after the fan-out returns: reconciling the timeout and deadline budget along the whole call chain, checking that controls on one path do not defeat each other, composing the degradation modes into what the user experiences when several dependencies fail together, resolving the retry budget across layers, and ranking the failure modes left with no control as residual risk.

**Acceptance bar.** Every failure mode maps to a control with a concrete value or to an explicitly accepted residual risk with an owner. Every timeout is consistent with its caller's deadline along the whole chain. Every retry path names its budget and its idempotency basis. Every degradation mode names its activation switch and the user-visible result. Every control carries an evidence state, and unproven is a permitted and common value.

## Outputs

A complete run delivers this artifact set:

- `resilience-control-specification.md`: per control, the failure mode it absorbs, the enforcement layer, the concrete value, the source of that value or the derivation behind a proposed one, and the evidence state.
- `timeout-retry-budget.md`: the end-to-end deadline budget along each journey path, the per-hop timeouts that fit inside it, deadline propagation behavior, the retry budget per edge, the backoff and jitter parameters, and the idempotency basis that makes each retry safe.
- `degradation-mode-catalog.md`: per journey, each degradation mode with its trigger, its activation switch, what the user can still do, what they see, what silently stops, what accumulates while degraded, and the exit condition.
- `resilience-evidence-register.md`: every control with its state as designed, configured, exercised, or proven, the artifact that established that state, and the date where one exists.
- `residual-risk-register.md`: failure modes with no control, controls that cannot cover the whole mode, the exposure that remains, and the owner who accepts it.
- `resilience-downstream-handoff.md`: the control claims `chaos-resilience-testing-desk` should test first, ranked by tier and by the gap between claimed and proven, plus the shed and queue behavior `capacity-planning-desk` must size against.

Depth standard per artifact: a control entry an engineer can implement or audit without a follow-up, meaning the value, the unit, the layer, and the scope are all present. A degradation entry that names the accumulating consequence, since a queue that buffers during degradation produces a recovery spike that is itself a failure mode. A timeout entry that shows its relationship to the caller's deadline rather than standing alone.

In `diagnostic` mode, when the configuration source, the latency distribution, or the incident and experiment history exists and cannot be read, the run delivers `resilience-connector-diagnostic.md` reporting reachability, what was attempted, and the access needed. Controls are proposed in that mode and every one is recorded as designed rather than configured.

This desk fails by writing a value that sounds right next to a control that is not there. A timeout of 2 seconds, a breaker at 50 percent over 30 seconds, and a retry budget of 10 percent are all defensible engineering, and written into a table they become indistinguishable from a reading of the running configuration; the artifact then circulates as an inventory of what protects the system. A responder consults it mid-incident, believes a breaker will open, and it never does. So every value is marked either as read from a named configuration source or as proposed and not yet implemented, the two are never mixed in the same column, and the evidence state is set by an artifact rather than by confidence. A control is exercised only when a load test or chaos experiment with a date says so, and proven only when an incident record shows it holding under real failure. A page of controls honestly marked designed and unproven is an accurate map of the work ahead; the same page marked configured is a false sense of protection that costs an outage to correct.

## reliability_packet fields to update

- `resilience_controls[]`: `control`, `applied_at`, `configured_value`, `evidence`.
- `failure_modes[]` updated with the mitigation and the residual risk each control leaves.
- `reliability_risks[]` for accepted residual risks and for degradation modes that cannot be activated.
- `change_controls.rollback_trigger` where a degradation mode doubles as the reversal path for a change.
- `reliability_surface` set to `resilience_design`.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: accepting a residual risk on a tier 0 or tier 1 journey, or agreeing a degradation mode that changes what the product promises users, needs the service or product owner.
- Production or destructive: the next action would change live timeout, retry, breaker, shedding, rate limit, or queue configuration, or activate a degradation mode in production.
- Security or privacy: a control would fail open on an authorization, authentication, payment, or data-handling path, or a cache fallback would serve one user's data to another under degradation.
- Source conflict: the running configuration and the design documentation disagree on a control that a journey's objective depends on, so what protects the journey is genuinely undetermined.
- Release integrity: a control would be recorded as configured, tested, or proven without an artifact establishing that state.
- Connector unreachable: the configuration repository, the running configuration, or the latency distribution needed to derive a value exists and cannot be read.

Absent load test results, missing incident evidence, and an undocumented product position on acceptable staleness are soft gaps: specify the control, mark it unproven or the degradation decision as assumed, and record it where it was used. A fail-closed decision on an authorization or payment path is never relaxed to improve an availability figure.

## Downstream handoffs

`capacity-planning-desk` needs the shed thresholds, concurrency limits, and queue bounds, because they define the ceiling capacity must be planned against. `load-performance-testing-desk` needs the control values so a test can confirm behavior at and past them. `chaos-resilience-testing-desk` needs the claimed-but-unproven controls as its experiment backlog. `alerting-quality-desk` needs the degradation triggers, since entering a degraded mode is an event worth detecting. `runbook-engineering-desk` needs the degradation activation switches as first mitigating actions. `change-safety-desk` needs the reversible controls that can serve as rollback levers. Cross-suite: implementing a control is an SDLC suite change.

## Quality bar

Timeouts that make sense as a chain rather than as a list. Retries bounded by a budget that holds when a dependency is at its worst. Breakers with thresholds someone can defend against the observed error distribution. Degradation modes a support agent could explain to a customer, with an activation path someone has used. An evidence column that is mostly honest and occasionally uncomfortable, because that is what tells the next stage where to inject the fault.
