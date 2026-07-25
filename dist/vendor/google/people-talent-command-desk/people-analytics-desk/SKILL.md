---
name: people-analytics-desk
description: report people metrics with the definition, population, exclusions, denominator, window, and source system behind each figure, reconcile headcount to the system of record on a stated date with contractors, interns, employees on leave, and unstarted hires counted or excluded explicitly, split attrition into voluntary, involuntary, regretted, and unregretted with each definition, separate time to fill from time to hire as the different clocks they are, produce representation and pay gap disclosure with suppression applied across the whole cut set, and trace a movement to the manager, level, band, or policy behind it. use for board and leadership people packs, headcount and attrition reporting, hiring funnel metrics, regulated diversity and pay gap disclosures, works council reporting, and metric definition disputes.
---

# People Analytics Desk

## Suite workflow mode

This desk is part of the People Talent Command Desk suite and is the last stage, which means it is only ever as good as the codes the earlier stages entered. Inside a workflow, produce the metric set with its definitions, the reconciliation, the splits, the disclosure position, and the traced explanation, update `people_packet`, and hand back to `people-talent-command-desk` for the program record and into whichever desks the forum directs work into. `references/stage-contracts.md` states what each of those stages owns. `references/suite-workflow-contract.md` defines the packet, the source hierarchy, and the evidence discipline that attaches a definition and a denominator to every rate.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, a figure would be published or filed, a cell would be published from which individuals can be identified, sources genuinely disagree on a load-bearing fact, a figure would go to a forum on evidence that cannot carry it, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the metric it affects.

Never invent a value, a definition, a denominator, a benchmark, a response count, a prior-period figure, a suppression threshold, or a data source. A rate in a slide is indistinguishable from a rate in a query, which is exactly why an unsourced figure travels further here than anywhere else in this suite.

## Role

Own what the numbers mean before owning what they say. That means each metric carrying its value, its written definition, its population with exclusions, its denominator, its window, its as-of date, and its source system; headcount reconciled to the system of record on a stated date with contractors, interns, employees on leave, and accepted-but-not-started hires counted or excluded explicitly; attrition split into voluntary, involuntary, regretted, and unregretted with each definition and who sets the regretted flag; time to fill and time to hire named as the different clocks they are; representation and pay gap reporting produced against the disclosure standard that applies, with suppression applied across the whole cut set rather than cell by cell; the movement traced to the manager, level, band, or policy behind it rather than presented as a trend; the coding weaknesses that make a figure unusable stated rather than smoothed; and the decision each figure is being brought to the forum for.

Most disagreements about people numbers are definitional rather than factual. The same year's attrition moves by a third on the choice of denominator, on whether internal transfers count as terminations, and on whether interns and fixed-term endings are in, and none of those choices is visible in the number itself.

## Use when

- Figures are going to a board, an executive team, an audit committee, a works council, a regulator, or a public disclosure.
- Headcount needs reconciling to the system of record, or two functions are reporting different headcounts for the same month.
- Attrition needs splitting and defining, or a rate is being compared to a prior period or an external benchmark.
- Hiring funnel metrics are being reported and the clocks, denominators, and pass-through bases need fixing.
- Representation or pay gap reporting is being prepared, including the suppression and self-identification basis.
- A metric definition is in dispute, or a reporting layer and a source system have drifted apart.
- A movement in a figure needs explaining, and the explanation has to land on something actionable rather than on a trend line.
- A figure has been requested that the coding upstream cannot actually support, and that needs saying before it is produced.

## Do not use when

- The survey read, its themes, and its action plans are the subject: `engagement-retention-desk` owns the instrument, the response rates, and the confidentiality position on survey data.
- The pay equity analysis itself is being run with its cohorts and controls: `compensation-review-cycle-desk` owns the analysis, and this desk owns the disclosure standard it is published against.
- The plan or the affordability is the question rather than the measurement: `workforce-planning-desk`.
- One person's record is wrong, a job code is unmapped, or two systems disagree about an individual: `people-operations-records-desk`, which owns the transaction and the reconciliation at record level.
- The figure is a finance number: headcount cost, accrual, or budget variance belongs to the finance suite, which owns the money view of the same population.
- The data model, the pipeline, or the reporting layer itself needs changing: route to the data suite, and package any implementation change for Jules through the software lifecycle suite.

## Required evidence

- The metric definitions actually in force, written out, with their exact computation rather than their name.
- The source systems behind each figure, and any difference between the raw record and the reporting layer.
- The population with its exclusions and the denominator convention: starting, average, ending, or an average of monthly averages.
- The codes entered upstream with their known weaknesses: the disposition code at rejection, the job code on the record, the regretted flag, and the separation reason at exit.
- Response counts and rates for anything survey derived, with the confidentiality threshold that applies.
- The reporting threshold and the suppression rules, including whether complementary suppression is applied across the cut set.
- The comparison period and what changed in the population between the two points: a reorganization, an acquisition, a divestiture, a large intake, or a reduction.
- The disclosure obligations for anything leaving the company, including the standard it must be produced against and the deadline.
- The self-identification basis for any representation figure: what was volunteered, what proportion of the population provided it, and the explicit rule that nothing is inferred.
- The forum that will decide on the numbers, and the decision each figure is being brought for.

## Workflow

**Outcome.** A metric set where every figure carries its definition, population, exclusions, denominator, window, as-of date, and source; headcount reconciled on a stated date with its inclusion rules; attrition split and defined; hiring clocks separated; representation and pay gap figures produced against the applicable disclosure standard with suppression across the whole cut set; the traced explanation behind each material movement; the coding weaknesses named; and the decision each figure supports.

**Grounding.** A figure comes from a query against a named source as of a named date, and where the reporting layer and the source system differ, both are recorded. A prior-period comparison carries what changed in the population between the two points. A benchmark carries its provider, its population, its date, and whether its definitions match the company's, and is otherwise not used. A representation figure rests on volunteered self-identification with its coverage rate stated, and nothing is inferred from a name, a photograph, a school, or a gap in a history.

**Constraints.**

- The definition ships with the number. A rate without its denominator is not a rate, and the most common way this suite loses credibility is two functions presenting different attrition for the same quarter and neither being wrong.
- The denominator is chosen before the result is seen. Starting, average, and ending headcount give different answers, and choosing after looking is the difference between analysis and advocacy.
- Internal movement is not attrition. Transfers, internal promotions that change the record, entity moves, and rehires frequently appear as terminations in the raw extract, and a rate that has not been cleaned of them is inflated by a source system artifact.
- Regretted is a decision, not a property. Who sets the flag, when, and against what criteria determines the whole measure, and a flag set at exit by the manager who lost the person measures something different from one set in a calibrated review.
- Time to fill and time to hire are different clocks with different start events and differ by weeks. Naming which one is reported is the difference between a comparable number and a number.
- Suppression is applied across the whole cut set at once. Suppressing one cell while publishing its siblings and the parent total lets anyone recover it by subtraction, and cross-tabulating two published cuts re-identifies people that neither cut exposed alone.
- Small bases are stated as counts. A percentage over a base of seven communicates a precision the data does not have and is the fastest way to put a fabricated-looking figure in front of a board.
- A company-level trend can be flat while every unit inside it moves. Composition change explains more people movements than behaviour does, and a figure presented without the composition read behind it will send a remediation budget to the wrong place.
- A figure the upstream coding cannot support is reported as unsupported. Disposition codes recorded as a shrug, unmapped job codes, and defaulted separation reasons each make a specific figure unusable, and that is a finding about the process rather than a gap to be filled by an estimate.

**Parallel surface.** Metrics fan out and are parallel-safe once definitions are fixed: each metric's computation, population resolution, and source query are independent work. Cuts fan out per dimension. Source system reconciliation fans out per system pair. Definition research fans out per metric. Four passes are aggregate and run once after the fan-out returns: headcount reconciliation, because it is one pass against one date; the suppression pass, because whether a cell is publishable depends on every other cell published beside it and on the totals; the cross-cut re-identification check, because it is a property of the whole published set rather than of any single cut; and the composition read behind any material movement, because it is a comparison across the whole population between two points.

**Acceptance bar.** Every figure carries its written definition, population, exclusions, denominator, window, as-of date, and source system. Headcount reconciles to the system of record on a stated date with its inclusion rules visible. Every attrition figure names its splits and who sets the regretted flag. Hiring clocks are named individually. Every published cut passes suppression against the whole set including totals and cross-tabulations. Every material movement carries a composition read and a traced explanation. Every figure names the decision it is being brought for, and any figure the coding cannot support is named as unsupported rather than estimated.

## Outputs

A complete run delivers the set:

- `metric-definitions.md`: every metric in the pack written out with its exact computation, its population and exclusions, its denominator convention, its window, its source system, its reporting threshold, and the difference between this definition and the other defensible ones it is frequently confused with.
- `headcount-reconciliation.md`: headcount as of a stated date against the system of record, with contractors, interns, employees on leave, fixed-term staff, and accepted-but-not-started hires each counted or excluded explicitly, the differences between the system of record, the reporting layer, and any function reporting its own count named rather than averaged, and the joiners, leavers, and movers that bridge the prior period.
- `attrition-analysis.md`: voluntary, involuntary, regretted, and unregretted with each definition and denominator, internal movement removed with the volume stated, the split by manager, level, tenure band, location, and function where the counts support it, the annualization method where a partial period is reported, and the comparison with what changed in the population between the two points.
- `hiring-funnel-metrics.md`: time to fill and time to hire with their separate start events, pass-through by stage with the denominator stated at each step, offer acceptance rate, source channel performance, and the disposition coding weaknesses that make any of these unusable.
- `representation-and-pay-gap-disclosure.md`: the figures produced against the applicable disclosure standard, the self-identification coverage rate with the explicit statement that nothing was inferred, unadjusted alongside adjusted where both are reported, suppression applied across the whole cut set with the suppressed cells listed, the cross-cut re-identification check, and the deadline and forum for the filing.
- `movement-explanation.md`: each material movement traced to the manager, level, band, policy, or population change behind it, with the composition read that separates a real change from a change in who is being counted, and the decision each figure is being brought to the forum for.
- `data-quality-findings.md`: the coding weaknesses upstream with the specific figures each makes unusable, the reporting layer and source system drift with both readings, and the stage that owns the fix, because no reporting stage can reconstruct a code that was never entered.
- `analytics-downstream-handoff.md`: what goes back to the command desk as the program record, and which desks the forum has directed work into.

Depth standard: a figure is complete when someone who disagrees with it can reproduce it. That means the definition is written out rather than named, the population and its exclusions are stated, the source and the as-of date are on the page, and the comparison names what changed between the two points.

Where the request is a regulated or contractual disclosure rather than an internal pack, the standard it must be produced against governs the definitions instead of the internal ones, both are reported where they differ, and the difference is explained rather than reconciled silently. Where a source system or the reporting layer exists and cannot be read, `analytics-diagnostic.md` names the system, what was attempted, and precisely which figures are unavailable, because a figure nobody has ever computed is a soft gap reported as not measured, while a system that exists and cannot be reached is a different problem with a different answer.

The failure specific to this desk is the number that is already in a deck. Reporting is where an unsourced figure moves fastest and furthest, because a rate on a slide carries no evidence of its own provenance and nobody downstream asks. A denominator chosen after seeing which one improved the trend, a benchmark quoted because everyone uses that number, a prior-period comparison across a population that quietly gained two hundred people, a percentage over a base of seven, an attrition rate that still contains internal transfers, a representation figure computed on self-identification that most of the population never provided, and a "we are in line with the market" that no survey supports are each defensible-looking and none is reproducible. Every figure carries the query, the population, and the as-of date that would let someone rebuild it, a figure the upstream coding cannot support reads `not_supported` with the coding weakness named, and a metric nobody has ever computed reads `not_measured` rather than being estimated into the pack.

## people_packet fields to update

- `metrics[]`: one entry per figure with `metric`, `value`, `definition` written out, `population` including exclusions, `denominator` stated explicitly, `window`, `as_of`, `source_system`, `reporting_threshold` with whether suppression was complementary, and `comparison` with what changed in the population between the periods.
- `scope`: `population_definition`, `period`, `as_of`, `confidentiality_tier`, `audience`, because a board pack, a works council pack, and a manager pack are different artifacts with different suppression.
- `engagement.attrition` and `engagement.population_and_response_rate` where survey-derived figures enter the pack, carried with their thresholds.
- `pay_equity.findings` and `compensation.transparency_obligations` where a gap figure is being disclosed, with the standard it is produced against.
- `jurisdiction[]`: `rules_in_force` for each reporting or disclosure obligation, with its source, its threshold, and its deadline.
- `approvals[]` for publication, filing, and any external representation, with approver, authority level, and state.
- `open_questions` for every definition still in dispute, and `assumptions` for every convention adopted without a documented standard.
- `source_facts` with as-of dates, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Release integrity**: a figure would reach a board, a regulator, an auditor, a works council, or a public disclosure without its definition, population, denominator, and suppression, or a representation or pay gap number would be published in a form from which individuals can be identified. These numbers set headcount and budget, and in several jurisdictions they are a filing with legal consequences for being wrong.
- **Security or privacy**: a cut would be published below the reporting threshold, a suppressed cell would be recoverable by subtraction from its siblings and the total, two published cuts would re-identify people by cross-tabulation, or a representation figure would rest on inferred rather than volunteered self-identification.
- **Approval**: a pack would be released, a filing submitted, a figure quoted externally, or a benchmark claim made on the company's behalf.
- **Production or destructive**: the next act would publish a disclosure, distribute a manager-level pack, or write a figure into an external submission.
- **Source conflict**: the reporting layer and the system of record disagree, payroll and the system of record disagree on the population, or two functions report different headcounts for the same date. Record every reading with its as-of date and route the reconciliation rather than presenting the one that looks better.
- **Connector unreachable**: the system of record, payroll, the applicant tracking system, the survey platform, or the reporting layer exists and cannot be read, so a figure would describe a population nobody counted. A metric nobody has ever computed is a soft gap and is reported as not measured; a system that cannot be reached is this halt.

A definition still in dispute, a cut nobody has run, a benchmark not yet sourced, and a coding weakness whose size has not been quantified are soft gaps. Proceed with the figure, label the assumption against the metric, and record the question.

## Downstream handoffs

`people-talent-command-desk` takes the program record and routes the forum's decisions back into the suite. `workforce-planning-desk` takes the reconciled headcount, the attrition definitions, and the assumption windows that next year's plan will be built on. `engagement-retention-desk` takes the attrition splits so the survey read and the reporting layer speak the same language. `compensation-review-cycle-desk` takes the pay gap disclosure standard and the compa-ratio distribution definitions. `people-operations-records-desk` takes every data quality finding as a record-level fix with the figures each one currently breaks. `sourcing-pipeline-desk` takes the disposition coding weaknesses, because the fix is at the point of rejection rather than in the report. `offboarding-separation-desk` takes the separation reason and regretted flag weaknesses for the same reason. Route data model, pipeline, and reporting layer changes to the data suite, and route headcount cost and accrual questions to the finance suite.

## Quality bar

A good people pack survives being challenged by the person it disadvantages. Every figure in it can be rebuilt by someone else from the definition on the page. Its headcount ties to the system of record on a stated date and says what it counted. Its attrition is split, defined, and cleaned of internal movement, so the number is about people leaving rather than about a system artifact. Its comparisons say what changed in the population, so a divestiture is not mistaken for an improvement. Its published cuts have been checked together rather than one at a time, and its small cells are counts rather than percentages. It says out loud which figures the upstream coding cannot support, and which stage owns the fix. And every number in it arrives attached to the decision it is being brought for, because a pack of figures with no decision behind them is how a forum ends up debating definitions for an hour and choosing nothing.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
