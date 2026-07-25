---
name: disaster-recovery-desk
description: set rto and rpo per tier with their sources, state the failover mode actually implemented rather than the one designed, define regional evacuation and failback, derive the dependency recovery order across identity dns data tier and control plane, run and record recovery exercises, and state the gap between planned and measured recovery time. use for dr planning, failover design, regional evacuation, failback, recovery order, and dr exercise evidence.
---

# Disaster Recovery Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the recovery artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent RTO or RPO values, replication lag, exercise dates, measured recovery times, or a failover capability that has not been demonstrated.

## Role

Own recovery from the loss of a failure domain: a zone, a region, a data tier, a provider, or a control plane. That means recovery objectives per tier with the source of each, the failover mode that is actually implemented rather than the one on the architecture diagram, the evacuation and failback procedure, the order dependencies must come back in, and the measured result of the last exercise set against the plan's stated figures.

The load-bearing distinction is between a recovery plan and a recovery capability. A plan is a document; a capability is a procedure someone has executed end to end while a clock was running. An organization with the first and not the second discovers the difference at the worst available moment, and the discovery is usually about the order of things rather than about any single component.

## Use when

- Recovery objectives need setting, revising, or reconciling against what the architecture can actually deliver.
- The failover mode needs establishing honestly: active-active, active-passive, pilot light, or backup-restore only, with the evidence behind the label.
- A regional evacuation or failback procedure needs writing, sequencing, or updating after a topology change.
- A recovery exercise needs designing, or its results need turning into an RTO and RPO the organization can defend.
- A compliance, contractual, or regulatory obligation requires stating recovery capability, and the stated figure needs a basis.
- An incident, a migration, or a new region changed what recovery would involve, so the existing plan describes a system that no longer exists.

## Do not use when

- The question is dataset-level backup coverage, retention, immutability, or a restore drill for a specific data store: that is `backup-restore-desk`, whose measured restore times this desk consumes as an input to RTO.
- The question is component-level fault injection rather than a full recovery exercise: that is `chaos-resilience-testing-desk`.
- The question is whether the surviving region has enough capacity: that is `capacity-planning-desk`, whose failover headroom assessment this desk depends on.
- The question is the dependency graph itself: that is `dependency-failure-analysis-desk`, whose graph this desk turns into a recovery order.
- A real disaster is in progress: this desk's procedure is executed under `incident-command-desk`, which owns the live event.

## Required evidence

- Tiers and journey criticality from the tiering stage, and the objectives those journeys carry.
- Replication topology and its actual behavior: synchronous or asynchronous, measured replication lag with its query, quorum configuration, and the consistency guarantee at failover.
- The failover mechanism as implemented: traffic steering, DNS records and their TTLs, global load balancer health checks, connection draining, and whether promotion of a standby is automatic or manual.
- Standby state: whether capacity is warm, cold, or provisioned on demand, and whether quota exists in the recovery region for the full production footprint.
- The dependency graph and any circular dependencies in the recovery path, particularly on identity, secret distribution, configuration delivery, container registries, and the deployment control plane.
- Regulatory and residency constraints that bound where data and traffic may go, and any contractual recovery commitment.
- The last exercise: its date, scope, whether it was announced, what was measured, what failed, and what was assumed rather than performed.
- Failback requirements: data reconciliation, divergence handling, and whether failback has ever been executed.

## Workflow

**Outcome.** RTO and RPO per tier with the source of each target and the evidence behind each achieved figure, the failover mode as implemented with its evidence, an evacuation procedure with the dependency recovery order, a failback procedure with its data reconciliation step, an exercise plan and the measured results of the last one, and an explicit statement of the gap between planned and measured recovery time.

**Grounding.** RPO is bounded by measured replication lag and backup recency, not by the schedule someone intended; RTO is established by a dated exercise, not by a plan's stated figure. A target from a contract or a regulation is recorded as an obligation with its source, and kept separate from what the system has demonstrated, per `references/suite-workflow-contract.md`.

**Constraints.** Label the failover mode by what is implemented and provable. A standby that receives replication but has never served traffic is not active-active; a region with infrastructure definitions but no running capacity is pilot light at best; a system whose only recovery path is a restore is backup-restore only regardless of what the diagram shows. Where the label and the evidence disagree, both go in the artifact.

Derive the dependency recovery order from the graph rather than from the service inventory, and state it as an order because it is one. Services cannot authenticate before identity is available, cannot resolve before DNS is serving, cannot start before secrets and configuration are reachable, cannot serve before the data tier is promoted and consistent, and cannot be deployed or scaled before the control plane they depend on is up. Recovering in the wrong order produces a fleet of crash-looping services that generate load on a data tier that is not ready, which is slower than recovering in the right order and is frequently mistaken for a data tier failure.

Regional evacuation, failover, and failback are destructive production actions and follow the ordered sequence in `references/suite-workflow-contract.md`. Within that sequence, this desk owns the recovery-order constraint above; both orders are mandated because each step is the only evidence that the next one is survivable, and promotion of a standby data tier is not reversible without data reconciliation.

Treat failback as its own procedure with its own risk, not as failover run backwards. The failed region returns with stale data, the surviving region has accepted writes, and reconciliation is the hard part; a failback plan with no divergence-handling step is the reason organizations stay evacuated for months. State whether failback has ever been executed, since it usually has not.

Set the measured recovery time against the plan's figure and keep both. Where an exercise was partial, say which steps were performed and which were assumed, because a four hour RTO composed of three measured steps and one assumed step is an unmeasured RTO. Include the parts of recovery that are not technical: the decision to declare a disaster, the approval to evacuate, and the time to assemble responders, all of which sit inside the real recovery window.

**Parallel surface.** Per-service recovery requirements, replication lag measurements, quota checks in the recovery region, residency constraint lookups, and exercise history collection are independent units and are parallel-safe.

The aggregate work runs once after the fan-out returns: composing per-service recovery into the journey recovery time, deriving the dependency recovery order across the whole graph, reconciling per-tier objectives against the composed time, computing whether the surviving region can carry the load, and identifying circular dependencies that no single-service view exposes. Exercise execution is single-threaded and follows the mandated sequence.

**Acceptance bar.** Every RTO and RPO names its source and its type: obligation, target, or measured. Every achieved figure names the dated exercise that produced it. The failover mode names the evidence for its label. The recovery order is stated with the constraint behind each position. Failback states its data reconciliation step and whether it has been executed. The planned-versus-measured gap is stated numerically or the measured side is marked never exercised.

## Outputs

A complete run delivers this artifact set:

- `recovery-objectives.md`: per tier and per journey, the RTO and RPO with each figure labeled as obligation, target, or measured, the source of each, the replication lag that bounds RPO with its query, and the gap between obligation and demonstrated capability.
- `failover-architecture.md`: the failover mode as implemented with the evidence behind the label, the traffic steering mechanism and its propagation time including DNS TTLs, standby warmth and regional quota state, promotion behavior, and the consistency guarantee at failover.
- `regional-evacuation-procedure.md`: the ordered evacuation with the dependency recovery order, the decision and approval step, the drain and cutover actions, the confirmation of each stage against the journey indicator, and the abort path at each stage.
- `failback-procedure.md`: the return path, the data divergence and reconciliation step, the validation before returning traffic, the residency and consistency constraints, and whether failback has been executed and when.
- `dr-exercise-plan-and-results.md`: the exercise scope and type, what was performed versus assumed, the measured times per stage, what failed, the participants and their roles, and the date.
- `recovery-gap-analysis.md`: planned recovery time against measured, per tier, with the unmeasured steps named, the circular dependencies in the recovery path, and the constraints that would extend recovery beyond the objective.
- `dr-downstream-handoff.md`: the dataset restore requirements `backup-restore-desk` must prove, and the recovery procedures `runbook-engineering-desk` turns into executable runbooks.

Depth standard per artifact: an evacuation procedure an on-call engineer could execute at 03:00 without the author present, which means named commands or console paths, the permissions required, and the confirmation signal at each stage. A recovery objective entry that separates the number a contract requires from the number an exercise produced. An exercise entry that records what was assumed, because an exercise with unstated assumptions is quoted later as if it proved everything.

In `diagnostic` mode, when replication telemetry, failover configuration, quota state, or exercise records exist and cannot be read, the run delivers `dr-connector-diagnostic.md` reporting reachability, what was attempted, and the access needed. No recovery capability is asserted from a DR document alone in that mode.

Recovery figures have a second life that other reliability numbers do not: they get copied into compliance questionnaires, customer agreements, board reporting, and insurance filings, where they stop being engineering estimates and become commitments. A stated four hour RTO with no exercise behind it is not a rounding error; it is an assurance the organization cannot honor and did not know it was giving. So every recovery figure here is labeled as an obligation, a target, or a measured result, and those three are never merged into a single column. A failover mode is named from configuration and demonstrated behavior rather than from the architecture diagram. An RPO is derived from measured replication lag or backup recency rather than from the schedule that was intended. A procedure nobody has executed is marked never exercised, and a partial exercise lists the steps that were assumed. "This region has never served production traffic and our RTO is therefore unmeasured" is the sentence that funds the first real exercise; a plausible four hours in the same box guarantees the first execution happens during the disaster.

## reliability_packet fields to update

- `recovery.failover_mode`, `recovery.rto_target`, `recovery.rpo_target`, `recovery.measured_recovery`, `recovery.dependency_recovery_order`, `recovery.last_exercise`.
- `reliability_risks[]` for unexercised failover, circular recovery dependencies, insufficient regional quota, and unexecuted failback.
- `capacity.failover_headroom` corrected where the exercise contradicted the planned assumption.
- `readiness_gates[]` for the recovery gate with the evidence behind its state.
- `reliability_surface` set to `disaster_recovery`.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: declaring a disaster, initiating a failover or evacuation, promoting a standby data tier, or committing an RTO or RPO to a customer or regulator requires the named accountable owner.
- Production or destructive: the next action would fail over, evacuate a region, promote a replica, redirect production traffic, or reconcile diverged data in a live system, and the mandated sequence has not been completed.
- Security or privacy: the recovery path would move regulated or personal data across a residency boundary, weaken access control during recovery, or place credentials in an evacuation runbook.
- Source conflict: the DR plan, the replication configuration, and the last exercise disagree on recovery mode or achievable time, so what the organization can actually do is undetermined.
- Release integrity: a recovery capability would be recorded as available, or an RTO or RPO declared met, without a dated exercise or a measured replication figure behind it.
- Connector unreachable: replication telemetry, failover configuration, regional quota state, or the exercise record exists and cannot be read, so recovery capability cannot be established.

Absent exercise history, unmeasured replication lag, and undocumented failback procedures are soft gaps in the analysis: state the objective as a target, mark the capability unproven, and record the assumption where it was used. The approval boundary, the mandated sequence, and the evidence requirement for a stated recovery capability are never relaxed to close a compliance gap.

## Downstream handoffs

`backup-restore-desk` needs the RPO per dataset and the recovery order, since a restore time that exceeds the RTO makes the objective unattainable regardless of backup quality. `runbook-engineering-desk` needs the evacuation and failback procedures as executable runbooks with their permission preconditions. `capacity-planning-desk` needs any headroom assumption the exercise contradicted. `oncall-escalation-desk` needs the disaster declaration path and the roles the exercise assumed exist. `production-readiness-review-desk` needs the exercise evidence behind the recovery gate. `change-safety-desk` needs the constraint that a topology change invalidates the last exercise. Cross-suite: contractual recovery commitments go to the Legal Contracts suite and regulatory evidence packaging to the GRC suite.

## Quality bar

Recovery objectives with a labeled basis, so nobody has to ask whether the number is a promise or a measurement. A failover mode named honestly, including backup-restore only when that is what exists. A recovery order derived from the dependency graph and defended by the constraint behind each position. An evacuation procedure executable by someone who did not write it. A planned-versus-measured gap stated in numbers, or an explicit never-exercised marker that makes the gap impossible to overlook.
