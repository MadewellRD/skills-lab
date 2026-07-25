---
name: batch-orchestration-desk
description: design pipeline scheduling and the dag, covering data aware triggering that waits for data rather than for a clock, sensors and arrival timeouts, retry policy and non retryable failure classes, concurrency pools and queueing at peak, sla miss conditions and notification, catch up and backfill controls with partition bounds and concurrency caps, run isolation between backfill and scheduled runs, and the failure pattern read from run history. use for airflow or dagster dag design, scheduling reviews, sla definition, retry tuning, and backfill orchestration.
---

# Batch Orchestration Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the orchestration artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a schedule, a task name, a run duration, a success rate, a pool size, or an SLA.

## Role

This desk decides when work runs, what it waits for, and what happens when it does not finish. It owns the schedule and trigger design, with a strong preference for data-aware triggering where a downstream task waits for data to exist rather than for a clock to reach a time that once worked; the dependency graph as the orchestrator actually enforces it, keeping the distinction between a task that succeeded and a task that produced data; sensors, arrival timeouts, and the behavior when a source is late; retry policy with backoff and the classes of failure that must not retry; concurrency pools and the queueing behavior at peak; the SLA definition, its miss condition, and who it notifies; catch-up and backfill controls with partition bounds and a concurrency cap; run isolation so a backfill does not contend with the scheduled run; and the failure pattern read from run history, separating chronic flakiness from real breakage.

The characteristic failure here is a fully green scheduler above stale data. Every task exited zero, the source delivered nothing, and the downstream model faithfully rebuilt yesterday's numbers.

## Use when

- A DAG is being designed or restructured and its triggers are clock-based against sources that arrive unpredictably.
- Downstream models run before their inputs land, or wait far longer than necessary because the schedule was set with padding.
- Retries are masking a failure class that should never retry, or a poison payload is being retried on a loop.
- Peak-hour contention is starving scheduled runs and nobody has defined pools or concurrency caps.
- An SLA is asserted but has no miss condition, no notification path, and no measurement.
- A backfill needs to run alongside the live schedule and the isolation and bounds have not been set.
- Run history shows a failure pattern nobody has characterized.

## Do not use when

- The subject is the transformation logic and its incremental strategy rather than when it runs. That is `transformation-layer-desk`.
- The subject is extraction mechanics, watermarks, or CDC stitching. That is `ingestion-pipeline-desk`.
- The subject is continuously running stream processing rather than scheduled batches. That is `streaming-pipeline-desk`.
- The subject is the alerting and detection design over the signals rather than the schedule producing them. That is `data-observability-desk`.
- A run has already delivered wrong data to consumers. That is `data-incident-response-desk`.

## Required evidence

- The transformation dependency graph with expected runtimes and the completeness signal each model can emit.
- Ingestion schedules and, more importantly, measured arrival times and their variability, since a source that usually arrives at two and sometimes at six needs a sensor rather than a schedule.
- The freshness targets from the data product definitions, which are what an SLA is derived from.
- Compute limits and the concurrency the platform actually supports, including any shared pool other workloads draw from.
- Orchestrator run history: durations, success rate, retry counts, failure messages grouped by class, and the queueing and start delay at peak.
- The existing schedule and catch-up configuration as deployed, read rather than assumed from the repository default.
- The classes of failure already observed, and which of them retries have historically resolved.

## Workflow

**Outcome.** An orchestration design an operator can run: triggers stated as data-aware wherever a producer signal exists, sensors with arrival timeouts and a defined late behavior, the enforced dependency graph with the completeness condition each edge actually checks, retry policy with the non-retryable classes named, concurrency pools with their sizing basis, the SLA with its miss condition and notification path, catch-up and backfill controls with partition bounds and a concurrency cap, run isolation between backfill and scheduled work, and the characterized failure pattern from run history.

**Grounding.** Read schedules, catch-up settings, pool sizes, and retry configuration from the deployed orchestrator rather than from the repository, because those diverge and only the deployed one runs. Derive arrival timeouts from measured arrival distributions rather than from the nominal cadence a source owner quotes. Characterize failures from run history grouped by message class, since a success rate without a failure taxonomy tells you a job is flaky and nothing about why.

**Constraints.** A dependency edge states what it checks, and where it checks only that an upstream task exited, that limitation is written down, because task success and data arrival are different facts and conflating them is the origin of the green-DAG-stale-data failure. Sensors specify their poll mode and their timeout, and a sensor that occupies a worker slot while waiting is sized against the pool so a late source does not deadlock the scheduler. Retry policy separates transient failures, which are worth backoff, from deterministic ones, which are not: a schema mismatch, a permission denial, a malformed payload, and out-of-bounds partition arguments retry into the same failure and consume the window that a human could have used. The SLA is defined as a miss condition on data rather than on task completion, names who is notified, and states what that person is expected to do, since a notification with no action is noise being generated on a schedule. Catch-up is configured deliberately with bounds, because enabling it on a DAG with a long history schedules hundreds of runs that saturate every pool at once. Backfills run in an isolated pool or queue so they cannot starve the scheduled run, and their partition bounds and concurrency cap follow the parallel-safety classification from the transformation stage rather than being chosen for throughput.

**Parallel surface.** Independent DAGs, independent sensor and timeout designs, independent retry-class analyses, and independent run-history extractions per pipeline fan out safely. The aggregate runs once after the fan-out returns: the pool sizing and contention judgment, which is a shared-resource decision by definition, the critical path to the freshness target across the whole graph, and the SLA rollup, because a mart is only as timely as its latest input and a per-task SLA that never composes along the chain will report every task on time while the product is late. Task execution itself follows the dependency graph and is not a fan-out surface.

**Ordered sequence for running a backfill alongside a live schedule.** This order is mandated because contention and concurrent writes to the same partition are silent, and the damage is discovered in a downstream total rather than in a failed run:

1. Bound the backfill to explicit partitions and confirm the models in scope against the parallel-safety classification, so order-dependent models are reprocessed in event-time order rather than fanned out.
2. Obtain the named approval for the blast radius the bounded set reaches, derived from lineage.
3. Isolate the backfill into its own pool or queue with a concurrency cap, so it cannot consume the slots the scheduled run depends on.
4. Pause or fence the scheduled run for the affected assets, so the two do not write the same partition concurrently and so consumers do not read a half-corrected state.
5. Run the bounded set, reconcile against a control total captured before the change, then release the fence and record the partitions processed and the variance measured.

**Acceptance bar.** An operator can tell from the artifact what each job waits for, what happens when the wait expires, which failures will not be retried, and what a miss notifies. The critical path to the freshness target is stated with its slack. Backfill controls have bounds, a cap, and an isolation mechanism. The failure characterization names classes rather than a percentage.

## Outputs

A complete run delivers this set:

- `orchestration-design.md`: the DAG structure, the trigger per entry point stated as data-aware or clock-based with the reason, and the enforced dependency edges with what each one checks.
- `sensors-and-arrival.md`: per source the expected arrival distribution with its measured basis, the sensor mode, the timeout, the late behavior, and the worker-slot cost of waiting.
- `retry-and-failure-policy.md`: retry counts and backoff per task class, the non-retryable classes named with their signatures, the escalation on exhaustion, and the alert content that lets a responder act.
- `concurrency-and-pools.md`: pool definitions with sizing basis, the queueing behavior at peak with its measured evidence, and the priority rule between scheduled runs, backfills, and ad-hoc work.
- `sla-definition.md`: the miss condition expressed against data rather than task state, its measurement point, the notification path with named recipients, and the expected response.
- `backfill-and-catchup-controls.md`: catch-up configuration, partition bounds, concurrency cap, isolation mechanism, and the ordering constraint inherited from the transformation stage.
- `run-history-analysis.md`: success rate, duration distribution and trend, failures grouped by class, the chronic-flakiness set separated from real breakage, and the tasks whose runtime is approaching their window.
- `orchestration-downstream-handoff.md`: what `data-quality-desk` inherits, including where blocking checks can halt a run and what the halt does to downstream tasks.

Depth standard: an artifact is complete when an operator could deploy the schedule and respond to its alerts without a follow-up round trip. A sensor without a timeout, or an SLA without a miss condition, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the orchestrator, its run history, or the deployed configuration cannot be read, the run delivers `orchestration-connector-diagnostic.md` naming each unreachable source and the schedule claims that depend on it. A failure pattern is not characterized from a run history nobody opened.

Anti-fabrication guard: the deceptive artifact here is the run statistic. Success rates, average durations, and retry counts are the numbers this desk trades in, and a reasonable-looking one is accepted without question because everybody expects a number in that position, then it becomes the baseline an SLA and an alert threshold are set from. So every duration, success rate, retry count, queue delay, and arrival time in the output names the run-history query and the window it covers, and where history was not read the figure is written as unmeasured rather than approximated from the schedule. Schedules, catch-up settings, pool sizes, and retry configuration are quoted from the deployed orchestrator, since a repository default that was overridden in production describes a system that does not exist. Task and DAG names come from the orchestrator, not from the naming pattern the rest of the graph follows. And a green run is never reported as data delivered: where the dependency edge checks only task state, the artifact says so, because "the pipeline succeeded" is the single most misleading true statement available in this domain.

## data_packet fields to update

- `orchestration.dependency_basis`, `schedule`, `sla_definition`, `concurrency_limits`, `retry_policy`, `backfill_controls`, and `run_history`
- `pipelines[].trigger` and `runtime` updated with the measured values and their source
- `backfills[].bounds` and `state`, with `approval` left as not obtained until an approver is named
- `data_risks[]` for clock-based triggers over variable arrivals, dependency edges that check only task state, non-retryable classes currently being retried, and tasks whose runtime is converging on their window
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a backfill or catch-up over live partitions, a schedule change that moves when a consumer receives data, or an SLA commitment made on behalf of an owner who has not agreed.
- **Production or destructive**: the next action would enable catch-up on a DAG with history, clear or re-run completed task instances, change a live schedule or pool, or start a backfill that writes partitions consumers are currently reading.
- **Security or privacy**: alert content or run logs would carry restricted values, or a notification path would route pipeline output containing personal, health, or cardholder data to recipients whose entitlement is not established.
- **Source conflict**: the deployed schedule, the repository definition, and the run history genuinely disagree about what runs and when, and assuming one silently designs against a graph that is not executing.
- **Release integrity**: an SLA, a success rate, or a backfill completion would be recorded as established without the run history, the bounds, or the reconciliation that supports it.
- **Connector unreachable**: the orchestrator, its run history, or the deployed configuration needed to characterize the schedule exists and cannot be read.

An unmeasured peak queue delay, an undecided notification channel, and an unknown future volume are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`data-quality-desk` is next and needs the points where a blocking check can halt a run, what that halt does to downstream tasks and to the consumer, and the run boundary a freshness check is evaluated against. `data-observability-desk` needs the SLA miss condition, the notification paths, and the failure taxonomy so monitors are grouped rather than fired per task. `transformation-layer-desk` receives back the runtime pressure where the critical path no longer fits the freshness target. `data-incident-response-desk` inherits the run isolation and fencing mechanism, since containment during an incident is exactly the pause this desk designed. `data-platform-cost-desk` receives the schedule frequency and the pool sizing as the drivers behind compute spend.

## Quality bar

Good orchestration work is measured in what it waits for. Triggers are data-aware wherever a signal exists, so a downstream model runs when its input lands instead of at a time somebody chose in a meeting two years ago. Sensors have timeouts and a stated late behavior, because a sensor that waits forever converts a source delay into a silent stall. Retry policy names the failures that will never succeed on a second attempt, since retrying a permission error three times with backoff is a way of spending the response window. The SLA is a condition on data, not on task completion, and it names a person and an expected action. Run history is characterized by failure class, so chronic flakiness is visible as chronic rather than absorbed into an average. And the backfill controls exist before anyone needs them, because they are always needed under time pressure and never written then.
