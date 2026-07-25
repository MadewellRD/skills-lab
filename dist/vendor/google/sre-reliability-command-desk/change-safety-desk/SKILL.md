---
name: change-safety-desk
description: make production change safe through rollout strategy and staged exposure, canary analysis signals and promotion thresholds, bake time per stage, rollback triggers and whether rollback has ever actually succeeded, freeze policy and its exception path, schema and data migration safety using expand and contract, and change failure rate measured against the error budget policy.
---

# Change Safety Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the change safety artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent rollout stage percentages, canary thresholds, bake durations, rollback outcomes, freeze windows, deploy timestamps, or change failure rates.

## Role

Own the reliability of change itself. Most production incidents begin with something someone did on purpose: a deploy, a configuration push, a flag flip, a schema migration, a certificate rotation, a scaling policy edit. This desk decides how those reach users, what watches them, what reverses them, and what the organization does when the budget says stop.

Three claims get made in every rollout plan and each of them is routinely false. The first is that the change is exposed gradually, when the canary receives one percent of traffic that contains none of the affected journeys. The second is that a rollback exists, when nothing has ever been rolled back and the artifact for the previous version has expired. The third is that the canary is being analyzed, when a human glances at a dashboard for ninety seconds and clicks promote. This desk's job is to make each of those claims either true or explicitly false in writing.

Configuration and flags carry the same weight as code here. They ship faster, they skip more gates, and they cause a disproportionate share of outages precisely because nobody calls them a deploy.

## Use when

- A rollout needs stages, promotion criteria, bake time, and a rollback trigger before the first user sees the change.
- Canary analysis needs signals and thresholds rather than a person watching graphs.
- A schema change, data migration, or backfill needs sequencing so it stays reversible.
- Rollback capability itself is in question: whether the mechanism exists, whether it has ever been executed, how long it takes.
- A freeze is being proposed, contested, or exceptioned, or an error budget policy has triggered one.
- Change failure rate is the question, or a series of incidents traces to changes that all followed the process.
- Configuration and flag changes are reaching production without the controls that code changes get.

## Do not use when

- The service is not ready to receive users at all: that is `production-readiness-review-desk`, whose decision this desk implements as a rollout.
- The signal that would judge a canary does not exist: that is `sli-specification-desk`, since a canary analysis without a user-impact signal is a comparison of infrastructure metrics.
- The objective and budget policy that a freeze derives from are the actual argument: that is `slo-error-budget-desk`.
- A change has already broken production: that is `incident-command-desk`, and the rollback belongs to the incident rather than to a rollout plan.
- The work is the code change, its tests, its review, or its release mechanics: cross-suite handoff to the SDLC suite for release operations, deployment, and verification. This desk owns the reliability controls around the change, not the change.

## Required evidence

- The readiness decision and any open waivers or conditions attached to it.
- The deployment mechanism as it exists: orchestrator, rollout controller, flag system, configuration delivery path, and the artifact retention that bounds how far back a rollback can reach.
- The SLIs and burn-rate signals available to judge a rollout, with their measurement point and their latency, since a signal that lags twenty minutes cannot gate a five minute bake.
- Deploy and configuration change history with timestamps, and the incident records that correlate with them.
- Rollback history: attempts, outcomes, durations, and the changes where rollback was not possible.
- Current error budget state and the budget policy's stated consequence.
- Freeze calendar, regulated change windows, and the exception authority.
- Schema and data migration tooling, replication topology, and the readers and writers of every table or topic the migration touches.

## Workflow

**Outcome.** A rollout plan with stages that expose real journeys, canary analysis with named signals and thresholds evaluated automatically where the tooling allows, bake times matched to the failure modes they are meant to reveal, a rollback trigger and an honest account of whether rollback works, freeze policy with an exception path, migration sequencing that stays reversible, and change failure rate measured against the budget policy.

**Grounding.** Deploy history, flag audit logs, and configuration history state what actually changed and when. The metrics backend states what happened to the journey afterward. The incident tracker states which changes caused harm. Rollout documents state intent. When the plan says canary and the deploy history shows every release going to all instances within four minutes, the history is the fact and both are recorded per `references/suite-workflow-contract.md`.

**Constraints.** A canary stage that does not carry the affected journey is not a canary, so stage composition is judged by journey coverage rather than by traffic percentage. Promotion criteria are stated before the rollout begins, are expressed as signal and threshold rather than as a person's judgment, and include guardrail signals that catch harm the primary SLI misses: saturation, dependency error rate, queue depth, and cost or quota consumption where a change can exhaust one.

Bake time is set by the failure mode, not by convention. Memory leaks, connection pool exhaustion, cache poisoning, and slow data corruption do not appear in five minutes, and a plan that bakes a leak-prone change for the same duration as a stateless one has picked a number rather than a window.

Rollback is asserted only where it has a mechanism and a demonstrated execution. Where rollback is not possible, the plan says so and names the forward fix and its lead time. One-way changes are common and specific: schema drops, data backfills, message format changes already consumed by downstream systems, and any change that has written state the old version cannot read.

Schema and data migrations follow expand and contract, and this order is mandated because the contract step is irreversible and every earlier step is the evidence that it is safe:

1. Expand: add the new column, table, topic, or field, with the old one still authoritative and untouched.
2. Dual write: write both, keeping the old path authoritative for reads.
3. Backfill: migrate existing data, at a rate bounded by replication lag and lock contention, with progress and correctness measurable.
4. Dual read with the new path authoritative and the old path retained as fallback, held for a bake window long enough to surface a read path nobody knew about.
5. Stop writing the old path, and hold again.
6. Contract: drop the old column, table, or field only after the retention window that would allow recovery has passed.

Compressing steps 4 through 6 into one release is the specific mistake that turns a routine migration into data loss, because the reader nobody inventoried is discovered after the column is gone.

**Parallel surface.** Services, changes, flags, migrations, and canary signals are independent units and are parallel-safe: per-change classification, per-service rollout design, per-signal threshold derivation, per-table reader and writer inventory, and connector preflight across deploy history, flag audit log, and metrics all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: composing the promotion decision at each stage, judging blast radius across services that share a dependency the change touches, computing change failure rate over the period, and the migration sequence above. Stage promotion is sequential by definition, since the point of a stage is that the previous one has already reported.

**Acceptance bar.** Every stage names its exposure, the journeys it actually carries, its promotion signals with thresholds, and its bake duration with the failure mode that duration is chosen for. Every rollout states its rollback trigger, its rollback mechanism, and whether that mechanism has ever succeeded, with the date. Every migration plan states its reversibility per step and the point of no return. Change failure rate is stated with the window and the source, or as unmeasured.

## Outputs

A complete run delivers this artifact set:

- `change-rollout-plan.md`: stages with exposure, journey coverage, promotion signals and thresholds, bake time per stage with its rationale, the abort criteria, and the audience that sees the change first.
- `change-canary-analysis.md`: the canary and baseline definition, the signals compared with their thresholds and evaluation windows, the guardrail signals, the minimum observation volume before a verdict means anything, and the automated versus manual decision boundary.
- `change-rollback-plan.md`: the rollback trigger, the mechanism, its measured duration where one exists, the artifact and data retention that bound it, the point of no return, and the forward fix where rollback is not available.
- `change-migration-safety.md`: the expand and contract sequence for each schema or data change, the readers and writers inventoried per surface, replication and lock constraints, backfill rate limits, and the correctness signal per step.
- `change-freeze-policy.md`: the freeze conditions including budget exhaustion, the change classes exempted, the emergency path, the approval authority, and how a freeze ends.
- `change-failure-rate-report.md`: changes over the period, the share that caused user impact, time to detect and time to reverse, and the correlation with the error budget policy.
- `change-safety-downstream-handoff.md`: what `incident-command-desk` inherits, including the change surface to check first during a degradation.

Depth standard per artifact: a stage entry states the exposure and the journeys inside it, not just a percentage. A canary signal entry states the metric, the comparison, the threshold, and the window. A rollback entry states the command path and the measured duration, or states plainly that rollback has never been executed. "Monitor the canary" is not a promotion criterion.

In `diagnostic` mode, when deploy history, flag audit logs, or the metrics backend exists and cannot be read, the run delivers `change-connector-diagnostic.md` naming what was reachable, what was attempted, and the exact access required. Change failure rate is not computed in that mode, and canary thresholds are proposed as unvalidated.

The dangerous sentence in this desk is "we can roll back." It appears in nearly every rollout plan, it costs nothing to write, and it is the assumption that converts a contained regression into an extended outage when the artifact is gone, the schema has moved, or the mechanism has never been exercised. So a rollback in these artifacts is claimed only with a mechanism named and an execution dated, and is otherwise written as untested or unavailable with the forward fix beside it. The same discipline governs the two other claims that fabricate easily here: a stage is called a canary only when the journey it carries is named, and a change failure rate is a number computed from the deploy record and the incident record together, never an impression of how the last quarter felt.

## reliability_packet fields to update

- `change_controls.rollout_strategy`, `canary_analysis`, `bake_time`, `rollback_trigger`, `rollback_tested`, `freeze_policy`, and `change_failure_rate`.
- `slos[].error_budget_remaining` and `burn_rate` where the rollout consumed budget, with the window.
- `failure_modes[]` for change-induced modes such as a partially rolled fleet serving two incompatible versions, or a migration leaving a reader on a dropped surface.
- `alerts[]` where the rollout requires a temporary or permanent guardrail signal.
- `readiness_gates[]` for the change safety gate, with its state and evidence.
- `reliability_risks[]` where a one-way change is proceeding with a known irreversibility.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: promoting past a stage whose criteria were not met, overriding a freeze, or executing a change class that requires a named authorizer who has not authorized it.
- Production or destructive: the next action would deploy, promote, flip a flag, push configuration, run a migration or backfill, drop a column or table, or execute a rollback against a live system.
- Security or privacy: the change alters authentication, authorization, encryption, data residency, or retention, and its effect cannot be established from evidence; or a backfill would move personal data across a boundary that has not been cleared.
- Source conflict: the deploy history and the rollout plan disagree about how the change is actually delivered, or the schema inventory and the application code disagree about who reads a surface being dropped. Proceeding on the wrong one drops a surface that is still in use.
- Release integrity: a rollback would be recorded as available without a mechanism and an execution, a stage promoted without its criterion evaluated, or a migration declared reversible past its contract step.
- Connector unreachable: the deploy history, flag audit log, metrics backend, or schema and dependency inventory needed to plan the change exists and cannot be read.

An unmeasured historical change failure rate, unknown per-stage traffic composition, and an absent prior rollback record are soft gaps. Proceed with each named, and with the rollback recorded as untested rather than assumed. Bake time is never shortened because a release is late, the expand and contract order is never compressed, and a freeze triggered by budget exhaustion is never softened by this desk on its own authority.

## Downstream handoffs

`incident-command-desk` needs the recent change surface, the rollback trigger, and the reversible mitigation options, since the first question in most degradations is what changed. `alerting-quality-desk` receives the guardrail signals that need to become durable rules. `runbook-engineering-desk` receives the rollback and flag procedures that belong in a runbook rather than in a plan. `reliability-review-desk` receives change failure rate and budget consumption for the period. `postmortem-desk` receives the change timeline when an incident traces to a rollout. The code change, its tests, and its release mechanics hand to the SDLC suite as a labeled cross-suite handoff.

## Quality bar

A rollout where the first users to see a change are the ones chosen deliberately, where promotion answers to a threshold rather than to a schedule, where the bake time matches the failure it is watching for, and where the rollback claim is either demonstrably true or plainly labeled as untested. Migrations that can be stopped halfway without losing data, and a change failure rate that comes from records rather than recollection.
