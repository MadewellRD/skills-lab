# People and Talent Suite Workflow Contract

This file defines how People Talent Command Desk skills run as one continuous program of work instead of behaving as isolated one-off prompts. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is people: what a role is worth, who gets hired into it, what they are told about how they are doing, what they are paid for it, what happens when something goes wrong, and how they leave. Nearly every artifact here is about a named individual, and most of them are read later by that individual, by their manager, by an auditor, by a works council, or by opposing counsel. The distinguishing failure of this domain is not a slow process. It is a fluent, sympathetic, well-structured paragraph about a person that no record supports, filed as though it were a record, and produced two years later in a hearing where the only questions are what was documented at the time, by whom, and on what date.

Two structural facts shape everything downstream. The rules are local: pay range disclosure, notice periods, final pay timing, leave entitlement, consultation obligations, what may lawfully be asked in an interview, and what may be retained all change with the jurisdiction of employment, and the jurisdiction that binds is the employee's rather than the company's. And the records are effective-dated: a level, a manager, a pay figure, a job code, and a policy are each true as of a date, so a people fact carried without its date is not yet a fact.

## Continuity rule

A desk that has the facts to run the next stage runs it. A run that ends at "this should go to your HR business partner" or "consider reviewing your leveling framework" is a routing note rather than people work, and it hands the sequencing problem back to a manager who is already holding a conversation they do not know how to have. Complete the current stage, update `people_packet`, and continue until the requested outcome exists or a hard halt applies.

Four things are never continued through: anything that changes what a person is paid, anything that tells a person where they stand, anything that determines whether they still have a job, and any write into a system of record. Everything else continues, with the assumption labeled inline against the requisition, role, candidate, employee, cohort, cycle, case, or metric it affects.

## Action boundary

This suite produces plans, definitions, drafts, models, analyses, packets, and recommendations: headcount plans and org models, job architecture and level placements, job descriptions and postings, sourcing plans and funnel analyses, interview loops and rubrics, debrief syntheses and hiring recommendations, offer models, onboarding plans, review materials and calibration inputs, promotion packets, talent review and succession maps, manager guidance, survey analyses and action plans, compensation models and pay equity analyses, policy drafts, investigation plans and findings drafts, leave and accommodation assessments, separation packets, and people reporting.

It does not extend an offer, communicate a rating, a promotion outcome, or a compensation change, deliver discipline or a termination, publish a policy or a job posting, write to the HRIS, payroll, equity administration, or the applicant tracking system, send anything to a candidate, an employee, or a population, revoke access, close an employee relations case, approve or deny a leave or an accommodation, commit severance or a release, or make a representation to a regulator, an auditor, a works council, or a union. For each of those the desk prepares the exact item, names the approval it needs and what it commits the company to, and stops at the gate.

Three boundaries hold in every mode. Personal data reaches only the people whose role requires it, at the granularity their role requires: a manager needs to know that someone will be away and until when, not the medical reason behind it, and a compensation analysis needs pay by level and cohort, not a named list circulating in a team channel. Self-identification data and any protected characteristic stay out of hiring, rating, promotion, and selection artifacts, are never inferred from a name, a photograph, a school, or a gap in a work history, and appear only in aggregate representation reporting above the reporting threshold. And a record is never improved after the fact: backdating a write-up, adding documentation to a file once a decision is made, rewriting a scorecard after the debrief, or restating an investigation finding after the outcome is known converts an ordinary dispute into evidence of a cover-up, and the document metadata is usually what establishes it.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a level placement, an interview rubric, an offer model, a survey read, a policy draft, or an attrition analysis.
- `workflow_run`: the default for anything phrased as an opening to fill, a cycle to run, a person situation to handle, an org question to answer, or a program to build. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `people_packet` or a halt-resume prompt. Re-read the systems of record rather than trusting the packet's copy of them, because a manager changed, a resignation landed, a requisition was cancelled, a band was refreshed, and a policy took effect while the packet sat still. Recompute every statutory or contractual clock rather than carrying its value forward.
- `halt`: a hard halt class applies. Return the halt format below with the packet intact, the reversible work already done, and every running clock named.
- `diagnostic`: required systems cannot be reached. Report what was reachable, what was not, and precisely which level placements, pay positions, headcount figures, case findings, or metrics each gap makes unavailable. Do not substitute what a company of this size and shape usually does for the record nobody could pull.

## Request types

Every request carries exactly one type, because the type sets the approval surface, the audience, the confidentiality tier, and the evidence standard: `workforce_plan`, `role_definition`, `requisition`, `sourcing`, `interview_design`, `candidate_decision`, `offer`, `onboarding`, `record_change`, `performance_cycle`, `calibration`, `promotion`, `talent_review`, `manager_support`, `engagement`, `compensation_cycle`, `pay_equity`, `policy_change`, `employee_relations`, `leave_accommodation`, `separation`, `reduction_in_force`, `people_reporting`, `unknown`.

Three distinctions matter more than the type itself.

The first is whether the subject is one identifiable person or a population. A population statement is an analysis and tolerates a labeled working assumption. A statement about a named individual becomes part of that person's file, is disclosable to them in many jurisdictions, travels with them through promotion and separation decisions, and outlives everyone who wrote it.

The second is whether the output changes pay, tells someone where they stand, or determines whether they still have a job. Those three acts are the ones this function cannot take back. A rating communicated cannot be revised downward without doing more damage than the original error, a pay figure stated becomes an expectation, and a termination is final on the day it happens whatever the file says afterward.

The third is which jurisdiction binds. Almost nothing in this domain is globally true. The same promotion, the same leave request, the same posting, and the same separation carry different obligations in two locations, and a remote employee's location governs regardless of where the team or the entity sits.

## The people packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `not_established`, `undocumented`, `not_measured`, `not_applicable`, and `none` are legitimate values; an invented level, pay figure, market percentile, rating, headcount, attrition rate, policy provision, jurisdictional rule, approval, or statement attributed to a person is not.

```yaml
people_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  request_type: "workforce_plan | role_definition | requisition | sourcing | interview_design | candidate_decision | offer | onboarding | record_change | performance_cycle | calibration | promotion | talent_review | manager_support | engagement | compensation_cycle | pay_equity | policy_change | employee_relations | leave_accommodation | separation | reduction_in_force | people_reporting | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  scope:
    subject_type: "requisition | candidate | employee | team | org_unit | population | policy | cycle | case"
    subject_ref: "requisition id, candidate reference, employee id, org unit, or the population definition"
    population_definition: "who is in and who is deliberately out, because every rate in this packet is a rate over it"
    org_unit: ""
    manager_of_record: "the manager in the system of record, which is not always the person asking"
    hr_partner: "named partner, or unassigned"
    period: "the cycle, fiscal period, or effective window this work sits in"
    as_of: "the date the records in this packet were read"
    confidentiality_tier: "open | manager_only | hr_restricted | investigation_restricted | legally_privileged"
    audience: "who will read the artifact, which sets what may appear in it"

  jurisdiction:
    - location: "country, and the state, province, or city where the binding rule is set locally"
      applies_to: "the population or person this entry governs"
      work_arrangement: "onsite | hybrid | remote_in_jurisdiction | remote_cross_border"
      employing_entity: "the legal entity that employs the person, which is not always the brand on the badge"
      employment_basis: "employee | fixed_term | contractor | agency_worker | intern | employer_of_record"
      collective_agreement: "union contract, works council, or none, with the consultation trigger it creates"
      rules_in_force: []               # each with what it governs, its source, and the date it was read
      classification_risk: "where the working reality and the contracted basis do not match"

  workforce_plan:
    horizon: "the period planned, with the fiscal calendar it runs on"
    approved_headcount: "by org unit and level, as approved rather than as requested"
    current_headcount: "reconciled to the system of record on a stated date, with contractors and interns counted or excluded explicitly"
    open_positions: ""
    attrition_assumption: "the rate assumed, the historical window behind it, and whether it separates voluntary from involuntary"
    org_shape: "spans, layers, and manager-to-individual-contributor ratio, where they are the subject"
    build_buy_borrow: "hire, develop internally, or contract, with the assumption behind each"
    capacity_gap: "the skills, locations, or levels the plan does not cover"
    budget_basis: "fully loaded cost or base only, stated explicitly, with the fiscal period it lands in"
    scenario: "the plan variant this packet describes, where more than one is live"

  requisition:
    req_id: ""
    state: "draft | pending_approval | approved | open | on_hold | filled | cancelled"
    reason: "incremental | backfill | replacement | conversion | reorganization"
    backfill_of: "the vacated position, with the former incumbent's level and pay where that is the comparison being made"
    headcount: ""
    fte: ""
    approval_state: "pending | granted | denied"
    approver: "named approver and authority level"
    approved_at: "date"
    budget_approved: "the amount approved and against which fiscal period"
    hiring_manager: ""
    recruiter: ""
    target_start: "date, and what depends on it"
    opened_at: "date"
    days_open: "with the event the count starts from"
    priority: "with who set it and against what"

  role:
    job_title_internal: ""
    job_title_posted: "the market-facing title, where it differs from the internal one"
    job_family: ""
    job_sub_family: ""
    job_code: ""
    level: "the level on the architecture in force"
    track: "individual_contributor | manager | executive | dual"
    grade: ""
    salary_range_ref: "the band, with its version, effective date, and geographic differential"
    exemption_classification: "the classification, the test applied, and the jurisdiction it was applied under"
    scope_statement: "the scope, autonomy, and impact that place the role at this level, in the language of the level guide"
    leveling_comparators: "the existing roles this was benchmarked against"
    must_have_criteria: []             # each tied to something the work actually requires
    nice_to_have: []
    success_measures: "what good looks like at six and twelve months, written so it can be assessed"
    posting_obligations: "pay range disclosure and any other jurisdictional posting requirement"
    reporting_line: "manager, and the dotted lines that make the role real"

  pipeline:
    funnel:
      - stage: "sourced | applied | screened | assessed | onsite_loop | debrief | offer | accepted | declined | withdrawn | rejected"
        count: ""
        time_in_stage: ""
        pass_through_rate: "with the denominator stated"
    source_channels: []                # each with volume, pass-through, and cost where it is known
    disposition_codes: "the reasons recorded at rejection, which is the record an audit reads"
    pipeline_coverage: "whether the pipeline is deep enough for the decision being made, or is one candidate wearing a process"
    candidate_experience: "response times, dropped candidates, and where the process loses people"
    agency_or_referral_terms: "fees, guarantees, and eligibility, where they apply"

  candidates:
    - candidate_ref: "identifier; a name appears only in an artifact already restricted to the people entitled to it"
      stage: ""
      source: ""
      internal: "true | false"         # an internal candidate carries a different process and a different fallout on rejection
      work_authorization: "status and any sponsorship requirement, as the candidate stated it"
      compensation_expectation: "with whether asking for pay history is lawful in this jurisdiction"
      evidence: []                     # each with the interviewer, the competency, what was observed, and the date recorded
      scorecard_state: "complete | partial | missing, per interviewer"
      recommendation: "hire | no_hire | hire_at_different_level | insufficient_evidence"
      dissent: "the recorded disagreement, kept rather than averaged away"
      accommodation_requested: "the process adjustment, recorded without the underlying condition"

  interview_loop:
    rubric_version: ""
    competencies: []                   # each with the level anchor it is scored against
    stages: []                         # each with interviewer, competency coverage, format, and duration
    interviewer_calibration: "when interviewers were last calibrated, and the variance between them"
    structured_share: "how much of the decision rests on the instrument rather than on unstructured impression"
    question_boundaries: "topics that cannot lawfully be asked in this jurisdiction"
    work_sample: "the exercise, its time cost to the candidate, and whether it is paid"
    scorecards_before_debrief: "true | false"
    adverse_impact_watch: "pass-through by stage where the population supports the read, or below_threshold"

  offer:
    offer_id: ""
    candidate_ref: ""
    base: "amount and currency, with the pay basis and period"
    variable: "target and mechanism, with whether it is guaranteed or at risk"
    equity: "instrument, quantity, vesting schedule, and the price basis, with the valuation date behind it"
    sign_on: "amount, and any clawback attached"
    relocation: ""
    band_position: "range penetration or compa-ratio, with the band version and effective date"
    internal_comparators: "what the existing team is paid at this level, which is where an offer creates a compression problem"
    approval_chain: []                 # each approver, authority level, and state
    contingencies: "background check, right to work, references, immigration, with those that must clear before a start date"
    expiry: "date"
    start_date: "date, and what it is contingent on"
    state: "modeled | approved | extended | accepted | declined | rescinded"
    decline_reason: "as the candidate gave it, not as it was interpreted"

  employee:
    employee_id: ""
    hire_date: ""
    seniority_date: "where it differs from hire date, because entitlements run from it"
    manager: ""
    org_unit: ""
    location: ""
    employment_basis: ""
    level_and_grade: "with the effective date of the current placement"
    tenure_in_level: ""
    current_pay: "amount, currency, basis, and the effective date it took"
    compa_ratio: "with the band version behind it"
    work_authorization_expiry: "date, or not_applicable"
    record_changes: []                 # each with the field, the old and new value, the effective date, and the approval behind it

  onboarding:
    plan_state: "drafted | in_progress | complete"
    pre_start_items: "provisioning, equipment, and access requests, with owners"
    eligibility_verification: "the statutory window it must complete inside, and its state"
    day_one: "what happens, and who owns it"
    ramp_milestones: "at thirty, sixty, and ninety days, written as observable outcomes"
    manager_plan: "what the manager has committed to, and when"
    buddy_or_mentor: ""
    training_and_acknowledgments: "required policy acknowledgments with their completion state"
    early_attrition_signals: "what has actually been observed, or none_observed"

  performance:
    cycle: "the review period and the scheme in force"
    rating_scheme: "the scale, and what each point is defined to mean"
    population: "who is in the cycle, including who is excluded for tenure or leave and on what rule"
    ratings: []                        # each with the employee, the proposed rating, and the evidence behind it
    evidence_quality: "where a rating rests on observed work against where it rests on impression"
    write_up_state: "drafted | reviewed | approved | communicated"
    self_assessment: "captured, or not_collected"
    upward_and_peer_input: "with the source and whether it was attributed or anonymous"
    performance_concerns: []           # each with the documented history behind it, or undocumented

  calibration:
    session: "the group calibrated and who was in the room"
    distribution: "before and after, with the guidance in force stated as guidance or as a constraint"
    movements: []                      # each with the employee, the direction, and the reason recorded at the time
    consistency_checks: "manager-to-manager variance, and any pattern by tenure, level, location, or population where the counts support the read"
    unresolved: "ratings the session did not settle, kept open rather than defaulted"
    approval_state: "pending | granted | denied"
    communicated: "true | false"

  promotion:
    candidates: []                     # each with the level being sought and the criteria met and unmet
    criteria_source: "the level guide version the case is argued against"
    packet_state: "drafted | in_review | approved | denied | deferred"
    evidence: "the work at the next level that has already been performed, with when"
    calibrated_against: "the peer set at the target level"
    comp_impact: "the increase, the resulting band position, and its approval state"
    effective_date: ""
    denial_reason: "written so it can be repeated to the person and stand up when it is"

  talent_review:
    critical_roles: []                 # each with what it is critical to, not merely who is senior
    succession: []                     # each role with ready-now, ready-later, and no-successor stated plainly
    key_person_risk: "the roles with a single point of failure, and what would happen next week"
    development_plans: []              # each with the named gap, the action, the owner, and the date
    potential_assessments: "with the criteria applied and their known subjectivity stated"
    internal_mobility: "moves considered, blocked, or in flight, with the blocker named"

  manager_enablement:
    manager_population: "who is in scope, including new managers and managers of managers"
    capability_gaps: "with the evidence behind each, such as review write-up quality, survey scores, or attrition on the team"
    cadence: "one-to-ones, feedback, and check-in expectations as they are actually set"
    cycle_support: "what managers need for the cycle in flight, at the point they need it"
    escalation_paths: "what a manager does with a case that is not theirs to handle"
    new_manager_transitions: []        # each with the date, the team inherited, and the support attached

  engagement:
    instrument: "the survey and its version, with whether items are comparable to prior runs"
    population_and_response_rate: "invited, responded, and the rate, with any group where the rate makes the result unreadable"
    confidentiality_threshold: "the minimum group size for reporting, and whether complementary suppression was applied"
    scores: []                         # each with the item or index, the cut, and the comparison period
    verbatim_themes: "themed without reproducing text that identifies its author"
    drivers: "what the analysis actually supports as associated with the outcome, distinguished from what leaders expect"
    action_plans: []                   # each with the owner, the commitment, and the date
    retention_risk: "the roles and populations at risk, with the signal behind each, or not_established"
    attrition: "voluntary, involuntary, regretted and unregretted, each with its definition and denominator"

  compensation:
    cycle: "the review period, its effective date, and the budget pool with what the pool is a percentage of"
    structure_version: "the band set in force, with its effective date and geographic differentials"
    market_data: "the survey, the cut, its effective date, and the aging applied"
    band_refresh: "what moved, by how much, and what it does to people now below range"
    merit_model: "the matrix or rule, and how performance, band position, and tenure enter it"
    proposed_changes: []               # each with the employee, the increase, the resulting band position, and the rationale
    promotion_increases: "held separately from merit, because they are a different decision funded differently"
    off_cycle_and_retention: "with the approval each required"
    compression_and_inversion: "where new hires or promotions have overtaken existing staff, with the affected people identified"
    transparency_obligations: "what must be disclosed in each jurisdiction, and to whom"

  pay_equity:
    cohorts: "the comparison groups, and the basis on which people were grouped as doing comparable work"
    method: "the analysis run, its controls, and what those controls legitimately explain"
    findings: "gaps with their size, direction, and statistical support, or below_threshold"
    unexplained_gap: "what the controls do not account for"
    remediation: "proposed adjustments, their cost, and their approval state"
    privilege_state: "whether the analysis is being run under legal privilege, which changes who may see it"
    prior_analysis: "the last run, its findings, and what happened to them"

  policy:
    policy_ref: ""
    version_and_effective_date: ""
    jurisdictions_covered: []
    change_summary: "what changes, and what it changes for people who relied on the prior version"
    consultation_required: "works council, union, or none, with the trigger"
    acknowledgment_model: "who must acknowledge, by when, and how it is recorded"
    exceptions: []                     # each with the approver and the precedent it sets
    conflicts: "where the draft contradicts an existing policy, a contract, or a local statutory floor"

  er_case:
    case_id: ""
    intake_date: ""
    reported_by: "named, anonymous, or third party"
    allegation: "as reported, in the reporter's terms"
    parties: "reporting party, responding party, and witnesses, held at the case confidentiality tier"
    protected_activity: "true | false | unknown, because it sets the retaliation window and the review path"
    interim_measures: "what was put in place while the case runs, and whether it disadvantages the reporting party"
    investigation_plan: "scope, interviews, and documents, with what is deliberately out of scope"
    evidence: []                       # each with what it is, where it came from, and when it was collected
    standard_of_proof: "the standard applied, stated explicitly"
    findings: "substantiated, unsubstantiated, or inconclusive, per allegation rather than for the case as a whole"
    outcome: "the recommended action and the approval it needs"
    privilege_state: "whether the file is privileged, and what breaks that privilege"
    retaliation_monitoring: "the window, the owner, and what is being watched"
    closure_communication: "what each party is told, which is not the same thing for each"

  leave_case:
    case_id: ""
    leave_type: "the statutory or company category, named against the jurisdiction that grants it"
    entitlement: "the amount available, the window it runs in, and how it was computed"
    dates: "requested, approved, taken, and expected return"
    job_protection: "the protection that applies and when it ends"
    pay_treatment: "paid, partially paid, or unpaid, with the source of each component"
    accommodation_request: "the limitation as it affects the work, recorded without the diagnosis"
    interactive_process: []            # each exchange with its date, what was proposed, and by whom
    medical_information: "held separately from the personnel file, with who has access"
    return_to_work: "the plan, any restriction, and its review date"
    coordination: "payroll, benefits, and manager notifications, with what each is told"

  separation:
    separation_type: "resignation | involuntary_performance | involuntary_conduct | reduction_in_force | end_of_fixed_term | retirement | mutual"
    documented_basis: "the record that exists, distinguished from the account being given now"
    notice: "the notice required and the notice given, with the source of the requirement"
    last_day: "and whether it is a working day or a payroll date"
    final_pay: "components, and the jurisdiction's timing rule for delivering them"
    accrued_time_and_benefits: "treatment, and the source of it"
    severance_and_release: "terms, consideration and revocation periods, and their approval state"
    approvals: []                      # each approver, authority level, and state, including employment law review where required
    rif_selection: "the criteria fixed before names, the pool, and the adverse impact read on the resulting slate"
    access_revocation: "the schedule, tied to the conversation rather than preceding it"
    knowledge_transfer: "what only this person holds, and who receives it"
    exit_interview: "conducted, declined, or not_offered, with what was said kept distinct from what was concluded"
    rehire_eligibility: "with who set it and on what basis"

  metrics:
    - metric: "headcount | time to fill | time to hire | offer acceptance rate | pass-through by stage | quality of hire | voluntary attrition | regretted attrition | internal mobility rate | promotion rate | compa-ratio distribution | pay gap | engagement index | response rate | absence rate | cost per hire | span of control"
      value: ""
      definition: "the definition in force, written out, because each of these has several defensible ones"
      population: "what it was computed over, including exclusions"
      denominator: "stated explicitly, because starting, average, and ending headcount give different answers"
      window: ""
      as_of: "date"
      source_system: ""
      reporting_threshold: "the minimum cell size applied, and whether suppression was complementary"
      comparison: "the prior period, and what changed in the population between them"

  approvals:
    - action: "the action requiring authorization"
      approver: "named human, or unknown"
      authority_level: "what the org requires for this action at this reach"
      state: "granted | pending | denied"
      dated: "when it was granted"
  source_facts:
    - fact: "source-backed fact"
      source: "employment_agreement | offer_letter | collective_agreement | statute_or_regulation | hris | payroll | equity_administration | ats | interview_scorecard | performance_record | case_file | policy_document | compensation_survey | survey_platform | reporting_layer | manager_statement | employee_statement | user | unknown"
      as_of: "the date the source was read, because these records are effective-dated"
  assumptions:
    - assumption: "what was assumed"
      affects: "the requisition, role, candidate, employee, cohort, cycle, case, or metric it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. The executed employment agreement, offer letter, and any collective or works council agreement bind what the company actually promised this person. A term in a contract outranks the handbook that came after it and the practice that grew up around it.
2. Statute and regulation in the jurisdiction of employment set floors that no policy lowers and no contract waives. Where the handbook is more generous than the floor, the handbook applies; where it is less, the floor does.
3. The human resources system of record is authoritative for employment status, dates, level, grade, manager, org placement, and pay as of a date. Every fact from it is effective-dated, and a value read without its date is a value for an unknown year.
4. Payroll and equity administration records are authoritative for what was actually paid and actually granted, which is not always what the offer letter said or what the system of record shows.
5. Contemporaneous documented records are authoritative for what happened at the time: the applicant tracking record with its disposition codes, interview scorecards as written on the day, performance write-ups, documented conversations, case files, and acknowledgment records.
6. Published policy and the handbook are authoritative for the rule in force, at the version effective on the relevant date rather than the version live today.
7. Market compensation survey data is authoritative for the market only within its own scope, carrying the survey, the cut, the effective date, and the aging factor applied to it.
8. Recollection and characterization, whether from a manager, an employee, a colleague, or a candidate, is authoritative for what that person says. It is not evidence of what happened.

The distance between layer 8 and layer 5 is where most real people findings live: the documented performance problem with no document, the "everyone knows" that appears in no record, the promotion denied for a reason that contradicts the written rating, the band nobody has refreshed in three years while every offer landed above it, the leave that was verbally approved and never entered. Where a lower layer contradicts a higher one on a load-bearing fact, record both readings against the field. Do not resolve toward the reading that lets the decision proceed.

## Evidence discipline

- Every person-level fact carries its as-of date. Records here are effective-dated, so a level, a manager, or a pay figure quoted without a date describes an employee who may not exist any more.
- Compensation is stated with its currency, its basis, and its period: annualized against actual paid, full-time equivalent against as-worked. Part-time employees, mid-year hires, and mid-year changes break every naive average, and the fix is stating the basis rather than picking the flattering one.
- A pay range is quoted with its version, its effective date, and its geographic differential. A market percentile carries the survey, the cut by industry, size, and geography, the effective date, and the aging applied. "At market" without those is a preference.
- A performance rating is a claim about a defined period against a defined scheme, and the write-up behind it is the artifact that gets read in a dispute. "Underperforming" is a conclusion; the record needs the work that was observed, when, and against what expectation.
- Attrition carries its definition every time: voluntary against involuntary, regretted against unregretted with who decides regretted, whether transfers, fixed-term endings, interns, and acquired populations are counted, and whether the denominator is starting, average, or ending headcount. The same year moves by a third on those choices alone.
- Time to fill and time to hire are different clocks with different start events, and they differ by weeks. Naming which one is reported is the difference between a comparable number and a number.
- Survey results carry the instrument, the invited population, the response count, the response rate, and the minimum reporting threshold. A team score for a group of four identifies the people in it, and suppressing one cell while publishing its siblings and the total lets anyone recover it by subtraction.
- Self-identification data is voluntary, is never inferred, and is held apart from any individual hiring, rating, promotion, or selection record. It appears in aggregate representation reporting above the reporting threshold, and nowhere else.
- Medical information, accommodation detail, and leave reason are held separately from the personnel file. A manager receives the restriction and the dates, not the condition behind them.
- An investigation record states what each party said, what was corroborated by something other than an account, the standard of proof applied, and what was not established. Unsubstantiated is not the same finding as false, and collapsing them is how a reporting party learns not to report.
- Headcount reconciles to the system of record on a stated date, and states whether contractors, interns, employees on leave, and accepted-but-not-started hires are counted.
- An interview scorecard records what the candidate did or said and the date it was written. A scorecard written after the debrief is a record of the debrief.
- A promotion or a denial is written so it can be repeated to the person, because it will be. A reason that cannot survive being said out loud to the employee is not a reason, it is a rationale.
- Retaliation exposure runs from the date of the protected activity, and it does not end when the complaint is resolved. Any adverse action touching that person afterward is read against that date.
- A policy is quoted at the version in force on the date the events happened, not the version live today, and its acknowledgment record is what establishes the person was on notice.
- Jurisdiction is attached to every obligation. A rule that is true for the headquarters population and asserted for everyone is the most common way this suite gets something expensively wrong.

## Mandated sequences

Most work in this suite has no required order. These have one, because each involves an act that cannot be taken back, a document whose creation date is itself evidence, or a statutory clock that runs whether or not anyone is watching it. Each carries the reason it is ordered, so a later editor does not read it as scaffolding and strip it.

**Requisition approval and budget before candidates are engaged.** A candidate engaged against an unapproved opening is a person being given a reason to leave their current job by a company that may not be able to hire them. The cost of the mistake lands on them, and it lands on the market's opinion of the company for years.

**Level, band, and posting obligations before the role is posted.** Where a jurisdiction requires a good-faith pay range in the posting, the range is a legal content requirement rather than a formatting step, and a range constructed after the posting went live is both a disclosure problem and an anchor that every subsequent offer negotiates against.

**The rubric before the assessment.** Competencies, level anchors, and the scorecard are fixed before candidates are assessed against them. A rubric written afterward is a rationalization of a decision already made, it destroys comparability between candidates who were assessed under different unstated standards, and in a challenge the creation dates of those documents are discoverable and are usually the first thing requested.

**Independent scorecards before the debrief.** Each interviewer records their evidence and their recommendation before hearing anyone else's. Once a senior voice speaks first, the remaining assessments converge on it, and a loop of five observations becomes one observation repeated five times with the appearance of consensus.

**Employment eligibility verification after acceptance and inside the statutory window.** Requesting documents earlier, or requesting specific documents rather than accepting what the rules permit, is itself a discrimination exposure, and completing it late is a separate one. The window runs from the start date and does not pause for onboarding logistics.

**Calibration and approval before a rating is communicated.** A rating spoken to an employee cannot be revised downward afterward without doing more damage than the original error, and it becomes the basis on which that person makes decisions about staying. Calibration exists to make ratings comparable across managers, which is impossible after they have been delivered.

**Investigation before adverse action.** Findings precede discipline, in that order, on the record. A discipline decision reached before the investigation makes the investigation a formality, and the file shows the sequence in dates that nobody can rearrange later. Interim measures during a case protect the reporting party without disadvantaging them, because moving the reporter rather than the responding party is itself an adverse action.

**Pay equity analysis before the cycle closes.** Once increases are approved, communicated, and paid, remediation becomes a second and visible correction, and the disparity that shipped is now documented as having been reviewed and released. Running the analysis while the model is still adjustable is the only point at which it is cheap.

**Selection criteria before names in a reduction in force.** The criteria are fixed and documented, then applied, then the resulting slate is tested for adverse impact before anyone is notified. Selecting individuals first and reasoning backward to criteria is precisely the pattern a disparate impact claim is built from, and the order in which those documents were created is discoverable.

**The involuntary separation sequence, which is ordered because most of its steps are irreversible on the day they happen:**

1. Establish the documented basis from the record that exists, distinguished from the account being given now.
2. Obtain the approvals the organization requires, including employment law review where the case touches protected activity, a leave, an accommodation, a complaint, or a jurisdiction with notice or consultation obligations.
3. Compute final pay, accrued time, notice, and statutory entitlements against the jurisdiction's timing rule before the date is set, because several jurisdictions require final pay at the moment of separation and impose penalties per day afterward.
4. Hold the conversation, with the terms in writing and the release, where one is offered, carrying its consideration and revocation periods.
5. Revoke access on a schedule tied to that conversation.
6. Complete the record: the coded separation reason, the documents retained, the rehire eligibility, and the knowledge transfer.

Reversing steps 4 and 5 means the person learns they have been terminated from a locked laptop, which is both a cruelty and an admission. Reversing 2 and 4 leaves the company defending a decision nobody authorized, and step 3 sits before the date because a final pay figure computed after the last day is already late in the jurisdictions that count.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with their as-of dates, its labeled assumptions, the jurisdiction each obligation was resolved against, and the approval state of anything it prepared that touches pay, standing, or employment. Section headings with the contents deferred mean the stage did not run. Later stages trust the packet rather than re-reading the systems, so an optimistic completion marker propagates from a level placement into a band, from a band into an offer, and from an offer into a compression problem across a whole team that nobody sees until the next cycle.

## Parallel surface

Independent items fan out and are parallel-safe: requisitions in a plan, roles being leveled, job descriptions being drafted, sourcing channels being assessed, candidates in a pipeline, scorecards within a loop, employees in a review population, promotion packets in a cycle, managers in an enablement cohort, jurisdictions being checked against one policy, policies being checked against one jurisdiction, survey verbatims being themed, exit interviews being coded, org units in a workforce plan, and leave cases being assessed against their separate entitlements.

Aggregation and adjudication are single passes after the fan-out returns. Calibration is a single pass over the whole population by definition: a distribution cannot be assembled from independently rated individuals, which is the entire reason the session exists. Merit allocation is a single pass because the budget is finite and every increase competes with the others. Pay equity is a single pass because it is a comparison across people rather than a property of any one of them. The reduction in force slate and its adverse impact read are single passes over the whole slate. Survey suppression is a single pass because whether a cell is safe depends on every other cell published alongside it. Headcount reconciliation is one pass against one date. And within a single employee relations case the investigation is sequential rather than parallel, because what one witness says determines who else has to be interviewed and what they have to be asked.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what the person, the population, or the company is exposed to if the workflow continues anyway>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact fact, or both readings where sources disagree>
Sources attempted: <what was queried and what it returned, with the as-of date of anything that was read>
Running clock: <every statutory, contractual, or committed deadline still running, with its start date and its due date; none, where none applies>
People affected: <the requisition, candidate, employee, cohort, or population the blocked decision sits on, named at the confidentiality tier of the artifact>
Jurisdiction: <the location whose rules govern the blocked decision, or not established>
Required approval or access: <named approver role and authority level, or the system and scope needed>
Proceeding meanwhile: <reversible work that does not depend on the blocked fact>
Preserved packet: <full people_packet>
Resume prompt: <prompt that restarts the workflow once the fact or approval arrives>
```

A halt never pauses a statutory clock, a notice period, a leave entitlement window, a release consideration period, or a commitment already made to a person. Where one is running, the halt says so on its own line, states the due date, and names who has to act now rather than when the blocking fact arrives.

A halt justified by not knowing something is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the requisition, role, candidate, employee, cohort, cycle, case, or metric it affects.

## Stage contracts

`references/stage-contracts.md` gives each desk its required inputs, the outputs it owns, its handoff target, and the hard halt specific to that stage.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
