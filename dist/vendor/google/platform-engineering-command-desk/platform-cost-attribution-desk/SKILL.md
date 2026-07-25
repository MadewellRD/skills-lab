---
name: platform-cost-attribution-desk
description: build the cost allocation model for an internal developer platform including allocation keys and tagging, treatment of shared idle and untagged spend, showback and chargeback design with its behavioral consequences, unit economics per service environment and build minute, waste and idle reclamation targets, and a reporting cadence tenants can act on.
---

# Platform Cost Attribution Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the cost artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent spend figures, tenant budgets, allocation percentages, tag coverage, commitment terms, or savings estimates.

## Role

Own the answer to "what does this team's use of the platform cost, and who pays for it." That means the allocation keys, the split of shared and unallocable spend, the choice between showback and chargeback with its behavioral consequences, the unit economics that make platform spend comparable across teams, the reclamation targets for waste, and a reporting rhythm a team can actually act on.

Cost attribution on a platform is harder than cloud cost reporting because the platform deliberately hides infrastructure. The abstraction that makes provisioning easy is the same abstraction that makes a node's idle capacity belong to nobody. This desk decides where that cost lands and says so out loud.

## Use when

- Designing or reworking the allocation model: keys, tags, labels, account or project boundaries, and the mapping from resource to tenant.
- Shared, idle, or untagged spend has no home and the unallocable percentage is growing.
- Moving from no reporting to showback, or from showback to chargeback, and the incentive effects need thinking through before the first invoice.
- Unit economics are needed: cost per service, per environment, per preview environment, per build minute, per deploy.
- Waste is suspected and needs quantifying with an owner and a target: idle capacity, orphaned resources, oversized runners, always-on ephemeral environments, telemetry ingest, egress.
- A team disputes their platform bill and the model needs to be defensible line by line.

## Do not use when

- The subject is organization-wide cloud spend policy, commitment and discount management, or vendor negotiation: cross-suite handoff to the FinOps suite. This desk allocates the platform's slice; that suite governs the whole bill.
- Quota and fair-share enforcement as an isolation control rather than a spend model: that is `tenancy-isolation-desk`.
- Telemetry cardinality and retention limits themselves: that is `platform-observability-desk`. This desk prices what those limits allow; that desk sets them.
- Environment lifetime and reclamation rules as an environment design question: that is `environment-management-desk`, whose reclamation policy this desk turns into a number.
- Funding model, cost center ownership, and whether the platform is a cost center or charges internally: that is `platform-governance-desk`.

## Required evidence

- The billing or cost export at the granularity it is actually available, named by export and period rather than by dashboard screenshot.
- Tag and label state: coverage percentage, the keys in use, enforcement at provisioning time, and the untagged remainder.
- The tenancy model and allocation boundaries from the packet, since allocation follows the isolation boundary wherever one exists.
- Cluster or scheduler usage data separating requested from consumed capacity, because the gap between them is the idle cost that has to land somewhere.
- The platform's own operating cost: control plane, shared services, runner fleet, registries, telemetry backend, and the platform team's tooling.
- Build and pipeline usage: minutes by runner size, concurrency, cache hit rate, and the queue that concurrency buys.
- Any existing showback report or chargeback agreement, including what tenants were told the numbers mean.

## Workflow

**Outcome.** An allocation model that reconciles to the invoice, an explicit and defended treatment of shared and untagged spend, a showback or chargeback design with its expected behavioral effects stated, unit economics that survive a challenge, ranked reclamation targets with owners, and a reporting cadence tied to a decision someone makes.

**Grounding.** Read the billing export and usage records for reality; read the chargeback agreement, budget documents, and platform documentation for intent. Where the agreement describes an allocation the export cannot support, record both and preserve the conflict per `references/suite-workflow-contract.md`. That mismatch is usually the reason the model is disputed.

**Constraints.** The model reconciles: allocated spend plus explicitly shared spend plus declared unallocable spend equals the invoice total, and any residual is reported as a residual rather than distributed to make the columns sum. Shared cost treatment is a stated choice with a stated distortion, since a proportional split penalizes the largest good-faith user and an even split subsidizes them, and both are defensible only when written down. Idle capacity is assigned deliberately, because leaving it unassigned means the platform absorbs it silently and its budget looks like waste.

Behavioral consequences are part of the design rather than a footnote. Chargeback changes what teams do: it drives resource requests down toward under-provisioning, it makes the escape hatch look cheap when escape-hatch spend is untracked, and it turns platform adoption into a budget conversation rather than an engineering one. Every chargeback design states which behavior it intends to change and which behavior it will accidentally reward. Unit economics use a denominator a team recognizes, so cost per service per month and cost per preview environment beat cost per vCPU hour for every audience except the platform team itself. Reclamation targets carry an owner, a date, and the recovered amount with its source, not a percentage aspiration.

**Parallel surface.** Allocation keys, tenants, services, environments, cost line items, and waste categories are independent units and are parallel-safe; per-tenant allocation, per-line-item classification, per-waste-category quantification, and connector preflight across billing, usage, and tagging sources all fan out.

The aggregate work runs once after the fan-out returns: the reconciliation of every allocated share against the invoice total, the unallocable percentage, the shared-cost split that must sum to the shared pool exactly, the ranking of reclamation targets by recoverable amount against effort, and the cross-tenant fairness judgment that no single-tenant view can produce.

**Acceptance bar.** A team lead can read their own line and trace every figure to an export, a usage record, or a stated allocation rule. The shared and unallocable portions are visible rather than folded into someone's bill. Every currency figure names its source and its period. Reclamation items name a person and a date.

## Outputs

A complete run delivers this artifact set:

- `platform-cost-allocation-model.md`: keys, the resource-to-tenant mapping, shared and idle and untagged treatment with the distortion each choice introduces, and the reconciliation against the invoice total.
- `platform-cost-unit-economics.md`: cost per service, per environment class, per preview environment, per build minute, and per deploy, each with its denominator, its period, and its source.
- `platform-cost-waste-register.md`: quantified waste by category with the evidence, the recoverable amount, the owner, the reclamation date, and the risk of reclaiming it.
- `platform-cost-reporting-plan.md`: showback or chargeback design, statement format and cadence, the decision each report is meant to trigger, the anomaly path, and the dispute process.
- `platform-cost-downstream-handoff.md`: the spend consequences `platform-change-rollout-desk` and `platform-adoption-migration-desk` inherit, including which cohorts a chargeback change will move.

Depth standard per artifact: an allocation entry names the specific key, where it is set, and what happens to resources missing it, not the concept of tagging. A unit-economics entry states the denominator explicitly, because cost per build minute computed on billed minutes and cost per build minute computed on queue-inclusive wall clock differ by a factor that changes decisions. A waste entry that names a category without a quantity and a source is a hypothesis, and is labeled one.

In `diagnostic` mode, when the billing export, usage data, or tagging state exists and cannot be read, the run delivers `platform-cost-connector-diagnostic.md` reporting reachability, the exports attempted, and the exact access needed. Allocation figures are not drafted from list prices in that mode.

Money invents itself more easily than anything else in this suite. A currency figure carries the authority of an invoice regardless of where it came from, and once a per-team number is circulated it becomes the basis of a budget conversation nobody re-derives. Every figure in these artifacts names the export, usage query, or rate card behind it and the period it covers. A number derived from public list price rather than the actual negotiated invoice is labeled a list-price estimate every time it appears. Percentages state their denominator. Where allocated shares do not sum to the invoice, the artifact reports the model as unreconciled with the residual shown, because a model that balances by rounding is a model that will lose its first dispute and take the platform's credibility with it.

## platform_packet fields to update

- `cost_model.allocation_keys`, `cost_model.shared_cost_treatment`, `cost_model.reporting_state`, `cost_model.unit_economics`.
- `environments[].lifetime` where a reclamation rule changes to control spend.
- `governance.approval_gates` for chargeback activation and budget-affecting reclamation.
- `consumers[]` annotated with allocation state where the tenant boundary drives the split.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: activating chargeback, changing an allocation rule that moves spend between cost centers, or committing to a reclamation that reduces a tenant's capacity needs the named owner who has not given it.
- Production or destructive: the next action would delete, resize, or reclaim a live resource, cancel a commitment, or change a billing account structure.
- Security or privacy: the cost export carries account identifiers, contract terms, or personal data whose exposure in an artifact has not been cleared.
- Source conflict: the billing export, the usage data, and the chargeback agreement genuinely disagree on what a tenant owes, and picking one silently would produce an invoice nobody can defend.
- Release integrity: a cost model would be declared ready for chargeback without evidence that it reconciles to the invoice.
- Connector unreachable: the billing export, usage records, or tagging state exists and cannot be read.

Partial tag coverage, missing historical spend, and unknown idle attribution are soft gaps: proceed with the unallocable portion shown explicitly and named. A reconciliation gap is never closed by distributing the residual.

## Downstream handoffs

`platform-change-rollout-desk` needs the tenants whose bill changes and by how much, because a cost change is a tenant-affecting change with its own notice requirement. `platform-adoption-migration-desk` needs the spend comparison between the paved road and the escape hatch, since a chargeback model that prices the paved road higher will produce migration away from it. `platform-governance-desk` inherits the funding model and the disputes that need a forum. Cross-suite: commitment strategy and organization-wide spend policy go to the FinOps suite.

## Quality bar

A statement a team lead can read without a translator, tracing each line to an export. Shared and idle cost visible rather than hidden. Unit economics in denominators engineers recognize. Waste quantified with an owner attached. And an explicit sentence about what the model will make teams do, because a cost model is an incentive system whether or not it was designed as one.
