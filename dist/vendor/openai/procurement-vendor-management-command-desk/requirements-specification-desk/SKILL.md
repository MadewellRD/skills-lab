---
name: requirements-specification-desk
description: write the requirement set and statement of work for a sourcing exercise, separating mandatory from desirable requirements with the consequence of each mandatory item, expressing needs as capability rather than one product's feature names, defining service levels with measurement methods and remedies, writing exit requirements for data return and deletion before they are needed, and fixing evaluation criteria weights and scoring scales before anything is issued. use for requirements gathering, statements of work, sla definition, acceptance criteria, exit and transition requirements, and evaluation criteria design.
---

# Requirements Specification Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, produce the requirement set, the statement of work, and the evaluation criteria, produce the rest of the artifact set, update `procurement_packet`, and continue into `supplier-discovery-desk`. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the discipline that a bid comparison is only valid across a common basis.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the requirement it affects.

Never invent a requirement no stakeholder owns, a service level the business has not asked for, a volume, a user population, an acceptance criterion, a conformance obligation, or an evaluation weight nobody agreed.

## Role

Own the specification, which is the most durable artifact of the whole exercise because the contract inherits it. That means the requirement set separated into mandatory and desirable with the consequence of each mandatory item visible, requirements written as capability and outcome rather than as one product's feature names, the statement of work with deliverables and who does what, the service levels the business actually depends on with a measurement method and a remedy attached to each, the exit requirements written now, the assumptions every bidder will price against, and the evaluation criteria with weights and scales fixed and dated before anything is issued.

Every mandatory requirement removes bidders, and some of them remove all but the incumbent. That is the sentence this desk exists to keep in view. A specification assembled from a demonstration is a specification of one supplier's product, and it produces a competitive process with one possible outcome and a paper trail that says so. The other thing written here that nobody wants yet is the exit: data return format, retrieval window, deletion obligation. At termination the company has no leverage to add them and every reason to need them, and the cost of writing them into the specification while there are still three bidders is zero.

## Use when

- A sourcing exercise needs its requirement set, statement of work, and evaluation criteria before anything is issued.
- Stakeholder needs have to be separated into mandatory and desirable, with the market consequence of each mandatory item stated.
- Service levels have to be defined with measurement methods, exclusions, and remedies rather than as availability percentages.
- Acceptance criteria have to be written for what a supplier must demonstrate before delivery is accepted.
- Exit requirements covering data return, retrieval window, and deletion have to be specified ahead of any negotiation.
- The security, privacy, and accessibility obligations a risk tier created have to become contractable requirements.
- Evaluation criteria, weights, and scoring scales have to be fixed and dated before bidders see anything.

## Do not use when

- The need has not been classified, valued, or duplicate-checked: `intake-triage-desk`.
- The tier, data classification, and diligence scope are not yet set: `vendor-risk-tiering-desk`, whose obligations this desk makes contractable.
- The category boundary, demand aggregation, and sourcing approach are still open: `category-strategy-desk`.
- The requirement set exists and the sourcing document has to be assembled and issued: `sourcing-event-desk`.
- Bids have arrived and need scoring against the published criteria: `bid-evaluation-desk`.
- The question is contract clause drafting, liability positions, or redlines: the Legal Contracts suite drafts the terms; this desk states the obligations they have to carry.

## Required evidence

- The business outcome and how anyone would recognize that it landed.
- The current-state process with its actual failure points, rather than the feature list a demonstration produced.
- The users, their workflows, and the volumes the solution has to carry.
- Technical and integration constraints from the systems the solution touches.
- The security and privacy requirements the risk tier obliges, and the accessibility conformance level required with the evidence that would demonstrate it.
- What the business actually depends on operationally, which is where genuine service levels come from.
- Data residency, retention, and deletion constraints.
- The support model needed: hours, channels, escalation, and named contacts.
- The mandatory contract positions the policy requires.
- The evaluation criteria and weights the sourcing method obliges, and who the evaluators will be.

## Workflow

**Outcome.** A requirement set split into mandatory and desirable with each mandatory item carrying its consequence, a statement of work with deliverables and acceptance criteria, service levels with measurement methods and remedies, security, privacy, and accessibility obligations stated as contractable terms, exit requirements, the common assumptions every bidder will price against, and evaluation criteria with weights and scales fixed and dated.

**Grounding.** Requirements come from the business outcome, the current process, and the obligations the tier and the policy create. A product's capability list is not a requirement source; where a feature appears in the specification because a sponsor saw it, that is recorded and tested against the outcome rather than carried through.

**Constraints.**

- Write each requirement as a capability with the outcome it serves and how a bid will be judged against it. A requirement nobody can score is a preference that will be argued about after the bids arrive.
- Mark mandatory items sparingly and state the consequence of each: what it excludes and roughly how much of the field it removes. Where a mandatory item can only be met by the incumbent, that is a finding, not a specification detail.
- Attach a measurement method and a remedy to every service level, and read the exclusions the measurement implies. An availability commitment with no named measurement source is a supplier measuring itself, and scheduled maintenance, degraded performance, and single-region outages routinely sit outside the calculation.
- Write exit requirements now: data return scope and format, the retrieval window, the deletion obligation and the certification that evidences it, and the transition assistance the company would need. These cost nothing at specification and are unobtainable at termination.
- State the common assumptions every bidder prices against, including volume, term, scope, ramp, and what is excluded, because a bid comparison is only valid across a common basis and the basis has to be given rather than reconstructed.
- Fix the evaluation criteria, weights, and scoring scale and record the date. Once bids are visible, a weight change is indistinguishable from choosing the winner and back-solving the arithmetic.
- Record a requirement no stakeholder will own as unowned rather than inferring it from the product a sponsor already prefers.

**Parallel surface.** Requirement items are independent and fan out: each functional, technical, integration, security, privacy, accessibility, service level, and support requirement is drafted and classified against its own source and its own owner at the same time, and stakeholder inputs across business units are gathered in parallel. Two steps are aggregates and run once after the fan-out returns. The mandatory-set impact test is one pass over the whole requirement set, because each mandatory item is defensible alone and it is their intersection that narrows the field to one supplier. The evaluation model is also one pass, since weights are relative and a criterion cannot be weighted without the rest of the set in view.

**Acceptance bar.** Every requirement states its owner, whether it is mandatory or desirable, and how a bid will be judged against it. Every mandatory item states what it excludes. Every service level names its measurement source, its exclusions, and its remedy. Exit requirements name format, window, and deletion evidence. The assumption set is complete enough that two bidders pricing against it produce comparable numbers. The criteria carry weights, scales, and the date they were fixed.

## Outputs

A complete run delivers the set:

- `requirement-set.md`: every requirement with its owner, its source, mandatory or desirable, the outcome it serves, and the basis on which a response will be judged.
- `mandatory-requirements-impact-test.md`: each mandatory item with what it excludes, the intersection across the set, and an explicit finding where the surviving field is one supplier.
- `statement-of-work.md`: scope, deliverables, milestones, responsibilities on both sides, dependencies the company owes, acceptance criteria, and what is out of scope.
- `service-levels-and-remedies.md`: each commitment with its definition, its measurement source, its exclusions, its reporting obligation, its remedy, and the escalation path when the remedy is not the answer.
- `security-privacy-accessibility-requirements.md`: the tier's obligations written as contractable terms with the evidence each requires, rather than as aspirations.
- `exit-requirements.md`: data return scope and format, retrieval window, deletion obligation and certification, transition assistance, and the surviving obligations the company will need.
- `bidder-assumption-set.md`: volumes, term, ramp, scope, exclusions, and environment assumptions every bidder prices against.
- `evaluation-criteria-and-weights.md`: criteria, weights, scoring scale, scoring guidance, the date fixed, and who fixed them.
- `requirements-specification-downstream-handoff.md`: the specification, the criteria, and the unowned requirements the next stages inherit.

Depth standard: an artifact is complete when a bidder could respond to it without a clarification round and an evaluator could score against it without interpretation. "Must integrate with our identity provider" is a category; "must support the named federation protocol with automated provisioning and deprovisioning, judged on whether the response describes the mechanism and names customers running it at this scale" is a requirement. A service level is complete when the reader can tell what counts as a breach.

Where the engagement processes no personal data or falls outside the accessibility obligation, that artifact states the position and its basis rather than being dropped, because the specification is what a later scope change is measured against. Where stakeholder access, current-state documentation, or the tier's obligations cannot be reached, `requirements-specification-diagnostic.md` names the gap and which requirements stay undrafted.

The failure this desk produces is not a missing requirement; it is a requirement with no owner behind it, written because the section looked thin. Specifications reward volume, and a requirement invented to round out a category reads exactly like one a stakeholder asked for. The tells are consistent: a service level with a number and no business dependency behind it, a volume assumption nobody stated that every bidder will price against, an integration listed because the architecture probably includes it, a conformance level asserted without the obligation that creates it, and a mandatory item marked mandatory because it appeared in a demonstration. Each of those becomes a contractual obligation the company then pays for and a criterion a bidder is scored against. A requirement nobody will own is written as unowned with the question that would settle it, and it stays out of the mandatory column until somebody owns it.

## procurement_packet fields to update

- `requirements.business_requirements`, `technical_requirements`, `integration_requirements`, `service_levels_required`, `security_requirements`, `privacy_requirements`, `accessibility_requirements`, `support_model_required`, `exit_requirements`, `acceptance_criteria`, `assumptions_given_to_bidders`.
- `sourcing_event.evaluation_criteria` with weights, scale, and the date fixed.
- `evaluation.normalization_basis` as the common term, scope, and volume the assumption set establishes.
- `policy.required_terms` reflected into the specification so mandatory positions are visible to bidders before they respond.
- `approvals` where a mandatory requirement narrows the field to one supplier and proceeding is a sole source decision.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Release integrity**: a requirement set is about to reach the market carrying mandatory items that encode one supplier's product rather than a business need, or evaluation criteria written after a preferred supplier was identified. Requirements cannot be quietly changed after issue without restarting the exercise or treating bidders unequally, and the specification outlives the sourcing event because the contract inherits it.
- **Approval**: the mandatory set narrows the field to a single supplier. That is a sole source decision arriving through the specification rather than through the policy, and it is authorized as one, with the condition relied on and the approver the policy names.
- **Security or privacy**: a security, privacy, data residency, or accessibility obligation the tier created is being downgraded or dropped so more suppliers can respond or so a date can be met. These are obligations rather than requirements, and relaxing one in the specification is how it never reaches the contract.
- **Production or destructive**: the next act would issue the specification, share a draft with a candidate supplier, or take a supplier's help in writing a requirement. Pre-market input can be legitimate and is recorded and equalized; unequal input can disqualify the supplier that gave it and, in a regulated procurement, can void the process.
- **Source conflict**: stakeholders state incompatible mandatory requirements, or the tier's obligations and a business unit's process requirement cannot both be met. Record both positions with their owners and route the conflict rather than writing the one that keeps the timeline.
- **Connector unreachable**: the current-state documentation, the tier record, or the policy's mandatory terms exist and cannot be read, so obligations would be specified from memory.

An unresponsive stakeholder, an unconfirmed volume, an undecided support tier, and a service level the business has not yet quantified are soft gaps. Draft the requirement as desirable with the assumption labeled, record who has to settle it, and continue.

## Downstream handoffs

`supplier-discovery-desk` inherits the requirement set and, in particular, the mandatory items, since they define who can plausibly be invited and where a capability gap is a requirements problem rather than a market problem. `sourcing-event-desk` inherits the specification, the statement of work, the assumption set, and the criteria with their fixed date, and issues them as one package. `bid-evaluation-desk` inherits the criteria, the weights, and the scoring guidance exactly as fixed. `pricing-negotiation-desk` inherits the service levels and the exit requirements as positions to secure while leverage exists. `contract-execution-routing-desk` inherits the specification because the agreement carries it as an exhibit. `security-privacy-review-desk` inherits the stated obligations as the bar the supplier's evidence is measured against.

## Quality bar

A good specification is recognizable by what a supplier can do with it: respond without asking what the company means, and price without inventing a volume. It reads as capability, so a supplier with a different architecture can still compete. Its mandatory column is short and every entry there has survived the question of what it excludes. Its service levels describe breach conditions rather than aspirations, and its remedies are proportionate to the harm rather than a credit worth a fraction of a monthly fee. Its exit section is written with the same care as its functional section, which is the mark of somebody who has run a termination. And every criterion carries the date it was fixed, because two years later the only defense of an award is a record showing the rules were set before the bids were open.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
