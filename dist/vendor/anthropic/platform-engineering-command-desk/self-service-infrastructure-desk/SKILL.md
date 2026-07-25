---
name: self-service-infrastructure-desk
description: design self-service infrastructure abstractions and the provisioning path, covering reusable modules compositions and resource claims, module versioning and pinning, the reconciliation model and gitops sync behavior, state backends and locking, drift detection and remediation, request-to-resource latency targets, quota and policy preflight at provisioning time, and the day-two operations a tenant performs without filing a ticket. use for infrastructure module design, provisioning workflow, drift and reconciliation, resource claims, terraform or crossplane abstractions, and eliminating ticket-driven infrastructure.
---

# Self-Service Infrastructure Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the provisioning artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent module versions, provider constraints, resource identifiers, state backend locations, provisioning durations, drift counts, or quota values.

## Role

Own the path from a tenant's request to a running resource without a human in the middle. This desk defines the infrastructure abstractions tenants consume, the modules and compositions behind them, how a request is reconciled into real resources, how state and drift are handled, what preflight runs before anything is created, and which day-two operations a tenant performs on their own.

Day two is where self-service is won or lost. Provisioning a database is a one-time event; resizing it, restoring it, rotating its credentials, and changing its retention are the operations that generate tickets forever if the abstraction stops at creation.

## Use when

- Infrastructure is provisioned by ticket and the request path needs to become self-service.
- Module or composition design is being started or consolidated, including versioning, pinning, and the registry that serves them.
- The reconciliation model needs deciding or fixing: pipeline apply against control-plane reconciliation, sync behavior, pruning, and what happens when a tenant edits a managed resource by hand.
- Drift is suspected or known and detection, reporting, and remediation need designing.
- Provisioning succeeds and then strands tenants at day two, so the operation set a tenant owns needs defining.
- Quota or policy is enforced too late and half-built stacks are the result.

## Do not use when

- The subject is the schema tenants write against rather than the implementation behind it. That is `platform-api-contract-desk`.
- The subject is the tenancy boundary and isolation controls the provisioning path must respect. That is `tenancy-isolation-desk`, whose boundaries this desk consumes.
- The subject is the repository template that emits infrastructure definitions on scaffold. That is `scaffolding-templates-desk`.
- The subject is environment classes, promotion, and ephemeral lifetimes. That is `environment-management-desk`.
- The subject is the policy program with waivers and the advisory-to-blocking rollout. That is `platform-guardrails-policy-desk`; this desk owns the preflight enforcement point, that desk owns the policy program.

## Required evidence

- The module, composition, chart, and resource claim sources at their real versions, with their provider and dependency constraints.
- The module registry or repository layout, its release process, and how consumers pin versions.
- Reconciliation configuration: pipeline definitions or controller configuration, sync intervals, prune settings, drift behavior, and health assessment.
- State backend configuration, locking mechanism, and per-workspace or per-tenant separation.
- The current provisioning path end to end, including approval steps and any manual handoff.
- Plan or diff output and reconciliation history, which is the only evidence that establishes drift state.
- Inventory of resources created outside the managed path, which is where the real drift lives.
- Provisioning latency evidence from pipeline runs, controller events, or ticket cycle time.
- The tenancy boundaries and quota enforcement points from the upstream stage.

## Workflow

**Outcome.** A defined set of infrastructure abstractions with their backing modules and versions, a provisioning and reconciliation path that reaches a running resource without a ticket, stated request-to-resource latency expectations, a drift model with detection and remediation, preflight that fails a request before anything is created, and the day-two operation set a tenant owns.

**Grounding.** Read what the platform provisions from the module and composition sources, and read what exists from the reconciliation and state evidence. Drift is a comparison result, so it is reported from a plan, diff, or reconciliation status rather than inferred. Where the module source and the deployed resources disagree, that is the drift finding, recorded with both sides attributed.

**Constraints.** Every abstraction states what it actually creates, including the resources a tenant does not see, because the hidden resources are what appear on their cost report and in their incident. Modules are versioned and consumers pin, since an unpinned provider upgrade is a production change nobody authored. Preflight runs before creation and covers quota, policy, naming, and boundary constraints, because a request that fails halfway leaves an orphaned stack that only a platform engineer can clean up. Every change class is labeled in-place or replace, and replace on a stateful resource is treated as a data-loss path with its own approval rather than as a normal apply. Day-two operations are enumerated explicitly with the mechanism for each, and any operation not on the list is a known ticket source rather than an oversight. Latency expectations are stated per abstraction as a target with the measurement source, since request-to-resource time is the number tenants judge self-service by.

**Parallel surface.** Independent modules, independent abstractions, independent tenants, independent drift checks, and independent day-two operations fan out safely. The dependency ordering between abstractions, the aggregate drift picture across the estate, the shared-module blast radius judgment, and the decision about which abstractions ship first run once, after the fan-out returns.

**Ordered gate for bringing an existing resource under management.** This order is mandated because an apply against a resource absent from state creates a duplicate or destroys the live one, and step 4 is the first irreversible action:

1. Record the existing resource's current configuration and identifiers from the provider.
2. Import it into state so the managed definition and the live resource refer to the same object.
3. Produce a plan and reconcile the definition until the plan is empty or shows only intended in-place changes.
4. Apply, with any replace-class change on a stateful resource approved separately before this step runs.

Teardown and quota reduction follow the destructive sequence in `references/suite-workflow-contract.md` rather than this one.

**Acceptance bar.** A tenant could request the abstraction, receive a working resource, and perform every listed day-two operation without opening a ticket. Each abstraction names its backing module and version, what it creates, its preflight checks, its latency target with a measurement source, its drift behavior, and its day-two operation set with the mechanism for each.

## Outputs

A complete run delivers this set:

- `infrastructure-abstractions.md`: one entry per abstraction with the backing module or composition, its version, everything it creates including hidden resources, its inputs and their defaults, and its escape hatch.
- `provisioning-path.md`: request through preflight through reconciliation to ready, with the failure behavior at each point and where a human is still required.
- `reconciliation-and-drift-model.md`: the reconciliation mechanism, sync and prune behavior, how drift is detected, what is remediated automatically, what is reported, and how a hand edit to a managed resource is handled.
- `state-management.md`: backend layout, locking, per-tenant or per-workspace separation, recovery expectations, and the operations that require state manipulation.
- `preflight-and-quota-enforcement.md`: the checks that run before creation, their order relative to resource creation, the message a tenant receives on rejection, and the quota source each check reads.
- `day-two-operations.md`: the operations a tenant owns, the mechanism for each, the operations that remain platform-owned, and the ticket volume each remaining one generates.
- `provisioning-latency-targets.md`: per abstraction, the request-to-resource expectation, the current measured value or its unmeasured state, and where the time goes.
- `self-service-downstream-handoff.md`: what `scaffolding-templates-desk` inherits, including which abstractions templates should wire in by default.

Depth standard: an artifact is complete when a platform engineer could implement the abstraction and a tenant could operate it from the same set. An abstraction entry that omits hidden resources, or a day-two list with no mechanism per operation, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the module sources, state backend, reconciliation status, or provider inventory exists and cannot be read, the run delivers `self-service-connector-diagnostic.md` naming each unreachable source and the drift and coverage claims that depend on it. Drift state is not asserted from an unread plan.

Anti-fabrication guard: drift is a measurement, and this desk fails by reporting it as an impression. Writing that an estate is reconciled without a plan, diff, or controller status behind it produces the most dangerous kind of wrong answer, because it tells a reader to stop looking exactly where the divergence is. Every drift statement names the plan output, sync status, or reconciliation event it came from, and where none was available the state is `unknown` rather than `reconciled`, which is a legitimate packet value. Module versions, provider constraints, and resource identifiers are quoted from the sources or left unknown. Provisioning latency figures name the pipeline runs, controller events, or ticket records they were computed from, along with how many observations, since a target presented as a measurement is how a platform team ends up defending a number it never collected. A change is labeled replace only when a plan says so, because guessing that a change is in-place is how a stateful resource gets recreated.

## platform_packet fields to update

- `abstractions[]` with `name`, `version`, `provisions`, and `drift_state`
- `environments[].provisioning` for classes this path serves
- `tenancy.quota_policy` where provisioning-time enforcement changes it
- `guardrails[]` for preflight checks, with `enforcement_point` set to provisioning and their `mode`
- `devex_metrics` for provisioning wait, with its measured value or unmeasured state and source
- `support_load.request_classes` for operations that remain ticket-driven
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would apply against live infrastructure, manipulate or migrate state, prune resources, or execute a plan containing a replace on a stateful resource.
- **Missing approval**: a replace-class change to a stateful resource, a quota reduction, or adoption of another team's existing infrastructure into the managed path needs a named owner who has not authorized it.
- **Security or privacy**: module inputs, state contents, or plan output would expose secrets, keys, or connection strings, or the provisioning path would grant a role that crosses the tenancy boundary set upstream.
- **Source conflict**: the module source, the state file, and the live provider inventory genuinely disagree about what exists, and picking one silently would produce an apply that destroys or duplicates a resource.
- **Release integrity**: an abstraction would be published as self-service without evidence that its provisioning path completes and its day-two operations work.
- **Connector unreachable**: the module registry, state backend, reconciliation status, or provider inventory exists and cannot be read.

Missing latency measurements, absent drift history, and unknown ticket volume for a remaining manual operation are soft gaps. Name them and continue.

## Downstream handoffs

`scaffolding-templates-desk` is next and needs the abstractions, their default inputs, and their pinned versions so generated repositories reference the supported ones. `environment-management-desk` needs the provisioning path and its latency profile, since ephemeral environments are provisioning under a time constraint. `platform-guardrails-policy-desk` inherits the preflight checks as policy rules with enforcement points. `platform-cost-attribution-desk` needs the full resource list per abstraction, including the hidden resources, since those are the ones that arrive unexplained on a tenant's bill. `platform-observability-desk` needs the provisioning and reconciliation events worth instrumenting. Send implementation of the modules themselves to Claude Code through the SDLC suite handoff, labeled as a cross-suite handoff.

## Quality bar

Good self-service is judged at day two, not day one. The abstraction discloses everything it creates, including what the tenant will later find on their bill. Preflight fails a bad request before a single resource exists, and the rejection message tells the tenant what to change. Drift is detected on a schedule rather than discovered during an incident, and the model says plainly what is remediated automatically and what is only reported. The day-two list is honest about what still needs a platform engineer, because an unlisted operation does not disappear; it becomes a ticket and then a workaround and eventually an unmanaged resource.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
