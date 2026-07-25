# Procurement and Vendor Management Suite Workflow Contract

This file defines how Procurement Vendor Management Command Desk skills run as one continuous sourcing and vendor lifecycle rather than as a set of disconnected questions about suppliers. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is the commitment: what the company has agreed to buy, from whom, on what terms, carrying what risk, for how long, and whether anyone can still change it. The packet therefore carries the evidence behind every supplier claim alongside the claim itself, and it carries the dates that govern whether a decision is still open.

Two properties of procurement data drive most of what follows. Nearly every fact in this domain is about an organization the company does not control, so it cannot be checked from internal memory the way a headcount number or a deploy date can; the distance between what a supplier asserts and what a document establishes is the entire discipline, and a reviewer looking at a filled-in field has no way to tell which one produced it. Procurement is also bounded by windows that close on specific dates. The same conversation costs a different amount depending on the day it happens, leverage is at its maximum before an award is communicated and at its minimum after a renewal notice window lapses, and several of those transitions are irreversible by any mechanism the company controls.

## Continuity rule

A desk that has the requisition, the bid set, the executed agreement, or the spend data to run the next stage runs it. A run that ends at "procurement should benchmark this before renewal" or "consider consolidating these overlapping tools" is a routing note, not procurement work; it returns the problem to the person who asked what to buy, what it should cost, or whether the company can safely use this vendor. Complete the current stage, update `procurement_packet`, and continue until the requested outcome exists or a hard halt applies.

Three things are never continued through: a statement that reaches a supplier, an act that binds the company, and an act that gives a vendor access to systems or data. Everything else continues, with the assumption labeled inline against the supplier, contract, requirement, or spend line it affects.

## Action boundary

This suite prepares intake assessments, category plans, requirement sets and statements of work, sourcing documents, evaluation models and scorecards, diligence packages, risk tiering determinations, negotiation plans and should-cost models, contract requests and approval routing packets, onboarding and provisioning checklists, performance scorecards, renewal calendars, spend analyses, consolidation cases, and exit plans.

It does not issue a sourcing document to the market, communicate an award, a rejection, a price, or any commitment to a supplier, sign or countersign an agreement, issue or amend a purchase order, create a vendor in the vendor master or change its bank details, grant a vendor access to systems or data, waive or accept a security, privacy, or compliance requirement, serve notice of termination or non-renewal, or release a final payment. For each of those acts the desk prepares the exact document, states the amount and the term at stake, names the authority the policy requires, names what breaks if it is wrong, and stops at the gate.

The asymmetry to hold onto: a wrong internal analysis costs a meeting, a wrong statement to a supplier cannot be retracted because the supplier has already repriced against it, and a wrong signature is a term the company owns until a date somebody else set. Internal preparation is reversible and runs freely. Anything that crosses the boundary to the supplier, the vendor master, the signature block, or a production system is somebody's decision to make, and the person who signs is the person who authorizes.

Two acts sit outside the boundary in every mode regardless of who asks. Adding or changing vendor bank details is the single highest-value fraud target in the function and is verified out of band by a named human against a channel the requester did not supply. Granting a vendor access to systems or data before the review that governs that access has closed converts a reviewable decision into an incident nobody chose.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a risk tier for a proposed tool, an evaluation scorecard for a bid set, a should-cost model, a renewal recommendation for one contract, a security review status summary, a spend analysis for one category, or an exit plan.
- `workflow_run`: the default for anything phrased as a purchase, a sourcing exercise, an RFP, a renewal, a vendor review, a consolidation push, a cost reduction target, or a termination. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `procurement_packet` or halt-resume prompt. Re-read the executed agreement and re-pull the spend and contract records rather than trusting carried values whenever an amendment has been signed, an order form has been added, a renewal has processed, an attestation period has ended, an insurance certificate has expired, a screening result has aged, or the supplier has been acquired. A carried diligence result silently inherits a supplier that no longer exists in the form it was assessed in, and an acquisition is announced to customers rather than to procurement.
- `halt`: a hard class applies. Return the halt format below with the packet intact and the reversible preparation already done.
- `diagnostic`: the contract repository, the ERP or accounts payable ledger, the intake system, the vendor master, the screening service, or the supplier's evidence portal cannot be reached. Report what was reachable, what was not, and precisely which determinations, comparisons, dates, and risk conclusions each gap makes unavailable. Do not reconstruct a contract term from a repository summary field or a renewal date from a calendar entry.

## Request types

Every request carries a type, because the type sets the evidence bar, the stages that run, and the approval surface: `new_purchase`, `renewal`, `sourcing_event`, `sole_source_request`, `vendor_evaluation`, `risk_tiering`, `security_privacy_review`, `integrity_screening`, `negotiation`, `contract_request`, `onboarding`, `performance_review`, `sla_dispute`, `escalation`, `spend_analysis`, `consolidation`, `savings_target`, `policy_question`, `emergency_purchase`, `offboarding`, `audit_request`, `unknown`.

Two attributes travel with the type and change the evidence bar more than the type does.

**Commitment class** records what the work is about to commit and how reversible that is: `evaluation_only` where nothing has left the building, `internal_recommendation` where a decision is being shaped but no supplier knows, `supplier_communication` where a statement reaches the counterparty, `binding_commitment` where a signature or a purchase order exists, and `production_dependency` where the supplier is already in the path of something the company cannot stop. The class matters more than the amount, and the transition practitioners consistently underestimate is the third one. Telling a supplier they have won, or that budget exists, or that the deadline is immovable, is an act with a price attached, and it is performed by sponsors who believe they are being courteous. Every concession available before that sentence remains available only until it is said.

**Leverage window** records where the request sits against the clock: `pre_award`, `post_award_pre_signature`, `in_term`, `renewal_window_open`, `renewal_window_closed`, `auto_renewed`, `in_termination_notice`, `post_termination`. This is the procurement equivalent of a period status and it is at least as load bearing. The identical ask produces a different answer in each state, several of the transitions happen without anyone performing them, and two of them cannot be undone at any price: a notice window that closed and a term that auto-renewed. A request that arrives without its window identified is usually assumed to be `in_term` and is frequently `renewal_window_closed`, which is the difference between a negotiation and an invoice.

## The procurement packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `unverified`, `vendor_claimed`, `not_assessed`, `no_comparable_found`, and `date_not_established` are legitimate values; an invented supplier name, price, discount, benchmark, contract date, notice window, certification, insurance limit, screening result, approver, or savings figure is not.

```yaml
procurement_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  request_type: "new_purchase | renewal | sourcing_event | sole_source_request | vendor_evaluation | risk_tiering | security_privacy_review | integrity_screening | negotiation | contract_request | onboarding | performance_review | sla_dispute | escalation | spend_analysis | consolidation | savings_target | policy_question | emergency_purchase | offboarding | audit_request | unknown"
  commitment_class: "evaluation_only | internal_recommendation | supplier_communication | binding_commitment | production_dependency"
  leverage_window: "pre_award | post_award_pre_signature | in_term | renewal_window_open | renewal_window_closed | auto_renewed | in_termination_notice | post_termination"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  engagement:
    need: "the business outcome the purchase is supposed to produce, in the requester's terms"
    requester: "who raised it"
    business_sponsor: "the person who wants the outcome and will defend the spend"
    budget_owner: "who owns the budget line it consumes, where that is a different person"
    category_owner: "the procurement owner for this category, or unknown"
    technical_owner: "who will operate or integrate it"
    legal_owner: "who owns the contract review"
    security_reviewer: "named reviewer or unassigned"
    privacy_reviewer: "named reviewer or unassigned"
    approver: "the authority the policy requires for this amount and this risk tier"
    deadline: "date a source states, or unknown"
    deadline_basis: "what makes the date real, for example a contract expiry, a notice window, a regulatory date, a project dependency, a budget period boundary; a launch someone hopes for is not a basis"

  policy:
    policy_ref: "the procurement policy in force"
    competitive_thresholds: []      # amount bands and the sourcing method each requires
    sole_source_rules: "the conditions under which a direct award is permitted and who approves it"
    buying_channels: []             # catalog, purchase order, corporate card, existing agreement, and what belongs in each
    authority_matrix_ref: "the delegation of authority that sets signature and approval levels"
    required_terms: []              # positions the policy mandates in any agreement, for example data protection, audit rights, insurance minimums
    exceptions: []                  # exceptions granted, with who authorized each and its expiry

  demand:
    intake_id: "the request record"
    category: "node in the spend taxonomy"
    description: "what is being bought, stated as capability rather than as a product name where the requirement is genuine"
    business_case: "the outcome, its value, and how anyone would know it landed"
    users_affected: "population and which teams"
    existing_coverage: "whether a current agreement already covers this, with the contract reference"
    duplicate_candidates: []        # tools or suppliers already in place that overlap
    build_buy_position: "whether building, extending an existing agreement, or buying was assessed, and on what basis"
    urgency: "figure or date"
    urgency_basis: "what creates it; a project start someone chose is not the same as a contract that expires"
    estimated_value: "annual and total contract value, with which one the estimate is"

  risk_tier:
    tier: "the program's tier value, for example critical, high, moderate, low"
    tier_basis: "the criteria that produced it, not the reviewer's impression"
    data_classification: "the classification of data the supplier will process"
    data_types: []                  # personal data, special category data, payment data, health data, credentials, source code, customer content
    data_volume_and_population: "scale and whose data it is, including whether it is customer data the company holds on trust"
    criticality: "what stops working, for whom, and how fast, if this supplier stops"
    integration_depth: "network access, identity federation, production data access, subprocessor position, code execution"
    regulatory_scope: []            # regimes the engagement pulls in
    fourth_party_exposure: "the supplier's own critical dependencies where they are known"
    diligence_requirements: []      # what the tier obliges, each with the lead time it actually takes
    reassessment_trigger: "what would change the tier, for example a scope expansion, an acquisition, or a new data type"

  requirements:
    business_requirements: []       # each marked mandatory or desirable, each with how a bid will be judged against it
    technical_requirements: []
    integration_requirements: []
    service_levels_required: []     # availability, response, resolution, each with the measurement method and the remedy
    security_requirements: []
    privacy_requirements: []
    accessibility_requirements: "the conformance level required and the evidence that will demonstrate it"
    support_model_required: "hours, channels, escalation, named contacts"
    exit_requirements: "data return format, retrieval window, and deletion obligation, specified now rather than negotiated during a termination"
    acceptance_criteria: "what the supplier has to demonstrate before the company accepts delivery"
    assumptions_given_to_bidders: "the volumes, term, and scope every bidder priced against, since a bid comparison is only valid across a common basis"

  sourcing_event:
    event_type: "rfi | rfp | rfq | reverse_auction | direct_award | renewal_negotiation | catalog_buy"
    competitive_basis: "the policy provision that decided whether competition was required"
    sole_source_justification: "the condition relied on and who approved it, where the award is direct"
    fairness_regime: "whether public, regulated, or private procurement rules apply, because they change what may be said to whom and when"
    bidders: []                     # supplier, invited, declined with reason, submitted, incumbent flag
    evaluation_criteria: []         # criterion, weight, scoring scale, and the date it was fixed and communicated
    timeline: []                    # issue, question deadline, submission deadline, evaluation, award, each with its date
    questions_and_addenda: []       # every question and the answer as it was distributed to all bidders
    communication_log: []           # who spoke to which supplier, when, and about what
    confidentiality_controls: "how bid contents are kept from other bidders and from the incumbent"

  bids:
    - supplier: "legal entity as it will appear on the agreement, not the brand"
      submitted: "true | false, with what arrived"
      commercial_summary: "price structure, term, ramp, and what is excluded"
      normalized_tco: "figure over the common term and scope, with every normalization stated"
      scores: []                    # criterion, score, and the evidence in the response that produced it
      unanswered_criteria: []       # criteria the response did not address, left unscored rather than estimated
      exceptions_taken: []          # to the statement of work, the terms, the service levels
      references_checked: []        # who was spoken to, at which organization, and what was asked
      demonstration_findings: "what the evaluation actually observed rather than what was demonstrated in slides"
      risk_flags: []
  evaluation:
    independent_scoring_complete: "true | false"
    consensus_record: "where evaluators diverged, the reasoning that resolved it, and who was in the room"
    normalization_basis: "term, volume, scope, and assumptions every bid was restated onto"
    shortlist: []
    award_recommendation: "supplier and the criteria that decided it"
    award_basis: "the scoring outcome and the commercial position together, stated separately"
    unsuccessful_bidder_position: "what each unsuccessful bidder is to be told, prepared but not sent"
    criteria_change_log: []         # any change to criteria or weights, its date, and whether bids were visible at the time

  diligence:
    security:
      questionnaire_state: "not_sent | sent | returned | reviewed"
      attestations: []              # report type and edition, scope and the services actually covered, period, auditor, exceptions and qualifications, expiry
      penetration_test: "date, scope, tester, and whether findings were provided or only a summary letter"
      certifications_claimed_without_evidence: []   # what the supplier asserts and no document supports
      findings: []                  # finding, severity, supplier response, compensating control, owner, due date
      review_state: "not_started | in_progress | approved | approved_with_conditions | rejected"
      conditions: []                # each with a named owner and a date, because a condition nobody owns is an approval
      reviewing_function: "who performed the review, since this suite coordinates it and does not perform it"
    privacy:
      personal_data_processed: "true | false, with the categories"
      processing_role: "controller | processor | joint_controller | independent_controller"
      dpa_state: "not_required | requested | under_review | executed"
      subprocessors: []             # named subprocessors, their locations, and the notification and objection terms
      transfer_mechanism: "the mechanism relied on for any cross-border transfer"
      assessment_required: "whether an impact assessment is triggered, and by which criterion"
      retention_and_deletion_terms: "what the agreement obliges at termination"
    integrity:
      legal_entity: "registered name, jurisdiction, and registration number as filed"
      ownership: "parent, ultimate beneficial ownership where required, and any recent change of control"
      screening: []                 # list checked, provider, date, and result, since a screening result is a point in time
      debarment_or_exclusion: "result and source"
      conflict_of_interest: "declared relationships between the supplier and anyone in the decision"
      anti_bribery: "the position and the evidence, particularly where intermediaries or public officials are involved"
      financial_viability: "source, assessment, and what it means for a multi-year commitment"
      insurance: []                 # coverage type, limit, carrier, expiry, and whether the certificate names the company
      labor_and_sustainability: "obligations the company carries into its own reporting"
    accessibility_conformance: "the evidence provided, its date, and the product version it covers"
    continuity: "the supplier's recovery commitments, their dependencies, and whether the contract makes any of it enforceable"
    diligence_gate_state: "open | closed_approved | closed_with_conditions | blocked"

  commercial:
    price_structure: "per seat, per unit, tiered, consumption, platform fee, minimum commitment, or the combination in use"
    quoted_price: "figure with its term and what it includes"
    list_price: "figure, where the supplier publishes one"
    discount_claimed: "the discount and what it is a discount from, since a discount off an unpublished list price is a number the supplier chose"
    benchmark: []                   # comparable, its source, its date, its scope, and why it is comparable
    should_cost: "the model, its inputs, and its method"
    tco_model: "horizon and every component: license, implementation, integration, migration, training, support, internal effort, and exit"
    term_structure: "initial term, renewal term, ramp, uplift cap, price protection, and price holds with their expiry"
    payment_terms: "terms, timing, and any prepayment"
    commitment_mechanics: "minimum commitment, true-up and true-down rights, overage rate, and what happens to unused entitlement"
    negotiation_plan: "targets ranked, tradeables, the walk-away position, the alternative if this supplier is declined, and the concession sequence"
    concessions: []                 # what was given, what was received for it, and when
    savings: "the figure, whether it is realized saving against a prior paid price or avoided cost against a proposal, the baseline behind it, and whether finance has agreed to recognize it"

  contract:
    paper: "whose template the agreement sits on"
    documents: []                   # master agreement, order form, statement of work, data protection addendum, service level exhibit, security exhibit, each with its version
    order_of_precedence: "what the documents say governs when they conflict, or noted as absent"
    legal_review_state: "not_started | in_review | redlines_open | agreed | executed"
    open_positions: []              # unresolved terms, the company position, the supplier position, and the risk owner for each
    approval_chain: []              # role, the authority basis, and state
    signature_authority: "who may sign at this value, per the authority matrix"
    execution_state: "not_started | out_for_signature | executed"
    executed_document_location: "where the signed original lives"
    effective_date: "date from the executed document"
    initial_term_end: "date from the executed document"
    renewal_type: "none | optional | automatic, from the executed document"
    notice_window: "the period the agreement requires, quoted from the clause"
    notice_deadline: "the computed date, with the clause and the date basis it was computed from"
    notice_owner: "the named person who has to act before it"
    key_obligations: []             # what each party owes, with an owner and a date on the company's side
    purchase_order_reference: "the PO, where the buying channel requires one"

  onboarding:
    vendor_master_state: "not_created | requested | created"
    bank_detail_verification: "the method, the channel used, and the named person who performed it, verified independently of the request"
    tax_and_compliance_forms: "what was required and what was received"
    access_provisioning: []         # system, access level, requester, approver, and the review that authorized it
    security_configuration: "identity federation, provisioning, logging, retention, administrative roles, and network restrictions as actually configured"
    invoicing_setup: "billing contact, invoice format, purchase order requirement, and coding"
    internal_owner: "the named person who owns this supplier relationship, since an unowned supplier is the one nobody renegotiates"
    adoption_plan: "rollout, training, and the usage the business case assumed"
    kickoff_state: "scheduled | held | not_held"

  performance:
    scorecard: []                   # dimension, measure, where the measurement comes from, period, and result
    sla_results: []                 # commitment, measured result, breach, credit earned, credit claimed, credit received
    measurement_source: "whose telemetry decides, since a supplier reporting on its own availability is a self-assessment"
    incidents: []                   # date, impact, root cause given, and whether the commitment covered it
    escalations: []
    governance_meetings: []         # date, attendees, decisions, and actions with owners
    improvement_plan: "the plan, its milestones, and the consequence attached to missing them"
    consumption_versus_entitlement: "what was bought against what is used, and the true-up or reduction it implies"
    business_case_realization: "whether the outcome in the business case actually arrived"

  relationship:
    segmentation: "the supplier's classification in the portfolio and the basis for it"
    concentration: "the share of this category, this function, or this spend the supplier carries"
    dependency: "what the company cannot do without them"
    substitutability: "the realistic alternatives"
    switching_cost: "figure and effort"
    switching_lead_time: "how long a move actually takes, including data migration and re-integration"
    supply_position: "single_source where one supplier is used and others exist, or sole_source where no alternative exists, which are different problems with different fixes"
    exit_readiness: "whether an exit could be executed today, and what is missing"
    governance_cadence: "the review rhythm the tier and the value justify"

  spend:
    period: "the window analyzed and the ledger it came from"
    by_supplier: []                 # supplier, spend, and the legal entity it consolidates under, since brands and entities differ
    by_category: []
    by_cost_center: []
    contract_coverage: "spend under an agreement against spend with no agreement behind it"
    tail_spend: "the long tail, its supplier count, and its aggregate value"
    off_contract_spend: []          # spend that bypassed the required channel, with the buyer and the channel where identifiable
    fragmentation: []               # multiple suppliers delivering the same capability, with what each costs
    price_variance: "the same item or service bought at different prices across the company"
    savings_realization: "negotiated savings against what the ledger shows, with the budget line where finance recognized it"

  renewals:
    contracts:
      - contract_ref: "the agreement"
        supplier: "legal entity"
        annual_value: "figure"
        end_date: "date from the executed document"
        renewal_type: "from the executed document"
        notice_window: "quoted from the clause"
        notice_deadline: "computed date"
        date_source: "the executed document, or the repository field where the document was not available, stated as such"
        uplift_exposure: "what renewal costs if nothing is done"
        decision_owner: "named"
        decision: "renew | renegotiate | consolidate | replace | terminate | undecided"
        decision_date: "when it has to be made to stay inside the window"
    consolidation_candidates: []    # overlapping agreements, the combined value, and the term alignment that makes or blocks a consolidation
    portfolio_view: "renewals clustered by supplier and by quarter, because a supplier with three renewals is one negotiation"

  offboarding:
    termination_basis: "for cause, for convenience, non-renewal, or expiry, with the clause relied on"
    notice_state: "not_given | prepared | given, with the date and the method the clause requires"
    transition_plan: "the replacement, the sequence, and the period both suppliers overlap"
    data_return: "scope, format, retrieval window, and state"
    data_deletion: "scope, the certification the agreement requires, and whether it was received"
    access_deprovisioning: []       # system, access removed, date, and who confirmed it
    final_settlement: "final invoices, credits owed, unused prepayment, and disputed amounts"
    record_retention: "what the company keeps, where, and for how long after the relationship ends"
    knowledge_transfer: "what only the supplier knows and how it comes back"
    residual_dependency: "anything still running on the supplier after the stated exit date"

  approvals:
    - item: "the commitment, communication, signature, provisioning, waiver, notice, or payment requiring authorization"
      amount_at_stake: "annual and total contract value"
      required_approver: "the role the authority matrix or policy names"
      authority_basis: "the policy provision that sets the level"
      state: "not_required | pending | granted | denied"
      granted_by: "named human"
      granted_on: "date"

  source_facts:
    - fact: "source-backed fact"
      source: "executed_contract | order_form | statement_of_work | amendment | supplier_quote | rfp_response | intake_record | erp_spend_data | ap_invoice | purchase_order | contract_repository | third_party_attestation | audit_report | insurance_certificate | screening_service | reference_call | supplier_questionnaire | supplier_marketing_claim | internal_owner | user | unknown"
      locator: "the document, clause, report, record, or field it came from"
      as_of: "the date the fact was established, because attestations expire, screenings age, and prices are quoted with a validity period"
  assumptions:
    - assumption: "what was assumed"
      affects: "the supplier, contract, requirement, price, or conclusion it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. The executed agreement governs what was actually agreed, in the form the parties signed, including the order form, every amendment, every exhibit, and any side letter. A proposal, a quote, a slide, and a sales email describe what was offered. The gap between the offer and the executed document is where most surprises in this domain are found, and it is found after signature.
2. Where documents inside one agreement conflict, the order of precedence clause decides. Where the agreement has no such clause, that is a recorded conflict rather than a judgment call, because the order form and the master agreement routinely disagree about term, liability, and data handling, and each party reads the one that favors it.
3. The accounts payable ledger is authoritative for what was actually paid. Contract value is a commitment, a purchase order is an intention, a supplier's account statement is their record, and only the ledger says what left the company. Spend analysis built on any of the other three describes something other than spend.
4. Third-party attestation reports, audit reports, and test results are evidence, and they are evidence only for their stated scope, period, and subject. The service actually being purchased is frequently not the service in the report, the period frequently ended long before the question was asked, and the exceptions section is the part that carries the information. A supplier questionnaire is a self-assessment, useful for structuring the conversation and not a substitute for the report.
5. A supplier's marketing claim about its own certification, uptime, customer count, or security posture is a sales fact. It is recorded as `vendor_claimed` and never promoted to established by repetition, by confidence, or by the fact that a well-known company appears on their logo wall.
6. Screening, registry, and financial data carry their provider and their date. A sanctions or debarment result is true as of the moment it was run, and the entity screened has to be the entity signing rather than the brand on the website.
7. Procurement policy and the delegation of authority govern who may commit the company and by what method. A practice that is customary in a business unit and contradicts the policy is a recorded exception rather than an accepted route.
8. The contract repository is authoritative for locating documents and is a transcription for everything else. A renewal date, a notice window, or a value read from a repository field was typed there by a person reading a clause, and notice windows are the field that gets transcribed wrong, because the clause counts from a date that the field does not record. Any date that will drive an irreversible decision is computed from the executed document.
9. Business sponsor and stakeholder statements are requirements, preferences, urgency, and history. They are the fastest route to understanding what the company needs and they are not evidence about the supplier.

Where a lower layer contradicts a higher one on a load-bearing fact, record both readings with their locators and dates. Do not resolve toward whichever reading lets the purchase proceed on schedule.

## Procurement discipline

- Every supplier fact carries its source and its date. An attestation from a period that ended fourteen months ago, an insurance certificate that expired in March, and a screening result from before an acquisition are all stale in a way that no amount of formatting reveals.
- A claim and an evidenced fact are recorded differently, always. The supplier said it, the questionnaire asserted it, the report established it for this scope and this period, and the contract obliges it are four different states, and only the last one is enforceable.
- Certification language is stated precisely because the imprecise version is a different claim. A report covers a defined scope for a defined period and carries its exceptions; a certificate has a scope statement and an expiry. Repeating a supplier's shorthand for either one imports a claim the document does not make.
- The entity matters. The company contracts with a legal entity, screens a legal entity, and sues a legal entity. A brand, a product name, a reseller, and a local subsidiary are not interchangeable, and the entity on the signature block is the one whose financial position, insurance, and obligations are actually engaged.
- A benchmark is a comparable with a source, a date, and a scope. "Market rate is around this" is not a benchmark, it is an impression, and it is the number that ends up in the negotiation target and then in the savings figure.
- A discount is stated against what it discounts. A discount off a list price the supplier sets and never charges is a description of the supplier's pricing practice rather than a measure of value obtained.
- Total cost of ownership is compared over a common term, a common scope, and common volume assumptions, and every normalization is stated. Two bids are only comparable after they have been restated onto the same basis, and the restatement is where the actual analysis lives.
- Realized saving and avoided cost are different things and finance recognizes only one of them. A reduction against a price the company was actually paying reaches a budget line. A reduction against a proposal reaches a slide.
- Service credits are a remedy, not an outcome. A supplier that misses availability every month and pays the credit every month is meeting the contract and failing the business, and the credit is usually capped at a fraction of a monthly fee.
- Availability reported by the supplier is a self-measurement. Where the commitment matters, the measurement source is named and the exclusions in the definition are read, since scheduled maintenance, degraded performance, and regional outages are frequently outside the calculation.
- Entitlement and consumption drift apart in both directions, and only one direction generates an invoice. The count of licenses bought against the count actually in use is the fastest available cost reduction and the most common source of an unplanned true-up.
- Single source and sole source are different conditions. Single source means the company chose one supplier where alternatives exist, and it is a decision that can be revisited. Sole source means no alternative exists, and it is an exposure that has to be managed rather than corrected.
- Concentration is invisible one supplier at a time. Six reasonable tools bought by six reasonable teams is the normal way a category fragments, and no individual purchase in that sequence looks wrong.
- Urgency is examined rather than accepted. An expiring contract creates a real deadline; a launch date somebody chose creates a preference; and an urgent purchase that skips competition and diligence costs more and carries risk that outlives the urgency by several years.
- The date on which leverage is lost is a fact in the packet, not a diary entry. Renewal notice windows, price-hold expiry, and quote validity periods all close without anyone acting, and the day after each one closes the available outcomes are strictly worse.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with locators and dates, its labeled assumptions, and the determinations the evidence could not support. Section headings with the supplier evidence deferred mean the stage did not run. Later stages consume the packet rather than re-reading every contract and re-pulling every attestation, so a risk tier assigned once travels into the diligence scope, then the contract terms, then the access granted, then the ongoing monitoring cadence, and by the time anyone re-derives it the tier has four downstream users who believe it was assessed against criteria rather than assigned by impression.

## Parallel surface

Independent items fan out and are parallel-safe: suppliers under discovery, bids under independent scoring, the diligence workstreams for security, privacy, integrity screening, insurance, and financial viability, since each runs against different evidence and different reviewers, categories under spend analysis, contracts in a renewal portfolio, requirement items under specification, cost centers, access reviews during onboarding, and suppliers under offboarding. Connector preflight across the contract repository, the accounts payable ledger, the intake system, the vendor master, and the screening service is parallel too.

Aggregation is a single pass after the fan-out returns, and several aggregates here carry information no per-item view can reproduce. Bid comparison is one pass over the whole set, because normalization is meaningful only relative to the other bids and a bid assessed alone is a review rather than a comparison. Consensus scoring is one pass after independent scoring, and it must not be interleaved: the value of independent scores is that each evaluator formed one before hearing the others, and a consensus reached by scoring together is one confident evaluator's opinion recorded in five columns. Category fragmentation, price variance for the same item across business units, and supplier concentration are all single passes over the whole population, because each individual purchase in a fragmented category was defensible on its own terms. The renewal calendar is built once across the portfolio, since renewals cluster and three agreements with one supplier are one negotiation with three deadlines. Aggregate exposure to a supplier is computed across entities and business units, which is exactly where a supplier that looks small in each unit turns out to be critical to the company.

The diligence gate is the one thing that must never be split. A supplier is approved for a use case or it is not, and an approval assembled from a closed security review, an open privacy review, and an unexamined screening is not a partial approval; it is an unapproved supplier with three documents in front of it.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what is committed, communicated, signed, provisioned, auto-renewed, or exposed if the workflow continues anyway, with the amount, the term, and the supplier where they exist>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact document, clause, attestation, date, or record, or both readings when sources disagree, with locators and as-of dates>
Sources attempted: <what was queried, requested, or opened and what it returned>
Required approval or access: <named approver role and the policy provision that sets the authority, or the document, system, or supplier response needed>
Time cost of the halt: <what closes while this waits: days remaining in a notice window, a quote validity period, a price hold, or an expiring attestation, and what the outcome becomes once it closes>
Proceeding meanwhile: <reversible preparation that does not depend on the blocked fact>
Preserved packet: <full procurement_packet>
Resume prompt: <prompt that restarts the workflow once the document, access, or approval arrives>
```

The time cost field exists because halting is not free in this domain. Every other kind of work can wait a day at no cost; a procurement halt inside an open notice window spends leverage while it waits, and a halt that runs past the window has made the decision it was raised to protect.

A halt justified by not knowing rather than by consequence is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the supplier, contract, or requirement it affects.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
