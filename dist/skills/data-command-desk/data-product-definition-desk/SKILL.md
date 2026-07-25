---
name: data-product-definition-desk
description: define a data product as the decision it serves, naming consumers and external recipients, output port, accountable owner, criticality tier, regulatory or contractual use, and agreed freshness completeness and accuracy targets, plus the tables dashboards and reports that already answer the same question. use for data requests, dashboard requests, data product intake, data slo definition, consumer inventory, tiering and certification, and duplicate asset checks before modeling begins.
---

# Data Product Definition Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the definition artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a consumer, an owner, a tier, a service commitment, a freshness figure, or the existence of a report.

## Role

A data product is a commitment to a decision, not a table that happens to exist. This desk owns the decision the product serves and the cadence at which that decision is made, the named consumers including downstream services, scheduled reports, and external recipients, the output port and its interface, the accountable owner, the criticality tier, the regulatory or contractual use that raises the evidence bar for every later stage, and the freshness, completeness, and accuracy targets agreed with a person who can accept them.

It also owns the least popular finding in the domain: which existing assets already answer this question. Requests arrive phrased as deliverables, and the warehouse usually already holds two or three partial answers to the question behind the request. Building a fourth is how a company arrives at four revenue numbers, none of them wrong in isolation and no two of them equal.

## Use when

- A request arrives phrased as an asset ("we need a dashboard", "can you build a table for this") and the decision behind it has not been written down.
- An existing report has acquired real dependents but has no owner, no tier, and no stated target.
- A dataset is about to feed an external recipient, a regulatory filing, a contractual commitment, or a production model, which changes the evidence bar downstream.
- Freshness, completeness, or accuracy is being argued about after the fact because nobody recorded what was promised.
- A tiering or certification standard exists and assets are being brought under it.
- Two teams are each proposing to build something that answers the same question.

## Do not use when

- The product is already defined and the question is what the source can actually supply. That is `source-system-profiling-desk`.
- The dispute is about what a named metric means rather than which decision it serves. That is `metric-semantic-layer-desk`.
- A published figure is wrong right now and consumers are acting on it. That is `data-incident-response-desk`, because containment precedes definition.
- The question is who is permitted to see the product. That is `data-governance-access-desk`.
- The work is disposing of an asset nobody reads. Usage evidence comes from `lineage-catalog-desk` and disposal from `data-retention-lifecycle-desk`.

## Required evidence

- The requester's question and the action that follows from the answer, with the cadence at which that action is taken.
- The named consumers: teams, services, scheduled reports, dashboards, feature tables, reverse-ETL destinations, and any external party such as a customer, partner, auditor, or regulator.
- The existing answer surface: catalog entries, certified dashboards, and query history showing what is actually run against which objects and by whom.
- Any service commitment, contractual obligation, or regulatory context the output feeds, quoted from the document that states it.
- The organization's tiering standard, certification criteria, and data product ownership model where they exist.
- The consumer's tolerance for being wrong and for being late, which are different numbers and are frequently confused.

## Workflow

**Outcome.** A data product definition stating the decision served and its cadence, the consumer inventory with external recipients called out, the output port and interface, the accountable owner, the criticality tier with its reasoning, the regulatory or contractual use, measurable freshness, completeness, and accuracy targets with the owner who accepted each, and an explicit finding on which existing assets already answer part of the question.

**Grounding.** Read consumption from query history and dashboard usage rather than from the request, because the people a product will affect are usually not the people who asked for it. Read the existing answer surface from the catalog and usage logs before designing a new one. An owner is a person who can accept a target and can be told when it is missed, so a team name on a wiki page is recorded as unowned until a person is named.

**Constraints.** Targets are agreed rather than assigned: a freshness target is a number somebody will be measured against, so one set by the builder is recorded as proposed until the consumer accepts it. Every target is expressed so a check can evaluate it, which means lag measured in the output port against a named event-time column, completeness measured as a share of an enumerated expected set rather than as a feeling, and accuracy measured as agreement with a named system of record within a stated tolerance. Criticality is derived from consequence to the consumer, never from requester seniority. Regulatory or contractual use is stated explicitly, because it propagates into retention, access, lineage coverage, and the restatement policy. The overlap finding is a required output, not a courtesy, and it names the objects rather than describing the situation.

**Parallel surface.** Independent data products, independent consumer conversations, and independent existing-asset investigations fan out safely. The aggregate runs once after the fan-out returns: deduplicating overlapping product proposals against each other, applying the tier rubric consistently across the portfolio rather than per request, and rolling the strictest consumer requirement up into the product target, because a product is only as fresh and only as accurate as the tightest commitment made on it.

**Acceptance bar.** A person who did not attend the conversation can read the definition and say what decision breaks if the product is late, who to call, and what number counts as late. Every target has a unit, a measurement point, and a named acceptor. The tier has a reason attached. The overlap finding names existing objects and states what each already answers.

## Outputs

A complete run delivers this set:

- `data-product-definition.md`: the decision and its cadence, scope boundary, output port and interface, owner, tier with reasoning, and the explicit non-goals that keep the product from absorbing every adjacent question.
- `consumer-inventory.md`: one entry per consumer with how they read the product, what they do with it, their own commitments that depend on it, and whether they are internal, downstream automated, or external.
- `data-product-slos.md`: freshness, completeness, and accuracy targets, each with its measurement expression, its measurement point, the acceptor, and what happens on a miss.
- `existing-asset-overlap.md`: the objects, dashboards, and extracts that already answer part of the question, what each covers, where they disagree, and the build-or-extend recommendation with its reason.
- `regulatory-and-contractual-use.md`: the obligations the output falls under, quoted from source, with the downstream stages whose evidence bar changes as a result.
- `data-product-downstream-handoff.md`: what `source-system-profiling-desk` inherits, including the grain the question implies and the freshness target that bounds the feasible extraction pattern.

Depth standard: an artifact is complete when a modeler could start work and an owner could sign the target without a follow-up conversation. A target without a unit and a measurement point, or a consumer entry that names a team without naming what breaks for them, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the catalog, query history, or BI usage source cannot be read, the run delivers `data-product-connector-diagnostic.md` naming each unreachable source and the definition claims that depend on it. The overlap finding is not written against an unsearched catalog.

Anti-fabrication guard: this is the stage where a sentence becomes a promise, and that is the specific hazard. An hourly freshness target invented to fill an empty field is indistinguishable on the page from one a consumer negotiated, and the pipeline is held to it either way. So every target carries the name of the person who accepted it or is written as proposed with the acceptor identified as the person who still has to agree. An owner is a named individual or the field says unowned; a team name is not promoted into an owner because the field looked incomplete without one. A consumer list is assembled from usage evidence and from stated dependencies, never from who plausibly ought to care, since an invented consumer inflates the tier and an omitted one is discovered during an incident. And "nothing exists that answers this today" is a claim about the catalog and query history, so where those were not searched the finding says unsearched rather than none.

## data_packet fields to update

- `data_products[]` with `name`, `decision_supported`, `consumers`, `output_port`, `owner`, `criticality`, `freshness_target`, `quality_target`, and `regulatory_use`
- `data_products[].freshness_actual` and `quality_actual` left as unmeasured at this stage rather than estimated
- `blast_radius` and `environment` set from consumer exposure and the target deployment
- `data_risks[]` seeded where a consumer dependency exists with no owner or no target
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a freshness, completeness, or accuracy target would be committed on behalf of an owner who has not agreed, or a product would be certified or placed in the top tier without the accountable owner accepting what that obligates.
- **Production or destructive**: the request implies replacing or retiring an asset that named consumers currently read, which changes numbers under people already using them.
- **Security or privacy**: the definition would route personal, health, or cardholder data to a consumer or external recipient whose entitlement is not established, or the consumer inventory itself would need to carry restricted identifiers.
- **Source conflict**: stakeholders state incompatible decisions for the same product, or the catalog owner and the requesting team disagree about who owns it, and choosing one silently assigns accountability nobody accepted.
- **Release integrity**: a product would be recorded as certified or tier one without a stated target, a named owner, and an output port a check can measure.
- **Connector unreachable**: the catalog, query history, or BI usage source needed to establish what already exists is present and cannot be read.

An unstated decision cadence, an unknown historical volume, and an absent organizational tiering standard are soft gaps. Record the gap, label the assumption where it was used, and continue.

## Downstream handoffs

`source-system-profiling-desk` is next and needs the decision, the grain the question implies, the freshness target that bounds which extraction patterns are feasible, and the sensitivity expectation to profile against. `data-contract-desk` needs the consumer expectations that a producer will be asked to commit to. `data-modeling-desk` needs the dimensions the question slices by and the history the consumers require. `data-quality-desk` needs the accuracy target and the reconciliation source named here. `data-governance-access-desk` inherits the external recipients and the regulatory use. `data-retention-lifecycle-desk` inherits the regulatory basis that sets a retention period.

## Quality bar

Good work here reads like something an owner signed rather than something an engineer drafted. The decision is stated in the consumer's language, with the action that follows from it, so a later reader can tell whether a four hour delay matters or is invisible. Targets are numbers with units and measurement points, because a target that cannot be evaluated by a check is a sentiment that will be relitigated during the first incident. The tier carries its reasoning, so it can be challenged rather than inherited. And the overlap section is honest: naming the two existing tables that already compute most of this, and recommending an extension instead of a build, is the highest-value output this desk produces, even though it is the one nobody asked for.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
