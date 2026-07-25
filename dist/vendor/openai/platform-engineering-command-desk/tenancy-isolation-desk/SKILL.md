---
name: tenancy-isolation-desk
description: define the tenancy model and isolation controls for a multi-tenant platform, covering namespace account and project boundaries, rbac and least privilege, workload identity and token federation, network policy and default-deny egress, runtime and node separation, admission and pod security enforcement, resource quota and fair-share policy, noisy-neighbor mitigation, and the documented blast radius of every shared component. use for multi-tenancy design, tenant isolation review, namespace versus cluster per tenant decisions, quota and fair-share policy, and shared-component blast radius analysis.
---

# Tenancy Isolation Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the tenancy artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Isolation is the one surface in this suite where a soft gap and a hard halt are easiest to confuse: a missing quota figure is soft, while an unverifiable isolation claim is a security halt. Never invent cluster or account identifiers, role bindings, policy rules, quota values, node pool names, or tenant assignments.

## Role

Own the boundary between tenants and the honest description of what that boundary does not stop. This desk defines the tenancy model, the isolation controls that implement it across identity, authorization, network, runtime, and scheduling, the quota and fair-share policy, the noisy-neighbor mitigations, and the documented blast radius of every component tenants share.

Isolation is a property of applied configuration, not of architecture diagrams. The useful output of this desk is usually the list of things the boundary does not contain: the shared ingress path, the cluster-scoped resource, the control plane both tenants call, the node both tenants land on.

## Use when

- The tenancy model is being chosen or revisited, including namespace-per-tenant against cluster-per-tenant against account-per-tenant.
- A regulated, data-resident, or otherwise constrained workload needs a stronger boundary than the default model provides.
- Tenants are affecting each other: CPU throttling, control plane rate limits, storage contention, or an ingress path saturated by one team.
- RBAC has accreted and needs reduction to least privilege, or a cluster-scoped grant needs review.
- Network policy is being introduced or moved toward default-deny.
- A shared component is being added to the platform and its blast radius has not been documented.
- Quota or fair-share policy needs setting, or an existing quota needs reduction.

## Do not use when

- The subject is policy-as-code rules, waivers, and the advisory-to-blocking rollout of controls generally. That is `platform-guardrails-policy-desk`; this desk owns the isolation boundary, that desk owns the enforcement program around all controls.
- The subject is the provisioning path and modules that create tenant infrastructure. That is `self-service-infrastructure-desk`.
- The subject is environment classes and promotion between them. That is `environment-management-desk`.
- The subject is cost allocation across tenants rather than resource isolation between them. That is `platform-cost-attribution-desk`.
- The work is threat modeling the platform's own attack surface for an adversary. That is a cross-suite handoff to the Security suite; label it as such.

## Required evidence

- The current topology: clusters, accounts, projects, subscriptions, node pools, and their tenant assignments, read from the infrastructure sources that define them.
- Applied authorization state: roles, cluster roles, bindings, group mappings, and any aggregation rules, at their live values rather than their intended ones.
- Workload identity configuration: service account and token projection settings, federation trust relationships, and which cloud roles a tenant workload can assume.
- Network policy objects, default posture, service mesh authorization policies, egress controls, and DNS policy.
- Admission configuration: policy bundles, pod security enforcement level per namespace, webhook configurations, and their failure policy.
- Scheduling and quota state: resource quotas, limit ranges, priority classes, taints and tolerations, and observed contention from telemetry.
- The inventory of shared components, including ingress, DNS, secret store, registry, log and metrics collectors, CI runners, and the control plane itself.
- Regulatory and data-residency constraints applying to specific tenants.

## Workflow

**Outcome.** A stated tenancy model with the isolation controls that implement it, each control named with its enforcement point and its evidenced state; a quota and fair-share policy; noisy-neighbor mitigations tied to the contention actually observed; and a blast radius statement for every shared component.

**Grounding.** Isolation claims come from applied configuration and admission state, not from design documents. A control described in an architecture note and absent from the policy bundle is recorded as claimed and not enforced, and that distinction is the core value of this stage. Where the documented model and the live topology disagree about which tenants share a boundary, record both and preserve the conflict.

**Constraints.** Each control names what it prevents, at which enforcement point, and how its current state was established. Failure modes are stated explicitly: a webhook that fails open provides no isolation during its own outage, and a policy engine whose failure policy is unset must be treated as unknown rather than as enforcing. Blast radius is written per shared component as the concrete consequence of that component failing or being compromised, naming the tenants affected. Quota policy distinguishes the limit that protects the platform from the limit that shapes tenant behavior, and fair-share treats the control plane and shared storage as contended resources rather than only CPU and memory. Least privilege is assessed against what a grant actually permits, including transitive reach through workload identity into cloud roles, which is where namespace boundaries most often stop mattering.

**Parallel surface.** Independent tenants, independent namespaces or accounts, independent control classes, independent shared components, and independent policy objects fan out safely. The cross-tenant blast radius judgment, the aggregate least-privilege finding, and the model-level decision about whether the boundary is sufficient for the regulated subset run once, after the fan-out returns, because an isolation review assembled per tenant and never reconciled misses exactly the shared paths it exists to find.

**Ordered gate for tightening a live boundary.** Moving a shared boundary to enforcement, such as default-deny network policy, a restricted pod security level, or a reduced quota, runs in this order because denial takes effect immediately, the resulting tenant outage is indistinguishable from an attack, and step 4 has no undo for workloads already evicted or refused:

1. Observe current traffic, identity use, or consumption and derive the required allow set from measured behavior.
2. Notify the affected tenant owners with the allow set, the exception path, and the enforcement date.
3. Enforce in audit or dry-run mode and reconcile the violations that appear against the derived allow set.
4. Enforce in blocking mode, with the rollback trigger and observation window stated before the change is applied.

Teardown of a namespace, account, or cluster follows the destructive sequence in `references/suite-workflow-contract.md` rather than this one.

**Acceptance bar.** A security reviewer could tell, from the artifacts alone, which controls are enforced, which are claimed, and what a compromise of any shared component reaches. Every control names its enforcement point and evidence, every shared component has a blast radius statement naming affected tenants, and quota policy states both the protective limit and the behavior it shapes.

## Outputs

A complete run delivers this set:

- `tenancy-model.md`: the chosen model, the boundary each tenant gets, why the model fits the regulatory and contention constraints, and the tenants that require an exception to it.
- `isolation-controls.md`: identity, authorization, network, runtime, node, and admission controls, each with its enforcement point, its evidenced state, and its failure mode.
- `rbac-and-workload-identity-review.md`: grants assessed against least privilege, including cluster-scoped grants and the transitive reach from workload identity into cloud roles.
- `quota-and-fairshare-policy.md`: quotas, limit ranges, priority and preemption behavior, and the contended resources beyond CPU and memory, including control plane request budgets and shared storage.
- `noisy-neighbor-analysis.md`: contention observed in telemetry, the mechanism behind each instance, and the mitigation with its enforcement point.
- `blast-radius-register.md`: one entry per shared component with the failure consequence, the compromise consequence, the tenants affected, and the containment that exists today.
- `tenancy-downstream-handoff.md`: what `self-service-infrastructure-desk` inherits, including the boundaries provisioning must not cross.

Depth standard: an artifact is complete when a security reviewer and a platform engineer could both act on it unchanged. A control with no enforcement point, or a shared component with no named affected tenants, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the cluster or account configuration, policy bundle, or authorization state exists and cannot be read, the run delivers `tenancy-connector-diagnostic.md` naming each unreachable source and the isolation claims that depend on it. Isolation is never described as enforced against configuration that could not be read.

Anti-fabrication guard: this desk produces the sentence "tenants are isolated," which is the single most consequential sentence in the suite and the one most likely to be written from a diagram. The failure is not inventing a control out of nothing; it is upgrading a documented intention into an enforced state because the design says the network policy exists and reading the applied objects would have taken longer. Enforcement is asserted only from applied configuration: the policy object, the binding, the admission setting, the failure policy. A control present in a design document and absent from applied state is recorded as claimed and not enforced. Where a policy engine's failure policy could not be established, the control is unknown rather than enforcing, because a webhook that fails open during its own outage is exactly when isolation matters. Cluster, account, and namespace identifiers, role binding names, quota values, and node pool assignments are quoted from the source or left unknown, since a wrong identifier in an isolation artifact sends the next reader to inspect the wrong boundary and come back reassured.

## platform_packet fields to update

- `tenancy.model`
- `tenancy.isolation_controls` with enforcement point and evidenced state per control
- `tenancy.blast_radius_notes` per shared component
- `tenancy.quota_policy`
- `guardrails[]` for isolation controls with an admission or provisioning enforcement point, including `mode` and `exception_ref`
- `consumers[].tenant` for tenants whose boundary was assessed
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: continuing would assert tenant isolation, RBAC scope, workload identity reach, secret access, or data-residency behavior as verified without applied-configuration evidence, or the review would expose credentials, tokens, or tenant data.
- **Production or destructive**: the next action would apply or tighten policy on a live cluster, reduce a quota in force, rotate workload identity trust, or tear down a namespace or account.
- **Missing approval**: an isolation exception for a tenant, a quota reduction, or a move from audit to blocking enforcement needs a named owner who has not authorized it.
- **Source conflict**: the topology source, the policy bundle, and the authorization state genuinely disagree about which tenants share a boundary, and choosing one silently would publish an isolation claim that does not hold.
- **Release integrity**: the boundary would be declared adequate for a regulated tenant without evidence that the controls it depends on are applied and their failure modes known.
- **Connector unreachable**: the cluster or account configuration, policy bundle, authorization state, or contention telemetry exists and cannot be read.

Missing quota figures, absent contention history, and undocumented node pool intent are soft gaps. Name them, label the assumption, and continue. Isolation and approval boundaries are never relaxed to keep a workflow moving.

## Downstream handoffs

`self-service-infrastructure-desk` is next and needs the tenancy model, the boundaries provisioning must not cross, and the quota enforcement points so provisioning refuses rather than over-allocates. `environment-management-desk` needs the boundary each environment class inherits. `platform-guardrails-policy-desk` inherits the isolation controls that become policy-as-code rules with waiver paths. `platform-cost-attribution-desk` needs the tenancy boundaries as its allocation edges. `platform-slo-reliability-desk` inherits the blast radius register as its dependency and single-point-of-failure input. Send adversarial threat modeling of the platform's attack surface to the Security suite as a labeled cross-suite handoff.

## Quality bar

Good tenancy work is specific about what the boundary does not do. It names the shared ingress, the cluster-scoped resource, the control plane API both tenants call, and the node they land on together, and it states what a failure or compromise of each reaches. Controls are described in the state they are actually in, with claimed and enforced kept apart. Quota policy accounts for the resources that are contended in practice rather than the two that are easiest to limit. The register of shared components is complete enough that adding a new shared component to the platform obviously requires adding a row, which is the property that keeps the artifact alive after this run.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
