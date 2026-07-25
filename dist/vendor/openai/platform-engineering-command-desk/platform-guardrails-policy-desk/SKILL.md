---
name: platform-guardrails-policy-desk
description: define policy-as-code guardrails for an internal developer platform including admission control, pipeline policy gates, provisioning-time checks, advisory versus blocking enforcement, secret and credential defaults, workload identity, waiver and exception registers with named owners and expiry, and the ratchet that moves a control to blocking without stalling delivery.
---

# Platform Guardrails Policy Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the guardrail artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent policy names, enforcement modes, waiver owners, expiry dates, violation counts, or compliance obligations.

## Role

Own the platform's enforced opinions. This desk decides which rules exist, where in the developer's path each one fires, whether it warns or blocks, what a tenant does when a rule is wrong for them, and how a control tightens without turning every pipeline red on a Tuesday morning.

The distinction that matters here is between a rule that exists in a policy repository and a rule that is loaded into a running engine at an enforcement point a developer actually passes through. Only the second is a guardrail. The first is a document.

## Use when

- Policy-as-code work: admission control constraints, mutating defaults, IaC plan policy, pipeline policy gates, repository and branch protection rules, or cloud org-level constraints.
- A control needs an enforcement-mode decision, or an existing advisory control is being tightened to blocking.
- Secret and credential defaults are being set: static keys versus federated workload identity, secret-manager references, rotation expectations, or scanning at the push and pipeline boundary.
- The exception register is unmanaged: waivers with no owner, no expiry, or no compensating control.
- A compliance obligation needs a technical enforcement point rather than a policy document.

## Do not use when

- The pipeline itself is the subject (runner fleet, cache, registry layout, provenance and attestation mechanics): that is `cicd-platform-desk`, which owns the surface this desk attaches gates to.
- The isolation boundary is the subject (namespace and account topology, RBAC design, network policy, quota fairness): that is `tenancy-isolation-desk`.
- Who may approve a standard, how a standard becomes mandatory, or how exception decisions are ratified: that is `platform-governance-desk`. This desk builds the register; governance runs the review.
- Rolling an enforcement change across tenant rings with notice and rollback: that is `platform-change-rollout-desk`.
- Threat modeling the platform's own attack surface: cross-suite handoff to the Security suite.

## Required evidence

- The policy bundle as deployed: constraint templates and constraints, policy modules, admission webhook configurations with their failure policy, and the engine version actually running.
- Pipeline and workflow definitions showing where policy steps run, and whether the step is blocking or informational in each reusable workflow.
- Provisioning-path policy: plan-time checks in the IaC pipeline, and cloud organization or subscription-level constraints.
- Current violation output in whatever mode the control runs today, with the query or export it came from.
- The exception or waiver register: waiver id, scope, owner, justification, compensating control, expiry.
- Applicable compliance obligations mapped to controls, from the obligations source rather than from memory.
- Secret handling reality: identity federation configuration, secret-manager wiring, long-lived credential inventory, scanning configuration.

## Workflow

**Outcome.** A control set where every rule names its enforcement point, its current mode, its failure posture when the engine is unavailable, the waiver path with an owner and an expiry, and the evidence that established each of those, plus the tightening plan for controls that are not yet blocking.

**Grounding.** Read the running configuration for reality and the policy documentation for intent, and keep the two labeled separately per `references/suite-workflow-contract.md`. A rule present in the repository but absent from the deployed bundle, or deployed with `dryrun` while the documentation says enforced, is a finding to record rather than a discrepancy to smooth over.

**Constraints.** Every control carries a mode, an enforcement point, and a named owner. Fail-open versus fail-closed is decided per control and stated, because an admission webhook set to fail closed converts an engine outage into a platform-wide delivery outage, and one set to fail open converts it into a silent compliance gap. Waivers are scoped, owned by a person who can be paged, and dated; a waiver without an expiry is recorded as an unmanaged exception, not as an approved one. Controls that duplicate an existing cloud-native or repository-native guardrail are consolidated rather than stacked, because two engines enforcing the same intent produce two different verdicts on the edge cases.

Tightening a control from advisory to blocking follows this order, and the order is mandated because each step produces the evidence that makes the next one survivable, while a direct flip to blocking breaks every non-conforming tenant at once with no rollback except reverting the policy:

1. Run the control in advisory mode and capture the violation set per tenant from the engine's own output.
2. Publish the violating inventory to the named owners with the conforming example and the remediation.
3. Ratchet: block new or changed resources while grandfathering the existing violation set under a dated exemption.
4. Flip the grandfathered set to blocking once the remaining count and its owners are known and accounted for.

**Parallel surface.** Policy rules, enforcement points, tenants, and repositories are independent units and are parallel-safe; per-rule drafting, per-tenant violation assessment, and connector preflight across the policy bundle, pipelines, and IaC repositories all fan out.

The aggregate work runs once after the fan-out returns: the total violation count and its per-tenant distribution, the fail-open versus fail-closed posture judged across the engine as a whole, the ranking that decides which control tightens first, and the ordered tightening sequence above.

**Acceptance bar.** A platform engineer can read the control list and say, for each rule, exactly where it fires, what a developer sees when it fires, what happens when the engine is down, who signs a waiver, and when that waiver dies. Every mode and coverage claim traces to the deployed configuration or is written as unverified.

## Outputs

A complete run delivers this artifact set:

- `platform-guardrails-policy.md`: the control register with enforcement point, mode, failure posture, owner, backing obligation, and the consolidation decision where controls overlapped.
- `platform-guardrails-enforcement-plan.md`: the advisory-to-blocking sequence per control, the ratchet boundary, the remediation each tenant needs, and the delivery impact expected at each rung.
- `platform-guardrails-exception-register.md`: every waiver with scope, owner, justification, compensating control, expiry date, and the review that renews or ends it.
- `platform-guardrails-downstream-handoff.md`: the enforcement points and modes that `platform-observability-desk` must be able to see, and the tenant-affecting enforcement changes that `platform-change-rollout-desk` inherits.

Depth standard per artifact: a control entry gives the actual rule intent and the resource or path it applies to, not the category it belongs to. "Require resource limits" is a category; the control entry states which workloads, at which admission point, in which mode, with which exempted namespaces. An enforcement-plan entry names the tenants in the current violation set or states that the set is uncounted and why. A register entry with a blank owner is an unmanaged exception, and is labeled as one.

In `diagnostic` mode, when the policy bundle, admission configuration, or pipeline definitions exist and cannot be read, the run delivers `platform-guardrails-connector-diagnostic.md` reporting reachability, what was attempted, and the exact access needed. Control state is not drafted from the documentation alone in that mode.

Guardrail writing fails in a specific way: enforcement mode is the easiest field in this domain to fill from what the rule obviously ought to be. A control whose deployed mode no configuration establishes is recorded as mode-unknown, never as blocking. A waiver owner is copied from the register or left as unassigned, because an invented owner manufactures accountability that nobody agreed to and produces an exception that looks reviewed. A short honest register beats a complete-looking one.

## platform_packet fields to update

- `guardrails[]`: `control`, `mode`, `enforcement_point`, `exception_ref`.
- `governance.open_exceptions`, `governance.approval_gates`.
- `pipeline_surface.supply_chain_controls` where a control lands on the build path.
- `tenancy.quota_policy` where a guardrail enforces it.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: tightening a control to blocking, or granting a waiver against a compliance obligation, needs a named human owner who has not given it.
- Production or destructive: the next action would change live enforcement mode, load or unload a policy bundle, alter an admission webhook, or modify organization-level constraints.
- Security or privacy: continuing would assert secret handling, credential rotation, workload identity, or data-residency enforcement as verified without configuration evidence, or would surface credential material found while reading the bundle.
- Source conflict: the deployed configuration, the policy repository, and the obligations register disagree on whether a control is enforced, and choosing one silently would launder a guess into a compliance claim.
- Release integrity: a control set would be declared covering an obligation without evidence that the rule is loaded and firing at a real enforcement point.
- Connector unreachable: the policy bundle, admission configuration, pipeline definitions, or exception register exists and cannot be read.

An uncounted violation set, an undocumented waiver rationale, or a missing owner record is a soft gap: proceed with it named. Compliance obligations are never relaxed, waived, or deferred to keep the workflow moving.

## Downstream handoffs

`platform-observability-desk` needs each enforcement point named so violation and denial signals are actually collected, plus the controls whose failure is currently invisible. `platform-change-rollout-desk` needs every pending mode change classified as tenant-affecting, with the violating cohort attached. `platform-governance-desk` inherits the exception register for expiry enforcement and the audit evidence trail. Cross-suite: control evidence packaging goes to the GRC suite, and attack-surface threat modeling goes to the Security suite.

## Quality bar

A control register that a tenant lead can read and predict their own pipeline outcome from. Modes are honest, including unknown. Every blocking control has a waiver path that a person can actually use, and every waiver has a death date. The tightening plan says who breaks and when, before it says the control is on.
