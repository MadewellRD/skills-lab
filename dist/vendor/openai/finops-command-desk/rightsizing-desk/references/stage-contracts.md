# FinOps Stage Contracts

One entry per desk in the FinOps Command Desk suite. Use these when running the suite as a continuous program of work, so a desk can carry an engagement into the next stage instead of telling the user to invoke another skill.

## Stage order

```text
cost-data-ingestion-desk
  -> cost-allocation-tagging-desk
  -> shared-cost-allocation-desk
  -> showback-reporting-desk
  -> unit-economics-desk
  -> software-cogs-margin-desk
  -> budget-planning-desk
  -> forecasting-variance-desk
  -> anomaly-detection-desk
  -> rightsizing-desk
  -> waste-elimination-desk
  -> cost-aware-architecture-desk
  -> commitment-portfolio-desk
  -> licensing-saas-spend-desk
  -> cloud-commercial-negotiation-desk
  -> optimization-backlog-desk
  -> engineering-cost-review-desk
  -> chargeback-invoicing-desk
  -> finops-maturity-desk
```

The order is a dependency chain, not a mandatory itinerary. Most engagements run a subsequence and enter partway: a bill that jumped overnight enters at `anomaly-detection-desk`, a margin question from finance enters at `software-cogs-margin-desk`, an expiring commitment enters at `commitment-portfolio-desk`, a chargeback dispute enters at `chargeback-invoicing-desk` and pushes backward into allocation. Never run a stage ahead of the packet state it consumes, and never skip a stage the data shows is load-bearing for the requested outcome. Record every skip with its reason.

The four optimization lanes between `rightsizing-desk` and `cost-aware-architecture-desk`, plus `licensing-saas-spend-desk`, consume the same cost and utilization data without consuming each other's output, so they fan out and converge into one deduplicated opportunity set at `optimization-backlog-desk`. `commitment-portfolio-desk` is deliberately downstream of all of them, because commitments are sized against the usage that remains after optimization rather than against the usage that exists today.

Each entry states the hard halt that is specific to that stage. The default posture everywhere else is to proceed with the assumption labeled inline against the account, service, workload, or opportunity it affects, per `references/halt-taxonomy.md`.

## Contracts

### cost-data-ingestion-desk
Requires: billing and usage exports for every provider in scope with their schema and refresh behavior, the provider invoices for the periods being analyzed, credit and discount records, the cost platform configuration where one is in use, SaaS vendor statements, currency and conversion policy, the amortization and capitalization conventions finance actually applies.
Owns: the cost basis declaration naming which cost column is in play and why, the dataset register with granularity, coverage window, refresh lag, and known limits per source, reconciliation of the dataset total to the invoice total with any variance explained rather than absorbed, credit, refund, tax, support, and marketplace charge treatment, currency normalization with its rate source, period state marked open, closed, or partial, and the explicit list of questions the available data cannot answer.
Hands to: `cost-allocation-tagging-desk`.
Hard halt: connector unreachable. The billing export, the invoice, or the provider account needed to establish what was actually billed cannot be read. Every figure downstream inherits this dataset, so an unreachable source produces a whole analysis that is internally consistent and unanchored. An empty export and an unreachable export look identical in a query result and mean opposite things, so say which one happened.

### cost-allocation-tagging-desk
Requires: the reconciled cost dataset, the account, subscription, and project hierarchy, the current tag and label inventory with values, the tagging policy and how it is enforced, the cost center and team structure from the ledger or the HR system, ownership records, provider-native cost grouping rules already in place.
Owns: the allocation hierarchy from resource to cost center with the rule at each level, tag key requirements with measured coverage per key and per account, tag value hygiene findings covering case, spelling, and orphaned values, allocation coverage as a percentage of total spend, the unallocated pool broken down by cause rather than reported as one number, the largest untagged contributors ranked by spend, enforcement recommendations separated into what can be enforced at provisioning and what needs retrofitting, and the backfill plan for historical periods that will never carry tags.
Hands to: `shared-cost-allocation-desk`.
Hard halt: source conflict. The tag inventory, the account structure, and the ledger cost center mapping give different owners for the same material spend. Allocation is the foundation every later figure sits on, and publishing an allocation built over an unresolved ownership conflict produces a chargeback that a team can prove is wrong, which costs the practice more credibility than the delay costs anyone.

### shared-cost-allocation-desk
Requires: the allocation hierarchy and coverage from the previous stage, container and cluster cost with workload-level resource metrics, the platform and shared services inventory, support and platform fee charges, network and data transfer cost, the split methods the organization has previously agreed, the teams that would receive each split.
Owns: the shared cost pool inventory with an amount and a split method per pool, the split rationale in terms the receiving teams can argue with, container cost allocation from cluster spend down to namespace or workload with the resource dimensions used, idle cluster capacity treated explicitly rather than spread silently, platform namespace handling, data transfer and egress attribution where the consumer and the payer differ, support and licensing fee distribution, and the residual that no defensible method allocates, reported as residual.
Hands to: `showback-reporting-desk`.
Hard halt: approval. A change to a split method changes what teams are charged without any team changing behavior, and the first person to notice is the team whose number went up. Method changes belong to the owner of the allocation model, applied from a stated effective period, with the before and after shown together.

### showback-reporting-desk
Requires: the allocated cost dataset including shared splits, the audiences and what each of them can actually act on, the reporting cadence and the decisions it feeds, prior reports and their trend baselines, known one-off charges and period effects, the materiality threshold.
Owns: the report set with one view per audience and the decision each view supports, trend presentation with its baseline named and partial periods flagged, the drivers behind every material movement stated as a change in consumption or rate rather than as a change in a chart, distortion warnings for migrations, credits, one-off purchases, and period effects, the top movers by absolute figure and by rate of change, unallocated spend shown rather than hidden in a total, and the narrative that tells each audience what to do next.
Hands to: `unit-economics-desk`.
Hard halt: release integrity. A report leaving the practice would carry totals that do not reconcile to the invoice, would compare a partial period against a complete one, or would show a figure whose cost basis is not stated. Published cost numbers get quoted back for quarters, and a correction never travels as far as the original.

### unit-economics-desk
Requires: allocated cost at the granularity the metric needs, the business volume from its system of record, the definition of that volume as the owning system defines it, product and customer structure, the decision the metric is meant to support, prior periods for trend.
Owns: the metric definition with its numerator scope, cost basis, denominator, and denominator source, the computed value with its period, trend against a named baseline, the driver decomposition separating rate changes from volume changes from mix changes, cohort or segment views where the aggregate hides the answer, the caveat set covering allocation gaps and shared cost assumptions that materially move the number, the owner who can actually move it, and the metrics the data cannot yet support, named rather than approximated.
Hands to: `software-cogs-margin-desk`.
Hard halt: source conflict. Two systems of record give materially different values for the same business denominator. A unit cost is a ratio, so a denominator dispute is not a rounding question; it changes the number the company manages to and frequently reverses the trend.

### software-cogs-margin-desk
Requires: the allocated cost dataset, the revenue figure with its source, the cost of revenue classification policy, the internal-use software capitalization policy, the general ledger extract for the period, the period state and who owns the close, product and service line structure, prior period classifications.
Owns: classification of infrastructure and vendor spend into cost of revenue against research, internal, or sales-facing cost with the policy rule behind each line, capitalized development cost identified with the project it belongs to, gross margin computed with its revenue basis stated, margin by product or service line where the structure supports it, the variance between the cost dataset and the posted ledger with its accrual, timing, and intercompany explanation, and the reclassification proposals prepared for the controller rather than applied.
Hands to: `budget-planning-desk`.
Hard halt: approval. A reclassification, a capitalization judgment, or a restatement that touches a closed period is the controller's decision and lands in audited statements. Cost of revenue and margin are reported externally, and moving a line between cost of revenue and research changes a metric that investors track, which makes it an accounting decision wearing an infrastructure costume.

### budget-planning-desk
Requires: the run rate from the reconciled dataset, the allocation hierarchy and the budget holders it maps to, planned launches, migrations, and decommissions with their timing, headcount and business plans that drive consumption, the prior budget with its actual outcome, the planning calendar and its submission dates, the commitment position already carried.
Owns: budget lines scoped to a named holder with the basis for each amount, run-rate baselines separated from growth assumptions and from step changes, the cost of planned work estimated from comparable measured workloads with the comparison named, seasonality and business cycle effects, alert thresholds set where they are actionable rather than where they are round, the reserve or contingency position with what it exists to absorb, and the budget lines that no owner has accepted, reported as unowned rather than assigned by inference.
Hands to: `forecasting-variance-desk`.
Hard halt: approval. A budget of record commits an organization's spending authority and becomes the number teams are measured against. Setting or changing one is the budget holder's decision with finance, and a budget quietly derived by the practice is a target nobody agreed to defend.

### forecasting-variance-desk
Requires: the historical cost series with periods marked complete or partial, the budget, the drivers with their sources, known step changes such as migrations, launches, renewals, and decommissions, the commitment agreements with their terms and drawdown, prior forecast accuracy, the horizon the decision needs.
Owns: the forecast with its method and the reason that method suits this spend profile, driver-based projection where drivers exist and run-rate projection where they do not, step changes modeled explicitly rather than smoothed into a trend, forecast range with what widens it, measured accuracy against prior actuals, variance analysis attributing each material gap to consumption, rate, allocation change, or timing, and the commitment trajectory showing drawdown against contracted spend with the shortfall or overage position quantified before the term ends.
Hands to: `anomaly-detection-desk`.
Hard halt: release integrity. A forecast would go to finance or leadership built on periods that were still open, on a trend that includes a partial month, or on a method whose prior accuracy is unmeasured and unmentioned. A forecast becomes a commitment the moment somebody plans against it, and the practice inherits the gap.

### anomaly-detection-desk
Requires: the cost series at the granularity anomalies actually appear in, detection thresholds or models with their sensitivity, the deployment, configuration, and migration record for the period, usage telemetry, the account and service ownership map, prior anomalies and how they resolved.
Owns: the anomaly set with detection basis, scope, delta figure, and baseline for each, triage into explained, expected, waste, or false positive with the evidence for the call, root cause traced to a specific change rather than attributed to the service the charge landed under, correlation with deployments, feature launches, retries, data growth, or a rate change, the distinction between a spend spike and a rate change that looks like one, threshold tuning where noise is suppressing real signal, and the recurrence control that stops the same cause returning.
Hands to: `rightsizing-desk` where the cause is capacity, `waste-elimination-desk` where the cause is idle or orphaned resource, and `cost-aware-architecture-desk` where the cause is a design behavior such as retry storms, chatty cross-zone traffic, or unbounded retention.
Hard halt: security or privacy. The spend pattern is consistent with credential compromise, cryptomining, or exfiltration-scale data transfer. Cost is frequently the first place this becomes visible, and the correct next move is a security incident rather than a cost optimization. Route it and preserve the evidence rather than quietly terminating the resources that constitute it.

### rightsizing-desk
Requires: workload-level utilization telemetry over at least one full business cycle including peaks, current resource configuration and cost, the workload's performance requirements and any service level it supports, autoscaling and scheduling behavior already in place, licensing implications of a size or family change, the owning team, the change process that would apply.
Owns: rightsizing candidates with measured current utilization against the observation window that produced it, the proposed configuration with the headroom it leaves and the peak it was tested against, the saving with its baseline, family and generation migration options including their compatibility constraints, storage and database sizing alongside compute, autoscaling and schedule changes where the answer is elasticity rather than a smaller size, the performance risk with the evidence behind that judgment, and the candidates explicitly rejected because the measurement window did not cover their cycle.
Hands to: `waste-elimination-desk`.
Hard halt: production or destructive. Resizing, restarting, or reconfiguring a running workload is a change to production with an availability consequence, and databases, stateful services, and anything carrying a service level are the cases where it is least reversible. Prepare the change with its evidence, its rollback, and its window; the owning team executes it.

### waste-elimination-desk
Requires: the resource inventory with age, attachment state, and last activity, cost per waste candidate, snapshot and backup retention policies, log and data retention configuration, non-production environment schedules, the owner map, retention and legal hold obligations, dependency information for anything proposed for removal.
Owns: the waste inventory by category covering idle and stopped resources still incurring charge, unattached storage volumes and addresses, orphaned snapshots and images, abandoned environments, over-retained logs and backups, duplicated data copies, and forgotten test infrastructure, each with its cost, age, and the evidence that it is genuinely unused, non-production scheduling opportunities, retention tier changes with the recovery consequence stated, an owner and a confirmation route per candidate, and the candidates that look like waste and are not, recorded so the next sweep does not resurface them.
Hands to: `cost-aware-architecture-desk`.
Hard halt: production or destructive. Deletion is the one action in this suite with no undo. A snapshot is the restore path for something, an idle instance is a disaster recovery standby or a quarterly job, and an unattached volume holds the only copy of something nobody documented. Retention obligations and legal holds outrank a saving in every case. Prepare the removal set with owner confirmation and a reversible staging step; a named human authorizes the deletion.

### cost-aware-architecture-desk
Requires: the architecture and data flow for the workloads under review, cost by service and by charge type including data transfer, storage class distribution and access patterns, request and retry behavior, replication and multi-region topology, the availability and latency requirements the design is meeting, the engineering capacity that would implement a change.
Owns: the cost drivers of the design stated as design decisions rather than as line items, data transfer and egress cost traced to the traffic pattern producing it including cross-zone chatter, replication, and unnecessary round trips through the edge, storage class and lifecycle recommendations grounded in measured access patterns, managed service against self-operated cost comparison including the operational cost both ways, elasticity and interruptible capacity opportunities with the workload characteristics that make them safe, retry, polling, and logging behavior priced, the resilience cost that is deliberately being paid and what it buys, and the architectural changes whose saving does not justify the engineering cost, named as such.
Hands to: `commitment-portfolio-desk`.
Hard halt: approval. An architectural change to reduce cost can move a resilience, latency, or data residency position that somebody committed to a customer or a regulator. Cheaper is not a design authority. The owner of the service level and the architecture owner decide what the design gives up.

### commitment-portfolio-desk
Requires: the post-optimization usage baseline with the optimization work that produced it, the current commitment portfolio with utilization, coverage, expiry, and flexibility per instrument, the forecast and its confidence, the workload stability picture including anything planned for migration or decommission, the commercial agreements governing rates and eligible spend, the purchase authority matrix.
Owns: coverage and utilization measured against the eligible base rather than against total spend, the effective savings rate with its baseline named, stranded commitment identified with its cause, expiry cliffs mapped forward with the increase each one lands, the purchase recommendation sized against post-optimization usage with term, payment option, and flexibility chosen for the workload's stability, the downside case quantified for the scenario where usage falls, laddering across expiry dates so the portfolio does not renew in one lump, and the position that no purchase is justified where the data says so.
Hands to: `licensing-saas-spend-desk`.
Hard halt: approval. A commitment purchase spends real money on a term that generally cannot be cancelled or refunded. Sizing it against pre-optimization usage locks in waste for the full term, and a wrong purchase is not fixed by a later analysis; it is paid for monthly until it expires. The purchase authority the matrix names approves the quantity, the term, and the payment option.

### licensing-saas-spend-desk
Requires: the application inventory with spend and agreement references, seat or unit entitlements against measured activity, renewal dates and notice windows, license models including bring-your-own against included licensing, marketplace purchasing arrangements and whether that spend draws down a provider commitment, overlapping tool coverage, the owning business function per application.
Owns: utilization per application measured against how activity is actually defined for that product, shelfware quantified with the renewal date it must be actioned before, license model comparison where the same software can be licensed several ways with materially different economics, marketplace and channel routing analysis including commitment drawdown effects, tool overlap where several products cover one need, tiering and edition analysis against real feature use, and the renewal calendar with the last safe date to act on each notice window.
Hands to: `cloud-commercial-negotiation-desk`.
Hard halt: connector unreachable. Entitlement data or usage telemetry for a material application cannot be read, so a seat reduction would be recommended against unknown actual use. Reducing entitlements that are in use is a production outage delivered by a spreadsheet, and the affected users find out at login.

### cloud-commercial-negotiation-desk
Requires: the spend trajectory and forecast, the current agreements with commit amounts, terms, discount structures, and eligible spend definitions, drawdown position and any shortfall exposure, workload mix and growth case, credible alternatives and their switching cost, the renewal timeline and its notice windows, prior negotiation outcomes, the procurement and legal owners.
Owns: the negotiation evidence pack with spend history and forecast expressed the way a vendor account team will model it, commit sizing options with the shortfall exposure quantified for each, the ask list with a value attached to every ask covering discount depth, eligible spend breadth, migration and transition funding, egress and transfer relief, support tier, marketplace treatment, and flexibility terms, the leverage assessment grounded in evidence rather than in posture, the walk-away and status-quo cost, and the timeline working backward from the notice windows that actually constrain the deal.
Hands to: `optimization-backlog-desk`, with the paper going to the Legal Contracts suite and the sourcing relationship to the Procurement suite.
Hard halt: approval. A commitment level, a term, or an ask that leaves for a vendor commits the organization commercially. This desk prepares the position and the evidence; procurement and legal own the negotiation and the paper, and the authority matrix names who can commit the spend. Nothing goes to a counterparty from here.

### optimization-backlog-desk
Requires: every opportunity from every lane with its scope, sizing, and evidence, the commitment recommendations, the engineering capacity and roadmap it competes with, the change process and its lead times, prior accepted and rejected opportunities, the savings realization record.
Owns: the deduplicated opportunity register where overlapping opportunities are netted rather than summed, prioritization on savings against effort, risk, and reversibility rather than on savings alone, the sequencing constraint that optimization precedes commitment, ownership assignment to the team that must act with the ask stated in engineering terms, acceptance and rejection states with the rejection reason preserved so the same finding is not rediscovered next quarter, savings realization tracked against the bill rather than against the estimate, and the estimate-to-actual gap fed back into how future opportunities are sized.
Hands to: `engineering-cost-review-desk`.
Hard halt: release integrity. A savings total would be reported that sums overlapping opportunities, mixes cost avoidance into realized savings, or counts an estimate as a result. A backlog that claims more savings than the bill can lose is the fastest way for a practice to lose its mandate, because the first person to check is the person whose budget was cut on the strength of it.

### engineering-cost-review-desk
Requires: allocated cost per team with the coverage caveats that apply to it, unit economics where they exist, the opportunity register filtered to that team, the team's own service ownership and roadmap, prior review actions and their outcomes, the guardrails and policies in force, the forum and cadence the review runs in.
Owns: the team-facing cost picture in the vocabulary of the services the team actually owns, movement explained as consumption, rate, or allocation change so the conversation is about engineering rather than about the report, the action set with owners and dates rather than a list of observations, cost signals placed where engineering decisions are already made such as design review, provisioning, and pull request when the evidence supports it, guardrail proposals separated into what should block and what should inform, the accountability model naming who owns a number and what happens when it moves, and the findings that belong to the platform rather than to the team, routed away rather than presented as their problem.
Hands to: `chargeback-invoicing-desk`.
Hard halt: approval. A guardrail that blocks provisioning, a hard budget stop, or a policy that fails a deployment is an availability control wearing a cost label. It belongs to platform and engineering leadership, because the failure mode is a team unable to scale during an incident.

### chargeback-invoicing-desk
Requires: the fully allocated dataset including shared splits and the residual, the chargeback model and its approval state, the cost center structure and the ledger accounts, the invoice for tie-out, the internal rate card where one exists, dispute history, the finance posting calendar and the period state.
Owns: the chargeback ledger that balances to the invoice with any residual shown rather than absorbed, postings per cost center with the allocation rule that produced each figure, the internal rate card with the basis for any markup or subsidy, the statement each cost center receives with enough detail to check the number rather than only to pay it, dispute intake with the specific allocation rule under challenge, resolution that either corrects the allocation for everyone or explains why the rule holds, the model change proposal where disputes reveal a structural problem, and the reconciliation between what was charged and what was billed.
Hands to: `finops-maturity-desk`.
Hard halt: production or destructive. Posting a chargeback moves money between cost centers in the ledger, and reversing a posted period requires finance to unwind it. A posting into a closed period, a ledger that does not tie to the invoice, and a model change applied retroactively are each a finance action with an audit trail, so they stop at the gate with the controller.

### finops-maturity-desk
Requires: the evidence of what the practice actually does covering allocation coverage, forecast accuracy, realization rate, anomaly response time, and adoption, the framework and rubric being assessed against, stakeholder coverage across engineering, finance, procurement, product, and leadership, tooling and its real usage, prior assessments, the practice's own operating model and headcount.
Owns: capability scoring against the rubric with evidence for each level rather than self-report, the gap analysis naming what is missing to reach the next level per capability, persona coverage showing which groups actually consume output and act on it and which receive reports nobody opens, the operating model with roles, cadences, and decision rights, the roadmap sequenced by dependency because allocation precedes chargeback and forecasting precedes commitment strategy, the metrics the practice is measured on with their current values, and the capabilities deliberately not being pursued with the reason.
Hands to: `finops-command-desk` for the engagement record, and back into whichever desk owns the highest-value gap.
Hard halt: source conflict. The assessment evidence and the practice's self-assessment disagree materially on a capability that a roadmap or a hiring case depends on. A maturity score is a funding argument, so a level claimed without evidence behind it puts investment against the wrong gap and the real gap stays where it was.

## Packet rule

Every stage updates `finops_packet` as defined in `references/suite-workflow-contract.md` before handing off. Source facts, assumptions, opportunities, anomalies, approvals, and open questions accumulate across stages and are never dropped to keep an artifact short. An opportunity removed from the register is removed with its reason and the period it was resolved in, because the same idle cluster gets rediscovered every quarter and the useful record is why it was left alone the last three times.
