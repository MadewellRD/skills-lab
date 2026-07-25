---
name: data-modeling-desk
description: design conceptual logical and physical data models with a declared grain per fact, transaction periodic snapshot and accumulating snapshot fact types, conformed dimensions and the bus matrix, slowly changing dimension type per attribute with effective dating, natural and surrogate keys, unknown member handling, bridge tables and fan-out, late arriving fact and dimension policy, and measure additivity. use for star schema design, dimensional modeling, scd2 design, data vault, normalization decisions, and mart shape reviews.
---

# Data Modeling Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the model artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a table, a column, a data type, a join key, a cardinality, or a history requirement.

## Role

This desk decides the shape the warehouse will keep. It owns the conceptual and logical model with entities, relationships, and cardinality; the declared grain of every fact, written as one row per something; the fact classification across transaction, periodic snapshot, and accumulating snapshot; dimension design including conformed dimensions and the bus matrix that keeps them conformed, degenerate and junk dimensions, and role-playing dates; the slowly changing type chosen per attribute rather than per table, with its effective dating; the natural key and surrogate key strategy including how a missing or unknown key is represented rather than silently dropped; bridge handling for many-to-many relationships with their allocation rules; the late-arriving fact and late-arriving dimension policy; and the additivity of every measure.

Grain is the load-bearing decision, and it is the one most often described instead of declared. "Detailed order data" is not a grain. One row per order line per shipment is a grain, and the difference is that only the second one tells you whether joining a second dimension will double the revenue total.

## Use when

- A new mart, fact, or dimension is being designed and the grain has not been written as one row per something.
- Numbers inflate when a report adds a dimension, which is a fan-out symptom rather than a query bug.
- History is required for an attribute and the type of slowly changing dimension has not been decided per attribute.
- The same dimension exists three times with different keys and conformance has to be established or abandoned deliberately.
- A many-to-many relationship is about to be flattened into a fact and the allocation rule has not been agreed.
- Facts arrive for dimension members that do not exist yet, and they are currently being dropped or defaulted silently.

## Do not use when

- The source shape and its real keys have not been established. That is `source-system-profiling-desk`, and modeling on an unmeasured key is how a fan-out gets designed in.
- The producer commitment behind the fields is unsettled. That is `data-contract-desk`.
- The subject is physical layout, partitioning, clustering, or file sizing rather than logical shape. That is `warehouse-lakehouse-architecture-desk`.
- The work is implementing the model in SQL with materializations and merge keys. That is `transformation-layer-desk`.
- The dispute is about a metric expression on top of an existing model. That is `metric-semantic-layer-desk`.

## Required evidence

- The profiled sources with real keys, cardinality, orphan rates, and null behavior, since every relationship in the model is a claim about those numbers.
- The agreed contracts with field semantics, particularly units, currency basis, timezone, and null meaning, which decide how a measure can be aggregated at all.
- The consuming questions and the dimensions those questions slice by, including the ones that only appear in a filter.
- The history requirements the consumers actually stated, attribute by attribute, since keeping history on everything is as much a design failure as keeping none.
- The existing model where one exists: current DDL, keys, and the conformance state of dimensions already in use.
- Known reporting disputes, which usually point at a grain or an additivity problem rather than at a calculation.

## Workflow

**Outcome.** A model a builder can implement: entities and relationships with cardinality, every fact with its declared grain and classification, every measure with its additivity and its aggregation rule, dimensions with conformance state and per-attribute slowly changing type with effective dating, natural and surrogate key strategy with unknown and not-applicable member handling, bridges with allocation rules, and a stated policy for late-arriving facts and late-arriving dimensions.

**Grounding.** Every key in the model exists in a real schema, and every cardinality claim traces to a profiled count rather than to an entity diagram. Where the source profile shows the declared key is not unique, the model reflects the measured key and records the discrepancy. Where consumers describe a history requirement, record the attribute they need it on, because "we need history" applied to a whole dimension usually means two attributes.

**Constraints.** Grain is declared in words before any column is placed, and the uniqueness of that grain is stated as the assertion the quality stage will test rather than assumed. Additivity is declared per measure, because a semi-additive balance summed across time and a non-additive ratio averaged across rows are the two most common silent errors in a finished mart. Slowly changing type is chosen per attribute with the reason, and every type two attribute carries its validity window convention, stated as half-open so adjacent versions neither overlap nor leave a gap, plus the current-row indicator and what happens to it on a late correction. Surrogate keys carry a stated generation basis and a stated stability guarantee, since a hashed key that includes a mutable attribute silently changes identity. Unknown, not-applicable, and late-arriving members get explicit dimension rows rather than nulls, because an inner join is how a fact quietly disappears from a report. Many-to-many relationships are modeled deliberately with a bridge and a stated allocation rule, and the double-count risk is named where the allocation does not sum to one. Rejected alternatives are recorded with the reason so the next reader does not relitigate them.

**Parallel surface.** Independent subject areas, independent facts, independent dimensions, and independent attribute-level history decisions fan out safely. The aggregate runs once after the fan-out returns: the bus matrix that establishes which dimensions are actually conformed across facts, the cross-fact grain review that catches two facts at different grains being joined in a report, and the key strategy applied consistently across the portfolio. Conformance is by definition not a per-table judgment, and a dimension designed independently three times is exactly how a company ends up with three customer counts.

**Acceptance bar.** Someone can build the model from the artifact without asking what a row means. Every fact states one row per something. Every measure states its additivity and its aggregation rule. Every type two attribute states its validity convention and its current indicator. Every relationship states cardinality with the profiled evidence behind it. Every join key exists in a real schema or is marked as proposed.

## Outputs

A complete run delivers this set:

- `conceptual-and-logical-model.md`: entities, relationships, cardinality with its profiled basis, and the business definition of each entity in the consumer's language.
- `fact-specifications.md`: per fact the declared grain, classification across transaction, periodic snapshot, and accumulating snapshot, the measure list with additivity and aggregation rule, degenerate dimensions carried, and the milestone set with its date columns where the fact is an accumulating snapshot.
- `dimension-specifications.md`: per dimension the natural key, the surrogate key strategy, conformance state, per-attribute slowly changing type with effective dating and current indicator, role-playing usage, and the unknown and not-applicable member rows.
- `bus-matrix.md`: facts against conformed dimensions, showing where a dimension is genuinely shared and where two variants exist under one name.
- `key-strategy.md`: natural and surrogate key generation, stability guarantees, unknown and late-arriving member handling, and the orphan policy with its profiled orphan rate.
- `late-arriving-and-history-policy.md`: what happens when a fact arrives before its dimension member and when a dimension change arrives after facts were already assigned, including whether history is restated or left as recorded.
- `modeling-decisions.md`: the alternatives considered and rejected with the reason, including the normalization or wide-table trade taken and the fan-out risks accepted.
- `data-modeling-downstream-handoff.md`: what `warehouse-lakehouse-architecture-desk` inherits, including expected row counts per grain and the query predicates the model implies.

Depth standard: an artifact is complete when a builder could implement it and a quality author could write assertions from it without a follow-up round trip. A fact without a declared grain, or a type two attribute without its validity convention, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the source profile, existing DDL, or catalog cannot be read, the run delivers `data-modeling-connector-diagnostic.md` naming the unreachable evidence and the model claims that depend on it. A join key is not committed against a schema nobody read.

Anti-fabrication guard: a star schema is a drawing until every key in it exists somewhere real, and this desk's specific hazard is that a diagram is fluent, symmetrical, and completely disconnected from the warehouse. A column that follows the table's naming convention reads exactly like a column that exists, and a one-to-many arrow reads exactly like a profiled cardinality. So every column and type placed in the model is quoted from the information schema, the DDL, or an agreed contract, and anything else is written as proposed with the source that would have to supply it. Every cardinality, orphan rate, and expected row count names the profile that produced it or is written as unprofiled, because the relationships that look obviously one-to-many are precisely the ones that turn out to have four percent duplicates. Conformance is asserted only where the dimensions were compared; two dimensions with the same name are recorded as unconformed until the comparison was actually made. And a grain is never softened into an adjective: undeclared is an acceptable value here and "granular" is not.

## data_packet fields to update

- `models[]` with `name`, `layer`, `pattern`, `grain`, `keys`, and `late_arriving_policy`
- `models[].column_basis` set to catalog, DDL, contract, or inferred, per model rather than for the set
- `metrics[].additivity` seeded for every measure declared here, so the semantic stage inherits the aggregation rule rather than re-deriving it
- `data_risks[]` for fan-out paths, unconformed dimensions sharing a name, and orphan rates above the accepted tolerance
- `source_facts` with per-fact attribution, `decisions` including the rejected alternatives, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a grain change, a conformance decision, or an allocation rule for a many-to-many relationship would change figures a named owner already publishes, and that owner has not accepted the change.
- **Production or destructive**: the next action would alter an existing table's grain, drop or retype a column, or rebuild a type two dimension in a way that rewrites validity windows over history a consumer has already reported from.
- **Security or privacy**: the model would carry a restricted column into a wider-access mart, promote a personal identifier into a surrogate key visible in exports, or place health or cardholder data in a dimension whose access model is broader than the source.
- **Source conflict**: the profile, the contract, and the existing DDL disagree about a key's uniqueness or a relationship's cardinality, and choosing one silently designs a fan-out into a fact table.
- **Release integrity**: a model would be recorded as complete with an undeclared grain, an untested uniqueness assertion, or a measure whose additivity nobody established.
- **Connector unreachable**: the source profile, the existing DDL, or the catalog needed to confirm that a key exists cannot be read.

An undecided attribute-level history requirement, an unknown future volume, and an unresolved naming convention are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`warehouse-lakehouse-architecture-desk` is next and needs the grain, expected row counts, and the predicates the consuming questions imply, since those decide partitioning. `transformation-layer-desk` needs the slowly changing type per attribute, the validity convention, the merge keys, and the late-arriving policy it has to implement. `data-quality-desk` needs the declared grain as the uniqueness assertion, the relationships as referential-integrity assertions, and the enum domains as accepted-value assertions. `metric-semantic-layer-desk` needs the additivity classification and the grain at which each measure is valid. `data-migration-desk` inherits the key strategy when identity has to survive a platform move.

## Quality bar

Good modeling reads as a set of decisions with consequences attached rather than a diagram with boxes. The grain line for every fact is a sentence a business person can check. Additivity is stated even for the measures where it is obvious, because the obvious ones are where a semi-additive balance gets summed across months. History decisions are per attribute with a reason, so nobody discovers later that the entire dimension is type two because it was easier. The bus matrix shows the uncomfortable truth about which dimensions are actually conformed. And the rejected alternatives are written down with their reasons, because the second most expensive thing in a warehouse is a design nobody can defend, and the most expensive is the same design rebuilt two years later by someone who assumed there was no reason.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
