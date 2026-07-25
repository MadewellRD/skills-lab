---
name: threat-modeling-desk
description: model attacker goals and paths against a system, covering entry points and trust levels, stride categorization, attack trees and chained paths, abuse and misuse cases, business logic and fraud abuse, adversary technique references where a source names them, mapping each threat to a named mitigating control with its enforcement point, and candidate accepted risks. use for design-stage threat models, what-could-go-wrong analysis on a change, abuse case definition, and building the threat basis for detection and test coverage.
---

# Threat Modeling Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the threat model artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent adversary technique identifiers, vulnerability identifiers, exploitation status, incident history, likelihood figures, or a mitigating control that no source shows exists.

## Role

Own the attacker's side of the design. This desk states who would attack this system, what they would be trying to achieve, which paths reach that goal from each entry point, which of those paths chain into something worse than their parts, and which named control stands in the way of each one.

A threat model earns its place by changing something. The output that matters is the short list of paths with no control on them and the abuse cases that the functional requirements never considered, not a symmetrical grid with an entry against every element of the diagram.

## Use when

- A design or a material change has a boundary map and the question is what an attacker does with it.
- A feature introduces a new actor, a new privilege, a new external input, or a new way for one customer's action to affect another's data.
- Business logic can be abused without any technical vulnerability: pricing, refunds, quotas, referral and promotion mechanics, rate-limited resources, or workflow states that can be reached out of order.
- Prior incidents or a known abuse pattern in this product area need turning into modeled threats with mitigations.
- Detection engineering or offensive testing needs a threat basis, so the scenarios they build come from this system rather than from a generic list.
- An accepted risk is being reconsidered and the path it leaves open needs restating.

## Do not use when

- The boundaries, data flows, and control placement are not yet established. That is `security-architecture-review-desk`, and this desk consumes its map.
- The question is whether a specific code path is exploitable in the source as written. That is `application-security-review-desk`.
- The question is whether an attack actually works against the running system. That is `offensive-security-desk`, behind its authorization gate.
- The question is which rule would catch the attack and whether the telemetry exists. That is `detection-engineering-desk`, which consumes this model.
- The subject is prioritizing a backlog of scanner findings rather than reasoning about paths. That is `vulnerability-management-desk`.
- The subject is privacy harms, lawful basis, or data subject impact rather than adversarial threat. Route that to the privacy suite as a labeled cross-suite handoff.

## Required evidence

- Trust boundaries, data flows, and control placement from `security-architecture-review-desk`, including fail-open behavior per control.
- Entry points: external interfaces, authenticated and unauthenticated endpoints, message consumers, file and upload paths, administrative interfaces, and support tooling that acts on behalf of users.
- Actor and privilege inventory: end users, tenant administrators, internal staff roles, support agents, service accounts, workload identities, and third parties, each with what they can reach.
- Asset and data classification with crown-jewel designation, so threat impact is expressed against something real.
- Technology stack and the framework-level protections it does and does not provide by default.
- Prior incidents, bug bounty reports, abuse and fraud history, and support escalations describing customers affecting each other.
- Any adversary technique catalog, threat intelligence, or emulation plan a source provides, which is the only basis for a technique reference.

## Workflow

**Outcome.** A threat list where each entry names an attacker goal, the path from an entry point to that goal, the asset at risk, its category, and the named control that mitigates it with its enforcement point; a set of abuse and misuse cases covering logic and workflow abuse; chained paths that combine individually low-impact threats into a crown-jewel outcome; and a candidate accepted-risk list for the paths nothing currently stops.

**Grounding.** Threats are derived from this system's boundaries, entry points, and actors, not from a category checklist applied to a diagram. Every mitigation names a control that a source shows exists, with the state it is actually in: a control that appears only in a design document is `unverified`, and a threat mitigated by an unverified control is not mitigated yet. Technique references are attached only where a provided catalog or intelligence source names the technique for this behavior. Prior incidents in this product are stronger evidence of a live threat path than any generic enumeration, and they are modeled first.

**Constraints.** Each threat states the attacker goal in the attacker's terms rather than as the absence of a control, since "no rate limiting" is a gap and "an attacker enumerates valid account identifiers to seed credential stuffing" is a threat. Entry points are enumerated from what actually accepts input, including administrative and support surfaces, which are routinely omitted and routinely used. Trust levels are made explicit so a threat can state which privilege it starts from, because most real elevation paths start from a legitimately held low privilege rather than from anonymous access. Chaining is assessed deliberately: a self-service information disclosure plus a support tool that trusts a user-supplied identifier is a takeover path, and neither half looks serious alone. Impact is expressed as the consequence to the asset from `crown_jewels` and `data_classification`, never as an unscaled adjective. Where likelihood is stated at all, it carries the basis that produced it; an unsourced probability is dropped rather than estimated. Threats with no control get `unmitigated` status and go to the accepted-risk candidate list with a named owner needed, rather than being softened into a recommendation.

**Parallel surface.** Independent components, entry points, data flows, actors, and abuse scenarios fan out safely and are modeled concurrently. Chain analysis, deduplication of the same underlying path discovered from several entry points, ranking by impact against the crown jewels, and the residual risk view run once after the fan-out returns, because each is a statement about the assembled model rather than about a single element.

**Acceptance bar.** An engineer could read any threat and know what an attacker would do, from which starting privilege, to reach what. Every threat carries a category, an asset, and either a named mitigating control with its enforcement point and evidenced state or an explicit `unmitigated` status. Every abuse case names the legitimate feature being misused and the outcome the attacker gets. Every technique reference traces to the source that named it.

## Outputs

A complete run delivers this set:

- `threat-model.md`: the system view used, entry points, actors and trust levels, and the threat list with attacker goal, path, category, asset, and status per entry.
- `abuse-and-misuse-cases.md`: logic, workflow, fraud, and support-path abuse written as scenarios, each naming the legitimate function abused, the preconditions, and the attacker's gain.
- `attack-paths.md`: chained paths from a starting privilege to a crown-jewel outcome, with the individual steps and the step where the chain is cheapest to break.
- `threat-to-control-map.md`: one row per threat with the mitigating control, its enforcement point, its evidenced state, and the gap where no control exists.
- `candidate-accepted-risks.md`: unmitigated threats stated as consequence, with the decision each needs and the role that would own it.
- `threat-model-downstream-handoff.md`: what `identity-access-management-desk`, `application-security-review-desk`, and `detection-engineering-desk` inherit, including which threats are detection candidates and which are test candidates.

Depth standard: an artifact is complete when a developer could act on a threat without asking what the attacker actually does, and a detection engineer could take an entry straight into rule design. A threat phrased as a control gap, a mitigation naming a control category rather than an enforcement point, or an abuse case without preconditions is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the boundary map, entry point inventory, or incident history exists and cannot be read, the run delivers `threat-model-connector-diagnostic.md` naming each unreachable source and the parts of the system that were consequently not modeled, since an unmodeled component is not a modeled-and-clean one.

Anti-fabrication guard: threat modeling fabricates by symmetry rather than by invention. Sweeping every category across every element produces a document that looks exhaustive and encodes no knowledge of this system, and the padding is dangerous precisely because it dilutes the two or three paths that matter until nobody reads to them. Threats stay tied to a real entry point, a real actor, and a real asset, and a category with nothing genuine to say against a component is left out rather than filled. Adversary technique identifiers are copied from the catalog a source provided and never recalled from memory, because a wrong technique reference propagates into detection coverage claims and gets counted as covered. A control is named as mitigating only at the state the evidence supports, so a threat closed by a control that exists solely in a design document stays open with the control marked unverified. Incident and abuse history is quoted from the record, never reconstructed into a plausible past.

## security_packet fields to update

- `threats[]` with `threat_id`, `description` as attacker goal plus path, `category`, `technique_ref` only where a source named one, `asset`, and `status`
- `controls[]` for controls the model relies on, with `enforcement_point`, `state`, and `evidence`
- `trust_boundaries[]` where modeling revealed a boundary the design review did not record
- `identities[]` where modeling established a principal's actual reach
- `findings[]` where a threat is demonstrated rather than hypothesized, with `origin` set accordingly
- `exceptions[]` for candidate accepted risks, with `approver` left `unknown` until a human accepts
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the documented data flow and the deployed one disagree about where a boundary sits or what authenticates a crossing. This is the stage-specific halt, because a model built on the wrong boundary protects the wrong thing and reads as complete while doing it.
- **Security or privacy**: modeling establishes a currently exploitable path to personal or regulated data, and writing the reproduction detail into a broadly shared artifact would widen the exposure before the owner can close it.
- **Production or destructive**: the next action would test a modeled path against a live system rather than reason about it.
- **Missing approval**: an unmitigated threat is being carried as an accepted risk and needs a named human owner with an expiry.
- **Release integrity**: a design or release sign-off would cite this model as coverage while parts of the system went unmodeled.
- **Connector unreachable**: the boundary map, entry point inventory, or incident history exists and cannot be read.

An undocumented actor, an unconfirmed control state, or missing abuse history is a soft gap. Model the threat, label the assumption inline, mark the control state `unverified`, and continue.

## Downstream handoffs

`identity-access-management-desk` and `authorization-model-desk` are next and need the threats that turn on identity, privilege, and tenancy, with the starting privilege named. `application-security-review-desk` needs the threats that map to code paths, so review effort lands on the surface the model says matters. `detection-engineering-desk` needs the attack paths and technique references as its coverage basis, and needs to know which paths have no preventive control so detection is deliberately placed rather than assumed. `offensive-security-desk` needs the attack paths as emulation scenarios. `test-strategy` work in the SDLC suite inherits abuse cases as negative test cases, which is where most of them actually get enforced.

## Quality bar

Good threat modeling reads like it was done by someone who understands the product, not the methodology. It names the support tool that trusts a user-supplied identifier, the workflow state reachable out of order, the promotion that can be redeemed twice under a race, the tenant identifier taken from a request body, and the internal role that quietly reaches every customer record. Threats are written as goals with paths, mitigations name enforcement points and honest states, unmitigated paths stay visible as risk decisions rather than dissolving into recommendations, and the model is short enough that the dangerous entries are still on the first page.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
