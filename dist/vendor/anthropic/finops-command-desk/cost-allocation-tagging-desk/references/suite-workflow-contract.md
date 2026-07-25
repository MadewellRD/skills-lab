# FinOps Suite Workflow Contract

This file defines how FinOps Command Desk skills run as one continuous program of work rather than as a set of one-off cost questions. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is what the technology estate costs, who consumed it, what the organization got for the money, and which of those costs can be reduced without breaking something that earns revenue. The packet therefore carries the cost basis, the allocation state, and the evidence behind every savings figure alongside the totals, because the distinguishing failure of this domain is a number that is precise, well formatted, confidently presented, and not the number on the invoice.

Two properties of cost data drive most of what follows. Cost data is late: the current period is incomplete, corrections and credits land after the fact, and a month that looked final in a dashboard on the third gets restated on the eleventh. Cost data is also plural: the same consumption has a billed cost, an effective cost after commitments and discounts amortize, a list cost, and a contracted cost, and every one of them is correct for a different question. A figure without its cost basis and its as-of date is not a fact, it is a screenshot.

## Continuity rule

A desk that has the billing data and the allocation state to run the next stage runs it. A run that ends at "engineering should now review these instances" or "consider buying commitments" is a routing note, not FinOps work; it hands the analysis back to the person who asked what to do about the bill. Complete the current stage, update `finops_packet`, and continue until the requested outcome exists or a hard halt applies.

Three things are never continued through: an act that spends money or changes a running resource, a figure published outside the practice that no dataset supports, and a restatement of a closed accounting period. Everything else continues, with the assumption labeled inline against the account, service, workload, or opportunity it affects.

## Action boundary

This suite produces cost models, allocation rules, showback and chargeback reports, unit economics, budgets, forecasts, variance analyses, anomaly triage, optimization opportunities with sizing and risk, commitment recommendations, negotiation evidence packs, backlogs, scorecards, and maturity assessments. It does not purchase a commitment or a reservation, resize or terminate a running resource, delete a snapshot or a storage bucket, change an autoscaling policy, modify tag enforcement in a live account, post a journal entry, publish a chargeback to cost centers, set a budget of record, sign or countersign a provider agreement, open a billing dispute with a vendor, or cancel a subscription. For those acts the desk prepares the exact item, states what it costs or commits, names the authority level it requires, names what breaks if it is wrong, and stops at the gate.

The asymmetry to hold onto: a bad report wastes an afternoon, a bad purchase is locked in for one to three years, and a bad termination is an outage. Analysis is reversible and runs freely. Anything that reaches the estate or the ledger is somebody's decision to make, and the person who carries the consequence is the person who authorizes it.

Restating a closed accounting period, editing a posted allocation, backdating a rate, and deleting or overwriting a billing export are outside the boundary in every mode. The provider invoice and the general ledger are the record of what happened; a corrected copy that finance never posted is a second set of books.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a tag coverage report, a rightsizing candidate list, a commitment coverage snapshot, a unit cost calculation, or the root cause of one anomaly.
- `workflow_run`: the default for anything phrased as a cost review, an optimization pass, a budget cycle, a bill investigation, a margin question, a renewal, or a practice assessment. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `finops_packet` or halt-resume prompt. Re-pull the billing data rather than trusting the carried figure whenever a billing period has closed since, a correction or adjustment record could have landed, credits or a true-up have been applied, a commitment has been purchased or expired, or the estate has changed shape through a migration or an account move. A carried total silently inherits a period that has since been restated, and the restatement is never announced.
- `halt`: a hard class applies. Return the halt format below with the packet intact and the reversible analysis already done.
- `diagnostic`: the billing export, the cost platform, the telemetry, the contract, or the ledger cannot be reached. Report what was reachable, what was not, and precisely which totals, allocations, savings figures, or margin conclusions each gap makes unavailable. Do not reconstruct a missing month from the shape of the months around it.

## Request types

Every request carries a type, because the type sets the evidence bar, the stages that run, and the approval surface: `cost_spike`, `allocation_buildout`, `showback_report`, `unit_economics`, `budget_build`, `forecast`, `variance_review`, `optimization_pass`, `rightsizing_review`, `waste_sweep`, `commitment_review`, `commitment_purchase`, `license_review`, `contract_negotiation`, `chargeback_design`, `cogs_and_margin`, `engineering_cost_review`, `maturity_assessment`, `unknown`.

Two attributes travel with the type and change the evidence bar more than the type does.

**Decision class** records what the number is for: internal exploration, an engineering change, a purchase, a budget of record, a figure that leaves the company in a board pack or an investor metric, an audited financial statement, or a customer-facing margin commitment. The same analysis carries a different bar at each level, and the bar is set by where the number lands rather than by how confident the analysis feels.

**Period state** records whether the period in question is open, closed, or partial. A partial period cannot be trended or annualized without saying so. A closed period cannot be restated without the controller who owns the close. Most cost reporting arguments are period-state arguments that nobody labeled as such.

## The FinOps packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `unmeasured`, `untagged`, `unallocated`, and `not_reconciled` are legitimate values; an invented account identifier, savings figure, utilization percentage, commit amount, or owner is not.

```yaml
finops_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  request_type: "cost_spike | allocation_buildout | showback_report | unit_economics | budget_build | forecast | variance_review | optimization_pass | rightsizing_review | waste_sweep | commitment_review | commitment_purchase | license_review | contract_negotiation | chargeback_design | cogs_and_margin | engineering_cost_review | maturity_assessment | unknown"
  decision_class: "internal_exploration | engineering_change | purchase | budget_of_record | external_reporting | audited_statement | customer_commitment"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  engagement:
    question: "the decision this work has to support, in the requester's terms"
    requester: "who asked"
    finops_owner: "practitioner carrying the work, or unknown"
    budget_holder: "the person whose budget the answer lands on, or unknown"
    finance_partner: "FP&A or controller contact, or unknown"
    engineering_owner: "the team that would implement a change, or unknown"
    decision_deadline: "date a source states, or unknown"
    deadline_basis: "what makes the date real, for example a close date, a commitment expiry, a renewal notice window, a board meeting"
    materiality_threshold:
      amount: "figure below which findings are not individually tracked"
      basis: "the policy or practice standard that sets it"

  cost_basis:
    view: "billed | effective | amortized | list | contracted | blended | unblended"
    view_rationale: "why this view answers this question"
    amortization_treatment: "how commitment fees, upfront payments, and prepaid credits are spread"
    credit_treatment: "which credits, refunds, adjustments, and negotiated discounts are in or out"
    tax_treatment: "included or excluded, as the dataset carries it"
    support_and_fee_treatment: "how support charges, platform fees, and marketplace charges are handled"
    currency: "reporting currency"
    fx_source: "rate source and the date the rate was taken, where conversion applies"
    period:
      start: "period start"
      end: "period end"
      state: "open | closed | partial"
      partial_reason: "why the period is incomplete, for example export lag or a month in progress"

  datasets:
    - dataset: "the billing export, cost platform view, ledger extract, or telemetry source"
      provider: "the provider or vendor it covers"
      schema: "the export schema and version, for example a FOCUS-conformed dataset at its stated version"
      granularity: "resource, sku, account, or summary level"
      coverage_window: "the periods it actually contains"
      refresh_lag: "how far behind live consumption it runs"
      last_refresh: "timestamp the data was produced"
      known_limits: "what this dataset cannot answer"

  reconciliation:
    invoice_total: "the figure the provider actually billed"
    dataset_total: "the figure the analysis dataset sums to"
    variance_amount: "difference"
    variance_pct: "difference as a percentage"
    variance_explanation: "what accounts for it, for example credits applied outside the export, tax, or a correction record"
    state: "reconciled | reconciled_with_explained_variance | unreconciled | not_attempted"

  allocation:
    hierarchy: []                 # how cost rolls up, for example account -> cost center -> team -> product -> service
    tag_keys:
      - key: "tag or label key"
        required_for: "the scope it is mandatory on"
        enforcement: "how it is enforced, or none"
        coverage_pct: "measured coverage"
        value_hygiene: "known value drift, for example case and spelling variants"
    allocation_coverage_pct: "share of spend attributable to a named owner"
    unallocated:
      amount: "figure"
      pct: "share of total"
      largest_contributors: []    # accounts, services, or resources driving the gap
      reason_breakdown: []        # untagged, untaggable, shared, or in a structure that cannot carry a tag
    shared_cost_pools:
      - pool: "what the pool covers, for example network, observability, data platform, support, or licensing"
        amount: "figure"
        split_method: "proportional | even | fixed | usage_metric"
        driver: "the metric the split runs on, where usage-based"
        rationale: "why this method is defensible to the teams it charges"
        approved_by: "who signed off on the method, or unapproved"
    container_allocation:
      method: "how workload cost is derived from cluster cost"
      cost_drivers: "the resource dimensions used, for example requested versus used compute and memory"
      idle_capacity_treatment: "who carries cluster idle, and why"
      shared_namespace_treatment: "how platform namespaces are handled"
      clusters_in_scope: []
      tooling: "the source of the allocation data"

  reporting:
    audiences: []                 # engineering, finance, procurement, product, leadership, each with what they act on
    cadence: "how often each view is produced"
    views: []                     # the report set and what decision each one supports
    trend_baseline: "the comparison basis, for example prior period, prior year, or plan"
    known_distortions: []         # one-off charges, migrations, credits, or period effects that make a trend misleading

  unit_economics:
    - metric_id: "UE-01"
      metric: "the unit cost, for example cost per tenant, per transaction, per active user, per inference, per gigabyte served"
      numerator_scope: "which costs are in it and which cost basis"
      denominator: "the business volume"
      denominator_source: "the system of record for that volume"
      denominator_definition: "quoted, because the same word means different things in different systems"
      value: "computed figure"
      period: "the period it covers"
      trend: "direction with the comparison basis"
      owner: "who can move it"
      caveats: []                 # allocation gaps, shared cost assumptions, or denominator drift

  cogs:
    classification_policy_ref: "the policy that decides what lands in cost of revenue"
    cogs_lines: []                # what is classified into cost of revenue, with the rule that puts it there
    excluded_lines: []            # research, internal tooling, or sales infrastructure, with the rule that excludes it
    capitalization:
      policy_ref: "the internal-use software capitalization policy applied"
      capitalized_amount: "figure"
      basis: "what was capitalized and against which project"
    cogs_amount: "figure"
    revenue_basis: "revenue figure and where it came from"
    gross_margin_pct: "computed margin"
    period_state: "open | closed"
    controller_owner: "who owns the close for this period"
    ledger_variance: "difference between the cost dataset and the posted ledger, with its explanation"

  budgets:
    - budget_id: "B-01"
      scope: "what it covers"
      owner: "the budget holder"
      period: "the budget period"
      amount: "approved figure"
      basis: "how it was built, for example prior run rate, driver model, or bottom-up plan"
      consumed_to_date: "figure"
      remaining: "figure"
      variance_amount: "against plan to date"
      variance_drivers: []        # what actually caused the variance, not the service it appeared under
      alert_thresholds: []
      approval_state: "draft | submitted | approved"

  forecast:
    method: "run_rate | driver_based | seasonal | bottom_up | hybrid"
    drivers: []                   # the business or technical drivers the model runs on, with their sources
    horizon: "how far out it projects"
    projection:
      - period: "period"
        amount: "figure"
        range: "expected range where the method produces one"
        confidence_basis: "what makes this credible, for example prior accuracy or committed pipeline"
    known_step_changes: []        # migrations, launches, decommissions, or renewals that break the trend
    accuracy:
      prior_period_error: "measured error against actuals"
      method: "how the error is measured"
    commitment_trajectory:
      agreement_ref: "the commitment agreement this tracks against"
      commit_amount: "the contracted commitment"
      term_end: "when the term ends"
      consumed_to_date: "figure"
      required_run_rate: "the run rate needed to meet the commitment"
      projected_position: "shortfall, on track, or overage, with the figure"

  anomalies:
    - anomaly_id: "AN-01"
      detected_on: "date"
      detection_basis: "the threshold or model that flagged it"
      scope: "account, service, region, or resource"
      delta_amount: "the spend difference"
      baseline: "what it is being compared against"
      duration: "one-off, ongoing, or recurring"
      state: "new | triaged | explained | expected | waste | false_positive"
      root_cause: "the change that caused it, with the evidence that establishes it"
      correlated_change: "the deployment, migration, config change, or usage event it lines up with"
      owner: "who owns the resolution"
      recurrence_control: "what stops it happening again, or none"

  opportunities:
    - opportunity_id: "OPT-01"
      lever: "rightsizing | scheduling | waste_removal | storage_tiering | architecture | commitment | rate | licensing | data_transfer | retention"
      scope: "the resources, workloads, or subscriptions it applies to"
      current_state: "measured current cost and utilization"
      proposed_state: "what changes"
      estimated_savings:
        amount: "figure"
        period: "monthly, annualized, or over the term"
        baseline: "what the saving is measured against"
        confidence: "the basis for the estimate, not a bare adjective"
      savings_type: "realized | cost_avoidance"
      overlaps_with: []           # other opportunity ids that touch the same spend
      net_of_overlap: "the saving that remains once overlap is removed"
      implementation_effort: "the work required, with who does it"
      performance_risk: "what could degrade, and the evidence behind that judgment"
      blast_radius: "what is affected if it goes wrong"
      reversibility: "how the change is undone, and how quickly"
      owner: "the team that must act"
      state: "identified | accepted | scheduled | implemented | verified | rejected | superseded"
      rejection_reason: "why, where rejected, because the same finding will resurface next quarter"
      realized_amount: "what actually showed up on the bill"
      realization_evidence: "the billing line that demonstrates it"

  commitments:
    portfolio:
      - instrument_id: "identifier from the provider or the tracking system"
        type: "spend_commitment | usage_commitment | reservation | capacity_reservation"
        scope: "what it applies to, including any flexibility across families or regions"
        term: "term length"
        payment_option: "as purchased"
        commitment_rate: "the hourly or periodic amount committed"
        start: "start date"
        end: "expiry date"
        utilization_pct: "share of the commitment actually consumed"
        coverage_pct: "share of eligible usage it covers"
        exchangeable: "true | false"
        cancellable: "true | false"
        break_even: "the point at which it pays back"
    targets:
      coverage_target: "with the basis for the target"
      utilization_floor: "the level below which a commitment is destroying value"
    effective_savings_rate: "blended saving against the stated baseline, with the baseline named"
    expiring_within_horizon: []   # instruments expiring soon, with the cliff each one creates
    stranded_commitment: []       # commitment paid for and not consumed, with the cause
    purchase_recommendations:
      - instrument: "what to buy"
        quantity: "how much"
        term: "term length"
        payment_option: "which option and why"
        assumed_baseline_usage: "the post-optimization usage this is sized against"
        projected_saving: "figure with its baseline"
        downside_case: "what this costs if usage falls, quantified"
        approver_required: "the role the authority matrix names"
        approval_state: "not_requested | pending | granted | denied"

  licensing_saas:
    - application: "the product"
      vendor: "the vendor"
      agreement_ref: "the contract this sits under"
      spend_annual: "figure"
      seats_or_units_purchased: "figure"
      seats_or_units_active: "figure with how activity is measured"
      utilization_pct: "computed"
      renewal_date: "date"
      notice_window: "the window and the last safe date to act"
      auto_renew: "true | false | unknown"
      license_model: "bring_your_own | included | consumption | seat"
      counts_toward_commitment: "whether this spend draws down a provider commitment"
      duplication: "overlapping tools covering the same need"

  commercial:
    agreements:
      - agreement_ref: "the agreement"
        provider: "counterparty"
        structure: "spend commitment, private pricing, volume tier, or marketplace arrangement"
        commit_amount: "the contracted amount"
        term_start: "date"
        term_end: "date"
        discount_structure: "as the agreement writes it"
        consumed_pct: "drawdown to date"
        shortfall_exposure: "the true-up figure if the trajectory holds"
        eligible_spend_definition: "what counts toward the commitment, as written"
    negotiation_inputs: []        # the spend trajectory, workload mix, growth case, and alternatives that give the ask its weight
    asks: []                      # each ask with what it is worth, quantified
    leverage_basis: "what actually gives the organization position, evidenced"
    renewal_timeline: "the dates that constrain the negotiation"

  chargeback:
    model: "showback | proportional | fixed_allocation | usage_based | internal_rate_card"
    model_rationale: "why this model suits the organization's structure"
    ledger_ties_to_invoice: "true | false"
    tie_out_variance: "the difference and its explanation, where one exists"
    postings:
      - cost_center: "the receiving cost center"
        amount: "figure"
        period: "period"
        basis: "the allocation rule that produced it"
        state: "draft | approved | posted"
    disputes:
      - dispute_id: "D-01"
        cost_center: "who disputes"
        amount: "the amount in question"
        basis: "the grounds"
        state: "open | investigating | upheld | adjusted | withdrawn"
        resolution: "what changed, including any allocation rule change it forced"

  governance:
    policies: []                  # tagging requirements, provisioning guardrails, budget alert thresholds, purchase authority levels, retention defaults
    approvals:
      - item: "the purchase, change, posting, or publication requiring authorization"
        amount_at_stake: "figure"
        required_approver: "the role the authority matrix names"
        authority_basis: "the policy or matrix provision that sets the level"
        state: "not_required | pending | granted | denied"
        granted_by: "named human"
        granted_on: "date"
    exceptions: []                # granted exceptions with their owner, rationale, and expiry

  maturity:
    framework_ref: "the assessment framework in use"
    capability_scores:
      - capability: "the capability assessed"
        score: "the level with the rubric it came from"
        evidence: "what demonstrates the level, not what the team believes"
        gap: "what is missing to reach the next level"
        owner: "who owns the gap"
    persona_coverage: []          # which stakeholder groups actually consume FinOps output and act on it
    roadmap_items: []             # sequenced improvements with their owners and dependencies

  source_facts:
    - fact: "source-backed fact"
      source: "billing_export | cost_platform | provider_console | invoice | contract | erp_ledger | budget_file | tagging_inventory | cmdb | telemetry | container_metrics | apm | vendor_statement | ticket | user | unknown"
      locator: "the dataset, report, account, or document and the field it came from"
      as_of: "the period and refresh time the figure belongs to"
  assumptions:
    - assumption: "what was assumed"
      affects: "the figure, allocation, opportunity, or conclusion it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. The provider invoice is authoritative for what was actually billed. Every published total ties to it or carries a stated and explained variance. A dashboard that disagrees with the invoice is wrong regardless of how well it renders.
2. The billing and usage export is authoritative for the composition of that invoice at the granularity it carries, subject to its lag and its correction behavior. Cost management consoles are a view over this data with their own filters and defaults, so a console figure that cannot be reproduced from the export is treated as a lead rather than a fact.
3. The executed agreement governs rates, discounts, commitment amounts, eligible spend, and true-up mechanics. A discount observed in the data is an effect; the agreement is the cause, and only the agreement says what happens if the commitment is not met.
4. The general ledger is authoritative for what was recognized, in which period, against which cost center. Cost tooling and the ledger disagree routinely because of accrual timing, capitalization, and intercompany treatment, and the ledger is what an auditor reads.
5. Utilization telemetry, container metrics, and application performance data are authoritative for what a workload actually used and how it behaved. They are not authoritative for cost, and the join between a metric and a cost line is an inference that carries its own error.
6. The tagging inventory and the configuration database are claims about ownership. Where they disagree with the account structure and the cost center mapping in the ledger, the ledger wins for financial reporting and the disagreement is recorded as a hygiene finding rather than smoothed.
7. Team statements, tickets, and architecture intent are context and history. They explain why spend moved and they are frequently the fastest route to a root cause, but "we turned that off last month" is checked against the bill before it becomes a fact.

Where a lower layer contradicts a higher one on a load-bearing figure, record both readings with their locators. Do not resolve toward whichever reading makes the saving look larger or the variance look smaller.

## Measurement discipline

- Every figure carries its cost basis, its period, and the refresh time of the dataset behind it. Billed and amortized figures are not comparable, and the gap between them is widest exactly where commitments are heaviest, which is exactly where the interesting questions are.
- The current period is incomplete. Do not trend, annualize, or compare a partial period without stating that it is partial and how much lag the dataset carries. Month-over-month comparisons that include a partial month are the most common self-inflicted cost scare in the practice.
- Late-arriving records restate history. A figure quoted from a period that has since closed is re-pulled rather than carried, because corrections, credits, and refunds land after the fact and nobody sends a notification when a number changes.
- Realized savings and cost avoidance are different things and are reported separately. A realized saving reduces the next invoice and can be pointed at. An avoidance reduces a cost that was never going to be billed, which is a legitimate result and an illegitimate line in a savings total.
- Two recommendations against the same spend do not add. Rightsizing an instance and committing to that instance overlap, scheduling a workload down and reserving capacity for it overlap, and stacking them is the standard mechanism by which an optimization backlog reports more savings than the service costs.
- The baseline is stated with every saving. A saving against list price, against on-demand equivalent, against last quarter's run rate, and against the plan are four different numbers, and the largest of them is the one that gets quoted if nobody names which is in use.
- Untagged is not unowned; it is unattributed. Cost that cannot be attributed is reported as unallocated, with what would allocate it. Assigning it to the team that looks most likely is how an allocation model loses the trust it takes a year to build.
- Percentages carry their denominator. Coverage, utilization, allocation, and margin percentages all move sharply depending on what sits underneath them, and a percentage without its base is a rhetorical device.
- Unit cost denominators come from the system of record for that business metric, and the definition is quoted. Active user, customer, tenant, and transaction each mean several different things inside one company, and picking the flattering definition is indistinguishable from picking the right one in the artifact.
- Blended rates across consolidated accounts are a billing artifact, not the cost of anything an engineer can change. Never hand a team a blended figure and ask them to reduce it.
- Currency conversion carries the rate and its date, and mixed-currency totals say which rate applied to which portion.
- A resource that is measured over a window shorter than its business cycle is not measured. Utilization over three quiet days is evidence about three quiet days, and month-end, quarter-end, batch, and seasonal peaks are exactly where rightsizing causes incidents.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with locators and as-of dates, its labeled assumptions, and the figures it could not establish. Section headings with the numbers deferred mean the stage did not run. Later stages consume the packet rather than re-querying the billing data, so a total that was estimated once travels into a unit cost, then a margin, then a board slide, and by then nobody remembers that the first figure was a placeholder.

## Parallel surface

Independent items fan out and are parallel-safe: accounts and subscriptions, services, resources, clusters and namespaces, tags and tag keys, teams and cost centers, workloads, anomaly candidates, optimization opportunities, SaaS applications, budget lines, and the separate analysis lanes for rightsizing, waste, architecture, licensing, and rate work each stand on their own inputs. Connector preflight across the billing export, the cost platform, telemetry, the ledger, and the contract set is parallel too.

Aggregation is a single pass after the fan-out returns, and in this domain the aggregate is where the truth lives. Reconciling the dataset to the invoice is a statement about the whole bill. Allocation coverage is a percentage of the total and cannot be assembled from per-team views that each look complete. The chargeback ledger has to balance to the invoice, so it is built once over the full set rather than per cost center. Commitment sizing is inherently global: commitments float across the estate, so a per-team recommendation double-counts the same eligible usage, and the portfolio is sized once against post-optimization usage for the whole footprint. Net savings after overlap removal is the same shape of problem, since the overlaps are precisely what a fan-out cannot see. Forecast rollup, effective savings rate, and gross margin are all whole-set figures.

The commitment portfolio is the one that must never be split. Two workstreams each sizing commitments for their own scope will each produce a defensible recommendation, and the combined purchase over-commits the estate against usage that only exists once. That mistake is not correctable for the length of the term.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what is spent, broken, misstated, or committed if the workflow continues anyway, with the figure where one exists>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact figure or dataset, or both readings when sources disagree, with locators and as-of dates>
Sources attempted: <what was queried or opened and what it returned>
Required approval or access: <named approver role and authority basis, or the dataset, contract, or system needed>
Proceeding meanwhile: <reversible analysis that does not depend on the blocked fact>
Preserved packet: <full finops_packet>
Resume prompt: <prompt that restarts the workflow once the data, access, or approval arrives>
```

A halt justified by uncertainty rather than consequence is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the figure or opportunity it affects.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
