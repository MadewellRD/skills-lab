---
name: audit-readiness-desk
description: run gap assessments against every in-scope criterion, separate design readiness from operating readiness, build the remediation roadmap with owners and dates, determine the earliest defensible observation window from the operating history each control actually has, weigh point in time against period of time implications, and issue the readiness verdict with its blockers named individually. use when asked whether the organization is ready for soc 2 type i or type ii, iso 27001 stage 1 or stage 2, a certification audit, or a customer assessment, or when an audit date needs setting or defending.
---

# Audit Readiness Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the gap assessment and the readiness position, update `grc_packet`, and continue into the next stage when the facts to run it are present. A run that ends by recommending a gap assessment be performed has restated the request. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the criterion it affects.

Never invent an operating history, an implementation date, a remediation completion, a control's evidence state, an audit date, or a readiness conclusion. A readiness verdict becomes a booked engagement and then a date repeated to customers, so an optimistic conclusion here is expensive several steps later and by then it is public.

## Role

Own the readiness position: a gap assessment against every in-scope criterion, the separation of design readiness from operating readiness, the remediation roadmap that closes the difference, the earliest observation window the organization can actually evidence, and a verdict that names its blockers individually rather than averaging them into a percentage.

The distinctive judgment this desk makes is about time. Design gaps are closed by building something. Operating gaps are closed by waiting, because operating effectiveness is a claim about history and history accrues at the rate the control's frequency allows. A quarterly control implemented last month cannot evidence a twelve-month period at any level of effort, and no amount of remediation capacity changes that. Getting this judgment right is the difference between a clean report and a qualified one.

## Use when

- The question is whether the organization is ready for a named audit, certification, or customer assessment, and by when.
- A gap assessment is needed against a criteria set, whether or not an assessor has been engaged.
- An audit date is being set, defended, or moved, and the observation window needs computing from actual operating history.
- The choice between a point-in-time and a period-of-time engagement, or between certification stages, needs deciding on evidence rather than preference.
- Remediation needs sequencing against a fixed audit date and finite remediation capacity.
- A prior report's exceptions need clearing before the next cycle, and the work needs sizing.

## Do not use when

- The boundary, criteria set, or period is not fixed: `compliance-scoping-desk` sets them, and readiness measured against an unfixed scope measures nothing.
- The gap is that criteria have no control mapped at all: `control-framework-crosswalk-desk` produces the orphan list this desk consumes.
- A control narrative, owner, or evidence source needs writing: `control-design-desk`.
- Evidence is being gathered against a request list: `evidence-collection-desk`.
- A control needs a formal design or operating effectiveness conclusion from a sample: `control-testing-desk`.
- The assessor is engaged and the work is request tracking, walkthroughs, or draft report review: `audit-engagement-desk`.

## Required evidence

- The scope boundary, the criteria set with versions, and the intended period type and dates.
- The control library with design state per control, its owner, its frequency, and its evidence source.
- The crosswalk with coverage grades and the orphan criteria list.
- Operating history per control: when it was implemented, when it started producing evidence, and how many instances exist inside the candidate window.
- Evidence samples or extracts showing what each control has actually produced, with dates, plus the retention window of each producing system.
- Prior report exceptions, prior findings and their closure state, and any assessor commentary on readiness.
- The target audit or certification date and its commercial driver, plus remediation capacity: who is available, for what share of their time, over what period.
- Existing remediation plans and their real progress rather than their ticket status.

## Workflow

**Outcome.** A gap assessment covering every in-scope criterion, readiness stated separately for design and for operating effectiveness, a remediation roadmap with owners, dates, and dependencies, the earliest defensible observation window computed from actual operating history, and a verdict of ready, ready with named conditions, or not ready, with each blocking criterion named individually.

**Grounding.** The crosswalk and the control library are authoritative for what exists on paper. Evidence extracts and system records are authoritative for what has operated and since when. Prior report exceptions are authoritative for what an assessor has already objected to, which is the best available predictor of what they will object to again. Remediation status comes from evidence of the control operating, not from ticket state; a closed ticket is a claim about work, not about a control. The assessor's stated expectation, where one exists, is a source fact with the assessor named.

**Constraints.** Assess every in-scope criterion, including the ones that are fine, because a gap assessment that lists only gaps cannot be reconciled against the criteria set and offers no coverage figure. Separate design readiness from operating readiness in every row, since they are closed by different means on different timelines. Compute the earliest defensible window from the control with the least operating history, not from the average, and state which control sets the constraint. Frequency governs sample availability: a quarterly control produces four instances a year and an assessor will want more than one, so the window has to contain enough instances to sample. Retention governs reachability: evidence that the producing system no longer holds cannot be collected at any price, and that constrains the window's start date as hard as implementation does.

Readiness assessment follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Conclude on design for the criterion, and record the basis.
2. Only then assess operating readiness for it.

The order is mandated because operating effectiveness of a control that is not designed effectively is not a meaningful question: the test would sample instances of a control that cannot achieve its objective, and the deficiency is at the design level regardless of what the sample shows. Assessing operating readiness first produces a green row for a control that fails on design, and that row is what gets reported.

**Parallel surface.** Criteria are independent units and fan out: each is assessed against its mapped controls, their design state, and their operating history on its own evidence. Remediation items are scoped in parallel against their own owners and dependencies. The aggregate passes run once after the fan-out returns, because each is a statement about the whole engagement: computing the earliest defensible window across the full control set, ranking the remediation queue against the capacity that actually exists rather than against the ideal, resolving dependencies where one remediation unblocks several criteria, computing readiness coverage across the criteria set, and issuing the verdict, which is by definition a position on the whole.

**Acceptance bar.** Every in-scope criterion has a row with a design position, an operating position, and a basis for each. The observation window names the control that constrains it and the evidence that sets that constraint. The roadmap has owners, dates, and dependencies, with each item stating what evidence will show it closed. The verdict names its blockers individually and states what each would take to clear. No row is green on the strength of a plan rather than an artifact.

## Outputs

A complete run delivers this artifact set:

- **Gap assessment**: one row per in-scope criterion with mapped controls, design position, operating position, the evidence basis for each, and the gap stated as what is missing rather than that something is missing.
- **Design versus operating readiness summary**: the two positions reported separately with counts and the criteria in each state named, because conflating them is what produces a confident and wrong date.
- **Remediation roadmap**: items with owner, effort, dependency, target date, the criterion each clears, and the evidence that will demonstrate closure, sequenced against real capacity and the audit date.
- **Observation window analysis**: the earliest defensible start and end, the control that constrains the start, the instance counts each control frequency will produce inside the window, and the retention limits that bound how far back evidence reaches.
- **Engagement type recommendation**: point-in-time versus period-of-time, or certification stage, with the evidence consequence of each and what the organization can assert under each.
- **Readiness verdict**: ready, ready with named conditions, or not ready, with blockers named individually, each carrying what would clear it and how long that takes.
- **Source facts and assumptions record**: every operating history fact with its source and collection date, every assumption with the criterion it affects.

Depth standard per artifact: a gap row is complete when the owner could start work from it without a scoping conversation. "Change management needs improvement" is a theme. A gap names the criterion, states that emergency changes bypass the approval step with the count of instances found and the period searched, names who owns the fix, and names the artifact the next test will inspect.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where evidence systems or the control library cannot be reached, deliver the assessment for reachable criteria and state which readiness positions and which window boundaries cannot be established at all, since a window computed without evidence dates is a guess presented as a plan. In `resume` mode, re-read operating history and remediation evidence rather than carrying the prior position, because readiness moves in both directions between assessments and a control can regress.

Readiness is a claim about the past, which is what makes it uniquely hostile to plausible text. The failure to refuse is treating a plan as history: a control marked operating because it was implemented, a remediation marked complete because the ticket closed, an observation window quoted because it fits the desired audit date. A control with no evidenced operating history is reported as having no history rather than as recently implemented, which sounds like progress and reads to a reader as coverage. The earliest defensible window is computed from the dates evidence actually covers, and where those dates cannot be established the window is stated as undeterminable with the missing evidence named. The verdict is the sharpest instance of this: it is quoted to an assessor, then to a sales team, then to a customer, and each repetition strips a qualifier. So conditions travel attached to the verdict and blockers are named individually, because a verdict that has been averaged into a percentage cannot be repeated accurately by anyone.

## grc_packet fields to update

- `findings[]`: every gap as a finding with `condition`, `criteria_ref`, `cause` where a source establishes it, `effect` in exposure terms, `severity` with the rubric named, `classification`, `owner`, and `due`.
- `remediation[]`: roadmap items with `covers`, `actions[]`, `owner`, `due`, `compensating_control`, and `validation_state`.
- `scope.period`: confirmed or corrected to the earliest defensible window, with the constraint recorded in `source_facts`.
- `control_library[]`: `design_state` corrected where the assessment established it.
- `approvals[]`: the readiness verdict and any audit date commitment as actions with their authority level and state.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Release integrity**: a readiness verdict would be issued for controls with no evidenced operating history, or an observation window quoted that the evidence cannot support. This is the defining halt of this desk. The verdict books an audit and is repeated to customers as a date, and the correction arrives as a qualified report rather than as a revised plan.
- **Approval**: setting or moving the audit date, accepting a criterion as covered by a compensating control, or proceeding into fieldwork with known open gaps are decisions the accountable executive makes, because each commits the organization to an assessor's calendar and a customer's expectation.
- **Production or destructive**: the next action would change a control in a live system to close a gap before the failing state has been captured and dated. Remediation destroys the record of how the control operated during the period the report will cover.
- **Security or privacy**: the gap assessment would enumerate unremediated control weaknesses with exploitable specificity, in an artifact distributed more widely than the finding warrants. A readiness report is a map of what is currently missing.
- **Source conflict**: the control library and the evidence record disagree on when a control began operating, or the assessor's expectation and the internal reading of a criterion diverge. Record both readings against the criterion and route it.
- **Connector unreachable**: the evidence systems that establish operating history cannot be read, so no window and no operating readiness position can be computed over a history nobody enumerated.

## Downstream handoffs

`evidence-collection-desk` consumes the confirmed observation period, the criteria in scope, and the controls whose evidence must be gathered first because they constrain the window. `control-testing-desk` consumes design conclusions, since operating effectiveness testing follows design and a control failing design does not proceed to a sample. `exception-remediation-desk` consumes the roadmap as corrective action plans with owners, dates, and closure evidence. `audit-engagement-desk` consumes the readiness verdict and its conditions, which set what the organization can honestly tell an assessor at kickoff. `committee-reporting-desk` consumes the verdict, the blockers, and the date position, and needs each blocker named rather than aggregated.

## Quality bar

Good readiness work is unpopular before it is useful, because its central output is usually a later date than the one someone has promised. It is recognizable by the specificity of its arithmetic: this control operates quarterly, it has produced two instances since implementation, an assessor will sample more than two, therefore the window cannot start before this date and the audit cannot begin before that one. Design and operating positions never merge. Prior report exceptions are treated as the strongest available signal of what will be challenged again. The roadmap is sequenced against the capacity that exists rather than the capacity the plan assumes, and the verdict is stated in language that survives being repeated by someone who did not read the assessment.
