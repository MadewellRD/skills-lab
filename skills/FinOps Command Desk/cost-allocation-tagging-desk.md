---
name: cost-allocation-tagging-desk
description: build the cloud cost allocation hierarchy and measure tag coverage so spend resolves to named owners. covers tag and label key requirements with measured coverage per key and per account, tag value hygiene and case and spelling drift, account subscription and project hierarchy mapping to cost centers, allocation coverage percentage against total spend, the unallocated and untagged pool broken down by cause, largest untagged contributors by spend, provisioning-time enforcement versus retrofit, and the backfill plan for historical periods.
---

# Cost Allocation Tagging Desk

## Suite workflow mode

This desk is part of the FinOps Command Desk suite. Complete the artifact set, update `finops_packet`, and continue to the next stage whenever the facts allow rather than stopping at a bare next-desk recommendation. The packet shape, the source hierarchy, the measurement discipline, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline against the account, service, or resource it affects and recorded in `open_questions`. Never invent tag values, resource owners, team or cost center names, account identifiers, coverage percentages, or the size of an unallocated pool.

## Role

Own the mapping from a charge to a person who can act on it. This desk defines the allocation hierarchy from resource up through account, cost center, team, product, and service with the rule that applies at each level, states which tag keys are mandatory on which scope and measures actual coverage per key and per account, finds the value hygiene damage that turns one team into four columns, computes allocation coverage as a share of reconciled total spend, and breaks the unallocated pool down by cause rather than reporting it as a single embarrassing number.

The load-bearing distinction is that untagged is not unowned; it is unattributed. Somebody is consuming that spend and somebody's budget will absorb it. The practice's job is to say how much cannot be attributed and what would attribute it, because assigning the remainder to the team that looks most likely is how an allocation model loses trust that takes a year to build and one disputed chargeback to destroy.

## Use when

- An allocation or chargeback program is starting and coverage has never been measured.
- Tag or label policy is being designed, tightened, or consolidated, including closing an open value list that has grown several spellings of one team name.
- Coverage needs measuring per key, per account, and as a share of spend, because those figures diverge and the spend-weighted one is the one finance asks about.
- The unallocated pool needs decomposing into untagged, untaggable, shared, and structurally unattributable causes.
- Ownership needs mapping from the account structure, the ledger cost center list, and the tagging inventory, including where those three disagree.
- Enforcement needs designing, separating what can be blocked at provisioning from what has to be retrofitted onto resources that already exist.
- Historical periods need a backfill decision, including the periods that will never carry tags and have to be handled another way.

## Do not use when

- The cost basis, dataset register, or invoice reconciliation is unsettled: that is `cost-data-ingestion-desk`, and allocation coverage over an unreconciled total is a percentage of an unknown.
- Cluster, platform, network, or support spend needs splitting across consumers who share it: that is `shared-cost-allocation-desk`. This desk establishes what cannot be directly attributed; that desk decides how the shared remainder is divided.
- A report needs building for an audience with trends and a narrative: that is `showback-reporting-desk`.
- Cost centers need actual postings in the ledger with statements and disputes: that is `chargeback-invoicing-desk`.
- A team needs its own cost picture and an action set: that is `engineering-cost-review-desk`.
- Tag enforcement needs implementing in provisioning code or provider policy: cross-suite handoff to the Cloud Infrastructure suite, which owns the enforcement points this desk specifies.

## Required evidence

- The reconciled cost dataset from `cost-data-ingestion-desk`, at the finest granularity the export carries.
- The account, subscription, project, and resource group hierarchy as it actually exists, including accounts nobody claims.
- The current tag and label inventory with values exactly as they are, including the case variants, the misspellings, the trailing spaces, and the empty strings, because the mess is the finding.
- The tagging policy in force and the mechanism enforcing it, or the absence of one.
- The cost center and team structure from the ledger or the people system, which is the financial authority for who carries a cost.
- Ownership records: a service catalog, a directory group mapping, an on-call roster, or whatever spreadsheet is actually maintained.
- Provider-native cost grouping or allocation rules already configured, since those silently move spend between reports.
- The resource types and charge types in this estate that cannot carry a tag at all.

## Workflow

**Outcome.** An allocation hierarchy with the rule at each level, a mandatory tag key set where every key names the decision it enables, measured coverage per key and per account and as a share of spend, a value hygiene finding set, allocation coverage as a percentage of reconciled total spend with its denominator named, the unallocated pool decomposed by cause with the largest contributors ranked by spend, an enforcement design split between provisioning-time and retrofit, and a backfill plan for the history.

**Grounding.** The ledger cost center mapping wins over the tagging inventory for financial reporting, because the ledger is what an auditor reads and the tag is a claim somebody typed. The account structure is stronger evidence than a resource tag, since it is harder to get wrong and harder to change. Team statements about ownership are checked against the bill before they become facts. Where these disagree on material spend the disagreement is recorded as a hygiene finding with both readings, per `references/suite-workflow-contract.md`.

**Constraints.** Coverage is reported both by resource count and by share of spend, because the untagged remainder skews systematically toward older, larger, and less-governed resources and the two figures diverge in the direction that matters. Every percentage carries its denominator, and the denominator is the reconciled total rather than the subset that happened to return. Tag keys are treated as case sensitive with a canonical form stated, since two case variants of one key produce two columns in every cost report and neither is the total. Untaggable resource types and untaggable charge types are enumerated as a named residue rather than left to depress the coverage figure silently. An owner is a record from a source, never an inference from a naming convention or an account name. Enforcement mechanisms are specified with their limits: provisioning-time controls only affect what is created through that path and generally do not retroactively fix the estate that already exists.

**Parallel surface.** Accounts and subscriptions, projects and resource groups, individual tag keys, services, teams and cost centers, and per-violation triage are independent units and fan out, as does connector preflight across the cost dataset, the tag inventory, the ledger extract, and the ownership records.

The aggregate runs once after the fan-out returns. Allocation coverage is a share of the whole estate and cannot be assembled from per-team views that each look complete, because the spend nobody claims appears in nobody's view. The unallocated pool is the same shape: it is defined by what is left over, so it only exists at the level of the total. Averaging per-account coverage produces the mean of a set of unrelated fractions, which is not the estate's coverage and is usually flattering.

**Acceptance bar.** Anyone can take a charge from the reconciled dataset and resolve it to a cost center and a named owner, or to an explicit unallocated state with its cause, and can state the estate's allocation coverage with the query and denominator behind the figure.

## Outputs

A complete run delivers this artifact set:

- `allocation-hierarchy.md`: the roll-up from resource through account, cost center, team, product, and service, with the rule that resolves each level and what happens when a level is missing.
- `tag-key-requirements.md`: each mandatory key with the decision it enables, its canonical form, its allowed value list, the scope it is mandatory on, and how it is enforced or that it is not.
- `tag-coverage-report.md`: coverage per key, per account, by resource count and by share of spend, each with its denominator and the query behind it, plus the untaggable residue enumerated separately.
- `tag-value-hygiene.md`: case variants, spelling drift, orphaned values pointing at teams that no longer exist, free-text owner fields that resolve to nobody, and the consolidation each one needs.
- `unallocated-pool-analysis.md`: the pool by amount and share, decomposed into untagged, untaggable, shared and pending split, and structurally unattributable, with the largest contributors ranked by spend and what would allocate each.
- `tag-enforcement-plan.md`: what can be blocked at provisioning, what needs retrofitting, the mechanism at each point with its limits, and the sequence that gets coverage up without blocking a team mid-incident.
- `allocation-backfill-plan.md`: historical periods ordered by consequence, with the periods that will never carry tags named and the alternative attribution route stated for each.

Depth standard per artifact: a hierarchy entry gives the resolution rule, not a diagram label. A coverage figure gives numerator, denominator, and the query. A hygiene finding names the actual variant strings and the canonical target. An unallocated entry gives the amount, the cause, and the specific thing that would fix it, so "eleven percent sits in three accounts with no tag policy attached, largest is the shared data platform account" rather than "some spend is untagged".

In `diagnostic` mode, when the tag inventory, the ledger extract, or an account's cost data exists and cannot be read, the run delivers `allocation-connector-diagnostic.md` naming what was attempted and the access needed. Coverage is not computed over the accounts that happened to respond, because untagged spend concentrates in exactly the accounts nobody enumerated and a partial coverage figure is biased upward by construction.

The specific temptation here is the owner column, and it is stronger than it looks. A resource whose name carries a team prefix, in an account whose name matches a group, invites an owner value that is very probably correct. Very probably correct is how a chargeback lands on a cost center that did not spend the money, and the team that proves it costs the practice more credibility than the unallocated line ever would have. An owner with no record behind it is written as unresolved, and unresolved carries a figure so it is a finding rather than a blank. The same rule holds for coverage: a percentage that no query produces is not reported, and a coverage claim computed over a partial account list is labeled with the accounts it covered.

## finops_packet fields to update

- `allocation.hierarchy` with the rule at each level.
- `allocation.tag_keys[]` with `key`, `required_for`, `enforcement`, `coverage_pct`, and `value_hygiene`.
- `allocation.allocation_coverage_pct` with its denominator recorded in `source_facts`.
- `allocation.unallocated` with `amount`, `pct`, `largest_contributors`, and `reason_breakdown`.
- `governance.policies` where a tagging requirement or provisioning guardrail is proposed, and `governance.exceptions` where one is already granted.
- `source_facts[]` with `locator` and `as_of` per figure, plus `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Source conflict: the tag inventory, the account structure, and the ledger cost center mapping give different owners for the same material spend. This is the defining halt for this stage. Allocation is the foundation every later figure sits on, and publishing an allocation built over an unresolved ownership conflict produces a chargeback a team can prove is wrong, which costs more than the delay does.
- Production or destructive: the next action would apply or modify tags on live resources at scale, or attach a policy that blocks resource creation in accounts that were never evaluated against it. A blocking tag policy is an availability control wearing a cost label.
- Missing approval: making a tag mandatory in blocking mode, assigning ownership to a team that has not accepted it, or changing the cost center mapping needs a named human owner.
- Security or privacy: tag values or resource names carry personal data, customer identifiers, or credential fragments that would enter an artifact.
- Release integrity: a coverage percentage or an allocation completeness claim would leave the practice without the export and query behind it, or computed over a partial account list without saying so.
- Connector unreachable: the cost dataset, the tag inventory, the ledger extract, or an in-scope account cannot be read. Say whether the source was empty or unreachable, because those look identical in a query result and mean opposite things.

A missing rationale for an existing tag key, an undocumented historical value, or an unresponsive team lead is a soft gap: proceed with it named against the account it affects.

## Downstream handoffs

`shared-cost-allocation-desk` needs the coverage figure, the untaggable residue, and the pool of spend that is shared rather than merely untagged, because those are different problems with different methods. `showback-reporting-desk` needs coverage and the unallocated pool so the report shows the gap rather than hiding it inside a total. `unit-economics-desk` needs the coverage caveat, since a unit cost computed over a partially allocated numerator inherits the gap without showing it. `chargeback-invoicing-desk` needs the hierarchy and every allocation rule, because a dispute is almost always about a rule rather than about an amount. `engineering-cost-review-desk` needs per-team coverage so a team is not handed a number whose accuracy the practice cannot defend.

## Quality bar

A mandatory tag set short enough that people fill it and specific enough that the values mean something. Coverage measured twice with its denominator stated both times. An unallocated pool decomposed by cause with its largest contributors named, rather than a single percentage presented as a confession. Ownership that traces to a record every time, with the unresolved share stated as a figure. An enforcement plan that raises coverage without becoming the reason a deployment fails at three in the morning.
