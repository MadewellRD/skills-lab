---
name: supplier-relationship-governance-desk
description: manage the supplier portfolio view by segmenting suppliers on value and criticality, computing concentration across legal entities business units and categories, assessing dependency and substitutability with realistic switching cost and lead time, distinguishing a single source choice from a sole source exposure, testing exit readiness against what the contract actually enables, and setting the governance cadence a tier and value justify. use for supplier segmentation, concentration and dependency risk, critical supplier registers, business continuity and exit readiness, single versus sole source analysis, quarterly business review governance, and supplier relationship strategy.
---

# Supplier Relationship Governance Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, build the portfolio view, produce the artifact set, update `procurement_packet`, and continue into `spend-analysis-desk`. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the discipline that separates a continuity claim a supplier makes from a continuity capability the contract makes enforceable.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the supplier or dependency it affects.

Never invent a criticality rating, a concentration figure, a dependency, an alternative supplier, a switching cost, a switching lead time, a recovery objective, a continuity test, an exit test, a supplier's financial trajectory, an ownership change, a product end-of-life date, or a governance commitment nobody made.

## Role

Own the view that no individual purchase produces. Every supplier in the portfolio was bought for a defensible reason by someone acting reasonably, and the exposures that matter are visible only across the whole population: the supplier that carries eight percent of spend and one hundred percent of a capability, the four business units that each depend on the same platform through different agreements and different resellers, the vendor whose contract permits termination for convenience and whose data format makes leaving take eleven months, and the critical dependency whose exit plan has never been tested by anyone.

Two distinctions carry this desk. Spend and importance diverge sharply, and the cheapest supplier in the portfolio is frequently the one that can stop the business, so segmentation runs on value and criticality together rather than on value alone. And single source is not sole source: single source means the company chose one supplier where alternatives exist, which is a decision that can be revisited; sole source means no alternative exists, which is an exposure to be managed rather than corrected. Calling the second one the first is how a critical dependency stays unaddressed for years, because the register says a choice was made when in fact no choice existed.

## Use when

- The supplier portfolio needs segmenting, or an existing segmentation needs re-deriving against current value and criticality.
- Concentration has to be computed across legal entities, business units, categories, and brands, where the same supplier appears under several names.
- A dependency assessment is needed: what the company cannot do without, for how long, and who feels it first.
- Substitutability, switching cost, and realistic switching lead time have to be established for a supplier the company may need to leave.
- A single source position needs distinguishing from a sole source exposure, with different responses attached to each.
- Exit readiness has to be assessed, tested, or reported, including for a critical supplier register or a regulator-facing outsourcing record.
- The governance cadence for a supplier needs setting or fixing, including who attends, what the agenda is, and where decisions are recorded.
- The supplier's own direction has changed: an acquisition, a change of control, a financial deterioration, or an end-of-life notice for the product the company depends on.

## Do not use when

- The question is one supplier's performance in a period, its service levels, or its credits: `supplier-performance-sla-desk`.
- The question is the spend baseline, category fragmentation, or savings realization from the ledger: `spend-analysis-desk`, which this desk consumes and does not reproduce.
- The risk tier for a specific use case is being set: `vendor-risk-tiering-desk`.
- The entity, ownership, sanctions, or financial viability checks themselves are the work: `supplier-integrity-screening-desk`.
- The exit is actually happening and the notice, data return, and deprovisioning sequence is the work: `vendor-offboarding-desk`, which executes what this desk assessed.
- The third-party risk program, its control framework, or the regulator-facing submission is the subject: the GRC suite owns the program; this desk supplies the portfolio evidence.

## Required evidence

- The supplier portfolio with annual value, contract value, risk tier, and category for each, mapped to legal entities rather than brands.
- Performance history and scorecard trends, including incidents and unresolved commitments.
- Spend by supplier across business units and legal entities, so concentration is computed on the consolidated view rather than per unit.
- The capability map: what each supplier actually delivers and where two suppliers deliver the same thing.
- Contract terms that govern exit: termination rights and their notice, transition assistance and its duration and fee, data return format and retrieval window, deletion obligations, change of control, and any step-in or escrow arrangement.
- Continuity evidence: the supplier's recovery commitments, its own critical dependencies where known, and whether any of it is contractually enforceable or merely stated.
- Switching evidence: the realistic alternatives, integration depth, data volume and format, retraining scope, and what a move has actually taken elsewhere.
- The supplier's own trajectory: ownership changes, funding position, product roadmap, end-of-life notices, and support policy changes.
- The governance in place: cadence, attendees, agenda, decisions taken, and whether actions were closed.

## Workflow

**Outcome.** A portfolio segmentation with the basis stated, a concentration view computed across entities and business units, a dependency assessment, a substitutability position with switching cost and lead time, an explicit single source against sole source determination per critical supplier, an exit readiness assessment naming what is missing, a governance cadence matched to tier and value, and a relationship risk register covering the supplier's own direction.

**Grounding.** Concentration is computed from consolidated spend and consolidated capability, not from the contract list, because the same supplier arrives through resellers, marketplaces, subsidiaries, and inconsistent vendor master entries. Exit readiness is grounded in the executed contract terms and in what has actually been tested; a supplier's statement about its transition support is a claim, and a transition assistance clause with a duration and a fee is a capability.

**Constraints.**

- Segment on value and criticality together, and state the basis for each axis. A segmentation that ranks by spend puts the payroll platform below the office furniture.
- Compute concentration on the consolidated entity, then again by capability. A supplier can be modest in spend and total in capability, and that is the version that matters.
- State dependency in operational terms: what stops, for whom, how quickly, and what the manual fallback actually is if there is one.
- Distinguish single source from sole source explicitly for every critical supplier, and attach a different response to each. One gets a plan to create an alternative; the other gets a plan to survive the exposure.
- Express switching lead time as elapsed time including data migration, re-integration, retraining, and the parallel running period, rather than as the length of a project plan.
- Test exit readiness against the contract rather than against intent. Whether the company can retrieve its data, in a usable format, inside a window that is long enough, while the agreement is still in force, is four separate questions and each one fails independently.
- Mark every continuity and exit claim as evidenced, contractual, or untested. The distinction is the whole content of the assessment.
- Match governance cadence to tier and value, and record decisions with owners. A quarterly meeting with no decision record is a status update the supplier prepares.

**Parallel surface.** Independent items fan out and are parallel safe: each supplier's dependency and substitutability assessment, each exit readiness review against its own contract, each relationship risk profile, and the governance cadence design per supplier. The aggregates are single passes over the whole population and cannot be assembled supplier by supplier, which is the entire reason this desk exists: concentration by entity, by capability, and by business unit, the segmentation itself since it is a ranking rather than a rating, the fourth-party overlap where several suppliers depend on the same underlying provider, and the portfolio view of where two suppliers deliver one capability. A supplier assessed alone always looks proportionate.

**Acceptance bar.** Segmentation states both axes and the basis for each supplier's placement. Concentration is stated as a share with the population and the consolidation rule named. Dependency names what stops, for whom, and how fast. Substitutability names actual alternatives or states that none exists. Switching lead time is elapsed and includes migration. Every critical supplier carries an explicit single source or sole source determination. Exit readiness states, per supplier, whether an exit could be executed today and exactly what is missing. Every continuity claim is marked evidenced, contractual, or untested.

## Outputs

A complete run delivers the set:

- `portfolio-segmentation.md`: every supplier placed on value and criticality with the basis for both, the segment definitions in use, and the suppliers whose placement changed since the last view with the reason.
- `concentration-view.md`: share by consolidated legal entity, by capability, and by business unit, with the consolidation rules applied and the entries where a parent relationship could not be confirmed.
- `dependency-assessment.md`: per critical supplier, what stops, for whom, how quickly, what the fallback is, and how long the company could operate without them.
- `substitutability-and-switching.md`: realistic alternatives per critical supplier, switching cost, elapsed switching lead time including migration and parallel running, and the lock-in mechanisms that drive both.
- `single-versus-sole-source-register.md`: an explicit determination per critical supplier, with the alternatives that exist for a single source position and the exposure statement for a sole source one, and the different action each carries.
- `exit-readiness-assessment.md`: per critical supplier, whether an exit could be executed today, the contract rights it would rely on, what is missing, whether any part has been tested and when, and the untested assumptions stated as untested.
- `relationship-risk-register.md`: the supplier's financial trajectory, ownership and change of control exposure, product direction and end-of-life notices, key person and support model changes, and what each would do to the company.
- `governance-cadence-plan.md`: per supplier, the rhythm the tier and value justify, the attendees on both sides, the standing agenda, the decisions the forum may take, and where they are recorded.
- `fourth-party-exposure-note.md`: where several suppliers depend on the same underlying provider, what that concentration means, and the evidence behind it.
- `relationship-governance-downstream-handoff.md`: the segmentation, concentration, and exit positions the spend, renewal, and offboarding stages inherit.

Depth standard: an artifact is complete when a risk committee could act on it without commissioning a study. "Critical supplier, high dependency" is a label; "the sole provider of a capability that stops customer billing within one business day, with no alternative able to serve at this transaction volume, a data export limited to a proprietary format, an elapsed switching lead time driven by re-integration rather than by migration, and an exit that has never been exercised" is an assessment.

Where a supplier is genuinely substitutable and low criticality, the register says so briefly rather than being padded to match the critical entries, because an assessment that treats every supplier as significant tells a reader nothing about which three matter. Where the spend data, the contract terms, or the supplier's own dependency disclosures cannot be reached, `relationship-governance-diagnostic.md` names the gap and states which concentration and exit conclusions are unavailable.

Something unusual happens to this desk's central artifact: it is read almost exclusively by people who have no way to test it. An exit plan and a continuity position are consumed by a risk committee, an auditor, an insurer, a customer security questionnaire, and in regulated sectors a supervisory register, and every one of those readers takes the document as a description of a capability. Nothing in the format distinguishes an exit that was rehearsed, an exit that follows from contract rights somebody read, an exit inferred from the fact that the product exports data, and an exit somebody hoped would work. The company then inherits its own assessment into its own attestations and answers for it, and the moment of discovery is a supplier failure, which is the worst possible time to learn that the retrieval window was thirty days and the migration takes four months. So each claim here is marked evidenced, contractual, or untested; an exit that has never been exercised is written as untested with the test that would settle it and what the test would cost; an alternative supplier nobody has qualified is written as unqualified rather than counted as substitutability; and a concentration figure built on an unconfirmed parent-subsidiary mapping is written with that mapping flagged, because the whole number depends on it.

## procurement_packet fields to update

- `relationship.segmentation`, `concentration`, `dependency`, `substitutability`, `switching_cost`, `switching_lead_time`, `supply_position`, `exit_readiness`, `governance_cadence`.
- `risk_tier.fourth_party_exposure` and `reassessment_trigger` where the portfolio view surfaces exposures a single use case assessment could not see.
- `diligence.continuity` with the recovery commitments, their dependencies, and whether the contract makes any of them enforceable.
- `offboarding.transition_plan` and `residual_dependency` in draft form for critical suppliers, so an exit is not designed during the crisis that requires it.
- `contract.open_positions` where exit readiness depends on a term the agreement does not contain, for the next renewal to fix.
- `approvals` where a concentration position, a sole source exposure, or an untested exit plan is being accepted as residual risk by a named owner.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Release integrity**: a continuity or exit readiness position is about to leave the company, into a customer security questionnaire, a regulator response, an audit, an insurance submission, or a board risk report, without the evidence behind it. An untested exit plan for a critical supplier is an assumption written in the format of a control, relied on by readers who cannot tell the difference. This is the defining halt for this desk.
- **Approval**: accepting a concentration position, a sole source exposure, or an untested exit plan as residual risk, and committing the company to a governance or partnership arrangement. Each is a decision with a named owner and a review date.
- **Production or destructive**: any relationship position that reaches the supplier, including a segmentation that tells them where they stand, a statement about the company's dependency, or a signal that the company is exploring alternatives. Telling a sole source supplier that they are the sole source is a commercial act with a price.
- **Security or privacy**: the portfolio view would require assembling incident, access, or personal data beyond what the assessment needs, or a fourth-party disclosure the company holds under confidentiality would be circulated further than its terms permit.
- **Source conflict**: the spend systems, the contract portfolio, and the business units disagree about which supplier delivers a capability or which entity the company contracts with, which makes every concentration figure a different number depending on the source. Record both readings with their locators.
- **Connector unreachable**: the spend data, the contract repository, or the supplier master exists and cannot be read, so concentration would be computed over a population that is partly unseen. Note that a partial population produces a confident understatement, which is the failure mode this view exists to prevent.

A supplier that has not returned its continuity documentation, an alternative whose capability has not been qualified, an unconfirmed switching estimate, and a governance forum with no attendee list are soft gaps. Record each against the supplier, state what it leaves unestablished, and continue.

## Downstream handoffs

`spend-analysis-desk` inherits the consolidation rules and the entity mapping, and returns the ledger view that tests whether the concentration picture was right. `renewal-consolidation-desk` inherits the segmentation and the portfolio clustering, since three agreements with one supplier are one negotiation and the governance view is where that becomes visible. `vendor-offboarding-desk` inherits the exit readiness assessment and the missing items, and it is the stage that proves whether the assessment was honest. `pricing-negotiation-desk` inherits the dependency and substitutability position, because a walk-away is only credible where an alternative exists and this is the desk that knows whether it does. `vendor-risk-tiering-desk` inherits the fourth-party exposure for future tiering.

## Quality bar

A good portfolio view changes what somebody does. It names the three suppliers that could actually stop the business and says why, rather than rating forty. It computes concentration on entities rather than on invoices, so the supplier that appears four times under four names appears once at its real size. It is candid about exit readiness, including for the suppliers where the honest answer is that the company could not leave inside a year. It says which continuity claims have been tested and which have only been received. And it makes the single source and sole source distinction explicitly for every critical dependency, because those two conditions look identical on a register and need opposite responses.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
