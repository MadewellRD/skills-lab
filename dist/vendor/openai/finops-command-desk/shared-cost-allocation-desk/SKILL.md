---
name: shared-cost-allocation-desk
description: split shared and container cloud cost across the teams that consume it with methods the receiving teams can argue with. covers shared pool inventory for network, observability, data platform, support, and licensing spend, proportional even fixed and usage-metric split methods with their rationale, kubernetes cluster cost attribution to namespace and workload from requested versus used resources, idle cluster capacity treatment, platform namespace handling, data transfer and egress attribution where consumer and payer differ, and the residual no defensible method allocates.
---

# Shared Cost Allocation Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the pool, cluster, or namespace it affects and recorded in `open_questions`. Never invent split percentages, namespace cost figures, idle capacity shares, resource request or usage values, egress volumes, or approval for a method nobody signed off.

## Role

Own the cost that no single team consumed alone. This desk inventories the shared pools covering network and data transfer, observability and logging, the data platform, support charges, platform fees, and shared licensing, assigns each pool a split method with a rationale the receiving teams can argue with, attributes container cost from cluster spend down to namespace and workload using stated resource dimensions, treats idle cluster capacity explicitly instead of spreading it silently, handles platform and system namespaces deliberately, attributes data transfer where the consumer and the payer differ, and reports the residual that no defensible method allocates as a residual.

A split method is a political instrument as much as an analytical one. Every method is defensible and every method makes somebody's number go up. The practice's protection is that the method, its driver, and its rationale are written down before the numbers are, so the conversation is about whether the method is fair rather than about whether the practice is picking on a team. A split whose method appears only after a team complains is indistinguishable from a split chosen to produce that result.

## Use when

- Shared platform, network, observability, support, or licensing spend is landing in an unallocated pool and needs distributing.
- Kubernetes or container cluster cost needs resolving to namespaces, workloads, or tenants.
- Idle cluster capacity is material and nobody has decided who carries it.
- Data transfer or egress charges are billed to one account and driven by consumers in another.
- A shared pool split method is being designed, changed, or defended against a team that disputes it.
- Platform and system namespaces are absorbing cost that belongs to the platform rather than to tenants, or the reverse.
- Support charges, marketplace fees, or enterprise-wide licensing need distributing across cost centers.

## Do not use when

- Directly attributable spend has never been measured for coverage: that is `cost-allocation-tagging-desk`, which establishes how much is genuinely shared rather than merely untagged. Splitting untagged spend as if it were shared hides a hygiene problem inside a method.
- The cost basis or invoice reconciliation is unsettled: that is `cost-data-ingestion-desk`.
- The split output needs posting to cost centers with statements and dispute handling: that is `chargeback-invoicing-desk`.
- Cluster nodes are oversized or the cluster is over-provisioned as an engineering matter: that is `rightsizing-desk` for node and request sizing, and `cost-aware-architecture-desk` where cross-zone chatter or replication topology is the driver.
- Cluster capacity is idle because workloads were abandoned rather than because headroom was designed in: that is `waste-elimination-desk`.
- A report needs assembling for an audience: that is `showback-reporting-desk`.

## Required evidence

- The allocation hierarchy, coverage figure, and unallocated pool from `cost-allocation-tagging-desk`, so shared spend is separated from untagged spend.
- Cluster cost at node and node-group level, with the workload resource metrics that go with it: requests, limits, and actual usage for compute and memory, per namespace and per workload, over a window long enough to include the cycle.
- The platform and shared services inventory: what each shared component is, who operates it, and who is supposed to be consuming it.
- Support charges, platform fees, and marketplace charges with the basis on which the provider calculates them.
- Network and data transfer cost broken down by charge type, with the traffic pattern behind it where the export carries it.
- Split methods the organization has already agreed, with who agreed them and when they took effect.
- The list of teams or cost centers that would receive each split, and who owns the allocation model.

## Workflow

**Outcome.** A shared pool inventory with an amount, a split method, a driver, and a rationale per pool, container cost attributed from cluster spend to namespace and workload with the resource dimensions and the window stated, an explicit idle capacity treatment with the reason it lands where it lands, platform namespace handling, data transfer attribution that separates the payer from the consumer, support and licensing fee distribution, and the unallocable residual reported at its full size.

**Grounding.** Cost comes from the billing export and utilization comes from cluster and telemetry sources; the join between them is an inference that carries its own error, and it is labeled as such per `references/suite-workflow-contract.md`. Container allocation tooling produces a model, not a measurement, so the model's assumptions travel with its output. Where the allocation tool and the billing export disagree on cluster cost, the export is the cost and the tool is the distribution.

**Constraints.** The resource dimension driving container allocation is named explicitly, because requested capacity and actual usage produce materially different bills to the same team and each answers a different question: requests measure what a team reserved and removed from the pool, usage measures what it consumed. Charging on usage alone lets a team hold capacity for free; charging on requests alone penalizes accurate request setting. Whichever is chosen, the choice is stated and applied consistently across tenants. Idle cluster capacity is never spread silently into tenant costs, because that makes a platform decision look like a tenant's consumption; it is either carried by the platform, distributed with the method named, or shown as a separate line, and the choice is a stated position with a reason. Data transfer is attributed to the traffic pattern that generates it rather than to the account the charge lands in, and where the two differ the artifact shows both. Every split percentage carries its driver and the period the driver was measured over. A method change is applied from a stated effective period, never retroactively into a period a team has already been charged for.

One ordering is mandated when a split method changes, because a method change moves money between teams without any team changing behavior, and the first person to notice is whoever's number went up:

1. Measure the current split and the proposed split over the same period.
2. Show the before and after per receiving team, in figures.
3. Obtain the allocation model owner's approval with the effective period named.
4. Apply it forward from that period, leaving prior postings intact.

**Parallel surface.** Individual shared pools, clusters, namespaces, workloads, node groups, and per-team impact analyses are independent units and fan out, as does connector preflight across the cost dataset, cluster metrics, the platform inventory, and the network cost breakdown.

The aggregate is a single pass after the fan-out returns. The splits have to sum to the pool and the pools have to sum to the shared total, so the reconciliation of allocated plus residual back to the shared spend is a whole-set calculation. Idle capacity is defined as cluster cost minus attributed workload cost, which only exists at the cluster level and cannot be derived from any namespace's view. Per-namespace attribution computed independently and then summed will not equal cluster cost, and the gap is the finding rather than a rounding error to be distributed away.

**Acceptance bar.** A team receiving a shared charge can see the pool it came from, the method, the driver value used for their share, the period the driver was measured over, and the person who approved the method, and the sum of every split plus the residual equals the shared spend in the reconciled dataset.

## Outputs

A complete run delivers this artifact set:

- `shared-cost-pools.md`: each pool with what it covers, its amount, its split method, its driver, its rationale in terms the receiving teams can dispute, and its approval state.
- `container-cost-allocation.md`: cluster spend resolved to namespace and workload, the resource dimensions used, the measurement window, the tooling behind the numbers, and the per-namespace figures with their share of cluster cost.
- `idle-capacity-treatment.md`: measured idle as cluster cost minus attributed workload cost, the headroom that is deliberate and what it buys, the idle that is not, where the charge lands and why.
- `data-transfer-attribution.md`: transfer and egress cost by charge type traced to the consuming workload or service, with the payer and the consumer named separately wherever they differ.
- `shared-cost-residual.md`: the spend no defensible method allocates, at its full amount and share, with what would allocate each component.
- `split-method-change-log.md`: any proposed or applied method change with the before and after per team, the effective period, and the approver.

Depth standard per artifact: a pool entry gives the driver value and period, not the method name alone, so a team can recompute its own share. A container allocation entry gives requests, usage, and cost per namespace rather than cost alone, because the ratio between the first two is the conversation the number is meant to start. An idle figure gives the cluster, the window, and the split between designed headroom and unclaimed capacity. A transfer entry names the traffic pattern, so "cross-zone replication between the primary and standby of the order service" rather than "inter-region data transfer".

In `diagnostic` mode, when cluster metrics, the network cost breakdown, or the shared services inventory exists and cannot be read, the run delivers `shared-cost-connector-diagnostic.md` naming what was attempted and which pools and clusters that gap leaves unsplit. A cluster is not attributed from node count alone when the workload metrics are unreachable.

The failure mode this desk has to guard against is the method that sounds agreed. A split presented with a percentage, a driver, and confident phrasing reads as an accepted allocation model whether or not anyone approved it, and once it appears in a report a team is being charged on the strength of a number that originated in this artifact. Every method carries its approval state, and `unapproved` is written out as `unapproved` rather than omitted. The same discipline applies to the residual: when the splits do not sum to the pool, the gap appears as a residual line with its size, never proportionally smeared across the receiving teams to make the arithmetic close. A residual of nine percent is a finding the allocation model owner can act on; a set of splits that sums exactly because the remainder was quietly distributed is a model that will be disproved by the first team that rebuilds it.

## finops_packet fields to update

- `allocation.shared_cost_pools[]` with `pool`, `amount`, `split_method`, `driver`, `rationale`, and `approved_by`.
- `allocation.container_allocation` with `method`, `cost_drivers`, `idle_capacity_treatment`, `shared_namespace_treatment`, `clusters_in_scope`, and `tooling`.
- `allocation.unallocated` updated where a split resolves part of the pool, with the residual recorded rather than absorbed.
- `governance.approvals[]` for any method that requires the allocation model owner's sign-off, with `authority_basis` and `state`.
- `source_facts[]` with `locator` and `as_of` per driver value, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: a split method is being introduced or changed. This is the defining halt for this stage, because a method change alters what teams are charged with no change in their behavior, and it belongs to the owner of the allocation model with a stated effective period and the before and after shown together.
- Source conflict: the container allocation tool and the billing export disagree on cluster cost, or the platform inventory and the cost data disagree on which team consumes a shared service, on spend material enough to move a team's charge.
- Release integrity: a split would leave the practice with a driver nobody measured, a residual absorbed rather than shown, or an idle share presented as tenant consumption.
- Production or destructive: the next action would change a live allocation configuration, a cost grouping rule, or a posted split for a period already charged.
- Security or privacy: namespace names, workload identifiers, or tenant labels in the allocation output would expose customer identity or another tenant's consumption to a recipient who should not see it.
- Connector unreachable: cluster metrics, the network cost breakdown, or the shared services inventory cannot be read, so a split would be modeled against unknown consumption. State whether the source was empty or unreachable.

A missing rationale for a historical split, an unresponsive platform owner, or an unmeasured driver for a small pool below the materiality threshold is a soft gap: proceed with the method labeled proposed and the question recorded.

## Downstream handoffs

`showback-reporting-desk` needs every pool with its method and rationale, because the first question any audience asks about a shared charge is how it was calculated. `unit-economics-desk` needs the shared cost assumptions as caveats, since a unit cost built on a split method inherits that method's judgment. `chargeback-invoicing-desk` needs the approved methods, the effective periods, and the residual, because the ledger has to balance to the invoice and the residual is exactly what would otherwise be silently absorbed. `rightsizing-desk` receives the request-versus-usage gap per workload as candidate evidence. `engineering-cost-review-desk` needs the per-namespace picture in the vocabulary of the services a team owns.

## Quality bar

Every pool has a method, a driver, a rationale, and an approval state. Container cost resolves to namespaces with the resource dimension named and the window stated. Idle is measured and placed deliberately, not spread by default. Transfer cost names the traffic pattern rather than the charge code. The splits plus the residual equal the shared spend, and the residual is visible at its real size. A team that disagrees with its charge can find the method, recompute its own share, and argue about the right thing.
