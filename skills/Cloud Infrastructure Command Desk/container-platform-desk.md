---
name: container-platform-desk
description: design the managed kubernetes and container platform, covering cluster topology and how many clusters exist for what reason, control plane and node group configuration, node autoscaling and bin packing with requests limits and disruption budgets, cluster version upgrades against the provider support window and removed apis, ingress and service exposure, container registry and image provenance, admission control and in-cluster isolation, storage classes, and the platform-versus-workload ownership boundary. use for cluster design, node pool sizing, cluster upgrade planning, ingress architecture, registry and image signing, and multi-tenancy inside a cluster.
---

# Container Platform Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the container platform artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Never invent cluster names or identifiers, control plane or node versions, support window end dates, node pool names, image digests or tags, registry paths, admission policy contents, address ranges for pods and services, or quota values.

## Role

Own the orchestrator and the boundary around it. This desk decides cluster topology and how many clusters exist for what reason, configures the control plane and node groups, sets node autoscaling and bin packing, plans version upgrades against the provider support window, designs ingress and service exposure, governs the registry and image provenance, defines admission control and isolation inside a shared cluster, selects storage classes, and draws the line between what the platform team owns and what a workload team owns.

Two forces pull in opposite directions here and every real decision sits between them. Fewer clusters means lower operational load and better bin packing, and it also means a control plane incident is an estate-wide outage. More clusters means smaller blast radius, and it also means an upgrade programme that nobody finishes, which ends with a fleet spread across four versions where two are out of support. Cluster count is a blast-radius-against-upgrade-capacity decision, and stating which side the organization chose is more useful than the number itself.

## Use when

- Cluster topology is being decided or revisited, including cluster count, per-environment against per-tenant separation, and regional spread.
- Node groups are being designed or resized, including instance diversity, taints and labels, and the interruptible portion.
- Node autoscaling or bin packing needs work: unschedulable pods, low packing density, scale-down blocked by workloads that cannot be evicted.
- A cluster version upgrade is due, overdue, or approaching the end of its support window, or removed APIs need finding before the control plane moves.
- Ingress and service exposure is being designed, consolidated, or moved between controller types.
- The registry, image provenance, signing, or admission of unsigned images needs defining.
- Isolation inside a shared cluster needs designing: namespaces, network policy, admission enforcement, and resource quota between teams.
- The ownership boundary is unclear and platform and workload teams are each assuming the other owns something.

## Do not use when

- The subject is the machines, images, and capacity model underneath the cluster. That is `compute-platform-desk`, whose node capacity model and image lineage this desk consumes.
- The subject is the cloud-side address plan the cluster draws pod and service ranges from. That is `cloud-network-architecture-desk`; supply the pod and service address requirement to that desk before its register closes.
- The subject is golden paths, service catalogue, scaffolding, or the developer self-service surface built on this cluster. That is a labeled cross-suite handoff to the Platform Engineering suite.
- The subject is benchmark-mapped posture findings across the estate. That is `cloud-security-posture-desk`.
- The subject is the database or object store the workload talks to. Those are `managed-database-platform-desk` and `cloud-storage-data-services-desk`.

## Required evidence

- The cluster inventory: clusters, their control plane versions, their regions and accounts, their creation dates, and the workloads on each.
- The provider support window for each version in use, with the end date as published, plus any extended-support billing already in effect.
- API deprecation and removal information for the versions being moved between, and the current usage of any API scheduled for removal, read from the cluster rather than from the manifests in a repository.
- Node group configuration: instance types, sizes, counts, minimum and maximum bounds, taints, labels, the interruptible portion, and the node image version and its patch state.
- Scheduling state: resource requests and limits as actually set on workloads, pod disruption budgets, priority classes, topology spread constraints, and the pending-pod and packing-density history.
- Address consumption: the pod and service ranges in use, the addressing mode, the maximum pods per node in force, and the remaining free addresses in the ranges the cluster draws from.
- Ingress configuration: controllers, load balancer objects created, listener and certificate bindings, and the names each fronts.
- Registry state: registries in use, image provenance and signing configuration, mutable tag usage, admission enforcement of signature or digest requirements, and the vulnerability scan state.
- Admission and isolation state: policy bundles, their failure policy, pod security enforcement level per namespace, network policy objects, and resource quotas.
- Storage classes, their provisioners, reclaim policies, volume expansion support, and the persistent volumes in use.

## Workflow

**Outcome.** A cluster topology with the blast-radius reasoning behind the count, node group configuration with its capacity and diversity model, autoscaling and bin packing settings tied to observed scheduling behavior, an upgrade plan measured against the support window and the removed APIs actually in use, ingress and exposure design, registry and provenance rules with their enforcement point, in-cluster isolation, storage classes, and a written ownership boundary.

**Grounding.** Version and support state comes from the cluster and the provider's published calendar, not from the version a repository declares. API usage that a coming version removes is established from live cluster request data where it exists, because a manifest search finds only what is in the repository and misses the operator, the controller, and the tool that call the same removed API from somewhere else. Isolation and provenance are read from applied policy objects and admission configuration; a signing requirement present in a design and absent from admission blocks nothing. Where the declared node group configuration and the running nodes disagree, record both and preserve the conflict.

**Constraints.** Cluster count states the reason: the blast radius each boundary contains, the upgrade capacity the organization actually has, and the isolation requirement that could not be met inside a shared cluster. Node group design states instance diversity, since a single instance type across a node group turns one capacity shortage into an unschedulable cluster, and it states the interruptible portion with the eviction behavior that follows. Bin packing is assessed against requests as actually set, because packing density is a function of requests rather than of usage and the gap between them is where the money goes. Scale-down behavior names what blocks it, since a workload without a disruption budget and a workload that cannot be evicted look identical to a node autoscaler and only one of them is a bug. Address consumption is stated in absolute addresses, not in node counts, and it is handed to the network stage before the allocation register closes, because pod-per-address modes consume the subnet at a rate the address plan rarely anticipated. Ingress states what terminates connections, where certificates come from, and what a controller failure removes. Provenance rules name their enforcement point and their failure policy, and a mutable tag in a production workload is recorded as an unversioned deployment rather than as a convention. The ownership boundary is written as a two-column statement so that no object type is owned by both teams or by neither.

**Parallel surface.** Independent clusters, node groups, namespaces, workloads, storage classes, and policy objects are independent assessment units and fan out safely, as does the per-cluster read of version and configuration state. The fleet-wide upgrade sequence, the aggregate address consumption against the ranges available, the cross-cluster blast radius judgment, and the estate-level support window position run once after the fan-out returns, because a per-cluster upgrade plan cannot see that all of them depend on one shared registry or that their combined pod ranges exceed what the address register has left.

**Ordered gate for a cluster version upgrade.** A managed control plane upgrade is one-way, nodes newer than their control plane are unsupported, and an API removed in the target version stops serving the moment the control plane moves. That is why this order is mandated and why step 3 is the point past which the only recovery is a rebuild:

1. Establish the target version's removed and deprecated APIs and find their live usage from cluster request data, including usage by operators, controllers, and tooling rather than only by workload manifests.
2. Remediate that usage and confirm workloads carry disruption budgets that permit a rolling node replacement without taking the service below its minimum.
3. Upgrade the control plane, which cannot be rolled back, then verify the cluster serves before touching nodes.
4. Upgrade node groups behind the control plane version, draining rather than terminating, then bring addons and controllers to their compatible versions.

Cluster deletion, node group teardown, and namespace removal follow the destructive sequence in `references/suite-workflow-contract.md` instead of this one.

**Acceptance bar.** A platform engineer could operate the fleet from these artifacts and a workload team could tell exactly what it owns. Every cluster's support position is a dated statement, every removed API in the upgrade path has a live-usage finding attached, address consumption is stated in addresses, and every provenance rule names its enforcement point.

## Outputs

A complete run delivers this set:

- `cluster-topology.md`: the clusters, the reason each boundary exists, the blast radius each contains, and the upgrade capacity that justifies the count.
- `node-group-design.md`: node groups with instance diversity, bounds, taints and labels, node image version, the interruptible portion, and the eviction behavior it implies.
- `scheduling-and-binpacking.md`: requests and limits practice, disruption budgets, priority classes, spread constraints, observed packing density, and what currently blocks scale-down.
- `cluster-upgrade-plan.md`: current versions against the published support window with dates, removed APIs with their live usage findings, the upgrade sequence, and the extended-support exposure.
- `address-consumption.md`: pod and service range usage in absolute addresses, maximum pods per node, remaining headroom, and the requirement handed back to the network stage.
- `ingress-and-exposure.md`: controllers, listeners, certificate bindings, the names each fronts, and what a controller failure removes.
- `registry-and-image-provenance.md`: registries, signing and attestation requirements, the admission enforcement point and its failure policy, mutable tag usage, and scan state.
- `in-cluster-isolation.md`: namespace boundaries, network policy posture, pod security enforcement level per namespace, resource quotas, and the admission policy failure behavior.
- `ownership-boundary.md`: a two-column statement of what the platform team owns and what the workload team owns, with no object type unowned or doubly owned.
- `container-downstream-handoff.md`: what `cloud-storage-data-services-desk` and the resilience stage inherit, including persistent volume behavior and cluster failure domains.

Depth standard: an artifact is complete when a platform engineer could act on it and a workload owner could plan against it, both unchanged. A cluster with no dated support position, an upgrade plan with no removed-API finding, and an isolation control with no enforcement point are unfinished rather than draft.

When the cluster configuration, applied policy objects, registry state, or provider support calendar exists and cannot be read, the run delivers `container-connector-diagnostic.md` naming each unreachable source and the version, isolation, or provenance claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: cluster versions and their support end dates are the fabrication hazard specific to this desk, because version strings are formulaic and support windows follow a rhythm regular enough to extrapolate. Writing a plausible end-of-support date turns a real deadline into a fictional one in both directions: an invented date that is later than the truth ends with a fleet dropped out of support and silently billed for extended support, and one that is earlier burns a quarter of engineering time on an emergency that was not due. Versions, support end dates, and extended-support status are quoted from the cluster and the provider's published calendar, or recorded as unconfirmed with the calendar that would settle it. The related trap is the removed-API check performed against a repository and reported as an upgrade readiness result: manifests in a repository are not the set of API callers, so an upgrade readiness statement built only from them is recorded as partial, naming the caller classes that were not inspected. Cluster identifiers, node pool names, image digests, and policy contents are transcribed or left unresolved.

## infrastructure_packet fields to update

- `compute[]` entries with `platform: managed_kubernetes`, including control plane and node versions, sizing, scaling policy, capacity model, and the upgrade path with its support window dates
- `network.ipam_plan[]` updated with the pod and service ranges consumed, in absolute addresses
- `network.private_service_access` and `network.segmentation` where ingress and network policy change reachability
- `organization.guardrail_policies[]` for admission and provenance controls with their attachment point and mode
- `resilience.failure_domains` extended with cluster and control plane boundaries
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would upgrade a live control plane, replace or drain node groups, apply admission policy in blocking mode, change ingress bindings, or delete a cluster or namespace.
- **Release integrity**: an upgrade would proceed without the removed-API usage established from live cluster data, or a cluster would be declared within its support window without the published date behind it.
- **Security or privacy**: continuing would assert image provenance, admission enforcement, network policy, or namespace isolation as verified without applied-configuration evidence, or an unsigned or unattested image is running in a regulated namespace.
- **Missing approval**: a cluster upgrade window, a topology change, a move of admission policy to blocking, or acceptance of extended-support billing needs a named owner who has not authorized it.
- **Source conflict**: the cluster state, the declared configuration, and the registry or policy inventory genuinely disagree about versions, images, or enforcement, and choosing one silently would publish a readiness claim that does not hold.
- **Connector unreachable**: the cluster API, applied policy objects, registry, or provider support calendar exists and cannot be read.

Unknown historical node group intent, missing packing density history, and undocumented workload ownership are soft gaps. Name them, label the assumption, and continue. Support window obligations, image provenance requirements, and upgrade approval are never relaxed to keep a workflow moving.

## Downstream handoffs

`cloud-storage-data-services-desk` is next and needs the storage class design, the persistent volume behavior including reclaim policy, and the backup expectation for stateful workloads in the cluster. `managed-database-platform-desk` needs the connection pattern and the workload identity path clusters use to reach databases. `resilience-multi-region-desk` inherits the cluster and control plane failure domains and the recovery-region node quota the failover would consume. `cloud-network-architecture-desk` receives the pod and service address consumption as a register update. `cloud-security-posture-desk` inherits admission gaps, unsigned image findings, and namespace isolation state. `infrastructure-as-code-desk` needs the cluster and node group definitions to bring under code. Send golden paths, service catalogue, and developer self-service surfaces to the Platform Engineering suite as a labeled cross-suite handoff.

## Quality bar

Good container platform work is honest about the trade it made. It states why there are three clusters rather than one or thirty, and it names the upgrade capacity that number assumes. The support window position is a date, not a feeling. Address consumption is counted in addresses and handed back to the address register before it closes, because pod addressing is the single most common way a cloud address plan runs out early. Provenance is described at the admission point that enforces it rather than at the policy that requests it. And the ownership boundary is specific enough to settle an argument at two in the morning about whether the platform team or the workload team owns the thing that is currently down.
