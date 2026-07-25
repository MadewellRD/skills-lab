# Privacy Suite Workflow Contract

This file defines how Privacy Data Protection Command Desk skills run as one continuous program of work instead of behaving as isolated one-off prompts. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is personal data: what the organization holds, why it is permitted to hold it, what it told people it would do with it, who else touches it, where it crosses a border, how long it stays, what happens when a person asks about it, and what happens when it reaches somewhere it should not have. The packet therefore carries evidence state, clock state, and approval state alongside the compliance record, because the distinguishing failure of this domain is a register that is complete on paper and traceable to nothing in the systems it describes.

## Continuity rule

A desk that has the facts to run the next stage runs it. A run that ends at "you should now complete a DPIA for this" or "consider reviewing your lawful basis" is a routing note, not privacy work; it hands the sequencing problem back to the person who asked for the assessment. Complete the current stage, update `privacy_packet`, and continue until the requested outcome exists or a hard halt applies.

Three things are never continued through: an irreversible external act such as a filing, a disclosure, or a deletion; a statement that would leave the organization without the named human who authorized it; and a lawfulness or coverage claim that no source supports. Everything else continues, with the assumption labeled inline against the processing activity, request, transfer, or notification it affects.

## Action boundary

This suite produces registers, determinations, assessments, drafts, response packages, schedules, and reporting packets. It does not file a breach notification with a supervisory authority, send a notification to affected individuals, release a rights-request response to a requester, execute a deletion, publish or amend a live privacy notice, execute a data protection agreement or a transfer instrument, change a consent banner or tag configuration in production, or answer a regulator on the record. For those acts the desk prepares the exact item, states the authority level it requires and what it commits the organization to, and stops at the gate.

Editing a signed assessment, amending a breach register entry after the fact, backdating a consent record or an executed agreement, and rewriting a rights-request log to close a missed deadline are outside the boundary in every mode. The privacy record is itself an accountability artifact that a regulator is entitled to inspect, and a repaired record is worth less than an acknowledged gap.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a legitimate interests assessment, a cookie audit, a transfer impact assessment, or a DSAR scope.
- `workflow_run`: the default for anything phrased as a review, an assessment, a program build, a request to handle, an incident, or a readiness question. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `privacy_packet`, a halt-resume prompt, or an earlier assessment. Re-read any tracker scan, data map, consent record, or vendor agreement whose `collected` date predates the last change to the surface it describes, and recompute every deadline rather than trusting the carried value. Tag configurations, sub-processor lists, and statutory clocks all move between readings.
- `halt`: a hard halt class applies. Return the halt format below with the packet intact and the reversible work already done.
- `diagnostic`: required sources cannot be reached. Report what was reachable, what was not, and precisely which coverage figures, lawfulness positions, or affected-population counts each gap makes unavailable. Do not backfill an unreachable system with the data it probably holds.

## Engagement types

Every request carries exactly one type, because the type sets the clock, the approval surface, the evidence standard, and who eventually reads the output: `program_buildout`, `new_processing_review`, `ropa_refresh`, `lawfulness_review`, `notice_update`, `consent_review`, `cookie_audit`, `rights_request`, `retention_review`, `transfer_assessment`, `vendor_onboarding`, `breach_response`, `regulator_inquiry`, `program_reporting`, `unknown`.

Two distinctions matter more than the rest. The first is whether a statutory clock is already running: a rights request, a breach, and a regulator inquiry each carry a deadline that started before the work did, and the deadline does not pause for analysis. The second is whether the output leaves the organization. An internal gap assessment tolerates working assumptions labeled as such. A notice, a DSAR response, a regulator filing, and an answer to a customer questionnaire do not, because they are consumed as assertions by people who cannot see the assumption and, in the case of the individual, cannot check it.

## The privacy packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `undetermined`, `not_assessed`, `never`, and `unknown` are legitimate values; an invented lawful basis, vendor name, affected-record count, or article reference is not.

```yaml
privacy_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  engagement_type: "program_buildout | new_processing_review | ropa_refresh | lawfulness_review | notice_update | consent_review | cookie_audit | rights_request | retention_review | transfer_assessment | vendor_onboarding | breach_response | regulator_inquiry | program_reporting | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  applicability:
    - regime: "the law, regulation, or code a source names, with the provision that brings it into scope"
      entity: "the legal entity the regime attaches to"
      jurisdictions: []
      trigger: "establishment | targeting | monitoring | sectoral | contractual | unknown"
      role: "controller | joint_controller | processor | sub_processor | service_provider | third_party | undetermined"
      role_basis: "who decides purposes and means, and the source that establishes it"
      determined_by: "counsel, privacy office, or unknown; never inferred from an org chart or a contract label"
  accountability_roles:
    dpo: {required: "yes | no | undetermined", appointed: "named role, or unknown", contact_published: "true | false | unknown", basis: "the provision or analysis behind the requirement"}
    representative: {required: "yes | no | undetermined", appointed: "named entity, or unknown", jurisdiction: "where it is established"}
    privacy_contact: "the route an individual or a regulator actually reaches, or unknown"

  processing_activities:              # RoPA rows, keyed to purpose rather than to system
    - activity_id: "PA-01"
      name: "processing activity"
      purpose: "the specific purpose, stated so an individual could recognize it in the notice"
      data_subject_categories: []
      data_categories: []
      special_category: "true | false | undetermined"
      special_category_types: []
      criminal_offence_data: "true | false | undetermined"
      children_involved: "true | false | undetermined"
      lawful_basis: "the basis actually assessed and selected, or undetermined"
      special_category_condition: "the condition relied on, or not_applicable"
      recipients: []
      systems: []
      transfers: []                   # transfer_id references
      retention_ref: "retention schedule row, or unknown"
      security_measures: "described, or unknown"
      owner: "accountable business owner, or unknown"
      source: "what this row was built from"
      last_reviewed: "date, or never"

  data_inventory:
    - system: "system or service"
      data_store: "table, bucket, index, queue, or file share"
      elements: []
      classification: "the org classification label, or unknown"
      identifiability: "identified | pseudonymized | de_identified | aggregated | anonymous | undetermined"
      identifiability_basis: "the technique, the auxiliary data considered, and who assessed re-identification"
      special_category: "true | false | undetermined"
      volume: "record count with the date it was counted, or unknown"
      residency: "where the data physically sits, or unknown"
      discovery_method: "scan | schema_read | interview | vendor_documentation | unknown"
      examined: "true | false"         # false means this system was listed, not read

  data_flows:
    - flow_id: "DF-01"
      from: "system or party"
      to: "system or party"
      direction: "internal | to_processor | to_controller | to_third_party | cross_border"
      data_categories: []
      purpose: "the purpose the flow serves"
      mechanism: "api | batch_file | tag | sdk | replication | export | remote_access | unknown"
      authorization: "the contract, clause, or configuration that permits it, or unknown"

  lawful_bases:
    - activity_id: "PA-01"
      basis: "the basis, or undetermined"
      necessity: "why the purpose cannot be achieved with less, rather than why the processing is useful"
      lia:                            # required wherever legitimate interests is claimed
        purpose_test: ""
        necessity_test: ""
        balancing_test: "the individual's interests, rights, and reasonable expectations weighed against the interest"
        safeguards: []
        objection_route: "how an individual objects, and what happens when they do"
        completed_by: "named human, or not_completed"
        completed_on: "date, or none"
      special_category_condition: "the condition and its own additional requirement, or not_applicable"
      compatible_use:
        original_purpose: ""
        new_purpose: ""
        outcome: "compatible | incompatible | not_assessed"
      basis_changed_from: "prior basis and the date it changed; a mid-processing basis switch is itself a disclosure event"

  notices:
    - notice_id: "N-01"
      surface: "web, app, form, offline channel, or third-party collection point"
      audience: "who reads it"
      version: "version"
      effective_date: "date, or unknown"
      languages: []
      disclosures_covered: []         # identity and contact, purposes, bases, recipients, transfers, retention, rights, withdrawal, complaint route, source where not collected from the individual, automated decisions
      gaps: []                        # the disclosures a regime requires and this notice does not carry
      change_log: "what changed, and whether the change is material enough to require telling existing individuals"
      last_reviewed: "date, or never"

  consent:
    - consent_id: "CN-01"
      purpose: "the specific purpose consented to"
      surface: "where consent was captured"
      granularity: "per_purpose | bundled | unknown"
      capture_record: "timestamp, notice version, the exact wording shown, and the identifier the consent attaches to"
      withdrawal_path: "how a person withdraws, and whether it is as easy as giving it was"
      state: "valid | stale | invalid | withdrawn | never_captured"
      invalid_reason: "pre-ticked, bundled, no wording retained, inherited from superseded text, no withdrawal route, or other"
      refresh_due: "date, or none"
  preference_signals:
    global_privacy_control: "honored | not_honored | unknown"
    opt_out_of_sale_or_share: "state, or unknown"
    sensitive_data_limitation: "state, or unknown"
    enforced_at: "the layer where the signal actually changes behavior, not where it is received"

  trackers:
    - name: "cookie, pixel, tag, or SDK"
      host: "the domain that sets or reads it"
      vendor: "named recipient, or unidentified"
      category: "strictly_necessary | functional | analytics | advertising | unclassified"
      purpose: "what it does, from evidence rather than from the vendor's category"
      storage_duration: "duration, or unknown"
      fires_before_consent: "true | false | unknown"
      observed_where: "the pages or screens it was seen on, including authenticated paths"
      discovered_on: "scan date"
      disposition: "keep | gate | remove | investigate"

  minimization:
    - activity_id: "PA-01"
      field: "the element under review"
      decision: "retain | reduce | drop | pseudonymize | tokenize | aggregate | generalize"
      necessity_basis: "the named purpose the field serves, or none found"
      technique: "the technique applied and where the keys or mapping live"
      re_identification_assessment: "who assessed it, against what auxiliary data, or not_assessed"

  design_reviews:
    - feature: "the change under review"
      stage: "concept | design | build | pre_launch | live"
      privacy_requirements: []        # written as acceptance criteria, not as principles
      default_settings: "the setting as configured, not the setting that is available"
      deceptive_pattern_findings: []
      gate_state: "not_started | in_review | cleared | cleared_with_conditions | blocked"
      conditions: []

  assessments:
    - assessment_id: "AS-01"
      type: "threshold | dpia | pia | legitimate_interests | transfer_impact | automated_decision"
      covers: "activity_id or feature"
      trigger: "the criterion that brought it into scope"
      threshold_outcome: "required | not_required | undetermined"
      necessity_and_proportionality: "measured against the purpose, not against convenience"
      risks:
        - risk: "the harm to the individual, stated as the harm rather than as a control gap"
          likelihood: ""
          severity: ""
          scale: "the rating scale it came from"
      mitigations: []                 # each mapped to the specific risk it reduces
      residual_risk: "value with its scale, after mitigation"
      consulted: []                   # DPO, security, counsel, and the individuals affected or their representatives
      automated_decision:
        present: "true | false | undetermined"
        legal_or_significant_effect: "true | false | undetermined"
        logic_explanation: "what the individual is told about the logic involved"
        human_review_route: "how a person obtains human intervention"
        opt_out_route: "how a person objects or opts out"
      signed_off_by: "named human, or unsigned"
      signed_off_on: "date, or none"
      prior_consultation: "not_required | required | submitted | response_received"
      processing_started_before_assessment: "true | false | unknown"
      review_due: "date, or unknown"

  childrens_data:
    in_scope: "true | false | undetermined"
    audience_basis: "what establishes whether the service is directed to or likely accessed by children"
    age_range: "the range in scope"
    knowledge_standard: "actual | constructive | none | unknown"
    age_assurance_method: "method, plus the data it collects in order to work"
    parental_consent_method: "method and the evidence it produces, or not_applicable"
    high_privacy_defaults: []         # geolocation, profiling, discoverability, nudges, sharing
    restricted_processing: []         # targeted advertising, profiling, and other uses closed off for minors
    transition_rules: "what changes when a user ages into or out of the regime"
    applicable_codes: []

  transfers:
    - transfer_id: "TR-01"
      exporter: "entity"
      importer: "entity"
      importer_role: "controller | processor | sub_processor | undetermined"
      destination_countries: []
      data_categories: []
      mechanism: "adequacy | standard_clauses | uk_addendum | idta | binding_corporate_rules | derogation | none"
      module_or_annex: "the module or annex matching the parties' actual roles"
      executed_on: "date the instrument was signed, or not_executed"
      transfer_impact_assessment:
        completed: "true | false"
        laws_assessed: []
        government_access_analysis: "the specific access powers considered"
        supplementary_measures: []    # each stated against the access route it is meant to defeat
        outcome: "proceed | proceed_with_measures | do_not_proceed | not_assessed"
      onward_transfers: []
      localization_requirement: "the requirement and its source, or none"
      state: "covered | uncovered | under_review"

  processors:
    - vendor: "name"
      role: "processor | sub_processor | joint_controller | service_provider | third_party | undetermined"
      activities: []                  # activity_id references
      data_categories: []
      agreement:
        executed: "true | false | unknown"
        executed_on: "date, or none"
        clause_coverage: []           # instruction-only processing, confidentiality, security, sub-processing, rights assistance, breach assistance, audit, deletion or return
        gaps: []
      sub_processors:
        list: []
        notification_mechanism: "how changes are announced"
        objection_right: "the route and the window, or none"
      audit_rights: "what the agreement actually permits"
      deletion_or_return: "the commitment, tested against what the vendor can technically do"
      transfer_ref: "transfer_id where the vendor sits outside the exporting jurisdiction"
      review_state: "current | overdue | never | in_progress"
      next_review_due: "date, or unknown"

  rights_requests:
    - request_id: "RR-01"
      regime: "the regime the right is exercised under"
      right: "access | rectification | erasure | restriction | portability | objection | opt_out_of_sale_or_share | limit_sensitive_use | automated_decision_review | appeal | unknown"
      requester_type: "data_subject | authorized_agent | parent_or_guardian | unknown"
      received_on: "the date the request arrived, which starts the clock"
      identity_verification:
        method: "what was used"
        assurance_level: "proportionate to what will be disclosed"
        state: "verified | unverified | failed | not_required"
        verified_on: "date, or none"
      deadline: "the statutory date computed from the receipt date and the regime that set it"
      extension: {taken: "true | false", basis: "the ground the regime allows", new_deadline: "date, or none"}
      scope:
        systems_searched: []
        systems_not_searched: []      # named, with the reason; this is not a blank field
        backups_and_archives: "how they were treated and on what basis"
        processors_instructed: []
      exemptions_applied:
        - exemption: "the exemption"
          citation: "the provision it rests on"
          applied_to: "the records or content it covers"
      third_party_data: "how personal data of others in the same records was handled"
      fee_or_refusal: "none | manifestly_unfounded | excessive, with the basis"
      response_state: "intake | verifying | retrieving | in_review | ready_for_release | delivered | refused | appealed"
      delivered_on: "date, or none"
      delivery_channel: "the channel the requester was authenticated on"
      appeal: {received: "true | false", outcome: "", regulator_referral: "true | false"}

  retention:
    - record_class: "the class of record"
      period: "the period"
      basis: "statutory citation, contractual clause, or documented business rationale; convention is not a basis"
      trigger_event: "what starts the clock"
      systems_covered: []
      backups_and_archives: "how the period reaches them, or the expiry cycle that does"
      exports_and_copies: []          # reports, data warehouse copies, vendor-side copies, offline extracts
      disposal_method: "hard_delete | crypto_shred | anonymize | archive_then_delete"
      legal_hold: {active: "true | false", matter: "", scope: "", released_on: "date, or none"}
      state: "defined | scheduled | executed | overdue | blocked_by_hold | undefined"

  deletion_records:
    - deletion_id: "DL-01"
      covers: "request_id or retention record_class"
      hold_check: "performed with its result, or not_performed"
      systems_executed: []
      systems_pending: []
      processors_instructed: []       # with the confirmation received, or none
      verification_basis: "what confirmed absence, and in which system; a closed ticket is not verification"
      exceptions:
        - system: ""
          reason: ""
          retention_basis: "what permits the copy to remain"
      completed_on: "date, or none"

  breaches:
    - incident_id: "IN-01"
      awareness_at: "the moment the organization knew, which is when every clock starts"
      discovered_by: "who or what surfaced it"
      breach_type: "confidentiality | integrity | availability"
      personal_data_involved: "true | false | undetermined"
      data_categories: []
      special_category: "true | false | undetermined"
      affected_subjects: "approximate number with the basis for the estimate, or unknown"
      affected_records: "count with its basis, or unknown"
      cause: "what a source establishes, not what is likely"
      containment_state: "the state and when it was reached"
      mitigating_factors: []          # measures that genuinely reduce risk to individuals, such as keys held apart from the exposed data
      risk_to_individuals:
        likely_consequences: "the harms, stated as harms"
        severity: ""
        likelihood: ""
        method: "the assessment method used"
        outcome: "no_risk | risk | high_risk | undetermined"
      notifiability:
        - regime: ""
          authority: ""
          notifiable: "yes | no | undetermined"
          deadline: "computed from awareness_at"
          basis: "the threshold the determination turns on"
      register_entry: "recorded whether or not it was notifiable, because the register is its own obligation"
      processor_notified_controller_at: "timestamp, or not_applicable"

  notifications:
    - notification_id: "NT-01"
      covers: "incident_id"
      audience: "supervisory_authority | affected_individuals | controller | partner | other_regulator"
      authority: "the named authority, or not_applicable"
      phased: "true | false"          # a filing made on incomplete facts, with what is still under investigation stated
      content_summary: "nature, categories and approximate numbers, contact point, likely consequences, measures taken"
      submitted_on: "date, or none"
      reference: "the authority's reference, or none"
      individual_notification: {required: "yes | no | undetermined", method: "", sent_on: "date, or none", substitute_notice_basis: "why direct contact was not possible, or not_applicable"}
      approved_by: "named human who authorized the filing, or pending"

  program_metrics:
    - metric: "name"
      value: "measured value"
      computed_basis: "the query, export, or count behind it"
      population: "what it was measured over"
      as_of: "date"

  approvals:
    - action: "the action requiring authorization"
      approver: "named human, or unknown"
      authority_level: "what the org or the regime requires"
      state: "granted | pending | denied"

  source_facts:
    - fact: "source-backed fact"
      source: "regulation_text | regulator_guidance | executed_contract | privacy_notice | ropa | consent_record | cmp_export | tag_scan | data_catalog | schema | system_scan | log_extract | ticket_system | vendor_documentation | counsel_position | user | unknown"
      collected: "when the source was read"
  assumptions:
    - assumption: "what was assumed"
      affects: "the activity, basis, request, transfer, notification, or metric it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  active_clocks:
    - obligation: "what is due"
      started: "the date the clock started and the event that started it"
      due: "the statutory or contractual date"
  ready_to_continue: true
```

## Source hierarchy

1. Executed and issued instruments bind, and establish what the organization committed to and to whom: signed data protection agreements and transfer instruments with their dates and modules, published notices at the version and effective date they carried, consent records including the wording shown, regulator correspondence, and recorded approvals.
2. System-generated records are authoritative for what actually happens to data, bounded by what they covered and when they were taken: schema and catalog exports, tag and cookie scans taken on the live page, tag manager and CMP configuration, data flow configuration, access and query logs, deletion job output, and backup inventories.
3. Published legal text, regulator guidance, and codes of practice are authoritative for what is required. Counsel or the supervisory authority is authoritative for how a requirement applies to this organization, and that interpretation is a source fact with a named interpreter, never an inference drawn from the text.
4. The privacy registers are authoritative for the program's record of itself: the RoPA, the assessment library, the breach register, the rights request log, the retention schedule. A register row is a claim about the world and is outranked by layer 2 wherever the two disagree.
5. Notices as descriptions of practice, questionnaire answers, vendor privacy statements, internal policies, and self-assessments are authoritative for what someone said. They are not evidence of what a system does.
6. Tickets, chat, and email are timeline and decision context.

The distance between layer 5 and layer 2 is where nearly every real privacy finding comes from: the notice that lists three recipients while the tag scan shows eleven, the vendor questionnaire that promises regional storage while the console shows a global replica. Where a lower layer contradicts a higher one on a load-bearing fact, record both readings against the field. Do not resolve it toward whichever reading leaves the processing lawful.

## Evidence discipline

- A lawful basis is recorded because someone assessed and selected it, not because the column needed a value. Legitimate interests with no completed balancing test is `undetermined`, and an activity where no basis holds is recorded as unlawful processing rather than as a documentation gap.
- The line between pseudonymized and anonymous is an assessment, not a label. Pseudonymized data is still personal data. Anonymous is claimed only against a stated re-identification analysis naming the auxiliary data considered and who performed it, because the anonymous label removes a dataset from every other control in this suite at once.
- A consent record is the timestamp, the notice version, the exact wording shown, the granularity, and the identifier it attaches to. A boolean column proves that a flag is set, not that a person agreed to something specific.
- Tracker behavior is measured on the live surface, not read from the tag manager. Configuration states intent; the scan states what fired. An unidentified tag is recorded as unidentified rather than attributed to the vendor it resembles.
- Deadlines are computed from the regime and the recorded start event, and both dates travel with the obligation. A deadline nobody can trace back to a receipt or awareness timestamp is not a deadline.
- Coverage travels with every search and every map. A rights request names the systems searched and the systems not searched, including backups, archives, exports, and processor-held copies. A data map that examined nine of forty systems is a map of nine systems.
- Deletion is `executed` only where a system confirms absence. A closed ticket records that someone was asked. Where a platform cannot hard delete, the method and its limit are recorded rather than rounded up to deletion.
- Breach figures carry the basis for the estimate. "Approximately 4,000, derived from the export row count" is a legitimate value; a round number nobody computed is not.
- Article, section, clause, and recital references are quoted from the published text and attached only to conclusions the provision actually carries. A citation borrowed from a similar case is a fabricated authority.
- Transfer state is `covered` only where the instrument exists and was executed, with the module matching the parties' real roles. Drafted is not signed, and the wrong module is not coverage.
- Personal data itself stays out of the packet and out of artifacts. Reference it by system, locator, and category. Copying a requester's own record into a working artifact creates a second copy in a place with a wider audience, its own retention clock, and its own breach exposure.

## Mandated sequences

Most work in this suite has no required order. These six do, because each involves an act that cannot be undone or a clock that has already started. Each carries the reason it is ordered, so a later editor does not read it as scaffolding and remove it.

**Consent before the tracker fires.** Non-essential cookies, pixels, and SDKs are set or read only after consent is captured. The placement is the regulated act, so a tracker that already fired cannot be cured by consent collected afterward.

**Identity verification before disclosure.** A rights request is verified to an assurance level proportionate to what will be disclosed, and only then is anything released. Disclosing to an unverified requester is a breach committed while answering a request made under the same law, and a disclosure cannot be withdrawn.

**Assessment before processing begins.** Where a threshold assessment says a full assessment is required, it is completed before the processing starts, and where high residual risk survives mitigation the prior consultation happens before the processing proceeds. The obligation attaches to the timing: an assessment written after launch documents an exposure rather than preventing one, and the packet records that the processing started first.

**Executed agreement before the processor receives data.** The data protection agreement and any required transfer instrument are executed before personal data reaches the vendor. Sending data to an uncontracted processor is the violation itself, and an agreement signed afterward does not reach back over what already went.

**Legal hold check before any deletion executes.** Every deletion, whether it comes from an erasure request or from a retention schedule, passes a hold check first. Deletion is irreversible and destroying data under hold converts a routine retention task into a spoliation problem that no privacy argument repairs.

**The breach sequence, which runs from awareness rather than from certainty:**

1. Record the awareness timestamp. Every clock in this domain runs from when the organization knew, not from when it finished analyzing.
2. Determine whether the incident is a personal data breach at all.
3. Assess the risk to the individuals, stated as harms to them rather than as impact to the organization.
4. Determine notifiability per regime, each with its own threshold and its own deadline.
5. Notify the authority within the deadline, filing in phases where facts are still incomplete rather than filing late.
6. Notify affected individuals where the risk to them is high, in plain language with the steps they can take.
7. Enter it in the breach register whether or not it was notifiable.

The order is mandated because a late notification is a separate violation from the breach itself, and because step 5 does not wait for steps 2 through 4 to reach certainty. A processor's notification to its controller runs on its own clock, in parallel, from the same awareness timestamp.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with collection dates, its labeled assumptions, its coverage statement, and any clock it started or inherited. Section headings with the contents deferred mean the stage did not run. Later stages trust the packet rather than re-reading the systems, so an optimistic completion marker propagates into a lawfulness position and from there into a notice, a filing, or a response to an individual.

## Parallel surface

Independent items fan out and are parallel-safe: processing activities, systems in a data inventory, trackers, notices and their surfaces, vendors and their agreements, transfers, retention schedule rows, design reviews, assessments, and open rights requests. Within a single rights request, the per-system searches are independent of each other and fan out too.

Aggregation is a single pass after the fan-out returns. Deduplicating one data element that appears in eleven systems, computing RoPA or assessment coverage across the estate, assembling the consolidated data map, ranking one remediation queue against capacity, counting affected individuals across systems in a breach, resolving a notifiability determination that spans regimes with different thresholds, computing a program metric over a population, and assembling the response package or the regulator filing are each statements about the whole set and cannot be produced in parallel from parts.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what the organization or the affected individuals are exposed to if the workflow continues anyway>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact fact, or both readings where sources disagree>
Sources attempted: <what was queried and what it returned>
Regulatory clock: <any statutory or contractual deadline still running, with its start event, start date, and due date; none, where none applies>
Required approval or access: <named approver role and authority level, or the connector and scope needed>
Proceeding meanwhile: <reversible work that does not depend on the blocked fact>
Preserved packet: <full privacy_packet>
Resume prompt: <prompt that restarts the workflow once the fact or approval arrives>
```

A halt never pauses a deadline. Where a clock is running, the halt says so on its own line, states the due date, and names who has to be told now rather than when the blocking fact arrives.

A halt justified by uncertainty rather than consequence is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the activity, request, or transfer it affects.

## Stage contracts

`references/stage-contracts.md` gives each desk its required inputs, the outputs it owns, its handoff target, and the hard halt specific to that stage.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
