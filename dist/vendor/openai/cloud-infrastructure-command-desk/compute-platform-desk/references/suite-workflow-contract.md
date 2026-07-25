# Cloud Infrastructure Suite Workflow Contract

## Purpose

This reference defines how the Cloud Infrastructure Command Desk suite behaves as one continuous workflow instead of a set of isolated prompts. Every desk in the suite reads it, updates the `infrastructure_packet`, and hands that packet to the next stage.

The subject of this suite is the cloud estate itself: the organization and account hierarchy, the address space, the identity model, the compute and data services, the code that provisions all of it, the pipeline that applies that code, and the live resources that result. Cloud infrastructure has a property most domains do not: the artifacts this suite produces are executable. A CIDR block, a policy statement, a resource identifier, or an engine version written into a document tends to end up inside a module and then inside a live account. The packet therefore carries what is known from live state separately from what is declared in code, because those two things disagree constantly and the disagreement is usually the finding.

## Continuity rule

Do not stop with a bare next-desk recommendation when the next stage can be completed from available source facts. Complete the current stage, update the `infrastructure_packet`, and continue until the target outcome is reached or a hard halt applies.

A stage is complete when the next desk can act on its output without rediscovering scope, identifiers, owners, evidence, or gates. A stage that emitted headings and deferred their contents is incomplete, because every later stage trusts the packet rather than re-reading the provider inventory.

## Operating modes

- `single_stage`: run one desk because the user asked for one specific infrastructure artifact.
- `workflow_run`: default. Run the stage path needed to reach the target outcome, carrying the packet through each stage.
- `resume`: continue from a prior `infrastructure_packet` or a halt-resume prompt, treating the packet's `completed_stages` as done rather than redoing them.
- `halt`: stop on a hard-halt class from `references/halt-taxonomy.md` and emit the halt format below.
- `diagnostic`: the IaC repository, state backend, provider inventory, billing export, posture findings, or telemetry cannot be reached, so the run reports reachability and evidence gaps instead of asserting what the estate contains.

## Infrastructure packet

Every desk preserves and updates this packet. Unknown is a legitimate value; a fabricated value is not. An identifier, address range, version, or figure that no source produced stays unresolved rather than being filled with something well-formed.

```yaml
infrastructure_packet:
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
  infrastructure_surface: "landing_zone | identity | network | connectivity | compute | containers | storage | database | resilience | iac | provisioning | secrets | posture | inventory | cost | drift | migration | decommission | unknown"
  change_class: "greenfield | extension | hardening | remediation | rightsizing | migration | teardown"
  environment_scope: "sandbox | development | test | staging | production | shared_services | all | unknown"
  blast_radius: "single_resource | single_account | single_region | multi_region | organization_wide | unknown"
  providers:
    - provider: "cloud provider as named by the source, or unknown"
      regions: []
      accounts: []            # account, subscription, or project identifiers, source-backed only
      landing_zone_pattern: "source-backed pattern name or unknown"
  workload_profile:
    criticality_tier: "source-backed tier or unknown"
    data_classification: "source-backed classification or unknown"
    compliance_regimes: []
    rto: "source-backed target or unstated"
    rpo: "source-backed target or unstated"
    residency_constraints: []
  organization:
    hierarchy: []             # organizational unit, folder, or management group path
    account_vending: "how accounts are created and by whom, or unknown"
    guardrail_policies:
      - control: ""
        mechanism: "organization deny policy, policy-as-code rule, permission boundary, or provider config rule"
        attachment_point: "root, organizational unit, account, or resource scope"
        mode: "advisory | blocking"
        exception_ref: "waiver id, owner, and expiry, or none"
    baseline_services: []     # audit logging, config recording, backup, threat detection per account
  identity:
    human_access_model: "federated single sign-on, local users, or unknown"
    workload_identity: "how workloads authenticate without static keys, or unknown"
    privileged_roles: []
    permission_boundaries: []
    standing_access_findings: []
    break_glass: "path, storage, and alerting for emergency access, or unknown"
    access_review_cadence: "source-backed cadence or unknown"
  network:
    ipam_plan:
      - range: "allocated CIDR, source-backed only"
        scope: "region, account, environment, or purpose"
        owner: "source-backed owner or unknown"
        state: "allocated | reserved | in_use | reclaimable"
    topology: "hub_spoke | mesh | flat | isolated | unknown"
    segmentation: []
    egress_model: "central inspection, per-account gateway, or unknown"
    private_service_access: []
    dns_zones: []
    hybrid_links:
      - link: "dedicated circuit or tunnel, as named by the source"
        bandwidth: "source-backed or unknown"
        redundancy: "single path, dual path, or unknown"
        routing: "route exchange and failover behavior"
  compute:
    - platform: "vm | autoscaling_group | managed_kubernetes | serverless_function | managed_container_runtime | batch | bare_metal"
      image_or_runtime: "image lineage or runtime version, source-backed"
      sizing: "instance family and size, or unknown"
      scaling_policy: "trigger, bounds, and cooldown, or unknown"
      capacity_model: "on_demand | reserved | interruptible | mixed | unknown"
      upgrade_path: "who patches, on what cadence, and what forces it"
  data_stores:
    - kind: "object | block | file | relational | key_value | document | cache | warehouse | stream"
      engine_and_version: "source-backed, including end-of-support date when the provider publishes one"
      ha_topology: "replica layout and failure domains"
      backup_policy: "frequency, retention, and destination"
      restore_tested: "date of last exercised restore, or never"
      encryption: "key type and who holds it"
      lifecycle_or_tiering: "source-backed rule or none"
  resilience:
    availability_target: "source-backed objective or unstated"
    failure_domains: []
    failover_mode: "active_active | active_passive | pilot_light | backup_restore | none | unknown"
    replication_lag_budget: "source-backed or unknown"
    quota_headroom: []        # limits that must hold in the recovery region, with current values
    last_exercise: "date of last failover test, or never"
  iac:
    approach: "declarative code, provisioning pipeline, or click-ops, as evidenced"
    repo_layout: "stack, workspace, and environment structure"
    state_backend: "location, locking, encryption, and access, or unknown"
    module_versions: []
    coverage: "share of the estate under code, measured or unmeasured"
    test_gates: []            # validation, policy-as-code, plan checks, contract tests
  provisioning:
    pipeline: "how code reaches an account, or unknown"
    plan_review_gate: "who reads the plan and what they must see"
    approval_gates: []
    apply_identity: "the role the pipeline assumes and its scope"
    manual_change_path: "sanctioned out-of-band route, or none"
    environment_promotion: []
  secrets_and_config:
    key_hierarchy: []         # keys, their scope, rotation state, and owner
    secret_store: "source-backed store or unknown"
    rotation_policy: []
    dynamic_credentials: "where short-lived credentials replace static keys"
    config_layers: []
    known_exposure: []        # secrets found in state, images, logs, or code
  posture:
    - finding_id: ""
      control: ""
      benchmark_ref: "named benchmark and control number, source-backed"
      severity: "as scored by the source, not re-scored"
      exposure_path: "how the misconfiguration is actually reachable"
      state: "open | remediated | accepted | false_positive"
      owner: "source-backed owner or unknown"
      exception_expiry: "date or none"
  inventory:
    tag_schema: []
    mandatory_tags: []
    enforcement_point: "code, pipeline policy, provider tag policy, or none"
    untagged_share: "measured value or unmeasured"
    unmanaged_resources: []   # live resources with no code or owner
    ownership_map_state: "complete | partial | absent"
  cost:
    allocation_state: "none | showback | chargeback | unknown"
    budget_envelope: "source-backed figure or unstated"
    committed_coverage: "commitment and reservation coverage, measured or unmeasured"
    rightsizing_candidates: []
    waste_findings: []        # idle, orphaned, oversized, or unattached resources with evidence
    unit_cost_metric: "cost per tenant, request, environment, or unknown"
  drift:
    detection_cadence: "source-backed cadence or none"
    drifted_resources: []
    out_of_band_change_source: "who or what changed it, from audit log evidence"
    reconciliation_policy: "codify | revert | adopt | accept_with_reason"
  migration:
    - workload: ""
      disposition: "rehost | replatform | refactor | repurchase | retain | retire"
      wave: "wave id or unassigned"
      dependencies: []
      data_move_method: "replication, bulk transfer, or dual write"
      cutover_window: "source-backed window or unscheduled"
      rollback_boundary: "the last point at which rollback is still possible"
  decommission:
    - target: "resource, stack, account, or region"
      dependents_checked: "evidence used to establish nothing still calls it"
      data_disposition: "archive, destroy, or hold"
      retention_hold: "legal or regulatory hold, or none"
      teardown_state: "announced | drained | quarantined | deleted | closed"
  source_facts:
    - fact: "source-backed fact"
      source: "iac_repo | state_backend | provider_inventory | audit_log | billing_export | posture_tool | telemetry | dns | ticketing | docs | user | connector | uploaded_file | unknown"
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

Run only the stages the target outcome needs. A rightsizing review does not need a landing zone stage; a new account baseline does not need a migration wave plan. Skipping a stage is recorded in `skipped_stages` with the reason, so a later reader can tell a deliberate skip from an omission.

## Source discipline

Read declared state and live state from different places and keep them labeled as such. This split is the spine of the domain, not a formality.

Declared state: the IaC repository, module definitions, pipeline configuration, policy bundles, architecture decision records, network design documents, and runbooks state what the estate is supposed to be. Ticket queues and change records state what somebody intended to change.

Live state: the provider resource inventory, the IaC state backend, configuration recorders and asset inventories, audit and activity logs, flow logs, DNS zone contents, posture findings, and telemetry state what the estate actually is. The billing export is source of truth for spend and is frequently the only complete inventory of what exists, because a resource nobody codified still appears on the invoice.

Where declared and live disagree, that gap is drift and drift is the finding. Record both sides with attribution, name which source each came from, and do not resolve one into the other. A module that declares an encrypted bucket and an inventory that shows it unencrypted are two facts, not one contradiction to be smoothed over.

Keep source facts separate from assumptions and from inference in every artifact. Never invent account, subscription, project, or resource identifiers; CIDR ranges or IP addresses; region or availability zone names; instance families or sizes; engine or runtime versions; quota limits; key or secret names; policy statement contents; benchmark control numbers; cost figures; tag values; resource owners; recovery objectives; or dates.

## Halt behavior

The default posture is to proceed with the assumption labeled inline. Hard halts are justified by consequence, never by uncertainty, and belong to the six classes in `references/halt-taxonomy.md`. Evidence that is merely absent is a soft gap; evidence that exists and cannot be read is a hard halt.

Irreversible cloud actions carry an order that is not a stylistic preference. Deleting a stateful resource, closing an account or subscription, destroying or migrating a state backend, rotating a trust root or root key, reducing a quota, releasing an address block, and applying a plan that marks a resource for replacement all run in this sequence:

1. Enumerate what will actually change, from the execution plan and the live inventory, separating create from update-in-place from replace from destroy, and identify every dependent of anything in the replace or destroy set.
2. Confirm a restore point exists for the data involved and that its restore path has been exercised, not merely configured.
3. Obtain the named approval the blast radius requires, recorded against this specific plan before anything is applied.
4. Remove traffic and access first through draining, weight shifting, or a deny policy, leaving the resource intact and reversible for a stated observation window.
5. Delete or close.
6. Revoke the credentials, release the addresses and names, and confirm the billing line stops.

This order is mandated because each step produces the evidence that the next one is safe, and step 5 is the point of no return. A cloud delete does not fail loudly when a dependent still needs the resource; it succeeds immediately and fails later, in someone else's outage, without an undo. Approval collected after exposure is not approval. Do not compress these steps to save a cycle, and do not reorder them if a future edit makes the list look redundant.

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
<copy-paste prompt carrying the current infrastructure_packet>
```

A halt that only reports being stuck is incomplete. Name the exact export, permission, plan artifact, or approver that unblocks it.

## Parallel surface

Independent accounts, subscriptions, projects, regions, virtual networks, resource groups, IaC modules and stacks, posture findings, tag violations, drifted resources, cost line items, and migration workloads are independent review units and are parallel-safe. Connector preflight across the IaC repository, state backend, provider inventory, billing export, posture tool, and audit log is likewise parallel-safe.

The aggregate steps are not, and they run once, after the fan-out returns. Address space allocation is the clearest case: two workers each carving a range for their own account will both choose something reasonable and produce a collision that stays invisible until the day the two networks are peered. The same applies to any finite shared pool, including service quotas consumed across parallel provisioning, reserved capacity in a recovery region, and public address blocks. The organization-wide blast radius judgment, the cost and coverage rollup, the migration dependency graph that sequences waves, and the stage-order dependency between desks are also aggregates. A per-account picture assembled in parallel and never reconciled is locally correct and globally wrong.

## Cross-suite handoffs

Label cross-suite work explicitly rather than implying those desks belong to this suite. Send formal product requirements, technical discovery, architecture decision records, issue planning, implementation handoff, verification, and release operations to the SDLC suite. Send the internal developer platform layer built on top of this infrastructure, including golden paths, service catalog, and self-service developer surfaces, to the Platform Engineering suite. Send production incident command, on-call practice, and service-level reliability engineering to the SRE suite. Send organization-wide spend policy, commitment portfolio management, and forecast negotiation to the FinOps suite. Send audit response and control evidence packaging to the GRC suite, and application threat modeling and detection engineering to the Security suite.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model, including context budget, native self-verification, long-horizon continuation, and parallel fan-out, along with the governance invariants that do not relax as models improve.
