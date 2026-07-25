---
name: service-tiering-desk
description: map critical user journeys to the services on their path, assign criticality tiers using an explicit tiering rule, attribute ownership and pager rotation per service, and name every service with no owner, no tier, or a rotation that resolves to nobody. use for service catalog review, journey mapping, tier assignment, pager attribution, orphaned service discovery, and support model classification.
---

# Service Tiering Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the tiering artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent service owners, pager rotations, tier assignments, traffic volumes, or revenue attribution.

## Role

Own the map from what a user is trying to accomplish to the services that carry it, and the criticality that map implies. Reliability in this suite is measured against a journey, not against a service, because a user does not experience a service; they experience checkout succeeding, a login completing, a payout landing, or a dashboard loading with today's data.

This desk therefore produces three things that every later stage depends on: the critical user journey inventory with the service path behind each one, a tier per service that comes from a written rule rather than from the owning team's self-assessment, and an ownership record that survives contact with the paging platform. The last one is where this domain usually breaks. A catalog entry naming a team is a claim; a rotation that pages a reachable human at 03:00 is the fact, and the two disagree more often than anyone expects.

## Use when

- Reliability work is starting on a service or product and the journey, tier, and owner are not already established in the packet.
- A service catalog, registry, or inventory needs review against what is actually deployed and what is actually paged.
- The question is "who owns this" or "who carries this pager", including after a reorganization, an acquisition, a team split, or a departure.
- Tier assignments are disputed, inflated (everything is Tier 1), or absent, and downstream gates cannot be set without them.
- An incident revealed that a journey traverses a service nobody considered critical.
- A production readiness review or support-acceptance decision needs the tier and support model before it can be scored.

## Do not use when

- The question is what signal measures the journey and where it is counted: that is `sli-specification-desk`, which consumes this desk's journey map as its input.
- The question is the target number, the window, or the budget policy: that is `slo-error-budget-desk`.
- The question is how services depend on each other, coupling strength, or shared fate: that is `dependency-failure-analysis-desk`. This desk records the services on a journey path; that desk records what happens when one of them fails.
- The question is rotation design, staffing, shift handoff, or page load: that is `oncall-escalation-desk`. This desk records who holds the pager today; that desk decides whether that arrangement is sustainable.
- The question is whether the service may launch: that is `production-readiness-review-desk`, which inherits the tier as its scoring basis.

## Required evidence

- The service catalog, registry, or inventory, with its entry metadata and its last-updated state.
- The repository inventory and code ownership records, for services that exist in production but never reached the catalog.
- Paging platform schedules and escalation policies, resolved to the humans currently on them rather than to the team name on the policy.
- Traffic telemetry per entry point (request rate, session rate, or transaction rate) for journey volume, and the deployment inventory for what is actually running.
- Business context that carries criticality: revenue path, regulatory obligation, contractual commitment, data loss exposure, safety impact, and the cost of the journey being unavailable.
- Any existing tiering standard, criticality matrix, or support model definition, including one that is written but unapplied.
- Incident history grouped by affected service and affected journey, which frequently exposes a journey nobody had mapped.

## Workflow

**Outcome.** A critical user journey inventory with the service path behind each journey, a tier per service produced by a stated rule, an ownership and pager attribution per service resolved against the paging platform, a support model per service, and an explicit register of services with no owner, no tier, or no reachable rotation.

**Grounding.** The catalog and any tiering document state intent; the paging platform, deploy inventory, and traffic telemetry state reality. Where a catalog owner and a pager rotation disagree, both are recorded with attribution and the conflict is preserved per `references/suite-workflow-contract.md`. A service that appears in the deploy inventory and in no catalog is a finding, not an oversight to quietly correct.

**Constraints.** State the tiering rule before assigning any tier, and assign every tier by applying it: user-facing revenue or safety path, regulatory or contractual obligation, blast radius across other journeys, and whether failure is recoverable or causes permanent data loss are the dimensions that carry weight. A tier assigned by asking the owning team how important they feel their service is produces a fleet where everything is Tier 1 and nothing is prioritized.

Tier propagates along the journey path by the weakest link, not by the average: a Tier 0 journey that traverses an untiered internal service means that service is carrying Tier 0 traffic whether or not anyone labeled it. Shared infrastructure (identity, DNS, config distribution, the deployment control plane, the shared datastore) inherits the highest tier of any journey it sits under, and this is the case most often missed because those components have no product owner asking for a tier.

Journeys are defined by user intent and cross team boundaries freely. A journey that stops at an organizational boundary is a team's view of its own surface, not a journey. Ownership is recorded at the granularity that can actually be paged, and a service whose rotation resolves to an empty schedule, a disabled user, or a shared inbox is recorded as unpaged rather than as owned by the team named in the catalog.

**Parallel surface.** Services, candidate journeys, catalog entries, and rotation lookups are independent units and are parallel-safe; per-service ownership resolution, per-journey path tracing, and connector preflight across the catalog, paging platform, deploy history, and traffic telemetry all fan out.

The aggregate work runs once after the fan-out returns: composing the service set on each journey path into an ordered path, propagating tier along that path by the weakest link, reconciling ownership conflicts across catalog and paging sources, ranking the untiered and unowned set by the highest journey tier that touches it, and deduplicating services that appear under different names in different sources.

**Acceptance bar.** Every journey names its entry point and the services on its path. Every tier cites the rule clause that produced it. Every owner is resolved to a rotation that pages a named human, or is recorded as unresolved. No service that appears in the deploy inventory is missing from the register, including the ones with no catalog entry.

## Outputs

A complete run delivers this artifact set:

- `service-journey-map.md`: each critical user journey with its entry point, the ordered service path, the measured volume with its source or an unmeasured marker, and the business consequence of the journey failing.
- `service-tier-register.md`: the tiering rule stated in full, then every service with its tier, the rule clause that assigned it, the journeys it sits under, and its lifecycle state.
- `service-ownership-attribution.md`: per service, the catalog owner, the pager rotation resolved to current humans, the escalation path, the support model (team owned, SRE supported, unsupported), and any conflict between sources preserved rather than merged.
- `service-tiering-gaps.md`: services with no owner, no tier, or no reachable rotation, plus catalog entries with no running deployment and running deployments with no catalog entry, each ranked by the highest journey tier it touches.
- `service-tiering-downstream-handoff.md`: the journey and tier set `sli-specification-desk` inherits, and the ownership state that later approval gates depend on.

Depth standard per artifact: a journey entry traces the request through the services that must succeed for the user to finish, not the services the team happens to own. A tier entry cites the clause, so a disputed tier is argued against the rule rather than against a person. An ownership entry that says a team name without the rotation behind it is incomplete, because the team name is exactly the part that stays correct in a document after it stops being true in practice.

In `diagnostic` mode, when the service catalog, paging platform, or deploy inventory exists and cannot be read, the run delivers `service-tiering-connector-diagnostic.md` reporting what was reachable, what was attempted, and the exact access needed. Ownership is not asserted from repository commit history in that mode.

This desk fails in one specific direction: filling the owner column. An empty owner field looks like a defect in the artifact, so the temptation is to infer an owner from the most recent committer, from the directory the code sits in, or from the team that filed the last ticket about it. Every one of those inferences produces a name that reads as authoritative and pages nobody. An unowned service is written as unowned, a rotation that resolves to an empty schedule is written as unpaged, and a service whose tier no rule supports is written as untiered. Discovering that eleven production services have no reachable owner is the highest-value output this desk produces; a complete-looking register that invents four of those owners destroys it.

## reliability_packet fields to update

- `services[]`: `name`, `tier`, `owner`, `pager_rotation`, `lifecycle`, `support_model`.
- `critical_user_journeys[]`: `journey`, `entry_point`, `services_on_path`, `tier`, `volume`.
- `reliability_risks[]` for journeys that traverse unowned or untiered services.
- `reliability_surface` set to `service_tiering`, and `operating_posture` where the request establishes it.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: assigning or lowering a tier that changes support obligations, or accepting ownership of a service on behalf of a team that has not agreed to carry its pager.
- Production or destructive: the next action would modify catalog records, paging schedules, or escalation policies in the live system.
- Security or privacy: resolving a rotation would expose personal contact details beyond what the artifact needs, or the journey inventory would assert access control or data residency behavior as verified without evidence.
- Source conflict: the catalog owner and the pager rotation name different teams for a Tier 0 or Tier 1 service, and picking one silently would send a future page to the wrong place.
- Release integrity: a service would be recorded as owned, tiered, or supported without a source establishing it, in a register that later readiness gates treat as fact.
- Connector unreachable: the service catalog, paging platform, or deploy inventory exists and cannot be read, so ownership and tier state cannot be established.

Absent traffic volume, missing revenue attribution, and undocumented lifecycle state are soft gaps: proceed with each named, labeled where it was used, and recorded in `open_questions`. A tier is never assigned to make a register look complete, and an owner is never inferred to fill a column.

## Downstream handoffs

`sli-specification-desk` needs the journey inventory with entry points and service paths, because an SLI is specified per journey and a journey with no path cannot be measured end to end. `slo-error-budget-desk` needs the tier, since the tier constrains what objective is defensible. `dependency-failure-analysis-desk` needs the service path to trace coupling along. `oncall-escalation-desk` needs the ownership and rotation attribution as the starting state for coverage analysis. `production-readiness-review-desk` needs the tier and support model as its scoring basis. Cross-suite: service decomposition and code ownership changes go to the SDLC suite.

## Quality bar

A journey map an engineer outside the owning team can follow from entry point to data store. A tiering rule specific enough that two reviewers assign the same tier to the same service. Ownership that resolves to a human who answers a page, with every failure to resolve stated plainly. An untiered and unowned list that is uncomfortable to read, because that discomfort is the finding the rest of the suite depends on.
