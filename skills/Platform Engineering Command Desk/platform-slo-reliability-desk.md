---
name: platform-slo-reliability-desk
description: define platform slis and slos for the control plane, provisioning path, pipelines, registries, and developer portal including error budget policy and its consequences, dependency and single-point-of-failure analysis, degradation modes when a platform component fails, and the honest split between measured and aspirational objectives.
---

# Platform SLO Reliability Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the reliability artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent objective figures, measured availability, incident counts, dependency inventories, or error budget states.

## Role

Own the reliability commitments the platform makes to its tenants, and the honesty of those commitments. The platform is a dependency of every team's delivery path, so its outage is their outage; this desk states what the platform promises about the control plane, the provisioning path, the build and deploy pipelines, the registries, and the portal, what the promise costs when it is missed, and what still works when a component fails.

The load-bearing distinction is between an objective with a query behind it and an objective that appeared in a document. Both look identical on a slide. Only one can be missed.

## Use when

- Defining or revising SLIs and SLOs for platform components rather than for tenant workloads.
- An error budget policy needs writing, or the existing one has no consequence attached and nobody acts on a burn.
- Dependency and single-point-of-failure analysis for the platform: identity provider, DNS, secret store, container registry, source host, cloud control-plane API, shared ingress, the single control-plane cluster, the single region.
- Degradation behavior needs specifying: what a tenant can still do when the portal, the admission engine, the reconciler, or the runner fleet is unavailable.
- A commitment is being quoted to tenants or leadership and its measurement basis needs establishing before it is published.
- Incident history suggests the platform's stated reliability and its lived reliability disagree.

## Do not use when

- The signals do not exist yet and the work is instrumentation, routing, or schema: that is `platform-observability-desk`, whose measured-versus-unmeasured verdict this desk consumes.
- The subject is a tenant service's own SLOs, its on-call rotation, or incident command for a tenant workload: cross-suite handoff to the SRE suite.
- Support response expectations, ticket routing, and rotation staffing for platform requests: that is `platform-support-operations-desk`. An SLO covers the system; a response expectation covers the humans.
- Isolation blast radius as a tenancy design question: that is `tenancy-isolation-desk`. This desk consumes its blast-radius notes as dependency input.
- Sequencing a risky platform upgrade across rings: that is `platform-change-rollout-desk`, which consumes the error budget state as a promotion gate.

## Required evidence

- The platform component inventory with the interface each one exposes to tenants.
- Telemetry availability per candidate SLI from the observability stage, including which signals are emitted today and which are not.
- Existing recording rules, SLO definitions, and dashboards, with their query text rather than their titles.
- Incident and outage history for platform components, with duration, affected tenants, and cause where recorded.
- The dependency map: what the platform calls, what calls the platform, and which of those are shared with the tenants themselves.
- Current error budget consumption and how it was computed, if anything computes it.
- Any commitment already published to tenants in the portal, a service description, or a chargeback agreement.

## Workflow

**Outcome.** A set of platform SLIs with implementations that a reader could rebuild from the definition, objectives labeled measured or aspirational against real query evidence, an error budget policy whose consequences bind someone, a ranked dependency and single-point-of-failure list, and a stated degradation mode per component.

**Grounding.** Read recording rules, dashboards, and incident records for reality; read the service description, portal, and reliability documentation for intent. A published objective with no rule computing it is recorded as aspirational with both sources attributed, per `references/suite-workflow-contract.md`. That gap is the deliverable, not a formatting problem.

**Constraints.** Each SLI states its good-event and valid-event definitions precisely enough that two people compute the same number, and names its measurement point, because a control-plane availability measured at the load balancer and one measured from a tenant's pipeline are different commitments. Failure attribution is fixed before the objective is published: a build pipeline SLO that counts tenant test failures as platform misses is unusable, and one that lets the platform exclude anything it chooses is unfalsifiable, so the exclusion rule is written in advance and applied uniformly.

Objectives are set against what tenants need from the platform, not against the number the current data happens to produce. An objective that the platform currently misses is a valid output; adjusting the target to match observed performance is how a reliability program stops meaning anything. The error budget policy names what changes on burn, who is bound by it, and who can override it, because a policy with no named consequence is a metric. Degradation modes are stated per component in terms of what a tenant can still accomplish, since "the portal is down" matters far less than whether deploys still work while it is down.

**Parallel surface.** Platform components, candidate SLIs, dependencies, and failure modes are independent units and are parallel-safe; per-component SLI drafting, per-dependency failure analysis, and connector preflight across telemetry, incident records, and documentation all fan out.

The aggregate work runs once after the fan-out returns: the composite reliability of an end-to-end developer journey across chained components, the single-point-of-failure ranking, the total error budget policy that governs all objectives together, and the reconciliation of per-component views into the platform's overall posture.

**Acceptance bar.** Every objective is labeled measured or aspirational with the query or the absence of one named. Every dependency has a stated failure consequence for tenants. The error budget policy names a person or role that is bound by it. No objective is stated as a percentage without a window and a measurement point.

## Outputs

A complete run delivers this artifact set:

- `platform-slo-definitions.md`: SLI specification and implementation per component with measurement point, window, objective, attribution and exclusion rule, and the measured or aspirational label with its evidence.
- `platform-error-budget-policy.md`: burn thresholds, what changes at each threshold, who is bound, the override path with its approver, and the reset boundary.
- `platform-dependency-risk.md`: the dependency map with single points of failure ranked, blast radius per failure, current mitigation, and the residual risk that no mitigation covers.
- `platform-degradation-modes.md`: per component, what tenants can still do during its failure, what silently stops, what accumulates while it is down, and the recovery expectation.
- `platform-slo-downstream-handoff.md`: the budget state and promotion gates `platform-change-rollout-desk` inherits, and the objectives `platform-cost-attribution-desk` should price.

Depth standard per artifact: an SLI entry gives the ratio, the events on both sides of it, and where they are counted, not the component name plus a target. A degradation entry names the accumulating consequence, since a stopped reconciler produces drift that surfaces days later rather than an outage anyone notices at the time. A dependency entry that says "highly available" without naming the failure domain that availability spans is incomplete.

In `diagnostic` mode, when telemetry, recording rules, or incident history exists and cannot be read, the run delivers `platform-slo-connector-diagnostic.md` reporting reachability, the queries attempted, and the exact access needed. Objectives are not labeled measured in that mode.

Reliability documents fail by publishing a number nobody computes. A percentage carries authority that its source rarely earns, and once "99.9% control plane availability" is in a portal page, every downstream decision treats it as observed. In these artifacts an objective without a query behind it is written as aspirational and stays that way until instrumentation exists; an availability figure names the recording rule or dashboard that produced it; an incident count comes from the incident record rather than from recollection; and a dependency described as redundant names the failure domain the redundancy actually spans. An objective honestly marked aspirational is a working commitment to instrument it. A fabricated measured objective is a promise the platform will be held to and cannot check.

## platform_packet fields to update

- `platform_slos[]`: `service`, `sli`, `objective`, `window`, `error_budget_policy`, `current_state`.
- `tenancy.blast_radius_notes` extended with dependency-driven blast radius.
- `devex_metrics[]` where a reliability metric doubles as an experience baseline, with its source.
- `governance.approval_gates` for the budget-policy consequences that require an owner.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: publishing an objective to tenants, or activating an error budget consequence that halts feature work, needs the named owner who has not given it.
- Production or destructive: the next action would change live alerting, recording rules, or failover configuration for a shared platform component.
- Security or privacy: dependency analysis would require asserting identity-provider, secret-store, or trust-root behavior as verified without evidence, or would expose credential paths in a runbook-adjacent artifact.
- Source conflict: telemetry, incident records, and the published service description genuinely disagree about availability or scope, and picking one silently would misstate a commitment.
- Release integrity: an objective would be declared measured, or a component declared meeting its target, without a query or export establishing it.
- Connector unreachable: the telemetry backend, recording-rule definitions, or incident record exists and cannot be read.

Absent incident history, unmeasured components, and undocumented dependency ownership are soft gaps: proceed with them named. An objective is never relabeled from aspirational to measured to make a report look complete.

## Downstream handoffs

`platform-cost-attribution-desk` needs the reliability commitments that carry cost, since redundancy across failure domains is a spend decision. `platform-change-rollout-desk` needs the error budget state as its ring promotion gate and the degradation modes as its rollback triggers. `platform-support-operations-desk` needs the degradation modes as the basis for its runbooks and the objectives that shape escalation. Cross-suite: tenant-workload reliability engineering and incident command go to the SRE suite.

## Quality bar

Objectives a tenant would recognize as describing their experience, computed from queries that exist, missed openly when they are missed. Dependencies named down to the failure domain. A budget policy that has changed someone's plan at least once, or an explicit note that it has not. Aspirational objectives labeled as such without embarrassment, because that label is what makes the measured ones credible.
