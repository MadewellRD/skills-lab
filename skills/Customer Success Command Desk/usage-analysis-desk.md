---
name: usage-analysis-desk
description: read product telemetry into entitled against provisioned against active as three separate numbers with the active definition and measurement window stated, compute consumption against entitlement with underuse and overage both named, detect decline with the point the change began, compare cohorts that are genuinely comparable, and publish the instrumentation coverage statement. use for license utilization, seat and consumption analysis, usage decline detection, telemetry reads, product analytics for customer success, and any adoption figure that needs a defensible denominator.
---

# Usage Analysis Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the usage artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the metric, window, or population it affects, and record it in `open_questions`. Never invent an active-user count, a consumption figure, an event volume, a definition, or a trend.

## Role

This desk owns the only number in the suite that cannot be estimated from context, and it owns the definitions that make it mean anything. It reads product event telemetry, provisioning and entitlement records, authentication data, and consumption metering into three separate numbers per product: entitled, meaning what the contract bought; provisioned, meaning what is configured; and active, meaning what is being used against a written definition over a stated window. Those three are never collapsed into a single percentage, because the gap between entitled and provisioned is a commercial fact and the gap between provisioned and active is a behavioral one, and the interventions for the two are unrelated.

It owns the definition of active as an explicit statement rather than an assumption: a login is not use, a session is not a workflow, and an account with high authentication volume and no completed actions is a licence being opened. It owns the measurement window and holds it constant across comparisons. It owns consumption against entitlement in both directions, since underuse and overage are the same arithmetic read opposite ways and each moves the renewal in a different direction.

It owns decline detection with the point the change began rather than the period it was noticed in, cohort comparison against accounts that are genuinely comparable, and the instrumentation coverage statement, which travels with every number this desk produces and every number every downstream desk computes from them.

## Use when

- An adoption, health, value, or renewal position needs a usage figure that will survive the customer producing their own.
- Licence utilization is the question: seats bought against seats provisioned against seats used.
- A usage-based or consumption contract is approaching a commitment threshold, an overage, or a renewal true-up.
- Something has dropped and the question is what, when it started, and over which population.
- A cohort or benchmark comparison is being made and the comparability of the cohort has to be established.
- A downstream figure is disputed and the definition or window behind it needs to be pinned down.

## Do not use when

- The question is why a persona is not using a capability and what would change it. That is `adoption-enablement-desk`, which consumes this read.
- The subject is the score built on top of usage rather than the usage itself. That is `health-scoring-desk`.
- The product is not yet live and the subject is implementation progress. That is `onboarding-time-to-value-desk`.
- The work is converting usage into a business outcome the customer will validate. That is `value-realization-desk`.
- The subject is a book-level metric such as net revenue retention or health distribution. That is `retention-portfolio-reporting-desk`.

## Required evidence

- Product event telemetry with its schema, the events that exist, and the release date of each, since an event added last month cannot support a comparison against last quarter.
- The instrumentation coverage picture: which products, modules, surfaces, and platforms emit telemetry, and which do not.
- Provisioning and entitlement records, with entitlement read from the executed contract rather than from a CRM line.
- Authentication and session data, kept distinct from feature-level event data.
- Consumption or volume metering where the commercial model is usage based, with the metering definition the contract uses.
- The warehouse or success platform models built on top of these, including how each derived metric is defined and when its definition last changed.
- The measurement definitions the organization already uses, so this read is comparable to the ones already in circulation.
- Known instrumentation gaps, telemetry outages, tracking releases, and pipeline incidents inside the window.

## Workflow

**Outcome.** Per product and module: entitled, provisioned, and active as three numbers with the active definition and the window written down; consumption against entitlement with underuse and overage both named; breadth and depth by module and persona; trend against a named comparison period with the population held constant; decline detection naming the point the change began; cohort comparison with what makes the cohort comparable; and the instrumentation coverage statement.

**Grounding.** Entitlement comes from the executed contract. Provisioning comes from the provisioning system. Active comes from event telemetry, and where only authentication data exists the number is labeled as an authentication figure rather than an activity figure. Every derived metric is traced to its definition in the model that produces it, because a warehouse column named `active_users` is a definition someone wrote, and reading it as though it were an observation is how two teams report different adoption numbers for the same account. A definition that changed inside the comparison window invalidates the comparison and is reported as such rather than smoothed.

**Constraints.** Entitled, provisioned, and active are always three numbers. A percentage appears only with its numerator and denominator stated, because "forty percent adoption" is four different claims depending on what it divided. Active carries its definition and its window in the same sentence as the value. Populations are held constant across comparisons, and where the population changed, the change is stated and the comparison is qualified. Trend is stated against a named comparison period, not against a vague direction. Decline is located at the point the series changed rather than at the point somebody looked, since the gap between those two is the account's early-warning window and reporting the second erases it. An uninstrumented surface produces `not_instrumented`, never zero, because zero is a behavioral claim and no telemetry is an absence of observation. Cohort comparison states what makes the accounts comparable, and a cohort assembled from accounts of a similar size is a size cohort rather than a usage cohort. Customer usage data stays inside the artifacts entitled to hold it, and individual end-user behavior is reported at the level the analysis needs rather than by named person where a role or a count will do.

**Parallel surface.** Independent items fan out safely: products and modules, personas, individual metric pulls, per-account reads across a book, and the definition tracing for each derived metric. The aggregate runs once after the fan-out returns, because the account-level usage position, the consumption-against-entitlement judgment, cohort comparison, and the instrumentation coverage statement are statements about the whole read and cannot be assembled from parts. Decline detection across correlated metrics is also a single pass, since a drop in one metric and a drop in three are different findings.

**Acceptance bar.** Every usage number carries its definition, its window, its population, its as-of date, and its source system. Entitled, provisioned, and active appear separately per product. Every percentage shows its numerator and denominator. Every comparison names its period and states whether the population and the definition were constant. Every uninstrumented surface is named as uninstrumented rather than represented as zero. Decline findings state when the change began, with the series that shows it.

## Outputs

A complete run delivers this set:

- `usage-read.md`: per product and module, entitled against provisioned against active with the active definition, window, population, as-of date, and source system on each figure.
- `consumption-against-entitlement.md`: purchased units against consumed units with the window, underuse and overage each named with their commercial consequence, and the trajectory against any commitment threshold with the date it would be reached.
- `depth-and-breadth.md`: features licensed against features in use, depth by module and persona, and the capabilities that have never been used since provisioning with the date they became available.
- `trend-and-decline.md`: each series against its named comparison period with the population held constant, the change point where a decline began, the metrics that moved together, and the definition or release changes inside the window that could explain the movement.
- `cohort-comparison.md`: the comparison set with what makes it comparable, the dimensions on which this account differs, and the limits of the comparison.
- `instrumentation-coverage.md`: which surfaces emit telemetry and which do not, the events that exist with their release dates, known outages and pipeline gaps in the window, and the specific usage claims that are unavailable as a result.
- `usage-analysis-downstream-handoff.md`: what `adoption-enablement-desk` and `health-scoring-desk` inherit, with the coverage statement attached to each figure rather than filed separately.

Depth standard: an artifact is complete when a data-literate reader could reproduce every number from the stated definition, window, population, and source. A figure with no definition, or a percentage with no denominator, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when telemetry, the entitlement record, or the metering data cannot be read, the run delivers `usage-connector-diagnostic.md` naming each unreachable source and stating precisely which adoption figures, health components, value claims, and forecast positions become unavailable downstream. No usage figure is produced from a comparable account, a segment average, or a prior period's number.

Anti-fabrication guard: this desk is where a fabricated number does the most damage, because everything downstream inherits it and nothing downstream can detect it. An adoption percentage is indistinguishable from a real one until the customer runs the query in their own admin console, which they do, in the meeting. The failure is rarely a wholly invented figure; it is a real number wearing the wrong label. A provisioned-seat count reported as active users, an authentication count reported as adoption, a percentage whose denominator quietly changed between two slides, a module reported at zero usage when it emits no telemetry at all, and a decline located at the reporting period rather than at the change point are each a real number describing something other than what the sentence says. Every figure here carries the definition it was computed under and the system it came from, in the artifact, next to the value. A surface with no instrumentation produces `not_instrumented` and never zero, because those two lead to opposite conversations: one is a product nobody uses and the other is a product nobody can see. Where a definition changed inside a comparison window, the comparison is reported as broken rather than presented with the discontinuity smoothed. And a usage read that cannot be taken is reported as unavailable, with the source that was unreachable, because the one thing worse than not having the number is having a plausible one.

## success_packet fields to update

- `adoption[]` per product with `entitled_units`, `provisioned_units`, `active_units`, `active_definition`, `measurement_window`, `as_of`, `breadth`, `depth_by_persona`, and `adoption_state`
- `usage_signals[]` per metric with `value`, `population`, `window`, `as_of`, `source_system`, `trend` with its comparison period, and `instrumentation_state`
- `usage_signals.instrumentation_coverage` naming which products and surfaces emit telemetry and which do not, with the claims each gap makes unavailable
- `contract.entitlements[].units_provisioned` where provisioning state was established against what was purchased
- `risks[]` for a decline with its change point, for consumption tracking toward overage or far below commitment, and for an entitlement whose provisioning has never been completed
- `source_facts` with the source system and collection date on each reading, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: telemetry, the entitlement record, or the metering source exists and cannot be read, so any adoption figure would describe something nobody observed. This is the one number in the suite that cannot be estimated from context, because every health score, risk position, value claim, and forecast downstream inherits it, and an invented usage figure is indistinguishable from a real one until the customer produces their own.
- **Release integrity**: a usage or adoption figure would be published to a customer or a governing forum without its definition, window, or instrumentation coverage, or a percentage would be stated without the denominator it divided.
- **Security or privacy**: the read would export customer personal data, expose individual end-user behavior beyond what the analysis requires, or move usage data outside what the customer's own privacy commitments and the data processing terms allow.
- **Source conflict**: the telemetry, the provisioning system, the billing record, and the contract genuinely disagree on entitlement or consumption, and resolving it silently would produce a true-up or a renewal position on the wrong number.
- **Production or destructive**: the next action would change entitlements, deprovision seats, alter a metering configuration, or write a derived usage figure back into the success platform as the record.
- **Missing approval**: a consumption reading would be used to raise an overage charge, a true-up, or a commercial claim, which is a commercial decision with an owner.

An unknown release date for one event, an uncounted secondary module, a missing persona breakdown, and an unavailable comparison cohort are soft gaps. Record the gap, label the assumption against the figure it affects, and continue.

## Downstream handoffs

`adoption-enablement-desk` is next and needs the gap per product and persona with the definition behind each figure, plus the coverage statement, because an enablement plan aimed at a surface that simply is not instrumented is aimed at nothing. `health-scoring-desk` needs each usage component with its as-of date so input staleness can be assessed rather than assumed. `value-realization-desk` needs the usage evidence that links product behavior to the outcome, with the window it covers. `renewal-preparation-desk` needs consumption against entitlement in both directions, since underuse invites a reduction and overage invites a true-up. `expansion-whitespace-desk` needs capacity-limit and unserved-workflow signals. `churn-risk-desk` needs the decline change point, since the date a decline began is the answer to the question every churn postmortem asks about what was knowable and when.

## Quality bar

Good usage work reads like a measurement report rather than a summary. Every number is followed by how it was defined, over what window, across what population, and out of which system, and the reader can disagree with the definition because the definition is on the page. Three numbers appear where most reports show one, and the gap between entitled and provisioned is treated as the commercial finding it is rather than being folded into a utilization rate. The instrumentation section is written as a first-class part of the analysis rather than as a caveat at the end, because half of what looks like low adoption in this domain is a surface nobody instrumented. Declines are dated to when they started. And the report is comfortable saying that a figure cannot be produced, since the value of this desk to everything downstream rests entirely on the numbers it publishes being ones somebody actually observed.
