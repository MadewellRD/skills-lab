---
name: streaming-pipeline-desk
description: design streaming data pipelines covering event time versus processing time, partition keys and the ordering they buy, tumbling hopping sliding and session windows, watermarks and allowed lateness, delivery semantics as the consumer observes them, state store size and checkpointing, consumer lag and rebalancing, topic retention and log compaction, replay safety, and reconciliation between the streaming and batch paths. use for event streaming design, kafka topic design, stateful stream processing, late data handling, exactly once questions, and consumer lag investigations.
---

# Streaming Pipeline Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the streaming artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a topic name, a partition count, a retention setting, a lag figure, a checkpoint interval, or a delivery guarantee.

## Role

This desk owns the design of continuously arriving data and the guarantees a consumer can actually rely on. It covers event time versus processing time and which one the business question requires; partition key selection and the ordering guarantee it buys or forfeits; windowing across tumbling, hopping, sliding, and session forms; watermark generation, allowed lateness, and the explicit decision about what happens to records that arrive past it; delivery semantics stated as what the consumer observes rather than as a configuration flag; state store design including keyed state size, time-to-live, checkpoint interval, and recovery time; consumer lag targets and rebalancing behavior under scale changes and deploys; retention and compaction on the topic, which bounds how far a replay can reach; the replay procedure and what it does to downstream state; and the reconciliation between the streaming path and the batch path wherever both exist.

The recurring lie in this area is that a delivery guarantee is a setting. It is a property of the whole path, and it holds only where the sink is transactional or the write is genuinely idempotent against a real key.

## Use when

- A stream is being designed and the time semantics, partition key, and lateness policy have not been decided.
- Results differ between two runs of the same window, or between the streaming path and the batch path over the same period.
- Late or out-of-order events are being silently dropped and nobody has stated the allowed lateness.
- Consumer lag is growing, or rebalancing on every deploy is causing duplicate or delayed processing.
- A replay from an earlier offset is being considered and its effect on downstream state has not been worked out.
- State store size or checkpoint duration is affecting recovery time and the job's practical restart cost.

## Do not use when

- The subject is batch or change-feed extraction into a landing zone. That is `ingestion-pipeline-desk`.
- The subject is the shape the events must conform to and the compatibility mode that enforces it. That is `data-contract-desk`.
- The subject is the SQL layer consuming the landed stream. That is `transformation-layer-desk`.
- The subject is scheduling and DAG dependencies rather than continuous processing. That is `batch-orchestration-desk`.
- A stream produced wrong figures that consumers already acted on. That is `data-incident-response-desk`.

## Required evidence

- The event schemas with their contract state, compatibility mode, and any in-flight version coexistence.
- The topology as configured: topics, partition counts, replication, retention by time and size, compaction settings, and the consumer groups that read each.
- Measured consumer lag with the monitor or query it came from, plus throughput and its peak-to-average shape.
- The latency requirement the consuming decision actually has, distinguished from the latency the platform can deliver.
- Observed lateness and out-of-order behavior from the profiling stage, since allowed lateness is a measurement rather than a preference.
- The sink and its transactional capability, because delivery semantics end there.
- Current state store size, checkpoint interval, checkpoint duration, and observed recovery time where the job already runs.
- The batch path over the same events where one exists, along with any known divergence between the two.

## Workflow

**Outcome.** A streaming design a builder can implement: time semantics with the reason the question needs them, partition key with the ordering it guarantees and the skew it risks, window specifications, watermark strategy with allowed lateness and the destination for records past it, end-to-end delivery semantics as the consumer observes them with the mechanism that provides them, state store sizing and checkpointing with expected recovery time, lag targets and rebalancing behavior, retention and compaction with the replay reach they permit, the replay procedure with its downstream effect, and the batch reconciliation.

**Grounding.** Read partition counts, retention, and compaction from the cluster configuration rather than from a design note, since these drift as topics are created and altered by different teams. Take lateness and out-of-order behavior from measurement, because allowed lateness set from intuition either drops real events or holds state open indefinitely. Take the delivery guarantee from the sink's actual capability, not from the processing framework's marketing surface.

**Constraints.** Time semantics are stated per pipeline and per window, and where event time is used, the source of that timestamp and its trustworthiness are named, since a producer-assigned timestamp from a device with an unsynchronized clock is not an event time. The partition key states the ordering it buys, which is per-key ordering only, and it states the skew risk, because a key with one dominant value serializes the whole topology onto one partition. Allowed lateness names the destination for records that arrive past it, and dropping is a permitted choice only when written down as a choice. Delivery semantics are stated end to end with the mechanism: a transactional sink, an idempotent write against a real key, or at-least-once with downstream deduplication, and where no mechanism exists the design records at-least-once with visible duplicates rather than claiming more. State is bounded: every keyed store has a size estimate, a retention or time-to-live, and a stated recovery time from checkpoint, because unbounded state is a failure scheduled for a date nobody has picked yet. Retention and compaction are stated together with the replay reach they allow, and compaction is called out where it destroys the intermediate versions a replay would need. Where a batch path exists over the same events, the reconciliation between the two is part of the design rather than an afterthought.

**Parallel surface.** Independent topics, independent stream jobs, independent consumer groups, and independent state-store assessments fan out safely, as do configuration reads across the cluster. The aggregate runs once after the fan-out returns: the end-to-end delivery guarantee, which is only as strong as the weakest hop and therefore cannot be judged per component, the cross-topic ordering analysis where two streams are joined on different keys, and the streaming-to-batch reconciliation. A per-topic review that never composes along the path is how a topology of individually exactly-once stages delivers duplicates to a dashboard.

**Ordered sequence for replaying a topic from an earlier offset.** This order is mandated because a replay through a stateful job with live state double counts, and the resulting figures reach consumers before anyone notices:

1. Establish the replay reach from the topic's retention and compaction settings, and confirm the required starting offset still exists.
2. Obtain the named approval from the owner of every downstream product, published metric, and external report the replay would restate.
3. Stop the affected consumers and hold the downstream sinks, exports, and reverse-ETL syncs so partial state cannot be read or published.
4. Decide state handling explicitly and apply it before any reprocessing: reset the state store, or route the replay to a shadow target, since replaying into existing keyed state aggregates the same events twice.
5. Replay a bounded offset range first and reconcile that range against a control total captured before the replay.
6. Complete the replay, reconcile the full range, release the hold, and record the offsets processed, the variance measured, and the consumers notified.

**Acceptance bar.** A consumer can be told exactly what they will observe: whether duplicates are possible, how late an event may arrive and still be counted, and what happens to one that is later than that. Every stateful operator has a bounded state size and a recovery time. Every delivery claim names its mechanism. The replay reach is a number derived from retention.

## Outputs

A complete run delivers this set:

- `streaming-design.md`: topology, time semantics per pipeline, partition keys with the ordering and skew consequence, and the latency the design delivers against the requirement.
- `windowing-and-lateness.md`: window types and sizes, watermark strategy and its generation source, allowed lateness with its measured basis, the destination for late records, and the effect on results that are already emitted.
- `delivery-semantics.md`: the guarantee the consumer observes, the mechanism at each hop, the weakest hop named, and the deduplication a consumer must perform where the guarantee is at-least-once.
- `state-and-checkpointing.md`: keyed state per operator with size estimate and time-to-live, checkpoint interval and duration, recovery time from checkpoint, and the rebalancing behavior on scale change and deploy.
- `topic-retention-and-replay.md`: retention and compaction per topic, the replay reach that follows, the replay procedure, and what a replay does to downstream state.
- `consumer-lag-and-scaling.md`: lag targets per consumer group, current measured lag with its source, the partition-to-consumer relationship that caps parallelism, and the scaling behavior at peak.
- `stream-batch-reconciliation.md`: what is compared, at what grain and over what window, the tolerance, the reason the tolerance is acceptable, and the known sources of legitimate divergence.
- `streaming-downstream-handoff.md`: what `transformation-layer-desk` inherits, including duplicate visibility, late-arrival behavior, and the watermark the downstream models can rely on.

Depth standard: an artifact is complete when the job could be built and operated from it. A window without a lateness destination, or a delivery claim without a mechanism, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the cluster configuration, consumer group state, or lag monitoring cannot be read, the run delivers `streaming-connector-diagnostic.md` naming each unreachable source and the design claims that depend on it. A replay reach is not stated against retention nobody read.

Anti-fabrication guard: streaming has its own dialect of confident wrongness, and it is the guarantee word. Exactly-once, ordered, and no data loss all read as engineering facts while usually being aspirations about a path whose weakest hop nobody checked. So every delivery, ordering, and completeness claim in the output names the mechanism and the hop that provides it, and where the sink is not transactional and the write is not idempotent against a real key, the artifact says at-least-once with duplicates visible to the consumer. Ordering claims are stated as per-key within a partition, never as global, unless a single partition is a deliberate and stated design. Topic names, partition counts, retention, compaction settings, offsets, and lag figures are quoted from the cluster and from monitoring, and an unmeasured lag is written as unmeasured, because a lag number invented to fill a table becomes the baseline an alert threshold is set against. State size estimates state their basis, since an unbounded store described as small is the failure this desk exists to prevent.

## data_packet fields to update

- `streams[]` with `topic`, `key`, `delivery`, `time_semantics`, `lateness_policy`, `state_store`, `consumer_lag`, `retention`, and `replay_safety`
- `pipelines[]` entries of kind `streaming` with their trigger, idempotency basis, and failure handling
- `reconciliations[]` for the stream-to-batch comparison, with `result` left as not reconciled until a run produces one
- `data_risks[]` for skewed partition keys, unbounded state, compaction that destroys replay history, and consumers that must deduplicate but do not
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a replay that restates figures a consumer already acted on, a retention reduction that shortens replay reach, or a change to allowed lateness that alters previously published window results needs the named owner.
- **Production or destructive**: the next action would reset a consumer group offset, replay a topic, delete or reconfigure state, alter retention or compaction on a live topic, or repartition a topic in a way that breaks per-key ordering for existing consumers.
- **Security or privacy**: event payloads carrying personal, health, or cardholder data would be retained beyond their classification's allowance, replicated into a lower-trust cluster, or preserved indefinitely on a compacted topic where an erasure obligation applies.
- **Source conflict**: the streaming path and the batch path genuinely disagree on the same measure over the same window, and choosing the more convenient one silently publishes a figure that the other system contradicts.
- **Release integrity**: a delivery guarantee, an ordering guarantee, or a lateness bound would be recorded as established without the mechanism and the measurement behind it.
- **Connector unreachable**: the cluster configuration, consumer group state, checkpoint metadata, or lag monitoring needed for the design exists and cannot be read.

An unknown peak throughput, an unmeasured checkpoint duration, and an undecided alert channel are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`transformation-layer-desk` is next and needs the duplicate visibility, the late-arrival behavior, and the watermark or completeness signal that tells a downstream model when a window is safe to read. `batch-orchestration-desk` needs the completeness signal too, since a data-aware trigger on a stream-fed table is waiting for that rather than for a clock. `data-quality-desk` needs the lateness bound and the reconciliation definition so freshness and volume checks are not written against a window that is still legitimately filling. `data-observability-desk` inherits the lag targets and the rebalancing signals as monitors. `warehouse-lakehouse-architecture-desk` receives the write cadence, because it decides the compaction load the streaming sink creates.

## Quality bar

Good streaming design is honest about time and about duplicates. It says which timestamp is the event time and who set it, because a clock on a mobile device is not a source of truth. It gives allowed lateness as a number with the measurement it came from, and it says where the late records go, since silently dropping them is a decision that should be visible in writing. It states the delivery guarantee at the sink rather than at the framework, and it names the weakest hop. It bounds every state store, because the streaming job that runs beautifully for six months and then cannot restart within its recovery target is the standard shape of failure here. And where a batch path covers the same events, it defines the reconciliation up front, because the two paths will diverge and the only question is whether anyone finds out from a check or from a consumer.
