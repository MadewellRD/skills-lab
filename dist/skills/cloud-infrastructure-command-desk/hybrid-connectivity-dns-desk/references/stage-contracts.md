# Cloud Infrastructure Stage Contracts

One entry per desk in the suite: what it requires on input, what it owns on output, and where it hands the `infrastructure_packet`. The orchestrator uses these contracts to route; each member desk uses its own entry as the acceptance boundary for "this stage is done."

## Default sequence

```text
cloud-workload-intake
  -> landing-zone-account-structure
  -> cloud-identity-access
  -> cloud-network-architecture
  -> hybrid-connectivity-dns
  -> compute-platform
  -> container-platform
  -> cloud-storage-data-services
  -> managed-database-platform
  -> resilience-multi-region
  -> infrastructure-as-code
  -> provisioning-pipeline
  -> configuration-secrets
  -> cloud-security-posture
  -> tagging-inventory
  -> cloud-cost-rightsizing
  -> drift-detection-reconciliation
  -> cloud-migration
  -> cloud-decommissioning
```

The chain is ordered by packet dependency, not by calendar. A request that starts mid-chain starts at the earliest desk whose inputs are already satisfied.

## Stage completion rule

Every desk emits: source facts with attribution, decisions, its artifact set, the packet fields it updated, assumptions labeled where they were used, open questions, halt conditions, and next-stage readiness. Unknown values stay unknown in the packet. Identifiers, address ranges, versions, and figures appear only when a source produced them.

---

## cloud-infrastructure-command-desk

- **Requires**: the user request, target outcome, and whatever connector access exists for the IaC repository, state backend, provider inventory, audit log, billing export, and posture tool.
- **Owns**: request classification across surface, blast radius, and change class; stage path selection; packet initialization and carriage; adjudication of declared-versus-live conflicts across stages; the production apply gate; the workflow-level record; and the cross-suite handoff decision.
- **Hands to**: the earliest member desk whose inputs are satisfied, then each successive stage until the target outcome is reached or a hard halt applies.

## cloud-workload-intake-desk

- **Requires**: the request or demand signal, existing architecture and product docs, the compliance and data-classification context, stated recovery expectations, budget envelope, and any provider or region constraint already decided.
- **Owns**: workload framing and criticality tiering, data classification and residency constraints, the recovery objectives the design must meet and whether they are commitments or aspirations, the regulatory regimes in scope, provider and region candidacy, the build-versus-managed-service disposition, and the explicit non-goals that keep the estate from absorbing work it should not.
- **Hands to**: `landing-zone-account-structure-desk`.

## landing-zone-account-structure-desk

- **Requires**: the workload profile with its compliance and residency constraints, the existing organization hierarchy export, current account inventory, and any adopted landing zone pattern.
- **Owns**: the organization, folder, or management-group hierarchy and the isolation rationale behind each boundary; account, subscription, and project separation by environment, sensitivity, and blast radius; the account vending path and what a new account receives on day one; organization-level deny policies with their attachment points; region enablement and restriction; the centralized audit, logging, and backup accounts; and the baseline services every account carries whether or not a team asks for them.
- **Hands to**: `cloud-identity-access-desk`.

## cloud-identity-access-desk

- **Requires**: the account hierarchy and its boundaries, the identity provider and federation state, current role and policy inventory, privileged access records, and applicable separation-of-duties obligations.
- **Owns**: the human access model and federation design, role and permission-set structure with least-privilege scoping, permission boundaries and the interaction between organization-level denies and account-level grants, workload identity that removes static credentials, cross-account trust relationships and their direction, privileged and standing-access findings, the break-glass path with its storage and alerting, and the access review cadence with named reviewers.
- **Hands to**: `cloud-network-architecture-desk`.

## cloud-network-architecture-desk

- **Requires**: the account structure and region set, the existing address allocation register, current network topology export, segmentation and inspection requirements, and the workload connectivity patterns from intake.
- **Owns**: the address plan and allocation register with owner and state per range, virtual network and subnet layout across availability zones, the hub-and-spoke or mesh topology decision with its routing consequences, segmentation and security group or firewall policy structure, the egress model and whether inspection is centralized, private service access and endpoint placement, load balancer and ingress tiers, and the reachability matrix stating which segments may talk to which.
- **Hands to**: `hybrid-connectivity-dns-desk`.

## hybrid-connectivity-dns-desk

- **Requires**: the network topology and address plan, on-premises or partner network facts, existing circuit and tunnel inventory, current DNS zone structure, and the latency and bandwidth expectations from intake.
- **Owns**: dedicated circuit and tunnel design with redundancy and diverse paths, route exchange and failover behavior including what happens when the primary path drops, on-premises address overlap resolution, DNS zone architecture across the hybrid boundary including split-horizon resolution and forwarding rules, certificate and name ownership, content delivery and global traffic distribution where the workload needs it, and the connectivity failure modes with their observable symptoms.
- **Hands to**: `compute-platform-desk`.

## compute-platform-desk

- **Requires**: the workload profile and its performance characteristics, network placement decisions, identity model for workload credentials, and current compute inventory with utilization evidence.
- **Owns**: compute platform selection per workload including virtual machines, autoscaling groups, serverless functions, and managed container runtimes; instance family and size selection with the reason each was chosen; the machine image or runtime lineage and how it is rebuilt; autoscaling triggers, bounds, and cooldowns; the interruptible-capacity mix and what it costs in resilience; placement across failure domains; and the patch and upgrade path including what the provider will force and when.
- **Hands to**: `container-platform-desk`.

## container-platform-desk

- **Requires**: the compute platform decisions, network layout including pod and service address requirements, identity model for workload identity federation, and the current cluster inventory with version and support-window state.
- **Owns**: cluster topology and how many clusters exist for what reason, control plane and node group configuration, node autoscaling and bin-packing strategy, cluster version upgrade cadence against the provider support window, ingress and service exposure, container registry and image provenance, admission control and workload isolation inside a shared cluster, storage class and persistent volume design, and the boundary between cluster-platform ownership and workload-team ownership.
- **Hands to**: `cloud-storage-data-services-desk`.

## cloud-storage-data-services-desk

- **Requires**: the data classification and retention obligations, network private-access decisions, key management expectations, and the current storage inventory with size and access-pattern evidence.
- **Owns**: object, block, and file storage selection per access pattern; bucket, share, and volume layout with access policy; lifecycle and tiering rules with the retrieval cost they imply; versioning, object lock, and immutability where retention obligations require it; encryption with named key ownership; backup destination, frequency, and retention; cross-region copy for durability; public-access blocking and its enforcement point; and the restore path with the date it was last exercised.
- **Hands to**: `managed-database-platform-desk`.

## managed-database-platform-desk

- **Requires**: the workload data model and consistency requirements, recovery objectives from intake, network and private endpoint placement, key management decisions, and the current database inventory with engine versions and end-of-support dates.
- **Owns**: engine and service selection against the access pattern, instance sizing and storage configuration, high-availability topology across failure domains, read replica placement and replication lag expectations, backup and point-in-time recovery windows measured against the stated recovery objectives, parameter and configuration baselines, connection pooling and limits, major version upgrade path against provider end-of-support dates, and encryption plus credential handling for database access.
- **Hands to**: `resilience-multi-region-desk`.

## resilience-multi-region-desk

- **Requires**: the recovery objectives, the full compute, storage, database, network, and identity topology from prior stages, dependency evidence, and current quota values in every candidate recovery location.
- **Owns**: the failure domain model across zones and regions, the failover mode and what it actually costs to run, replication topology and lag budget per data store, dependency analysis including the components that exist in only one location, quota and capacity headroom in the recovery region as a precondition rather than a discovery, the failover and failback runbook with its decision authority, degraded-mode behavior, and the honest split between recovery objectives that have been exercised and objectives that are stated on a page.
- **Hands to**: `infrastructure-as-code-desk`.

## infrastructure-as-code-desk

- **Requires**: the target architecture from the design stages, the existing repository layout and module inventory, state backend configuration, provider version constraints, and evidence of what portion of the estate is currently codified.
- **Owns**: repository and stack layout with the blast radius of each state boundary, module design and the interface each module exposes, module versioning and the upgrade path for consumers, state backend location with locking, encryption, and access control, provider and dependency version pinning, the composition pattern that assembles modules into environments, code-level test and validation gates, the rule that keeps secrets out of state and code, and a measured statement of what share of the estate is under code.
- **Hands to**: `provisioning-pipeline-desk`.

## provisioning-pipeline-desk

- **Requires**: the IaC layout and state boundaries, the identity model for the applying role, guardrail and policy controls that must run against a plan, and the environment promotion expectations.
- **Owns**: the pipeline that turns code into resources, the plan generation and review gate including what a reviewer must see before approving, policy-as-code evaluation against the plan, the approval matrix keyed to blast radius, the least-privileged apply identity and its scope per environment, the rule that the reviewed plan artifact is the one applied, environment promotion and what may differ between environments, concurrency and locking behavior, the sanctioned manual change path and how it is recorded, and the rollback boundary for each stack.
- **Hands to**: `configuration-secrets-desk`.

## configuration-secrets-desk

- **Requires**: the identity model and workload identity decisions, the apply identity from the provisioning pipeline, the data classification from intake, and the current key, secret, and parameter inventory.
- **Owns**: the key hierarchy with scope, ownership, and rotation state; the secret store and access policy per consumer; rotation policy per credential class with what breaks during rotation; replacement of static keys with short-lived credentials; configuration layering and precedence across environments; secret delivery into compute, container, and pipeline surfaces; the state and log exposure review that finds credentials where they should not be; and the remediation path for anything already exposed.
- **Hands to**: `cloud-security-posture-desk`.

## cloud-security-posture-desk

- **Requires**: the deployed topology from prior stages, posture and configuration findings from the scanning tool, guardrail policy state, identity and network evidence, and the benchmark or control framework in force.
- **Owns**: the posture assessment mapped to named benchmark controls, exposure analysis that establishes whether a misconfiguration is actually reachable rather than merely present, public exposure review across storage, compute, database, and network surfaces, encryption and logging coverage, guardrail coverage gaps where a control exists in policy but not at any enforcement point, finding prioritization by exposure path rather than by raw severity, the exception register with named owners and expiry dates, and the remediation plan with the change class each fix belongs to.
- **Hands to**: `tagging-inventory-desk`.

## tagging-inventory-desk

- **Requires**: the account structure, the full resource inventory export, the IaC state and code inventory, the billing export as an independent resource list, and the ownership records that exist today.
- **Owns**: the tag taxonomy and mandatory tag set with the decisions each tag is meant to support, enforcement point selection across code, pipeline policy, and provider tag policy, tag coverage measurement with the untagged share stated as a measured figure, reconciliation between what code declares, what the inventory shows, and what the invoice lists, identification of unmanaged and orphaned resources with the evidence that nothing owns them, the ownership map and its completeness state, and the backfill plan for existing resources that predate the schema.
- **Hands to**: `cloud-cost-rightsizing-desk`.

## cloud-cost-rightsizing-desk

- **Requires**: the tag coverage and ownership map, the billing or cost export at resource granularity, utilization telemetry, commitment and reservation inventory, and the criticality tiers from intake.
- **Owns**: the cost allocation model and what share of spend is allocable given current tag coverage, budget and anomaly thresholds with named recipients, rightsizing candidates with the utilization evidence and the performance risk each carries, commitment and reservation coverage against a stable baseline, storage tiering and retention savings, idle and orphaned resource reclamation with the dependency check that makes deletion safe, unit cost metrics tied to something the business recognizes, and the separation between savings that require a decision and savings that require only an apply.
- **Hands to**: `drift-detection-reconciliation-desk`.

## drift-detection-reconciliation-desk

- **Requires**: the IaC state and code, the live provider inventory, audit and activity log evidence, the manual change path definition, and the guardrail policy set.
- **Owns**: the detection method and cadence that compares declared state to live state, the drift inventory with severity judged by consequence rather than by count, attribution of each drift to its actual origin from audit log evidence, the reconciliation disposition per item across codifying, reverting, adopting, and accepting with reason, the import path for unmanaged resources that should be under code, the systemic finding when drift repeats in the same place because the sanctioned path is too slow, and the guardrail change that prevents recurrence rather than re-fixing the symptom.
- **Hands to**: `cloud-migration-desk`.

## cloud-migration-desk

- **Requires**: the landing foundation from the prior stages, the source estate discovery and dependency evidence, application ownership, data volumes and change rates, and the cutover constraints the business will accept.
- **Owns**: workload discovery and the dependency graph that determines what must move together, disposition per workload across rehost, replatform, refactor, repurchase, retain, and retire, wave sequencing derived from the dependency graph rather than from convenience, landing readiness checks per wave, data migration method and the replication lag that determines the cutover window, the cutover runbook with its rollback boundary and the point past which rollback stops being possible, coexistence and dual-running behavior during the transition, and post-cutover validation criteria including the source-side resources that must not be deleted yet.
- **Hands to**: `cloud-decommissioning-desk`.

## cloud-decommissioning-desk

- **Requires**: the retirement target, dependency and traffic evidence proving what still calls it, retention and legal hold obligations, the approval the blast radius requires, and the backup or archive state.
- **Owns**: the dependent inventory with the evidence used to establish that nothing still needs the target, the announcement and notice window with named owners, the quarantine step that removes access while leaving the resource reversible, data disposition across archive, destroy, and hold with the retention obligation that governs it, the ordered teardown with its irreversible boundary marked, credential revocation and address and name release, account or subscription closure, removal of the corresponding code and pipeline entries so the resource does not reappear, and confirmation that the billing line actually stopped.
- **Hands to**: the orchestrator for workflow close, or back to `cloud-migration-desk` when dependents remain and a migration wave has to run before teardown can advance.

---

## Cross-suite boundary

These stages hand outward rather than to another desk in this suite: formal product requirements, technical discovery, architecture decision records, issue planning, implementation handoff, verification, and release operations go to the SDLC suite; golden paths, service catalog, and self-service developer surfaces built on top of this infrastructure go to the Platform Engineering suite; production incident command, on-call practice, and service-level reliability engineering go to the SRE suite; organization-wide spend policy and commitment portfolio management go to the FinOps suite; audit response and control evidence packaging go to the GRC suite; application threat modeling and detection engineering go to the Security suite. Label the handoff explicitly so nobody reads those desks as members of this one.
