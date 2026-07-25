# Platform Engineering Suite Workflow Contract

## Purpose

This reference defines how the Platform Engineering Command Desk suite behaves as one continuous workflow instead of a set of isolated prompts. Every desk in the suite reads it, updates the `platform_packet`, and hands that packet to the next stage.

The subject of this suite is the internal developer platform itself: golden paths, the service catalog, scaffolding templates, platform APIs, self-service infrastructure, environments, the CI/CD platform, guardrails, telemetry, the cost model, and the tenant teams who consume all of it. A platform is a product whose users can walk away to a workaround, so the packet carries consumer state and adoption state, not only design state.

## Continuity rule

Do not stop with a bare next-desk recommendation when the next stage can be completed from available source facts. Complete the current stage, update the `platform_packet`, and continue until the target outcome is reached or a hard halt applies.

A stage is complete when the next desk can act on its output without rediscovering scope, owners, evidence, or gates. A stage that emitted headings and deferred their contents is incomplete, because every later stage trusts the packet rather than re-reading the sources.

## Operating modes

- `single_stage`: run one desk because the user asked for one specific platform artifact.
- `workflow_run`: default. Run the stage path needed to reach the target outcome, carrying the packet through each stage.
- `resume`: continue from a prior `platform_packet` or a halt-resume prompt, treating the packet's `completed_stages` as done rather than redoing them.
- `halt`: stop on a hard-halt class from `references/halt-taxonomy.md` and emit the halt format below.
- `diagnostic`: the catalog, IaC repositories, pipeline definitions, portal, billing export, or telemetry backend cannot be reached, so the run reports reachability and evidence gaps instead of asserting platform state.

## Platform packet

Every desk preserves and updates this packet. Unknown is a legitimate value; a fabricated value is not.

```yaml
platform_packet:
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
  platform_surface: "golden_path | service_catalog | developer_portal | scaffolding | platform_api | self_service_infra | environments | cicd_platform | tenancy | guardrails | observability | slo | cost | adoption | governance | deprecation | unknown"
  platform_maturity: "greenfield | emerging | established | consolidating | unknown"
  consumers:
    - tenant: "team, squad, or business unit id"
      services: []
      onboarding_state: "not_started | piloting | onboarded | migrating | blocked | offboarded | unknown"
      escape_hatches_in_use: []
  developer_personas: []
  jobs_to_be_done: []
  golden_paths:
    - path_id: ""
      stack: "language, framework, runtime, deploy target"
      tier: "paved | supported | escape_hatch | unsupported"
      owner: "source-backed owner or unknown"
      backing_template: "template ref or none"
  catalog_entities:
    - kind: "component | system | api | resource | domain | group | template"
      ref: ""
      owner: "source-backed owner or unknown"
      lifecycle: "experimental | production | deprecated"
      metadata_gaps: []
  platform_apis:
    - name: ""
      version: ""
      stability: "alpha | beta | stable | deprecated"
      compatibility_guarantee: "what a consumer may rely on"
      breaking_change_window: "source-backed policy or unknown"
  abstractions:
    - name: "module, composition, chart, resource claim, or blueprint"
      version: ""
      provisions: "what infrastructure it actually creates"
      drift_state: "reconciled | drifted | unmanaged | unknown"
  templates:
    - ref: ""
      version: ""
      scaffolds: "repo, pipeline, infra, catalog entry, telemetry defaults"
      downstream_drift: "count of generated repos behind this version, or unknown"
  tenancy:
    model: "shared_namespace | namespace_per_tenant | cluster_per_tenant | account_per_tenant | project_per_tenant | unknown"
    isolation_controls: []
    blast_radius_notes: []
    quota_policy: "source-backed policy or unknown"
  environments:
    - name: ""
      class: "ephemeral | preview | integration | staging | production"
      provisioning: "how it is created and by whom"
      lifetime: "ttl, reclamation rule, or unknown"
      parity_gaps: []
  pipeline_surface:
    reusable_workflows: []
    runner_fleet: "hosted, self-hosted, sizes, or unknown"
    caches_and_registries: []
    supply_chain_controls: []
    build_slo: "source-backed target or unknown"
  guardrails:
    - control: ""
      mode: "advisory | blocking"
      enforcement_point: "template, pipeline, admission, provisioning, portal, or runtime"
      exception_ref: "waiver id and owner, or none"
  telemetry_defaults:
    - signal: "logs | metrics | traces | profiles | events"
      instrumentation: "what tenants get without asking"
      routing: "collector, pipeline, backend"
      retention_and_cardinality: "source-backed limits or unknown"
  platform_slos:
    - service: "control plane, pipeline, portal, provisioning API"
      sli: ""
      objective: ""
      window: ""
      error_budget_policy: "what happens when it burns"
      current_state: "measured | unmeasured | unknown"
  devex_metrics:
    - metric: "lead time, deploy frequency, change failure rate, restore time, time to first deploy, onboarding time, provisioning wait, support ticket rate"
      value: "measured value or unmeasured"
      source: "where the number came from"
  cost_model:
    allocation_keys: []
    shared_cost_treatment: "how untagged and platform-owned spend is split"
    reporting_state: "none | showback | chargeback | unknown"
    unit_economics: "cost per service, per environment, per build minute, or unknown"
  adoption:
    onboarded: "count or unknown"
    target_population: "count or unknown"
    migration_waves: []
    holdouts: []
    activation_definition: "what counts as adopted"
  support_load:
    request_classes: []
    toil_notes: []
    escalation_path: "source-backed path or unknown"
  governance:
    decision_forum: "source-backed forum or unknown"
    standards: []
    open_exceptions: []
    approval_gates: []
    funding_or_ownership_model: "source-backed model or unknown"
  deprecations:
    - capability: ""
      replacement: "named successor or none"
      announced: "source-backed date or unknown"
      eol: "source-backed date or unknown"
      consumers_remaining: "count or unknown"
      enforcement_state: "announced | advisory | blocking | removed"
  source_facts:
    - fact: "source-backed fact"
      source: "github | iac_repo | catalog | portal | ci | observability | billing | docs | ticketing | user | connector | uploaded_file | unknown"
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

Advance when the current desk's output would survive being handed to the next desk without a follow-up round trip. Consult `references/stage-contracts.md` for what each desk requires on input and owns on output.

Run only the stages the target outcome needs. A golden-path revision does not need a cost-attribution stage; a chargeback rollout does not need a scaffolding stage. Skipping a stage is recorded in `skipped_stages` with the reason, so a later reader can tell a deliberate skip from an omission.

## Source discipline

Treat the IaC repositories, cluster and control-plane manifests, pipeline definitions, policy bundles, template repositories, and the service catalog export as source of truth for what the platform actually does. Treat the developer portal, platform docs, RFCs, and architecture decision records as source of truth for what the platform intends to do, which is frequently not the same thing. Treat the billing or cost export as source of truth for spend, the telemetry backend as source of truth for platform reliability, and the ticket queue and developer survey as source of truth for consumer experience. Treat chat and meeting notes as decision context, never as platform state.

Where intent and reality disagree, that gap is the finding. Record both, attribute both, and do not resolve one into the other.

Keep source facts separate from assumptions and from inference in every artifact. Never invent tenant names, service owners, catalog entries, module versions, cluster or account IDs, SLO figures, adoption counts, cost numbers, ticket volumes, approval decisions, or deprecation dates.

## Halt behavior

The default posture is to proceed with the assumption labeled inline. Hard halts are justified by consequence, never by uncertainty, and belong to the six classes in `references/halt-taxonomy.md`. Evidence that is merely absent is a soft gap; evidence that exists and cannot be read is a hard halt.

Destructive platform actions carry an order that is not a stylistic preference. Quota reductions, namespace or account teardown, credential and trust-root rotation, cluster deletion, and removal of a platform capability run in this sequence:

1. Inventory the consumers from catalog, telemetry, and pipeline evidence.
2. Notify the named owners with the replacement path and the enforcement dates.
3. Enforce in advisory mode and measure who is still on the old path.
4. Enforce in blocking mode once the remaining consumers are known and accounted for.
5. Tear down.

This order is mandated because each step is the evidence that the next one is safe, and step 5 is irreversible. Running teardown before the inventory strands tenants with no rollback and no owner to call. Do not compress these steps to save a cycle, and do not reorder them if a future edit makes the list look redundant.

When halting, return:

```markdown
## Workflow Halt

Halt class: <one of the six hard classes>
Current stage: <stage>
Completed stages: <list>
Blocked next stage: <stage>
Consequence if we proceeded: <what would be irreversible, unapproved, exposed, or unverifiable>
Missing fact or access: <exact item, named precisely>
Already attempted: <sources read, queries run, connectors tried>
Required to resume:
- <specific fact, access grant, or approval, with the owner who can supply it>
Resume prompt:
<copy-paste prompt carrying the current platform_packet>
```

A halt that only reports being stuck is incomplete. Name the exact artifact, export, permission, or approver that unblocks it.

## Parallel surface

Independent tenants, services, catalog entities, IaC modules, templates, pipelines, environments, policy rules, and cost allocation keys are independent review units and are parallel-safe. Connector preflight across the catalog, repositories, CI, telemetry, and billing is likewise parallel-safe.

The aggregate steps are not: the rollup that ranks findings, the adoption or coverage total computed across tenants, the cross-tenant blast-radius judgment, and the stage-order dependency between desks all run once, after the fan-out returns. A per-tenant view assembled in parallel and never reconciled produces a platform picture that is locally correct and globally wrong.

## Cross-suite handoffs

Label cross-suite work explicitly rather than implying those desks belong to this suite. Send generic lifecycle work such as formal product requirements, technical discovery, architecture decision records, issue planning, implementation handoff, verification, and release operations to the SDLC suite. Send production incident command, on-call practice, and deep reliability engineering for tenant workloads to the SRE suite. Send organization-wide cloud spend policy to the FinOps suite, control evidence and audit response to the GRC suite, and threat modeling of the platform's own attack surface to the Security suite.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model, including context budget, native self-verification, long-horizon continuation, and parallel fan-out, along with the governance invariants that do not relax as models improve.
