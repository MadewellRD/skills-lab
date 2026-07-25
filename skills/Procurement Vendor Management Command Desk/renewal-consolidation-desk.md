---
name: renewal-consolidation-desk
description: build the renewal calendar from executed agreements by quoting the notice clause and computing the notice deadline and the date it counts from, set the earlier decision date that keeps options open, quantify uplift exposure and consumption against entitlement per contract, cluster renewals by supplier and quarter, identify consolidation candidates with the term alignment that makes or blocks them, and prepare notices in the form the clause requires. use for renewal calendars, auto renewal and notice window tracking, evergreen contract risk, uplift and escalator exposure, tool rationalization, contract consolidation, co-termination, and renewal decisions before the window closes.
---

# Renewal Consolidation Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, build the calendar, take the renewal position, produce the artifact set, update `procurement_packet`, and continue into `vendor-offboarding-desk` where the decision is to exit or back into `pricing-negotiation-desk` where it is to renegotiate. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that makes the executed clause govern over any repository field that summarizes it.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the contract it affects.

Never invent an end date, a renewal type, a notice window, a notice deadline, an uplift percentage, a price protection expiry, a consumption figure, an entitlement count, a consolidation saving, a migration cost, or a decision owner.

## Role

Own the clock. Almost every other exposure in procurement can be corrected late at some cost; a notice window cannot. It closes on a date, nothing reopens it, and the transition is performed by nobody, which is what makes an unnoticed auto-renewal the most common expensive mistake in the function. One day past the deadline converts an open decision into another full term at the contracted uplift, with no remedy, no appeal, and a loss equal to the entire value of the negotiation that will not now happen.

This desk therefore does two things that look administrative and are not. It computes dates from executed clauses rather than reading them off a repository field, because that field was typed by a person reading the clause and the notice window is precisely the value that gets transcribed wrong: the clause counts from a date the summary field does not record. And it sets a decision date that precedes the notice deadline by the time a decision actually takes, because a deadline that arrives with the decision unmade is a deadline that has already been missed.

The second half of the job is portfolio shaped. Renewals cluster, and three agreements with one supplier are one negotiation with three deadlines. Treated separately, the supplier gets three chances and the company gets none.

## Use when

- A renewal is approaching, has surfaced, or has already processed, and the position has to be established.
- The renewal calendar has to be built or rebuilt across a portfolio from executed documents.
- A notice window may be open or may have closed, and the deadline has to be computed rather than assumed.
- Uplift exposure has to be quantified: what renewal costs if nobody acts, under the escalator the agreement permits.
- Consumption against entitlement has to be brought into a renewal decision, since the reduction that is available only at renewal is the one people forget to take.
- Overlapping agreements are candidates for consolidation and the term alignment has to be assessed before the case is made.
- Several tools deliver one capability and a rationalization case needs migration cost and internal disruption stated rather than assumed away.
- A notice of non-renewal has to be prepared in the exact form and method the clause requires.
- An agreement auto-renewed and the company needs to know what is now committed and what the next opening is.

## Do not use when

- The dates have never been extracted from the executed document and no calendar exists yet: `contract-execution-routing-desk` performs the extraction this desk consumes.
- The commercial position, benchmarks, and negotiation plan for the renewal are the work: `pricing-negotiation-desk`.
- The supplier's performance in the period is the question: `supplier-performance-sla-desk`.
- The spend baseline, fragmentation, and coverage evidence behind a consolidation case are missing: `spend-analysis-desk`.
- The decision is to exit and the notice, data return, and deprovisioning sequence is the work: `vendor-offboarding-desk`.
- The portfolio segmentation, concentration, and dependency view is the question: `supplier-relationship-governance-desk`.

## Required evidence

- The executed agreements with every amendment and order form, since an amendment routinely changes the term, the renewal type, or the notice period and the original clause is the one people quote.
- The termination and renewal clauses in full, including the notice period, the method and address notice must use, and the date the period counts from.
- Current pricing and the uplift or escalator the renewal terms permit, including any index linkage and its floor.
- Price protection, price holds, and their expiry dates.
- Consumption against purchased entitlement, and the reduction rights the agreement grants at renewal.
- Performance history, open issues, unclaimed credits, and whether service levels held.
- The business need as it stands now rather than as it stood at signature, including whether the population that uses it still exists.
- Alternatives with their switching cost and elapsed switching lead time, measured against the time remaining.
- Overlapping agreements with their scope, value, and term end dates, for consolidation assessment.
- The named decision owner for each contract and the approval the decision engages.

## Workflow

**Outcome.** A renewal calendar built from executed documents with each notice deadline computed and sourced, a decision date per contract that precedes it, a renewal position per contract covering price, uplift exposure, consumption, performance, and continued need, consolidation candidates with term alignment and combined value, a portfolio view clustered by supplier and quarter, a renegotiation position taken while notice is still available, prepared notices where the decision is to exit, and an explicit list of contracts whose executed document could not be located.

**Grounding.** The executed clause is the source for every date. A repository field, a calendar reminder, a supplier's renewal email, and a finance accrual schedule are transcriptions and are recorded as such where they have to be used at all. The uplift is read from the agreement rather than from what the supplier proposes, because a supplier proposing an increase above what the clause permits is a negotiation, not a fact.

**Constraints.**

- Compute each date from the clause and state the date basis, since notice periods count from the term end, the anniversary of the effective date, or the order form start depending on the drafting, and those are different days.
- Set the decision date by working back from the notice deadline through the time a decision actually takes: the internal approval, the negotiation, and where relevant the alternative's lead time. The decision date is the one that goes in the calendar.
- Name an owner per contract. A deadline with no owner is a deadline nobody misses on purpose.
- Quantify uplift exposure as the cost of doing nothing, over the next full term, at the escalator the agreement permits.
- Bring consumption into every renewal position. The reduction right at renewal is usually the only moment entitlement can be lowered, and it lapses with the window.
- Assess consolidation on term alignment as well as scope. Two overlapping agreements ending eighteen months apart cannot be consolidated without a stub term, an early termination, or a co-termination concession, and the case has to say which.
- State migration cost and internal disruption in any rationalization case. A consolidation that ignores retraining, re-integration, and the business unit that will resist is a slide rather than a plan.
- Cluster by supplier and by quarter before taking positions, because a supplier with three renewals is one negotiation and the sequencing decides who has leverage.

**Mandated order.** The date chain below is set by contract law rather than by preference, and each step is the evidence for the next, so it is kept as an order:

1. Locate the executed agreement and every amendment in force.
2. Quote the notice clause and identify the date the period counts from.
3. Compute the notice deadline, then the decision date that precedes it.
4. Assign a named owner and take the decision inside the window.

The order is mandated because the window closes on a date and nothing reopens it, and a deadline computed without the amendments, or from a basis nobody identified, is confidently wrong in the one direction that costs a full term.

**Parallel surface.** Independent items fan out and are parallel safe: each contract's document retrieval, clause reading, date computation, uplift calculation, consumption reconciliation, and performance review runs on its own evidence. Two things are single passes after the fan-out returns. The portfolio view is one pass across the whole calendar, because clustering by supplier and by quarter is the entire point and it does not exist inside any one contract's entry. Consolidation assessment is also one pass, since overlap and term alignment are relationships between contracts rather than properties of them.

**Acceptance bar.** Every calendar entry states its end date, renewal type, notice window quoted from its clause, the date basis, the computed notice deadline, the source of every date, the days remaining, and a named owner. Every renewal position states current price, uplift exposure, consumption against entitlement, performance, and whether the need still exists. Consolidation candidates state combined value, overlapping scope, term alignment, and the mechanism that would make it possible. Contracts whose document could not be located are listed with dates unestablished and a retrieval action rather than with an inferred date.

## Outputs

A complete run delivers the set:

- `renewal-calendar.md`: a row per agreement with supplier entity, annual value, end date, renewal type, notice window quoted from its clause, date basis, computed notice deadline, decision date, days remaining, date source, and named owner.
- `notice-deadline-computations.md`: the working behind each date, quoting the clause and naming the amendment in force, so any date can be re-derived without reopening the file.
- `renewal-positions.md`: per contract, current price, the uplift the clause permits, exposure if nothing is done, consumption against entitlement, performance and unclaimed credits, whether the need persists, and the recommended decision.
- `portfolio-renewal-view.md`: renewals clustered by supplier and by quarter, with the sequencing that determines leverage and the agreements that should be negotiated together.
- `consolidation-candidates.md`: overlapping agreements with combined value, scope overlap, term alignment, the co-termination or stub term the consolidation needs, and the party whose concession makes it possible.
- `rationalization-case.md`: where several tools deliver one capability, the retained option, the migration cost, the internal disruption, the affected population, and the net position over a stated horizon.
- `renegotiation-position.md`: the leverage available while notice is still open, what closes on which date, and the asks that are only obtainable before the window shuts.
- `prepared-notices.md`: the notice text, the addressee, the method, and the delivery evidence the clause requires, prepared and unsent, with the deadline for sending it.
- `dates-unestablished.md`: contracts whose executed document could not be located, what is missing, the retrieval action, the owner, and whether a window may be open.
- `renewal-consolidation-downstream-handoff.md`: the decisions, deadlines, and positions the negotiation and offboarding stages inherit.

Depth standard: an artifact is complete when the owner could act on it without opening the contract. "Renews in the spring" is a note; "the initial term ends on a date stated in the executed order form as amended, renewing automatically for a further twelve months unless written notice is given not less than the period quoted from the named clause counting back from the term end, giving a notice deadline on a stated date, a decision date a stated number of days earlier, and a named owner" is a calendar entry.

Where an agreement genuinely has no renewal, the entry records expiry with what happens to service and data on that date, since an expiring agreement with a live integration is an outage rather than a saving. Where an executed document cannot be reached, `renewal-consolidation-diagnostic.md` names it and every date for that contract is recorded as date_not_established, and if a window may be open that item escalates immediately rather than waiting in the queue.

A renewal calendar is, of everything this suite produces, the file most likely to be copied into a shared tracker and trusted unmodified for a year. It is a table of dates, and a date carries no visible trace of its provenance: one computed from a quoted clause, one typed into a repository field by somebody reading that clause, one taken from a calendar reminder created two renewals ago, and one lifted from the supplier's renewal email all print as the same eight characters in the same column. The supplier's date is the least reliable of the four and the most likely to be believed, because it arrives looking like a service. So every date in this desk's output carries its source in the row rather than in a footnote, a transcribed date is never printed in the same column as a computed one without that label, a contract with no locatable document gets an empty date cell and a retrieval action rather than a plausible date, and an uplift the supplier has asserted is recorded as the supplier's proposal until the clause is read.

## procurement_packet fields to update

- `renewals.contracts[]` with contract reference, supplier entity, annual value, end date, renewal type, notice window, notice deadline, date source, uplift exposure, decision owner, decision, and decision date.
- `renewals.consolidation_candidates` and `portfolio_view`.
- `leverage_window`, which this desk is frequently the first stage to establish correctly, since a request that arrives assumed to be in term is often already inside or past its window.
- `commercial.term_structure` and `savings` where a renegotiation position is being taken.
- `performance.consumption_versus_entitlement` where the renewal reconciliation updated it.
- `offboarding.termination_basis` and `notice_state` where the decision is to exit and the notice has been prepared.
- `approvals` for the renewal decision, the notice, or the consolidation commitment, each with the amount at stake and the authority basis.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Approval**: both directions commit the company. Serving notice starts a clock against the supplier and cannot be recalled. Letting a term renew commits another full period at the contracted uplift and is performed by nobody, which is exactly why the decision to allow it is an approval rather than an omission. Consolidating onto a single agreement and agreeing an early termination to align terms are also approvals.
- **Production or destructive**: sending the notice, telling the supplier the company is considering leaving, or opening a renewal conversation. Each reaches the counterparty, and a signal of intent to leave that the company cannot follow through on is a position the supplier will test.
- **Connector unreachable**: the executed agreement cannot be reached and a notice window may be open. This halt costs money every day it stands and converts into an unrecoverable outcome on a known date, so it escalates immediately rather than being worked in queue order.
- **Source conflict**: the repository's renewal date and the executed clause disagree, an amendment contradicts the agreement it amends, or the supplier's stated notice period differs from the clause. Record both readings with their locators and treat the executed document as governing; where the conflict is between two executed documents with no order of precedence, that is the conflict to route.
- **Release integrity**: a renewal calendar would be published as authoritative with dates that were transcribed rather than computed, or a consolidation saving would be reported without the migration cost and the ledger baseline behind it.
- **Security or privacy**: a non-renewal decision would end a service holding company or customer data with no data return plan in place, which converts a commercial decision into a data loss on the termination date.

An unconfirmed consumption figure, an unnamed decision owner, a supplier who has not yet sent a renewal quote, and an alternative whose cost has not been established are soft gaps. Label them against the contract, keep the deadline visible, and continue; the deadline does not wait for the analysis.

## Downstream handoffs

`pricing-negotiation-desk` inherits the renegotiation position, the uplift exposure, the consumption gap, and the days remaining, which together set what is still obtainable. `vendor-offboarding-desk` inherits the prepared notice, its form and method, the termination basis, and the exit sequence timing, and it is the stage that has to complete data return before the term ends. `spend-analysis-desk` inherits the consolidation outcomes so the next baseline shows whether the saving arrived. `supplier-relationship-governance-desk` inherits the portfolio clustering and any dependency the renewal analysis exposed. `contract-execution-routing-desk` inherits the renegotiated position for execution, and returns the newly extracted dates into this calendar the day the amendment is signed.

## Quality bar

A good renewal calendar is trusted because every row shows its working. The dates are computed from clauses, the clauses are quoted, the amendments are accounted for, and the source of each date sits beside it. The decision date is earlier than the notice deadline by an amount that reflects how long a decision here actually takes, and it has a person's name against it. The portfolio view groups the three agreements with one supplier into one negotiation. The consolidation cases include the migration cost that makes some of them not worth doing. And the file is honest about the contracts it could not find, because a missing document inside an open window is the most urgent item in the whole portfolio and it is invisible on a calendar that only shows the contracts somebody could locate.
