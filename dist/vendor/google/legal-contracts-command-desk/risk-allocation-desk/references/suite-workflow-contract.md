# Legal Contracts Suite Workflow Contract

This file defines how Legal Contracts Command Desk skills run as one continuous program of work instead of behaving as isolated one-off prompts. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is enforceable text: what the organization has actually agreed to, on whose paper, under whose authority, against which legal entity, and what falls out of that agreement for the years it stays in force. The packet therefore carries clause-level state, position and deviation state, and approval state alongside the commercial summary, because the distinguishing failure of this domain is a clean summary that no longer matches the words that govern.

## Continuity rule

A desk that has the document and the playbook to run the next stage runs it. A run that ends at "legal should now review the indemnity" or "consider extracting the obligations" is a routing note, not contract work; it hands the sequencing problem back to the business owner who asked for a reviewed agreement. Complete the current stage, update `legal_packet`, and continue until the requested outcome exists or a hard halt applies.

Three things are never continued through: an act that binds the organization or leaves the building, a position that departs from the playbook without the approver the delegation of authority names, and a statement about what a document says that the document text does not carry. Everything else continues, with the assumption labeled inline against the clause, issue, or obligation it affects.

## Action boundary

This suite produces reviews, issues lists, redlines, position papers, clause comparisons, obligation registers, approval packages, execution packages, repository records, and reporting. It does not sign an agreement, send a redline or a counteroffer to a counterparty, serve or respond to a notice, accept a term, waive or release a right, grant an exception, execute a termination, settle a claim, release a legal hold, publish a template change, or file anything with a court or a registry. For those acts the desk prepares the exact item, names the authority level it requires under the delegation of authority, states what it commits the organization to and for how long, and stops at the gate. The person with the authority to bind the organization is the one who binds it.

This suite also does not issue legal advice of record. It prepares work product for a lawyer and for the business owner who carries the commercial decision. Where a question turns on how a court or a regulator would read a clause, that reading is counsel's to give, and it enters the packet as a source fact with the named lawyer attached rather than as an inference the desk drew.

Editing an executed document, overwriting a version of record, backdating an effective date, altering an executed signature page, or deleting a repository record is outside the boundary in every mode. An executed instrument is the evidence of what was agreed, and a corrected copy that nobody countersigned is worth less than an acknowledged error.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example an NDA turn, a liability position, a subprocessor comparison, an open source disposition, or an obligation extraction from a signed agreement.
- `workflow_run`: the default for anything phrased as a review, a negotiation, a deal, a renewal, an onboarding, a remediation, or a portfolio pass. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `legal_packet`, a halt-resume prompt, or an earlier review memo. Re-read the document rather than the summary whenever the turn number has moved, the counterparty has returned paper, an amendment has been signed since, or terms incorporated by reference could have been republished. A carried clause summary silently inherits a version it no longer describes.
- `halt`: a hard halt class applies. Return the halt format below with the packet intact and the reversible work already done.
- `diagnostic`: required documents or systems cannot be reached. Report what was reachable, what was not, and precisely which clause conclusions, obligation rows, or precedence determinations each gap makes unavailable. Do not reconstruct an unreachable exhibit from what the template usually says.

## Matter types

Every request carries exactly one matter type, because the type sets the playbook, the review depth, the approval surface, and the turnaround the business is entitled to expect: `nda`, `msa`, `saas_subscription`, `order_form`, `sow`, `dpa`, `security_exhibit`, `reseller_or_channel`, `partnership`, `inbound_procurement`, `software_license`, `open_source_review`, `amendment`, `renewal`, `termination`, `dispute`, `repository_remediation`, `unknown`.

Two attributes travel with the type and change the answer more than the type does. **Posture** records whether the organization is the customer, the supplier, or a genuine mutual party, because the same clause is a protection in one posture and an exposure in the other. **Paper** records whether the draft started from an approved template or arrived from the counterparty, because review on counterparty paper is a search for what is missing as much as for what is objectionable, and the absent clause is the one nobody flags.

## The legal packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `unstated`, and `not_yet_executed` are legitimate values; an invented section number, cap figure, entity name, or approver is not.

```yaml
legal_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  matter_type: "nda | msa | saas_subscription | order_form | sow | dpa | security_exhibit | reseller_or_channel | partnership | inbound_procurement | software_license | open_source_review | amendment | renewal | termination | dispute | repository_remediation | unknown"
  posture: "we_are_customer | we_are_supplier | mutual | unknown"
  paper: "our_paper | counterparty_paper | negotiated_hybrid | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  matter:
    request_id: "intake reference"
    requester: "who asked"
    business_owner: "the person who owns the commercial outcome, or unknown"
    legal_owner: "reviewing lawyer or legal ops owner, or unknown"
    needed_by: "date a source states, or unknown"
    urgency_basis: "what makes the date real, for example quarter end, an expiring NDA, a go-live"
    deal_value:
      amount: "figure from a source"
      currency: "currency"
      term_length: "as written"
      basis: "the order form, quote, or budget line it came from"
    risk_tier: "tier value plus the triage rubric it came from"
    privileged: "true | false | undetermined"

  parties:
    our_entity:
      legal_name: "the exact registered name, never the brand"
      jurisdiction: "state or country of formation"
      entity_type: "as registered"
      notice_address: "the address the notice clause requires, or unstated"
    counterparty:
      legal_name: "the exact registered name as the signature block gives it"
      jurisdiction: "state or country of formation"
      registration_number: "company or file number, or unknown"
      parent_or_affiliates: []
      notice_address: "as the notice clause requires, or unstated"
      verification_source: "registry extract, certificate, signature block, or unverified"
      screening_state: "cleared | flagged | not_screened"
    affiliate_rights: "whether affiliates may transact or receive services, and under which clause"

  instrument:
    title: "the document's own title"
    version_label: "the version and turn the file actually carries"
    parent_agreement: "the governing agreement this sits under, or none"
    family: []                      # order forms, SOWs, amendments, exhibits under the same parent
    incorporated_by_reference: []   # online terms, policies, SLA or subprocessor pages, with locator and the version retrieved
    order_of_precedence: "quoted from the clause that sets it, or unstated"
    effective_date: "as written, or unknown"
    execution_date: "when the last party signed, or not_yet_executed"
    initial_term: "as written"
    governing_law: "as written, or unstated"
    venue_and_forum: "as written, or unstated"
    dispute_mechanism: "litigation | arbitration with its rules and seat | escalation ladder | unstated"
    assignment_and_change_of_control: "as written"
    amendment_form: "what the text requires to amend it, for example a signed writing"

  positions:
    - clause_ref: "the section number as this document numbers it"
      topic: "the subject the playbook indexes"
      standard_position: "the approved position"
      fallback_ladder: []           # ordered acceptable retreats, from the playbook
      walk_away: "the position below which the playbook does not permit agreement"
      counterparty_position: "what their text does, in operative terms"
      state: "accepted | open | conceded | escalated"
      deviation: "none | within_fallback | outside_playbook"
      approver_required: "role the delegation of authority names, or none"

  issues:
    - issue_id: "I-01"
      clause_ref: "section number"
      severity: "value plus the rubric it came from"
      operative_effect: "what the text actually does, not the topic it belongs to"
      business_impact: "the consequence in commercial or operational terms"
      proposed_change: "the language change sought"
      status: "open | proposed | accepted | rejected | escalated | withdrawn"
      owner: "who carries it"
      turn_raised: "which negotiation turn it first appeared in"

  risk_terms:
    liability:
      cap: "the figure or formula quoted from the text"
      cap_basis: "what the formula multiplies, as written"
      supercaps: []                 # heightened caps and what they cover
      excluded_damage_types: []
      carve_outs: []                # what sits outside the cap entirely
      mutuality: "mutual | one_way_in_our_favor | one_way_against_us"
    indemnities:
      - trigger: "what activates it"
        indemnitor: "who owes it"
        scope: "claims covered, as written"
        defense_control: "who controls defense and settlement"
        cap_interaction: "inside the cap, outside it, or supercapped"
    warranties:
      - warranty: "what is warranted"
        duration: "as written"
        remedy: "the stated remedy"
        exclusivity: "whether it is the sole remedy"
    disclaimers: []
    insurance:
      - coverage_type: "line of coverage"
        limit: "as written"
        additional_insured: "required or not"
        certificate_state: "received | requested | not_provided"
    force_majeure: "scope and whether payment obligations are excused"

  commercial_terms:
    fees: "structure as written"
    payment_terms: "days, method, and late charges as written"
    price_escalation: "cap and mechanism, or none"
    renewal:
      type: "auto | mutual_written | none"
      notice_window: "days before expiry, as written"
      escalator: "as written, or none"
    service_levels:
      - commitment: "the metric and target as written"
        measurement: "how it is measured and by whom"
        credit: "the remedy"
        sole_remedy: "true | false"
    suspension_rights: "as written"
    termination_rights:
      - party: "who may terminate"
        ground: "for cause, convenience, or a named trigger"
        cure_period: "as written"
        notice_period: "as written"
    transition_assistance: "scope, duration, and rate, as written"

  data_protection:
    role: "controller | processor | joint_controller | independent_controllers | unknown"
    personal_data_categories: []
    data_subjects: []
    processing_purposes: []
    transfer_mechanism: "the mechanism the text names, or none"
    transfer_assessment_state: "completed | required | not_applicable | unknown"
    subprocessors:
      list_locator: "where the authorized list actually lives"
      objection_right: "as written"
      flow_down: "what the text requires of subprocessor terms"
    security_measures_ref: "the exhibit or schedule the DPA points at"
    breach_notification: "the trigger and window, quoted"
    deletion_and_return: "the obligation and its timeline, as written"
    audit_rights: "form, frequency, and cost allocation, as written"
    ai_training_use: "whether the text permits use of the data to train models, quoted"

  security_terms:
    required_attestations: []       # report or certificate the text requires, with period and refresh
    control_commitments: []
    vulnerability_remediation: []   # severity tiers and windows, as written
    penetration_testing: "obligation and evidence form"
    assessment_rights: "questionnaire, audit, or on-site, as written"
    personnel_and_access: "screening, training, and access constraints"
    resilience_commitments: "recovery objectives the text commits to"
    incident_obligations: "notification, cooperation, and cost allocation"

  ip_terms:
    background_ip: "who keeps what"
    work_product: "ownership of deliverables, as written"
    license_grants:
      - grantor: "who grants"
        scope: "permitted uses, as written"
        field_and_territory: "as written"
        exclusivity: "exclusive | non_exclusive"
        sublicensable: "true | false"
        term: "as written"
        revocability: "as written"
    feedback_clause: "what the counterparty gets in suggestions we give"
    residuals: "whether unaided memory carve-outs exist"
    publicity_and_marks: "logo, reference, and press consent"
    third_party_flow_down: "open source and third-party terms the agreement passes through"

  open_source:
    - component: "package and version"
      declared_license: "identifier as the license file states it"
      license_source: "where the license text was actually read"
      use_model: "linked | distributed | saas_only | modified"
      obligations: []               # attribution, source availability, notice, patent, copyleft reach
      compatibility_state: "compatible | conflict | undetermined"
      disposition: "approved | approved_with_conditions | blocked | undetermined"

  regulatory_terms:
    export_and_sanctions: "clauses and screening obligations"
    anti_corruption: "clauses and audit rights"
    flow_down_requirements: []      # terms a prime contract forces into subcontracts
    sector_obligations: []
    accessibility_commitments: "as written"
    ai_specific_terms: "model use, output ownership, training, and disclosure terms"

  obligations:
    - obligation_id: "OB-01"
      clause_ref: "section number"
      obligated_party: "us | counterparty | both"
      obligation: "what must be done, in operative terms"
      trigger: "the event or date that starts it"
      due_or_recurrence: "the deadline or cadence, as written"
      notice_requirement: "method, recipient, and address the clause requires, where one applies"
      owner: "named internal owner, or unknown"
      evidence_of_performance: "what would show it was done"
      state: "not_started | in_progress | met | missed | not_applicable"

  approvals:
    - item: "the deviation, position, or act requiring authorization"
      required_approver: "the role the delegation of authority names"
      authority_basis: "the policy or matrix clause that sets the level"
      state: "not_required | pending | granted | denied"
      granted_by: "named human"
      granted_on: "date"

  execution:
    signature_method: "wet ink | electronic | as the clause requires"
    signatories:
      - party: "which party"
        name: "named human"
        title: "as it will appear"
        authority_basis: "the resolution, delegation, or policy that authorizes them"
    counterparts: "permitted or not, as written"
    execution_version_ref: "the exact file that goes out for signature"
    fully_executed_copy: "locator, or not_yet_executed"
    effective_date_trigger: "what makes it effective, as written"

  repository:
    record_id: "system record"
    version_of_record: "the file the record points at"
    family_links: []
    metadata_state: "complete | partial | missing fields named"
    retention_class: "class from the retention schedule"
    access_restriction: "who may read it"
    hygiene_findings: []

  disputes:
    - matter_ref: "reference"
      claim: "what is alleged and under which clause"
      notice_direction: "sent | received"
      notice_date: "date"
      cure_period_state: "running with its end date, expired, or none"
      legal_hold_state: "issued | pending | not_required"
      external_counsel: "firm, or none"
      escalation_state: "as the escalation clause defines it"

  source_facts:
    - fact: "source-backed fact"
      source: "executed_contract | draft | counterparty_paper | template | playbook | clm_record | delegation_of_authority | counsel_note | registry | email | ticket | user | unknown"
      locator: "document, version, and the section or page it came from"
      read_on: "when the text was read"
  assumptions:
    - assumption: "what was assumed"
      affects: "the clause, issue, obligation, or position it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. The executed instrument governs: the signed agreement, its exhibits and schedules, its amendments, and any side letter, read together in the order of precedence the documents themselves set. Where the executed version and anything else disagree, the executed version wins and the disagreement is recorded rather than smoothed.
2. Terms incorporated by reference are part of the instrument and are read at the version the agreement fixes them to. Online terms, subprocessor lists, SLA pages, and acceptable use policies change under a URL that stays the same, so the retrieved copy carries the date it was retrieved and the version label it displayed.
3. The current draft with its turn number is authoritative for the negotiation state and for nothing else. A draft is what someone proposed, never what the parties agreed.
4. Approved templates, the clause playbook, and the delegation of authority matrix are authoritative for the organization's own positions and approval thresholds.
5. Counsel guidance and legal opinions are authoritative for interpretation, recorded with the named lawyer who gave them. An interpretation is a source fact with an attribution, not an inference the desk may draw on its own.
6. Repository and CLM metadata are a claim about the instrument and are outranked by the instrument itself. Renewal dates, cap figures, and party names in a CLM record are frequently wrong in exactly the way that matters.
7. Email, chat, and deal desk notes are negotiation history and evidence of intent. They also hide side letters, informal waivers, and commitments a business owner made that the master agreement never captured, so a contradiction between email and the instrument is surfaced rather than dismissed.

Where a lower layer contradicts a higher one on a load-bearing fact, record both readings against the field. Do not resolve toward whichever reading lets the deal close.

## Drafting and reading discipline

- Clause references are quoted as the document numbers them. Section numbers shift between turns when a clause is inserted or deleted, so a reference carries the version it belongs to. A pin cite into the wrong version is worse than no cite, because it looks checkable.
- Defined terms are read against the definitions section, not against ordinary usage. A capitalized term carries whatever meaning the agreement gives it, and a large share of real contract defects live in a definition rather than in the operative clause everybody argued about.
- Order of precedence is established before any clause conclusion is stated for an agreement family. An order form term, an MSA term, and an exhibit term can all address the same subject, and which one governs is decided by a precedence clause rather than by which document is longest or most recent.
- Amounts, caps, formulas, windows, cure periods, and notice periods are quoted from the text. Never restate a cap as a familiar multiple, a payment term as a familiar number of days, or a notice window as a familiar period. Familiar is exactly where this domain fabricates.
- The distinction between `shall`, `will`, `may`, `must use commercially reasonable efforts`, and `may in its sole discretion` is the substance of the obligation. Collapsing them into "the vendor agrees to" changes what the clause requires.
- Silence is a finding on counterparty paper. A missing limitation of liability, a missing termination for convenience, a missing data deletion obligation, and a missing assignment restriction are each recorded as absent, with what the absence means under the governing law where a source establishes it.
- "Market", "standard", and "customary" are claims that require a benchmark source. Without one, describe what the clause does and against which playbook position it sits.
- Dates are distinguished: effective date, execution date, commencement date, and the date a term or notice window is measured from are four different dates and are frequently four different values.
- Legal entity names come from the signature block and the registry, never from the brand, the domain, or the email footer. A parent and its subsidiary are different obligors with different balance sheets.
- Redlines carry rationale per change. A markup delivered without the reason for each edit forces the counterparty's lawyer to guess at intent, which produces a slower turn and a worse outcome.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with locators and read dates, its labeled assumptions, and the residual exposure it leaves behind. Section headings with the contents deferred mean the stage did not run. Later stages trust the packet rather than re-opening the document, so an optimistic completion marker propagates into an obligation register and from there into what the business believes it bought.

## Parallel surface

Independent items fan out and are parallel-safe: clauses within a document, agreements within a portfolio, open source components, subprocessors, obligations, repository records, counterparty entities, NDAs in an intake queue, and the separate review lanes for commercial terms, risk allocation, data protection, security, IP, open source, and regulatory flow-down each stand on their own inputs.

Aggregation is a single pass after the fan-out returns. Determining order of precedence across an agreement family, ranking one issues list by severity against the negotiating capital actually available, maintaining the concession log across turns where each turn depends on the last, rolling aggregate liability exposure across every contract with the same counterparty, building a renewal calendar across the portfolio, and assembling the approval package are each statements about the whole set. The approval package in particular cannot be split: an approver authorizing deviations one at a time never sees the combined exposure, which is how a deal accumulates a set of individually acceptable concessions that together sit outside anything the delegation of authority contemplated.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what the organization is exposed to or bound by if the workflow continues anyway>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact fact, or both readings when documents disagree, with locators>
Sources attempted: <what was opened or queried and what it returned>
Required approval or access: <named approver role and authority basis, or the document and system needed>
Proceeding meanwhile: <reversible work that does not depend on the blocked fact>
Preserved packet: <full legal_packet>
Resume prompt: <prompt that restarts the workflow once the fact, document, or approval arrives>
```

A halt justified by uncertainty rather than consequence is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the clause, issue, or obligation it affects.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
