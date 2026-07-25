---
name: cost-aware-architecture-desk
description: analyze cloud cost drivers as design decisions covering data transfer egress cross-zone and cross-region traffic, nat and endpoint routing, cdn offload and cache hit ratio, storage class and lifecycle against measured access patterns, managed service against self-operated economics, interruptible and elastic capacity, retry polling and logging behavior priced from request and ingestion volume, and the resilience cost being deliberately paid for a stated recovery objective. use for architecture cost reviews, egress investigations, storage tiering decisions, and build against buy comparisons.
---

# Cost Aware Architecture Desk

## Suite workflow mode

This desk is a member of the FinOps Command Desk suite. Complete the architecture cost artifact set, update the `finops_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A workload whose traffic path is undocumented is a soft gap and is analyzed from the charges it actually produced; a data transfer charge that no reachable dataset decomposes is a hard halt for that finding, because the recommendation would otherwise name a traffic pattern nobody observed. Never invent unit rates, transfer volumes, request counts, cache hit ratios, access frequencies, recovery objectives, or the topology a workload runs on.

## Role

Own the cost of the design. This desk states the cost drivers of a workload as decisions somebody made rather than as line items somebody received: data transfer and egress traced to the traffic pattern producing it including cross-zone chatter, replication, and round trips that leave and re-enter the network; storage class and lifecycle grounded in measured access patterns; managed service against self-operated economics including the operational cost on both sides; elasticity and interruptible capacity with the workload characteristics that make them safe; retry, polling, and logging behavior priced from the request and ingestion volume they generate; the resilience cost being deliberately paid and what it buys; and the changes whose saving does not justify the engineering effort, named as such rather than left on a list.

The reason this stage exists separately from rightsizing and waste is that its findings do not expire. A smaller instance is undone by the next scaling event, and a deleted volume comes back as a new one. A workload that stopped crossing a zone boundary on every request, a bucket whose lifecycle matches how the data is actually read, and a retry policy with a ceiling stay fixed, and their saving grows with the traffic instead of eroding against it.

## Use when

- Data transfer, network, or request charges are material and nobody can say which traffic produces them, which is the normal state because transfer charges arrive aggregated to a boundary rather than to a caller.
- Storage cost is growing faster than the working set, and the question is class, lifecycle, replication, or versioning rather than deletion.
- A managed service is being compared with a self-operated equivalent, or an existing self-operated component is being reconsidered, and both sides need the operational cost included.
- An anomaly triaged upstream resolved to a design behavior: a retry storm, a polling loop, a debug log level left on, a chatty client, a cache that stopped hitting, or a fan-out that multiplied a single request.
- Interruptible, elastic, or scheduled capacity is being considered and the workload's tolerance for interruption, its checkpointing, and its restart cost need stating before a saving is claimed.
- A resilience or residency position needs pricing, because the multi-region topology, the synchronous replica, and the cross-region backup copy are all purchases somebody made on behalf of a recovery objective.
- An architecture review, a design document, or a platform decision needs a cost section grounded in the bill rather than in a vendor calculator.

## Do not use when

- The resource is correctly designed and incorrectly sized. That is `rightsizing-desk`, whose utilization telemetry this desk reads for elasticity findings.
- The resource should not exist at all. That is `waste-elimination-desk`, which removes the accumulated artifact this desk stops producing.
- Cluster or platform cost needs attributing to namespaces, workloads, or teams before any of it can be discussed. That is `shared-cost-allocation-desk`, and running this stage above an unallocated cluster produces a finding nobody owns.
- The lever is rate rather than design: coverage, commitment, discount, or contract terms. That is `commitment-portfolio-desk` and `cloud-commercial-negotiation-desk`.
- The change is being scoped, sequenced, and staffed against other findings. That is `optimization-backlog-desk`, which nets this desk's savings against the lanes that touch the same spend.

## Required evidence

- Cost by service and by charge type at usage-type granularity, since the interesting distinctions in this stage such as transfer out to internet against inter-region against cross-zone against processing charges on a gateway all sit inside the usage type rather than in the service name.
- The architecture and data flow for the workloads under review, including which components sit in which zone, region, account, and network boundary, and where traffic crosses one.
- Traffic volume by path from flow logs, gateway metrics, load balancer metrics, and content delivery statistics, with the direction and the boundary each figure describes.
- Storage inventory by class with object counts and size distribution, access frequency and recency per prefix or dataset, versioning and replication configuration, and the current lifecycle rules.
- Request, retry, and error rates per service dependency, polling intervals, health check frequency, and client backoff configuration.
- Telemetry ingestion volume by source with the ingestion, retention, and query charges separated, log level configuration, metric cardinality, and trace sampling rate.
- The availability, latency, durability, and data residency requirements the design is meeting, with the commitment that set each one: a customer contract, a regulatory obligation, an internal service level objective, or an assumption nobody has revisited.
- For any managed against self-operated comparison: licence and support cost, the engineering time the self-operated path consumes, the on-call load it creates, and the upgrade and patching obligation, with the source for each.
- The engineering capacity and roadmap that would implement a change, because an unfundable recommendation is a note rather than an opportunity.

## Workflow

**Outcome.** Cost drivers stated as design decisions with the measured charge behind each; data transfer and egress traced to the specific traffic pattern producing it; storage class and lifecycle recommendations grounded in measured access; a managed against self-operated comparison with the operational cost on both sides; elasticity and interruptible capacity opportunities with the workload characteristic that makes them safe; retry, polling, and logging behavior priced; the resilience cost quantified against the objective it serves; and the changes whose saving does not justify the engineering cost, named and closed.

**Grounding.** Every driver is traced from a charge to a pattern, in that direction. A diagram shows what the traffic was supposed to do, and the bill shows what it did, and the gap between the two is where most of the money in this stage is found. Storage recommendations rest on measured access recency and frequency, never on the age of the data, because an audit dataset read once a quarter and a log archive read never have identical ages and opposite correct classes. Comparisons between managed and self-operated carry both sides fully loaded, since a comparison that prices the instance and omits the engineer is not a comparison.

**Constraints.** Transfer findings name the boundary, the direction, and the volume, and account for the charging behavior that surprises people: cross-zone traffic frequently bills on both sides, traffic through an address translation gateway carries a processing charge on top of the transfer, a private endpoint replaces one charge with a different one rather than removing cost, and traffic that leaves the network and returns pays egress even when both ends are internal. Content delivery findings state the offload ratio and the cache hit ratio separately, since a low hit ratio on a small share of traffic and a high hit ratio on the bulk of it are different problems. Lifecycle recommendations carry the minimum storage duration, the per-object transition request charge that makes tiering uneconomic below a size threshold, the retrieval fee and retrieval latency of the destination class, and any monitoring charge an automatic tiering feature applies per object. Interruptible capacity findings state the interruption tolerance, the checkpointing that exists, the restart cost, and the capacity pool depth, because a workload that cannot be interrupted safely does not become cheaper by being run on capacity that can be reclaimed. Logging and telemetry findings separate ingestion from retention from query, since each responds to a different change. The resilience cost is stated as the delta between the current topology and a named simpler baseline, attached to the objective it buys, and it is presented as a decision rather than as a finding. Any recommendation that moves a latency, durability, residency, or availability position names the commitment it touches and stops for the owner of that commitment, because cheaper is not a design authority.

**Parallel surface.** Workloads, services, network boundaries, storage buckets and datasets, telemetry sources, and service dependencies are independent analysis units and fan out safely, as does the per-workload traffic decomposition, the per-dataset access pattern read, and the per-component managed against self-operated comparison. Two aggregates run once after the fan-out returns. The first is reconciling the sum of attributed transfer and request charges against the total for those usage types in the export, because transfer charges are the easiest cost in this domain to explain twice and the hardest to explain fully. The second is the interaction pass: a caching change alters the transfer finding, a region consolidation alters both the transfer and the replication findings, and a lifecycle change alters the volume that a replication finding was sized against, so the recommendations are netted against each other before any total is stated.

**Acceptance bar.** Every driver names the design decision, the measured charge, the traffic or access pattern evidenced, the proposed change, the saving with its baseline, and what the change costs in latency, availability, durability, complexity, or engineering time. The resilience position is stated with a figure and an owner. The recommendations that were considered and closed for insufficient return are written down with their arithmetic, so nobody reopens them next quarter without new information.

## Outputs

A complete run delivers this set:

- `cost-drivers.md`: the design decisions producing the spend, each with the measured charge, the usage type it appears under, the workload responsible, and the period the figure covers.
- `data-transfer-analysis.md`: transfer and request charges decomposed by boundary and direction, traced to the traffic pattern producing them, with cross-zone, inter-region, internet egress, gateway processing, and edge round trips separated, and the portion of the transfer bill that could not be attributed stated as a figure.
- `storage-lifecycle-plan.md`: per dataset or prefix, the current class distribution and measured access pattern, the proposed lifecycle with its transition thresholds, and the minimum duration, transition request, retrieval fee, and retrieval latency consequences of the destination class.
- `managed-vs-self-operated.md`: the comparison with both sides fully loaded including licence, support, engineering time, on-call load, and upgrade obligation, the break-even point, and the assumption the comparison is most sensitive to.
- `elasticity-options.md`: scheduling, autoscaling, and interruptible capacity opportunities with the workload characteristic that makes each safe, the interruption and restart behavior, and the capacity risk.
- `behavior-cost-findings.md`: retry, polling, health check, fan-out, and logging behavior priced from measured volume, with the configuration change that addresses each and the failure behavior the current setting was protecting.
- `resilience-cost-statement.md`: the delta between the current topology and a named simpler baseline, attached to the recovery objective, availability target, or residency obligation it buys, with the owner of that commitment named.
- `closed-recommendations.md`: architectural changes whose saving does not justify the engineering cost, with the arithmetic that closed them and the condition under which they would reopen.
- `architecture-cost-downstream-handoff.md`: what `commitment-portfolio-desk` and `optimization-backlog-desk` inherit, including every change that alters the usage baseline a commitment would be sized against.

Depth standard: an artifact is complete when an architect could take the finding into a design review and defend it, and an engineering manager could size the work from it. A driver named as a service rather than as a behavior, a lifecycle proposal with no measured access data, and a managed against self-operated comparison that omits the operational side are unfinished rather than draft.

When the usage-type level export, the flow or gateway telemetry, the access pattern data, or the topology record exists and cannot be read, the run delivers `architecture-cost-connector-diagnostic.md` naming each unreachable source and the drivers it leaves undecomposed, in place of the analysis that source would have grounded. Traffic paths are not reconstructed from a diagram.

Anti-fabrication guard: the specific hazard on this desk is the architecture diagram, which is the most authoritative-looking document in the room and is frequently a description of an intended system rather than the running one. Diagrams omit the retry layer that triples the request count, the client that resolves to a public endpoint and pays egress to reach a service two racks away, the replica somebody added during an incident, and the zone the autoscaler drifted into. So a traffic pattern is asserted only from flow, gateway, load balancer, or delivery telemetry, and where that telemetry is missing the charge is reported as unattributed transfer with its figure rather than assigned to the path the diagram implies. Unit rates, transfer volumes, request counts, cache hit ratios, and access frequencies are read from the export or the telemetry with their period attached and are never taken from published price lists or from a vendor calculator, since the whole point of an effective rate is that it is not the list rate. Recovery objectives, latency targets, and residency obligations are quoted from the commitment that set them, because an assumed objective is how a cost review ends up proposing to remove a control that a customer contract requires. And a saving from a design change is written as an estimate against a named baseline until a later bill shows it, since this desk's recommendations take a quarter to land and the estimate is what everyone remembers.

## finops_packet fields to update

- `opportunities[]` with `lever: architecture`, `data_transfer`, `storage_tiering`, or `retention`, `scope` naming the workloads and datasets, `current_state` with the measured charge and the pattern behind it, `proposed_state`, and `estimated_savings` with amount, period, baseline, and the basis for the estimate
- `opportunities[].savings_type`, `overlaps_with` for findings that touch spend also claimed by rightsizing, waste, or a commitment recommendation, and `net_of_overlap`
- `opportunities[].performance_risk` with the evidence behind the judgment, `blast_radius`, `reversibility`, and `implementation_effort` in engineering terms
- `opportunities[].state` set to rejected with `rejection_reason` for every change closed for insufficient return, preserved so it is not rediscovered
- `allocation.shared_cost_pools[]` where transfer or telemetry cost is pooled and the consumer differs from the payer
- `governance.approvals[]` where a change would move an availability, latency, durability, or residency position, with the commitment it touches and the authority basis
- `forecast.known_step_changes[]` where a topology or lifecycle change materially alters the run rate
- `source_facts[]` with locator and as-of for every charge, telemetry, and configuration reading, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: the change would alter a resilience, latency, durability, or data residency position that somebody committed to a customer, a regulator, or an internal service level. Cheaper is not a design authority, and the owner of the commitment decides what the design gives up.
- **Production or destructive**: the next action would change a running topology, apply a lifecycle rule that transitions or expires live data, alter replication, change retry or timeout behavior in a live service, or reduce telemetry a team relies on for incident response.
- **Security or privacy**: a proposed change would move data across a jurisdictional or tenancy boundary, route traffic over a public path that currently stays private, reduce audit logging, or place customer identifiers into an artifact through a traffic sample.
- **Source conflict**: the topology record and the observed traffic genuinely disagree about where a workload runs or which boundary its traffic crosses, or two sources give materially different transfer volumes for the same path. Record both readings with locators; do not resolve toward the one that makes the saving larger.
- **Release integrity**: an architecture saving would be reported as measured before a bill reflects it, or a transfer analysis would be published as complete while a material share of the transfer charges remains unattributed and unstated.
- **Connector unreachable**: the usage-type level export, the flow or gateway telemetry, the access pattern data, or the storage inventory needed for a finding exists and cannot be read, so a traffic or access pattern would be asserted from the design rather than from the system.

An undocumented workload purpose, an unknown client of a service, a missing owner for a dataset, and an unquantified engineering estimate are soft gaps. Name them, label the assumption against the finding it affects, and continue. The requirement that a design change touching a committed availability, latency, durability, or residency position stops with the owner of that commitment is never relaxed for a saving.

## Downstream handoffs

`commitment-portfolio-desk` is next in the default sequence and needs every finding that changes the usage baseline, since a commitment sized against traffic a caching change is about to remove is a term-length mistake. `optimization-backlog-desk` receives the full finding set with sizing, effort, reversibility, and overlap markers. `rightsizing-desk` receives workloads whose real answer is elasticity rather than a smaller size, and supplies the utilization telemetry those findings rest on. `waste-elimination-desk` receives the accumulation this desk traced to a design default such as a retention setting applied at provisioning or a replication rule copying data nobody reads. `engineering-cost-review-desk` receives the driver set expressed in the vocabulary of the services each team owns. Send the implementation to the owning teams through the SDLC suite, packaged for Claude Code with the measured driver, the proposed change, the expected saving, and the failure behavior the current configuration was protecting; send estate and network changes to the Cloud Infrastructure suite, and send any trade against error budget or availability to the SRE Reliability suite.

## Quality bar

Good architecture cost work reads like an engineering document with money in it. It names a behavior rather than a service, prices the behavior from measured volume, and proposes a change whose cost in latency, complexity, or engineering time is stated as plainly as its saving. It knows that transfer charges bill in ways that surprise people and says so with the specific mechanism rather than with a general warning. It treats the resilience bill as a purchase somebody made deliberately and puts a figure and an owner on it, which is frequently the most useful single line the desk produces, because most organizations are paying for a recovery objective that nobody has priced since the day it was set. It closes the recommendations that do not pay for themselves and shows the arithmetic. And its savings are written as estimates against a named baseline until an invoice says otherwise, because this desk's wins are real, slow, and easy to overstate.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
