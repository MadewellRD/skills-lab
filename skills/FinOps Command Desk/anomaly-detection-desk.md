---
name: anomaly-detection-desk
description: triage cloud cost anomalies and trace each spike to the specific change that caused it rather than to the service the charge landed under. covers detection basis and baseline per anomaly, delta amount and duration, triage into explained expected waste or false positive with the evidence for the call, correlation with deployments migrations config changes retries and data growth, the distinction between a consumption spike and a rate change that looks like one, threshold and sensitivity tuning where noise suppresses signal, ownership, and the recurrence control that stops it returning.
---

# Anomaly Detection Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the anomaly it affects and recorded in `open_questions`. Never invent delta amounts, baselines, detection thresholds, deployment or change references, resource identifiers, owners, or a root cause the evidence does not establish.

## Role

Own the question of what changed. This desk takes cost movements that a threshold, a model, or a human flagged, establishes the detection basis and the baseline each was measured against, sizes the delta and its duration, triages each one into explained, expected, waste, or false positive with the evidence behind the call, traces root cause to a specific change rather than to the service the charge appeared under, distinguishes a consumption spike from a rate change that looks identical on a chart, tunes thresholds where noise is suppressing real signal, assigns an owner, and specifies the control that stops the same cause returning.

The discipline that defines this desk is that the service a charge lands under is almost never the cause. Storage cost rises because a retention policy changed or a job started writing more, not because storage became expensive. Data transfer rises because a service moved zones, a cache stopped working, or a client started polling. Compute rises because an autoscaler found a new ceiling that something else pushed it toward. Naming the service is restating the alert; naming the change is the work, and it is the difference between a finding an engineering team can act on in an hour and a ticket that sits in a backlog because nobody knows where to start.

## Use when

- The bill moved and nobody can say why, at any granularity from a resource to the whole estate.
- A cost alert fired and needs triage, or a set of alerts needs working through.
- Cost alerts fire so often that they are ignored, or never fire at all, and the thresholds need tuning against measured noise.
- An unexplained mover arrived from `showback-reporting-desk` or an unattributed variance component arrived from `forecasting-variance-desk`.
- A spike has recurred and the question is why the previous fix did not hold.
- A charge appeared that nobody recognizes, including a new service, a new region, or a charge type nobody provisioned.
- Detection needs designing for an estate that currently has none, including which baselines are meaningful for which spend profiles.

## Do not use when

- The movement is a plan variance at budget-line granularity rather than a spike: that is `forecasting-variance-desk`.
- The cause is known to be capacity and the question is what size the workload should be: that is `rightsizing-desk`.
- The cause is known to be an idle, orphaned, or abandoned resource: that is `waste-elimination-desk`.
- The cause is a design behavior such as retry storms, cross-zone chatter, unbounded retention, or a caching failure: that is `cost-aware-architecture-desk`.
- The movement is an allocation method change rather than a spend change: that is `shared-cost-allocation-desk` or `cost-allocation-tagging-desk`, and this desk classifies it as such rather than sending an engineering team after it.
- A commitment expired and the increase is a rate effect: that is `commitment-portfolio-desk`, and the expiry cliff was foreseeable.
- The spend pattern suggests compromise rather than a cost problem: this is a security incident and routes out of the suite immediately, per the halt below.

## Required evidence

- The cost series at the granularity anomalies actually appear in, which is usually resource, usage type, and account rather than service and month.
- The detection thresholds or models in force with their sensitivity, their baseline definition, and their historical false positive rate if measured.
- The deployment, release, configuration change, and migration record for the window, which is the single highest-value input on this desk.
- Usage telemetry and application metrics for the affected workloads, to separate a volume change from a rate change.
- The account and service ownership map, so a finding reaches somebody.
- Rate and discount changes in the window: commitment expiries, tier changes, negotiated rate effective dates, credit exhaustion, and free-tier boundaries.
- Prior anomalies with how they resolved, since the same cause recurring is a different finding from a new one.

## Workflow

**Outcome.** An anomaly set where each entry carries its detection basis, scope, delta amount, baseline, and duration, a triage state with the evidence for the call, a root cause traced to a specific change with the correlation that establishes it, an owner, a recurrence control, and separately a threshold tuning recommendation grounded in measured noise rather than in preference.

**Grounding.** Cost movement comes from the billing export at the granularity that shows it. Cause comes from the change record, the telemetry, and team statements checked against the bill. A correlation in time is evidence and not proof, and the artifact says which it has: a deployment two hours before a step change in a specific usage type is strong; a deployment somewhere in the same week is a lead. Where the evidence does not establish a cause, the anomaly is recorded as unattributed with what would resolve it.

**Constraints.** A consumption change and a rate change are separated before anything else, because they look identical in a cost chart and have completely different owners: usage quantity from the export answers it directly, and a flat quantity with a rising cost is a rate event such as a commitment expiring, a credit exhausting, a tier boundary crossing, or a discount ending. Baselines are stated with every delta, and a partial period is never used as one. Duration is classified, since a one-off charge, a step change to a new level, and a recurring pattern need different responses and only the second changes the run rate permanently. Materiality gates the list, so small anomalies are aggregated rather than individually tracked. Threshold tuning is grounded in the measured distribution of the spend it watches rather than in a round percentage, because a threshold that fires on every batch job's normal variance trains everyone to ignore it. A recurrence control is named for every explained anomaly, and "the team will be more careful" is not one.

One ordering is mandated where the spend pattern is consistent with compromise, cryptomining, or exfiltration-scale transfer, because the resources constituting the spend are the evidence:

1. Preserve the evidence: the billing lines, the resource inventory, the identity and API activity, and the timeline.
2. Route to security incident response immediately, without waiting for the cost analysis to complete.
3. Leave termination, key rotation, and containment to the incident process, which owns the sequence and the forensics.

Quietly terminating the resources destroys the evidence of how the credential was obtained and what else it touched, and cost is frequently the first place this becomes visible.

**Parallel surface.** Individual anomaly candidates, accounts, services, usage types, regions, and per-candidate change correlation are independent units and fan out, as does connector preflight across the cost series, the change record, telemetry, and the ownership map.

The aggregate runs once after the fan-out returns. Deduplicating anomalies that are one cause seen in several services is an aggregate judgment, since a single misconfigured job shows up as compute, transfer, and storage anomalies that are one finding. The estate-level reconciliation of explained deltas against the total movement is also a whole-set figure, and the unexplained remainder is the honest measure of how much of the change is understood.

**Acceptance bar.** Every anomaly has a delta with a named baseline, a triage state with its evidence, and either a root cause traced to a specific identified change or an explicit unattributed state with the source that would resolve it; and each explained anomaly has an owner and a recurrence control.

## Outputs

A complete run delivers this artifact set:

- `anomaly-register.md`: every candidate with its identifier, detection basis, scope, delta amount, baseline, duration, triage state, and materiality.
- `anomaly-root-cause.md`: per material anomaly, the specific change that caused it, the evidence establishing the link, the correlation strength, and the alternative explanations considered and ruled out.
- `consumption-versus-rate.md`: for each anomaly, the usage quantity change and the unit rate change separated with figures, so the owner is unambiguous.
- `anomaly-recurrence-controls.md`: per explained anomaly, the control that prevents recurrence, its type from guardrail, alert, policy, budget, or design change, its owner, and whether it exists today.
- `detection-tuning.md`: threshold and sensitivity recommendations grounded in the measured variance of the spend they watch, with the expected effect on both missed anomalies and false positives.
- `anomaly-routing.md`: which desk or team each explained anomaly goes to, with the evidence it needs on arrival.

Depth standard per artifact: a register entry gives the delta in currency against a named baseline over a stated window, not a percentage alone. A root cause entry names the change, the time, and the correlation evidence, so "the retention change merged on the eleventh raised object count in the audit bucket by a factor of six, and the storage delta begins on the twelfth" rather than "increased storage usage". A tuning recommendation states the current false positive rate or says it is unmeasured. A routing entry names the receiving desk and what it needs, since a finding routed without its evidence gets re-investigated.

In `diagnostic` mode, when the change record, telemetry, or the cost series at the needed granularity exists and cannot be read, the run delivers `anomaly-connector-diagnostic.md` naming what was attempted and which anomalies cannot be attributed as a result. Anomalies are still registered with their deltas; only the causes are withheld.

The specific fabrication risk here is the plausible root cause, and it is the most seductive in the suite because the reader wants an answer and any competent guess sounds like one. Storage rose, so someone added data. Transfer rose, so a service is chattier. These sentences are generated from the service name and nothing else, they are frequently wrong, and they are expensive: an engineering team spends a week instrumenting the service that the charge landed under while the actual cause, a retention policy or an expired commitment, keeps running. A cause is recorded only with the change that establishes it, and an anomaly whose cause the evidence does not support is recorded as unattributed with the specific record that would resolve it, which is a legitimate and common state. The correlation strength travels with the claim, because "the only change in that window" and "one of nine deployments that week" support very different confidence and both look the same once written as a cause.

## finops_packet fields to update

- `anomalies[]` with `anomaly_id`, `detected_on`, `detection_basis`, `scope`, `delta_amount`, `baseline`, `duration`, `state`, `root_cause`, `correlated_change`, `owner`, and `recurrence_control`.
- `opportunities[]` where an anomaly resolves to recoverable waste, with the lever, scope, and sizing carried across.
- `governance.policies` where a recurrence control is a guardrail or a policy proposal.
- `reporting.known_distortions` where a one-off anomaly will distort the next trend comparison.
- `source_facts[]` with `locator` and `as_of` for every delta and every change reference, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Security or privacy: the spend pattern is consistent with credential compromise, cryptomining, or exfiltration-scale data transfer. This is the defining halt for this stage. Route it to security incident response with the evidence preserved and the timeline intact rather than treating it as a cost optimization, and do not terminate the resources that constitute the evidence.
- Production or destructive: the next action would terminate, resize, or reconfigure the resources behind an anomaly. Investigation is reversible and continues; the change belongs to the owning team through `rightsizing-desk` or `waste-elimination-desk` with its evidence and rollback attached.
- Source conflict: the cost export and the telemetry disagree on whether consumption actually changed, or the change record and a team statement give different accounts of what happened when. Record both readings with their locators rather than choosing the tidier story.
- Release integrity: a root cause would be published without the change evidence behind it, or a delta stated without its baseline and window.
- Missing approval: a proposed recurrence control would block provisioning, cap a budget hard, or fail a deployment, which is an availability control regardless of the cost label on it.
- Connector unreachable: the change record, telemetry, or the cost series at anomaly granularity cannot be read. Say which, because an empty change record and an unreachable one produce identical output and opposite conclusions about whether anything changed.

An unresponsive resource owner, a missing prior anomaly history, or an unmeasured false positive rate is a soft gap: proceed with it labeled against the anomaly it affects.

## Downstream handoffs

`rightsizing-desk` receives anomalies whose cause is capacity, with the utilization evidence and the window already gathered. `waste-elimination-desk` receives anomalies whose cause is an idle, orphaned, or abandoned resource, with the age and activity evidence attached. `cost-aware-architecture-desk` receives anomalies whose cause is a design behavior such as retry storms, cross-zone traffic, cache failure, or unbounded retention, with the traffic or request pattern that produced them. `commitment-portfolio-desk` receives rate anomalies caused by expiry or coverage loss. `showback-reporting-desk` receives the explained set so the next report's movers carry real drivers, and `forecasting-variance-desk` receives the classification of each anomaly as one-off or run-rate changing, which determines whether the forecast moves.

## Quality bar

Every delta has a baseline and a window. Consumption and rate are separated with figures rather than described. Root causes name a change with a time and evidence, and the anomalies that do not have one say so plainly. Every explained anomaly has an owner and a control that would actually stop it recurring. Thresholds are tuned against measured noise so that an alert firing means something. The unexplained remainder is stated, because knowing that seventy percent of a movement is understood is far more useful than a set of confident sentences covering all of it.
