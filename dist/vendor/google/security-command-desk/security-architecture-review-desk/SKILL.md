---
name: security-architecture-review-desk
description: review a system or change design for security control placement, covering trust boundary mapping, data flow analysis, conformance to the reference architecture, deviations and compensating controls, fail-open and fail-closed behavior, blast radius, conditions of approval, and residual design risk with the accepting party named. use for design reviews, architecture review board submissions, new service or major change assessment, segmentation and boundary decisions, and security sign-off before build starts.
---

# Security Architecture Review Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the design review artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent standard clauses, reference architecture requirements, control names, compensating controls, approval decisions, accepting parties, or expiry dates. An accepting party who has not accepted is `unknown`, and writing a plausible name there manufactures a governance record.

## Role

Own where the controls go and what happens where they are absent. This desk maps the trust boundaries a design actually creates, checks control placement against the reference architecture and the standards a source names, documents every deviation with a compensating control and a blast radius, sets the conditions a design must satisfy to proceed, and states the residual risk together with the named party accepting it.

Design review is the cheapest stage in this suite and the only one that can still move a boundary. Once a system is built, a misplaced trust boundary becomes a permanent finding that every later stage rediscovers and no remediation queue ever clears.

## Use when

- A new service, integration, data flow, or platform component is being designed and the control placement is not yet fixed.
- An existing system is undergoing a change that moves a boundary: a new tenant model, a new external consumer, a data store relocation, an authentication change, or a move between environments.
- A design is going to an architecture review board or a security design gate and needs its deviations, compensating controls, and residual risk written down.
- A design claims conformance to a reference architecture or paved road and that claim needs checking clause by clause.
- Regulated or classified data is about to cross a boundary it has not crossed before, including into an analytics copy, a vendor integration, or a lower environment.
- A prior design decision is being reopened because the residual risk it accepted has changed.

## Do not use when

- The estate, its exposure, or its data classification is not yet known. That is `attack-surface-inventory-desk`, and this desk consumes its output.
- The question is which attacker does what, through which path, with what goal. That is `threat-modeling-desk`, which runs on the boundary map this desk produces.
- The subject is authentication, federation, session policy, or privileged access design in detail. That is `identity-access-management-desk`.
- The subject is the authorization model, tenant isolation rules, or object-level access enforcement. That is `authorization-model-desk`.
- The subject is deployed state rather than intended design: what is actually configured in an account or cluster right now. That is `cloud-security-posture-desk` or `network-security-desk`.
- The subject is code-level implementation of a control already agreed in design. That is `application-security-review-desk`.

## Required evidence

- The design under review: architecture and solution design documents, decision records, sequence and data flow descriptions, and the interfaces the system exposes and consumes.
- Deployment topology: environments, network zones, accounts or projects, tenancy model, and where each component actually runs.
- The applicable reference architecture, paved-road pattern, or internal security standard, with the clauses that apply to this change identified.
- Asset inventory, data classification, and crown-jewel designation carried in from `attack-surface-inventory-desk`.
- Regulatory and contractual obligations that bind the design, named by a source rather than inferred from the industry.
- Existing exceptions and accepted risks that this design inherits or extends.
- The identity, key management, logging, and secrets platforms available to the design, so a control can be placed on something that exists.

## Workflow

**Outcome.** A trust boundary map for the design as drawn, a control placement review naming the enforcement point for every control the design relies on, a deviation register with a compensating control and blast radius per deviation, a set of conditions of approval that are concrete enough to check at build time, and a residual risk statement with the accepting party named or recorded as unknown.

**Grounding.** Design documents are authoritative for intent and never for deployed state, per the source hierarchy. Where the design describes an existing component, the running configuration outranks the description, and a disagreement between the two is preserved rather than resolved toward the design. Standards conformance is assessed clause by clause against the standard a source provided; a requirement nobody wrote down is a recommendation from this desk, labeled as such, and not a deviation.

**Constraints.** Every trust boundary names what is on each side, what crosses it, how the crossing is authenticated, and what the receiving side assumes about the sender. Control placement names the enforcement point rather than the layer: a control described as "the gateway validates the token" is placed only if the gateway is the sole path in, and where a second path exists, that is the finding. Fail behavior is stated for every control that can be unavailable, since a control that fails open is a control that is absent exactly when it is needed. Blast radius is written per boundary as the concrete reach of a compromise on the untrusted side. Compensating controls are only compensating where they reduce the same risk at a different point; a monitoring control offered against a missing preventive control is recorded as detection, not as compensation. Residual risk is expressed as the consequence that remains after the agreed controls, and the accepting party is a named human role with authority over that consequence.

**Ordered gate for a deviation from a mandated control.** A deviation follows this sequence, and the order is externally mandated because an approver cannot accept a risk they have not been shown, retroactive approval is a record rather than a decision, and code built on an unapproved deviation is expensive to unwind:

1. Identify the deviation against the specific standard or reference architecture clause it departs from.
2. State the residual risk and blast radius that the departure creates, in consequence terms.
3. Propose the compensating control with its enforcement point and its own fail behavior.
4. Obtain acceptance from the named party with authority over that consequence, with an expiry date.
5. Record the exception in `security_packet.exceptions` before implementation proceeds on the deviated path.

**Parallel surface.** Independent components, interfaces, data flows, boundaries, and standard clauses fan out safely and are assessed concurrently. The composite judgments run once after the fan-out returns: whether the design as a whole holds together, whether deviations that are individually acceptable combine into an unacceptable path, the overall residual risk statement, and the conditions of approval. Defense in depth is a property of the assembled design and cannot be evaluated component by component.

**Acceptance bar.** An engineer could build from the review without asking where a control goes, and a reviewer could check conformance at build time against the conditions of approval as written. Every boundary names its authentication and its fail behavior, every deviation carries a compensating control and a blast radius, and every residual risk names an accepting party or states plainly that none has accepted it.

## Outputs

A complete run delivers this set:

- `trust-boundary-map.md`: each boundary with the zones on either side, the protocols and data crossing it, how the crossing is authenticated, and what the trusting side assumes.
- `control-placement-review.md`: the controls the design depends on, each with its enforcement point, its fail-open or fail-closed behavior, and whether the placement is single-path or bypassable.
- `deviation-register.md`: departures from the reference architecture or a named standard clause, each with the residual risk, the compensating control and its enforcement point, and the approval state.
- `conditions-of-approval.md`: the concrete conditions the build must satisfy, written so each is checkable rather than aspirational, with the stage that will check it.
- `residual-design-risk.md`: what remains after the agreed controls, expressed as consequence, with the accepting party named or recorded as unknown and unaccepted.
- `architecture-review-downstream-handoff.md`: what `threat-modeling-desk` inherits, including boundaries whose authentication is undecided.

Depth standard: an artifact is complete when the design can be built and later audited from it without a follow-up round trip. A boundary with no stated authentication, a control with no enforcement point, or a condition of approval that cannot be checked is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the design documents, the reference architecture, or the deployment topology exists and cannot be read, the run delivers `architecture-connector-diagnostic.md` naming each unreachable source and the conformance claims that depend on it. Conformance is never asserted against a standard nobody read.

Anti-fabrication guard: the failure specific to this desk is the manufactured approval record. Design reviews are read later as governance evidence, so a deviation attributed to an accepting party who never saw it, an expiry date chosen to look reasonable, or a compensating control described as agreed when it was merely suggested creates an audit trail that is worse than an open gap, because the gap at least remains visible. Accepting parties come from an explicit acceptance a source records, and everything else is `unknown` with the deviation left in the unaccepted state. Standard clauses are quoted from the standard provided rather than recalled from the framework's general shape, since a conformance finding against a clause that does not exist discredits the ones that do. Where this desk raises a good practice that no provided standard requires, it is labeled as a recommendation from the review rather than promoted into a deviation.

## security_packet fields to update

- `trust_boundaries[]` with `name`, `between`, `protocols`, and `authenticated_by`
- `controls[]` with `control_id`, `enforcement_point`, `state`, `evidence`, and `owner`, using `unverified` for any control that exists only in the design
- `exceptions[]` with `covers`, `compensating_control`, `approver`, and `expires`
- `approvals[]` for pending design acceptances, with `state`
- `crown_jewels[]` and `data_classification[]` where the design moves or copies classified data
- `source_facts[]` with `source` and `collected`, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: the design deviates from a mandated control and a human must own the exception before the build proceeds on it. This is the stage-specific halt; the consequence of skipping it is a control waiver that nobody granted and nobody can revoke.
- **Security or privacy**: the review establishes that the design as drawn would place regulated or personal data across a boundary without a control, and continuing would ratify that placement rather than stop it.
- **Production or destructive**: the next action would change a live boundary, routing path, or trust relationship rather than document one.
- **Source conflict**: the design document and the deployed state genuinely disagree about where a component runs or which boundary it sits behind, and a review built on the wrong boundary places controls in the wrong place.
- **Release integrity**: a design sign-off or conformance statement would be issued without the standard, the topology, or the classification evidence behind it.
- **Connector unreachable**: the design, the reference architecture, or the topology source exists and cannot be read.

An undocumented data flow, a missing owner, or an undecided technology choice is a soft gap. State the assumption inline, name what it changes, and continue; a review that stops at the first unspecified component reviews nothing.

## Downstream handoffs

`threat-modeling-desk` is next and needs the boundary map, the data flows, and the control placement with fail behavior, because a threat model built on a boundary that does not exist protects the wrong asset. `identity-access-management-desk` and `authorization-model-desk` inherit the authentication expectations recorded at each boundary. `cryptography-key-management-desk` inherits the key custody boundary and the classification of the data crossing it. `secure-sdlc-controls-desk` inherits the conditions of approval as build-time gates. `compliance-evidence-desk` inherits the deviation register and exceptions as control evidence, which is why the accepting party field cannot be filled speculatively.

## Quality bar

Good architecture review is specific about the paths the design leaves open. It names the second route into the component the gateway was supposed to protect, the control that fails open under load, the boundary that exists in the diagram and not in the deployment, and the analytics copy that carries regulated data past every control placed on the primary store. Deviations are written so that the person accepting the risk can understand it without reading the design, conditions of approval are checkable by a later stage rather than by good intentions, and residual risk stays attached to a named human. The review is worth the stage only if a boundary could still move as a result of it.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
