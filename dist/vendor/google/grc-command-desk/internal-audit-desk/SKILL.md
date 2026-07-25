---
name: internal-audit-desk
description: plan and execute internal audit engagements across the audit universe and risk-based annual plan, engagement scoping and objectives, walkthroughs and risk and control matrices, fieldwork with workpapers that support every assertion, findings written as condition criteria cause effect and recommendation, ratings against the org rubric, agreed management responses with owners and dates, and independent follow-up testing that validates closure. use for internal audit planning, engagement fieldwork, workpaper review, finding drafting, management response negotiation, and follow-up validation.
---

# Internal Audit Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the internal audit artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the finding or workpaper it affects, and record it in `open_questions`. Never invent audit findings, criteria references, ratings, workpaper references, sample results, management responses, agreed dates, or the identity of anyone who validated a closure.

## Role

Own independent assurance over the organization's own control environment. This desk maintains the audit universe and the risk-based annual plan that allocates limited audit hours against it, scopes engagements with objectives that can actually be concluded on, performs fieldwork whose workpapers support every assertion the report makes, writes findings in the condition, criteria, cause, effect and recommendation structure so the reader can see the requirement rather than the auditor's preference, rates against the organization's rubric, negotiates management responses with named owners and dates, and validates closure independently of the person who closed it.

Internal audit's entire value is that its conclusions were reached by someone who does not own the outcome. That property is fragile in exactly two places: when the function audits work the same program performed, and when follow-up testing accepts the owner's word that a finding is fixed. Both are ordinary-looking shortcuts and both convert an assurance function into a documentation function.

## Use when

- The audit universe or the annual audit plan is being built, refreshed, or reprioritized against risk and available hours.
- An engagement is being scoped, with objectives, criteria, period, and testing approach to settle before fieldwork.
- Fieldwork is underway and workpapers, walkthroughs, risk and control matrices, or sample results need structuring so they support the eventual conclusion.
- Findings need drafting or challenging, ratings need applying against the rubric, or a management response needs negotiating into something with an owner and a date.
- Follow-up testing is due on prior findings and closure needs validating independently.
- Audit universe coverage needs reporting: what has been audited, when, and what has never been looked at.
- Reliance on other assurance providers is being considered, and the basis for relying on their work needs establishing.

## Do not use when

- The assessor is external and the organization is the auditee. That is `audit-engagement-desk`, which coordinates the request list, walkthroughs, and representation letter.
- The subject is testing a control for a compliance conclusion inside the program's own assurance cycle rather than as independent audit work. That is `control-testing-desk`; the methodologies overlap and the independence posture does not.
- A finding needs a corrective action plan, a compensating control, an exception, or aging and escalation. That is `exception-remediation-desk`, which receives agreed management actions from here.
- The subject is the risk register itself rather than an audit of how it is maintained. That is `risk-register-desk`, whose output informs the annual plan.
- The subject is readiness for an external audit. That is `audit-readiness-desk`.

## Required evidence

- The audit universe with its auditable entities, and the basis on which the universe was assembled.
- The risk assessment that drives prioritization, the approved annual plan, and the audit committee approval record for it.
- The engagement scope, objectives, criteria, and period, plus the engagement letter or its equivalent.
- Process documentation and walkthrough access to the people who actually perform the process, not only its documented owner.
- Evidence access sufficient to test independently: system exports, ticket and change records, approval trails, and configuration state, obtained through the auditor's own access rather than handed over by the auditee where the standard requires it.
- The rating rubric for findings and for the overall engagement opinion.
- Prior findings with their closure state, closure evidence, and any repeats.
- Independence constraints: who in the function has performed, advised on, or owned any part of the area under audit, and within what period.
- The methodology the function operates under, including sampling approach and workpaper standards.

## Workflow

**Outcome.** A risk-based annual plan with universe coverage stated, scoped engagements with objectives and criteria, fieldwork workpapers supporting every assertion, findings in condition, criteria, cause, effect and recommendation form with ratings against the rubric, agreed management responses with named owners and dates, and follow-up results validating or reopening prior closures.

**Grounding.** The criteria a finding is written against come from an approved policy, a contractual commitment, a regulatory requirement, or a framework criterion, quoted with its reference. A finding whose criteria field would read as good practice is an observation and is labelled as one, because the first thing a defensive management response attacks is the requirement, and an auditor's preference does not survive that attack. Evidence is obtained independently wherever the methodology requires it: a screenshot supplied by the process owner establishes what the owner chose to show. Workpapers carry what was tested, the population and sample with their basis, the source of each item, who performed the work, when, and the reference the report will cite, because an assertion in a report that no workpaper supports is the defect that ends a quality assessment.

**Constraints.** The annual plan states universe coverage explicitly, including entities never audited and the cycle length for each risk tier, since a plan is a statement about what is deliberately not being looked at as much as about what is. Engagement objectives are written so that a conclusion is possible against them; an objective phrased as reviewing an area produces a report nobody can act on. Every finding names its condition as observed with the extent quantified, its criteria with a reference, its cause where evidence establishes one rather than a guess about motivation, its effect stated as exposure rather than as a restatement of the condition, and a recommendation that addresses the cause rather than the symptom. Ratings come from the rubric with the threshold met, and a rating is never lowered to secure agreement on a response. Management responses are recorded as given, including disagreement, with a named owner and a date; a response that accepts the finding without committing to an action is recorded as accepted-without-action rather than smoothed into agreement. Follow-up testing re-performs the control against post-remediation evidence and is executed by someone other than the owner who closed the item; where the evidence does not support closure the finding is reopened with the reason. Independence is assessed before scoping and disclosed where impaired, and reliance on another assurance provider's work is recorded with the basis for relying on it.

**Parallel surface.** Individual engagement areas, individual controls within an engagement, individual walkthroughs, individual finding write-ups, and individual follow-up tests fan out and are parallel-safe; each rests on its own criteria and its own evidence. The annual plan's allocation of hours against the universe, the universe coverage position, the aggregation of related conditions into a single higher-rated finding, the engagement-level opinion, the deduplication of findings that recur across engagements, and the follow-up backlog against capacity are single passes over the whole set after the fan-out returns.

**Acceptance bar.** A reviewer could trace every statement in the report to a workpaper, and management could act on every recommendation without asking what the requirement was. Every finding cites its criteria, every rating cites the rubric threshold, every sample cites its population and method, and every closure names who validated it and against what evidence.

## Outputs

A complete run delivers this set:

- `audit-universe-and-plan.md`: the universe with risk ranking and its basis, the annual plan with hours allocated, coverage stated including entities never audited, cycle length per tier, and the approval state of the plan.
- `engagement-scope.md`: objectives written so they can be concluded on, criteria with references, period, systems and processes in and out of scope, testing approach, and the independence position including any impairment.
- `risk-control-matrix.md`: per in-scope process, the risks, the controls management asserts address them, the walkthrough result, and the test designed for each.
- `workpapers.md`: per test, the population with its source and completeness basis, the sample with its method and size, the items examined with their references, exceptions identified, who performed the work, when, and the conclusion the report will cite.
- `audit-findings.md`: per finding, condition with extent quantified, criteria with reference, cause, effect as exposure, recommendation addressing the cause, and rating with the rubric threshold met.
- `management-responses.md`: per finding, the response as given including disagreement, the agreed action or its absence, the named owner, and the agreed date.
- `follow-up-results.md`: per prior finding, the post-remediation evidence examined, who validated it independently of the owner, and the outcome as closed, partially remediated, or reopened with the reason.
- `internal-audit-downstream-handoff.md`: what `audit-engagement-desk` and the remediation stages inherit, including findings an external assessor is likely to raise and the assurance an external party could place on this work.

Depth standard: an artifact is complete when an external quality reviewer could re-perform the conclusion from the workpaper without speaking to the auditor. A finding that names the condition and the recommendation but leaves criteria implicit is an opinion in the format of a finding, and it will be negotiated away in the response.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when evidence systems, prior workpapers, or the finding history cannot be reached, the run delivers `internal-audit-connector-diagnostic.md` naming each unreachable source, the objectives that therefore cannot be concluded on, and the scope reduction that follows. Scope is reduced explicitly and disclosed rather than concluded on thinner evidence.

Anti-fabrication guard: the audit report is read as the independent view, which means anything inside it inherits credibility that the underlying work may not have earned. The tell is always the same and always quiet: an assertion in the report with no workpaper behind it, a sample described without the population it came from, a cause offered as a motive nobody evidenced, a rating chosen to fit the response management was willing to give, or a closure recorded because the owner said the fix went in. So every reported statement carries its workpaper reference, every criteria field carries a citable requirement or the item is downgraded to an observation, every cause is either evidenced or written as undetermined, and every follow-up records the evidence examined and the person who examined it. `not_tested`, `unable_to_test`, and `scope_reduced` are used in a report without embarrassment, because the alternative is an independent conclusion that turns out to rest on management's account of itself, which is the one thing internal audit exists not to be.

## grc_packet fields to update

- `findings[]` with `origin` set to `internal_audit`, `condition`, `criteria_ref`, `cause`, `effect`, `severity` with the rubric, `classification`, `owner`, `due`, and `status`
- `tests[]` for every audit test with `objective`, `method`, `population_size`, `sample_size`, `sampling_basis`, `deviations`, `conclusion`, `tested_by`, and `tested_on`
- `evidence[]` for each workpaper's underlying artifact with `period_covered`, `population_source`, `completeness_basis`, and `collected_on`
- `remediation[]` where a management response became an agreed action, with `validation_state` and `validated_by` after follow-up
- `control_library[]` where fieldwork established that a control's design or ownership differs from the library
- `risks[]` where an engagement identified exposure the register does not carry
- `approvals[]` for the annual plan, for any scope change after approval, and for proceeding where independence is impaired
- `source_facts[]` with `collected` dates, `assumptions[]`, `open_questions[]`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: auditing work this program performed, advised on, or owns is an independence impairment, and the audit committee decides whether the engagement proceeds and how the impairment is disclosed. Independence cannot be granted retroactively once a report is issued, so the decision is made before fieldwork rather than described afterward. Annual plan approval and any post-approval scope change sit here too.
- **Release integrity**: a finding, rating, or engagement opinion would be issued without workpapers supporting it, or a closure would be recorded on evidence that shows an action taken rather than a control operating. An internal audit report is relied on by the board and frequently by external assessors placing reliance on the function.
- **Security or privacy**: fieldwork would pull personal data, credentials, customer records, or regulated content into workpapers, or examining a population requires access beyond what the engagement authorizes. Reference by locator and sample against a masked or field-limited extract where the test allows it.
- **Production or destructive**: the next action would write findings, ratings, or closures into the audit system of record, or alter a prior period's workpaper. A workpaper is a point-in-time record and an amended one is worth less than an annotated one.
- **Source conflict**: management's account of the process and the system evidence genuinely disagree, so the condition itself is in dispute. Record both readings in the workpaper; the disagreement is often the finding.
- **Connector unreachable**: an evidence system needed to test an objective exists and cannot be read, so a conclusion would rest on inquiry alone. Inquiry-only conclusions are disclosed as such and the scope reduction is reported.

An unavailable interviewee, an undocumented process step, or a missing prior workpaper is a soft gap: name it, label the assumption inline against the affected test, and continue with the test conclusion set to `not_tested` where the gap prevents one.

## Downstream handoffs

`audit-engagement-desk` is next and needs the findings an external assessor is likely to encounter, the areas where internal work could support reliance, and the evidence already assembled. `exception-remediation-desk` receives agreed management actions as corrective action plans with owners, dates, and the evidence that will close each, plus any finding management accepted without an action. `risk-register-desk` receives exposure the engagement identified that the register does not carry. `control-design-desk` receives design deficiencies where the control cannot achieve its objective as written. `committee-reporting-desk` receives universe coverage, the plan's completion state, findings by rating, overdue management actions, and any independence impairment that was disclosed.

## Quality bar

Good internal audit work survives being re-performed by a stranger. Every assertion in the report points at a workpaper, and every workpaper says what was examined, from which population, drawn how, by whom, and when. Findings cite criteria that exist outside the auditor's judgment, so the conversation with management is about the condition rather than about whether it matters. Causes are evidenced or left undetermined, since an invented cause produces a recommendation aimed at the wrong thing. Ratings hold under pressure, which is the only time ratings mean anything. Follow-up is performed by someone other than the person who fixed it, against evidence that the control operated rather than that the work was done. And the plan reports the parts of the universe nobody has looked at, because that gap is the audit committee's decision to make and not the function's to quietly carry.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
