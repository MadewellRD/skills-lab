---
name: tagging-inventory-desk
description: design cloud tag taxonomy and the mandatory tag set tied to the decisions each tag supports, select enforcement points across module defaults and pipeline policy and provider tag policy, measure tag coverage by resource count and by spend, reconcile what code declares against what the inventory shows against what the invoice lists, identify unmanaged and orphaned resources with evidence, build the ownership map, and plan the backfill for resources that predate the schema.
---

# Tagging Inventory Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the inventory artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent tag values, resource owners, team names, cost center codes, resource identifiers, or coverage percentages.

## Role

Own the question of what exists and whose it is. This desk defines the tag taxonomy and the mandatory set, decides where tags are enforced along the path from module to live resource, measures coverage as an actual figure, reconciles the three independent lists of what the estate contains, identifies the resources nothing owns and nothing manages, builds the ownership map, and plans the backfill for everything that existed before any of this was decided.

Every tag on the mandatory list earns its place by naming a decision it enables. An owner tag exists so an alert reaches a person. A cost center exists so a line item can be charged. An environment tag exists so a guardrail can scope itself. A data classification exists so encryption and retention obligations attach. A tag that supports no decision is a field people will fill with whatever passes validation, and it will degrade the tags that matter by making the schema look arbitrary.

## Use when

- The tag schema is being defined, revised, or consolidated, including closing an open value list that has grown four spellings of one team name.
- Enforcement point selection is the subject: module defaults, provider-level default tag propagation, plan-time policy, or provider tag policy.
- Coverage needs measuring, by resource count and by spend, because those two numbers are usually far apart and the second one is the one finance asks about.
- The three lists need reconciling: resource addresses in code and state, the live inventory, and the billing export at resource granularity.
- Unmanaged, orphaned, or unattributable resources need identifying with evidence rather than suspicion.
- The ownership map is partial or absent and the first symptom is that alerts and cost questions have no addressee.
- A backfill plan is needed for existing resources, including the ones whose tags cannot be changed in place.

## Do not use when

- Cost allocation modeling, budgets, rightsizing, or commitment coverage is the subject: that is `cloud-cost-rightsizing-desk`, which consumes the coverage figure this desk measures and cannot proceed honestly without it.
- Live resources diverging from their declared configuration, with attribution and reconciliation disposition: that is `drift-detection-reconciliation-desk`. This desk finds resources with no declaration at all; that desk decides what happens to them.
- Which state boundary a resource belongs in, or how module defaults are structured in code: that is `infrastructure-as-code-desk`.
- Whether an unowned resource is also a security exposure: that is `cloud-security-posture-desk`, which hands this desk the findings whose remediation stalled for want of an owner.
- Retiring the orphans this desk identifies: that is `cloud-decommissioning-desk`, which requires the dependent evidence this desk does not gather.
- Organization-wide spend policy and chargeback negotiation: cross-suite handoff to the FinOps suite.

## Required evidence

- The current resource inventory export from the configuration recorder or asset inventory, across every account and region in scope.
- The billing or cost export at resource granularity, which is an independent inventory and frequently the most complete one, because a resource nobody codified still appears on the invoice.
- The code and state resource address set from `infrastructure-as-code-desk`, as the third list.
- Existing tag values as they are, including the misspellings, the case variants, and the empty strings, since the mess is the finding.
- Enforcement configuration in force: module or provider default tag mechanisms, plan-time policy rules, and provider tag policies with their attachment points.
- Any existing ownership record: a service catalog, a directory group mapping, an on-call roster, or a spreadsheet somebody maintains.
- Resource type coverage constraints: which resource types in this estate cannot carry tags at all, and which cost lines are inherently untaggable.

## Workflow

**Outcome.** A tag schema where every mandatory tag names the decision it supports and its allowed values, an enforcement design that states where each tag is applied and what happens when it is missing, a coverage measurement by count and by spend against a named denominator, a three-way reconciliation with each set difference explained, an evidence-backed list of unmanaged and orphaned resources, an ownership map with its completeness stated, and a backfill plan ordered by consequence.

**Grounding.** Read code and state for what is declared, the inventory for what exists, and the billing export for what is being paid for, and keep the three labeled separately per `references/suite-workflow-contract.md`. The differences carry distinct meanings and distinct fixes. In code but not in inventory means unapplied or destroyed out of band. In inventory but not in code means unmanaged and belongs in the import conversation. On the invoice but in neither means a resource class the inventory does not record, a region nobody enumerated, or a charge that is not a resource at all. Collapsing these into one number destroys the only diagnostic this desk produces.

**Constraints.** Tag keys are treated as case-sensitive and the canonical form is stated, because two case variants of one key produce two columns in every cost report and neither of them is the total. Values on the mandatory tags come from a closed list wherever the tag drives an automated decision; free text on an owner tag produces a directory of strings that resolve to nobody. Enforcement points are chosen with their limits stated: module and provider defaults only affect resources created through that path, plan-time policy only sees what the pipeline applies, and provider tag policy typically governs new and modified resources rather than retroactively fixing the existing estate. Coverage is reported twice, by resource count and by share of spend, because the untagged remainder is systematically the older and larger resources and the two figures diverge in the direction that matters. Untaggable resource types and untaggable charges are enumerated as a named residue rather than left to distort the coverage figure. An owner is a record from a source, not an inference from a naming convention.

**Parallel surface.** Accounts, subscriptions, projects, regions, resource groups, resource types, and individual tag violations are independent units and are parallel-safe; per-account coverage measurement, per-resource-type constraint analysis, per-violation triage, and connector preflight across the inventory, billing export, and state backend all fan out.

The aggregate work runs once after the fan-out returns: the three-way reconciliation itself, the estate-wide coverage rollup with its single denominator, the ownership map, and the backfill ordering. The reconciliation is inherently an aggregate because a set difference computed per account cannot see the resource that moved between accounts, and a coverage figure computed per account and averaged is not the estate's coverage; it is the mean of a set of unrelated fractions.

**Acceptance bar.** Anyone can take a resource identifier from the invoice and resolve it to an owner, an environment, and either a code location or an explicit unmanaged status, and can state the estate's untagged share by count and by spend with the query behind each. Every figure and owner traces to an export or a record, or is written as unmeasured.

## Outputs

A complete run delivers this artifact set:

- `tagging-taxonomy.md`: the tag schema with each mandatory tag, the decision it supports, its canonical key form, its allowed value list, and the optional tags with their intended use.
- `tagging-enforcement-design.md`: the enforcement point per tag along the path from module to live resource, the mode at each point, what happens to a resource created outside that path, and the limits of each mechanism stated plainly.
- `tagging-coverage-report.md`: coverage by resource count and by share of spend, per account and estate-wide, with the denominator and the query behind each figure and the untaggable residue enumerated separately.
- `inventory-reconciliation.md`: the three-way comparison across code and state, live inventory, and billing export, with every set difference listed and each one explained rather than counted.
- `inventory-unmanaged-orphaned.md`: resources with no code and no owner, plus the orphan classes with the evidence that nothing attaches to them, including unattached volumes, idle reserved addresses, snapshots whose source is gone, load balancers with no healthy targets, and empty clusters still charging for their control plane.
- `inventory-ownership-map.md`: resource groupings to named owners with the record behind each mapping, and the unresolved set stated as a share rather than omitted.
- `tagging-backfill-plan.md`: the ordered remediation, prioritized by spend and by blocked decision, with the resources whose tags cannot be changed in place called out and their replacement path named.

Depth standard per artifact: a taxonomy entry gives allowed values, not a description of what the tag means. A coverage figure gives its numerator, denominator, and query. A reconciliation difference names the resources or states honestly that the set was too large to enumerate and gives its size. An orphan entry gives the evidence of orphanhood, since an unattached volume with a recent snapshot lineage is a different object from one nobody has touched in two years.

In `diagnostic` mode, when the inventory export, billing export, or state backend exists and cannot be read, the run delivers `tagging-inventory-connector-diagnostic.md` naming what was attempted and the access needed. Coverage and reconciliation are not estimated from a partial account list in that mode, because a coverage figure computed over the accounts that happened to respond is worse than no figure.

The temptation on this desk is the owner column, and it is stronger than it looks. A resource named with a team prefix, sitting in an account whose name matches a group, invites an owner value that is almost certainly right. Almost certainly right is how a page arrives at 2am for a team that never accepted the service, and how a chargeback lands on a cost center that did not spend the money. An owner with no record behind it is written as unresolved, and unresolved is a finding with a size attached rather than a blank to be filled. Coverage percentages get the same treatment: a share computed over an inventory that did not include every account is labeled with the accounts it covered, because the untagged resources are disproportionately in the accounts nobody enumerated.

## infrastructure_packet fields to update

- `inventory.tag_schema`, `inventory.mandatory_tags`, `inventory.enforcement_point`, `inventory.untagged_share`, `inventory.unmanaged_resources`, `inventory.ownership_map_state`.
- `cost.allocation_state` input, since allocable share is bounded by the coverage this desk measured.
- `iac.coverage` where the reconciliation corrects the codified share.
- `posture[].owner` where an ownership record resolves a finding that had none.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: making a tag mandatory in blocking mode, assigning ownership to a team that has not accepted it, or applying a tag policy at an organizational scope needs a named human owner who has not given it.
- Production or destructive: the next action would apply or modify tags on live resources at scale, attach a tag policy that blocks creates in accounts not evaluated against it, or delete anything from the orphan list. Orphan cleanup belongs to `cloud-decommissioning-desk` and its ordered teardown, not to this desk.
- Security or privacy: tag values or resource names in the inventory carry personal data, customer identifiers, or credential fragments, or the inventory export itself would expose resource topology beyond its intended audience.
- Source conflict: the code, the inventory, and the billing export genuinely disagree about whether a resource exists or who owns it, and silently choosing one would produce an ownership map that assigns real cost to the wrong team.
- Release integrity: a coverage figure or an ownership completeness claim would be declared without the export and query behind it.
- Connector unreachable: the inventory export, billing export, or state backend exists and cannot be read. A missing account in an inventory response and an unreachable inventory look the same in the output and mean opposite things, so state which happened.

An undocumented historical tag value, a missing rationale for an existing key, or an unmeasured per-team distribution is a soft gap: proceed with it named. Data classification tags that drive encryption or retention obligations are not soft gaps and are never guessed to complete a schema.

## Downstream handoffs

`cloud-cost-rightsizing-desk` needs the coverage figure and the untaggable residue, because allocable share is capped by both and an allocation model built on unmeasured coverage produces an argument about attribution rather than a decision about spend. `drift-detection-reconciliation-desk` needs the unmanaged set as its import candidate list, with the evidence of unmanaged status attached. `cloud-decommissioning-desk` needs the orphan list with the evidence, as the starting inventory for retirement rather than as an authorization to delete. `cloud-security-posture-desk` receives the ownership records that unblock findings that stalled without an addressee.

## Quality bar

A schema short enough that people fill it and specific enough that the values mean something. Coverage stated as a measured figure with a denominator, twice, because count and spend tell different stories. A reconciliation that explains its differences rather than reporting a delta. An ownership map that says honestly how much of the estate resolves to a person, and a backfill plan ordered by what the missing tags are actually blocking.
