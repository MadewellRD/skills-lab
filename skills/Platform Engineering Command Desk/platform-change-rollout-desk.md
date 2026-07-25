---
name: platform-change-rollout-desk
description: ship platform changes to tenants safely using ring definitions and promotion criteria, breaking versus additive classification against the published compatibility guarantee, control-plane and cluster upgrade sequencing, rollback and pause criteria, tenant-facing change notice, and the freeze and exception path for tenants who cannot absorb a change on schedule.
---

# Platform Change Rollout Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the rollout artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent tenant names, ring membership, approval decisions, freeze windows, version numbers, or compatibility guarantees.

## Role

Own the delivery of a platform change into systems the platform team does not own. Every change here lands in someone else's pipeline, cluster namespace, or deployment path, which is why this desk exists separately from the desks that design the change: the design question is whether the change is right, and the rollout question is who absorbs it first, what tells you to stop, and what a tenant is owed before it reaches them.

The changes this desk handles include module and template version bumps, reusable pipeline updates, base image and runtime upgrades, admission policy mode flips, control-plane and cluster version upgrades, default value changes, and platform API version transitions.

## Use when

- A platform change is ready and needs a ring plan, promotion criteria, and a rollback trigger before the first tenant is touched.
- A change needs classifying as additive or breaking against a published compatibility guarantee, including the changes that look additive and are not: a stricter default, a tightened validation, a removed implicit behavior.
- A control-plane or cluster upgrade needs sequencing, including deprecated API surface checks and node pool handling.
- A tenant-facing change notice needs writing, or the notice window itself is in question.
- Tenants are asking for a freeze exemption, or a freeze window collides with a scheduled rollout.
- A rollout is in flight and the pause or rollback decision needs criteria rather than opinion.

## Do not use when

- The change is a capability being removed rather than shipped: that is `platform-deprecation-sunset-desk`, which owns the enforcement ladder and teardown.
- The change is moving tenants onto a new path rather than changing a path they are already on: that is `platform-adoption-migration-desk`. Rollout pushes; migration pulls.
- The compatibility guarantee itself needs defining or revising: that is `platform-api-contract-desk`, whose guarantee this desk classifies against.
- Who approves a tenant-affecting change and under what authority: that is `platform-governance-desk`.
- Deploying a tenant's own application: cross-suite handoff to the SDLC suite for release operations and deployment.

## Required evidence

- The exact change: version delta, diff or changelog, and the configuration or interface surface it touches.
- The published compatibility guarantee and stability label for every interface the change affects, from the platform API contract stage.
- The consumer inventory that depends on the changed surface, drawn from catalog, telemetry, pipeline usage, and registry pull evidence rather than from assumed adoption.
- Current error budget state and support signal, since both are promotion gates.
- Existing ring definitions and prior rollout records, including what previously failed and at which ring.
- Freeze calendar and any regulated or contractual change constraint that binds a subset of tenants.
- The rollback mechanism as it actually exists for this change type, including where a rollback is not possible.

## Workflow

**Outcome.** A rollout plan naming the rings and their members, the promotion criteria and observation window between them, the additive or breaking classification with its evidence, the rollback or fix-forward reality per stage, the pause triggers, the tenant notice, and the exception path for tenants who cannot take the change on schedule.

**Grounding.** Read the diff, the interface definition, and the consumer telemetry for reality; read the change proposal and release notes for intent. A change described as additive whose diff removes an implicit default is classified from the diff, with both sources recorded per `references/suite-workflow-contract.md`.

**Constraints.** Ring membership is drawn from the catalog and consumer inventory, never composed to look representative. Ring 0 carries only platform-owned services and tenants who consented to absorb first failures; a ring that contains a revenue-path service because it seemed low risk is not ring 0. Promotion criteria are objective and stated before the roll begins, and every ring has an observation window long enough for the failure mode in question to appear, which for a reconciler or a cache change is measured in days rather than minutes.

Rollback honesty is mandatory. Several platform changes are one-way: a control-plane minor version is generally not downgradable, a database engine upgrade is not reversible, and a schema conversion applied to stored resources cannot be un-applied. Where the rollback is fix-forward, the plan says so and names the forward fix, because a rollout plan claiming a rollback that does not exist is worse than one that admits the risk.

Control-plane and cluster upgrades run in this order, and the order is mandated because the later steps are unrecoverable and the earlier ones are the only opportunity to detect the incompatibility:

1. Inventory the deprecated and removed API surface the target version drops, and identify every tenant object and controller still using it.
2. Remediate or migrate those consumers, and confirm through the same inventory query that the usage is gone.
3. Upgrade the control plane, holding node and data plane components at the prior version within the supported skew.
4. Upgrade node pools and addons with disruption budgets respected, one failure domain at a time.
5. Close the change with the version state recorded and the skew resolved.

Reordering steps 1 and 3 leaves tenant objects unreadable after the upgrade with no path back, which is the specific way cluster upgrades strand teams.

**Parallel surface.** Tenants, services, changed interfaces, and pipelines are independent units and are parallel-safe; per-tenant impact assessment, per-interface breaking-change classification, per-consumer notice drafting, and connector preflight across the catalog, telemetry, and pipeline definitions all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: ring composition and ordering, the go decision for each promotion, the blast-radius judgment across tenants, the freeze collision check, and the sequential upgrade order above. Ring promotion is inherently sequential, because the point of a ring is that the previous one has already reported.

**Acceptance bar.** Every ring names real tenants from the catalog. Every promotion has a criterion and a window stated before the roll. Every change carries an additive or breaking verdict traced to the diff and the guarantee. Every stage states whether rollback exists, and names the forward fix where it does not. The notice tells a tenant what to do and what happens if they do nothing.

## Outputs

A complete run delivers this artifact set:

- `platform-change-classification.md`: the additive or breaking verdict per affected interface with the diff evidence, the guarantee it is judged against, and the required notice window that follows from it.
- `platform-change-ring-plan.md`: ring definitions with named members, entry and promotion criteria, observation windows, the signals watched at each ring, and the sequencing rationale.
- `platform-change-rollback-plan.md`: the pause triggers, the rollback mechanism per stage or the explicit statement that rollback is not available, the forward-fix path, and the point of no return.
- `platform-change-tenant-notice.md`: the tenant-facing communication with the change, the date, the required action, the consequence of inaction, the exception route, and the named contact.
- `platform-change-downstream-handoff.md`: what `platform-adoption-migration-desk` and `platform-support-operations-desk` inherit, including the cohorts expected to need help.

Depth standard per artifact: a ring entry lists members, not a description of the kind of tenant that belongs in it. A classification entry names the specific field, default, or behavior that changed and the consumer pattern it breaks. A notice that says a change is coming without saying what a tenant must do is an announcement, not a notice, and is incomplete.

In `diagnostic` mode, when the catalog, telemetry, or pipeline usage data exists and cannot be read, the run delivers `platform-change-connector-diagnostic.md` reporting reachability, the queries attempted, and the exact access needed. Ring membership is not composed from assumption in that mode.

This desk fails by populating a roster. Ring plans read as competent whether their tenant names came from the catalog or from what a plausible ring would contain, and a rollout executed against invented members touches teams nobody warned and misses teams nobody counted. Every tenant, service, and owner in these artifacts comes from the catalog, telemetry, or pipeline evidence, or the ring is written as unpopulated with the query that would fill it. The same rule governs the two other fabricable claims here: a change is additive only when the diff and the published guarantee say so, never because the author intended it to be; and a rollback is asserted only when the mechanism exists and has a path, because "we can roll back" is the sentence that turns a contained incident into an extended one.

## platform_packet fields to update

- `platform_apis[].version`, `platform_apis[].stability`, `platform_apis[].breaking_change_window` where the change moves them.
- `abstractions[].version` and `templates[].version` for the versions being rolled.
- `guardrails[].mode` where the change is an enforcement-mode flip.
- `consumers[]` with per-tenant ring assignment and absorption state.
- `governance.approval_gates` with the approval obtained or outstanding for this blast radius.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: the tenant-affecting change lacks the named approval its blast radius requires under the governance model, or a freeze exception has not been granted by the owner who can grant it.
- Production or destructive: the next action would begin the roll, upgrade a control plane or cluster, flip enforcement mode, or mutate shared platform infrastructure.
- Security or privacy: the change alters authentication, authorization, workload identity, secret handling, or isolation, and its effect cannot be established from evidence.
- Source conflict: the catalog, telemetry, and pipeline evidence disagree about who consumes the changed surface, and rolling against the wrong inventory would hit tenants nobody notified.
- Release integrity: the change would be promoted past a ring without the promotion criterion evaluated, or classified as additive without diff evidence.
- Connector unreachable: the catalog, telemetry, diff, or pipeline usage source needed for the consumer inventory exists and cannot be read.

An unmeasured absorption estimate, absent prior rollout history, and unknown tenant maintenance windows are soft gaps: proceed with them named. Approval, ring order, and the upgrade sequence are never compressed to make a date.

## Downstream handoffs

`platform-adoption-migration-desk` needs the cohorts that will need migration help and the tenants who took an exception. `platform-support-operations-desk` needs the expected request classes and the ring calendar so the rotation is staffed for the days it lands. `platform-governance-desk` inherits the exceptions granted and their expiry. `platform-deprecation-sunset-desk` takes over when the change is the removal of a capability rather than a version move.

## Quality bar

A plan where the first failure lands on someone who agreed to catch it, where every promotion answers to a number rather than to a schedule, where rollback claims are true, and where a tenant reading the notice knows exactly what they must do and by when. Rings full of real names, or honestly empty.
