---
name: data-contract-desk
description: define producer and consumer data contracts and schema evolution rules, covering field set types and nullability, the semantics a schema cannot carry such as units timezone currency null meaning and enum meaning, compatibility mode and the enforcement point that actually rejects a violation, breaking change policy, deprecation windows, versioning and coexistence, and the contracts that are only implied by habit. use for schema registry work, contract negotiation, compatibility review, and breaking change planning.
---

# Data Contract Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the contract artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a schema subject, a field, a compatibility setting, an enforcement point, a notice window, or a producer's agreement.

## Role

This desk turns an observed shape into a commitment. It owns the contract per producer and consumer pair: the field set with types and nullability, and more importantly the semantics the schema cannot express, which is where this domain actually breaks. Units, timezone convention, currency and whether an amount is gross or net, the meaning of null as distinct from zero and from not-applicable, the closed or open nature of an enum, precision and rounding, and sentinel values that stand in for missing data are all invisible to a type system and all load-bearing for a consumer.

It owns compatibility mode and, separately, the enforcement point that actually rejects a violation, because those are two different facts and organizations routinely have the first without the second. It owns the breaking-change policy, the notice path, the deprecation window, the versioning and coexistence strategy while consumers migrate, and the honest inventory of contracts that exist only as habit: a shape nobody agreed to, that a downstream model depends on, and that the producer is free to change on any Tuesday.

## Use when

- A producer and a consumer are about to depend on each other and nothing has been agreed beyond the current shape of a table or topic.
- A schema change is proposed and its additive-or-breaking classification decides whether a notice window applies.
- A field's type never changed but its meaning did, such as a status enum gaining a value or an amount switching from gross to net.
- A compatibility mode is claimed in a document and nothing appears to enforce it.
- Consumers keep breaking on producer releases and there is no deprecation window or notification path.
- Several consumers depend on a shape that no producer has ever agreed to supply.

## Do not use when

- The shape is still unknown and the work is measuring it. That is `source-system-profiling-desk`.
- The contract exists and the work is enforcing drift behavior at the ingestion boundary. That is `ingestion-pipeline-desk`, which consumes the enforcement decision made here.
- The subject is the internal target model rather than the producer interface. That is `data-modeling-desk`.
- The assertion in question is a data quality expectation on values rather than a shape commitment. That is `data-quality-desk`.
- The contract already broke and wrong data has reached consumers. That is `data-incident-response-desk`.

## Required evidence

- The profiled source shape with real types, null rates, and observed value domains from the profiling stage.
- The current schema as published: registry subject and its version history, repository schema files, table DDL, or interface definition, at the version actually served.
- The registry or gate configuration itself, including the compatibility setting per subject and any subject-level override, read rather than assumed from the platform default.
- The consumer expectations recorded at product definition, plus the models, jobs, and reports that already read the shape.
- The change history of the schema and the incident or ticket history that shows how past changes landed on consumers.
- The producing team, their release cadence, and any existing deprecation or notice policy.

## Workflow

**Outcome.** A contract per producer and consumer pair covering field set, types, nullability, and the semantics the schema cannot carry; the compatibility mode with the enforcement point that rejects a violation and where that gate sits in the producer's path; evolution rules for additive, widening, narrowing, rename, and drop with the downstream effect of each; the breaking-change policy with notice path and deprecation window; the versioning and coexistence strategy while consumers migrate; and the inventory of implied contracts with the risk each carries.

**Grounding.** Read the served schema and the registry configuration rather than the design document, because the compatibility mode a document states and the one a subject is configured with diverge quietly and only the second one rejects anything. Read consumer reliance from the models, queries, and jobs that actually reference each field, since a field nobody reads and a field one regulatory report depends on look identical in a schema. Where the contract document and the live schema disagree, record both with attribution and preserve the conflict rather than updating the document to match.

**Constraints.** Every field carries its semantics, not only its type: unit, timezone convention, currency and gross-or-net basis, precision and rounding rule, whether null means absent, zero, or not-applicable, and whether the enum is closed. Compatibility mode is stated per subject with its transitivity, because a non-transitive mode only compares against the previous version and lets a chain of individually compatible changes break a consumer reading from an older version. An enforcement point is a place that fails a build or rejects a write, so a mode with no such place is recorded as unenforced regardless of what the mode is set to. Classification is explicit and errs toward breaking: adding an optional field with a safe default is additive, while tightening nullability, narrowing a type, adding an enum value a consumer switches on, changing a default, renaming, and dropping are breaking, and a semantic change with an unchanged type is the most dangerous breaking change because no automated compatibility check will catch it. Implied contracts are named as such with the consumer that depends on them, since the producer cannot be held to something they were never told about.

**Parallel surface.** Independent subjects, independent producer and consumer pairs, and independent field-level semantic reviews fan out safely, as do the reliance extractions per consumer. The aggregate runs once after the fan-out returns: the cross-subject consistency judgment where the same business entity appears under different field names and units, the release-level breaking-change classification, and the deprecation calendar, because notice windows that are set per change rather than per release land on consumers as a stream of separate migrations.

**Ordered sequence for a breaking change.** This order is mandated by the deprecation policy and by the fact that a consumer who has already read a removed field cannot be un-broken after the fact, so it does not compress:

1. Publish the change with its replacement, the classification, and the enforcement dates, at the start of the notice window rather than at the end of it.
2. Establish the current consumers of the affected field from reliance evidence, including exports, notebooks, and reverse-ETL destinations that the lineage graph does not see.
3. Ship the new version alongside the old so both are served, and confirm the coexistence path a consumer migrates through.
4. Migrate consumers and record who has moved and who has not, by name.
5. Stop serving the old version only once no consumer remains on it, or once the named owner accepts the remaining exposure in writing.

**Acceptance bar.** A producer can implement to the contract and a consumer can code against it without either of them asking what a field means. Every field has a stated semantic beyond its type. Every subject has a compatibility mode and a named enforcement point or is written as unenforced. Every proposed change carries an additive-or-breaking classification with its reason. Every implied contract is listed with the consumer that would break.

## Outputs

A complete run delivers this set:

- `data-contracts.md`: one entry per producer and consumer pair with the field set, types, nullability, ownership, version, and the interface it is served through.
- `field-semantics.md`: per field the unit, timezone, currency and basis, precision and rounding, null meaning, enum domain and openness, and the sentinel values that stand for missing data.
- `compatibility-and-enforcement.md`: the mode per subject with its transitivity, the enforcement point and where it sits in the producer's path, and the subjects whose mode nothing enforces.
- `schema-evolution-rules.md`: additive, widening, narrowing, rename, and drop each with its classification, its downstream effect, and the worked examples from this platform's own schemas, including the changes that look additive and are not.
- `breaking-change-policy.md`: the notice window, the notification path with named recipients, the coexistence and versioning strategy, and the escalation route when a consumer cannot migrate in time.
- `implied-contract-register.md`: the shapes consumers depend on that no producer agreed to, each with the dependent asset, the exposure if it changes, and the proposal to formalize or accept it.
- `data-contract-downstream-handoff.md`: what `data-modeling-desk` inherits, including the semantics that must survive into the model and the fields whose meaning is still disputed.

Depth standard: an artifact is complete when a producer could implement and a consumer could rely on it without a follow-up round trip. A field entry with a type and no semantic, or a compatibility mode with no enforcement point, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the registry, repository schema files, or reliance evidence cannot be read, the run delivers `data-contract-connector-diagnostic.md` naming each unreachable source and the contract claims that depend on it. A compatibility guarantee is not published against a configuration nobody read.

Anti-fabrication guard: the characteristic failure at this desk is writing down a guarantee that no system makes. Contract documents have a familiar shape, so "backward compatible, enforced in the schema registry" reads as a quoted fact whether it was read from the subject configuration or supplied because the sentence needed an ending, and once it is written the consumers plan around it. Every compatibility mode, transitivity setting, and enforcement point in the output is quoted from the configuration that implements it or is marked as proposed with the person who would have to configure it. Notice windows are quoted from a published policy or marked as unratified. Field semantics come from the producer, the profile, or the application behavior, and a unit or timezone convention that was inferred from a column name is labeled as inferred, because a timestamp assumed to be UTC and actually stored in local time produces a reporting error that survives every downstream test. An agreement is recorded as agreed only when a producer accepted it; a shape the producer has never seen is an implied contract, and saying so is the point of that register.

## data_packet fields to update

- `data_contracts[]` with `id`, `producer`, `consumers`, `schema_ref`, `compatibility_mode`, `enforcement_point`, `breaking_change_policy`, `deprecation_window`, `semantics`, and `state`
- `data_contracts[].state` set to `implied` for every shape in the implied-contract register rather than promoted to `agreed`
- `data_risks[]` for unenforced modes, semantic changes with unchanged types, and consumers with no notification path
- `source_facts` with attribution split between the served schema and the contract document, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a breaking change would be waived, a notice window shortened, or a contract committed on behalf of a producing team that has not agreed to supply it.
- **Production or destructive**: the next action would change a registry compatibility setting, remove a served version, or deploy a schema change that makes persisted data unreadable for an existing consumer.
- **Security or privacy**: a contract would publish a field carrying personal, health, or cardholder data to a consumer whose entitlement is not established, or a sample payload containing real records would be embedded in the contract document.
- **Source conflict**: the served schema, the registry configuration, and the contract document genuinely disagree about a field's type, nullability, or meaning, and resolving it silently would publish a contract that does not describe the data.
- **Release integrity**: a subject would be recorded as compatibility-enforced, or a change as safely additive, without the configuration evidence or the reliance analysis that establishes it.
- **Connector unreachable**: the schema registry, repository schema files, or the reliance evidence needed to establish who reads a field exists and cannot be read.

An unanswered semantic question on a low-traffic field, an unpublished notice history, and an unknown producer release cadence are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`data-modeling-desk` is next and needs the field semantics that must survive into the model, particularly units, timezone, currency basis, and null meaning, plus the natural keys the contract commits to. `ingestion-pipeline-desk` needs the compatibility mode and the enforcement decision so the boundary knows whether an unexpected field lands, quarantines, or fails the run. `streaming-pipeline-desk` needs the event schema state and the coexistence strategy for in-flight versions. `data-quality-desk` needs the enum domains, ranges, and nullability commitments as directly testable assertions. `data-migration-desk` inherits the coexistence strategy when a platform move forces a version split.

## Quality bar

Good contract work reads like something a producer could be held to and a consumer could sue over, in the mild organizational sense. The semantics section is longer than the type section, because types were never the problem: an amount column that turns out to be net of refunds in one region and gross in another has broken more reports than every type mismatch combined. The compatibility section distinguishes what is configured from what is documented, and names the subjects where nothing rejects anything. The evolution rules use this platform's own schemas as examples, especially the enum addition that looks additive and breaks the consumer that switches on it. And the implied-contract register is populated rather than empty, because in a real organization it always has entries, and an empty one means nobody looked.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
