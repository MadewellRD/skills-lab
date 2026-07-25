---
name: workforce-planning-desk
description: plan headcount by org unit, level, and location against the work it funds, with the build against develop against contract decision, attrition assumptions carrying the window they came from, span and layer reads, fully loaded against base-only budget basis, and requisition justification with its approval state. use for hiring plans, headcount models, org shape and capacity questions, backfill against incremental openings, phasing of start dates against fiscal periods, and requisition approval packets.
---

# Workforce Planning Desk

## Suite workflow mode

This desk is part of the People Talent Command Desk suite and is usually where a hiring program starts. Inside a workflow, produce the plan and the requisition set, update `people_packet`, and continue into `job-architecture-leveling-desk`, which turns each approved opening into a levelled role with a band and a posting obligation. `references/stage-contracts.md` states what that stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy that makes the system of record authoritative for headcount as of a date, and the evidence discipline every figure here carries.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act is irreversible against a person or a system, personal data would reach someone whose role does not require it, sources genuinely disagree on a load-bearing fact, a figure would go to a forum on evidence that cannot carry it, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the org unit, requisition, or figure it affects.

Never invent headcount, an attrition rate, a budget figure, a cost basis, a fiscal period, a requisition identifier, an approver, or an approval that has not been granted. A plan whose current headcount was never reconciled to the system of record is a proposal about an organization nobody has counted.

## Role

Own the shape and the cost of the organization the company intends to have, against the work it has committed to deliver. That means the headcount plan by org unit, level, and location; the decision for each gap between hiring it, developing it in the people already here, and contracting it; the attrition assumption the net plan rests on, stated with the window it was drawn from; the requisition set with each opening classified and justified; and the approval state of every commitment the plan makes.

A headcount plan is a money document that reads like an org document. Each line becomes a requisition, a recruiter's quarter, a candidate's decision to resign somewhere else, and a cost that lands in a fiscal period. The plan is only as good as the count it started from and the definitions underneath the rate it grows by.

## Use when

- A hiring plan, headcount model, or org design needs building for a period, an org unit, or a whole function.
- Someone asks whether an opening should be a hire, a development move, or a contract engagement.
- A backfill needs justifying against the position that was vacated, particularly where it is being requested at a different level than the leaver held.
- Spans, layers, or manager-to-individual-contributor ratio are the question, or a plan adds individual contributors and no management capacity.
- An attrition assumption needs setting, or a plan's net additions need converting into the gross hires they actually require.
- A requisition needs its justification, its classification, its budget basis, and its approval packet before it is opened.
- More than one plan scenario is live and the differences need making explicit.

## Do not use when

- The opening is already approved and the question is the level, family, band, or posting: `job-architecture-leveling-desk`.
- The plan exists and the question is why the funnel is not filling it: `sourcing-pipeline-desk`.
- The question is the merit budget, band refresh, or what the current population is paid: `compensation-review-cycle-desk`.
- The question is who could grow into a role and what is missing: `talent-review-succession-desk`.
- The attrition figure itself is the deliverable, with its definition and denominator going to a forum: `people-analytics-desk`.
- The reduction is real and named people are in scope: prepare the criteria and the pool here, then route the slate, the adverse impact read, and the notification sequence to `offboarding-separation-desk`.

## Required evidence

- Current headcount reconciled to the system of record on a stated date, with contractors, interns, employees on leave, and accepted-but-not-started hires each counted or excluded explicitly.
- The approved plan and the fiscal calendar it runs on, with the period each cost is expected to land in.
- Budget by org unit, with whether it is fully loaded or base only stated rather than assumed.
- Attrition history with its definitions: voluntary against involuntary, regretted against unregretted, what is counted, and whether the denominator is starting, average, or ending headcount.
- The org shape as spans and layers rather than as a chart, including which managers have no reports and which have fourteen.
- The work the plan is meant to deliver, at enough resolution to attach a role to it.
- Location, entity, and work arrangement constraints, including where a role can lawfully be employed and through which entity.
- The approval authority for headcount, for budget, for an org change, and for any reduction.

## Workflow

**Outcome.** A headcount plan by org unit, level, and location tied to the work it funds; a build against develop against contract disposition for every gap with the assumption behind it; the attrition assumption with its window and definitions; the requisition set with each opening classified as incremental, backfill, replacement, conversion, or reorganization and carrying its justification, budget basis, and approval state; the capacity gaps the plan does not close, stated rather than absorbed; and the scenario variants where more than one plan is live.

**Grounding.** Current headcount comes from the system of record on a named date, not from a chart or a distribution list. Attrition comes from a computed history with its definitions written out, not from a rate someone remembers. Budget comes from the approved figure with its basis, and an approval comes from a named approver with an authority level and a date. Where the plan's own count and finance's differ, both readings are recorded rather than reconciled toward the one that fits.

**Constraints.**

- A net plan is not a hiring plan. Net additions plus expected losses give the gross hires the plan actually requires, and the loss rate carries the window it came from and whether it separates voluntary from involuntary.
- Start dates are phased. A role approved for a period costs what it costs from the date someone actually starts, so a plan that books full-period cost for a role opening late overstates spend and a plan that books none understates the next period.
- The count is defined before it is planned. Contractors, interns, employees on leave, fixed-term staff, and accepted-but-not-started hires each move a headcount figure materially, and the same plan reads as growth or as flat depending on which are in it.
- Span and layer are outputs of the plan, not commentary on it. A plan that adds individual contributors without management capacity has made a decision about spans whether or not anyone wrote it down.
- Contract and employer-of-record engagements are not a cheaper version of a hire. They carry a different cost basis, a different notice position, and a classification risk where the working reality does not match the contracted basis, and that risk is named against the engagement.
- A backfill requested at a higher level than the vacated position is a reclassification wearing a backfill, and the comparison names the former incumbent's level and pay because that is what the argument turns on.

Requisition approval and budget precede any candidate engagement, and the order is mandated rather than procedural: a candidate engaged against an unapproved opening is a person being given a reason to resign by a company that may not be able to hire them, the cost lands on them, and it lands on the market's opinion of the company for years.

**Parallel surface.** Org units fan out and are parallel-safe: each unit's current count, gap analysis, build against develop against contract disposition, and requisition drafts are independent work. Scenario variants fan out against the same base. Location and entity feasibility checks fan out per location. Three passes are aggregate and run once after the fan-out returns: the total plan against the approved budget, because units compete for one pool; the span and layer read, because it is a property of the whole structure rather than of any unit; and the attrition-adjusted net, because losses in one unit are frequently backfilled from another.

**Acceptance bar.** Every planned position carries an org unit, a level, a location, a classification, and the work it exists to do. Current headcount carries its as-of date and its inclusion rules. Every rate carries its definition, its window, and its denominator. Every cost carries its basis and its fiscal period. Every requisition carries a named approver, an authority level, and a state, with nothing recorded as approved that was not.

## Outputs

A complete run delivers the set:

- `headcount-plan.md`: the plan by org unit, level, and location, with current reconciled count and its as-of date, planned additions with phased start assumptions, the build against develop against contract disposition per gap, and the work each position is funded to deliver.
- `requisition-set.md`: one entry per opening with its classification, its justification, the backfill comparison where it is a backfill, the budget approved and the fiscal period it lands in, the hiring manager and recruiter, the target start and what depends on it, and the approval state with the named approver and authority level.
- `plan-assumptions-and-capacity-gaps.md`: the attrition assumption with its window, definitions, and denominator; the span and layer read before and after; the capacity gaps in skills, levels, and locations the plan does not close; and the scenario variants with what separates them.
- `workforce-planning-downstream-handoff.md`: what `job-architecture-leveling-desk` inherits per opening, the approvals still outstanding, and the assumptions a later stage would otherwise treat as settled.

Depth standard: a plan entry is complete when a budget holder can approve it without asking a follow-up question. That means the count is reconciled and dated, the rate is defined, the cost carries its basis and period, the classification is argued rather than asserted, and a development or contract disposition names what makes it viable rather than recording a preference. A requisition entry states who approves it at what authority level, so the packet routes itself.

Where a reduction scenario is in scope, the selection criteria and the pool are prepared here, fixed and documented before any names are attached, and handed to `offboarding-separation-desk` for the slate, the adverse impact read, and the notification sequence. Where the system of record, the budget source, or the attrition history cannot be reached, `workforce-planning-diagnostic.md` names the system, what was attempted, and precisely which counts, rates, and cost figures are unavailable without it.

The hazard specific to this desk is arithmetic that closes. A headcount model is a grid, and a grid with an empty cell looks broken while a grid with a plausible number in it looks finished, so the pressure to populate is structural rather than occasional. An attrition rate carried over from last year's deck, a contractor count nobody pulled, a fully loaded multiplier applied because it is the usual one, a start date set to the first of the quarter because the model needed a date, and a budget described as approved because the conversation went well are all invisible inside a total that balances. Cells with no source read `not_reconciled`, `not_measured`, or `pending_approval` and stay that way in the total, and a plan that visibly does not add up because two units have not been counted is a more useful document than one that does.

## people_packet fields to update

- `workforce_plan`: `horizon`, `approved_headcount`, `current_headcount` with its as-of date and inclusion rules, `open_positions`, `attrition_assumption` with its window and definitions, `org_shape`, `build_buy_borrow`, `capacity_gap`, `budget_basis`, `scenario`.
- `requisition` per opening: `req_id`, `state`, `reason`, `backfill_of`, `headcount`, `fte`, `approval_state`, `approver`, `approved_at`, `budget_approved`, `hiring_manager`, `recruiter`, `target_start`, `priority`.
- `scope`: `org_unit`, `population_definition`, `period`, `as_of`, `confidentiality_tier`, `audience`.
- `jurisdiction[]` per planned location, with `employing_entity`, `employment_basis`, `collective_agreement` and its consultation trigger, and `classification_risk` where a contract engagement is proposed.
- `approvals[]` for headcount, budget, org change, and each requisition, with authority level and state.
- `metrics[]` where headcount, span of control, or attrition is reported, each with its written definition, population, denominator, and window.
- `source_facts` with as-of dates, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: a headcount plan, a budget, an org change, a conversion, or a reduction would be adopted, or a requisition opened. Each commits money the organization has to find, and in a reduction it commits the jobs of named people. A plan circulating as approved starts hiring conversations, reorganization rumours, and retention risk that no later correction reverses.
- **Production or destructive**: the next act would create or change a requisition in the applicant tracking system, alter a position record, or notify anyone that a role is being added, held, or removed.
- **Security or privacy**: a plan would name individuals in a reduction pool, a flight risk, or a role marked for elimination in a document reaching an audience not entitled to it, or would circulate pay for identifiable individuals as part of a cost model.
- **Source conflict**: the system of record, finance's headcount, and the manager's own count disagree, or the approved budget and the plan's cost basis are computed on different footings. Record every reading with its as-of date and route the conflict rather than adopting the one that balances.
- **Release integrity**: a headcount, an attrition rate, or a cost figure would go to a board, a budget forum, or a works council without its definition, population, denominator, and basis.
- **Connector unreachable**: the system of record, the payroll or budget source, or the attrition history exists and cannot be read, so the plan's baseline would describe an organization nobody observed.

An unconfirmed start date, a role whose level is not yet placed, a location not yet cleared for employment, and a development plan without a named owner are soft gaps. Proceed with the assumption labeled against the position it affects and record the question.

## Downstream handoffs

`job-architecture-leveling-desk` takes each approved opening and places it against the level guide, which every band, offer, and later comparable-work cohort inherits. `sourcing-pipeline-desk` takes the requisition set with its priorities and target starts. `compensation-review-cycle-desk` takes the plan's cost basis and the population it grows. `talent-review-succession-desk` takes the develop dispositions as named development commitments. `people-analytics-desk` takes the plan's definitions so the figures reported later mean the same thing. `offboarding-separation-desk` takes the reduction criteria and pool where one exists.

## Quality bar

A good plan is one a finance partner and a hiring manager can both work from without either recomputing it. Its baseline is a reconciled count on a stated date with its inclusion rules visible, not a number from a chart. Its growth rate is defined in the same terms the reporting layer will use later, so next year's variance is a real variance rather than a definitional one. Each opening reads as work that needs doing rather than as a level someone wants, and each backfill states the level and pay of what it replaces. The develop and contract dispositions are argued, not used as a place to put the roles nobody funded. And the plan's own gaps are on the page: the location with no entity, the skill nobody has, the manager already carrying twelve reports. A plan that is honest about what it does not cover is the one that survives the quarter it was written for.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
