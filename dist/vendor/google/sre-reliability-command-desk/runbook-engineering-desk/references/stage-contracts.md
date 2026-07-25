# SRE Reliability Stage Contracts

One entry per desk in the suite: what it requires on input, what it owns on output, and where it hands the `reliability_packet`. The orchestrator uses these contracts to route; each member desk uses its own entry as the acceptance boundary for "this stage is done."

## Default sequence

```text
service-tiering
  -> sli-specification
  -> slo-error-budget
  -> dependency-failure-analysis
  -> resilience-architecture
  -> capacity-planning
  -> load-performance-testing
  -> chaos-resilience-testing
  -> disaster-recovery
  -> backup-restore
  -> alerting-quality
  -> runbook-engineering
  -> oncall-escalation
  -> production-readiness-review
  -> change-safety
  -> incident-command
  -> postmortem
  -> toil-reduction
  -> reliability-review
```

The chain is ordered by packet dependency, not by calendar. A request that starts mid-chain starts at the earliest desk whose inputs are already satisfied, and an active incident enters at `incident-command-desk` regardless of what is upstream of it.

## Stage completion rule

Every desk emits: source facts with attribution, decisions, its artifact set, the packet fields it updated, assumptions labeled where they were used, open questions, halt conditions, and next-stage readiness. Measurement state travels with every number. Unmeasured stays unmeasured in the packet.

---

## sre-reliability-command-desk

- **Requires**: the user request, target outcome, operating posture, and whatever connector access exists for metrics, paging, incidents, deploys, catalog, and backups.
- **Owns**: request classification, stage path selection, packet initialization and carriage, adjudication of conflicts between measured behavior and documented intent, the workflow-level record, and the cross-suite handoff decision.
- **Hands to**: the earliest member desk whose inputs are satisfied, then each successive stage until the target outcome is reached or a hard halt applies.

## service-tiering-desk

- **Requires**: the service or product in scope, the service catalog or repository inventory, ownership records, pager rotations, traffic or revenue context, and any existing tiering standard.
- **Owns**: the critical user journey map, the service-to-journey path, criticality tiers with the rule that assigns them, ownership and pager attribution per service, support model per service (team owned, SRE supported, unsupported), and the honest list of services with no owner or no tier.
- **Hands to**: `sli-specification-desk`.

## sli-specification-desk

- **Requires**: the critical user journey map with tiers, the request path and its measurement points, existing dashboards and metric names, and the telemetry actually emitted today.
- **Owns**: SLI specifications per journey (what event is counted, what makes an event good, over what window), the measurement point and its bias, the implementation query or export behind each SLI, the split between measured, partially measured, and unmeasured, and the instrumentation gaps that must close before an objective means anything.
- **Hands to**: `slo-error-budget-desk`.

## slo-error-budget-desk

- **Requires**: SLI specifications with their measurement state, historical attainment where it exists, tier expectations, and the business or contractual commitments that constrain the target.
- **Owns**: objectives with their windows, error budget definition and current balance, burn rate accounting, the error budget policy and what exhausting it actually changes, the agreement state per objective (agreed with the owner, proposed, or aspirational), and the separation between an objective that is measured and one that is only written down.
- **Hands to**: `dependency-failure-analysis-desk`.

## dependency-failure-analysis-desk

- **Requires**: the journey paths, service and infrastructure topology, dependency configuration (timeouts, retries, clients), observed dependency availability, and incident history.
- **Owns**: the dependency graph along each journey with hard, soft, and degraded-ok coupling; single points of failure and shared-fate analysis across zones, clusters, datastores, identity, DNS, and control planes; failure mode analysis with trigger, propagation, detection, and mitigation per mode; correlated failure and retry-storm risk; and the composed journey availability implied by the graph against the objective the journey carries.
- **Hands to**: `resilience-architecture-desk`.

## resilience-architecture-desk

- **Requires**: the failure mode inventory and dependency coupling, current client and server configuration, degradation options the product allows, and the objectives each journey must hold.
- **Owns**: timeout and retry budgets with concrete values, circuit breaker and bulkhead placement, load shedding and admission control policy, backpressure and queue depth handling, cache and stale-serve fallbacks, idempotency and replay safety, graceful degradation modes with what the user sees in each, and the evidence state per control (configured, tested, proven in an incident, or unproven).
- **Hands to**: `capacity-planning-desk`.

## capacity-planning-desk

- **Requires**: demand history and forecast, saturation signals and current utilization, scaling limits and quotas, provisioning lead times, cost constraints, and the failover topology the recovery stage will assume.
- **Owns**: the demand model and its drivers, headroom against the binding saturation signal rather than against average CPU, the ceilings that bound scaling (quota, connection, partition, thread pool, licence, lead time), failover headroom for the surviving zone or region under real peak, the provisioning plan with its lead time, and the measured-versus-assumed split for every number in it.
- **Hands to**: `load-performance-testing-desk`.

## load-performance-testing-desk

- **Requires**: the capacity model and its saturation hypotheses, the workload mix from production telemetry, a test target with a stated fidelity gap, and the objectives the test is asked to defend.
- **Owns**: the workload model and how it was derived from real traffic, the test profiles (load, stress, soak, spike, breakpoint) and what each is asked to prove, environment fidelity gaps and what they invalidate, the measured saturation point and failure behavior past it, latency distribution at target and beyond, and the performance regression gate that ties results back to the objective.
- **Hands to**: `chaos-resilience-testing-desk`.

## chaos-resilience-testing-desk

- **Requires**: the failure mode inventory, the resilience controls claimed to handle each mode, the steady-state signal that defines normal, and the approval and environment boundary for injecting faults.
- **Owns**: experiment design with an explicit steady-state hypothesis, the fault and its scope, blast radius containment and the abort criteria stated before injection, game day plans and the roles they exercise, results that confirm or disprove each hypothesis, and the promotion of a disproved control from claimed to broken with the failure mode it leaves open.
- **Hands to**: `disaster-recovery-desk`.

## disaster-recovery-desk

- **Requires**: tiers and journey criticality, the dependency recovery order implied by the graph, replication and failover topology, regulatory or residency constraints, and the last exercise result if one exists.
- **Owns**: RTO and RPO targets per tier with their source, the failover mode actually implemented (active-active, active-passive, pilot light, backup-restore only), the regional evacuation and failback procedure, the dependency recovery order including identity, DNS, data tier, and control plane, the exercise plan and its measured results, and the gap between the plan's stated recovery time and the last measured one.
- **Hands to**: `backup-restore-desk`.

## backup-restore-desk

- **Requires**: the data inventory with classification and RPO targets, backup system configuration, retention and immutability settings, restore tooling, and the history of restore attempts.
- **Owns**: backup coverage per dataset against the data inventory including what is not backed up, mechanism, schedule, retention, and immutability with their sources, the restore procedure and its measured time from a dated drill, integrity and corruption detection, ransomware and accidental-deletion resistance, and the explicit statement of which datasets have never had a restore proven.
- **Hands to**: `alerting-quality-desk`.

## alerting-quality-desk

- **Requires**: the SLIs and error budget policy, the current alert rule inventory, page history from the paging platform, incident detection sources, and runbook coverage.
- **Owns**: the alert set with symptom-based paging on user impact, multi-window multi-burn-rate rules tied to error budget spend, the page-versus-ticket-versus-dashboard routing decision per alert, deduplication, grouping, and dependency-aware suppression, the noise review that names alerts that fire without action and alerts that have never fired, and the detection gaps where incidents were found by customers rather than by a signal.
- **Hands to**: `runbook-engineering-desk`.

## runbook-engineering-desk

- **Requires**: the alert set with routing, failure modes and their mitigations, resilience control values and degradation modes, access and permission requirements, and existing runbook content.
- **Owns**: runbooks keyed to the alert or failure mode that triggers them, the first mitigating action stated before any diagnosis, the diagnostic decision tree with the exact queries and dashboards it depends on, escalation and rollback branches, the access and permission preconditions an on-call engineer needs at three in the morning, freshness state per runbook, and the alerts left without a runbook.
- **Hands to**: `oncall-escalation-desk`.

## oncall-escalation-desk

- **Requires**: rotations and staffing, page history and its out-of-hours distribution, severity definitions, runbook coverage, and the organizational escalation and support policy.
- **Owns**: rotation design and coverage including follow-the-sun or out-of-hours arrangements, the escalation path with named tiers and response expectations, the primary-to-secondary and shift handoff ritual with what open state transfers, the page load budget and what happens when a rotation exceeds it, onboarding and shadowing for new responders, and the coverage gaps where nobody is actually reachable.
- **Hands to**: `production-readiness-review-desk`.

## production-readiness-review-desk

- **Requires**: the packet state from every upstream reliability stage, the launch or support-acceptance request, the tier the service claims, and the standard the review is conducted against.
- **Owns**: the readiness gate set with a pass, waived, failed, or not-assessed state per gate and the evidence behind each state, the launch or support-acceptance decision, waivers with a named owner and an expiry rather than an open-ended exception, the reliability debt the service enters production carrying, and the explicit refusal to record a gate as passed on the basis of a document that no measurement supports.
- **Hands to**: `change-safety-desk`.

## change-safety-desk

- **Requires**: the readiness decision and open waivers, the deployment and rollout mechanism, the SLIs and burn-rate signals that judge a rollout, error budget state, and rollback capability.
- **Owns**: the rollout strategy and its stages, canary analysis with the signal and threshold that decides promotion or reversal, bake time per stage, the rollback trigger and whether rollback has actually been executed successfully before, freeze policy and its override path, migration and schema change safety including the expand-and-contract sequence, and change failure rate against the error budget policy.
- **Hands to**: `incident-command-desk`.

## incident-command-desk

- **Requires**: the active signal or report, severity definitions, the service tier and journey affected, runbooks and dependency graph, recent deploy and configuration change history, and the escalation and communication policy.
- **Owns**: severity classification and its declaration, the command structure (incident commander, operations lead, communications lead, scribe) and who holds each role, the mitigation decision with reversible options preferred over diagnostic ones, the evidence capture that a restart would destroy, internal and customer communication cadence including the status page, the reconciled timeline, and the recovery confirmation measured against the journey SLI rather than the symptom that paged.
- **Hands to**: `postmortem-desk`.

## postmortem-desk

- **Requires**: the incident timeline and evidence, detection and mitigation timestamps, the change history around the event, the journey and budget impact, and the participants who can supply the narrative.
- **Owns**: the blameless narrative with a timeline anchored to timestamped evidence, contributing factors across technical, detection, and process dimensions, counterfactual discipline that resists the single-root-cause story, the what-went-well record including the controls that worked, action items classified as prevent, detect, mitigate, or process with named owners and due dates, the error budget consumed, and the trend view across prior incidents that says whether this is a recurrence.
- **Hands to**: `toil-reduction-desk`.

## toil-reduction-desk

- **Requires**: page and ticket history, the operational task inventory, postmortem action items, runbook steps that are executed manually, and the operational load budget the team works to.
- **Owns**: toil accounting with hours per week per recurring task and how the hours were established, classification of each task as automatable, partially automatable, or inherent, the elimination path per task (automation, self-service, or a design change that removes the task), the prioritized backlog against operational load, and the honest separation between measured toil and estimated toil.
- **Hands to**: `reliability-review-desk`.

## reliability-review-desk

- **Requires**: error budget attainment and burn across the review period, incident and page trends, open postmortem actions, toil accounting, open readiness waivers and their expiry, and the reliability risks recorded upstream.
- **Owns**: the recurring service reliability review record, the error budget policy adjudication for the period including whether a freeze applies, the reliability risk register with exposure and owner, the reliability roadmap that ranks debt against journey impact rather than against the loudest incident, objective revision proposals with evidence, and the report a service owner and an executive can both act on without a follow-up round trip.
- **Hands to**: the orchestrator for workflow close, or back to `slo-error-budget-desk` when the review concludes an objective no longer describes what users actually need.

---

## Cross-suite boundary

These hand outward rather than to another desk in this suite: software defect triage, hotfix implementation, issue planning, and implementation handoff go to the SDLC suite; the internal developer platform and its golden paths go to the Platform Engineering suite; security incident handling, breach response, and threat modeling go to the Security suite; cloud spend policy goes to the FinOps suite; audit response and control evidence go to the GRC suite. Label the handoff explicitly so nobody reads those desks as members of this one.
