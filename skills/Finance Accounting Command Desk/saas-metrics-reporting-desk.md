---
name: saas-metrics-reporting-desk
description: build arr and mrr with the movement bridge from opening through new expansion contraction and churn to closing across the whole customer base, reconcile the run rate to recognized revenue, define and compute net and gross revenue retention and logo and revenue churn, and produce burn multiple cac payback magic number and efficiency metrics with a definition change register. use for saas metrics, arr bridges, retention cohorts, churn analysis, investor and board metric packages, diligence metric rebuilds, and metric definition disputes.
---

# Saas Metrics Reporting Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it runs after `cash-flow-treasury-desk`, because the efficiency metrics take burn as an input and burn only means one thing once its definition is fixed. Inside a workflow, produce the metric artifacts, update `finance_packet`, and continue into `budget-planning-desk`, which builds the revenue plan on the retention and expansion rates settled here. `references/stage-contracts.md` states what each later stage inherits, and `references/suite-workflow-contract.md` defines the packet, the source hierarchy that makes the executed contract authoritative for what was promised, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would publish externally, confidential information would be exposed, sources genuinely disagree on a load-bearing figure, a metric would leave the company without the contract base behind it, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the customer, cohort, or metric it affects.

Never invent a contract value, a start or end date, a customer, a churn event, a cohort population, a definition, or a prior period metric value. A metric the contract base cannot support yet is named as not computable with the data that would make it computable, and a definition the company has not written down is recorded as undefined rather than inferred from the number somebody quoted last quarter.

## Role

Own the operating metrics that describe the subscription business, and own the definitions underneath them. That means annual recurring revenue and its monthly equivalent with the annualization rule stated, the movement bridge from opening through new, expansion, contraction, and churn to closing, built once across the whole customer base and closing exactly; the reconciliation that shows why the run rate and recognized revenue legitimately differ; net and gross revenue retention with their cohorts, windows, and treatment of upsell and downgrade; logo and revenue churn defined separately because they answer different questions; burn multiple, customer acquisition payback, magic number, and growth against margin measures with the exact costs and periods that go into each; and a register of every definition change, because a metric that improved by being redefined is the most common way a trend misleads.

These figures leave the company more reliably than any others in this suite. They get built into valuations, written into covenants, and rebuilt line by line during diligence by somebody with the contract base in front of them and no interest in how it was computed originally.

## Use when

- ARR, MRR, or the movement bridge is being produced for a board package, an investor update, or an internal review.
- Retention or churn is being computed, or two people are quoting different retention numbers from the same data.
- A diligence process, a lender, or an investor has asked for the metric set and expects it to rebuild from the contract base.
- The run rate and recognized revenue have diverged and somebody wants to know whether that is a problem or a definition.
- Efficiency metrics are needed and the costs and periods that belong inside them have not been settled.
- A definition is being changed, or a prior period series was built on a definition nobody wrote down.
- A large contract has an unusual structure, a ramp, a usage component, or a services element, and it is about to be annualized incorrectly.

## Do not use when

- The question is when revenue is recognized on a contract under the accounting framework: `revenue-recognition-desk`.
- Recognized revenue by stream for a closed period is the deliverable: `financial-reporting-desk`.
- The invoice does not match the contract: `billing-order-to-cash-desk`.
- Burn or runway is the liquidity question rather than a metric input: `cash-flow-treasury-desk`.
- Retention and expansion rates are being used to build next year's revenue plan: `budget-planning-desk`.
- The metric moved against plan and the cause is the question: `variance-analysis-desk`.
- The customer is not paying rather than not renewing: `accounts-receivable-collections-desk`.

## Required evidence

- The contract base with customer, contract value, recurring against non-recurring components, start and end dates, ramp schedules, usage minimums, and any termination or non-renewal notice already served.
- Recognized revenue by stream for the period from the reporting stage, with its period status.
- The customer and cohort structure, including how customers are grouped and whether the grouping has changed.
- Churn, downgrade, and non-renewal events with their effective dates and the document that establishes each.
- Prior period metric values together with the definitions that produced them, not only the numbers.
- Sales and marketing spend by period with the components included, and gross margin by revenue stream, for the efficiency metrics.
- Net burn with its definition from the treasury stage.
- The written definitions document where the company has recorded what each metric means, and its version history.
- Currency and the treatment of non-reporting-currency contracts, since a retention rate can move entirely on translation.

## Workflow

**Outcome.** A metric set that rebuilds from the contract base without a second conversation: ARR with its as-of date and its annualization rule, a bridge that closes exactly with each movement traced to an event, a reconciliation between the run rate and recognized revenue that names each legitimate difference, retention and churn with their cohorts and windows written on the same artifact as the numbers, efficiency metrics with their inputs itemized, caveats where a cohort change or a one-off contract makes a trend misleading, and a definition register showing what changed and when.

**Grounding.** The executed contract governs what is recurring, what is committed, and for how long; the billing system says what was invoiced and only the contract says what was promised. Churn events govern churn, meaning a dated termination, non-renewal, or downgrade with a document behind it. Recognized revenue from the closed ledger governs the reconciliation target. Written definitions govern the computation, and where none exist the definition adopted is stated explicitly in the artifact as the definition adopted rather than presented as the company's.

**Constraints.**

- The bridge is built once across the whole customer base. Assembled per segment it will foot within each segment and not across them, because a customer who downgraded one product and expanded another is a single net movement rather than two independent ones.
- The annualization rule is stated and applied consistently: how multi-year contracts are treated, how a ramp is handled before it steps up, how usage and overage are annualized or excluded, and how professional services and one-time fees are kept out. A month annualized with a one-time fee inside it produces an ARR that no contract supports.
- Contraction and churn are different events and are separated. A customer who reduced seats is contraction, a customer who left is churn, and merging them makes gross retention unreadable.
- Retention carries its cohort, its window, and its denominator. Net and gross revenue retention answer different questions and the difference between them is exactly the expansion the business earned, so presenting one without the other hides the more informative of the two.
- The reconciliation between run rate and recognized revenue is a bridge of named differences: timing of starts and ends within the period, ramps, usage above or below the recurring base, services revenue, and any recognition pattern that is not ratable. A residual is stated as unreconciled at its full amount.
- Every efficiency metric names its inputs. Customer acquisition payback changes materially depending on whether it uses gross new ARR or net new ARR, which sales and marketing costs are inside it, and whether it is gross margin adjusted. Burn multiple names the burn definition and the net new ARR definition on the same line as the result.
- One-off contracts and cohort composition changes are called out as caveats. A trend that moved because one large customer entered or left the population is a composition change wearing the costume of a business result.

Where a metric definition changes, the order is mandated: compute the current period on the definition previously in force, compute it on the new definition, restate the prior period series on the new definition, and present the new series only after that, with the change and its effect disclosed. The order is mandated because a current period computed on a new definition and shown against history computed on the old one manufactures a movement the business never produced, and once that series has gone to a board or an investor it becomes the anchor every later period is judged against, so the correction reads as a restatement of the metric rather than as the improvement it actually was.

**Parallel surface.** Independent items fan out: individual contracts under parsing for their recurring component, customers under churn and expansion classification, cohorts under retention computation, and separate efficiency metrics each stand on their own inputs. Two passes are aggregate and run once after the fan-out returns. The ARR bridge is a closed loop over the entire customer base at one point in time, so opening plus new plus expansion less contraction less churn equals closing across the whole population or the bridge has not closed. And the reconciliation to recognized revenue is a single pass against the period's reported revenue, because per-customer reconciliations that each look reasonable still miss the total.

**Acceptance bar.** ARR carries its as-of date, its annualization rule, and what is included and excluded. The bridge closes exactly across the whole base, and where it does not, the difference is reported at its full amount rather than absorbed. Every movement in the bridge traces to a dated event with a document. Retention states its cohort, window, denominator, and the treatment of upsell and downgrade. Every efficiency metric lists its inputs and periods. Every definition in use is either cited to the definitions document or stated in the artifact as the definition adopted for this run. Caveats name the specific contract or cohort change that makes a trend misleading.

## Outputs

A complete run delivers the set:

- `arr-and-bridge.md`: ARR with its as-of date and basis, the movement bridge from opening to closing with each component, and the customer-level events behind each movement.
- `annualization-rules.md`: what counts as recurring, how multi-year, ramped, usage-based, and services components are treated, how currency is handled, and the boundary cases the contract base actually contains.
- `arr-to-revenue-reconciliation.md`: the run rate at the period end against recognized revenue for the period, with each legitimate difference named and quantified, and any residual stated as unreconciled.
- `retention-and-churn.md`: net and gross revenue retention with cohort, window, and denominator; logo and revenue churn defined separately; the underlying churn and downgrade events with their effective dates.
- `efficiency-metrics.md`: burn multiple, customer acquisition payback, magic number, and growth against margin measures, each with its inputs, its periods, and the sensitivity of the result to the input choices.
- `definition-change-register.md`: every definition currently in force, what changed since the prior period, when, who approved it, and the restated effect on the prior series.
- `metric-caveats.md`: cohort composition changes, one-off contracts, currency effects, and anything else that makes a period-over-period comparison misleading, each tied to the metric it distorts.
- `saas-metrics-downstream-handoff.md`: what `budget-planning-desk` and `forecast-scenario-desk` inherit, with the metrics the contract base cannot yet support named.

Depth standard: an artifact is complete when a diligence analyst rebuilds the number from it using the contract base. A bridge line reads as the customer, the event, the effective date, the amount, and the document. A retention figure reads as the cohort population, the starting ARR, the ending ARR from that same population, and the treatment applied to each movement type. An efficiency metric shows its numerator and denominator as figures, not as names.

Where the run covers one metric or one segment rather than the full set, scope the artifacts and say so. Where the contract repository, the billing system, or the ledger cannot be reached, `saas-metrics-diagnostic.md` names what was attempted, what returned, and which metrics are unavailable as a result.

The hazard specific to this desk is arithmetic rather than fluency. A bridge closes by construction if any one of its five lines is computed as the residual of the other four, and churn is invariably the line handed that job, because it is the one nobody wants to go looking for events to support. Churn built by subtraction is a number with no customer behind it, and it is the first line a diligence team rebuilds from the contract base. Every movement in the bridge originates from a dated event with a document; where the events do not account for the closing balance, the bridge is reported as not closing, at the full difference, with the population that could not be explained named. The same discipline applies to a retention denominator: a cohort quietly re-based to exclude the customers who left is a defensible-looking number describing a population chosen for its outcome.

## finance_packet fields to update

- `saas_metrics.definitions_ref` and the definition change register; `saas_metrics.arr.value`, `.as_of`, `.basis`, `.bridge` with each component, and `.reconciliation_to_revenue`.
- `saas_metrics.retention` with cohort, window, and treatment; `saas_metrics.churn` with logo and revenue churn defined separately.
- `saas_metrics.burn_multiple`, `saas_metrics.cac_payback`, `saas_metrics.magic_number`, `saas_metrics.rule_of_40`, each with its inputs named.
- `saas_metrics.caveats[]` with the contract, cohort, or definition change that distorts each affected trend.
- `approvals[]` for any external publication of a metric set and for any definition change, with `required_approver` and `authority_basis`.
- `source_facts` with the contract base, churn events, and revenue figures read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: publishing a metric set to investors, a lender, a board, or a data room, and adopting or changing a definition. A metric that has been published becomes the baseline every later period is measured against, and a definition change is a communication decision rather than a computation.
- **Production or destructive**: the next act would overwrite the prior metric series, re-base a published cohort, or change the definitions document of record.
- **Security or privacy**: an artifact would carry customer names alongside contract pricing that the agreement treats as confidential, or would expose commercial terms to an audience the contract does not permit.
- **Source conflict**: the contract, the billing system, and the customer record disagree on value, term, or end date; a churn event has a different effective date in two systems; or the prior period metric cannot be reproduced from the definition it was supposedly built on.
- **Release integrity**: a metric would go outside the company without the contract base behind it, a bridge would be presented that does not close, or a run rate would be presented where a reader will read it as revenue. An ARR figure that cannot be rebuilt during diligence costs more than the round it was prepared for.
- **Connector unreachable**: the contract repository, the billing system, or the ledger exists and cannot be read, so a metric would describe a customer base that was never examined.

A contract whose signed version has not surfaced, a churn event whose effective date is unconfirmed, a customer whose usage component is still being measured, and a sales cost allocation nobody has settled are soft gaps. Compute what the data supports, label the assumption against that customer or metric, and record the question.

## Downstream handoffs

`budget-planning-desk` takes the retention, expansion, and churn rates as the basis for the revenue build, with the cohort and window attached so the plan is not built on a rate computed differently from how it will be measured. `forecast-scenario-desk` takes the bridge components as forecastable drivers and the caveats that make a trend unreliable. `financial-reporting-desk` takes the metric definitions and reconciliations for the board package and for any non-GAAP presentation. `cash-flow-treasury-desk` takes net new ARR where it feeds an efficiency measure back into the burn conversation. `audit-support-desk` takes the contract base workings where a diligence or audit process asks for the rebuild.

## Quality bar

A good metric package is one a stranger can rebuild. The bridge closes from events rather than from subtraction, every rate carries its cohort and window, and the difference between the run rate and recognized revenue is explained rather than apologized for. The definitions register is the tell of a serious operation: a company that has changed a definition and disclosed it reads as disciplined, while a series that has been silently consistent for eight quarters through two product launches and a pricing change usually means nobody looked. And the caveats section earns the most trust, because naming the one contract that flatters the quarter is the thing a diligence team was going to find anyway.
