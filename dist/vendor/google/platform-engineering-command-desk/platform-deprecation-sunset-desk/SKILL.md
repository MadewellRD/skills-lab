---
name: platform-deprecation-sunset-desk
description: retire a platform capability without stranding consumers, covering deprecation policy and notice windows, consumer inventory with remaining-user counts, the replacement and migration path, the enforcement ladder from announced to advisory to blocking to removed, communication to each named owner, and teardown with data retention and its rollback boundary.
---

# Platform Deprecation Sunset Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the deprecation artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, the destructive-action sequence, and the halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent consumer counts, end-of-life dates, replacement readiness, owner names, notice history, or retention commitments.

## Role

Own the retirement of a platform capability: a golden path, a template, an IaC module, a platform API version, a reusable pipeline, an environment class, a cluster, a registry, or an entire tool. The work is not the teardown. The work is knowing who is still on it, giving them a real replacement and enough notice to use it, tightening enforcement in a sequence they can survive, and stopping short of the point where the decision can no longer be undone.

Every capability retired badly teaches the organization that platform commitments are temporary, which raises the cost of every future adoption ask. That is why this desk is separate from ordinary change rollout: the final step here destroys something.

## Use when

- A capability is being retired, consolidated away, or replaced, and needs a deprecation plan before anything is announced.
- A deprecation was announced and enforcement has not advanced, so consumers are still on the old path with no consequence and no date they believe.
- The consumer inventory for a capability is unknown and needs establishing from evidence before any enforcement decision.
- An enforcement rung needs advancing: from announced to advisory, advisory to blocking, or blocking to removed.
- Teardown is being planned and the data retention, export, and restore boundary needs stating.
- A platform API version, module major version, or template line is reaching end of support and the notice window follows from a published guarantee.

## Do not use when

- The capability is being changed rather than removed: that is `platform-change-rollout-desk`, which handles version moves and enforcement-mode flips on capabilities that continue to exist.
- Teams are being moved onto a new capability and the remaining population needs waves, enablement, and holdout analysis: that is `platform-adoption-migration-desk`. Hand back to it when the remaining consumers need a migration wave before enforcement can advance.
- The retirement decision itself has not been made and needs decision rights, a forum, or ratification: that is `platform-governance-desk`.
- The subject is a tenant's own service, API, or feature being decommissioned rather than a platform capability: cross-suite handoff to the SDLC suite.

## Required evidence

- The published deprecation policy and the notice window it obliges for this capability's stability tier, from the platform API contract stage.
- The consumer inventory assembled from several evidence types, since none is complete alone: catalog dependency records, API gateway or control-plane request logs by client, registry and module pull records, pipeline usage of the reusable workflow, and code search for the import or reference across the organization.
- Remaining-user counts with the lookback window and the query that produced each.
- The named replacement, its readiness state, and whether it covers every use the deprecated capability actually serves rather than the use it was designed for.
- The governance approval for the retirement, with its date and approver.
- Owner records for each remaining consumer, because a broadcast announcement is not notice.
- Data, state, and configuration held by the capability, with the retention obligation that binds it.

## Workflow

**Outcome.** A deprecation plan with the notice window derived from the published policy, a sourced consumer inventory with remaining counts, a replacement path that covers real usage, a dated enforcement ladder with an owner per rung, per-owner communication, and a teardown plan that names its rollback boundary and its retention obligation.

**Grounding.** Read request logs, pull records, pipeline definitions, and code search for who actually uses the capability; read the deprecation policy, the portal, and the roadmap for what was promised. Where the announcement claims a migration path that the replacement does not yet support, record both and preserve the conflict per `references/suite-workflow-contract.md`. That gap is why consumers stayed.

**Constraints.** The notice window follows the published guarantee for the capability's stability tier rather than the platform team's schedule, and shortening it is an approval decision with a named owner, not an efficiency. Deprecation is signalled in the artifact itself and not only in a document: the response header, the CLI warning, the template output, the catalog lifecycle field, and the portal state all say deprecated, because consumers discover deprecation where they work rather than where it was published.

The replacement covers the actual usage, including the uses the capability was never designed for and acquired anyway; a replacement that covers eighty percent of usage leaves the other twenty percent as permanent holdouts and a permanent exception. Communication goes to each remaining consumer's named owner with their own usage list attached, since a global announcement reliably reaches everyone except the people it concerns.

Retirement runs on the destructive-action sequence in `references/suite-workflow-contract.md`, expressed here as the enforcement ladder. The order is mandated because each rung is the evidence that the next one is safe and the last is irreversible:

1. Announce, with the replacement path, the dates, and the deprecation markers set in the artifact itself.
2. Advisory: the capability still works and warns, while usage is measured against the inventory to see who is moving.
3. Blocking for new usage, grandfathering existing consumers under dated exceptions, so the population stops growing while the remainder migrates.
4. Blocking for all usage, once the remaining consumers are individually known and accounted for.
5. Remove and tear down, after the rollback boundary is stated and the retention obligation is satisfied.

Do not compress these rungs to recover a slipped date, and do not reorder them if a future edit makes a rung look redundant. Running teardown ahead of a complete inventory strands tenants with no rollback and no owner to call.

**Parallel surface.** Consumers, usage evidence sources, replacement gap assessments, and per-owner communications are independent units and are parallel-safe; per-consumer impact assessment, per-source inventory queries, and connector preflight across the catalog, logs, registry, and pipeline definitions all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: the reconciliation of the several evidence sources into one consumer inventory, the remaining-user count and its confidence, the rung advancement decision, and the teardown go-ahead. The ladder itself is sequential by mandate, and the rung decision waits for the reconciled inventory rather than for any single source.

**Acceptance bar.** Every remaining-user count names its sources, its lookback window, and where the sources disagree. Every rung has a date and a named owner. Every remaining consumer has a named owner who received a notice with their own usage attached. The teardown plan states exactly what becomes unrecoverable and at which step. The replacement gap, where one exists, is written down rather than assumed closed.

## Outputs

A complete run delivers this artifact set:

- `platform-deprecation-policy-and-plan.md`: the capability, its stability tier, the obliged notice window with the guarantee it derives from, the announced and end-of-life dates, and the approval that authorized the retirement.
- `platform-deprecation-consumer-inventory.md`: remaining consumers by evidence source, the reconciled count with its lookback window, the disagreements between sources preserved, and the named owner per consumer.
- `platform-deprecation-replacement-path.md`: the successor capability, the usage-by-usage coverage assessment including the uses it does not cover, the migration steps, and any automated migration the platform will supply.
- `platform-deprecation-enforcement-ladder.md`: each rung with its date, owner, mechanism, the deprecation markers set in the artifact, the exception path, and the criterion that permits advancing.
- `platform-deprecation-comms-plan.md`: per-owner notice content with their usage list, the channel, the schedule, the reminder cadence, and the escalation for owners who do not respond.
- `platform-deprecation-teardown-plan.md`: what is deleted, the data export and retention with its period and restore procedure, the rollback boundary named as a specific step, and the post-teardown verification of what remains.

Depth standard per artifact: an inventory entry names the consumer, the evidence that found it, and the last observed usage date. A ladder entry names the mechanism that enforces the rung, not the intent to enforce it. A teardown entry states the irreversible step explicitly, because "we will remove the cluster" and "after the persistent volumes are deleted, restore is no longer possible" are different sentences and only the second is a boundary.

In `diagnostic` mode, when the catalog, request logs, registry records, or pipeline definitions exist and cannot be read, the run delivers `platform-deprecation-connector-diagnostic.md` reporting reachability, the queries attempted, and the exact access needed. No enforcement rung advances on an inventory that could not be built.

One sentence in this desk causes more damage than any other: "no remaining consumers." It is the claim that authorizes teardown, it is easy to produce from an incomplete query, and it is unfalsifiable until a team's pipeline breaks. Here a count of zero is only written when named sources with a stated lookback window return nothing, and each source is listed with what it covers and what it cannot see. Where evidence is missing, the count is unknown, and unknown blocks the ladder rather than permitting it, which is the opposite of how absent evidence is treated everywhere else in this suite. Dates are governed the same way: an end-of-life date comes from the approved plan or the published policy, never from what a reasonable window would be, because a fabricated date gets published and then honored by someone with delete permissions.

## platform_packet fields to update

- `deprecations[]`: `capability`, `replacement`, `announced`, `eol`, `consumers_remaining`, `enforcement_state`.
- `golden_paths[].tier` and `catalog_entities[].lifecycle` moved to deprecated where the retirement applies.
- `platform_apis[].stability` set to deprecated with the breaking-change window recorded.
- `consumers[].onboarding_state` for tenants still on the retiring capability.
- `governance.approval_gates` and `governance.open_exceptions` for the retirement approval and the grandfathered exceptions.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: the retirement, the end-of-life date, a shortened notice window, or advancing to a blocking rung lacks the named owner the governance model requires.
- Production or destructive: the next action would remove the capability, delete data or infrastructure, revoke credentials, or block usage that is currently working.
- Security or privacy: teardown would delete data under a retention obligation, or the consumer inventory would expose tenant or personal data whose handling has not been cleared.
- Source conflict: catalog, request logs, registry records, and pipeline evidence genuinely disagree on who still uses the capability, and picking the lowest count would authorize teardown on a guess.
- Release integrity: the capability would be declared unused, or the replacement declared covering, without evidence from a source that could have seen the usage.
- Connector unreachable: the catalog, request logs, registry, or pipeline definitions needed for the consumer inventory exist and cannot be read.

Missing migration effort estimates and unknown consumer timelines are soft gaps: proceed with them named. An unbuildable consumer inventory is not a soft gap at this desk, because the ladder's safety depends on it. Notice windows, ladder order, and retention obligations are never compressed to recover a schedule.

## Downstream handoffs

Return to the orchestrator for workflow close when the ladder is complete and teardown is either done or explicitly scheduled with its approval in hand. Hand back to `platform-adoption-migration-desk` when the remaining consumers need a migration wave before the next rung can advance, with the inventory and owners attached. `platform-governance-desk` inherits the grandfathered exceptions and their expiry. `platform-support-operations-desk` needs the expected request surge at each rung and the runbook for consumers who hit the blocking rung unprepared.

## Quality bar

A retirement where every remaining consumer got a personal notice with their own usage attached, where the enforcement dates did not move because the inventory was already correct, where the replacement covered the awkward uses as well as the intended ones, and where the irreversible step is named in writing before anyone reaches it.
