# Platform Engineering Stage Contracts

One entry per desk in the suite: what it requires on input, what it owns on output, and where it hands the `platform_packet`. The orchestrator uses these contracts to route; each member desk uses its own entry as the acceptance boundary for "this stage is done."

## Default sequence

```text
platform-product-intake
  -> developer-experience-research
  -> golden-path-design
  -> service-catalog
  -> platform-api-contract
  -> tenancy-isolation
  -> self-service-infrastructure
  -> scaffolding-templates
  -> environment-management
  -> cicd-platform
  -> platform-guardrails-policy
  -> platform-observability
  -> platform-slo-reliability
  -> platform-cost-attribution
  -> platform-change-rollout
  -> platform-adoption-migration
  -> platform-support-operations
  -> platform-governance
  -> platform-deprecation-sunset
```

The chain is ordered by packet dependency, not by calendar. A request that starts mid-chain starts at the earliest desk whose inputs are already satisfied.

## Stage completion rule

Every desk emits: source facts with attribution, decisions, its artifact set, the packet fields it updated, assumptions labeled where they were used, open questions, halt conditions, and next-stage readiness. Unknown values stay unknown in the packet.

---

## platform-engineering-command-desk

- **Requires**: the user request, target outcome, and whatever connector access exists for catalog, repositories, CI, telemetry, billing, and portal.
- **Owns**: request classification, stage path selection, packet initialization and carriage, cross-stage conflict adjudication, the workflow-level record, and the cross-suite handoff decision.
- **Hands to**: the earliest member desk whose inputs are satisfied, then each successive stage until the target outcome is reached or a hard halt applies.

## platform-product-intake-desk

- **Requires**: the request or demand signal, existing platform docs and roadmap, prior RFCs, current capability inventory, and any stated funding or headcount constraint.
- **Owns**: platform-as-a-product framing, demand intake and triage, developer personas and jobs-to-be-done, the build-versus-buy-versus-adopt disposition, capability scope and non-goals, and the success measure the capability will be judged on.
- **Hands to**: `developer-experience-research-desk`.

## developer-experience-research-desk

- **Requires**: the intake framing, access to ticket queues, survey results, pipeline and deploy telemetry, onboarding records, and the current toolchain inventory.
- **Owns**: the friction map across the developer journey, cognitive load assessment, delivery and experience baselines (lead time, deploy frequency, change failure rate, restore time, time to first deploy, provisioning wait, onboarding time), the measured-versus-unmeasured split, and the prioritized friction list the platform will address.
- **Hands to**: `golden-path-design-desk`.

## golden-path-design-desk

- **Requires**: personas and jobs-to-be-done, the friction map, the existing stack inventory, and the organization's supported technology constraints.
- **Owns**: golden path definitions by stack, path tiering (paved, supported, escape hatch, unsupported), opinionated defaults and what each default buys the developer, the escape-hatch policy and its support boundary, and the supported matrix a platform team commits to maintain.
- **Hands to**: `service-catalog-desk`.

## service-catalog-desk

- **Requires**: the golden path tiers, repository and deployment inventory, ownership records, and any existing catalog or registry export.
- **Owns**: the catalog entity model and kind definitions, ownership and lifecycle metadata, registration and ingestion mechanics, metadata quality and freshness rules, scorecard definitions, and the portal surface through which developers discover and act on catalog entities.
- **Hands to**: `platform-api-contract-desk`.

## platform-api-contract-desk

- **Requires**: golden path definitions, catalog entity kinds, existing platform interfaces (APIs, custom resources, CLI verbs, portal actions), and current consumer usage.
- **Owns**: the platform's own interface contracts and resource schemas, versioning and stability labels, backward-compatibility guarantees, the breaking-change window and notification policy, client and CLI surface, and the abstraction boundary that says what the platform hides and what it deliberately exposes.
- **Hands to**: `tenancy-isolation-desk`.

## tenancy-isolation-desk

- **Requires**: the platform API contracts, consumer inventory, regulatory and data-residency constraints, and the current cluster, account, or project topology.
- **Owns**: the tenancy model, isolation controls (namespace and account boundaries, RBAC, workload identity, network policy, node and runtime separation), quota and fair-share policy, noisy-neighbor mitigation, and the documented blast radius of each shared component.
- **Hands to**: `self-service-infrastructure-desk`.

## self-service-infrastructure-desk

- **Requires**: the tenancy model and isolation controls, platform API contracts, existing IaC modules and compositions, and the provisioning path in use today.
- **Owns**: infrastructure abstractions and reusable modules, the provisioning and reconciliation path, request-to-resource latency expectations, state and drift handling, quota enforcement at provisioning time, and the day-two operations a tenant can perform without a ticket.
- **Hands to**: `scaffolding-templates-desk`.

## scaffolding-templates-desk

- **Requires**: golden path definitions, platform API contracts, infrastructure abstractions, catalog registration mechanics, and telemetry and guardrail defaults that templates must wire in.
- **Owns**: software templates and repository scaffolding, what a generated repository contains on day one, template versioning, the renovation path that keeps generated repositories current, ownership of generated code after handoff, and template drift measurement across the generated fleet.
- **Hands to**: `environment-management-desk`.

## environment-management-desk

- **Requires**: infrastructure abstractions, tenancy model, template outputs, and the current environment topology with its data and secret sources.
- **Owns**: environment classes and topology, ephemeral and preview environment provisioning, promotion path between classes, test-data seeding and masking, lifetime and reclamation rules, and the parity gaps between each lower environment and production.
- **Hands to**: `cicd-platform-desk`.

## cicd-platform-desk

- **Requires**: environment topology and promotion path, template-generated pipeline definitions, artifact and registry inventory, and current build and deploy telemetry.
- **Owns**: reusable pipeline and workflow definitions, runner fleet sizing and isolation, cache and artifact strategy, registry and dependency proxy layout, supply-chain controls (provenance, attestation, signing, bill of materials), build and queue performance targets, and the boundary between platform-owned pipeline stages and tenant-owned ones.
- **Hands to**: `platform-guardrails-policy-desk`.

## platform-guardrails-policy-desk

- **Requires**: pipeline and provisioning enforcement points, tenancy and isolation controls, applicable compliance obligations, and the current policy bundle and exception register.
- **Owns**: policy-as-code rules with their enforcement point, the advisory-versus-blocking decision per control, secret and credential defaults, the exception and waiver flow with named owners and expiry, and the rollout path that moves a control from advisory to blocking without stalling delivery.
- **Hands to**: `platform-observability-desk`.

## platform-observability-desk

- **Requires**: template and pipeline injection points, tenancy boundaries, existing telemetry backends and agents, and current signal volume and spend.
- **Owns**: the instrumentation baseline every tenant receives by default, the telemetry pipeline and routing, signal schema and naming conventions, cardinality and retention limits with their cost consequence, tenant-scoped dashboards and access, and the coverage gaps where the platform is blind to its own consumers.
- **Hands to**: `platform-slo-reliability-desk`.

## platform-slo-reliability-desk

- **Requires**: the telemetry baseline and its measurement state, the platform component inventory, dependency map, and current incident and outage history.
- **Owns**: platform SLIs and SLOs for control plane, provisioning, pipelines, registries, and portal; error budget policy and what burning it changes; dependency and single-point-of-failure analysis; degradation modes when a platform component fails; and the honest split between objectives that are measured and objectives that are aspirational.
- **Hands to**: `platform-cost-attribution-desk`.

## platform-cost-attribution-desk

- **Requires**: the tenancy model and allocation boundaries, billing or cost export, tagging and labeling state, and the platform's own operating cost.
- **Owns**: the allocation model and keys, treatment of shared and untagged spend, showback or chargeback design and its behavioral consequences, unit economics per service, environment, and build minute, waste and idle reclamation targets, and the reporting cadence tenants can act on.
- **Hands to**: `platform-change-rollout-desk`.

## platform-change-rollout-desk

- **Requires**: the change being shipped, the consumer inventory that depends on it, compatibility guarantees from the API contract stage, and the SLO and error budget state.
- **Owns**: tenant ring definitions and the promotion criteria between rings, the breaking-versus-additive classification for each change, control-plane and cluster upgrade sequencing, rollback and pause criteria, tenant-facing change notice, and the freeze or exception path for tenants who cannot absorb the change on schedule.
- **Hands to**: `platform-adoption-migration-desk`.

## platform-adoption-migration-desk

- **Requires**: golden path tiers and their backing capabilities, the consumer inventory with onboarding state, migration effort evidence, and the activation definition.
- **Owns**: the adoption funnel and activation definition, migration wave sequencing with named cohorts, onboarding and enablement material, the incentive and support model that moves holdouts, migration debt tracking, and the escape-hatch usage that signals a golden path is not actually paved.
- **Hands to**: `platform-support-operations-desk`.

## platform-support-operations-desk

- **Requires**: adoption state, the request history and ticket queue, runbook inventory, and platform SLO and error budget state.
- **Owns**: the support model and rotation, request class taxonomy with routing, self-service deflection targets, runbooks for the platform's own failure modes, escalation path and response expectations, toil accounting, and the feedback loop that turns repeat requests into platform capability rather than repeat answers.
- **Hands to**: `platform-governance-desk`.

## platform-governance-desk

- **Requires**: the standards and defaults produced upstream, the open exception register, scorecard data, ownership records, and the funding or staffing model.
- **Owns**: decision rights and the forum that exercises them, the RFC and architecture-decision path, standard tiers and how a standard becomes mandatory, scorecard thresholds and their consequences, exception review with expiry enforcement, ownership and funding model, and the audit-ready evidence trail for platform-enforced controls.
- **Hands to**: `platform-deprecation-sunset-desk`.

## platform-deprecation-sunset-desk

- **Requires**: the capability being retired, its consumer inventory from catalog and telemetry evidence, the named replacement path, and the governance approval for the retirement.
- **Owns**: the deprecation policy and notice windows, consumer inventory with remaining-user counts, the replacement and migration path, the enforcement ladder from announced to advisory to blocking to removed, communication plan by owner, and the teardown and data-retention plan with its rollback boundary.
- **Hands to**: the orchestrator for workflow close, or back to `platform-adoption-migration-desk` when remaining consumers need a migration wave before enforcement can advance.

---

## Cross-suite boundary

These stages hand outward rather than to another desk in this suite: formal product requirements, technical discovery, architecture decision records, issue planning, implementation handoff, and release operations go to the SDLC suite; tenant-workload incident command and on-call practice go to the SRE suite; organization-wide cloud spend policy goes to the FinOps suite; audit response and control evidence go to the GRC suite; threat modeling of the platform's own attack surface goes to the Security suite. Label the handoff explicitly so nobody reads those desks as members of this one.
