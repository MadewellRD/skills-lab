---
name: platform-adoption-migration-desk
description: drive adoption of an internal developer platform including the adoption funnel and activation definition, migration wave sequencing with named cohorts, onboarding and enablement material, the incentive and support model that moves holdouts, migration debt tracking, and escape-hatch usage that signals a golden path is not actually paved.
---

# Platform Adoption Migration Desk

## Suite workflow mode

This desk is part of the Platform Engineering Command Desk suite. Complete the adoption artifact set, update the `platform_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent tenant names, adoption counts, migration effort estimates, cohort membership, onboarding dates, or holdout reasons.

## Role

Own the movement of teams onto the platform and the truth about how far that has actually gone. A platform is a product whose users can walk away to a workaround, so adoption is not a rollout schedule; it is a funnel with a defensible activation definition, cohorts sequenced by real dependency and risk, enablement that reduces the work rather than describing it, and a holdout analysis that distinguishes teams who will not move from teams who cannot.

This desk also owns the platform's most honest instrument: escape-hatch usage. Teams routing around the paved road are not deviants, they are a measurement. When many of them route around the same point, the finding belongs upstream in the golden path, not in an enablement campaign.

## Use when

- Defining or correcting the activation definition and the adoption funnel that sits behind an adoption number.
- Sequencing a migration into waves with named cohorts, effort estimates, and a capacity check against the platform team's ability to support concurrent migrations.
- Onboarding and enablement material is needed: quickstarts, migration guides, worked examples, paired migration sessions, automated migration pull requests.
- Adoption has stalled and the holdouts need classifying by cause rather than by attitude.
- Migration debt has accumulated: partially migrated services, dual-running systems, forked templates, temporary shims that outlived their reason.
- Escape-hatch usage is rising and the question is whether the golden path has a gap.

## Do not use when

- The change is being pushed to teams already on the path rather than moving teams onto it: that is `platform-change-rollout-desk`. Rollout pushes a version; this desk pulls a population.
- The finding is that the paved road is missing a capability, a supported stack, or a sane default: route upstream to `golden-path-design-desk`, because enablement cannot fix an unpaved path.
- The friction baseline itself needs measuring: onboarding time, lead time, provisioning wait, and survey evidence belong to `developer-experience-research-desk`.
- The capability teams are being moved off is being retired with notice windows and an enforcement ladder: that is `platform-deprecation-sunset-desk`.
- Repeated onboarding questions have become a support load problem: that is `platform-support-operations-desk`.

## Required evidence

- The consumer inventory with per-tenant onboarding state, from the catalog rather than from a spreadsheet of intentions.
- Telemetry that distinguishes activation from registration: pipeline runs through the paved path, deploys reaching production, provisioned resources created through the platform API.
- Escape-hatch signals: direct IaC outside the platform modules, custom pipelines bypassing the reusable workflows, console-created resources, forked templates, and the tenants attached to each.
- Migration effort evidence: prior migration durations, service complexity signals, and stated blockers from tickets or the survey.
- Existing enablement material with its currency, since a migration guide written against a superseded template version actively costs adoption.
- Golden path tiers and their backing templates, so a cohort is not scheduled onto a path with no template behind it.
- The platform team's available support capacity for the wave window.

## Workflow

**Outcome.** An adoption funnel with a defensible activation definition and current counts from real sources, a wave plan with named cohorts and sequencing rationale, enablement material matched to the cohorts that need it, a holdout classification by cause with the specific action each class needs, a migration debt register, and an escape-hatch analysis that routes structural gaps upstream.

**Grounding.** Read catalog and telemetry for who is actually on the platform; read onboarding records, tickets, and survey responses for why they are or are not. Where the adoption dashboard and the pipeline telemetry disagree about who is onboarded, record both and preserve the conflict per `references/suite-workflow-contract.md`. That disagreement is usually the activation definition failing.

**Constraints.** Activation is defined as a behavior with a signal behind it, such as a production deploy through the paved pipeline, rather than a state that costs a tenant nothing, such as a repository created from a template. An adoption number computed on the weaker definition is the single most common way a platform program reports success while its consumers are still on the old path.

Wave sequencing follows dependency and risk, not alphabetical or organizational convenience: services with shared dependencies move together or the migration produces a period where both paths must work; stateless before stateful; non-revenue before revenue path; regulated cohorts last and with their own constraints. Every wave is sized against the platform team's actual support capacity for that window, because a wave that exceeds it converts migration support into a queue and turns willing teams into holdouts.

Holdouts are classified by cause: blocked by a missing capability, blocked by an unpaid migration cost, unaware, or unwilling. Each class takes a different action, and only the last is a governance conversation. Escape-hatch usage is treated as a diagnostic signal rather than as non-compliance; where a single gap explains a cluster of escapes, the finding is routed upstream rather than converted into a compliance push.

**Parallel surface.** Tenants, services, cohorts, escape-hatch instances, and enablement assets are independent units and are parallel-safe; per-tenant migration assessment, per-service effort estimation, per-asset currency review, and connector preflight across the catalog, telemetry, and ticket queue all fan out.

The aggregate work runs once after the fan-out returns: the funnel totals and the adoption percentage with its denominator, the wave ordering under dependency constraints, the support capacity check across concurrent waves, the holdout ranking, and the cross-tenant pattern that turns a set of individual escapes into a golden-path finding.

**Acceptance bar.** The activation definition is stated and every count is computed against it from a named source. Cohorts contain real tenants with real owners. Each holdout class has an action that matches its cause. Enablement material is current against the template version the platform ships today. Escape-hatch clusters are either explained or routed upstream.

## Outputs

A complete run delivers this artifact set:

- `platform-adoption-funnel.md`: stage definitions, the activation definition with its signal, current counts per stage with the query behind each, the denominator for every percentage, and the drop-off point that costs the most.
- `platform-migration-waves.md`: cohorts with named tenants and services, sequencing rationale, per-wave effort and support capacity, entry and exit criteria, and the dependency constraints that fix the order.
- `platform-enablement-plan.md`: the material each cohort needs, its current state and version alignment, the assisted-migration offer, and the owner of each asset.
- `platform-migration-debt.md`: partially migrated services, dual-running systems, shims and forks with the reason each exists, the cost of leaving it, and the closure owner and date.
- `platform-adoption-downstream-handoff.md`: for `platform-support-operations-desk`, the request classes each wave will generate; for `golden-path-design-desk`, the structural gaps the escape-hatch analysis surfaced.

Depth standard per artifact: a funnel entry states the query and the population it ran against, not a stage label with a number beside it. A cohort entry names its services and their owners. A holdout entry names the specific blocking capability or the specific unpaid cost, because "resistant to change" is not a cause anyone can act on. A debt entry states what breaks if the shim is removed today.

In `diagnostic` mode, when the catalog, telemetry, or ticket queue exists and cannot be read, the run delivers `platform-adoption-connector-diagnostic.md` reporting reachability, the queries attempted, and the exact access needed. Adoption counts are not estimated in that mode.

Adoption is where this suite is most tempted to grade its own homework. A percentage reads as measurement whether it was queried or inferred, and an adoption figure is quoted in leadership reviews long after anyone could reconstruct it. In these artifacts every count names the catalog query, telemetry query, or export that produced it and the date it was run; every percentage names its denominator; and a population nobody counted is written as unmeasured rather than approximated. Cohort membership comes from the catalog, because a migration wave containing a team that does not exist wastes a support window and one missing a team that does exist strands them at cutover. A holdout reason is quoted from the ticket, the survey response, or the named conversation, never inferred from the fact that a team has not moved.

## platform_packet fields to update

- `adoption.onboarded`, `adoption.target_population`, `adoption.activation_definition`, `adoption.migration_waves`, `adoption.holdouts`.
- `consumers[].onboarding_state` and `consumers[].escape_hatches_in_use` per tenant.
- `golden_paths[].tier` where escape-hatch evidence contradicts a claimed paved tier.
- `devex_metrics[]` for time-to-first-deploy and onboarding time where this stage measured them.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: a migration deadline, a mandate, or an incentive that changes a team's committed roadmap needs the named owner who has not given it.
- Production or destructive: the next action would migrate, cut over, or decommission a tenant's live workload or its existing path.
- Security or privacy: a cohort includes systems whose migration crosses a data-residency, regulated, or isolation boundary that has not been cleared.
- Source conflict: the catalog, telemetry, and the adoption dashboard genuinely disagree on who is onboarded, and picking one silently would misreport program state to the people funding it.
- Release integrity: a cohort would be scheduled onto a golden path with no evidence that a backing template, module, or pipeline exists and works.
- Connector unreachable: the catalog, telemetry, onboarding records, or ticket queue exists and cannot be read.

Missing effort estimates, absent survey data, and unknown team capacity are soft gaps: proceed with them named. An adoption number is never estimated to fill a reporting line, and a wave is never scheduled onto an unbacked path to hit a date.

## Downstream handoffs

`platform-support-operations-desk` needs the wave calendar and the request classes each cohort will generate, so the rotation is staffed before the wave rather than after it. `platform-governance-desk` inherits the holdouts that are genuinely a decision-rights question and the exceptions granted to teams that cannot move. `golden-path-design-desk` receives the escape-hatch findings that are structural. `platform-deprecation-sunset-desk` takes the remaining-user picture when the old path is being retired.

## Quality bar

An adoption number the platform team would defend in front of the teams it describes. Cohorts that match reality, sequenced by dependency rather than by convenience. Enablement that removes work instead of documenting it. Holdouts explained by cause. And escape-hatch usage read as feedback about the road, which is what it is.
