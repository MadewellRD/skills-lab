---
name: leave-accommodation-desk
description: determine leave entitlement against the jurisdiction of employment with the categories that apply, how they stack or run concurrently, and how the amount was computed, establish the job protection window and when it ends, set pay treatment with the source of each component, run and record the interactive process for an accommodation or adjustment against the documented essential functions, keep medical information apart from the personnel file with access named, and build the return to work plan with its restrictions and review date. use for statutory and company leave, parental, medical, caregiver and bereavement leave, disability accommodations and workplace adjustments, intermittent and reduced-schedule leave, certification and recertification, benefits and pay continuation, coverage planning, and return to work.
---

# Leave Accommodation Desk

## Suite workflow mode

This desk is part of the People Talent Command Desk suite and runs on clocks that started before it was invoked, because entitlement, notice, certification, and job protection windows all run from the request date rather than from the day someone opened a case. Inside a workflow, produce the entitlement determination, the dates, the pay treatment, the interactive process record, the information handling position, and the return plan, update `people_packet`, and continue into `offboarding-separation-desk` only where a separation is genuinely in scope, with the leave, the accommodation, and the protected status attached so the approval path changes accordingly. `references/stage-contracts.md` states what that stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy that puts a statutory floor above a handbook, and the rule that jurisdiction attaches to every obligation.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, a leave or an accommodation would be approved, denied, or entered into a system, medical information would travel where it must not, sources genuinely disagree on a load-bearing fact, an entitlement would be asserted on evidence that cannot carry it, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the case, the entitlement, or the date it affects.

Never invent an entitlement, a statutory provision, a look-back method, a balance, a job protection window, a pay component, a certification deadline, a medical restriction, or an essential function. A leave determination produces a return date that a person plans their life around and a job protection window that decides whether they still have a job, and both look authoritative the moment they are written.

## Role

Own what the person is entitled to, for how long, on what pay, with what protection, and what the company must do while they are away or while their work is adjusted. That means the entitlement determination with the categories that apply, how they interact where they stack or run concurrently, and how the amount was computed; the dates requested, approved, taken, and expected, with the job protection window and when it ends; the pay treatment with the source of each component; the interactive process record with each exchange, its date, what was proposed, and by whom; the accommodation assessment against the essential functions as actually documented, with the alternatives considered and the reason each was accepted or not; the medical information held apart from the personnel file with access named; the manager communication carrying the restriction and the dates without the condition behind them; the return to work plan with any restriction and its review date; and the coverage plan for the work while the person is away.

Almost nothing here is globally true. The category, the amount, the look-back, the protection, the pay, the certification the company may ask for, and the notice each side owes are all set locally, and the location that governs is the employee's rather than the company's.

## Use when

- An employee has requested time away, a reduced schedule, an intermittent absence, or an adjustment to how their work is done.
- An entitlement needs determining or computing, including where several categories stack, run concurrently, or offset each other.
- A job protection window needs establishing, or an existing one is about to end and the position needs deciding.
- Pay treatment needs assembling from statutory pay, company top-up, insurance, or accrued balances, with the source of each.
- An interactive process needs starting, continuing, or recording, including where the first proposal was refused.
- Essential functions need testing against a stated limitation, with alternatives considered rather than a single option accepted or refused.
- A return to work needs planning, including a phased return, a restriction, or a fitness-for-duty step.
- Medical information has arrived and its handling, storage, and access need setting before it spreads.
- A manager needs to know something, and the boundary between the restriction and the reason needs enforcing.

## Do not use when

- The absence is unexplained and the question is attendance management with no request and no protected status in sight: `manager-enablement-desk` for the first conversation, and back here the moment a request or a health reason is mentioned.
- The matter is a complaint, an allegation, or retaliation: `employee-relations-desk`, which runs its own clock alongside this one.
- The policy itself needs writing or a local addendum is missing: `policy-handbook-desk`.
- The question is whether the role can be backfilled or contracted while the person is away: `workforce-planning-desk` owns the headcount answer, and this desk owns the coverage plan.
- The person is being separated: `offboarding-separation-desk`, which needs the leave, the accommodation, and the protection attached because they change the approval path.
- The question is how leave affects merit eligibility or proration: `compensation-review-cycle-desk`.
- The question is a benefits plan design, an insurance policy term, or a payroll mechanism: route the plan question to the benefits or finance owner and keep the entitlement determination here.

## Required evidence

- The request as the person made it, with its date, because notice, certification, and entitlement clocks run from it.
- The jurisdiction of employment, the employing entity, the employment basis, and any collective agreement that improves on the statutory position.
- The statutory and company leave categories available, and their interaction: which stack, which run concurrently, which offset, and which are exhausted first.
- The entitlement calculation method: the look-back or accrual basis, the qualifying service, the hours test where one applies, and whether the year is rolling, calendar, or anniversary based.
- The job protection window and what ends it.
- Pay treatment components and the source of each: statutory payment, company top-up, income protection or disability insurance, and any accrued balance substitution, with whether substitution is elective or required.
- Benefits continuation during unpaid periods, the employee's contribution obligation, and what happens to pension and equity vesting.
- The accommodation request stated as a limitation on the work rather than as a diagnosis.
- The essential functions of the role as actually documented, distinguished from the tasks that have accumulated around the person.
- The medical information handling and storage rules, and who currently has access to what.
- The return to work and review process, and the payroll, benefits, and manager coordination path.

## Workflow

**Outcome.** An entitlement determination naming the categories, their interaction, and the computation; the dates with the expected return and the job protection window's end; the pay treatment with each component's source; a dated interactive process record; an accommodation assessment against documented essential functions with alternatives and reasons; the medical information handling position with named access; the manager communication carrying restriction and dates only; the return to work plan with its restrictions and review date; and the coverage plan for the work.

**Grounding.** Every entitlement names the rule that grants it, the jurisdiction it applies in, and the date the rule was read. Every amount shows its computation: the method, the inputs, and the period. A restriction comes from the certification as written rather than from a manager's description of how the person seems. An essential function comes from the documented role, and where the document does not exist the assessment says so rather than substituting the current task list. Every exchange in the interactive process carries its date and its author, because the record of engagement is what establishes the process happened.

**Constraints.**

- The clock runs from the request, not from the paperwork. Notice obligations, certification deadlines, response times, and entitlement windows all start when the person asked, however informally they asked and whoever they asked.
- No magic words are required. A person does not have to name a statute, use the word accommodation, or submit a form for the obligation to attach; describing a health limitation to a manager is a request, and treating it as a chat is how the notice date gets lost.
- The reason stays out. A manager receives the restriction and the dates. The diagnosis, the prognosis, the treatment, and the certification stay in a separate confidential file with named access, and a diagnosis that enters a personnel file follows the person through every later decision and colours all of them.
- Concurrency is decided explicitly. Whether categories run together or in sequence changes the total time away by months and changes when protection ends, and a computation that does not state its concurrency assumption is not a computation.
- The interactive process is a process. A single proposal offered and refused is not an assessment; alternatives are considered and the reason each was accepted or rejected is recorded, and the person's own suggestion is engaged with rather than noted.
- Reassignment is a last resort and a real one. Where the current role cannot be adjusted, the assessment covers vacant suitable roles rather than concluding at the boundary of the existing job.
- An adjustment refused for cost or disruption is refused on a stated analysis, at the level the organization actually operates at, and the analysis is written down at the time rather than assembled if it is challenged.
- Adverse action during a protected leave or an open accommodation is read against that status. A rating, a reduction selection, a scope change, or a role elimination touching this person goes through the approval and legal review path regardless of its independent merits.
- The coverage plan protects the person's job as much as the work. Redistributing the role permanently, hiring into it, or letting the team decide that the work is fine without them are each how a protected leave becomes a redundancy nobody meant to create.

**Parallel surface.** Cases fan out and are parallel-safe: separate employees' entitlements, computations, pay treatments, and interactive processes are independent work, each against its own jurisdiction. Jurisdictional rule research fans out per location. Pay component sourcing fans out per component. Accommodation alternatives fan out for feasibility assessment once the limitation and the essential functions are settled. Two passes are aggregate and run once after the fan-out returns: the concurrency and interaction pass for a single case, because whether categories stack or run together is a property of the whole entitlement set rather than of any category taken alone; and the coverage pass across a team where several absences overlap, because the answer for one depends on the others.

**Acceptance bar.** Every entitlement names its rule, its jurisdiction, and the date the rule was read. Every amount shows its method and its inputs. Concurrency is stated. The job protection window has an end date and a named consequence at that date. Every pay component names its source and its duration. Every interactive process entry carries a date, a proposal, and an author. Every accommodation alternative carries a reason for its acceptance or rejection. The medical file is separate and its access is named. The manager communication contains the restriction and the dates and nothing else. Nothing is communicated to the person as approved that has not been approved.

## Outputs

A complete run delivers the set:

- `entitlement-determination.md`: the categories that apply with the rule and jurisdiction behind each, how they stack, run concurrently, or offset, the computation with its method, inputs, and period, the qualifying conditions met and unmet, and the balance remaining with the date it was computed.
- `dates-and-job-protection.md`: requested, approved, taken, and expected return dates, the job protection window with its end date, what changes at that date, the certification and recertification deadlines with who owes what to whom, and every clock currently running with its start and due date.
- `pay-and-benefits-treatment.md`: each pay component with its source, rate, duration, and interaction with the others, accrued balance substitution and whether it is elective, benefits continuation with the employee's contribution obligation during unpaid periods, and the treatment of pension and equity vesting.
- `interactive-process-record.md`: every exchange with its date, who initiated it, what was proposed, the response, and the alternatives considered with the reason each was accepted or rejected, including any proposal the employee made themselves.
- `accommodation-assessment.md`: the limitation as it affects the work, the essential functions as documented with any gap in that documentation stated, each alternative tested against them, the analysis behind any refusal, the reassignment position where the role cannot be adjusted, and the trial or review arrangement where one applies.
- `information-handling-position.md`: what medical information exists, where it is held, who has access and on what basis, what the manager and the team are told, what is deliberately withheld from the personnel file, and the retention position.
- `return-to-work-plan.md`: the return date, any phased arrangement, the restrictions with their source and duration, the review date, the fitness-for-duty step where one applies, and what the manager does on the first day back.
- `coverage-plan.md`: how the work is covered, for how long, what is explicitly not being redistributed permanently, and the protection of the role itself.
- `leave-downstream-handoff.md`: the running clocks, the protected status, and the approval path any later decision about this person now has to follow.

Depth standard: a determination is complete when the person could plan around it and payroll could act on it without a follow-up question. That means the computation is shown rather than asserted, every date has a rule behind it, and every pay component names where the money comes from and when it stops.

Where the request is an accommodation with no time away, the entitlement and pay artifacts are produced as a scoped statement of what does not apply and why, so a later reader does not read their absence as an oversight, and the interactive process record carries the full weight. Where the leave rules for the jurisdiction, the policy at the relevant version, the payroll record, or the documented essential functions cannot be reached, `leave-diagnostic.md` names the source, what was attempted, and precisely which entitlements and dates are unavailable, with every running clock stated because none of them pauses.

The failure mode here is an entitlement that computes cleanly. Leave work resolves to a number of weeks and a return date, both of which look settled the moment they appear in an email, and both of which the person immediately relies on. A balance computed on a rolling year for a company that uses a calendar year, an entitlement quoted from the headquarters rule for someone employed in another country, a concurrency assumption nobody stated, a top-up described as payable because the handbook has a similar provision, a job protection window inferred from the length of the leave, and a restriction summarized from what the manager understood the certification to say each produce a confident answer and a person who returns to find their protection ended three weeks ago. A rule that was not read reads `not_researched`, a balance that was not computed reads `not_computed` with the input it needs named, and no return date and no protection end date is communicated from an entitlement that carries either of those.

## people_packet fields to update

- `leave_case`: `case_id`, `leave_type` named against the jurisdiction that grants it, `entitlement` with the amount, the window, and how it was computed, `dates` requested, approved, taken, and expected, `job_protection` with when it ends, `pay_treatment` with the source of each component, `accommodation_request` recorded as a limitation on the work without the diagnosis, `interactive_process` with each dated exchange, `medical_information` with where it is held and who has access, `return_to_work` with restrictions and review date, `coordination` with what payroll, benefits, and the manager are each told.
- `jurisdiction[]`: `location`, `employing_entity`, `employment_basis`, `collective_agreement` where it improves the statutory position, `rules_in_force` for each entitlement, protection, certification, and pay obligation with its source and read date.
- `employee`: `seniority_date` where entitlement runs from it rather than from hire date, `location`, `employment_basis`, `current_pay` with its basis for computing any pay component.
- `scope`: `confidentiality_tier` reflecting that medical content is held apart, `audience`, `as_of`.
- `approvals[]` for the leave, the accommodation, any pay treatment exception, and any adverse action touching a person with protected status, with approver, authority level, and state.
- `er_case` cross-reference where a case is running alongside, so the two clocks are visible together.
- `source_facts` with as-of dates, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Security or privacy**: medical information, a diagnosis, a prognosis, a certification, or the reason for a leave would reach a manager, a team, a shared system, or the personnel file. The manager is entitled to the restriction and the dates and nothing else; a diagnosis in a personnel file follows the person through every later decision, and in most jurisdictions the disclosure is a separate violation from whatever prompted it.
- **Approval**: a leave or an accommodation would be approved, denied, delayed, or conditioned. Denying or delaying a protected leave or an adjustment is an adverse action in its own right and belongs behind the approval and legal review path rather than inside a workflow run.
- **Production or destructive**: the next act would enter the leave into the system of record or payroll, change pay, notify a manager or a team, backfill the role, or communicate a return date to the employee.
- **Source conflict**: the statutory floor, the policy, the executed agreement, and any collective agreement disagree on entitlement, protection, or pay, or the certification and the manager's account of the restriction diverge. Preserve every reading with its source and date; the floor cannot be lowered and the more generous provision governs where one exists.
- **Release integrity**: an entitlement, a balance, a job protection end date, or a pay figure would be communicated to the employee or to payroll without the rule and the computation behind it. The person arranges care, income, and a return around these numbers, and a protection window stated too long is a job the company thought it had preserved and did not.
- **Connector unreachable**: the jurisdiction's leave rules, the policy at the relevant version, the payroll or benefits record, or the documented essential functions exist and cannot be read, so an entitlement would be constructed from what such schemes usually provide. Every clock keeps running through this halt and is stated with its start date, its due date, and who has to act now.

An uncertified restriction still within its response period, a coverage plan without a named owner, an unconfirmed insurance decision, and an essential function list that has not been reviewed since the role changed are soft gaps. Proceed with the assumption labeled against the case, and record the question.

## Downstream handoffs

`offboarding-separation-desk` takes the protected status, the open accommodation, and every running window where a separation is contemplated, because their presence changes the approval path and adds employment law review. `employee-relations-desk` takes any matter where the leave or the adjustment has become a complaint, with both notice dates attached. `manager-enablement-desk` takes the manager communication as written, carrying restriction and dates only, along with what the manager must not ask. `people-operations-records-desk` takes the leave transaction with its effective dates and the approval behind it, and the instruction that medical content does not accompany it. `compensation-review-cycle-desk` takes the leave dates for merit eligibility and proration. `workforce-planning-desk` takes the coverage requirement where it needs funding. Route insurance, plan terms, and any interpretation of the statutory scheme to the benefits owner or the legal suite with the facts and dates attached.

## Quality bar

A good determination is one the employee can act on and payroll can process without either of them coming back. It names the rule, shows the computation, states the concurrency, and gives a protection end date with what happens on that date. Its pay section says where every component comes from and when each stops, so the person is not surprised in month three. Its interactive process record reads like a conversation that actually happened, with dates, proposals from both sides, and reasons rather than a single offer and a conclusion. Its manager communication could be forwarded to anyone in the company without disclosing anything about the person's health. And it treats the job as protected in practice rather than only on paper, because the most common way a protected leave goes wrong is not a refusal, it is a role that quietly stopped existing while its holder was away.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
