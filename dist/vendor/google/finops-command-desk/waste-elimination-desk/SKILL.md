---
name: waste-elimination-desk
description: inventory and eliminate cloud waste covering idle and stopped resources still billing, unattached volumes and unassociated addresses, orphaned snapshots and machine images, abandoned non-production environments, over-retained logs and backups, duplicate data copies, and forgotten test infrastructure, each with cost age and evidence of genuine disuse, plus non-production scheduling, retention tier changes, owner confirmation routes, and the candidates that look like waste and are not. use for waste sweeps, idle resource cleanup, snapshot and backup retention reviews, and dev environment shutdown schedules.
---

# Waste Elimination Desk

## Suite workflow mode

This desk is a member of the FinOps Command Desk suite. Complete the waste artifact set, update the `finops_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A resource with no recorded owner is a soft gap and is reported as unowned with the confirmation route attached; a resource whose activity telemetry cannot be read is a hard halt for that candidate, because a deletion recommendation would then rest on the absence of a signal nobody collected. Never invent resource identifiers, ages, last-activity timestamps, costs, retention obligations, dependency relationships, or owners.

## Role

Own the waste inventory and the route from a candidate to a safe removal. This desk holds idle and stopped resources that still incur charge, unattached block storage and unassociated addresses, orphaned snapshots and machine images, abandoned environments, over-retained logs and backups, duplicate data copies, and forgotten test infrastructure, each carried with its cost, its age, and the specific evidence that it is genuinely unused. It also holds non-production scheduling, retention tier changes with their recovery consequence, the owner confirmation route per candidate, and the register of candidates that look like waste and are not.

The distinguishing property of this stage is asymmetry. A missed idle volume costs a few dollars a month until the next sweep. A deleted volume that held the only copy of something is unrecoverable, and the person who finds out is on an incident call. That asymmetry is why this desk spends most of its effort on evidence and confirmation rather than on discovery, since discovery is the easy half and every provider console will do it for free.

## Use when

- A waste sweep is due, spend has grown without a matching workload, or a cleanup target has been set and needs a candidate list with evidence rather than a console filter export.
- Storage charges are growing while the working set is not, which usually resolves to snapshot chains, backup vaults with no lifecycle, log retention set once at creation, or replicated copies of data nobody reads.
- Non-production environments run continuously and a scheduling change is being considered, including the exceptions that make a naive nights-and-weekends schedule an outage.
- An anomaly triaged upstream resolved to an orphaned or idle resource rather than to a capacity or design cause.
- Account or project decommissioning is in progress and the residue needs inventorying before the account is closed.
- A prior sweep's candidates need re-examining, and the record of what was deliberately left alone last time needs to prevent the same conversation.

## Do not use when

- The resource is in use and the question is whether it is the right size or the right family. That is `rightsizing-desk`, which supplies the utilization telemetry this desk reuses for its idle determinations.
- The cost is caused by a design behavior such as replication topology, storage class choice, retry volume, or log verbosity at source. That is `cost-aware-architecture-desk`; this desk removes the accumulated artifact, that desk stops it accumulating.
- The subject is a commitment or reservation that is unused. Stranded commitment is `commitment-portfolio-desk`, and terminating the resources a commitment covers makes the stranding worse rather than better.
- The subject is unused software entitlements rather than unused infrastructure. That is `licensing-saas-spend-desk`.
- The candidates are found and the question is sequencing, ownership, and whether the saving is additive to other findings. That is `optimization-backlog-desk`.

## Required evidence

- The resource inventory at resource granularity with creation date, current state, attachment state, region, account, and cost for the period, taken from the billing and usage export rather than from a console summary.
- Activity telemetry per candidate: read and write operations, network throughput, control plane activity records, session or login history, and the date each signal was last non-zero, with the observation window stated.
- Snapshot and image inventory with the source resource, the chain relationship where snapshots are incremental, the retention policy that created them, and whether the source still exists.
- Backup and log retention configuration per scope, with the ingestion, storage, and query charges separated, since they price differently and only one of them is reduced by a retention change.
- Non-production environment inventory with the schedule already in force, the teams and time zones that use it, and any batch, scheduled test, or offshore usage the schedule would interrupt.
- Retention obligations: legal holds, regulatory retention periods, contractual data retention commitments, and the recovery objectives the backup set exists to meet.
- Dependency information for anything proposed for removal: attachments, mounts, restore paths, machine images referenced by launch configurations or scaling groups, and infrastructure-as-code definitions that would recreate the resource on the next apply.
- The owner map from tags, account structure, the ledger cost center mapping, and the infrastructure-as-code repository history, with disagreements preserved rather than reconciled.

## Workflow

**Outcome.** A waste inventory by category with cost, age, and the evidence of disuse per candidate; a non-production scheduling proposal with the exceptions named; retention and tier changes with the recovery consequence of each stated; an owner and a confirmation route per candidate; a staged removal plan with its reversible step; and the not-waste register recording every candidate deliberately left in place with the reason.

**Grounding.** Disuse is established from a positive signal, not from the absence of one. A resource that emits no metrics because nothing collects them looks identical in a query to a resource that is genuinely dormant, so each candidate carries the specific signal examined, the window it covers, and the date it was last non-zero. Cost per candidate comes from the export at resource granularity with its cost basis, because a resource covered by a commitment does not stop costing money when it is terminated. Age comes from the creation record rather than from the first date the current export happens to cover.

**Constraints.** The observation window covers the resource's real cycle, which for a quarterly job, a seasonal environment, or a disaster recovery standby is longer than any default lookback a console offers. Snapshot removal accounts for chain relationships, since deleting a base snapshot in an incremental chain either fails or silently forces a full copy that costs more than it saved. Retention reductions state what recovery capability is being given up in the terms of the recovery objective, not as a storage figure. Tier changes carry minimum storage duration charges, early deletion fees, per-object transition request costs that make lifecycle rules uneconomic on large numbers of small objects, and retrieval fees that a restore would incur. Scheduling proposals name the hours, the calendar, the exceptions, and the wake-up path, because a developer who cannot start an environment on a Saturday will build a permanent one. Anything defined in infrastructure as code is removed at the definition, since deleting the resource alone produces drift and a resurrection on the next apply. Legal holds and regulatory retention outrank every saving on this desk without exception.

Removal of a resource follows a mandated order, and the reason is recorded here so a later editor does not read it as scaffolding: deletion has no undo, so the evidence has to exist before the action, not after it.

1. Establish the disuse evidence and the dependency check for the specific resource, including whether it is a restore path, an image referenced by a scaling configuration, or a standby.
2. Confirm purpose with the named owner, or record the owner as unreachable and escalate to the account owner.
3. Stage a reversible step: stop rather than terminate, detach and label rather than delete, snapshot before destroying a volume, and hold a soak period long enough to cover the resource's cycle.
4. Obtain the named authorization for the irreversible act and execute it in a change window with the restore path documented.

**Parallel surface.** Candidates fan out cleanly. Individual resources, accounts and subscriptions, regions, environments, snapshot sets, and log or backup scopes are independent assessment units, and the per-candidate evidence pull, cost lookup, dependency check, and owner resolution all run in parallel. The aggregate runs once after the fan-out returns: the total waste figure reconciled against the export, the deduplication of candidates that appear in more than one category such as an idle instance whose attached volume and snapshots are each also listed, the netting against rightsizing candidates that cover the same resources, and the scheduling proposal, which is a single calendar over the whole non-production estate rather than a per-environment decision.

**Acceptance bar.** Every candidate carries its cost, its age, the signal that establishes disuse with the window that produced it, its owner or an explicit unowned marker, its dependency check result, and the reversible staging step that precedes its removal. The saving total is netted against overlapping findings and states which portion is realized reduction against which portion depends on a retention or schedule change that only takes effect prospectively. The not-waste register is populated, because a sweep that produces no exclusions did not check.

## Outputs

A complete run delivers this set:

- `waste-inventory.md`: candidates grouped by category with cost for the period, age, region and account, the disuse signal and its observation window, and the cost basis the figure carries.
- `disuse-evidence.md`: per candidate, the specific signals examined, the window, the last non-zero date, and the signals that were unavailable, so a reader can tell dormant from unmonitored.
- `scheduling-plan.md`: the non-production calendar with hours, exceptions for batch windows, scheduled tests, on-call and offshore usage, the wake-up path, the resources excluded from scheduling with the reason, and the saving computed from the actual hours removed rather than from a headline percentage.
- `retention-changes.md`: proposed log, snapshot, and backup retention and tier changes, each with the recovery capability given up stated against the recovery objective, the minimum duration, early deletion, transition request, and retrieval charges that apply, and the retention obligations that bound the change.
- `removal-plan.md`: the staged removal set with the reversible step, the soak period, the change window, the restore path, the infrastructure-as-code definition to update, and the named authorization each irreversible act requires.
- `owner-confirmation.md`: the confirmation route per candidate with the owner source, the disagreements between tag, account, and ledger ownership preserved, and the candidates whose owner could not be established.
- `not-waste-register.md`: candidates that look like waste and are not, with the reason and the evidence, so the next sweep does not spend the same effort or make the same mistake.
- `waste-downstream-handoff.md`: what `cost-aware-architecture-desk` and `optimization-backlog-desk` inherit, including the candidates whose root cause is a design behavior rather than an oversight.

Depth standard: an artifact is complete when the owning engineer could act on a candidate without re-deriving the evidence and a change approver could authorize the deletion from what is written. A candidate with a cost and no disuse signal, a retention change with no stated recovery consequence, and a schedule with no exception list are unfinished rather than draft.

When the resource inventory, the activity telemetry, or the retention configuration exists and cannot be read, the run delivers `waste-connector-diagnostic.md` naming each unreachable source and the categories of candidate it makes undecidable, in place of the inventory that source would have grounded. Candidates are not assembled from naming conventions or from what an estate of this shape usually contains.

Anti-fabrication guard: the characteristic error here is treating silence as proof. A resource with no telemetry, no tags, no documentation, and no recent activity record looks exactly like an abandoned one, and it is also exactly what a disaster recovery standby, a break-glass environment, an annual regulatory job, and a licence-pinned host look like from the billing export. This desk therefore never converts an absence into a finding: where a signal was not collected, the candidate is recorded as unmonitored rather than idle, and it stays out of the removal set until a signal exists or the owner confirms in writing. Ages, last-activity dates, and dependency relationships are copied from the record that carries them and are never inferred from a resource name, a tag value, or the age of the account it sits in. The cost attached to a candidate is the cost the export shows for that resource, not the on-demand list price of its type, because the two differ by exactly the discount that makes the saving smaller than it looks. And a retention obligation that could not be checked blocks the candidate rather than being assumed absent, since the artifact that survives this desk longest is the one nobody deleted.

## finops_packet fields to update

- `opportunities[]` with `lever: waste_removal`, `retention`, or `scheduling`, `scope` naming the specific resources, `current_state` with measured cost and the disuse signal, `proposed_state`, `estimated_savings` with amount, period, baseline, and the basis for the estimate
- `opportunities[].savings_type` separating realized reduction from avoidance, `overlaps_with` for candidates also appearing as rightsizing or commitment scope, and `net_of_overlap`
- `opportunities[].performance_risk`, `blast_radius`, `reversibility`, and `implementation_effort` with who performs it
- `opportunities[].owner`, `state`, and `rejection_reason` for every candidate placed in the not-waste register, preserved so the finding is not rediscovered next quarter
- `allocation.unallocated.largest_contributors` where untagged waste is a material share of the unallocated pool
- `governance.approvals[]` with the deletion or retention change as the item, the amount at stake, the required approver, and the authority basis
- `governance.policies` where a retention default or a provisioning guardrail would prevent the category recurring
- `source_facts[]` with locator and as-of for every inventory, telemetry, and retention reading, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would terminate, delete, or detach a resource, remove a snapshot or backup, shorten a retention period, or apply a shutdown schedule to a running environment. This is the defining halt of this desk. Prepare the removal set with its evidence, its reversible staging step, and its restore path, and stop at the gate for a named human.
- **Missing approval**: a retention reduction, a schedule change to an environment another team depends on, or a deletion of anything under a recovery objective needs the owner of that objective, who has not agreed.
- **Security or privacy**: a candidate holds personal, regulated, or customer data whose deletion has notification or record-keeping consequences, evidence of a legal hold exists or cannot be checked, or the resource is part of an ongoing investigation whose evidence must be preserved rather than cleaned up.
- **Source conflict**: the tag owner, the account structure, and the ledger cost center name different owners for a material candidate, or the dependency record and the running configuration disagree on whether a snapshot or image is still referenced. Record both readings and route the conflict; do not resolve toward the reading that permits the deletion.
- **Release integrity**: a waste saving would be published as realized while it depends on a retention or schedule change that only reduces future charges, or the total would sum candidates that overlap with rightsizing scope already counted elsewhere.
- **Connector unreachable**: the resource inventory, the activity telemetry, the snapshot chain metadata, or the retention configuration exists and cannot be read, so disuse would be asserted from the absence of a signal nobody collected.

An unknown owner, a missing tag, a resource with no documented purpose, and an environment whose usage pattern is undocumented are soft gaps. Name them, label the assumption against the candidate it affects, and continue with the candidate held out of the removal set. The evidence, owner, and reversible-staging sequence is never compressed to hit a cleanup deadline.

## Downstream handoffs

`cost-aware-architecture-desk` is next in the default sequence and receives the candidates whose cause is a design behavior: retention defaults set at provisioning, replication that copies data nobody reads, log verbosity at source, and environments that exist because creating one is slow. `rightsizing-desk` supplies the utilization telemetry this desk reuses and receives back the resources found to be idle rather than merely oversized. `optimization-backlog-desk` receives the full candidate set with sizing, reversibility, owner, and overlap markers for deduplication against every other lane. `commitment-portfolio-desk` receives the removal set specifically as a baseline adjustment, since usage removed here must not appear in the usage a commitment is sized against. `engineering-cost-review-desk` receives the per-team candidate lists and the not-waste register. Send the implementation itself to the owning engineering teams through the SDLC suite, packaged for Jules with the resources, the evidence, the reversible step, and the rollback path attached; send estate changes to the Cloud Infrastructure suite.

## Quality bar

Good waste work is boring to argue with. Every candidate names a resource an engineer can open, carries a cost from the bill rather than from a rate card, and states the signal and the window that establish disuse so the owner can disagree with the evidence rather than with the conclusion. The scheduling proposal reads as though someone asked the teams what they do at night. Retention changes talk about recovery rather than about gigabytes, and the person who owns the recovery objective is named. The not-waste register is treated as a first-class output rather than as leftovers, because the sweep that gets run every quarter is the one that stopped resurfacing the disaster recovery standby on the third try. And the saving claimed here is the saving that shows up on a later invoice, which is smaller than the console estimate and is the only number worth reporting.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
