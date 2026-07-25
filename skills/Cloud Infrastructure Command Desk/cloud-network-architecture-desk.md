---
name: cloud-network-architecture-desk
description: design cloud network architecture, covering the address allocation register and cidr planning, virtual network and subnet layout across availability zones, hub-and-spoke or transit topology and its routing consequences, segmentation with security group and firewall policy structure, the egress model and centralized inspection, private service endpoints, load balancer and ingress tiers, and the reachability matrix stating which segments may reach which. use for vpc and vnet design, address planning, subnet sizing, transit routing, microsegmentation, egress inspection, and private endpoint placement.
---

# Cloud Network Architecture Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the network artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Never invent CIDR ranges, IP addresses, subnet masks, virtual network or subnet identifiers, route table entries, security group or firewall rule contents, availability zone names, or endpoint service names.

## Role

Own the address space and what may reach what. This desk maintains the allocation register with owner and state per range, lays out virtual networks and subnets across availability zones, decides the hub-and-spoke or transit topology and states the routing consequences that follow from it, structures segmentation and firewall policy, defines the egress model and whether inspection is centralized, places private service endpoints, sets the load balancer and ingress tiers, and publishes the reachability matrix.

Address space is the one resource in this suite that behaves like a finite shared pool with no runtime error. Two teams can each allocate a range that is free from where they are standing, and nothing fails, no alarm sounds, and the collision stays completely invisible until the day those two networks are peered or the tunnel to the corporate estate comes up. By then both sides are in production and neither can renumber cheaply.

## Use when

- A new virtual network, region, or account needs address space, or the allocation register needs building because allocations currently live in somebody's spreadsheet.
- Subnet layout across availability zones is being designed or resized, including sizing for managed services that consume addresses from the subnet.
- The topology decision is open: peering against a transit hub, single region against multi-region routing, or a flat network being broken into segments.
- Segmentation, security group structure, or firewall policy is being introduced, restructured, or reduced from an accreted rule set.
- The egress model is being decided or changed, including centralizing inspection or moving away from it.
- Private service endpoints are being placed, or traffic to managed services is still traversing public paths.
- The reachability matrix does not exist, or the one that exists does not match what the rules actually permit.

## Do not use when

- The subject is circuits, tunnels, route exchange with an external network, or DNS. That is `hybrid-connectivity-dns-desk`; this desk owns the cloud-side topology up to the boundary, that desk owns crossing it.
- The subject is which accounts exist and what they isolate. That is `landing-zone-account-structure-desk`, whose account set keys the allocation register.
- The subject is pod and service address consumption inside a cluster. That is `container-platform-desk`, which draws from the ranges allocated here and must be given its requirement before allocation closes.
- The subject is benchmark-mapped exposure findings across the estate. That is `cloud-security-posture-desk`.
- The subject is releasing an allocated range or tearing down a network. That is `cloud-decommissioning-desk`, under the destructive sequence.

## Required evidence

- The existing address allocation register or whatever stands in for it, including ranges allocated to on-premises estates, partner networks, and previously decommissioned environments that were never reclaimed.
- The live network inventory: virtual networks, subnets, their CIDRs, their availability zone placement, their free address counts, and the accounts they belong to.
- Route tables with their entries and propagation state, peering relationships, transit attachments, and any route that exists in the table but in no design document.
- Security group, network security group, and firewall policy contents at applied values, plus the rules that reference ranges no longer in use.
- Flow log evidence for what actually communicates, which is the only source that shows whether a permitted path is a used path.
- Private endpoint inventory, the services they front, and the accounts they are shared into.
- Address requirements from the workloads: expected instance and container counts, managed services that place interfaces into a subnet, and the pod and service address demand from the container stage.
- Residency and segmentation obligations from intake, and the account set and region enablement from the landing zone stage.
- Provider constraints that bound the design: minimum and maximum prefix lengths, per-network and per-route-table limits, addresses reserved by the provider in every subnet, and quota on peering or attachments.

## Workflow

**Outcome.** An allocation register with owner and state per range, a virtual network and subnet layout with availability zone placement and sizing rationale, a topology decision with its routing consequences stated, a segmentation and firewall policy structure, an egress model with its inspection point and its failure behavior, private endpoint placement, and a reachability matrix that matches the applied rules rather than the intended ones.

**Grounding.** The register is built from the live inventory plus every external allocation the organization has committed to, including on-premises and partner space, because a range that is free in the cloud inventory and in use on the corporate estate is not free. Reachability is derived from applied rules and corroborated with flow evidence; a matrix drawn from the design document describes an aspiration. Where the design document and the route tables disagree about whether two segments can reach each other, record both and preserve the conflict, since one of those two is what the next firewall change will be reviewed against.

**Constraints.** Every allocated range names its scope, its owner, its state, and the register entry that reserves it, and no range is written into a design until it has been checked against the whole register rather than against the local view. Subnet sizing states its growth assumption and accounts for the addresses the provider reserves in every subnet and for managed services that place their own interfaces into the subnet, which is the reason a nominally adequate subnet exhausts under a service the design never counted. Topology decisions state their routing consequences explicitly, including whether transitivity exists, because peering that is not transitive quietly produces a hub that routes for a set of spokes that cannot reach each other and a design that assumed they could. The egress model names its inspection point, its throughput ceiling, its per-gigabyte cost behavior, and what happens to traffic when the inspection path is unavailable, since a centralized egress that fails closed is an estate-wide outage and one that fails open is a control that is not a control. Segmentation is expressed so that a rule can be traced to the reachability requirement that justifies it, and rules referencing ranges no longer in use are named as reclaimable.

**Parallel surface.** Independent virtual networks, subnets, accounts, regions, security groups, firewall policies, and private endpoints are independent assessment units and fan out safely, as does the per-network read of applied rules and flow evidence. Address allocation is explicitly not part of that fan-out and runs once, after the fan-out returns and against the whole register at once. This is the canonical aggregate in the suite: two workers each carving a range for their own account will both choose something entirely reasonable, both will be locally correct, and the resulting overlap surfaces only when the two networks are joined. The topology decision, the estate-wide reachability matrix, and the egress model are aggregates for the same reason.

**Acceptance bar.** Someone could build a new environment from these artifacts without asking which range to use, and a security reviewer could read the reachability matrix and find it matches the applied rules. Every range in the register is traceable to a source, every subnet has a sizing rationale, and every permitted path in the matrix names the rule that permits it.

## Outputs

A complete run delivers this set:

- `address-allocation-register.md`: every range with scope, owner, state, and source, including external and on-premises allocations, plus the free space remaining and the supernet each allocation is carved from.
- `network-topology.md`: virtual networks, the hub-and-spoke or transit decision, peering and attachment relationships, and the routing consequences including where transitivity does and does not exist.
- `subnet-layout.md`: subnets per network with availability zone placement, tier, size, sizing rationale, growth headroom, and the provider-reserved and managed-service address consumption accounted for.
- `segmentation-and-firewall-policy.md`: the segmentation model, the rule structure, the rules that trace to a stated requirement, and the accreted rules that no longer trace to anything.
- `egress-model.md`: the egress path, the inspection point and its throughput ceiling, cost behavior, and the failure mode when the inspection path is unavailable.
- `private-service-access.md`: endpoints placed, the services they front, the accounts they serve, and the paths that still traverse public routing.
- `reachability-matrix.md`: which segments may reach which, on what ports, derived from applied rules, with flow evidence noted where it corroborates or contradicts.
- `network-downstream-handoff.md`: what `hybrid-connectivity-dns-desk` inherits, including the ranges that will be advertised externally and the overlaps already known.

Depth standard: an artifact is complete when a network engineer could implement from it and a reviewer could audit against it, both without a follow-up round trip. A range with no owner, a subnet with no sizing rationale, and a matrix entry with no rule behind it are unfinished rather than draft.

When the network inventory, route tables, applied rules, or flow logs exist and cannot be read, the run delivers `network-connector-diagnostic.md` naming each unreachable source and the topology or reachability claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: a CIDR block is the most dangerous string this suite produces, because a well-formed range and a free range are typographically identical and the difference only appears months later at a peering. The failure here is filling the register with plausible private space, the tidy sequence of ranges that any competent engineer would pick, when the actual free space was never established. Every range in the register carries the inventory query, export, or register entry that produced it. Where the free space could not be determined, the design states the requirement in prefix length and purpose and leaves the range unassigned, in a form nobody can copy into a module, paired with the query that would resolve it. The same restraint applies to route table entries, security group rules, availability zone names, and endpoint service names: an unallocated placeholder blocks a build for a day, while a fabricated range that reaches production is a renumbering project. A register that honestly reports "on-premises allocations unknown" is safe; one that assumes they do not overlap is the outage.

## infrastructure_packet fields to update

- `network.ipam_plan[]` with `range`, `scope`, `owner`, and `state` per allocation, source-backed only
- `network.topology` and the peering or transit relationships behind it
- `network.segmentation` with the rule structure and the reachability matrix reference
- `network.egress_model` with the inspection point and failure behavior
- `network.private_service_access` with endpoints and the services they front
- `providers[].regions` and `providers[].accounts` confirmed against the network inventory
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would change live routing, apply firewall or security group rules to a running network, delete a peering or attachment, release an allocated range, or move egress through a new inspection path.
- **Source conflict**: the allocation register, the live inventory, and the on-premises or partner address records genuinely disagree about whether a range is free, and choosing one silently would allocate space that is already in use somewhere the cloud inventory cannot see.
- **Security or privacy**: continuing would assert segmentation, private access, or exposure state as verified without applied-rule evidence, or a public path exists to a segment that intake classified as restricted.
- **Missing approval**: a topology change, an egress model change, a range allocation from shared or public space, or a segmentation exception needs a named owner who has not authorized it.
- **Release integrity**: a reachability matrix would be published as the enforced state without being derived from applied rules, or private access declared complete without evidence that no public path remains.
- **Connector unreachable**: the network inventory, route tables, applied rule sets, or flow logs exist and cannot be read. An empty rule set and an unreadable one look identical and mean opposite things, so say which occurred.

Unknown historical rule intent, missing flow history, and undocumented growth projections are soft gaps. Name them, label the assumption, and continue. Range allocation without register evidence, and segmentation obligations that come from a compliance regime, are never relaxed to keep a workflow moving.

## Downstream handoffs

`hybrid-connectivity-dns-desk` is next and needs the allocation register, the ranges that will be advertised externally, the topology, and any known overlap with on-premises space, because overlap resolution is that desk's hardest problem and it starts from this register. `compute-platform-desk` needs subnet placement and availability zone spread. `container-platform-desk` needs the ranges reserved for pod and service addressing, and its consumption must be counted before the register closes. `cloud-storage-data-services-desk` and `managed-database-platform-desk` need endpoint placement and the private paths their services will use. `resilience-multi-region-desk` needs the topology to establish which failure domains are genuinely independent. `cloud-security-posture-desk` inherits the reachability matrix as its exposure baseline. Send adversarial network threat modeling to the Security suite as a labeled cross-suite handoff.

## Quality bar

Good network work is boring in the right places and explicit in the dangerous ones. The register is complete enough that allocating a range is a lookup rather than a conversation, and it includes the space the cloud inventory cannot see. Subnets are sized against a stated growth assumption with the provider's own reservations counted. The topology document says out loud what does not route, because that is the sentence that prevents the design that assumed it did. And the reachability matrix is derived from the rules that are applied, so that when it disagrees with the architecture diagram the disagreement is captured as a finding instead of being resolved in favour of the prettier picture.
