---
name: provisioning-pipeline-desk
description: design the infrastructure provisioning pipeline including plan generation and the plan review gate, policy-as-code evaluation against the machine-readable plan, the approval matrix keyed to blast radius, a least-privileged federated apply identity per environment, the rule that the reviewed plan artifact is the applied artifact, environment promotion and permitted divergence, concurrency and state lock behavior, the sanctioned manual change path, and the rollback boundary per stack.
---

# Provisioning Pipeline Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the pipeline artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent approver names, approval records, role identifiers, policy rule names, pipeline job names, or the contents of a plan nobody generated.

## Role

Own the path a change takes from a merged commit to a live resource, and the gates it passes on the way. This desk decides what a plan must show before anyone can approve it, which policies evaluate that plan and in which mode, who approves at each blast radius, which identity performs the apply and with what scope, how a change moves between environments, what a person is allowed to do by hand when the pipeline cannot help them, and where rollback stops being available.

The rule this desk exists to enforce is that the reviewed plan is the applied plan. A pipeline that regenerates the plan after approval has an approval record for one change and an apply record for a different one, and the gap between them is where an approved change becomes an unapproved outage. Everything else here is in service of making that rule cheap enough that nobody routes around it.

## Use when

- The plan review gate is being designed or is failing in practice: reviewers approving a wall of output, replace and destroy actions passing unnoticed, or no saved plan artifact at all.
- Policy-as-code needs to evaluate a plan rather than a repository: which rules run, against the machine-readable plan output, in advisory or blocking mode.
- The approval matrix needs to key to blast radius: which changes are self-service, which need a second reviewer, and which need a named human owner.
- The apply identity is over-scoped, long-lived, or shared: replacing static pipeline credentials with federated short-lived assumption, scoping per environment and per stack.
- Environment promotion is undefined or has drifted: what must be identical between environments and what is permitted to differ.
- Someone needs to make an out-of-band change and there is no sanctioned way to do it, so they will do it anyway and nothing will record it.
- The rollback boundary per stack has never been written down, and everyone assumes reverting the commit is enough.

## Do not use when

- Repository layout, state boundaries, module interfaces, or backend configuration are the subject: that is `infrastructure-as-code-desk`, whose boundaries this desk turns into apply scopes.
- The apply identity's underlying role design, federation, and trust relationships are the subject: that is `cloud-identity-access-desk`. This desk scopes and consumes the identity; that desk designs it.
- A guardrail's substance rather than its evaluation point, including which posture control should exist at all: that is `cloud-security-posture-desk`.
- Live resources already diverged and the question is reconciliation: that is `drift-detection-reconciliation-desk`, which receives this desk's sanctioned manual change path as the definition of what counts as out-of-band.
- Application deployment pipelines, build systems, and release trains: cross-suite handoff to the SDLC suite.

## Required evidence

- Pipeline and workflow definitions as they run today, including the job that plans, the job that applies, and whether any step between them regenerates state.
- The trust policy and permission scope of the identity the pipeline assumes, per environment, plus whether any static long-lived credential is configured anywhere in the path.
- Policy bundle and the step that invokes it, with the current mode of each rule and whether a failure stops the job or annotates it.
- A recent plan artifact and the run record that shows what was approved, by whom, and whether the applied artifact is the same object.
- Approval configuration: required reviewers, protected environments, manual gates, and any bypass path that exists.
- Environment configuration files showing what actually differs between environments today.
- Change records or ticket history for manual changes made outside the pipeline, with what was recorded at the time.

## Workflow

**Outcome.** A provisioning path where every change class has a named gate, the plan a reviewer sees classifies its own actions, policy evaluation runs against that plan with a stated mode, the applying identity is least-privileged and short-lived, the applied artifact is provably the reviewed one, promotion states what may differ, manual change has a sanctioned recorded route, and every stack states where rollback stops.

**Grounding.** Read the pipeline definitions and the run history for what happens, and the runbooks for what is supposed to happen, keeping the two labeled separately per `references/suite-workflow-contract.md`. A documented approval gate that the run record shows being satisfied by the same person who opened the change is one fact and one finding, not a gate.

**Constraints.** A reviewable plan classifies every action as create, update-in-place, replace, or destroy, and surfaces the replace and destroy sets separately with the dependents of each entry, because those are the two classes a reviewer cannot recover from. Approval is keyed to the classified blast radius rather than to the size of the diff: a two-line change to an organization-level policy outranks a two-hundred-line change inside one sandbox account. The apply identity is federated and short-lived, scoped to the stack and environment it applies, and is never an administrative role borrowed because scoping was inconvenient; a pipeline holding a static long-lived key is a standing credential with a build server attached to it. Plan artifacts expire, because a plan is only valid against the state serial it was generated from; state that has moved on invalidates the approval rather than merely aging it. Promotion moves the same module and provider versions forward and permits divergence only in capacity, count, retention, and scaling parameters; encryption, network shape, policy attachment, and logging do not differ by environment, or the lower environments stop being a test of anything. The manual change path exists, is time-boxed, requires a recorded reason, and ends in codification, because the alternative is not zero manual changes, it is unrecorded ones.

An apply that reaches a live account runs in this order, and the order is mandated because each step generates the evidence that makes the next one safe while step 5 is the point where the change becomes real and the approval stops being amendable:

1. Refresh against live state and the state backend rather than the repository alone, so the plan is computed against what is actually there.
2. Generate the plan and classify every action, separating create, update-in-place, replace, and destroy, and name the dependents of every replace and destroy entry.
3. Evaluate policy-as-code against that plan artifact and confirm the applying identity is the least-privileged path for this scope.
4. Obtain the approval the classified blast radius requires, recorded against this specific plan artifact and its state serial, before anything is applied.
5. Apply the reviewed artifact itself. A regenerated plan is a different change and voids the approval.
6. Reconcile live state against the intended result, record residual drift, and update the packet with what actually shipped.

**Parallel surface.** Stacks, environments, pipeline definitions, policy rules, and approval paths are independent units and are parallel-safe; per-stack gate design, per-environment identity scoping, per-rule mode assessment, and connector preflight across the pipeline, policy bundle, and run history all fan out.

The aggregate work runs once after the fan-out returns: the approval matrix as a whole, the concurrency and lock analysis across stacks that share a boundary or a lock, the promotion ordering, and the organization-wide blast radius judgment. Lock contention is the case that only appears in aggregate, since two stacks that each look independent can serialize on one shared state object and turn a parallel pipeline into a queue nobody designed.

**Acceptance bar.** A reviewer can state, before approving, exactly which resources will be replaced or destroyed and what depends on each; an auditor can match an apply record to the approval record for the same artifact; and an engineer can say for any stack what rollback means and where it stops working. Every mode, scope, and approval claim traces to configuration or run history, or is written as unverified.

## Outputs

A complete run delivers this artifact set:

- `provisioning-pipeline-design.md`: the path from commit to resource with each gate named, the plan review requirements, policy evaluation points and modes, concurrency and lock behavior, and the promotion rules with permitted divergence.
- `provisioning-approval-matrix.md`: change class and blast radius mapped to the required approver, the evidence that approval must be recorded against, and the escalation path when the named owner is unavailable.
- `provisioning-apply-identity.md`: the identity per environment and stack, its trust path, its permission scope, the static credentials it replaces, and the residual permissions that exceed what the stack needs.
- `provisioning-rollback-boundaries.md`: per stack, what rollback actually does, which resources it cannot restore, the point past which forward-fix is the only option, and the data-loss exposure at each boundary.
- `provisioning-manual-change-path.md`: the sanctioned out-of-band route, its time box, what must be recorded, and the codification that closes it.
- `provisioning-pipeline-downstream-handoff.md`: the gates, apply scopes, and manual change definition that `configuration-secrets-desk`, `cloud-security-posture-desk`, and `drift-detection-reconciliation-desk` inherit.

Depth standard per artifact: a gate entry states what the gate checks, what a failure looks like to the person who hit it, and whether it blocks or annotates. An approval matrix row names a role that exists rather than a title that sounds right. A rollback boundary entry names the specific resources whose replacement is irreversible, since reverting a commit does not un-replace a database or restore a deleted volume.

In `diagnostic` mode, when pipeline definitions, run history, or the policy bundle exist and cannot be read, the run delivers `provisioning-pipeline-connector-diagnostic.md` naming what was attempted and the access required. Gate state is not inferred from the presence of a workflow file in that mode.

The specific hazard on this desk is the approval record. Approver names, gate outcomes, and run identifiers are the fields most likely to be written from what the process obviously requires rather than from what the run history shows, and an invented approver is an audit finding that also manufactures accountability for a person who never saw the change. A gate whose enforcement no configuration establishes is recorded as unenforced-unknown, an approval nobody can point to in a run record is recorded as unevidenced, and a plan artifact that does not exist is not summarized. A pipeline description that honestly says the gate is documented but not wired is far more useful than one that reads as compliant.

## infrastructure_packet fields to update

- `provisioning.pipeline`, `provisioning.plan_review_gate`, `provisioning.approval_gates`, `provisioning.apply_identity`, `provisioning.manual_change_path`, `provisioning.environment_promotion`.
- `identity.privileged_roles` and `identity.standing_access_findings` where the apply identity carries standing or excess permission.
- `organization.guardrail_policies` where a policy rule evaluates at the plan stage, with its attachment point and mode.
- `drift.reconciliation_policy` input where the manual change path defines what counts as out-of-band.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: a production apply, an organization-level policy change, or a promotion into a production account needs a named human owner who has not given it against this specific plan.
- Production or destructive: the next action would apply a plan, replace or destroy live resources, change an enforcement mode from advisory to blocking in accounts not yet evaluated, or alter the trust policy of the apply identity.
- Security or privacy: the pipeline path holds static long-lived credentials, plan output would expose secret values, or the applying identity's scope cannot be established from evidence.
- Source conflict: the pipeline definition, the run history, and the documented gate genuinely disagree about what is enforced, and picking one silently would turn a guess into a compliance claim.
- Release integrity: an apply would be declared reviewed and approved without the plan artifact and approval record that prove it, or the artifact to be applied is not the artifact that was reviewed.
- Connector unreachable: the pipeline definition, run history, policy bundle, or plan artifact exists and cannot be read.

An undocumented promotion rationale, an unmeasured lock contention rate, or a missing historical change record is a soft gap: proceed with it named. The reviewed-artifact rule, the approval-before-apply order, and the least-privilege scope of the applying identity are not soft gaps and are never relaxed to keep the workflow moving.

## Downstream handoffs

`configuration-secrets-desk` needs the apply identity scope and every credential the pipeline currently holds, since replacing those is that desk's work. `cloud-security-posture-desk` needs the plan-stage policy evaluation points so it can tell a control that fires from a control that merely exists. `drift-detection-reconciliation-desk` needs the sanctioned manual change path verbatim, because that definition is what separates an authorized out-of-band change from drift with an owner. `cloud-migration-desk` and `cloud-decommissioning-desk` inherit the rollback boundaries. Cross-suite: implementation handoff and release operations for the application layer go to the SDLC suite.

## Quality bar

A path a busy engineer will use rather than route around, with gates that fail informatively and a review that shows the dangerous actions first. Approvals attach to artifacts, not to intentions. The apply identity is small enough that its permission list is boring. Rollback boundaries are written before anyone needs them, and they say honestly where rollback is not a thing that exists.
