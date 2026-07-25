---
name: data-incident-response-desk
description: respond to bad data in production covering severity by consumer exposure rather than row count, containment that pauses dependents and holds exports, evidence capture before any re-run, lineage-derived blast radius including external recipients, the backfill restatement or withdrawal decision with its reconciliation, consumer notification and the restatement record, and the postmortem with the detection gap that let it run. use when a wrong number reached consumers, a load duplicated or dropped rows, or a schema break silently corrupted a mart.
---

# Data Incident Response Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the incident artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Pressure inverts the usual balance here, so the distinction is stated plainly: an unknown root cause is a soft gap and containment proceeds without it, while running a correction over live partitions is a destructive action that stops at its gate however obvious the fix looks. Never invent affected partition bounds, row counts, timestamps, consumer lists, recipients, the version that produced the data, or the root cause.

## Role

Own bad data that has already reached production. This desk holds severity classification by consumer exposure, containment that stops propagation, evidence capture taken before any re-run, blast radius derived from lineage including external recipients, the correction decision across backfill, restatement, and withdrawal with the reconciliation that shows it landed, consumer notification and the restatement record, and the postmortem with the detection gap that let the incident run.

Data incidents differ from service incidents in the property that governs every decision here. There is no outage: the pipeline succeeded, the dashboard rendered, the export was delivered, and a person made a decision on a number that was wrong. Time therefore does not pressure a fix, it pressures containment and notification, because every hour the bad figure remains readable is another set of decisions taken on it. The second property is that the correction is itself a destructive write against data consumers are reading, so the response has to be sequenced rather than raced; a hurried backfill that overwrites the evidence leaves an organization certain that something was wrong and unable to say what.

## Use when

- A wrong number has reached a dashboard, a report, an export, a feature table, or an external recipient.
- A load duplicated rows, dropped rows, or landed partially, and downstream marts have already been built on it.
- A schema change broke a transformation silently, so the model still produces rows with a column now null, truncated, or mistyped.
- A reconciliation, a finance close, or a consumer complaint has surfaced a discrepancy that the platform did not detect.
- A published or regulatory figure needs restating, or a delivered export needs withdrawing.
- A backfill or migration has produced overlapping, missing, or double-counted history that consumers are already reading.
- A postmortem is due for a data incident and needs the timeline, the contributing factors, the detection gap, and owned actions.

## Do not use when

- The number is disputed rather than wrong, because two definitions of the same metric are in use. That is `metric-semantic-layer-desk`.
- Nothing has reached a consumer and the question is what assertion should exist. That is `data-quality-desk`.
- The question is why nothing detected it, after containment and correction are complete. That is `data-observability-desk`, which this desk hands the detection gap to.
- The failure is the pipeline not running rather than running wrongly, with no bad data downstream. That is `batch-orchestration-desk`.
- The incident is a service outage, a cluster failure, or a platform availability event with no data correctness dimension. That is a labeled cross-suite handoff to the SRE suite.

## Required evidence

- The failing signal or consumer report with its timestamp and what the reporter actually observed.
- The affected assets and the exact partition, key, or time bounds, queried rather than inferred from when the job ran.
- Run history and logs for the failing run and the runs around it, plus the code, schema, and configuration version in effect when it produced data.
- The failing check output and the checks that passed, since a passing check over a wrong number is itself a finding.
- A sample of the upstream payload as it arrived, held under the same restrictions as the source data.
- The lineage graph, which is the instrument for blast radius, along with its known gaps as the bound on that answer.
- Query history and BI view logs over the exposure window, which is what identifies who actually read the wrong figure rather than who could have.
- The export, extract, reverse-ETL, and external delivery record over the same window, including the deliveries that already left the organization.
- A control total captured before any correction, and the snapshot or time travel window that bounds the recovery path.

## Workflow

**Outcome.** A severity classification with the exposure that justifies it, a containment record, a captured evidence set, a blast radius naming every downstream asset, dashboard, export, feature table, and external recipient with the graph gaps that bound it, a correction decision with its reconciliation, a notification record, a restatement record for any published figure that changed, and a postmortem with contributing factors, the detection gap, and owned actions.

**Grounding.** Severity is set by consumer exposure rather than by row count, because eleven wrong rows in a regulatory return outrank four million wrong rows in a staging table nobody reads. The dimensions that set it are who consumed the data, whether a decision was taken on it, whether a figure left the organization, whether a feature table fed a production model, and whether the period is closed. Bounds are queried rather than assumed, since the affected window is regularly wider than the failing run: a late-arriving correction, a re-run that partially succeeded, and a merge that matched on a changed key each corrupt periods outside the run that raised the alert. The blast radius is a traversal, and where the graph has known gaps on the path, the exposure answer says so rather than presenting itself as complete.

**Constraints.** Evidence capture precedes any corrective write, and the captured set is the affected bounds, the run logs, the failing and passing check results, the upstream payload sample, the code, schema, and configuration version, and the control total, because a re-run destroys most of them. Notification is written in terms of what a consumer should do: which figure, which periods, which direction and magnitude, whether to stop using it, and when the corrected version will exist. The correction decision is made explicitly across backfill, restatement, and withdrawal, and it names the reconciliation that will show it landed; a correction with no control total captured beforehand cannot be shown to have worked. Restatement of any published, external, or regulatory figure carries a named approver. Sample rows drawn as evidence keep the classification of their source, so restricted values do not migrate into an incident document with a wider reader set than the table it came from. The postmortem records the detection gap as a first-class finding, because in this domain the interval between the data being wrong and anyone knowing it is the number that determines the cost.

**Parallel surface.** Affected assets, per-consumer notification preparation, per-dashboard exposure assessment, evidence capture across separate systems, and per-partition bound queries are independent units and fan out safely. The aggregate work runs once after the fan-out returns: composing the blast radius across the lineage graph, ranking severity across the whole exposure set, sequencing the correction, and reconciling the corrected result against the control total. The correction itself is not parallel where the affected models are order-dependent: slowly changing dimensions, accumulating snapshots, running totals, and sessionized models are reprocessed in event-time order, since a parallel repair of a type 2 dimension produces overlapping validity windows on top of the original defect.

**Mandated response order.** This order is mandated because each step either preserves or destroys what the next one depends on, and it is stated here so a future editor does not read it as ceremony:

1. Contain before diagnosing: pause the affected pipeline and its downstream dependents, and hold exports, extracts, scheduled deliveries, and reverse-ETL syncs, so the bad partition stops propagating while the rest of the work proceeds.
2. Capture the failing state before any re-run: bounds, logs, check results, upstream payload, versions, and a control total. A re-run overwrites this and it cannot be recovered afterwards.
3. Scope the blast radius from lineage rather than from memory, including whether any figure has already left the organization, and record the graph gaps that bound the answer.
4. Notify the consumers who already acted, before the correction lands, because once the data is corrected there is no artifact a consumer can use to work out which of their decisions rested on the wrong version.
5. Correct within bounds and reconcile against the control total captured in step 2, then confirm freshness and the blocking checks on the corrected partitions.
6. Preserve the timeline, the notification record, and the restatement decision before the incident is closed.

The corrective write in step 5 is a destructive data operation and follows the ordered sequence in `references/suite-workflow-contract.md`, including the recovery-path confirmation and the bounded first pass, rather than being executed directly from here.

**Acceptance bar.** A reader could state what was wrong, over exactly which bounds, who consumed it, what each consumer was told and when, what the correction was and what reconciliation shows it landed, and why nothing detected it sooner. Every bound, count, and timestamp names the query or log it came from, and the blast radius carries the lineage gaps that bound it.

## Outputs

A complete run delivers this set:

- `incident-record.md`: severity with the exposure that justifies it, detection source and time, symptom stated as a consumer would see it, affected assets with queried bounds, status, and the timeline with each entry attributed to a log, run, or message.
- `containment-record.md`: what was paused and held, when, by whom, what remains running by design, and the release condition for each hold.
- `evidence-capture.md`: the captured bounds, run logs, check results, upstream payload reference, code, schema, and configuration versions, and the control total with the query that produced it.
- `blast-radius.md`: every downstream model, dashboard, export, feature table, and external recipient that consumed the data, who actually read it from query and view logs, and the lineage gaps that bound the completeness of the answer.
- `correction-plan.md`: the decision across backfill, restatement, and withdrawal with its reasoning, the exact bounds, the ordering constraint for order-dependent models, the reconciliation that will show it landed, the approver, and the rollback.
- `consumer-notification.md`: per audience, what they were told, when, which figure and periods, the direction and magnitude of the change, what to do in the interim, and the record of who was reached.
- `restatement-record.md`: for every published figure that changed, the old value, the new value, the periods, the approver, and the recipients informed, or an explicit statement that no published figure changed.
- `postmortem.md`: contributing factors without individual blame, the detection gap with the monitor or check that would have caught it, the containment and notification performance, and action items with named owners and dates.
- `incident-downstream-handoff.md`: what `data-quality-desk` and `data-observability-desk` inherit, stated as the specific missing assertion and the specific missing signal.

Depth standard: an artifact is complete when a consumer could act on the notification and an engineer could execute the correction from the plan. A blast radius listing asset counts rather than named consumers, a correction plan with no control total, and a postmortem whose actions have no owner are unfinished rather than draft.

When lineage, query history, run logs, or the export record exists and cannot be read, the run delivers `incident-connector-diagnostic.md` naming each unreachable source and the exposure and correction claims that depend on it, in place of the artifacts that source would have grounded. Containment does not wait for that diagnostic, because holding propagation is reversible and cheap.

Anti-fabrication guard: incident writing happens under time pressure, in a document that becomes the organization's permanent account of what happened, and the pressure pushes toward a coherent story rather than an evidenced one. A timeline reads better when the gap between the failing load and the first complaint is filled in, a root cause reads better as a single upstream change than as undetermined, and a blast radius reads better as a closed list than as a list with a note that the export path is not in the graph. Each of those improvements is a fabrication that later gets cited as fact in a customer conversation or an audit response. So every timeline entry names the log, run, or message it came from, and the intervals nobody can account for stay visible as unaccounted. A root cause is written as determined only where evidence establishes it, and as a hypothesis with the test that would confirm it otherwise. Affected bounds are queried and the query is quoted, since a window inferred from when a job ran routinely understates the damage. Consumers are enumerated from lineage and read logs rather than from who came to the incident channel, and the recipients of an export that already left are listed individually, because the one nobody remembered is the one who finds out from their own auditor.

## data_packet fields to update

- `data_incidents[]` with detection source and time, symptom, affected assets, queried bounds, downstream exposure, correction, notification, and status
- `backfills[]` for the correction with bounds, ordering constraint, idempotency basis, approver, and reconciliation
- `reconciliations[]` with the control total, its capture time, and the measured post-correction variance
- `quality_checks[]` and `monitors[]` gaps identified as the assertions and signals that would have caught it
- `lineage.known_gaps` for every path the blast radius could not traverse
- `metrics[]` where a published figure was restated, with the restatement recorded
- `data_risks[]` for the conditions that let the incident reach consumers
- `operating_posture` set to `active_data_incident` and then to `post_incident`
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would re-run the failing pipeline, backfill or overwrite live partitions, replace a table, replay a topic from an earlier offset, or publish a corrected figure. Containment holds are reversible and proceed; corrective writes stop here.
- **Missing approval**: restating a published, financial, or regulatory figure, withdrawing a delivered export, notifying an external recipient, or accepting a known-wrong figure for a period needs the accountable owner, who has not authorized it.
- **Security or privacy**: the incident involves exposure of personal, health, or cardholder data, or the evidence capture would place restricted values into an incident document, ticket, or channel with a wider reader set than the source.
- **Release integrity**: a correction would be recorded as reconciled, an incident as closed, or a blast radius as complete without the control total, the post-correction variance, or the traversal that establishes each.
- **Source conflict**: the systems genuinely disagree about which figure is correct, so correcting toward either one would publish a number chosen rather than established.
- **Connector unreachable**: lineage, query history, run logs, the check results, or the export record needed to scope exposure exists and cannot be read.

An undetermined root cause, an unknown upstream owner, a missing historical baseline, and an incomplete timeline are soft gaps. Contain, notify on the exposure that is established, name the gaps, and continue. The evidence-before-re-run requirement, the notification-before-correction order, and the approval boundary on restatements are never relaxed to close an incident faster, because each of them exists to protect an answer somebody will need after the incident is over.

## Downstream handoffs

`data-quality-desk` receives the specific assertion that would have caught this, written as an expression with a threshold rather than as a lesson. `data-observability-desk` receives the detection gap and the monitor that would have fired, plus the measured interval between the data being wrong and anyone knowing. `metric-semantic-layer-desk` receives any restated definition and the restatement record. `lineage-catalog-desk` receives every path the blast radius could not traverse, since each is a gap that will bound the next incident too. `data-contract-desk` receives the upstream change that broke the shape, where a producer change caused it. `analytics-enablement-desk` receives the consumers who need re-onboarding onto a certified asset. The orchestrator receives the workflow close. Send platform availability, cluster failure, and on-call command to the SRE suite, and any disclosure dimension to the Privacy or Security suite, as labeled cross-suite handoffs that are additive rather than a transfer of command.

## Quality bar

Good data incident work is judged on containment speed and notification honesty rather than on how fast the number was fixed. It pauses propagation and holds exports before it understands the cause. It captures the evidence a re-run would destroy. It tells the people who acted on the wrong figure before the figure changes underneath them, in terms of what they should do rather than what happened internally. Its blast radius names consumers and recipients and admits which paths the graph could not see. Its correction is bounded, reconciled against a control total captured beforehand, and reversible. And its postmortem leads with the detection gap, because in a domain where nothing goes down, the interval between wrong and known is the only measure of how well the platform is actually running.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
