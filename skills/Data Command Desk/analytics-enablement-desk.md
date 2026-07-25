---
name: analytics-enablement-desk
description: design the analytics consumption layer covering certified datasets and dashboards per persona, self-serve boundaries and the joins that produce wrong numbers, fan-out and grain-breaking query anti-patterns, dashboard hygiene with duplicates and orphans, reverse-etl and operational analytics, ad-hoc request intake, and the threshold that converts a repeated request into a modeled asset. use when analysts are drowning in ad-hoc requests, dashboards have multiplied, or self-serve users keep producing wrong numbers.
---

# Analytics Enablement Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the consumption artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A dashboard whose usage cannot be measured is a soft gap and stays in the inventory as unmeasured; a reverse-ETL sync that would write into a live operational system is a production action and stops at the gate. Never invent dashboard names, view counts, user counts, request volumes, personas, or the identity of whoever maintains a report.

## Role

Own the layer consumers actually touch. This desk defines certified datasets and dashboards per persona, the self-serve boundary including which joins produce wrong numbers, the query patterns and grain-breaking anti-patterns, dashboard hygiene covering duplicates and orphans, the reverse-ETL and operational analytics path, the ad-hoc intake, and the threshold at which a repeated request becomes a modeled asset.

This stage is where a modeling failure becomes a business decision. Everything upstream can be correct and the consumption layer can still produce a wrong number, because a consumer joining two facts at different grains gets rows back, not an error. The second property is economic rather than technical: an analytics team that answers every ad-hoc request individually converts itself into a query service and never models the asset that would end the requests, so the intake design and the promotion threshold are as load-bearing here as the dataset design.

## Use when

- Consumers need certified datasets or dashboards and the personas, their questions, and their tooling need mapping.
- Self-serve access is being opened or tightened, and the boundary between what a consumer may build and what will produce a wrong number needs stating.
- Users are producing wrong numbers from correct data through fan-out joins, double counting, filtering that moves a denominator, or averaging a ratio.
- Dashboards have multiplied and need a hygiene pass that separates duplicates, orphans, and abandoned reports from the ones a business actually runs on.
- The ad-hoc request load is unsustainable and needs an intake path, a triage rule, and a promotion threshold that turns recurring questions into modeled assets.
- Data needs to return to an operational system through reverse-ETL, and the destination, the sync semantics, and the failure behavior need designing.
- Onboarding or documentation is generating repeated questions that are really questions about grain, join keys, and what a column means.
- A certified metric layer exists and consumers are still building their own versions of the same figure.

## Do not use when

- The subject is what a metric means, its expression, or which of two definitions is correct. That is `metric-semantic-layer-desk`; this desk exposes what that stage certified.
- The subject is who is permitted to see a dataset, row-level predicates, or column masking. That is `data-governance-access-desk`; this desk states what an audience needs and that desk decides what it may reach.
- The subject is the model, its grain, or its keys. That is `data-modeling-desk`, which this desk escalates to when a recurring request needs a new modeled asset.
- The subject is dashboard freshness alerting or detection coverage. That is `data-observability-desk`.
- The subject is measured usage and lineage of an asset. That is `lineage-catalog-desk`, whose usage figures this desk consumes rather than re-deriving.

## Required evidence

- The certified metrics with their grain validity and refused slices, and the marts beneath them with declared grain and keys.
- BI usage logs: dashboards and reports with view counts, distinct viewers, last-opened dates, and scheduled delivery lists, which is what separates an orphan from a quarterly report.
- Query history from the consumption layer, including the ad-hoc queries consumers write themselves, which shows the joins they are actually performing.
- The dashboard and report inventory across every tool in use, including workbooks and spreadsheets fed by scheduled extracts.
- The ad-hoc request queue with its volume, requesters, recurring themes, and the turnaround the team currently sustains.
- The consumer personas with their tooling and their competence, stated from evidence rather than from an org chart.
- Existing reverse-ETL syncs, their destination objects, their field mappings, their cadence, and what the receiving system does with the records.
- Onboarding material, data dictionaries, and the questions that keep being asked despite them.

## Workflow

**Outcome.** A consumption design per persona naming the surface each audience uses and what it is trusted to build, a certified dataset and dashboard set with the question each answers, a self-serve boundary stating the permitted joins and the ones that produce wrong numbers, a query pattern and anti-pattern guide, a dashboard hygiene disposition per asset, a reverse-ETL design where operational delivery is in scope, an intake and triage design with the promotion threshold, and the documentation gaps that generate recurring questions.

**Grounding.** Personas come from observed behavior rather than from titles: the audience that writes SQL, the audience that pivots an extract, and the audience that opens one dashboard on Monday need different surfaces, and query history distinguishes them. Dashboard disposition rests on usage measured over a window that spans the reporting cycle, since a report opened four times a year at quarter close is not an orphan. Recurring requests are counted from the queue rather than estimated, because the promotion threshold is only defensible if the count behind it is real. Where the certified layer and a consumer's own query compute the same figure differently, that is a metric conflict and it travels back rather than being smoothed over here.

**Constraints.** The self-serve boundary is written as specific permitted and forbidden joins with the reason, not as a competence tier. Name the fact-to-fact join that fans out, the dimension join at the wrong grain that duplicates the measure, the many-to-many bridge that needs an allocation rule, the filter on a dimension that silently changes a denominator, the distinct count that does not sum across periods, and the ratio that cannot be averaged. Every certified asset names the question it answers, its grain, its refresh cadence, its owner, and what it must not be used for, since the misuse statement is what prevents the next wrong number. Reverse-ETL is designed as a write into a system of record: the destination object and field mapping, the matching key, the conflict rule when the operational system already holds a value, the sync cadence and its lag, the behavior on partial failure, and the fact that a bad figure delivered here becomes an action taken on a customer rather than a chart nobody opened. That last property is why any new or widened reverse-ETL sync carries a named approval from the owner of the receiving system before it runs. Dashboard hygiene disposes of every asset in the inventory rather than the interesting ones, and an asset with unmeasurable usage is dispositioned as unmeasured rather than as unused.

**Parallel surface.** Personas, individual dashboards, certified datasets, reverse-ETL destinations, and the per-asset hygiene assessment are independent units and fan out safely, as does harvesting query patterns per audience. The aggregate work runs once after the fan-out returns: deduplicating dashboards that answer the same question across tools, composing the self-serve boundary so it is consistent across every surface an audience can reach, ranking the ad-hoc themes to set the promotion threshold, and reconciling the certified set against what consumers actually open. A per-dashboard review that never composes into a portfolio view retires the reports nobody defends and leaves the six duplicates of the executive summary intact.

**Acceptance bar.** A named persona could find the certified asset for their question, understand the grain and the joins without asking, and be refused a join that would produce a wrong number. Every dashboard in the inventory carries a disposition with its usage evidence. Every recurring request theme is either answered by a certified asset or recorded as a modeling candidate with its request count.

## Outputs

A complete run delivers this set:

- `consumption-design.md`: per persona, the surface, the tooling, the questions they bring, what they are trusted to build, and the path from a question to an answer.
- `certified-asset-set.md`: per certified dataset and dashboard, the question it answers, its grain, its underlying model, its refresh cadence, its owner, and the uses it is explicitly not valid for.
- `self-serve-boundary.md`: permitted joins and filters with their grain, the forbidden ones with the wrong number each produces, and the escalation path when a consumer needs something outside the boundary.
- `query-patterns.md`: worked patterns for the recurring question shapes and the anti-patterns beside them, each showing what the wrong version returns rather than only that it is wrong.
- `dashboard-hygiene.md`: every asset in the inventory with measured usage, its window, and a disposition of keep, consolidate, deprecate, or unmeasured, with the duplicates grouped by the question they share.
- `reverse-etl-design.md`: destinations, field mappings, matching keys, conflict rules, cadence, failure behavior, and the approval state of each sync into an operational system.
- `enablement-intake.md`: the request intake and triage design, the recurring themes with their counts, the promotion threshold that converts a theme into a modeled asset, and the documentation gaps behind the repeated questions.
- `enablement-downstream-handoff.md`: what `data-governance-access-desk` inherits, including the audiences, the surfaces they reach, and the datasets each persona has been designed to receive.

Depth standard: an artifact is complete when a consumer could self-serve from it and an analytics engineer could act on the modeling candidates without reopening the queue. A self-serve boundary stated as a principle, a hygiene list with no usage evidence, and a reverse-ETL entry with no conflict rule are unfinished rather than draft.

When BI usage logs, the dashboard inventory, or the request queue exists and cannot be read, the run delivers `enablement-connector-diagnostic.md` naming each unreachable source and the disposition and threshold claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: the damage this desk can do is retirement by assumption. A dashboard whose name looks superseded, whose owner left, and whose usage log the run could not read is exactly the shape of the report a controller opens once a quarter to close the books, and a hygiene list that quietly moves it to deprecate reads as diligence right up until the quarter ends. So no asset is dispositioned as unused without a usage measurement and the window it covered, and where the measurement is unavailable the disposition is unmeasured, which is a finding rather than a failure. The same restraint applies to the demand side: request counts, viewer counts, and turnaround figures come from the queue and the logs or are reported as uncounted, because a promotion threshold justified by an invented volume commits an engineering team to build an asset for demand that was never there. Personas are drawn from observed query behavior rather than composed into a tidy set of three, and a dashboard's owner is quoted from the tool or recorded as unowned rather than attributed to the team that most likely maintains it.

## data_packet fields to update

- `catalog[].certification` and `catalog[].usage` for assets certified, consolidated, or deprecated at this stage
- `data_products[].consumers` and `output_port` where a persona surface or a reverse-ETL destination is added
- `metrics[].certification` where exposure through the consumption layer changes the certification requirement
- `access_policies[].purpose_limitation` drafted per audience as input to the governance stage
- `data_risks[]` for wrong-number paths a consumer can currently reach and for unowned reports in active use
- `open_questions` for every recurring request theme with no modeled asset behind it
- `source_facts` with per-fact attribution, `decisions`, `assumptions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would delete or unpublish a dashboard, revoke a scheduled delivery, or activate or widen a reverse-ETL sync that writes into a live operational system.
- **Missing approval**: retiring a report a named consumer still opens, certifying a dataset for an audience, or writing data back into a system of record needs the owner of that report, dataset, or system, who has not agreed.
- **Security or privacy**: a persona surface, an extract, or a reverse-ETL mapping would place personal, health, or cardholder data in front of an audience whose access has not been established, or would deliver restricted fields into an operational system with a wider reader set.
- **Source conflict**: the certified definition and a widely used consumer query genuinely disagree on the same figure, which belongs to `metric-semantic-layer-desk` for adjudication rather than being reconciled in a dashboard.
- **Release integrity**: a dataset or dashboard would be marked certified, or an asset declared unused, without the usage evidence and owner acceptance that support the claim.
- **Connector unreachable**: BI usage logs, the dashboard inventory, query history, or the request queue needed to disposition assets exists and cannot be read.

An unknown dashboard owner, a persona with no documented tooling, an unmeasured request theme, and a missing onboarding document are soft gaps. Name them, label the assumption, and continue. The requirement that a retirement rest on measured usage and that a write into an operational system carry its owner's approval are never relaxed to reduce a dashboard count.

## Downstream handoffs

`data-governance-access-desk` is next and needs the personas, their surfaces, and the datasets each is designed to receive, since purpose limitation is defined against an audience and a use. `data-modeling-desk` receives the modeling candidates with their request counts. `metric-semantic-layer-desk` receives every consumer-authored figure that competes with a certified definition. `lineage-catalog-desk` receives the consolidated and deprecated assets so the graph and catalog match what exists. `data-observability-desk` receives the certified dashboards that need a freshness signal beneath them. `data-platform-cost-desk` receives dashboard refresh frequency and extract schedules, which are frequently a larger spend driver than the pipelines that feed them. Send business process change and operational workflow design around a reverse-ETL destination to the owning business suite as a labeled cross-suite handoff.

## Quality bar

Good enablement work is specific about wrongness. It does not tell a consumer to be careful with joins; it names the join, the grain it breaks, and the number that comes back inflated. Certified assets say what they are not for. The hygiene pass dispositions every asset and shows the usage window behind each call, including the ones it could not measure. The intake design has a counted threshold rather than a sentiment about workload, so the decision to model an asset is defensible to whoever funds it. Reverse-ETL is treated as an operational write with a conflict rule and an owner, not as a delivery channel. And the documentation produced explains grain, keys, and joins rather than click paths, because every recurring question this stage sees is ultimately a question about what one row means.
