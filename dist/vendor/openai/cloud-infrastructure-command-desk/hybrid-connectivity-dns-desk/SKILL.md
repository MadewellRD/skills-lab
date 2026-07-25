---
name: hybrid-connectivity-dns-desk
description: design hybrid connectivity and dns, covering dedicated circuits and encrypted tunnels with genuinely diverse redundant paths, bgp route exchange and failover behavior including degraded-bandwidth backup, on-premises address overlap resolution, dns zone architecture across the hybrid boundary with split-horizon resolution forwarders and resolver endpoints, certificate ownership and renewal, and global traffic distribution with health checks and ttl behavior. use for direct circuit design, vpn failover, bgp routing, hybrid dns, split-horizon zones, certificate lifecycle, and latency or geo traffic steering.
---

# Hybrid Connectivity DNS Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the connectivity artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Never invent circuit identifiers, virtual interface or VLAN tags, autonomous system numbers, advertised prefixes, peer addresses, colocation facility names, bandwidth figures, DNS record contents, zone names, resolver endpoint addresses, certificate authorities, or expiry dates.

## Role

Own the boundary crossing. This desk designs dedicated circuits and encrypted tunnels with their redundancy, the route exchange between the cloud estate and everything outside it including what happens when the primary path drops, the resolution of on-premises address overlap, the DNS zone architecture across the hybrid boundary including split-horizon views, forwarding, and resolver placement, certificate and name ownership, global traffic distribution where the workload needs it, and the connectivity failure modes with the symptoms an operator will actually observe.

Two things make hybrid connectivity fail in ways the diagram never shows. Redundancy claims are about physical facts, not about counts: two circuits terminating in the same building, riding the same conduit, or bought from the same carrier are one circuit with two invoices. And failover is about capacity, not reachability: a backup tunnel that comes up in thirty seconds and carries a fraction of the primary's throughput has succeeded by every health check and failed by every user.

## Use when

- A dedicated circuit or encrypted tunnel is being ordered, designed, replaced, or reviewed for genuine path diversity.
- Route exchange is being designed or debugged: prefix advertisement, path preference, prefix limits, failure detection timing, or asymmetric routing through an inspection path.
- On-premises or acquired-company address space overlaps the cloud estate and the overlap has to be resolved rather than tolerated.
- DNS across the hybrid boundary is being designed or is misbehaving: split-horizon views, conditional forwarding, resolver endpoint placement, zone delegation, or queries leaving the private path.
- Certificate ownership, renewal automation, or an expiry with no named owner needs settling.
- Global traffic distribution is being introduced: latency, geographic, or weighted steering, health checks, and the TTL behavior that decides how fast a failover is actually observed.
- Connectivity failure modes need documenting with the symptoms an on-call engineer will see.

## Do not use when

- The subject is cloud-side address allocation, subnet layout, segmentation, or the internal reachability matrix. That is `cloud-network-architecture-desk`, whose register this desk consumes.
- The subject is which accounts exist and what regions are enabled. That is `landing-zone-account-structure-desk`.
- The subject is regional failover mode, replication topology, and recovery objectives. That is `resilience-multi-region-desk`; this desk supplies the resolution and steering mechanics that failover depends on.
- The subject is cluster ingress, service exposure inside a cluster, or gateway routing. That is `container-platform-desk`.
- The subject is application-layer content delivery strategy or edge compute logic. That is a labeled cross-suite handoff to the Web or Platform Engineering suites.

## Required evidence

- The circuit and tunnel inventory: each link with its provider, bandwidth, termination facility, the virtual interfaces or connections on it, and its current operational state.
- Physical diversity evidence: the facilities, cross-connects, carriers, and last-mile paths behind each link, which is the only basis on which redundancy can be claimed.
- Routing state: autonomous system numbers, advertised and received prefixes, prefix counts against the limits in force, path preference settings, failure detection timers, and the current session state per peer.
- The on-premises and partner address inventory, including anything that overlaps the cloud allocation register from the network stage.
- DNS state: zones and their authority, private and public views, record contents, forwarding and conditional forwarding rules, resolver endpoint placement, query logs where they exist, and the TTLs actually in force.
- Certificate inventory: subject names, issuers, expiry dates, renewal mechanism, and the named owner of each.
- Global traffic distribution configuration where it exists: steering policy, health check definitions and their evaluation points, and record TTLs.
- Latency and bandwidth expectations from intake, and the topology and allocation register from the network stage.
- Historical connectivity incidents, which are the most reliable source for what actually breaks.

## Workflow

**Outcome.** A connectivity design in which every redundancy claim rests on physical diversity evidence, failover behavior is stated in both reachability and capacity terms, address overlap has a resolution rather than a note, DNS resolution is described as an end-to-end path for each client population, certificates have named owners with automated renewal or a stated reason they do not, and the failure modes are written with their observable symptoms.

**Grounding.** Redundancy is established from facility, carrier, and path evidence, never from the number of links. Failover behavior is established from the configured timers, the prefix state, and the backup path's actual bandwidth, and where a previous incident demonstrated the real behavior, that evidence outranks the design. DNS resolution paths are traced per client population, since the interesting failures are asymmetric: cloud clients resolving correctly while on-premises clients resolve a public address and leave the private path is a working system by every test that only runs on one side. Where the routing design and the received prefix list disagree, record both and preserve the conflict.

**Constraints.** Every link states its bandwidth, its diversity basis, and the capacity available after the loss of any single path, so a design is never described as redundant when the surviving path cannot carry the load. Prefix advertisement states the exact ranges from the allocation register and the count against the prefix limit in force, because exceeding that limit drops the session rather than truncating the list. Overlap resolution names the mechanism and its consequences, and it states which names and addresses each side will see afterward. DNS architecture names the authoritative source per zone, the forwarding path in each direction, the resolver endpoints and their placement across failure domains, and the TTL in force per record class, with the TTL treated as a design parameter because it sets the floor on how quickly any DNS-based failover can take effect. Certificates carry a named human owner and a renewal mechanism, and a certificate whose renewal is manual is recorded as a scheduled outage with a date on it. Failure modes are written as symptom-first entries so the person paged at three in the morning can match what they are seeing to a known mode.

**Parallel surface.** Independent circuits, tunnels, peering sessions, DNS zones, certificate subjects, and client populations are independent assessment units and fan out safely. The end-to-end resolution path for a given name, the aggregate diversity judgment across all links, the post-failure capacity calculation, and the prefix budget against the limit run once after the fan-out returns, because a per-link review cannot see that two independently healthy links share a single conduit and a per-zone review cannot see that one population's resolver forwards into a loop.

**Ordered gate for a routing or name cutover.** Changing advertised prefixes, path preference, or a DNS record for a production name propagates to caches and peers that this estate does not control, and the old value keeps being served until it expires. That is why the order below is mandated, and why step 1 must complete a full old-TTL interval before step 3 begins:

1. Lower the TTL on the affected records to the intended cutover granularity and wait at least the previous TTL so caches holding the old value have expired.
2. Stage the new path or record and confirm it resolves and routes correctly from each client population, including the on-premises population, before it carries traffic.
3. Cut over, with the rollback trigger and the observation window stated in advance.
4. Restore the operational TTL only after the change is confirmed stable, since raising it early re-arms the same cache delay against the rollback.

Decommissioning a circuit, releasing an autonomous system number, or deleting a zone follows the destructive sequence in `references/suite-workflow-contract.md` instead of this one.

**Acceptance bar.** An operator could read these artifacts during an outage and know which path failed, what capacity remains, and what to expect from resolution. Every redundancy claim names its diversity evidence, every failover statement names both the time to converge and the bandwidth that survives, and every certificate has a named owner with a renewal mechanism.

## Outputs

A complete run delivers this set:

- `circuit-and-tunnel-design.md`: each link with bandwidth, termination, virtual interfaces, and the diversity evidence behind any redundancy claim, plus the capacity remaining after the loss of any single path.
- `route-exchange-and-failover.md`: autonomous system numbers, advertised and received prefixes with the count against the limit in force, path preference, failure detection timers, and the convergence behavior with its degraded-bandwidth consequence.
- `address-overlap-resolution.md`: the overlapping ranges, the resolution mechanism, what each side sees afterward, and the workloads whose configuration has to change.
- `dns-architecture.md`: zones and authority, private and public views, forwarding in each direction, resolver endpoint placement across failure domains, the resolution path per client population, and the TTL in force per record class.
- `certificate-register.md`: subject names, issuers, expiry dates, renewal mechanism, and the named owner of each, with manual renewals flagged as dated risks.
- `global-traffic-distribution.md`: steering policy, health check definitions and evaluation points, failover behavior, and the observed effect of the TTLs in force.
- `connectivity-failure-modes.md`: symptom-first entries for each mode with cause, blast radius, and the first diagnostic step.
- `connectivity-downstream-handoff.md`: what `compute-platform-desk` and the resilience stage inherit, including the resolution and steering mechanics failover depends on.

Depth standard: an artifact is complete when a network engineer could implement it and an on-call engineer could troubleshoot from it, both unchanged. A redundancy claim with no diversity evidence, a failover statement with no capacity figure, and a certificate with no owner are unfinished rather than draft.

When the circuit inventory, routing state, DNS zone contents, or certificate register exists and cannot be read, the run delivers `connectivity-connector-diagnostic.md` naming each unreachable source and the connectivity or resolution claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: this desk is the one whose artifacts get read during an outage, so a confident wrong sentence here costs minutes at exactly the wrong time. The characteristic failure is not inventing a circuit; it is writing "redundant, dual path" because the inventory lists two links, when no source established the facilities, carriers, or conduits behind them. Redundancy is asserted only from diversity evidence, and where that evidence is missing the honest entry is that path diversity is unverified, which is a finding an operations team can act on. The same rule governs failover: a backup path is described with the bandwidth it actually carries, because "failover succeeds" and "the site stays up" are different claims and only one of them was tested. Circuit identifiers, VLAN tags, autonomous system numbers, peer addresses, advertised prefixes, resolver addresses, and certificate expiry dates are transcribed from the source or left unresolved, since a plausible peer address in a runbook is followed by someone under pressure and sends them to the wrong device.

## infrastructure_packet fields to update

- `network.hybrid_links[]` with `link`, `bandwidth`, `redundancy`, and `routing`, each carrying its diversity and routing evidence
- `network.dns_zones` with authority, view, and forwarding direction per zone
- `network.ipam_plan[]` updated with on-premises and partner allocations discovered during overlap analysis
- `network.topology` confirmed or corrected against received routing state
- `resilience.failure_domains` extended with connectivity paths that are single points of failure
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would change advertised prefixes, path preference, a production DNS record, resolver forwarding, or a certificate binding, or would decommission a circuit or tunnel.
- **Source conflict**: the routing design, the received prefix list, and the on-premises address records genuinely disagree about what is advertised or what overlaps, and choosing one silently would produce a routing change that blackholes traffic.
- **Security or privacy**: continuing would assert encryption in transit, private resolution, or path isolation as verified without configuration evidence, or a private name or internal address range is exposed through a public zone.
- **Missing approval**: a circuit order, a routing preference change, a zone delegation, a certificate authority change, or a cutover window needs a named owner who has not authorized it.
- **Release integrity**: path diversity, failover capability, or resolution behavior would be declared satisfied without evidence that it was exercised rather than configured.
- **Connector unreachable**: the circuit inventory, routing state, DNS zone contents, query logs, or certificate register exists and cannot be read.

Unknown historical circuit intent, missing query log history, and absent latency baselines are soft gaps. Name them, label the assumption, and continue. Encryption obligations for traffic crossing an untrusted path, and the approval required for a production name or routing change, are never relaxed to keep a workflow moving.

## Downstream handoffs

`compute-platform-desk` is next and needs the resolution path and the connectivity constraints that bound instance placement. `container-platform-desk` needs the DNS forwarding behavior its cluster resolvers depend on and the ingress name ownership. `managed-database-platform-desk` needs the private resolution path clients will use to reach endpoints. `resilience-multi-region-desk` inherits the steering policy, the health check evaluation points, and the TTLs, because those set the floor on how fast any regional failover can be observed, plus every connectivity single point of failure found here. `cloud-security-posture-desk` inherits exposed public zones and unencrypted paths as findings. `cloud-decommissioning-desk` inherits the circuit and zone teardown obligations. Send edge content strategy and application-layer routing logic to the Web suite as a labeled cross-suite handoff.

## Quality bar

Good hybrid work is skeptical about the word redundant. It names the building, the carrier, and the conduit, and if it cannot, it says the diversity is unverified rather than counting links. It states failover in seconds and in gigabits per second together, because the second number is the one that decides whether anyone notices. DNS is described as a path per client population rather than as a set of zones, since the failure that costs the most is the population whose resolver behaves differently from the one the engineer tested from. Certificates have human names against them. And the failure mode list is written from the symptom inward, so it is usable by the person who has been awake for ninety seconds.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
