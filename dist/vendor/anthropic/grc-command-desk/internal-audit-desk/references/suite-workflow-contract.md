# GRC Suite Workflow Contract

This file defines how GRC Command Desk skills run as one continuous program of work instead of behaving as isolated one-off prompts. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is assurance: what the organization is obligated to do, what controls it says carry those obligations, whether those controls actually operated over a period, what evidence proves it, who accepted the risk where they did not, and what the organization tells auditors, customers, regulators, and its own board about all of it. The packet therefore carries evidence state and approval state alongside control state, because the distinguishing failure of this domain is a register that looks complete and is not backed by anything.

## Continuity rule

A desk that has the facts to run the next stage runs it. A run that ends at "you should now perform a gap assessment" or "consider collecting evidence for these controls" is a routing note, not GRC work; it hands the sequencing problem back to the person who asked for the assessment. Complete the current stage, update `grc_packet`, and continue until the requested outcome exists or a hard halt applies.

Three things are never continued through: an action that alters the system of record or the audit trail, a statement that leaves the organization without its named approver, and a conclusion that no evidence supports. Everything else continues, with the assumption labeled inline against the control, risk, or finding it affects.

## Action boundary

This suite produces registers, mappings, assessments, test results, evidence packages, plans, responses, and reporting packets. It does not approve a risk acceptance, grant or extend an exception, publish a policy, close a finding, sign a management representation, answer an auditor on the record, distribute an attestation, or change a control in a live system. For those actions the desk prepares the exact item, the authority level it requires, and what it commits the organization to, then stops at the gate. The person with the authority to sign is the one who signs.

Editing a prior period's workpaper, overwriting collected evidence, backdating a record, or changing a closed finding is outside the boundary in every mode. The audit trail is itself an assurance artifact, and a repaired trail is worth less than a gap in one.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a crosswalk, a policy review, a vendor tier decision, or a control test.
- `workflow_run`: the default for anything phrased as readiness, an assessment, an audit, a remediation effort, a risk review, or a reporting cycle. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `grc_packet`, a halt-resume prompt, or an earlier report. Re-read any evidence whose `collected_on` predates the current observation period, and any register row whose `review_due` has passed, rather than trusting the carried value. Control state decays, and a carried conclusion inherits a date it no longer has.
- `halt`: a hard halt class applies. Return the halt format below with the packet intact and the reversible work already done.
- `diagnostic`: required evidence sources cannot be reached. Report what was reachable, what was not, and precisely which control conclusions, populations, or coverage figures each gap makes unavailable. Do not backfill an unreachable source with its expected values.

## Engagement types

Every request carries exactly one type, because the type sets the approval surface, the evidence standard, and who eventually reads the output: `readiness`, `audit_cycle`, `risk_assessment`, `policy_review`, `evidence_request`, `control_test`, `third_party_review`, `continuity_exercise`, `internal_audit`, `regulatory_change`, `customer_assurance`, `committee_reporting`, `unknown`.

The distinction that matters most is whether the output leaves the organization. An internal gap assessment tolerates working assumptions labeled as such. An auditor response, a questionnaire answer, and a committee packet do not, because they are consumed as assertions by people who cannot see the assumption.

## The GRC packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `not_tested`, and `unable_to_test` are legitimate values; an invented control identifier or approver name is not.

```yaml
grc_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  engagement_type: "readiness | audit_cycle | risk_assessment | policy_review | evidence_request | control_test | third_party_review | continuity_exercise | internal_audit | regulatory_change | customer_assurance | committee_reporting | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  obligations:
    - obligation_id: "OB-01"
      source_type: "regulation | statute | contract | framework | customer_commitment | internal_policy"
      citation: "the clause, article, or criterion a source actually names"
      applies_to: []                  # entities, systems, data types, jurisdictions
      effective_date: "date from the source, or unknown"
      owner: "accountable role or named human, or unknown"
      applicability: "applicable | not_applicable | under_analysis"
      basis: "what established applicability, including who determined it"

  scope:
    engagement: "the audit, certification, or assessment named by a source"
    criteria_set: []                  # criteria, annex controls, or requirements with framework version
    in_scope_systems: []
    in_scope_entities: []
    locations: []
    subservice_orgs:
      - name: "provider"
        method: "carve_out | inclusive | unknown"
        cuecs: []                     # complementary user entity controls the report pushes back to customers
    out_of_scope:
      - item: "what was excluded"
        rationale: "why"
        set_by: "who decided"
    period:
      type: "point_in_time | period_of_time | unknown"
      start: "date, or unknown"
      end: "date, or unknown"

  control_library:
    - control_id: "C-01"
      title: "control"
      objective: "what it is meant to prevent or detect"
      owner: "named owner, or unknown"
      frequency: "continuous | daily | weekly | monthly | quarterly | annual | event_driven | unknown"
      control_type: "preventive | detective | corrective"
      automation: "automated | manual | hybrid"
      key_control: "true | false | undetermined"
      evidence_source: "the system that produces its evidence"
      design_state: "designed | partial | not_designed | unverified"

  crosswalk:
    - control_id: "C-01"
      framework: "framework and version named by a source"
      criteria_ref: "criterion or annex control identifier"
      coverage: "full | partial | none"
      mapping_basis: "published_mapping | practitioner_judgment"
      gap_note: "what the mapping does not cover, where coverage is partial"

  risks:
    - risk_id: "R-01"
      description: "the risk stated as a consequence, not a topic"
      category: "category from the org taxonomy, or unknown"
      inherent: {likelihood: "", impact: "", score: "", scale: "the rating scale it came from"}
      residual: {likelihood: "", impact: "", score: "", scale: ""}
      treatment: "mitigate | transfer | avoid | accept | undecided"
      linked_controls: []
      owner: "named risk owner, or unknown"
      review_due: "date, or unknown"

  risk_acceptances:
    - acceptance_id: "RA-01"
      covers: "risk_id"
      approver: "named human; never inferred from a role chart"
      authority_level: "the level the org rubric requires for this exposure"
      rationale: "why the exposure is acceptable"
      granted_on: "date"
      expires: "date, or unknown"

  policies:
    - policy_id: "P-01"
      title: "policy"
      version: "version"
      status: "draft | in_review | approved | published | retired"
      approver: "named approver, or unknown"
      approved_on: "date, or unknown"
      next_review_due: "date, or unknown"
      acknowledgment: "rate with the population it was measured over, or unknown"
      mapped_controls: []

  evidence:
    - evidence_id: "E-01"
      control_id: "C-01"
      description: "what the artifact shows"
      artifact_ref: "locator in the evidence repository; never the sensitive content itself"
      period_covered: "the dates the artifact actually covers"
      collected_by: "who"
      collected_on: "when"
      population_source: "the system and query the population came from"
      completeness_basis: "how the population was shown complete and accurate, or unknown"
      state: "collected | requested | unavailable | stale | rejected_by_auditor"

  tests:
    - test_id: "T-01"
      control_id: "C-01"
      objective: "design | operating_effectiveness"
      method: "inquiry | observation | inspection | reperformance"
      population_size: "count, or unknown"
      sample_size: "count, or unknown"
      sampling_basis: "the method and the source that set the size"
      deviations: "count"
      conclusion: "effective | deficient | not_tested | unable_to_test"
      tested_by: "who"
      tested_on: "when"

  findings:
    - finding_id: "F-01"
      origin: "self_assessment | internal_audit | external_audit | continuous_monitoring | control_test | questionnaire | incident | regulator"
      condition: "what was observed"
      criteria_ref: "the requirement it fails against"
      cause: "why it happened, where a source establishes it"
      effect: "the consequence, stated in exposure terms"
      severity: "value plus the rubric it came from"
      classification: "observation | deficiency | significant_deficiency | material_weakness | nonconformity"
      status: "open | in_remediation | remediated | closed | accepted"
      owner: "named owner, or unknown"
      due: "date derived from a stated policy or auditor deadline, or unknown"

  remediation:
    - cap_id: "CAP-01"
      covers: "finding_id"
      actions: []
      owner: "named owner, or unknown"
      due: "date"
      compensating_control: "what carries the exposure meanwhile, or none"
      validation_state: "not_validated | evidence_pending | validated"
      validated_by: "who confirmed the control now operates, or unknown"

  exceptions:
    - exception_id: "X-01"
      covers: "control_id or policy_id"
      reason: "why the requirement is not met"
      compensating_control: "what carries the exposure"
      approver: "named human"
      granted_on: "date"
      expires: "date; an exception with no expiry is a silent policy change"

  monitoring:
    - monitor_id: "M-01"
      control_id: "C-01"
      check: "what is evaluated"
      frequency: "how often it runs"
      signal_source: "the system it reads"
      state: "live | proposed | failing | blocked_on_source"
      last_result: "result plus when it ran, or unknown"
      coverage: "the share of the control population it observes, with the basis"

  third_parties:
    - vendor: "name"
      tier: "criticality tier from the org rubric"
      data_shared: []
      access_model: "how it reaches systems or data"
      attestation:
        type: "report or certificate type named by a source, or none"
        scope: "what it covered"
        period: "the period or validity window it covers"
        exceptions_noted: []
        bridge_letter: "covers the gap to today, or none"
      cuecs: []                       # controls the report assigns back to this organization
      review_state: "current | overdue | never | in_progress"
      contract_clauses: []            # right to audit, breach notification, flow-down, retention
      next_review_due: "date, or unknown"

  continuity:
    - process: "business process or service"
      criticality_tier: "tier from the impact analysis"
      committed_rto: "value and the commitment that set it"
      committed_rpo: "value and the commitment that set it"
      demonstrated_rto: "value from the last exercise, or never_tested"
      plan_ref: "plan locator"
      plan_approved_on: "date, or unknown"
      last_exercise:
        date: "date, or never"
        type: "tabletop | functional | full_interruption"
        scope: "what was exercised"
        result: "outcome, including what failed"
      corrective_actions: []

  audit_engagement:
    assessor: "firm or body named by a source, or none"
    engagement_type: "the engagement named by a source"
    request_list:
      open: []
      submitted: []
      accepted: []
      rejected: []                    # with the auditor's stated reason
    walkthroughs: []
    open_questions: []
    report_state: "not_started | fieldwork | draft | management_response | issued"
    exceptions_in_report: []

  attestations:
    - report_type: "report or certificate named by a source"
      scope_statement: "what it asserts coverage over"
      validity: "period or expiry"
      issued_on: "date, or unknown"
      distribution_constraint: "nda_required | customer_portal | public | internal_only"
      bridge_letter_through: "date, or none"

  committee:
    forum: "the governing body this reports to"
    reporting_period: "period"
    metrics:
      - name: "metric"
        value: "measured value"
        source: "where it was computed from"
        as_of: "date"
    escalations: []
    decisions_requested: []           # each with the authority level it needs

  approvals:
    - action: "the action requiring authorization"
      approver: "named human, or unknown"
      authority_level: "what the org rubric requires"
      state: "granted | pending | denied"

  source_facts:
    - fact: "source-backed fact"
      source: "contract | policy_doc | grc_platform | ticket_system | identity_provider | hr_system | cloud_config | log_extract | audit_report | vendor_portal | regulator_publication | user | unknown"
      collected: "when the evidence was read"
  assumptions:
    - assumption: "what was assumed"
      affects: "the control, risk, finding, or answer it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. Executed and signed instruments are authoritative for commitment and approval: contracts and their security schedules, approved policies with their approval record, issued reports and certificates, committee minutes, and signed acceptances. These establish what the organization is bound to and who bound it.
2. System-generated records are authoritative for whether a control operated, bounded by the population they actually cover and the moment they were extracted: configuration exports, ticket and change records, access review results, log extracts, and monitoring output.
3. Published regulatory text and framework criteria are authoritative for what is required. Counsel or the assessor is authoritative for how a requirement applies to this organization, and that interpretation is a source fact with a named interpreter, not an inference.
4. The GRC platform and its registers are authoritative for the program's own record of itself. A register row is a claim about the world and is outranked by layer 2 whenever the two disagree.
5. Control narratives, management assertions, questionnaire responses, and self-assessments are authoritative for what management says. They are not evidence that a control operated.
6. Tickets, chat, and email are decision context and timeline evidence.

The distance between layer 5 and layer 2 is where nearly every real finding in this domain comes from. Where a lower layer contradicts a higher one on a load-bearing fact, record both readings against the field. Do not resolve it toward whichever reading lets the assessment close.

## Evidence discipline

- Every evidence item carries its collection date and the period it actually covers. An undated screenshot proves nothing over an observation period, and a control verified once is not a control that operated monthly.
- A population carries how it was shown complete and accurate. A sample drawn from a population nobody established is not a test result, whatever the deviation count says, because the first thing an assessor re-performs is the population.
- Sample size and sampling method travel with the test and come from the methodology a source states. Do not derive, round, or restate a sample size, confidence level, or deviation threshold that no source set.
- Control conclusions use `effective`, `deficient`, `not_tested`, or `unable_to_test`. Missing evidence yields `not_tested`. "We did not test it" and "it works" are different statements and never collapse into each other.
- Coverage is part of every result. A control set that is 70 percent tested is reported as 70 percent tested, with the untested remainder named rather than averaged away.
- Framework identifiers, criterion references, clause numbers, and version labels are quoted from the published source. A crosswalk row records whether the mapping came from a published mapping or practitioner judgment, because a customer will later rely on it as though it were the former.
- Approvers, risk owners, and control owners are recorded because a source names them. Holding the role that usually approves this is not the same as having approved it.
- Evidence containing personal data, credentials, customer records, or regulated content is referenced by locator. Pulling the content into an artifact creates a second copy in a place with a wider audience and its own retention obligation.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with collection dates, its labeled assumptions, and its residual exposure. Section headings with the contents deferred mean the stage did not run. Later stages trust the packet rather than re-reading the evidence repository, so an optimistic completion marker propagates into a test conclusion and from there into an assertion.

## Parallel surface

Independent items fan out and are parallel-safe: controls, evidence requests, policies, risks, framework mappings, vendors, business processes, findings, obligations, and monitoring checks are each evaluated on their own inputs.

Aggregation is a single pass after the fan-out returns. Deduplicating one deficiency that fails several criteria, computing control coverage or acknowledgment rates across a population, ranking one remediation queue against capacity, rolling residual risk up to a register-level position, drawing a sample across a combined population, and assembling the committee packet are each statements about the whole set and cannot be produced in parallel from parts.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what the organization is exposed to if the workflow continues anyway>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact fact, or both readings when sources disagree>
Sources attempted: <what was queried and what it returned>
Required approval or access: <named approver role and authority level, or the connector and scope needed>
Proceeding meanwhile: <reversible work that does not depend on the blocked fact>
Preserved packet: <full grc_packet>
Resume prompt: <prompt that restarts the workflow once the fact or approval arrives>
```

A halt justified by uncertainty rather than consequence is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the control or finding it affects.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
