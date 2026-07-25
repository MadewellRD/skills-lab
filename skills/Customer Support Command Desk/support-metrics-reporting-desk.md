---
name: support-metrics-reporting-desk
description: report support numbers that leave the team, with every metric carrying its written definition, its population, its exclusions, its window, and its source system, satisfaction reported with response counts and response rates, response and resolution times computed on the contractual calendar with pause treatment stated, backlog by cohort, breach rate and credit exposure against contractual targets rather than configured ones, and the decision each figure is being brought for. use for qbrs, leadership reviews, board and customer-facing service reporting, and metric definition disputes.
---

# Support Metrics Reporting Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the reporting artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the metric it affects, and record it in `open_questions`. Never invent a value, a definition, a population, an exclusion, a response rate, a comparison figure, a target, or a source system.

## Role

This desk owns the numbers once they leave the team, which is the moment their properties stop being an internal matter. A figure in a leadership review sets headcount and tooling budget. A figure in a quarterly business review with an enterprise customer is read as contractual performance and is quoted back during renewal. A figure in a board pack is repeated for a year by people who will never see how it was computed.

Every metric in this domain has several defensible definitions, and the spread between them is routinely larger than any improvement a team will make in a quarter. First response time depends on whether it starts at arrival or at queue entry, whether an auto-acknowledgement counts, and whether it runs on the contractual calendar or on elapsed time. Resolution time depends on whether pending-customer periods are excluded and on which pause rule was applied. First contact resolution depends on the reopen window. Satisfaction depends entirely on who answered. So this desk's product is not the value; it is the value with its definition, its population, its exclusions, its window, and its source attached, tightly enough that they travel together.

Two properties get lost most often and cost most. Response rate on any survey-derived metric, because a score from eleven responses across four hundred solved tickets is a statement about eleven people, and the people who answer a support survey are correlated with the outcome being measured. And the difference between the contractual target and the configured one, because breach rate computed against the SLA policy in the helpdesk is a report about the configuration, while the credit the customer can claim is settled against the agreement.

The desk also owns the last mile: tracing movement to the queue, macro, driver, or defect behind it, and naming the decision each figure is being brought to the forum for. A number with no decision attached is a chart, and it will be discussed for twenty minutes and change nothing.

## Use when

- Support numbers are going to a leadership forum, a board pack, a QBR, or a customer-facing service review.
- A metric definition is disputed, or two reports of the same period disagree.
- Satisfaction, first response time, resolution time, first contact resolution, reopen rate, backlog age, contact rate, containment, cost per contact, or breach rate needs reporting properly.
- Contractual SLA performance needs stating against the agreement rather than against the configured policy.
- A number has moved and the movement needs tracing to something real before anyone acts on it.
- A metric set needs designing, or an existing one is measuring things nobody makes decisions on.
- A prior figure needs restating because its definition, population, or source has changed since.

## Do not use when

- The subject is the current queue and its aging rather than the reported period. That is `queue-backlog-health-desk`, which produces the cohort data this desk reports.
- The question is what is generating the demand behind a number. That is `contact-driver-analysis-desk`, which runs before this stage.
- The figures are about people's interaction quality and their sampling limits. That is `quality-assurance-review-desk`.
- The volume, staffing, and coverage model is the subject. That is `workforce-coverage-desk`.
- A calculation is wrong because the platform is configured wrongly and the fix is a policy, field, or view change. That is `support-tooling-automation-desk`.
- The report is one account's incident performance and its credits. That is `post-incident-followup-desk`, which owns the credit position.

## Required evidence

- The metric definitions actually in force, written out, with their effective dates and any change inside the reporting window.
- The source system behind each metric, and any difference between the raw ticket record and the reporting layer's computation of the same thing.
- The population each metric is computed over, with every exclusion applied and the rule behind it: merges, duplicates, spam, machine-generated tickets, internal tickets, and incident-generated contacts.
- Response counts and response rates for every survey-derived metric, with the population surveyed, the instrument, the trigger, and any suppression applied.
- The window and the comparison period, with any change between them in customer population, plan mix, product mix, coding rules, or configuration.
- The contractual targets from the executed agreements, and the configured SLA policies, kept separate where they differ.
- Calendar and pause treatment for every time-based metric, including timezone and holiday schedule.
- Prior reported figures as they were published, with their definitions at the time.
- The forum the numbers are going to, its audience, and the decisions on its agenda.

## Workflow

**Outcome.** A metric set where each figure carries its value, its written definition, its population, its exclusions, its window, its as-of date, and its source system; satisfaction reported with response counts and response rates; time-based metrics computed on the correct calendar with pause treatment stated; backlog reported by cohort; breach rate and credit exposure stated against contractual targets with the configured position alongside where they differ; movement traced to the queue, macro, driver, or defect behind it; and the decision each figure is being brought for.

**Grounding.** Every value comes from a named source over a stated window, and where the reporting layer and the raw record disagree, both are shown rather than reconciled toward the one that reads better. Definitions are quoted as they are written rather than described, since a paraphrased definition is a new definition. Contractual targets come from the agreements, and the configured policy is reported as configuration. Satisfaction comes with the instrument, the trigger, the suppression rules, and the response rate over the surveyed population. Comparisons hold the counting rules constant across both periods, and where a rule, a field, or a configuration changed inside the window, that discontinuity is shown on the series rather than left to be read as a trend.

**Constraints.** No figure leaves this desk without its definition, population, exclusions, window, and source. No survey-derived number is reported without its response count and response rate in the same place as the value. No time-based metric is reported without its calendar and its pause treatment. Backlog is reported by cohort with pending states separated, never as a single open count. Breach rate is reported against the contractual targets, with the configured reading shown separately where it differs, and the difference is never resolved silently toward compliance. Where a definition changed inside the window, the series is broken at that point and both definitions are shown rather than restating history under the new one. No individual agent's figures appear in a report going outside the team, because a team report is not a performance instrument. Customer-facing service reports carry only that customer's data, and no metric is presented as a contractual position without the agreement behind it.

**Parallel surface.** Independent items fan out safely: each metric computed from its own source over the stated window, each definition retrieved and quoted, each population and exclusion set resolved, each survey-derived figure's response rate computed, and each customer-facing report assembled per account. Four passes are single after the fan-out returns. The coherence read is set-level by definition, since metrics that must reconcile with each other, such as inflow, outflow, backlog movement, and resolution volume, only expose a contradiction when they are seen together. The comparison narrative is one statement across both periods. The movement tracing is a single pass, because a change in one number is usually explained by another number in the same set. And the report itself is written once, since a figure worded differently in two sections is the discrepancy the forum will spend its time on.

**Acceptance bar.** Every metric carries value, written definition, population, exclusions, window, as-of date, and source system. Every survey figure carries its response count and response rate. Every time-based metric carries its calendar and pause treatment. Breach and credit figures are stated against the contract with the configured reading alongside where it differs. Every comparison names what changed in the population between periods. Every definition change inside the window appears as a break in the series. Every figure names the decision it is being brought for, or is removed from the report.

## Outputs

A complete run delivers this set:

- `metric-register.md`: one entry per metric with its value, its definition quoted as written, its population, its exclusions with the rule behind each, its window, its as-of date, its source system, and its owner.
- `period-report.md`: the reporting narrative with each figure in context, the movement traced to the queue, macro, driver, defect, or population change behind it, and the decision each figure is being brought to the forum for.
- `satisfaction-report.md`: satisfaction and effort scores with the instrument, the trigger and suppression rules, the surveyed population, the response count, the response rate, the verbatim themes, and an explicit statement of what a rate at that level supports.
- `sla-performance-report.md`: response, restoration, and resolution performance against the contractual targets per plan and per account, on the correct calendar with pause treatment stated, the configured-policy reading alongside where it differs, the breach list, and the credit exposure the terms attach.
- `backlog-and-aging-report.md`: backlog by cohort with pending-customer and pending-engineering separated, inflow against outflow, and the counting rules stated so this period can be compared with the next.
- `definition-change-log.md`: every definition, population, exclusion, calendar, or configuration change affecting the series, its date, its effect on the figures, and the prior figures that are no longer comparable.
- `customer-facing-service-report.md`: the per-account report carrying only that account's data, its contractual targets, its performance against them, its incident history, and its credit position, with anything unverifiable removed rather than softened.
- `metrics-downstream-handoff.md`: what goes back into the desks the forum directs work into, with the decisions taken, the figures they rest on, and the open questions the numbers did not answer.

Depth standard: an artifact is complete when the first competent question from the forum is already answered inside it, and when a figure could be recomputed next period to the same definition without asking anyone. A metric whose definition is described rather than quoted, or a satisfaction score without its response rate on the same line, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the reporting layer, the raw ticket record, the survey platform, or the agreement store cannot be reached, the run delivers `metrics-connector-diagnostic.md` naming each unreachable source and precisely which metrics are unavailable because of it. The definition register and the definition change log still ship, because both are the part of this work that does not depend on this period's data, and a forum that receives written definitions with the values pending is better served than one that receives values nobody can define.

Anti-fabrication guard: the failure that matters here is not a number pulled from nowhere; it is a real number whose properties were quietly chosen after seeing it. A definition selected because it flatters the figure, an exclusion added because it removes the outliers that hurt, a comparison period chosen because it makes the direction right, a response rate omitted because it is embarrassing, and a figure carried forward from last quarter's deck because this quarter's query failed are all common, all invisible to the audience, and all produce a report that is defensible line by line and false as a whole. In these artifacts the definition is fixed before the value is computed and is quoted rather than paraphrased, every exclusion names the rule that has always applied rather than one introduced for this run, the comparison period is the standard one or the deviation is stated in the report, and a figure that could not be computed this period is shown as unavailable rather than repeated from the last one. A survey score always appears with its response count and rate in the same sentence, since separating them is how eleven responses become a company-wide satisfaction claim. And where the contractual and configured readings differ, both are printed, because reporting only the compliant one is the specific act that converts a breach into a number the customer will discover for themselves.

## support_packet fields to update

- `metrics[]` with one entry per metric carrying `value`, `definition` written out, `population` including exclusions, `window`, `as_of`, `source_system`, `response_rate` for anything survey-derived, and `comparison` naming the prior period and what changed in the population
- `queue_health[]` referenced rather than recomputed, so the period report and the queue read cannot disagree
- `entitlement.targets[]` and `clocks[]` used as the basis for breach reporting, with the contractual reading held distinct from the configured one
- `incident.credits_triggered` and the credit exposure carried into the reported breach position
- `drivers[]` referenced for the movement tracing, so a metric change points at a driver rather than at a trend
- `approvals[]` for any customer-facing service report, contractual performance statement, or externally published figure
- `open_questions` for every metric the sources could not support, and `assumptions` for every definition applied where none was documented
- `source_facts` with collection timestamps, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a metric would reach a leadership forum, a customer, or a contractual review without its definition, its population, or its exclusions. These figures set headcount, tooling budgets, and in enterprise accounts they are reported as contractual performance; a satisfaction score quoted without its response rate and a resolution time computed on the wrong calendar are both defensible in isolation and both wrong in the decision they produce.
- **Source conflict**: the reporting layer and the raw ticket record return different values for the same metric and window, or the contractual targets and the configured SLA policy disagree on what counts as a breach. Preserve both readings; adopting the configured one silently converts a contractual breach into a compliant metric.
- **Missing approval**: a customer-facing service report, a contractual performance statement, or an externally published figure would be sent. It becomes the company's stated position on its own performance, it is filed by the customer, and it is produced at renewal.
- **Security or privacy**: the report would carry another customer's data into an account-facing report, expose individual agent performance outside the team, or include ticket content and personal data in a document with a wide distribution.
- **Production or destructive**: the next action would overwrite a published figure, restate a prior period in place, or change a definition in the reporting layer without recording the break in the series.
- **Connector unreachable**: the reporting layer, the raw ticket record, the survey platform, or the agreement store exists and cannot be read, so a figure would be reported that nobody computed this period.

An unavailable cost per contact, a missing benchmark, an unowned metric, and an unexplained small movement are soft gaps. Report the metric with the gap stated on it, and say plainly where a figure is not available rather than approximating it.

## Downstream handoffs

This stage returns to `customer-support-command-desk` for the program record, and then back into whichever desks the forum directs work into. `queue-backlog-health-desk` receives any commitment made about backlog or breach reduction, with the capacity assumption it rests on. `workforce-coverage-desk` receives headcount and coverage decisions taken on these figures, since a decision made on an inflated containment rate becomes a coverage gap two months later. `contact-driver-analysis-desk` receives the movements this report could not explain, because an unexplained change in resolution time or satisfaction is almost always a driver, a macro, or a defect. `quality-assurance-review-desk` receives any satisfaction pattern that needs testing against what the interactions actually contain. `support-tooling-automation-desk` receives every definition this report found to be uncomputable with the current fields, since that is a configuration problem wearing a reporting label. `severity-sla-desk` receives any contractual target discrepancy, which affects live tickets rather than only the report.

## Quality bar

Good reporting is boring to write and hard to argue with. Definitions are quoted rather than described, and they sit next to the number rather than in an appendix, because the appendix is not read and the number is. Satisfaction never appears without its response count and rate in the same sentence, since the first honest question about a satisfaction score is how many people answered it. Time-based figures name the calendar and say what happened to paused time, so the customer whose four-hour target ran across a weekend and the internal chart agree about the same ticket. Breach performance is stated against the contract, with the configured reading printed alongside when they differ, because that gap is a finding and hiding it is the one act in this desk that is genuinely indefensible. Movement is traced to something real: this queue, that macro, this driver, that defect, rather than described as a trend. Every figure has a decision attached, and the figures with no decision behind them are cut, since a report that fits on two pages and changes something beats a dashboard nobody acts on. And when a definition changed mid-window, the chart shows the break rather than the improvement.
