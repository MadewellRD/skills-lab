# SRE Reliability Suite Workflow Contract

## Purpose

This reference defines how the SRE Reliability Command Desk suite behaves as one continuous workflow instead of a set of isolated prompts. Every desk in the suite reads it, updates the `reliability_packet`, and hands that packet to the next stage.

The subject of this suite is the reliability of running production services: what "working" means for a user journey, how much unreliability the business has agreed to spend, how the system fails, what absorbs those failures, how recovery is proven rather than assumed, who carries the pager, and what the organization learns after it breaks. The packet therefore carries measurement state alongside design state, because a reliability claim nobody computes is the most common artifact in this domain.

## Continuity rule

Do not stop with a bare next-desk recommendation when the next stage can be completed from available source facts. Complete the current stage, update the `reliability_packet`, and continue until the target outcome is reached or a hard halt applies.

A stage is complete when the next desk can act on its output without rediscovering scope, owners, evidence, or thresholds. A stage that emitted headings and deferred their contents is incomplete, because every later stage trusts the packet rather than re-reading the telemetry.

## Operating modes

- `single_stage`: run one desk because the user asked for one specific reliability artifact.
- `workflow_run`: default. Run the stage path the target outcome needs, carrying the packet through each stage.
- `resume`: continue from a prior `reliability_packet` or a halt-resume prompt, treating `completed_stages` as done rather than redoing them.
- `halt`: stop on a hard-halt class from `references/halt-taxonomy.md` and emit the halt format below.
- `diagnostic`: the metrics backend, paging platform, incident tracker, deploy history, backup inventory, or service catalog cannot be reached, so the run reports reachability and evidence gaps instead of asserting reliability state.

## Reliability packet

Every desk preserves and updates this packet. Unknown, unmeasured, and never-tested are legitimate values; a plausible number is not.

```yaml
reliability_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  current_stage: "stage-name"
  completed_stages:
    - "stage-name"
  skipped_stages:
    - stage: "stage-name"
      reason: "why it was not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  reliability_surface: "service_tiering | sli | slo_error_budget | dependency_analysis | resilience_design | capacity | load_test | chaos | disaster_recovery | backup_restore | alerting | runbook | oncall | production_readiness | change_safety | incident | postmortem | toil | reliability_review | unknown"
  operating_posture: "steady_state | pre_launch | change_window | active_incident | post_incident | budget_exhausted | freeze | unknown"
  services:
    - name: ""
      tier: "tier0 | tier1 | tier2 | tier3 | untiered | unknown"
      owner: "source-backed team or unknown"
      pager_rotation: "rotation ref or unknown"
      lifecycle: "pre_launch | ga | deprecated | unknown"
      support_model: "team_owned | sre_supported | unsupported | unknown"
  critical_user_journeys:
    - journey: "what the user is trying to do"
      entry_point: "surface the journey starts at"
      services_on_path: []
      tier: "inherited or assigned tier"
      volume: "measured request or session rate, or unmeasured"
  slis:
    - id: ""
      journey: "journey this measures"
      type: "availability | latency | correctness | freshness | durability | throughput | coverage"
      specification: "what event is counted and what makes an event good"
      measurement_point: "load balancer | server | client | synthetic probe | log pipeline | data job"
      source: "query, dashboard, or export the number comes from"
      state: "measured | partially_measured | unmeasured"
  slos:
    - sli_id: ""
      objective: "source-backed target or unset"
      window: "rolling or calendar window"
      current_attainment: "measured value or unmeasured"
      error_budget_remaining: "value with the window it was computed over, or unknown"
      burn_rate: "measured multiple of budget spend, or unmeasured"
      budget_policy: "what exhausting the budget actually changes"
      agreement_state: "agreed_with_owner | proposed | aspirational | unknown"
  dependencies:
    - name: ""
      kind: "internal_service | datastore | cache | queue | third_party | identity | network | dns | infra_control_plane"
      coupling: "hard | soft | degraded_ok"
      observed_availability: "measured value or unmeasured"
      timeout_and_retry: "configured values or unknown"
      blast_radius: "what breaks for the user when this fails"
  failure_modes:
    - id: ""
      trigger: "what starts it"
      propagation: "how it spreads, including correlated and shared-fate paths"
      detection: "signal that catches it today, or undetected"
      mitigation: "action that stops user impact"
      residual_risk: "what remains after the mitigation"
  resilience_controls:
    - control: "timeout | retry_budget | circuit_breaker | bulkhead | load_shed | backpressure | cache_fallback | queue_buffer | replica_failover | idempotency | graceful_degradation"
      applied_at: "caller, service, gateway, client, or infrastructure layer"
      configured_value: "source-backed value or unknown"
      evidence: "load test, chaos experiment, incident, config read, or unproven"
  capacity:
    demand_forecast: "source-backed forecast or unknown"
    current_headroom: "measured headroom against the saturation signal, or unmeasured"
    saturation_signals: []
    scaling_limits: "quota, connection, partition, thread, or licence ceilings"
    provisioning_lead_time: "source-backed lead time or unknown"
    failover_headroom: "whether surviving zones or regions can absorb the load, or unknown"
  load_tests:
    - profile: "load | stress | soak | spike | breakpoint"
      workload_model: "how the traffic mix was derived"
      environment_fidelity: "gaps between the test target and production"
      saturation_point: "measured knee or not reached"
      result: "measured outcome"
      date: "source-backed date"
  chaos_experiments:
    - hypothesis: "steady state expected to hold"
      fault: "what is injected"
      scope: "blast radius and environment"
      abort_criteria: "signal that stops the experiment"
      result: "hypothesis held, disproved, or aborted"
      date: "source-backed date"
  recovery:
    failover_mode: "active_active | active_passive | pilot_light | backup_restore_only | none | unknown"
    rto_target: "source-backed target per tier, or unset"
    rpo_target: "source-backed target per tier, or unset"
    measured_recovery: "result of the last exercise, or never exercised"
    dependency_recovery_order: []
    last_exercise: "date and scope, or never"
  backups:
    - dataset: ""
      mechanism: "snapshot, log shipping, replica, export"
      schedule: "source-backed schedule or unknown"
      retention: "source-backed retention or unknown"
      immutability: "immutable, deletable, or unknown"
      last_restore_test: "date and measured restore time, or never"
      coverage_gap: "what is not backed up"
  alerts:
    - name: ""
      condition: "the actual threshold or burn-rate expression"
      basis: "symptom | cause | burn_rate | synthetic | manual"
      slo_linked: "sli id or none"
      routing: "page | ticket | dashboard_only"
      runbook_ref: "runbook or none"
      signal_quality: "actionable | noisy | never_fired | unproven | unknown"
  runbooks:
    - ref: ""
      covers: "alert, failure mode, or procedure"
      first_mitigation: "the action that stops user impact"
      last_validated: "date, incident use, or never"
      gaps: []
  oncall:
    rotations: []
    escalation_path: "source-backed path or unknown"
    page_load: "pages per shift and out-of-hours share, measured or unmeasured"
    handoff: "how a shift transfers open state, or none"
    coverage_gaps: []
  readiness_gates:
    - gate: ""
      state: "pass | waived | failed | not_assessed"
      evidence: "what established the state"
      owner: "named owner or unknown"
      expiry: "waiver expiry or none"
  change_controls:
    rollout_strategy: "canary | blue_green | rolling | flagged | big_bang | unknown"
    canary_analysis: "what signal decides promotion, or none"
    bake_time: "source-backed observation window or unknown"
    rollback_trigger: "the condition that reverses the change"
    rollback_tested: "date or never"
    freeze_policy: "source-backed policy or unknown"
    change_failure_rate: "measured value or unmeasured"
  incidents:
    - id: ""
      severity: "source-backed severity"
      status: "detected | mitigated | resolved | monitoring"
      detected_at: "source-backed timestamp"
      detection_source: "alert, customer report, dependency, or manual"
      time_to_mitigate: "measured or unmeasured"
      journey_impact: "which journey degraded and how"
      budget_impact: "error budget consumed, or uncomputed"
      commander: "named IC or unassigned"
  postmortem_actions:
    - id: ""
      incident: "incident id"
      action: ""
      class: "prevent | detect | mitigate | process"
      owner: "named owner or unassigned"
      due: "source-backed date or unset"
      state: "open | in_progress | done | dropped"
  toil:
    - task: ""
      trigger: "what causes it"
      frequency: "measured or unmeasured"
      hours_per_week: "measured or unmeasured"
      automatable: "yes | partially | no | unassessed"
      elimination_path: "automation, self-service, or design change"
  reliability_risks:
    - risk: ""
      journeys_affected: []
      exposure: "what the user experiences if it lands"
      current_control: "control that exists today, or none"
      owner: "named owner or unknown"
  source_facts:
    - fact: "source-backed fact"
      source: "metrics | logs | traces | paging_platform | incident_tracker | status_page | deploy_history | config_repo | iac | service_catalog | runbook_repo | postmortem_archive | load_test_report | chaos_platform | backup_system | ticket_queue | docs | user | connector | uploaded_file | unknown"
  decisions:
    - "decision made at this stage"
  assumptions:
    - "assumption made to continue, labeled where it was used"
  open_questions:
    - "question blocking later work"
  artifacts:
    - "artifact name or path"
  halt_conditions:
    - "condition that requires stopping"
  ready_to_continue: true
```

## Stage advancement

Advance when the current desk's output would survive being handed to the next desk without a follow-up round trip. `references/stage-contracts.md` states what each desk requires on input and owns on output.

Run only the stages the target outcome needs. An alert noise review does not need a capacity stage; a backup restore drill does not need a chaos stage. Record every skip in `skipped_stages` with its reason, so a later reader can tell a deliberate skip from an omission.

## Source discipline

Read measured behavior and documented intent from different places and keep them labeled as such.

Measured behavior: the metrics backend, trace store, log pipeline, and synthetic probes state how the system actually behaves. The paging platform states what actually woke someone. The incident tracker, status page, and postmortem archive state what actually broke. Deploy and config history state what actually changed. The backup system and the last restore test state what is actually recoverable. Load test reports and chaos experiment results state what actually held under stress.

Documented intent: SLO documents, architecture and design docs, runbooks, DR plans, readiness checklists, and the service catalog state what the system is supposed to do and who is supposed to own it. Chat threads, incident channels, and meeting notes are decision context and incident narrative, never reliability state.

The gap between the two is usually the finding. An SLO in a document that no query computes, a runbook step that points at a decommissioned dashboard, a DR plan whose failover has never been exercised, and a backup schedule with no dated restore are the recurring shape of this domain. Record both sides, attribute both, and preserve the conflict rather than resolving it into whichever source is more convenient.

Keep source facts separate from assumptions and from inference in every artifact. Never invent service owners, pager rotations, availability or latency figures, error budget balances, burn rates, RTO or RPO values, restore times, incident timestamps, severities, page counts, toil hours, dependency lists, or approval decisions.

## Halt behavior

The default posture is to proceed with the assumption labeled inline. Hard halts are justified by consequence, never by uncertainty, and belong to the six classes in `references/halt-taxonomy.md`. Evidence that is merely absent is a soft gap; evidence that exists and cannot be read is a hard halt.

Recovery and destructive production actions carry an order that is not a stylistic preference. Failover, regional evacuation, restore-over-live-data, snapshot deletion, stateful node replacement, quota reduction, and capacity removal run in this sequence:

1. Establish that the recovery path is proven, using a dated restore or failover result with a measured time, before any action that depends on it.
2. Obtain the named approval for the blast radius, and notify the owners of dependent services and the journeys they carry.
3. Shift or drain traffic and confirm the receiving capacity absorbed it at the current demand, not at an average.
4. Execute the cutover, failover, or deletion.
5. Confirm the user journey against its SLI, then release the freeze and record what actually happened in the packet.

This order is mandated because step 1 is the only evidence that step 4 is survivable, and step 4 is irreversible. Failing over onto an unproven replica, or deleting the snapshot that the restore depends on, converts a recoverable degradation into permanent data loss. Do not compress these steps to save a cycle, and do not reorder them if a future edit makes the list look redundant.

When halting, return:

```markdown
## Workflow Halt

Halt class: <one of the six hard classes>
Current stage: <stage>
Completed stages: <list>
Blocked next stage: <stage>
Consequence if we proceeded: <what would be irreversible, unapproved, exposed, or asserted without evidence>
Missing fact or access: <exact item, named precisely>
Already attempted: <queries run, dashboards read, connectors tried>
Required to resume:
- <specific fact, access grant, or approval, with the owner who can supply it>
Resume prompt:
<copy-paste prompt carrying the current reliability_packet>
```

A halt that only reports being stuck is incomplete. Name the exact query, dashboard, export, permission, or approver that unblocks it.

## Parallel surface

Services, critical user journeys, SLIs, dependencies, failure modes, alert rules, runbooks, backup datasets, load test scenarios, chaos experiments, on-call rotations, and postmortem action items are independent units and are parallel-safe. Connector preflight across the metrics backend, paging platform, incident tracker, deploy history, catalog, and backup system is likewise parallel-safe.

The aggregate work is not parallel and runs once, after the fan-out returns: composing per-service availability along a journey path, rolling error budget up to the journey the user actually experiences, ranking reliability risks, deriving the dependency recovery order, and judging correlated failure across services that share a zone, a cluster, a database, or a control plane. A per-service picture assembled in parallel and never composed along the journey is the classic way this domain produces a dashboard where every service is green while the user cannot complete a purchase.

During an active incident the timeline is single-threaded by nature. Parallel investigation of hypotheses is expected; the timeline, severity, and the record of what was changed reconcile in one place, because two parallel workers each restarting a component produce an incident nobody can reconstruct afterward.

## Cross-suite handoffs

Label cross-suite work explicitly rather than implying those desks belong to this suite. Send software defect triage, hotfix implementation, root cause work that resolves into a code change, issue planning, and implementation handoff to the SDLC suite. Send the internal developer platform itself, its golden paths, and its self-service surfaces to the Platform Engineering suite. Send security incident handling, breach response, and threat modeling to the Security suite. Send cloud spend policy and commitment management to the FinOps suite, audit response and control evidence packaging to the GRC suite, and customer-facing communication policy beyond the status page to the Customer Support suite.

An incident with a security or privacy dimension belongs to both this suite and the Security suite at the same time, and the handoff is additive rather than a transfer of command.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model, including context budget, native self-verification, long-horizon continuation, and parallel fan-out, along with the governance invariants that do not relax as models improve.
