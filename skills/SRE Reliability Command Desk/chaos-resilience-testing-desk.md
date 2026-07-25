---
name: chaos-resilience-testing-desk
description: design chaos experiments with an explicit steady-state hypothesis, choose the fault and its scope, contain blast radius with abort criteria written before injection, run game days that exercise responders and runbooks, and promote controls that fail the experiment from claimed to broken with the failure mode they leave open. use for fault injection, resilience validation, game day design, failure drills, and blast radius containment.
---

# Chaos Resilience Testing Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the experiment artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent experiment results, steady-state figures, injection outcomes, or the date an experiment ran.

## Role

Own the conversion of resilience claims into evidence. Every control the design stage recorded as configured is a hypothesis about behavior under failure; this desk states that hypothesis in terms of a measurable steady state, injects the fault that tests it, contains the blast radius, and records whether the hypothesis held, was disproved, or the run was aborted.

A control that fails its experiment is not a failed experiment. It is a discovery that the failure mode the design believed was absorbed is in fact open, made in a window the team chose rather than at three in the morning during a real dependency outage. Promoting that control from claimed to broken, with the failure mode it leaves exposed, is the primary product of this desk.

## Use when

- Resilience controls exist with a configured value and an unproven evidence state, and the claim needs testing.
- A failure mode from the dependency analysis has a mitigation nobody has ever seen operate.
- A game day is being planned to exercise responders, runbooks, escalation, and communication rather than only the system.
- A recovery capability, a degradation mode, or a failover path is about to be relied on and has never been exercised.
- An incident revealed a control that did not behave as documented, and the fix needs proving rather than assuming.
- A new region, dependency, or major change is entering production and its failure behavior is unknown.

## Do not use when

- The failure modes and the controls that claim to absorb them are not established: start at `dependency-failure-analysis-desk` and `resilience-architecture-desk`.
- The question is behavior under volume rather than under fault: that is `load-performance-testing-desk`.
- The exercise is a full recovery or regional evacuation drill with RTO and RPO measurement: that is `disaster-recovery-desk`, which owns the recovery exercise; this desk owns component-level fault injection.
- The exercise is a restore drill for a dataset: that is `backup-restore-desk`.
- A real incident is in progress: injection stops and the work belongs to `incident-command-desk`.

## Required evidence

- The failure-mode inventory with propagation and detection state, and the control set with its evidence state, from the upstream stages.
- The steady-state signal for the journey in question: the indicator, its query, its normal range, and its variance, since a hypothesis cannot be stated against a metric whose normal behavior nobody has characterized.
- The injection capability actually available: fault injection tooling, service mesh fault rules, network controls, instance termination, resource pressure tooling, and the environments each one can reach.
- The abort and restoration path for each fault, including whether it can be reversed without a deploy and how long reversal takes.
- Approval boundaries and the change or freeze policy in force, plus the traffic and business calendar so the window avoids a peak or a launch.
- Runbooks, alert routing, and on-call state, because a game day exercises those as much as it exercises the system.
- Prior experiment results with their dates and outcomes, and incidents that already answered a hypothesis without a planned experiment.

## Workflow

**Outcome.** An experiment set with a steady-state hypothesis per experiment, the fault and its scope, a blast radius containment plan with abort criteria written before injection, a game day design with roles and the runbooks it exercises, results recorded as held, disproved, or aborted, and the control evidence state updated in both directions.

**Grounding.** Steady state comes from the indicator's query with its normal range observed rather than assumed; results come from the observed signal during a dated run, not from what was expected to happen, per `references/suite-workflow-contract.md`. An experiment whose fault did not verifiably land produces no result at all.

**Constraints.** State the hypothesis on the user-facing steady state, not on the system's internal signal. "Journey success rate stays within its normal band while one dependency returns errors for 10 percent of calls" is a hypothesis; "the circuit breaker opens" is an implementation detail that can be true while the user experience still fails. Include the expected magnitude and duration of any acceptable deviation, so a marginal result is not argued about afterwards.

Scope the fault to the smallest blast radius that can still disprove the hypothesis, and state the scope in the terms the system actually enforces: one instance, one zone, a percentage of traffic, a single tenant, a canary cohort, or a non-production environment with its fidelity gap stated. A fault scoped too small proves nothing; a fault scoped to the whole fleet is an outage the team caused deliberately.

Write the abort criteria and the kill switch before the injection, with the signal, the threshold, and who may call the abort. The abort path is confirmed reachable and reversible in the intended time before the fault is introduced, because an experiment whose reversal depends on a deploy pipeline has a recovery time measured in that pipeline's duration rather than in seconds.

Injecting a fault into a live system is a production-affecting action, and this sequence is mandated because each step is the only evidence that the next one is survivable and step 5 has real user impact that cannot be undone:

1. Obtain the named approval for the blast radius and confirm the change and freeze policy permits the window.
2. Confirm the abort path and kill switch work now, from the environment the operator will use, and time the reversal.
3. Establish and record the steady state from the indicator's query, so the comparison has a before.
4. Notify the on-call rotation, dependent service owners, and anyone whose alerting will fire, so a real incident during the window is not mistaken for the experiment.
5. Inject at the agreed scope, observe against the abort criteria, and abort on the criteria rather than on judgment.
6. Restore, confirm the steady state returned by the same query, and record the result including a hypothesis that was disproved.

Do not compress these steps to save a window, and do not reorder them if a future edit makes step 2 look redundant, because an unverified kill switch is how a bounded experiment becomes an unbounded incident.

Game days extend the experiment to the humans: the alert that should fire, the runbook that should be found, the escalation that should resolve, the communication that should go out, and the handoff that should happen. Assign roles and observers, and treat a responder failing to find a runbook as a first-class result rather than as a coaching note.

**Parallel surface.** Experiment design per failure mode, hypothesis drafting, tooling capability checks, and prior-result collection are independent units and are parallel-safe.

Execution is not parallel. Concurrent injections in overlapping blast radii produce a compound failure nobody can attribute, and the abort decision becomes ambiguous when two faults are live. One experiment runs at a time within a shared blast radius, and the aggregate work runs once after the fan-out returns: ranking experiments by the tier and exposure of the control they test, sequencing them so an earlier disproof cancels a later experiment that depended on it, and reconciling results into the control evidence register.

**Acceptance bar.** Every experiment names a steady-state hypothesis with a query and a normal range. Every experiment states its scope, its abort criteria, and its kill switch before injection. Every result records whether the fault verifiably landed. Every disproved hypothesis produces a control state change and an open failure mode with an owner. No control is marked proven by an experiment that did not exercise it.

## Outputs

A complete run delivers this artifact set:

- `chaos-experiment-design.md`: per experiment, the hypothesis with its steady-state query and normal band, the control under test, the fault and its parameters, the scope, the environment with its fidelity gap, and the expected result if the control holds.
- `blast-radius-and-abort-plan.md`: per experiment, the containment scope and how it is enforced, the abort signal and threshold, who may abort, the kill switch and its confirmed reversal time, the notification list, and the window constraints.
- `game-day-plan.md`: the scenario, the roles and observers, the runbooks and alerts under test, the injects and their timing, the communication path exercised, and the debrief structure.
- `chaos-experiment-results.md`: per run, the date, the scope, whether the fault landed and how that was confirmed, the observed steady state against the hypothesis, whether it held, was disproved, or aborted, and the unexpected behavior observed alongside the hypothesis.
- `disproved-control-register.md`: every control demoted from claimed to broken, the failure mode it leaves open, the user-visible exposure, the owner, and whether an interim mitigation exists.
- `chaos-downstream-handoff.md`: the recovery capabilities `disaster-recovery-desk` should exercise next, the detection gaps `alerting-quality-desk` inherits from faults that produced no page, and the runbook corrections for `runbook-engineering-desk`.

Depth standard per artifact: an experiment design another engineer could execute without asking what "degraded" means, which requires the band and the duration. A result entry that records the surprises alongside the hypothesis, since the incidental observation (an alert that did not fire, a dashboard that broke, a runbook link that 404s) is frequently worth more than the answer to the stated question. A disproved-control entry that states the exposure in user terms rather than as a failed test case.

In `diagnostic` mode, when the steady-state query, the injection tooling, or the prior result store exists and cannot be read, the run delivers `chaos-connector-diagnostic.md` reporting reachability, what was attempted, and the access needed. No experiment is designed against a steady state that cannot be observed, because the experiment would be unreadable even if it ran.

The characteristic false positive in this domain is the experiment where nothing actually broke. An injection rule that targeted a service no longer on the path, a fault applied to a replica receiving no traffic, a percentage rule that matched no requests, or a tool that reported success while silently failing to attach all produce a clean steady state and a hypothesis that appears confirmed. The control is then marked proven, the failure mode is closed, and the organization has bought confidence with an experiment that tested nothing. So every result records the evidence that the fault landed, taken from the target's own telemetry rather than from the injection tool's return code: the errors, the added latency, the terminated instance, the dropped connections. An experiment that cannot demonstrate its fault landed is recorded as inconclusive and rerun, never as held. Nothing here is written before the run: a result, a date, or a steady-state figure that anticipates the outcome is worse than no experiment, because an untested control is at least known to be untested.

## reliability_packet fields to update

- `chaos_experiments[]`: `hypothesis`, `fault`, `scope`, `abort_criteria`, `result`, `date`.
- `resilience_controls[]` evidence advanced to exercised or demoted where an experiment disproved the claim.
- `failure_modes[]` updated with detection results, including modes that produced no alert during injection.
- `reliability_risks[]` for disproved controls and the exposure they leave.
- `runbooks[]` gaps recorded where a game day exposed a missing, stale, or unusable procedure.
- `reliability_surface` set to `chaos`.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: injecting any fault into production or a shared environment, or running a game day that pages a rotation, requires the named owner of the affected system and confirmation that the change or freeze policy permits it.
- Production or destructive: the next action would terminate instances, partition networks, exhaust resources, fail over, or degrade a live dependency, and the abort path has not been confirmed reachable and reversible.
- Security or privacy: the fault would disable an authorization, authentication, audit, or data-protection control, or the experiment would expose customer data during degradation.
- Source conflict: the control documentation and a prior experiment or incident disagree on whether a control holds, so the exposure is genuinely undetermined and the experiment scope depends on which is true.
- Release integrity: a control would be recorded as proven, or a failure mode closed, without an experiment whose fault verifiably landed.
- Connector unreachable: the steady-state query, the injection tooling, or the observability needed to judge the hypothesis exists and cannot be read, which means an injection could not be evaluated or safely aborted.

Absent prior experiment history, a low-fidelity environment, and an unmeasured normal band are soft gaps: reduce the scope, state the fidelity limit, and record the assumption where it was used. Approval, the confirmed abort path, and the requirement that a fault landed are never relaxed to fit an experiment into a window.

## Downstream handoffs

`disaster-recovery-desk` needs the results for failover and dependency-loss experiments, since those are the components of a recovery claim. `alerting-quality-desk` needs every injected fault that produced no page, which is a detection gap with proof. `runbook-engineering-desk` needs the game day findings about procedures that were missing, stale, or unusable under pressure. `resilience-architecture-desk` needs the disproved controls to revisit values and placement. `production-readiness-review-desk` needs the experiment record as the evidence behind the chaos gate. `oncall-escalation-desk` needs the escalation and communication behavior the game day exercised. Cross-suite: fixing a broken control is an SDLC suite change.

## Quality bar

Hypotheses stated on what users experience, with a band and a duration. Blast radius small enough that a disproof is a finding rather than an outage, and large enough that a confirmation means something. Abort criteria written down before anyone touches the system, with a kill switch someone has just used. Results that record the surprises, and a disproved-control register that grows, because a chaos program producing only confirmations is testing the controls that were never in doubt.
