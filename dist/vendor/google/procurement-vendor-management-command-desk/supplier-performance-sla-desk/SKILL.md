---
name: supplier-performance-sla-desk
description: measure supplier performance against the contract by building a scorecard with a named measurement source per dimension, reading service level results against the exclusions in the definition, reconciling credits earned to credits claimed and received inside the claim window, separating contractual compliance from business outcome, and comparing consumption to purchased entitlement to expose shelfware and true-up exposure. use for supplier scorecards, sla measurement and breach assessment, service credit claims, availability and uptime disputes, incident and root cause review, quarterly business reviews, seat and licence utilization, and supplier improvement plans.
---

# Supplier Performance SLA Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, measure the period, produce the artifact set, update `procurement_packet`, and continue into `supplier-relationship-governance-desk`. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that makes the executed service level definition govern over the supplier's report of its own performance.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the measure it affects.

Never invent an availability figure, a downtime duration, an incident, a root cause, a response or resolution time, a ticket volume, a credit amount, a claim date, a utilization count, an active user number, a scorecard rating, or a supplier commitment the contract does not contain.

## Role

Own the answer to whether the company is getting what it bought, and own the distinction that question conceals. A supplier can meet every contractual commitment while the thing the company purchased does not work, and it can miss commitments repeatedly while remaining in compliance because the remedy is a capped credit it is content to pay. Contractual compliance and business outcome are measured separately here, and reported separately, because conflating them produces either a scorecard that exonerates a failing supplier or an escalation the contract does not support.

Three specifics carry most of the value. Service level results are read against the exclusions in the definition rather than against the headline percentage, because scheduled maintenance, emergency maintenance, degraded performance, single-region outages, customer-caused events, and third-party network faults are frequently outside the calculation, and whether an outage sits inside or outside that boundary is the whole question. Credits are almost never applied automatically and almost always carry a claim window measured in days, so a credit nobody claimed is a discount the company declined. And consumption against entitlement is the fastest cost reduction available anywhere in the portfolio, because the seats nobody uses cost more than the discount nobody offered.

## Use when

- A review period has closed and a scorecard is due, or a quarterly business review needs a factual basis.
- A service level may have been breached and the result has to be read against the definition, its exclusions, and the measurement source.
- Service credits need calculating, claiming inside the contractual window, or reconciling against what was actually received.
- An incident or a run of incidents needs recording with impact, the supplier's root cause account, and whether the commitment covered it.
- Support responsiveness, ticket volumes, resolution times, or escalation handling are in question.
- Purchased entitlement has to be compared to actual consumption ahead of a renewal, a true-up conversation, or a cost reduction target.
- Performance is below the bar and an improvement plan with milestones and consequences is needed.
- Someone says a supplier is too expensive and nobody has yet checked what is actually being used.

## Do not use when

- The service levels themselves are being specified before a purchase: `requirements-specification-desk`.
- The service levels were never extracted from the executed agreement and their definitions are unknown: `contract-execution-routing-desk`.
- The question is portfolio concentration, dependency, substitutability, or exit readiness: `supplier-relationship-governance-desk`.
- The question is price rather than performance, or the negotiation position for a renegotiation: `pricing-negotiation-desk`.
- The renewal decision, the notice deadline, and the decision date are the question: `renewal-consolidation-desk`, which consumes this desk's results.
- The relationship is ending and the exit sequence is the work: `vendor-offboarding-desk`.
- The dispute has become a contractual claim needing enforcement or termination for cause: prepare the evidence here and route the claim to the Legal Contracts suite.

## Required evidence

- The contracted service levels as executed, with each definition, its measurement window, its exclusions, its remedy, and the credit claim window and method.
- The measurement source for each commitment and whose telemetry decides, including whether the company has its own observation or is reading the supplier's report.
- Performance data for the period from every available source, including the supplier's report, the company's monitoring, and the status history.
- Incident history with dates, duration, impact, affected population, and the supplier's root cause statements with the dates those were delivered against any contractual commitment to deliver them.
- Support data: ticket volumes by severity, time to first response, time to workaround, time to resolution, and reopened tickets.
- The scorecard dimensions the relationship's tier and value justify, with the source that would measure each.
- Purchased entitlement from the order form, and consumption from the supplier's usage reporting or the company's own identity data, including last activity where available.
- The business case outcomes and whether they arrived.
- Escalation history, governance meeting records, and what came of prior commitments.

## Workflow

**Outcome.** A scorecard with a named measurement source per dimension, service level results read against their definitions and exclusions, a credit position covering earned, claimed, and received with the claim window state, an incident record, a consumption against entitlement position with the true-up or reduction it implies, a separate statement of business outcome against the business case, an improvement plan where performance sits below the bar, and an explicit list of dimensions with no measurement behind them.

**Grounding.** The executed service level definition governs. Availability reported by the supplier is a self-measurement, useful and not decisive; where the commitment matters the measurement source is named and the exclusions are read. Support metrics computed from the supplier's own ticketing system inherit that system's clock, its severity assignment, and its treatment of reopened tickets, and each of those is a place where the number moves without anyone changing the service.

**Constraints.**

- Read the definition before computing the result. An outage that falls inside a maintenance window, affects a single region, or degrades rather than removes service may be excluded, and the difference decides whether a breach occurred at all.
- Name the measurement source for every dimension. A dimension measured by impression is reported as unmeasured, not scored.
- Compute credits from the contractual formula and check them against the claim window, which is frequently short and starts at the incident rather than at the invoice. State whether the window is open, and what lapses on which date.
- Report credits earned, claimed, and received as three separate numbers, since they are routinely three different numbers and only the third one reaches the company.
- Separate contractual compliance from business outcome and state both. A supplier paying a capped credit every month is meeting the contract and failing the business, and only one of those facts appears on a compliance report.
- Compare consumption to entitlement using activity rather than provisioning. Accounts that exist and accounts that are used are different counts, and the gap between them is money.
- Use the contract's own remedies and escalation path rather than a generic ladder. The right to escalate, the chronic failure provision, and the termination right each have preconditions, and invoking one without meeting them forfeits it.
- Where the supplier's figures and the company's observations disagree, record both with the definition each used rather than adopting whichever is more convenient.

**Parallel surface.** Independent items fan out and are parallel safe: each service level commitment assessed against its own definition and data, each scorecard dimension against its own source, each incident against the commitment that covers it, support metrics by severity band, and the entitlement reconciliation per product or per business unit where the agreement covers several. Three steps are single passes after the fan-out returns. The credit position is computed once across the period, because caps, aggregations, and the sole remedy provision apply across the whole period rather than per incident. The overall performance disposition is one pass, since a supplier is performing or it is not and a rating assembled dimension by dimension hides the pattern that matters. The trend against prior periods is also a single pass, because a run of narrow passes is a different finding from one bad month and neither is visible inside a single period's numbers.

**Acceptance bar.** Every service level result states the commitment, the definition's exclusions as they were applied, the measurement source, the computed result, and whether a breach occurred. Every credit line shows the formula, the amount, the claim window with its deadline, and the state. Every scorecard dimension names its source or is marked unmeasured. The entitlement position states purchased, provisioned, and actively used counts with the observation window. The business outcome statement is separate from the compliance statement. Where the supplier's figure and the company's differ, both appear with their definitions.

## Outputs

A complete run delivers the set:

- `supplier-scorecard.md`: dimensions covering delivery, quality, responsiveness, commercial behavior, and risk posture, each with its measure, its named measurement source, the period, the result, and the trend, with unmeasured dimensions marked as such.
- `service-level-results.md`: a line per commitment with the contracted target, the definition and the exclusions as applied, the measurement source, the result, the breach determination, and the events that sat on the boundary of an exclusion.
- `credit-position.md`: credits earned by the contractual formula, credits claimed with dates, credits received, the claim window and its deadline per event, the cap and whether it binds, and the unclaimed value about to lapse.
- `incident-record.md`: each incident with date, duration, impact, affected population, the supplier's root cause account and when it arrived against any contractual deadline, and whether a commitment covered it.
- `support-performance.md`: volumes by severity, time to first response, workaround, and resolution against the contracted targets, reopened ticket rate, and the escalations raised with their outcomes.
- `consumption-versus-entitlement.md`: purchased, provisioned, and actively used counts with the observation window and the activity definition, the true-up or reduction implied, the timing rights the contract grants, and the annualized value of the gap.
- `business-outcome-assessment.md`: the outcome the business case promised, what arrived, and the gap, stated separately from contractual compliance.
- `improvement-plan.md`: the findings driving it, milestones with dates and owners on both sides, the measurement that will show recovery, and the consequence the contract attaches to missing it.
- `escalation-position.md`: the contractual remedy actually available, the preconditions it requires, what has been satisfied, and the prepared escalation with what it commits the company to.
- `supplier-performance-downstream-handoff.md`: the results, the unclaimed credits, the entitlement gap, and the open commitments the governance and renewal stages inherit.

Depth standard: an artifact is complete when the supplier's account manager could be handed it and would have to respond to specifics. "Availability missed the target" is an assertion; "the monthly commitment against the measured result, computed from a named source, with the two maintenance windows excluded under the named clause and the third excluded event contested because it exceeded the notified window, producing a credit at the contractual rate with a claim deadline on a stated date" is a claim somebody can pay.

Where a commitment has no measurement source at all, `service-level-results.md` records it as unmeasurable with what would have to exist to measure it, since an unmeasurable service level is itself a contract finding for the next renewal. Where the supplier's reporting portal, the monitoring data, or the usage telemetry cannot be reached, `supplier-performance-diagnostic.md` names the gap and states which commitments cannot be assessed for the period.

Performance work arrives in the shape of a grid, and the shape itself does the damage: a grid with an empty cell looks broken while a grid with a plausible number in it looks finished. The pressure to complete the table is strongest for exactly the dimensions nobody measures, which is why quality, responsiveness, and commercial behavior tend to arrive as ratings while availability arrives as a figure. A rating with no source behind it then survives into a quarterly review, a renewal recommendation, and occasionally into a claim, where it is the first thing the supplier asks about. So a dimension with no measurement is left marked unmeasured with the source that would fix it, an availability figure taken from the supplier's own report is labeled as the supplier's measurement rather than as the result, a root cause is recorded as the supplier's account rather than as the cause, and a utilization number without an activity definition and an observation window is not written at all.

## procurement_packet fields to update

- `performance.scorecard`, `sla_results`, `measurement_source`, `incidents`, `escalations`, `governance_meetings`, `improvement_plan`, `consumption_versus_entitlement`, `business_case_realization`.
- `commercial.commitment_mechanics` where consumption against entitlement changes the true-up or true-down position.
- `contract.open_positions` where a service level definition, an exclusion, or a credit mechanism proved unenforceable and has to change at renewal.
- `relationship.dependency` and `substitutability` where performance revealed how hard the supplier is to replace.
- `renewals.contracts[].uplift_exposure` context, since a supplier below the bar and a supplier with unused entitlement are different renewal conversations.
- `approvals` where a claim, an escalation, or a formal breach notice requires authorization.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Source conflict**: the supplier's reported performance and the company's own telemetry disagree about whether a commitment was met. This is routine, because the definitions differ, the exclusions differ, and the supplier is measuring itself. Asserting a breach on the wrong measurement forfeits the claim and damages a relationship the company may not be able to leave; accepting the supplier's figure without reading the definition means no commitment is ever measured. Record both readings with their sources and the definition each used.
- **Production or destructive**: a breach notice, a credit claim, a formal escalation, an improvement plan, or a performance position that reaches the supplier. Each is a statement the company then has to stand behind, and a claim withdrawn is worse than a claim not made.
- **Approval**: invoking a contractual remedy, waiving a credit, accepting a service level miss, agreeing an improvement plan on the company's behalf, or triggering a chronic failure or termination right. Each is a decision with a named owner.
- **Security or privacy**: the performance evidence would require circulating incident detail, customer impact data, or personal data beyond the people entitled to see it, or a supplier incident touched company or customer data and the assessment belongs with the security and privacy reviewers rather than in a scorecard.
- **Release integrity**: a performance position would be reported to an executive review, a regulator, an insurer, or a customer as measured when the measurement source does not exist or covers a different scope than the commitment.
- **Connector unreachable**: the supplier's reporting portal, the monitoring system, the ticketing system, or the usage telemetry exists and cannot be read, so results would be asserted for the period rather than measured.

A supplier that has not delivered a root cause statement, an unreturned ticket export, an unconfirmed maintenance notification, and an activity report still being generated are soft gaps. Record them against the measure, state what the gap prevents, and continue with the measures that do have sources.

## Downstream handoffs

`supplier-relationship-governance-desk` inherits the performance trend, the dependency the incidents exposed, and the governance cadence the results justify. `renewal-consolidation-desk` inherits the entitlement gap, the unclaimed credits, and the performance record, which together are the strongest material any renewal negotiation has. `pricing-negotiation-desk` inherits the consumption position and the service level failures as commercial positions, since a reduction in unused seats is a realized saving and a strengthened remedy is a term. `contract-execution-routing-desk` inherits the definitions that proved unenforceable so the next agreement fixes them. `spend-analysis-desk` inherits the utilization picture, which is what distinguishes a supplier that is expensive from a supplier that is over-purchased.

## Quality bar

A good performance review is one both parties can work from. It cites the definition rather than the headline number, it says where each figure came from, and it is explicit about what it could not measure. It reports credits as three numbers and names the date the unclaimed ones lapse. It states plainly when a supplier is compliant and the business is still not getting what it bought, because that sentence is the one that changes a renewal. And it holds its shape under pressure from both directions: it does not manufacture a breach for a sponsor who wants leverage, and it does not accept a self-reported figure from a supplier whose own definition excluded the outage everybody remembers.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
