---
name: metric-semantic-layer-desk
description: define metrics and the semantic layer covering metric expressions with filters exclusions and denominators, entity dimension and measure modeling, grain validity, additive semi-additive and non-additive aggregation, distinct counts that do not roll up, time basis timezone and fiscal calendar, metric certification and ownership, restatement policy for definition changes, and competing definitions of the same kpi preserved until adjudicated. use when two dashboards disagree on the same number or a metric needs an owned definition.
---

# Metric Semantic Layer Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the metric definition artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Two definitions of one metric name is a source conflict by construction, and it halts on adjudication rather than being resolved toward whichever expression looks cleaner. Never invent a metric expression, a filter, an exclusion, a denominator, a fiscal calendar boundary, an owner, or a certification state.

## Role

Own what a number means. This desk holds the metric definition set written as real expressions, the entity, dimension, and measure model the semantic layer exposes, grain validity and the dimensions a metric may be sliced by without becoming wrong, additivity classification with the aggregation rule for semi-additive and non-additive measures, the time basis and fiscal calendar, certification and ownership, the restatement policy for a definition change that moves a published number, and the competing definitions preserved with their sources until an owner adjudicates.

The distinguishing property of this stage is that its output is not a computation but an agreement, and the failure it prevents is unusually expensive. Two teams reporting different revenue figures is a visible problem that gets solved; two teams reporting the same figure computed differently is an invisible one that survives until an external filing forces a reconciliation. The second property is that a metric is only valid at certain grains, and the semantic layer's real job is refusing the slices that silently produce a wrong number rather than serving every slice a consumer can request.

## Use when

- Two dashboards, a report, and a spreadsheet disagree on a metric that carries one name, and the definitions need collecting, comparing, and adjudicating.
- A metric needs a definition written as an expression, including the filters, exclusions, denominator, and time basis that the name does not carry.
- A semantic layer is being designed or extended and entities, dimensions, measures, and their join paths need modeling.
- A measure is being sliced by a dimension it is not valid at, or a ratio is being averaged across a dimension where only its components may be summed.
- Balances, inventory levels, headcount, subscription counts, or any semi-additive measure needs an explicit aggregation rule across time against the rule across other dimensions.
- The time basis is ambiguous: booking date against ship date against recognition date, a timezone that shifts a day boundary, or a fiscal calendar that does not align to months.
- A definition change would move a figure that has already been published, and a restatement policy and notification path are needed before the change lands.
- A metric is being certified, or the current certification rests on nobody in particular.

## Do not use when

- The subject is whether the underlying data is correct rather than what it means. That is `data-quality-desk` for the assertion and `data-incident-response-desk` when a wrong number is already in front of consumers.
- The subject is the grain, keys, or additivity of the physical fact table itself. That is `data-modeling-desk`; this desk consumes the declared grain and refuses the slices it does not support.
- The subject is which dashboard an audience uses, dashboard hygiene, or self-serve boundaries. That is `analytics-enablement-desk`, which consumes the certified definitions produced here.
- The subject is which dashboards a change would break. That is `lineage-catalog-desk`, whose impact analysis this desk uses to scope a restatement.
- The subject is a financial control, statutory reporting policy, or an accounting treatment. That is a labeled cross-suite handoff to the Finance suite, and this desk records the definition it implies rather than adjudicating the treatment.

## Required evidence

- The marts and their declared grain, keys, and measure additivity, since a metric's validity is bounded by the fact table beneath it.
- Every existing computation of the metric wherever it currently lives: semantic layer definitions, BI tool calculated fields, dashboard-level filters, saved queries, scheduled reports, notebooks, and the spreadsheet a team maintains by hand.
- The reports and audiences each definition feeds, and whether any figure has left the organization or entered a filing.
- The owners who can adjudicate, which means the person accountable for the number rather than the person who built the dashboard.
- The fiscal calendar, period close dates, timezone convention, and currency conversion policy including the rate and the date it is applied on.
- Late-arriving data behavior for the underlying facts, since a metric that changes retroactively needs a stated as-of policy.
- Query history and BI usage showing which definition is actually being read, which is frequently not the certified one.
- Any existing certification, glossary entry, or metric catalog, read as documented intent rather than as state.

## Workflow

**Outcome.** A metric definition set with each definition written as an expression including its filters, exclusions, and denominator; the entity, dimension, and measure model with join paths; grain validity and the invalid slices stated per metric; additivity with the aggregation rule for every semi-additive and non-additive measure; the time basis, timezone, and fiscal calendar; certification state with a named owner; a restatement policy; and the competing definitions preserved as separate entries with their sources and the adjudication left open.

**Grounding.** A definition is quoted from where it actually runs, not composed to look canonical. The BI tool's calculated field, the dashboard filter applied above the query, and the semantic layer measure are three different definitions even when they carry the same name, and the difference is usually a filter nobody documented. Where a definition and its documentation disagree, the running expression is actual state and the document is intent, and both are recorded. Which definition is most read is measured from usage rather than assumed from certification, because the certified metric is frequently the one nobody queries.

**Constraints.** Every metric names the exact expression, the source model, the grain it is valid at, the dimensions that are invalid slices with the reason, the time basis field and timezone, the additivity class, and the owner. Exclusions are stated positively: test accounts, internal orders, cancelled and refunded rows, deleted records, and zero-value transactions are named individually rather than folded into a filter clause nobody can read. Ratios carry their numerator and denominator as separate measures so the layer can refuse to average them; a ratio aggregated by averaging its own values across a dimension is the most common silent error this stage exists to prevent. Distinct counts are marked as non-additive, since a count of distinct users per day does not sum to a count per week and a layer that lets it will produce that sum. Semi-additive measures name the rule per dimension: a balance sums across accounts and takes the closing or average value across time, and the choice is recorded because both are defensible and only one matches the report. Competing definitions are held as separate entries with their sources and their consumers, never merged, and the adjudication is named as open with the owner who must close it.

**Parallel surface.** Individual metrics, the collection of existing definitions per metric, dimension and entity modeling, and the per-metric grain validity assessment are independent units and fan out safely, as does harvesting definitions across BI tools, repositories, and saved queries. The aggregate work runs once after the fan-out returns: reconciling competing definitions of the same name against each other, checking metrics that share a denominator or a conformed dimension for mutual consistency, composing the entity and join-path model so two metrics from different facts can appear on one row, and scoping a restatement across every affected report. Reconciling two definitions is by definition not parallel with itself, since the finding is the difference between them.

**Ordered gate for a definition change that moves a published figure.** Changing a certified definition, correcting a filter, or repairing a denominator runs in this order, because a number that has been published cannot be withdrawn, only restated, and a figure that changes quietly between two readings destroys the reader's ability to trust either version:

1. Quantify the movement before deciding anything: compute the metric both ways over the published periods and record the variance per period and per audience.
2. Derive from lineage every report, export, filing, and external recipient that carries the old value, including figures already sent outside the organization.
3. Obtain the named approval from the metric owner and, where the figure entered a financial or regulatory report, from the accountable owner of that report.
4. Notify the consumers who acted on the old value before the new value appears, stating the size and direction of the change and the periods affected.
5. Publish the corrected definition with its version and effective date, restate the affected periods, and record the restatement with the old value, the new value, and the reason.

Step 1 precedes step 3 because an approver cannot consent to an unquantified change, and step 4 precedes step 5 because once the figure is corrected there is no longer any artifact a consumer can use to work out which of their decisions rested on the old one.

**Acceptance bar.** A reader could compute each certified metric from its written definition alone and reproduce the published figure, could tell which slices are refused and why, and could see for every contested metric how many definitions exist, where each runs, who reads each, and who must adjudicate. No metric is recorded as certified without a named owner who accepted it.

## Outputs

A complete run delivers this set:

- `metric-definitions.md`: per metric, the expression with filters, exclusions and denominator, source model, grain validity and invalid slices, additivity with its aggregation rule, time basis and timezone, owner, and certification state.
- `semantic-model.md`: entities, dimensions, measures, join paths, and the conformed dimensions two metrics must share to be shown on one row, with the join paths that produce fan-out named as forbidden.
- `competing-definitions.md`: every name computed more than one way, each variant quoted from where it runs with its consumers and its measured usage, the numeric difference between variants over a real period, and the owner who must adjudicate.
- `time-and-calendar-basis.md`: the date field per metric, timezone convention, fiscal calendar and period boundaries, currency conversion rate and date, and the as-of policy for late-arriving facts that move a closed period.
- `certification-register.md`: certification state and owner per metric, the review cadence, and the metrics whose current value depends on a definition nobody owns.
- `restatement-policy.md`: what qualifies as a restatement, the versioning and effective-dating scheme, the approval path, the notification template, and the record kept per restatement.
- `metric-downstream-handoff.md`: what `analytics-enablement-desk` inherits, including which definitions are safe to expose for self-serve and which slices the layer must refuse.

Depth standard: an artifact is complete when an analyst could implement the definition in the semantic layer and a finance reader could agree the expression matches what they mean. A definition stated in words without its filters, a grain validity claim with no invalid slice named, and a certification with no owner are unfinished rather than draft.

When BI metadata, the semantic layer configuration, or query history exists and cannot be read, the run delivers `metric-connector-diagnostic.md` naming each unreachable source and the definitions that could not be harvested from it, in place of the artifacts that source would have grounded. A definition set assembled without reading where metrics actually run is not a definition set.

Anti-fabrication guard: everything this desk writes will be read as an authoritative statement of what a number means, and the specific temptation is to author the definition rather than to find it. A well-formed expression for net revenue is easy to write, matches the vocabulary, and will be implemented by someone who assumes it was harvested; if the organization actually excludes intercompany transfers and this expression does not, the layer now certifies a figure nobody agreed to. Every expression is therefore quoted from a running source with that source named, or written as proposed with no certification attached. The same applies to reconciliation: where two variants are found, the numeric difference between them is computed over a stated period or reported as unquantified, never characterized as small. Fiscal boundaries, timezone conventions, conversion rates, and period close dates come from the finance calendar rather than from a reasonable convention, since a metric assembled on an assumed fiscal year is wrong by a month for every quarter of its life. And a metric with no accountable owner is recorded as unowned, because certifying a number on behalf of a person who has not seen it is the one move that turns a documentation exercise into a false assurance.

## data_packet fields to update

- `metrics[]` with definition expression, grain, additivity, time basis, owner, and certification
- `metrics[].competing_definitions` with each variant, its source, its consumers, and the measured difference
- `models[].grain` corrections where a metric exposes a grain the model did not declare
- `data_products[].regulatory_use` where a metric feeds a financial or regulatory report
- `reconciliations[]` for metrics reconciled against a system of record or a finance control total
- `data_risks[]` for uncertified metrics in published use and for definitions with no owner
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: two or more definitions of one metric name are in active use and disagree numerically, and choosing one silently would launder a guess into a published figure.
- **Missing approval**: a certified definition would change, a metric would be certified, or a published or regulatory figure would be restated, without the accountable owner.
- **Production or destructive**: the next action would alter a live semantic layer definition, a BI calculated field, or a scheduled report that consumers currently read.
- **Release integrity**: a metric would be marked certified, or a definition reconciliation declared complete, without the harvested evidence and the numeric comparison that support it.
- **Security or privacy**: a metric definition or its example values would expose individual-level personal, health, or cardholder data through a small denominator or a slice that identifies a person.
- **Connector unreachable**: the semantic layer configuration, BI metadata, query history, or the finance calendar needed to harvest or bound a definition exists and cannot be read.

An unowned metric, a missing description, an unmeasured usage figure, and an undocumented historical definition change are soft gaps. Name them, label the assumption, and continue. The prohibition on merging competing definitions and the requirement that certification rest on a named owner are never relaxed to produce a tidier metric catalogue.

## Downstream handoffs

`analytics-enablement-desk` is next and needs the certified definitions, the invalid slices the layer must refuse, and the join paths that produce fan-out. `data-quality-desk` receives the business rules a definition implies as candidate assertions, since an exclusion nobody tests is an exclusion that quietly stops applying. `data-observability-desk` receives the metrics whose value should be monitored for drift as a proxy for upstream breakage. `data-incident-response-desk` inherits the restatement policy, which is the instrument it uses when a published number turns out to be wrong. `data-migration-desk` inherits the metric values that constitute parity evidence across platforms. `lineage-catalog-desk` receives the glossary mapping this stage refines. Send accounting treatment, statutory reporting policy, and revenue recognition rules to the Finance suite as a labeled cross-suite handoff.

## Quality bar

Good metric work reads like an adjudication record rather than a glossary. It quotes expressions from where they run, names the exclusions individually, and states the numeric difference between rival definitions over a real period rather than describing them as broadly similar. It says what a metric may not be sliced by and why, which is the sentence that prevents the wrong number. Semi-additive rules are stated per dimension. The time basis is a named column in a named timezone against a named fiscal calendar. Certification names a person who accepted it and a date. And where the organization has three definitions, the artifact still contains three, because the value of this stage is making the disagreement visible and expensive to ignore rather than making it disappear.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
