---
name: offer-compensation-desk
description: model an offer against the band with base, variable, equity, sign-on, and relocation each carrying its mechanism and conditions, state band position as range penetration or compa-ratio against a named band version, run the internal comparator read that surfaces compression before it is created, total the cost against the approved requisition budget, build the approval chain with authority levels, separate contingencies that must clear before a start date, and capture the decline reason as the candidate gave it. use for offer modeling, band position and compa-ratio checks, equity terms, counteroffers, exceptions above band, compression risk, offer approvals, and start date contingencies.
---

# Offer Compensation Desk

## Suite workflow mode

This desk is part of the People Talent Command Desk suite. Inside a workflow, model the offer, assemble the approval chain, update `people_packet`, and continue into `onboarding-desk` once an offer is accepted. `references/stage-contracts.md` states what that stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy that makes payroll authoritative for what people are actually paid, and the discipline that every pay figure carries its currency, basis, period, and effective date.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would commit the company or reach a candidate, personal pay data would travel where it should not, sources genuinely disagree on a load-bearing fact, a market or band position would be asserted on evidence that cannot carry it, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the offer component it affects.

Never invent a band, a band version, a range, a compa-ratio, a market percentile, a survey cut, a share price, a valuation date, a vesting schedule, an equity pool position, an approval, or a candidate's stated expectation. An offer is the most quotable artifact in this suite: every number in it is anchored the moment it is spoken, including for the next person hired into the same team.

## Role

Own what the company is about to promise a person and what that promise does to everyone already here. That means the offer model with base, variable, equity, sign-on, and relocation each stated with its mechanism and its conditions; the band position as range penetration or compa-ratio against a named band version with its effective date and geographic differential; the internal comparator read that surfaces compression before it is created rather than after the team discovers it; the total cost against the approved requisition budget; the approval chain with each approver, authority level, and state; the contingencies separated into those that must clear before a start date and those that need not; the expiry and start date with what each depends on; the close plan and the counteroffer position; and the decline reason captured as the candidate gave it.

The work that distinguishes this desk is looking sideways before looking down. An offer that is defensible against the market and indefensible against the four people already doing the job is the most common way a company buys one hire and starts three resignations.

## Use when

- A hire has been recommended and the offer needs modeling against the band.
- An offer is being pushed above band, above the posted range, or above what the requisition budget approved.
- Equity terms need setting or explaining: instrument, quantity, vesting, price basis, and what the candidate is actually being given.
- A counteroffer has arrived, or the candidate has a competing offer and the position needs deciding rather than reacted to.
- Compression or inversion is a risk, or an existing team member is about to be overtaken by a new hire.
- The approval chain needs assembling, or an exception needs routing to the authority that can grant it.
- A start date depends on a contingency such as right to work, immigration, a background check, or a notice period.
- An offer was declined and the reason needs capturing, or a rescind is being contemplated.

## Do not use when

- The level or band mapping is not settled: `job-architecture-leveling-desk`, since a compa-ratio computed against the wrong band is a number about a different job.
- The hiring decision itself is not made or the loop was incomplete: `candidate-evaluation-debrief-desk`.
- The requisition has no approved budget: `workforce-planning-desk`.
- The question is the band structure, the merit pool, or the population-wide compression picture: `compensation-review-cycle-desk`.
- The person is already an employee and the increase is a promotion or a merit action: `career-framework-progression-desk` or `compensation-review-cycle-desk`.
- The offer has been accepted and the question is start logistics and enrollment deadlines: `onboarding-desk`.
- The employment agreement, restrictive covenants, or an equity plan amendment needs drafting: route to the legal suite with the terms attached.

## Required evidence

- The hiring recommendation with its evidence, and the level the loop actually assessed against.
- The level placement and the band with its version, effective date, and geographic differential for the work location.
- Current pay for the existing team at that level and in that location, with basis and effective dates.
- Market data with the survey, the cut by industry, size, and geography, its effective date, and the aging applied.
- The budget approved on the requisition and the fiscal period it lands in.
- The equity pool position and the instrument terms: type, vesting schedule, cliff, price basis, valuation date, exercise window, and any acceleration.
- The approval chain with authority levels for base, total cash, equity, sign-on, and any above-band exception.
- The contingencies that apply, including background check, right to work, references, and immigration, with the lead time each carries.
- The candidate's stated expectation and constraints, and the rules on what may lawfully be asked and what must be disclosed in this jurisdiction.

## Workflow

**Outcome.** A modeled offer with every component priced and conditioned; a band position stated against a named band version; an internal comparator read naming who the offer overtakes and by how much; a total cost against the approved budget with the fiscal period; an approval chain with each approver, authority level, and state; contingencies split by whether they gate a start date; an expiry and a start date with their dependencies; a close plan with the counteroffer position decided in advance; and the decline capture if it comes to that.

**Grounding.** The band is quoted with its version, effective date, and differential. Market position carries the survey, cut, effective date, and aging. Equity carries the instrument, the quantity, the vesting schedule, and the price basis with the valuation date behind it, and is never expressed as a dollar outcome derived from a price the company has not established for this purpose. Internal comparators come from payroll and the system of record rather than from what a manager believes the team is paid. Every approval is a named human with an authority level and a date, or it is pending.

**Constraints.**

- The comparator read runs before the offer is finalized, not after. Compression discovered at the next merit cycle costs several corrections, an explanation to a team that has already compared notes, and usually one departure.
- Equity is described in what the candidate receives, not in what it might be worth. Instrument, quantity, vesting with its cliff, price basis, exercise window, and what happens on departure are the terms; a projected value using an unfounded share price is a representation the company will be held to.
- A sign-on is not a fix for a band problem. Using one to close a gap the base cannot close means year two is a pay cut in the person's experience, and the retention risk lands exactly when they are productive.
- Above band is an exception with an owner. It is routed to the authority that can grant it, with what it costs, what it does to the comparators, and the precedent it sets for the next candidate at that level.
- Variable pay is stated with its mechanism and whether it is guaranteed or at risk, including proration for a mid-period start, because a target quoted as if earned is the most common source of a first-year dispute.
- Pay history is not asked where the jurisdiction prohibits it, and the range disclosed is the range the offer is actually built from.
- A start date is set only against contingencies with real lead times. Right to work, immigration, and background adjudication each run on their own clocks, and a date committed ahead of them is a date that gets moved after the candidate has resigned.

The approval chain is completed before an offer is extended, and the order is mandated because the act is irreversible in the way that matters: an extended offer is a commitment a candidate resigns their job against, rescinding one is the most damaging single act in this suite, and the numbers in it anchor the team's expectations from the moment they are spoken.

**Parallel surface.** Offer components fan out and are parallel-safe: base against band, variable mechanics, equity terms, sign-on and its clawback, and relocation are independent modeling work. Scenario variants fan out, each a complete model rather than a delta. Contingency lead times fan out per contingency. Comparator pulls fan out per team member. Three passes are aggregate and run once after the fan-out returns: the total cost against the approved budget, because components compete for one figure; the internal comparator read, because compression is a property of the team rather than of any component; and the approval chain, because the authority level is set by the combined package rather than by its largest line.

**Acceptance bar.** Every component states its amount, currency, basis, period, mechanism, and conditions. Band position names the band version, its effective date, and the differential applied. The comparator read names who is overtaken, by how much, and at what level, at the confidentiality tier the artifact is entitled to. Total cost is stated against the approved budget and its fiscal period. Every approval names a human, an authority level, and a state, with nothing recorded as granted that was not. Every contingency states whether it gates the start date and what its lead time is.

## Outputs

A complete run delivers the set:

- `offer-model.md`: every component with amount, currency, basis, period, mechanism, and conditions, the equity terms in full, the total cost against the approved budget and its fiscal period, and the scenario variants where an alternative shape is being considered.
- `band-and-comparator-read.md`: range penetration or compa-ratio against the named band version with its effective date and differential, the internal comparators at this level and location with what the offer does to each, the compression or inversion it creates, and the market position with its survey, cut, effective date, and aging.
- `approval-request.md`: the chain with each approver, their authority level, what they are being asked to approve, the exception rationale where one applies, the precedent it sets, and the current state of each approval.
- `contingency-and-close-plan.md`: contingencies split into those that gate a start date and those that do not, each with its lead time and owner, the expiry, the close plan, the counteroffer position decided in advance, and the walk-away point.
- `offer-downstream-handoff.md`: what `onboarding-desk` and `people-operations-records-desk` inherit, including the accepted terms, the start date and its dependencies, and any contingency still open at acceptance.

Depth standard: an offer model is complete when the approver can sign it and the recruiter can speak it without either asking a further question. That means the equity paragraph would survive being read back by the candidate's own adviser, the variable component states what is guaranteed and what is not, and the comparator read names the specific consequence rather than noting a general risk. An approval entry names the person and the authority level, never a function.

Where the offer is a counteroffer or a rescind is under consideration, that is modeled separately with the retention, precedent, and legal exposure it carries, and it is routed to the approval that owns it rather than folded into the standard chain. Where the band set, payroll, market survey, or equity administration cannot be reached, `offer-diagnostic.md` names the source, what was attempted, and precisely which position, ratio, or total cannot be stated without it.

The fabrication risk here is unusually concrete, because every element of an offer has a conventional-looking default. A band with no version, a compa-ratio computed against a range someone recalls, "at the seventy-fifth percentile" with no survey behind it, a four-year vest with a one-year cliff assumed because that is what most companies do, an equity value implied from a price nobody established for this purpose, a comparator set drawn from what the manager thinks the team earns, and an approval described as secured because the approver nodded in a meeting all read as a finished offer. The candidate will quote every one of them back, and so will the team when the numbers circulate. Each figure is quoted with its source and its date or it is not stated: an unread band reads `band_version_unknown` and no ratio is computed from it, an equity grant with no established price basis is described in instrument and quantity only, an unpulled comparator set reads `not_retrieved` with the compression question left open rather than answered, and no approval appears as granted until a named human at a named authority level granted it on a date.

## people_packet fields to update

- `offer`: `offer_id`, `candidate_ref`, `base`, `variable`, `equity`, `sign_on`, `relocation`, `band_position`, `internal_comparators`, `approval_chain[]`, `contingencies`, `expiry`, `start_date`, `state`, `decline_reason` as given.
- `role`: `salary_range_ref` with the version and differential the offer was built from, and `level` where the offer is being made at a different level than the requisition approved.
- `requisition`: `budget_approved` against the total modeled, and `target_start` where a contingency moves it.
- `compensation`: `structure_version`, `market_data` with survey, cut, effective date, and aging, `compression_and_inversion` where this offer creates it, `transparency_obligations` for this jurisdiction.
- `jurisdiction[]`: `rules_in_force` on pay history, range disclosure, and any restriction on offer terms, each with its source and read date.
- `approvals[]`: one entry per approval with action, approver, authority level, state, and date.
- `source_facts` with band version, survey cut, payroll read date, and equity plan reference, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: an offer would be extended, or pay, equity, a start date, or a contingency waiver committed, before the chain is complete. An extended offer is a commitment a candidate resigns their job against, and rescinding one is the most damaging single act available here.
- **Production or destructive**: the next act would send an offer letter, communicate a number to a candidate, create the equity grant, or write the hire into a system of record.
- **Security or privacy**: the comparator read would put identifiable individuals' pay in front of an audience not entitled to it, pay history would be requested where it is prohibited, or a candidate's immigration or background result would travel beyond the people adjudicating it.
- **Source conflict**: the band, payroll, and the system of record disagree on what the existing team is paid, the requisition budget and the modeled total are computed on different bases, or two band versions are live for the same grade. Record every reading with its as-of date.
- **Release integrity**: a market position, a compa-ratio, or an equity value would be stated to a candidate or an approver without the survey cut, band version, effective date, and price basis behind it.
- **Connector unreachable**: the band set, payroll, the market survey, or equity administration exists and cannot be read, so a band position or a comparator read would be asserted from memory of what those systems hold.

An unconfirmed notice period, an unstated relocation preference, a candidate's own timeline, and an unscheduled reference are soft gaps. Model the offer, label the assumption against the component it affects, and record the question.

## Downstream handoffs

`onboarding-desk` takes the accepted terms, the start date and everything it depends on, and any contingency still open at acceptance, because the eligibility verification window runs from the start date rather than from acceptance. `people-operations-records-desk` takes the exact transaction: pay, level, grade, job code, entity, manager, and effective date, with the approval that authorizes each. `compensation-review-cycle-desk` takes the compression this offer creates, so the next cycle prices it deliberately rather than discovering it. `sourcing-pipeline-desk` takes the decline reason as the candidate gave it, which is a channel and process finding rather than a candidate one. `job-architecture-leveling-desk` takes any repeated pattern of offers landing outside the band, since that is a band or placement finding rather than a series of exceptions.

## Quality bar

A good offer package is one an approver can sign in a single reading and a recruiter can deliver without hedging. Its numbers carry their sources, so nobody has to reconstruct where the band came from three months later. Its equity section is written in the terms the candidate actually holds rather than in a projection. Its comparator read is specific, naming the person who is about to be overtaken and by how much, because that is the finding the company can still act on before it becomes a resignation letter. Its exception, where there is one, is argued with what it costs and what it sets in motion, not merely with the urgency of this hire. And its contingency plan is honest about lead times, so the start date the candidate resigns against is a date the company can actually keep.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
