# People Talent Command Desk

Source Markdown suite for the people and talent function. One orchestrator routes and runs; nineteen member desks own a real stage of the work.

The subject of this suite is people: what a role is worth, who gets hired into it, what they are told about how they are doing, what they are paid for it, what happens when something goes wrong, and how they leave. The failure it exists to prevent is the coherent, sympathetic, well-structured paragraph about a named human being that no record supports, filed as though it were a record and produced two years later in a hearing where the only questions are what was documented at the time and on what date.

Two facts shape everything in here. The rules are local: pay range disclosure, notice, final pay timing, leave entitlement, consultation obligations, lawful interview questions, and retention all change with the jurisdiction of employment, and the jurisdiction that binds is the employee's rather than the company's. And the records are effective-dated: a level, a manager, a pay figure, and a policy are each true as of a date, so a people fact carried without its date is not yet a fact.

The suite covers the function end to end: workforce planning and headcount, job architecture and leveling, sourcing and pipeline, structured interview design, candidate evaluation and debrief, offers and compensation, onboarding, people operations records, performance review and calibration, career frameworks and progression, talent review and succession, manager enablement, engagement and retention, compensation review cycles and pay equity, policy and handbook, employee relations, leave and accommodation, offboarding and reductions in force, and people analytics.

Employment law interpretation, works council consultation, and agreement drafting belong to the Legal suite; this suite brings the facts and the dates. Employee and candidate data handling, retention, and subject requests belong to the Privacy suite. Access provisioning, access revocation, and any investigation that requires reading systems or devices belong to the Security suite. Headcount cost, payroll accounting, and budget reconciliation belong to the Finance suite, which owns the money view of the same headcount this suite plans.

## Desks in workflow order

- `people-talent-command-desk.md` (orchestrator)
- `workforce-planning-desk.md`
- `job-architecture-leveling-desk.md`
- `sourcing-pipeline-desk.md`
- `structured-interview-design-desk.md`
- `candidate-evaluation-debrief-desk.md`
- `offer-compensation-desk.md`
- `onboarding-desk.md`
- `people-operations-records-desk.md`
- `performance-review-calibration-desk.md`
- `career-framework-progression-desk.md`
- `talent-review-succession-desk.md`
- `manager-enablement-desk.md`
- `engagement-retention-desk.md`
- `compensation-review-cycle-desk.md`
- `policy-handbook-desk.md`
- `employee-relations-desk.md`
- `leave-accommodation-desk.md`
- `offboarding-separation-desk.md`
- `people-analytics-desk.md`

The first two make a role real: the headcount that funds it and the definition that levels it. The next four are the hire, from channel to signed offer. The next two are the join: the first ninety days, and the record that turns an accepted offer into an employee. The next six are the employment cycle, where people are assessed, progressed, succeeded, managed, engaged, and paid. The next three are the obligation layer the cycle keeps colliding with: the policy, the case, and the leave. Then the exit. Then the measurement that decides which of the eighteen stages above changes next year.

## How to start

Start at `people-talent-command-desk` and describe the outcome rather than the stage. Name the role, the person, the cohort, or the cycle, say what decision is waiting on the answer, say which location the person is employed in, and say whether a clock is running such as a notice period, a leave window, a release consideration period, or a posting that is already live.

Enter a member desk directly when the stage is already settled: a level placement when a title and a band disagree, an interview rubric before the loop runs, an offer model before the number is spoken out loud, a calibration input pack before the session, a policy draft before it reaches a works council, or a metric definition review before the figures go to a board.

Examples: "this req says senior but the band says otherwise, level it against the guide and tell me what the offer can actually be", "design the loop and rubric for this role and tell me what we cannot lawfully ask in each location we can hire in", "run the merit model against this budget and show me where it creates compression", "a manager wants to move someone out next week, tell me what is actually documented", "our attrition is up two points, find whether that is company-wide or two teams", "we are opening in a new country, tell me which handbook provisions do not survive the move".

This suite plans, levels, designs, models, drafts, investigates, and reports. It does not extend offers, communicate ratings or pay changes, issue discipline or terminations, publish policies or postings, write to the systems of record, send anything to candidates or employees, revoke access, or approve leave; it prepares the exact item with the approval it needs and stops at the gate.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `people_packet`, the operating modes, request types, the source hierarchy, evidence discipline, the action boundary, the mandated sequences, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.

Authoring convention: suite folders are human-readable product taxonomy, desk files are kebab-case and end in `.md`, and packaged {{AGENT}} skill folders under `_skills/` are generated artifacts rather than the primary authoring structure.

Most requests run a subsequence of the chain and enter partway. Requisitions in a plan, roles being leveled, candidates in a pipeline, scorecards in a loop, employees in a review population, managers in a cohort, jurisdictions being checked against one policy, and verbatims being themed all fan out in parallel; calibration, merit allocation, pay equity, a reduction in force slate and its adverse impact read, survey suppression across a cut set, and headcount reconciliation are each one pass over the whole set, and an employee relations investigation is sequential because each interview determines the next.
