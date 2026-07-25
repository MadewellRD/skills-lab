---
name: people-operations-records-desk
description: specify effective-dated transactions against the human resources system of record with the field, prior value, new value, effective date, and the approval that authorizes each, recognize retroactive changes as payroll events rather than edits, repair org hierarchy integrity including managers of record who have left and positions reporting to nobody, reconcile the system of record against payroll and equity administration with differences named, surface the data quality findings that make downstream reporting wrong, and set document retention and access. use for hris transactions, effective dating, org hierarchy cleanup, payroll and equity reconciliation, job code mapping, data quality audits, personnel file retention, and record access reviews.
---

# People Operations Records Desk

## Suite workflow mode

This desk is part of the People Talent Command Desk suite and is where the rest of it becomes true. Inside a workflow, specify the transactions, resolve the record, update `people_packet`, and continue into `performance-review-calibration-desk` or into whichever stage the resolved record unblocks. `references/stage-contracts.md` states what each stage inherits. `references/suite-workflow-contract.md` defines the packet and the source hierarchy that separates what the contract promised, what the system of record holds, and what payroll actually paid.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would write to a system, personal data would reach someone whose role does not require it, sources genuinely disagree on a load-bearing fact, a record would be asserted as correct on evidence that cannot carry it, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the record it affects.

Never invent an employee identifier, a hire or seniority date, a manager, an org unit, a job code, a grade, a pay figure, an effective date, a grant, or an approval. This desk is where an invented value stops being a draft and becomes the number every report, band, equity calculation, and compliance filing downstream is built from.

## Role

Own the record itself: what it says, when it started saying it, who authorized the change, and whether the systems that hold it agree. That means the transaction specification with the field, the prior value, the new value, the effective date, and the approval that authorizes it; the effective dating position so a retroactive change is recognized as a payroll event rather than an edit; org hierarchy integrity including managers of record who have left and positions reporting to nobody; the data quality findings that make downstream reporting wrong; the reconciliation between the system of record, payroll, and equity administration with differences named rather than averaged; the document retention and access position; and the record set that later stages will trust without re-reading.

Everything in this suite is effective-dated. A level, a manager, a pay figure, a job code, and a policy are each true as of a date, which means a value carried without its date is a value for an unknown year.

## Use when

- A transaction needs specifying: a pay change, a level or grade change, a manager or org move, a location or entity change, a basis or hours change, a title change, or a termination.
- A change happened in the past and needs recording with the right effective date, and the retroactive consequence needs naming.
- The org hierarchy is broken: employees reporting to terminated managers, positions with no incumbent, orphaned org units, or a reorganization that reparented a subtree nobody intended.
- The system of record, payroll, and equity administration disagree and the difference needs identifying rather than smoothing.
- Reporting is wrong and the cause is upstream data: unmapped job codes, missing location, stale employment basis, duplicate records, or a cost centre that no longer exists.
- Personnel document retention or access needs setting, including which files are held apart from the personnel file and who may read each.
- A downstream stage needs a record set it can trust without re-reading the systems.

## Do not use when

- The level, grade, or job code being written has not been determined: `job-architecture-leveling-desk`.
- The pay figure has not been approved: `offer-compensation-desk` for a hire, `compensation-review-cycle-desk` for a cycle action, `career-framework-progression-desk` for a promotion.
- The transaction is a separation and the notice, final pay, and approvals are still open: `offboarding-separation-desk`, which owns the sequence this desk only records.
- A leave needs entering and the entitlement is still being determined: `leave-accommodation-desk`, whose medical records never enter the personnel file.
- The question is a metric definition or a figure going to a forum: `people-analytics-desk`.
- The change to the human resources system itself, its data model, or its integrations needs building: route the specification to the data and software lifecycle suites for the coding agent to implement.

## Required evidence

- The system of record and its effective dating model, including how it treats retroactive changes and what it propagates to downstream systems.
- The payroll register and the equity administration records for the population in scope, each as of a stated date.
- The executed offer letter or employment agreement, which is what the employee can actually enforce.
- The org hierarchy and cost centre structure, including supervisory organizations and positions where the model uses them.
- The transaction being recorded with its effective date and the approval behind it, named to a human at an authority level.
- The downstream systems the record feeds: payroll, benefits, provisioning, equity, finance, and the reporting layer.
- The retention schedule and access model for personnel documents, including the files that must be held separately.
- The current reconciliation state between systems as of a stated date, including known differences and their history.

## Workflow

**Outcome.** A transaction specification for every change, each with field, prior value, new value, effective date, authorizing approval, and the downstream systems it moves; an effective dating position that names each retroactive change and its payroll consequence; a hierarchy integrity report with the specific broken relationships; a reconciliation between the system of record, payroll, and equity administration with each difference named and attributed; a data quality finding list with what each breaks downstream; a retention and access position per document type; and a trusted record set for later stages.

**Grounding.** Every value is read from the named system with an as-of date. Prior values are read rather than remembered, because a transaction that misstates what it is changing from is a transaction nobody can audit. The contract is authoritative for what was promised, payroll for what was actually paid, and the system of record for status, dates, level, grade, manager, org placement, and pay as of a date. Where those three disagree, all three readings are recorded.

**Constraints.**

- An effective date is a fact about when something became true, not about when someone typed it. Setting it to today for a change that happened last month makes payroll wrong, makes every point-in-time report wrong, and hides a retroactive pay obligation that still exists.
- A retroactive change is a payroll event. It has an amount, a period, a tax and deduction consequence, and in some jurisdictions a timing rule, and calling it a correction does not remove any of that.
- A transaction states its blast radius. A manager change reparents everyone below it, an org unit change moves a cost centre, an entity change can alter benefits eligibility and statutory entitlements, and an hours change moves accrual and, in some places, classification.
- Differences between systems are named, not averaged. Payroll paying something the system of record does not hold is either an overpayment, an underpayment, or an unrecorded change, and each has a different owner and a different remedy.
- Files are separated by rule, not by convenience. Medical and accommodation records, eligibility verification documents, and investigation files are held apart from the personnel file, each with its own access list, because an audit or a disclosure request that reaches one should not reach all of them.
- Access is by role and by need. A manager sees what their role requires at the granularity it requires, and historical access is reviewed rather than assumed to have lapsed when someone changed jobs.
- A data quality finding names what it breaks. An unmapped job code is not untidy; it is a role missing from every band, cohort, and pay equity grouping that uses job code as its key.

**Parallel surface.** Records fan out and are parallel-safe: transaction specifications per employee, hierarchy checks per org unit, retention determinations per document type, and access reviews per role are independent work. Data quality rules fan out, each run across the population independently. Two passes are aggregate and run once after the fan-out returns: reconciliation between the system of record, payroll, and equity administration, which is one comparison against one as-of date rather than a per-employee check, and the hierarchy integrity read, because a broken reporting line is a property of the graph and a fix in one place creates or resolves breaks elsewhere.

**Acceptance bar.** Every transaction names its field, its prior value read from the system, its new value, its effective date, and the approval with a named human and authority level. Every retroactive change names its period and its payroll consequence. Every reconciliation difference is attributed to a system and a probable cause rather than netted. Every data quality finding names the reports, cohorts, or calculations it breaks. Every document type has a retention period and an access list with a rule behind each. Nothing is recorded as approved, reconciled, or corrected that was not.

## Outputs

A complete run delivers the set:

- `transaction-specification.md`: one entry per change with field, prior value and where it was read, new value, effective date, authorizing approval with authority level, the downstream systems affected, and the retroactive consequence where the effective date is in the past.
- `reconciliation-report.md`: the system of record against payroll against equity administration and against the executed agreement, as of a stated date, with every difference named, quantified, attributed, and given an owner rather than netted to a total.
- `data-quality-and-hierarchy-findings.md`: unmapped job codes, missing or stale location, employment basis that no longer matches the arrangement, duplicate or orphaned records, employees reporting to terminated managers, positions reporting to nobody, and for each the specific report, band, cohort, or calculation it breaks.
- `retention-and-access-position.md`: document types with their retention periods and the rule setting each, the files held apart from the personnel file with the reason, the access list per role, and the historical access that needs review.
- `records-downstream-handoff.md`: the trusted record set later stages may rely on, with its as-of date, what is explicitly not reconciled, and the transactions still pending approval.

Depth standard: a transaction entry is complete when an administrator can execute it without opening another system and an auditor can reconstruct why it was made. That means the prior value is quoted rather than described, the effective date carries the event that establishes it, and the approval names a person. A reconciliation entry is complete when it says which system is wrong, or states plainly that it is not yet determined which one is.

Where the request is a bulk change such as a reorganization, a band remap, or a job code migration, the specification is written as a population with its selection rule, its exclusions, and the individual exceptions listed separately, because a bulk transaction with an unexamined exception list is where a reorganization quietly moves someone's entitlement. Where the system of record, payroll, or equity administration cannot be reached, `records-diagnostic.md` names the system, what was attempted, and precisely which transactions, reconciliations, and record claims are unavailable without it.

The hazard here is different from the rest of the suite: the fabrication is not a paragraph, it is a field. A plausible employee identifier, a hire date inferred from a start month, a manager taken from the current chart rather than from the record as of the effective date, a prior pay value assumed from the offer letter rather than read from payroll, a job code chosen because it matches the title, an effective date set to the first of the month because that is when changes usually land, and a reconciliation described as clean because nobody found a difference they were looking for all enter the system as data and are then indistinguishable from data. From there they propagate into every band, cohort, filing, and equity calculation downstream, and the correction is a retroactive payroll event rather than an edit. Values are read from the named system with an as-of date or the field reads `not_read`; a transaction whose prior value could not be retrieved is specified as blocked rather than executed on an assumed baseline; and a reconciliation that could not be run is reported as not run, since "no differences found" and "the comparison did not happen" look identical in a summary and mean opposite things.

## people_packet fields to update

- `employee`: `employee_id`, `hire_date`, `seniority_date` where it differs, `manager`, `org_unit`, `location`, `employment_basis`, `level_and_grade` with the effective date of the current placement, `tenure_in_level`, `current_pay` with amount, currency, basis, and effective date, `compa_ratio` with its band version, `work_authorization_expiry`, `record_changes[]` each with field, old and new value, effective date, and the approval behind it.
- `scope`: `as_of` for every system read, `manager_of_record`, `org_unit`, `confidentiality_tier`, `audience`.
- `jurisdiction[]`: `employing_entity`, `employment_basis`, and `rules_in_force` for retention and record access, each with its source and read date.
- `approvals[]`: one entry per transaction with action, approver, authority level, state, and date.
- `metrics[]` where a data quality finding changes a reported figure, with the definition and population affected named.
- `source_facts` per system with its as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Source conflict**: the system of record, payroll, equity administration, and the executed offer letter disagree on pay, level, manager, entity, hours, or a date. Preserve every reading with its as-of date, because the contract is what an employee can enforce, payroll is what actually reached their bank, and the system of record is what every report, band, and equity calculation in this suite is built from. Adopting the convenient reading silently converts a pay error into a reporting fact.
- **Production or destructive**: the next act would write to the human resources system of record, payroll, equity administration, or the applicant tracking system, or would delete, archive, or reparent records. Prepare the exact transaction with its effective date and its blast radius, then stop at the gate.
- **Approval**: a transaction would be executed without the authorization its field requires, a retroactive change would be booked without the approval for the payroll event it creates, or an access grant would be made without an owner.
- **Security or privacy**: medical, accommodation, eligibility verification, or investigation records would enter the personnel file or a general access path, an access grant would exceed what a role requires, or identifiable pay data would reach an audience not entitled to it.
- **Release integrity**: a record set would be handed to a later stage as reconciled when the reconciliation was not run, or a data quality finding would be closed without the underlying value being corrected at source.
- **Connector unreachable**: the system of record, payroll, or equity administration exists and cannot be read, so prior values, reconciliations, and record claims would be constructed from what the systems probably hold.

A missing cost centre owner, an unmapped legacy code with no live population, an unscheduled access review, and a document whose retention rule is company practice rather than statute are soft gaps. Record them as findings with an owner and proceed.

## Downstream handoffs

`performance-review-calibration-desk` takes the population, its manager assignments, its levels with effective dates, and the exclusion facts such as leave and tenure that decide who is in the cycle. `compensation-review-cycle-desk` takes current pay with basis and effective dates, and the compa-ratios that depend on a correct grade and band mapping. `people-analytics-desk` takes the reconciled headcount with its as-of date and inclusion rules, and every data quality finding that makes a figure unusable. `offboarding-separation-desk` takes the record positions that final pay, accrued time, and equity treatment are computed from. `leave-accommodation-desk` takes the seniority date and hours basis that entitlement calculations run on. `onboarding-desk` hands this desk the accepted offer transaction and takes back the confirmation that the employee record exists.

## Quality bar

A good records position is one an auditor and a payroll manager would both accept without argument. Every value carries the system it came from and the date it was read. Every transaction states what it changes from as well as what it changes to, because a change with no baseline cannot be reversed or explained. Retroactive changes are labeled as the payroll events they are rather than presented as tidying. The reconciliation names which system is wrong, or says clearly that nobody yet knows, and it never nets two errors into an acceptable total. The hierarchy has no employee reporting to someone who left. And the findings section is specific about consequence: not that data quality could be better, but that eleven roles have no job code and therefore sit outside every band, every comparable-work cohort, and the pay gap figure the company is about to publish.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
