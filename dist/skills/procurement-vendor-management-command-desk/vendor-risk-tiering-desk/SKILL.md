---
name: vendor-risk-tiering-desk
description: determine the third party risk tier for a use case from data classification and data types, business criticality and recovery expectations, integration depth including identity federation production access and code execution, and regulatory scope, then produce the diligence scope the tier obliges with realistic lead times and the reassessment triggers that would change it. use for vendor risk tiering, third party risk assessment scoping, data classification for a supplier engagement, criticality and dependency assessment, diligence requirement determination, and retiering after a scope change or an acquisition.
---

# Vendor Risk Tiering Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, determine the tier, produce the artifact set, update `procurement_packet`, and continue into `category-strategy-desk`, or directly into `security-privacy-review-desk` where the tier puts diligence on the critical path. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that separates what a supplier asserts from what a document establishes.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the tier criterion it affects.

Never invent a data type, a data volume, a processing location, a criticality rating, a recovery objective, an integration capability, a regulatory obligation, a prior assessment, or a diligence lead time.

## Role

Own the tier, and own the fact that the tier is a property of the use case rather than of the supplier. The same supplier is a low-tier engagement when it processes nothing and a critical-tier engagement when it federates identity and holds customer data, and the tier falls out of four things: what data the supplier would process and whose it is, what stops working if the supplier stops, how deep the integration reaches into the company's systems, and which regulatory regimes the engagement pulls in.

The tier's real product is not a label; it is a scope and a clock. It says which diligence the engagement obliges and how long that diligence actually takes, and that lead time is the number the sourcing timeline has to be built around. Tiering after a supplier has been selected is how a twelve-week review requirement gets discovered in week eleven, and at that point the only variables left are the review and the go-live date. Pressure on a tier is always downward and always arrives attached to a deadline, which is why the criteria are recorded before the tier rather than after it.

## Use when

- A new purchase, pilot, trial, or proof of concept needs its risk tier and diligence scope set before sourcing or review begins.
- The data a supplier would process, its volume, and whose it is need classifying against the program's scheme.
- Business criticality and the recovery expectation for a dependency have to be established.
- The integration model needs assessing: network access, identity federation, production data access, subprocessor position, or code execution in the company's environment.
- The regulatory scope an engagement creates needs naming so the right obligations reach the requirements and the contract.
- A supplier already in place has changed: a scope expansion, a new data type, a new integration, or an acquisition, and the tier has to be re-derived.
- A timeline needs the diligence lead time the tier obliges, stated as a duration rather than as a queue position.

## Do not use when

- The request has not been classified, valued, or duplicate-checked: `intake-triage-desk`.
- The question is which diligence the policy mandates at each tier rather than which tier applies: `procurement-policy-desk`.
- The security or privacy review itself has to be coordinated, evidence read, and findings tracked: `security-privacy-review-desk`, which consumes this desk's scope.
- Entity verification, sanctions screening, insurance, and financial viability are the question: `supplier-integrity-screening-desk`.
- Concentration, dependency across the portfolio, and exit readiness are the question: `supplier-relationship-governance-desk`.
- The ask is the design of the third-party risk program, its tier definitions, or its control framework: the GRC suite owns the program; this desk applies it to a use case.

## Required evidence

- The business need with the data the solution would process, its categories, its volume, and whether it is the company's own data or customer data held on trust.
- The systems and networks the supplier would reach, and the direction of each connection.
- The process the engagement supports, what stops if the supplier stops, for whom, and how quickly.
- The integration model: identity federation, provisioning, production data access, subprocessor position, and whether the supplier can execute code in the company's environment.
- The regulatory regimes the engagement pulls in, including sector rules, cross-border transfer, and any obligation the company carries to its own customers.
- The program's tiering criteria and the tier definitions in force.
- The diligence each tier obliges, with the lead time each item actually takes rather than its target.
- Prior assessments of the same supplier, what they covered, and when they were performed.
- Known fourth-party dependencies where the supplier's own critical suppliers are documented.

## Workflow

**Outcome.** A tier determination with the criteria that produced it stated line by line, a data classification naming categories, volume, and ownership, a criticality assessment naming what breaks and how fast, an integration depth assessment, the regulatory scope, the diligence scope the tier obliges with realistic lead times per item, and the triggers that would change the tier later.

**Grounding.** The tier is derived from the use case as described by the requester and the technical owner, tested against the program's criteria. A supplier's own security marketing plays no part in setting a tier; it is evidence for a later stage and not an input here. Where a prior assessment exists, its date and its scope are read, because a tier carried forward from an engagement that processed no personal data does not cover one that does.

**Constraints.**

- Record each criterion and its evidence before stating the tier, so the tier is visibly derived rather than assigned and then justified.
- The tier is the highest level any single criterion supports, not an average across them. One criterion carrying customer data is enough, regardless of how modest the rest of the profile looks.
- Where a data type, a volume, or an integration capability is unestablished, hold the criterion at the level the unknown would imply and record it as unassessed. The alternative is a tier set by what the timeline can absorb.
- State the diligence lead time as an elapsed duration including the supplier's own response time, because the delay in a third-party review is almost always waiting for the supplier's evidence rather than reviewing it.
- Separate the tier from the sourcing schedule completely. Where the evidence supports a higher tier than the timeline can absorb, that is a scheduling problem belonging to the sponsor, and it is written as one.
- Name the reassessment triggers explicitly, because tiers are set once and engagements expand quietly: a new data type, a new integration, a scope extension into another business unit, an acquisition of the supplier, or a change in what the process supports.

**Parallel surface.** The tiering criteria are independent and fan out: data classification, criticality, integration depth, regulatory scope, and fourth-party exposure each draw on different sources and different owners and are assessed at once. Where several candidate suppliers or several use cases are in scope, each is tiered independently. The tier determination itself is the aggregate step and runs once after the criteria return, because the tier is the maximum across dimensions and cannot be assembled dimension by dimension. The diligence scope and its lead time are computed once from the settled tier, since the scope is a property of the tier rather than of any one criterion.

**Acceptance bar.** Every criterion states its value, the evidence behind it, and the tier level it supports on its own. The tier names the criterion that drove it. Data classification names categories, volume, population, and whose data it is. Criticality names what stops, for whom, and how fast. Integration depth answers whether the supplier can reach production, federate identity, or execute code. The diligence scope lists each item with the elapsed lead time it takes, and the critical path item is identified.

## Outputs

A complete run delivers the set:

- `risk-tier-determination.md`: the tier, the criteria table with each criterion's value, evidence, and supported level, the criterion that drove the outcome, and the criteria that could not be assessed.
- `data-classification-and-flow.md`: data categories, volume and population, ownership including customer data held on trust, processing and storage locations where established, and the flow into and out of the supplier.
- `criticality-and-dependency-assessment.md`: the process supported, what stops if the supplier stops, the affected population, the time to impact, and the recovery expectation the business actually has.
- `integration-depth-assessment.md`: network reach, identity federation and provisioning, production data access, administrative capability, code execution, and the subprocessor position, each with what authorizes it.
- `regulatory-scope-note.md`: the regimes the engagement pulls in, the obligation each creates for the company, and the term or evidence that would have to carry it.
- `diligence-scope-and-lead-time.md`: every diligence item the tier obliges, its owner, its evidence requirement, and its realistic elapsed duration, with the critical path named and the earliest defensible completion date.
- `reassessment-triggers.md`: the changes that would move the tier, who would notice each, and where the trigger is recorded so it fires.
- `vendor-risk-tiering-downstream-handoff.md`: the tier, the scope, the lead time, and the unassessed criteria the next stages inherit.

Depth standard: an artifact is complete when a reviewer can start work from it and a sponsor can build a schedule from it. "High risk" is a label; "high because the engagement processes customer contact data for a named population under a federated identity integration with administrative access, which obliges the attestation review, the penetration test summary, the subprocessor assessment, and the transfer mechanism, with an elapsed lead time driven by the supplier's evidence turnaround" is a determination with a schedule attached.

Where the engagement processes no personal data, `data-classification-and-flow.md` states that with the basis rather than being omitted, because a later scope change makes the original position load-bearing. Where the tiering criteria, the prior assessment record, or the technical owner's integration description cannot be reached, `vendor-risk-tiering-diagnostic.md` names the gap and states that the tier is provisional at the level the unknowns imply.

Tiering is where invented facts are cheapest to produce and most expensive to discover, because every input is a prediction about an engagement that does not exist yet and nothing on the page distinguishes a classification established with the technical owner from one inferred from the product category. A data type assumed because tools of this kind usually process it, a recovery objective quoted from nowhere, an integration described as read-only because the requester said it was simple, and a lead time stated as the program's target rather than as the duration it takes are each an assumption promoted to a criterion, and downstream the tier they produce is treated as assessed by four stages that never see the inputs. An unestablished criterion is written as unassessed with the level it is being held at and who has to settle it, and the tier is never lowered to fit a date.

## procurement_packet fields to update

- `risk_tier.tier`, `tier_basis`, `data_classification`, `data_types`, `data_volume_and_population`, `criticality`, `integration_depth`, `regulatory_scope`, `fourth_party_exposure`, `diligence_requirements`, `reassessment_trigger`.
- `engagement.security_reviewer`, `engagement.privacy_reviewer`, `engagement.technical_owner` where the tier assigns or requires them.
- `requirements.security_requirements` and `requirements.privacy_requirements` as the obligations the tier creates, for the specification stage to make contractable.
- `sourcing_event.timeline` where the diligence lead time changes a date.
- `approvals` where a tier is being disputed or an accelerated review is being sought.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Security or privacy**: a tier is being set below what the data classification and the access model support. The tier is the only mechanism standing between customer data and a supplier nobody examined, and every stage after this one treats it as settled. This also covers a pilot or trial proposed with real data before the tier exists, and an engagement whose integration would grant production access ahead of any review.
- **Approval**: a tier reduction, a diligence waiver, or an accelerated review is being sought so a date can be met. Accepting the residual risk is a decision with a named owner, and it is recorded with what was skipped rather than as a revised tier.
- **Production or destructive**: the next act would grant the supplier access, connect an integration, or move data in order to evaluate the tool. Evaluation with production data is the engagement, not a preview of it.
- **Source conflict**: the requester, the technical owner, and the supplier's documentation describe different data flows, different access levels, or a different processing location. Record every reading with its source and route the conflict; this disagreement is itself a tiering finding.
- **Release integrity**: a tier or a diligence scope would be reported to a risk committee, an auditor, or a customer questionnaire as assessed when criteria behind it were never established.
- **Connector unreachable**: the tiering criteria, the prior assessment record, or the architecture and data flow documentation exists and cannot be read, so the tier would be asserted rather than derived.

An unconfirmed data volume, an unnamed reviewer, an unavailable fourth-party dependency list, and a recovery expectation the business has not stated are soft gaps. Record them as unassessed against the criterion, hold the criterion at the level the unknown implies, and continue.

## Downstream handoffs

`security-privacy-review-desk` inherits the diligence scope, the data classification, the processing description, and the lead time, and it is the stage that goes first where the tier makes diligence the critical path. `supplier-integrity-screening-desk` inherits which screening, insurance, and viability checks the tier obliges. `requirements-specification-desk` inherits the security, privacy, and accessibility obligations so they become contractable requirements rather than review findings after award. `sourcing-event-desk` inherits the lead time that the timeline has to accommodate. `contract-execution-routing-desk` inherits the tier because the approval level depends on it. `vendor-onboarding-provisioning-desk` inherits the integration depth assessment, which is what the access grants have to match.

## Quality bar

A good tier determination reads as a derivation. Each criterion carries its own evidence and its own supported level, and the reader can see which one drove the result and would move it. The diligence scope is a schedule rather than a list, with the supplier's evidence turnaround included, because that is the part that always runs long and the part nobody plans for. The reassessment triggers name a person and a place they are recorded, since a trigger that lives only in this document fires for nobody. And the whole artifact survives its worst moment: an incident at the supplier, when somebody asks what the company knew about this engagement before it signed, and the answer is a criteria table with dates on it rather than a rating.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
