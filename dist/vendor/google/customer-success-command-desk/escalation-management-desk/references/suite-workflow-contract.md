# Customer Success Suite Workflow Contract

This file defines how Customer Success Command Desk skills run as one continuous program of work instead of behaving as isolated one-off prompts. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is a paying relationship over time: what the customer bought, what they were told it would do for them, whether the people who signed are still there, what the product is actually being used for, what that is worth in their numbers rather than in ours, what is quietly going wrong, and whether they will pay again. The packet therefore carries contract state, telemetry state, stakeholder state, and approval state alongside the account record, because the distinguishing failure of this domain is an account that is green in every system right up to the day it gives notice.

## Continuity rule

A desk that has the facts to run the next stage runs it. A run that ends at "you should now build a success plan for this account" or "consider reviewing adoption before the renewal" is a routing note, not customer success work; it hands the sequencing problem back to the CSM who asked for the review, usually the week before the notice deadline. Complete the current stage, update `success_packet`, and continue until the requested outcome exists or a hard halt applies.

Three things are never continued through: anything that reaches the customer, anything that commits the company commercially, and any claim about usage, value, or health that the underlying systems do not support. Everything else continues, with the assumption labeled inline against the account, stakeholder, outcome, or risk it affects.

## Action boundary

This suite produces plans, analyses, scores, registers, narratives, decks, briefs, drafts, and reporting. It does not send a customer-facing email or message, present or deliver a business review, offer a discount, credit, extension, or service commitment, sign or amend a contract, publish a logo, quote, or case study, arrange a reference call, write to the CRM or the success platform, change a health score model in production, provision or deprovision entitlements, send a survey, close an escalation record of record, or change a renewal forecast category of record. For those acts the desk prepares the exact item, names the approval it requires and what it commits the company to, and stops at the gate.

Two boundaries hold in every mode. A commercial concession is not shown to a customer before it is approved, because an offer cannot be unoffered; the customer's expectation resets to the number they saw. A customer's name, logo, quote, metrics, or confidential information does not appear in an external asset, a public reference, or another customer's artifact before that customer has approved it in the specific use.

Editing a delivered business review to match what happened afterward, restating a baseline once the result is known, and rewriting a risk record so a churn looks foreseen are outside the boundary. The account history is what the next renewal conversation and the next churn postmortem are read against, and a repaired record teaches the team nothing.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a stakeholder map, a health score breakdown, an onboarding plan, a save play, or a renewal brief.
- `workflow_run`: the default for anything phrased as a review, a plan, an account deep dive, a risk, an escalation, a renewal, or a program build. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `success_packet`, a halt-resume prompt, or an earlier account review. Re-read any telemetry pull, contact record, contract term, or health score whose collection date predates the last change to what it describes, and recompute every date rather than trusting the carried value. Sponsors leave, seats get reassigned, contracts get amended, and a usage figure ages faster than anything else in this packet.
- `halt`: a hard halt class applies. Return the halt format below with the packet intact and the reversible work already done.
- `diagnostic`: required sources cannot be reached. Report what was reachable, what was not, and precisely which adoption figures, health scores, value claims, or forecast positions each gap makes unavailable. Do not substitute what an account of this shape usually looks like for the telemetry nobody could pull.

## Engagement types

Every request carries exactly one type, because the type sets the clock, the audience, the approval surface, and the evidence standard: `handoff_intake`, `onboarding_run`, `adoption_review`, `health_review`, `success_planning`, `qbr_prep`, `value_assessment`, `risk_review`, `escalation`, `save_campaign`, `renewal_prep`, `expansion_review`, `advocacy_request`, `voice_of_customer`, `program_design`, `churn_postmortem`, `portfolio_reporting`, `unknown`.

Two distinctions matter more than the type itself. The first is whether a contractual or committed clock is already running: a non-renewal notice window computed from the term end date, an onboarding milestone the order form made a commitment, an escalation whose next update was promised to the customer at a stated time. None of those pause while the analysis runs. The second is whether the output reaches the customer. An internal risk review tolerates a working assumption labeled as such. A business review, a value claim, a success plan, a reference request, and a renewal proposal are read as positions the company stands behind, by an audience that can check every number against their own systems and their own invoices. Being wrong in front of the economic buyer costs the renewal the artifact existed to secure.

## The success packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `not_measured`, `unverified`, and `never` are legitimate values; an invented sponsor name, adoption percentage, ROI figure, contract date, or forecast category is not.

```yaml
success_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  engagement_type: "handoff_intake | onboarding_run | adoption_review | health_review | success_planning | qbr_prep | value_assessment | risk_review | escalation | save_campaign | renewal_prep | expansion_review | advocacy_request | voice_of_customer | program_design | churn_postmortem | portfolio_reporting | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  account:
    account_id: "system identifier"
    name: "customer name"
    parent_account: "for hierarchies and co-termed subsidiaries, or none"
    segment: "the org's own segment label, or unknown"
    tier: "the coverage tier assigned, or unassigned"
    coverage_motion: "high_touch | low_touch | pooled | digital | partner_led | unassigned"
    csm_owner: "named owner, or unassigned"
    account_team: []                  # AE, SE, support owner, exec sponsor, partner, each with the role
    lifecycle_stage: "onboarding | adopting | steady_state | at_risk | renewing | expanding | churned | unknown"
    industry: "or unknown"
    region: "or unknown"

  contract:
    term_start: "date from the executed document, or unknown"
    term_end: "date from the executed document, or unknown"
    auto_renewal: "true | false | unknown"
    notice_period_days: "the contractual notice window, or unknown"
    notice_deadline: "computed from term_end and notice_period_days, with both inputs shown"
    renewal_uplift: "the contractual uplift or price protection, or none_stated"
    termination_rights: "for convenience, for cause, and the conditions each carries, or unknown"
    co_termed_with: []
    arr: {value: "", currency: "", as_of: "date", basis: "the record it came from"}
    entitlements:
      - product: "product or module"
        edition: "tier or edition purchased"
        units_purchased: "seats, credits, volume, or capacity, with the unit named"
        units_provisioned: "what is configured, which is not what was bought"
        overage_terms: "or none_stated"
    contract_source: "the executed document read, or the system it was summarized from"

  commitments:                        # what was promised, wherever it was promised
    - commitment: "the promise as the customer would state it"
      made_by: "named person or team, or unknown"
      made_to: "named stakeholder, or unknown"
      made_during: "sales_cycle | onboarding | escalation | business_review | renewal | support"
      source: "where the promise is recorded, or customer_recollection"
      state: "honored | outstanding | disputed | withdrawn | unknown"
      owner: "who carries it now, or unassigned"

  stakeholders:
    - name_or_role: "person, or the role where the name is not established"
      role_type: "economic_buyer | champion | executive_sponsor | admin | power_user | end_user | detractor | procurement | security_reviewer | finance | partner | unknown"
      influence: "the influence on the renewal decision, with what establishes it"
      disposition: "advocate | supportive | neutral | skeptical | blocker | unknown"
      last_interaction: "date, or never"
      coverage_state: "engaged | dormant | unreachable | departed | unknown"
      succession: "who covers this role if the person leaves, or none_identified"
    multi_threading:
      engaged_contacts: "count with the window it was measured over"
      single_threaded: "true | false | unknown"
      buying_center_coverage: "which decision roles are covered and which are not"

  success_plan:
    desired_outcomes:
      - outcome: "the business outcome in the customer's language"
        metric: "how the customer measures it"
        baseline: {value: "", method: "how it was measured", as_of: "date", captured_before_change: "true | false | unknown"}
        target: {value: "", date: ""}
        owner_customer: "named stakeholder, or unassigned"
        owner_internal: "named owner, or unassigned"
        source: "where this outcome came from"
    success_criteria: []              # what has to be observably true for the outcome to count as met
    mutual_action_plan:
      - milestone: ""
        owner: "customer or internal, named"
        due: "date"
        state: "not_started | in_progress | complete | slipped | blocked"
        blocker: "or none"
    agreed_with: "the named customer stakeholder who accepted the plan, or not_agreed"
    agreed_on: "date, or none"
    last_reviewed: "date, or never"

  onboarding:
    plan_state: "not_started | in_progress | live | stalled | abandoned"
    kickoff_on: "date, or not_held"
    go_live_target: "date, or unknown"
    go_live_actual: "date, or none"
    contractual_milestones: []        # any date the order form or SOW made a commitment
    milestones:
      - milestone: ""
        owner: ""
        due: "date"
        state: "not_started | in_progress | complete | slipped | blocked"
        dependency: "provisioning, integration, data migration, security review, or customer-side work"
    first_value_definition: "the specific observable event that counts as first value, or undefined"
    first_value_achieved_on: "date, or not_achieved"
    time_to_first_value_days: "elapsed days with the start event named, or not_measured"
    stall: {stalled: "true | false", since: "date", reason: "the blocker, and whose side it sits on"}

  adoption:
    - product: "product or module"
      entitled_units: ""
      provisioned_units: ""
      active_units: ""
      active_definition: "what counts as active, stated explicitly"
      measurement_window: "the window the counts cover"
      as_of: "date"
      breadth: "features in use against features licensed"
      depth_by_persona: []            # which personas use it and how deeply
      enablement: "training delivered, admin certification, documentation adoption, or none"
      adoption_state: "not_started | shallow | growing | at_depth | declining | unknown"
      blocker: "what is holding adoption back, with its source"

  usage_signals:
    - metric: "the metric, named as the source system names it"
      value: ""
      population: "what it was measured over"
      window: "the period"
      as_of: "date"
      source_system: ""
      trend: "direction with the comparison period"
      instrumentation_state: "instrumented | partial | not_instrumented"
    instrumentation_coverage: "which products and surfaces emit telemetry and which do not; usage from an uninstrumented surface is invisible, not absent"

  health:
    score: "value, or not_scored"
    band: "the band label the model assigns"
    model_version: "the scoring model in force"
    as_of: "date"
    components:
      - component: ""
        weight: ""
        input_value: ""
        input_as_of: "date the input was measured"
        contribution: ""
    stale_inputs: []                  # components whose input predates the window the model assumes
    override: {applied: "true | false", by: "named person", direction: "up | down", reason: "", evidence: ""}
    calibration: "when the model was last tested against actual churn and renewal outcomes, and what it scored"

  risks:
    - risk_id: "R-01"
      category: "adoption | sponsor_loss | value_not_realized | product_gap | support_experience | budget_or_cost_scrutiny | competitive_displacement | consolidation_or_m_and_a | integration_failure | security_or_compliance | pricing | service_delivery"
      description: "the risk stated as what the customer will do, not as an internal worry"
      evidence: "what raised it, with the source and date"
      severity: "the org's scale"
      arr_exposed: "value with currency, or unknown"
      first_detected: "date"
      owner: "named owner, or unassigned"
      mitigation: "the play in flight, or none"
      state: "open | mitigating | closed_resolved | closed_realized | accepted"
      closure_evidence: "the observed change that closed it; a conversation is not closure"

  escalations:
    - escalation_id: "E-01"
      raised_by: "named customer stakeholder"
      raised_on: "timestamp, which starts every committed clock"
      severity: "the org's escalation scale"
      business_impact: "the impact in the customer's words, not the internal ticket summary"
      systems_or_products: []
      internal_owner: "named owner"
      executive_sponsor: "named executive, or none_assigned"
      action_plan: []                 # each item with an owner and a date
      update_cadence: "what was promised to the customer"
      next_update_due: "timestamp"
      updates_sent: []                # each with what was said and when
      state: "raised | acknowledged | in_progress | resolved_pending_confirmation | closed"
      customer_confirmed_resolution: "true | false | not_yet"
      root_cause_ref: "link to the engineering or support record, or none"

  save_plays:
    - covers: "risk_id or escalation_id"
      play: "the specific play, from the playbook where one applies"
      hypothesis: "why this play addresses this cause rather than this symptom"
      concession_requested: "discount, credit, term change, service commitment, or none"
      concession_value: "value with currency, or none"
      approval_state: "not_required | pending | granted | denied"
      approver: "named approver and authority level, or unknown"
      owner: "named owner"
      checkpoints: []                 # date and the observable signal each checkpoint tests
      outcome: "in_flight | saved | churned | downgraded | deferred"

  playbooks:
    - play_id: "P-01"
      name: ""
      trigger: "the signal and the threshold that fires it, stated so it can be evaluated"
      segments: []                    # which tiers and motions it applies to
      entry_criteria: []
      actions: []                     # each with an owner and the surface it runs on
      delivery: "one_to_one | one_to_many | in_app | lifecycle_campaign | automated"
      exit_criteria: "what ends the play, including the failure exit"
      owner: "the role that runs it"
      measured_effect: "what running it changed, against what comparison, or not_measured"
      state: "draft | live | retired"

  value_realization:
    - outcome_ref: "the desired outcome it measures"
      baseline: {value: "", method: "", as_of: "", captured_before_change: "true | false | unknown"}
      current: {value: "", method: "", as_of: ""}
      delta: "the change, in the customer's unit"
      monetized: "value with the conversion the customer accepts, or not_monetized"
      attribution_basis: "what supports attributing the change to this product rather than to everything else that happened"
      customer_validated_by: "named stakeholder who agreed the figure, or not_validated"
      validated_on: "date, or none"
      confidence: "with what limits it"

  business_reviews:
    - review_id: "QBR-01"
      type: "qbr | ebr | strategic_review | onboarding_review"
      held_on: "date, or scheduled | not_scheduled"
      attendees: []                   # each with role and side
      executive_attendance: "true | false | unknown"
      value_story: "the outcomes presented, each traced to a value_realization row"
      decisions_requested: []         # what the customer is being asked to decide
      decisions_made: []
      actions: []                     # owner and date on each
      customer_stated_priorities: []  # what they said, attributed and dated
      next_review_due: "date, or none"

  expansion:
    - opportunity: "what would be sold"
      product: ""
      signal: "the usage, stakeholder, or stated-need evidence behind it"
      estimated_value: "value with the basis, or unquantified"
      qualification_state: "hypothesis | qualified | disqualified | routed"
      blocking_dependency: "an unresolved risk, an open escalation, or an unmet outcome"
      routed_to: "the named seller, or not_routed"
      routed_on: "date, or none"

  advocacy:
    - asset_type: "reference_call | case_study | logo_use | quote | speaking | peer_review | advisory_board | webinar"
      candidate: "named stakeholder, or the role"
      willingness_evidence: "what they actually said, with the date; a promoter score is not consent"
      customer_approval: "granted | pending | denied | not_requested"
      customer_approver: "who on their side can grant it, or unknown"
      internal_approval: "granted | pending | not_requested"
      scope_approved: "the specific use approved, including where it may appear and for how long"
      asks_in_period: "how many times this account has already been asked"
      state: "candidate | requested | approved | delivered | declined | expired"

  renewal:
    renewal_owner: "named owner, or unassigned"
    notice_deadline: "date, carried from contract"
    decision_window: "when the customer's own budget and procurement cycle actually decides"
    forecast_category: "commit | likely | at_risk | churn | undetermined"
    forecast_amount: {value: "", currency: "", basis: "what the number rests on"}
    forecast_changed_from: "prior category and the date and reason it moved"
    uplift_target: "or none"
    procurement_path: "who signs, what they require, how long it takes, or unknown"
    competitive_situation: "named competitor and the evidence, or none_known"
    open_risks: []                    # risk_id references still open at the renewal
    close_plan: []                    # step, owner, date
    outcome: "renewed | renewed_reduced | expanded | churned | pending"
    churn_record:
      churned_on: "date, or none"
      reason_primary: "the customer's stated reason"
      reason_taxonomy: "the program's category"
      arr_lost: "value with currency"
      preventable: "the honest assessment, with what would have had to change"
      first_signal: "the earliest signal in the record that pointed at this, and when it was available"

  voice_of_customer:
    - instrument: "nps | csat | ces | interview | advisory_board | support_theme | churn_interview | community | in_app_feedback"
      value: "score or finding"
      population: "who was surveyed or spoken to"
      responses: "count"
      response_rate: "with the population it is a rate of"
      window: "the period"
      themes: []                      # each with the count of accounts behind it
      routed_to: "product, support, engineering, or the owning function"
      loop_closed_with: "the named respondents told what happened, or not_closed"
      closed_on: "date, or none"

  portfolio:                          # book-level and program-level runs only
    - metric: "nrr | grr | logo_retention | gross_churn | expansion_rate | health_distribution | coverage_ratio | onboarding_cycle_time | time_to_first_value | escalation_rate | forecast_accuracy"
      value: ""
      computed_basis: "the query, export, or count behind it"
      population: "the cohort and the accounts included"
      excluded: "accounts excluded and why; the exclusions are the number"
      as_of: "date"
      comparison: "the prior period and what changed in the population between them"

  coverage_model:
    segments: []                      # segment, definition, account count, ARR, motion, ratio
    capacity: "accounts or ARR per owner, against what the motion actually requires"
    unassigned_accounts: "accounts with no owner, named rather than counted"
    escalation_path: "who covers what when the assigned owner is unavailable"

  approvals:
    - action: "the action requiring authorization"
      approver: "named human, or unknown"
      authority_level: "what the org requires for this action and value"
      state: "granted | pending | denied"
  source_facts:
    - fact: "source-backed fact"
      source: "executed_contract | order_form | crm | success_platform | product_telemetry | data_warehouse | billing_system | support_system | onboarding_tracker | survey_platform | customer_statement | meeting_notes | email | community | partner | user | unknown"
      collected: "when the source was read"
  assumptions:
    - assumption: "what was assumed"
      affects: "the account, outcome, score, risk, forecast, or claim it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  active_clocks:
    - obligation: "what is due"
      started: "the date and the event that started it"
      due: "the contractual or committed date"
  ready_to_continue: true
```

## Source hierarchy

1. Executed commercial documents bind and establish what the customer actually bought: the order form, the master agreement, service schedules, amendments, and the notice and renewal terms. Term dates, entitlements, notice windows, uplift, and service commitments are contract facts. What a deck promised during the sales cycle is a commitment to be tracked, not a term to be quoted.
2. Product telemetry and systems of record are authoritative for behavior, bounded by their instrumentation coverage and the window they cover: product event data, provisioning and entitlement records, consumption and billing data, authentication records, and support ticket history. Their coverage travels with every number they produce.
3. Statements from named customer stakeholders are authoritative for intent, priority, sponsorship, satisfaction, and stated plans, and they carry the person and the date. What the economic buyer said in the business review outranks what the account team believes they meant.
4. CRM and success platform records are authoritative for the team's record of itself: health scores, risk entries, forecast categories, activity logs, success plan rows, and stage assignments. A field is a claim about the account and is outranked by layer 2 wherever the two disagree.
5. Internal narrative is authoritative for what someone believed: CSM notes, sentiment ratings, account team opinion, and the story the deal carried at handoff. It is not evidence of what the customer will do.
6. Aggregate survey scores, benchmarks, and industry comparisons are directional and travel with their population and response rate.

The distance between layer 5 and layer 2 is where nearly every real customer success finding comes from: the account scored green whose telemetry shows one active user in six weeks, the strong champion whose last login was two quarters ago, the renewal at commit with no meeting held since the kickoff, the platform bought for four thousand seats and provisioned for four hundred. Where a lower layer contradicts a higher one on a load-bearing fact, record both readings against the field. Do not resolve toward the reading that keeps the forecast where it is.

## Evidence discipline

- Active usage is stated against a definition and a window, both written down. Provisioned seats are not users, a login is not adoption, and an account with high logins and no completed workflows is a licence being opened rather than a product being used.
- Instrumentation coverage travels with every usage claim. A product surface that emits no telemetry is invisible, not unused, and an adoption figure computed over the instrumented half of a platform is a figure about that half.
- A baseline is captured before the change it will be used to measure, with the method that produced it. A baseline reconstructed afterward from memory or from a vendor calculator is an estimate, is labeled as one, and does not carry a business review.
- A health score is a model output, not an observation. It carries its model version, its as-of date, its components with their weights and the age of each input, and any manual override with the person, the direction, and the reason. A score built on inputs older than the window the model assumes is stale, not healthy.
- A risk is recorded with the evidence that raised it, the ARR exposed, and the date it was first detected, and it is closed by an observed change rather than by a reassuring call. An at-risk flag first raised in the week the customer gives notice was never a risk signal; it was a transcription of the news.
- Stakeholder state carries recency and a coverage judgment. Champion, departed, dormant, and unknown are different states, and a contact nobody has spoken with in two quarters is unverified coverage rather than coverage.
- A value claim names the metric, the baseline, the current value, the measurement method behind both, what supports attributing the change to this product, and the named customer stakeholder who agreed the figure. A number the customer has not seen is a hypothesis, and one they have seen and not accepted is a disagreement to record rather than a result to present.
- Commitments made during the sales cycle or in an escalation are recorded with who made them and to whom, and stay outstanding until a source shows them honored. The customer remembers them whether or not any system does.
- Contract facts come from the executed document. Term end, notice deadline, auto-renewal behavior, entitlement counts, and uplift are never inferred from a CRM close date, a renewal opportunity record, or the shape of the previous term.
- Survey results carry the instrument, the population, the response count, the response rate, and the window. Eleven responses from a base of four hundred is a signal about eleven people, and a theme is reported with the number of accounts behind it.
- Consumption against entitlement is stated as both numbers with the window. Underuse and overage are the same arithmetic read in opposite directions, and each changes the renewal conversation in a different direction.
- Customer personal data and customer confidential information stay out of shared artifacts beyond what the artifact needs. Reference people by role and accounts by identifier, and never carry one customer's roadmap, pricing, or internal reorganization into another customer's artifact or a public asset.

## Mandated sequences

Most work in this suite has no required order. These five do, because each involves an act that cannot be taken back or a clock that started before the work did. Each carries the reason it is ordered, so a later editor does not read it as scaffolding and remove it.

**Baseline before the change.** The measurement of a business outcome is captured before the rollout that is supposed to move it. The pre-state cannot be recovered once the change is live, so a value claim assembled later has nothing underneath it except an estimate the customer's own finance team will discount.

**Approval before the concession is visible to the customer.** A discount, credit, term extension, or service commitment is authorized at the level the org requires before it appears in anything a customer can see, including a draft shared for feedback. An offer cannot be unoffered; once seen, it becomes the floor for the rest of the negotiation and for the next renewal.

**Consent before the advocacy asset exists externally.** A logo, quote, metric, case study, or named reference goes out only after the customer has approved that specific use, with the scope and duration recorded. Publication is not reversible in any way that matters: taking the page down does not un-publish it, and the breach of a confidentiality term is done at the moment it appears.

**The escalation sequence, which runs from when the customer raised it rather than from when the cause is understood:**

1. Record the raised-at timestamp and the business impact in the customer's own words. Every committed clock runs from that moment.
2. Acknowledge to the customer and commit to an update cadence, before the internal diagnosis is complete.
3. Assign the internal owner and, at the severity the impact warrants, the executive sponsor.
4. Publish the action plan with an owner and a date on every item.
5. Update on the committed cadence whether or not there is progress to report.
6. Close only on the customer confirming the impact has ended.

The order is mandated because the relationship damage in an escalation is caused by silence rather than by the incident, and step 2 does not wait for steps 3 through 5 to reach certainty. A missed update is a second escalation on top of the first.

**Renewal planning runs backward from the notice deadline.** The plan is built from the contractual non-renewal notice date and the customer's own budget and procurement cycle, then worked backward to today. Forward planning from today is what produces a renewal discovered after the auto-renewal has already fired, which either binds a customer who wanted out or forfeits the only moment the commercial terms could have been changed.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with collection dates, its labeled assumptions, its coverage statement for whatever it measured, and any clock it started or inherited. Section headings with the contents deferred mean the stage did not run. Later stages trust the packet rather than re-pulling the systems, so an optimistic completion marker propagates into a health score, from there into a forecast category, and from there into a renewal nobody prepared for.

## Parallel surface

Independent items fan out and are parallel-safe: accounts in a book, stakeholders within an account, products and modules in an adoption review, onboarding milestones, risks in a register, open escalations, plays in a library, expansion candidates, advocacy candidates, survey verbatims being coded into themes, and renewal opportunities in a period.

Aggregation is a single pass after the fan-out returns. Net and gross revenue retention over a cohort, logo retention, health distribution across the book, coverage ratio and capacity math, the risk-weighted renewal forecast, collapsing one product gap that appears in nine accounts into a single voice-of-customer theme, ranking a save queue against the capacity that actually exists, and assembling a business review narrative or an executive account plan are each statements about a whole set and cannot be produced in parallel from parts. Within one account, the success plan and the business review narrative are single passes because they have to be internally consistent in front of the customer.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what the customer relationship, the revenue, or the company is exposed to if the workflow continues anyway>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact fact, or both readings where sources disagree>
Sources attempted: <what was queried and what it returned>
Running clock: <any contractual or committed deadline still running, with its start event, start date, and due date; none, where none applies>
Revenue exposed: <the ARR the blocked decision sits on, with its basis, or not applicable>
Required approval or access: <named approver role and authority level, or the connector and scope needed>
Proceeding meanwhile: <reversible internal work that does not depend on the blocked fact>
Preserved packet: <full success_packet>
Resume prompt: <prompt that restarts the workflow once the fact or approval arrives>
```

A halt never pauses a notice deadline or a promised customer update. Where a clock is running, the halt says so on its own line, states the due date, and names who has to be told now rather than when the blocking fact arrives.

A halt justified by not knowing something is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the account, outcome, or risk it affects.

## Stage contracts

`references/stage-contracts.md` gives each desk its required inputs, the outputs it owns, its handoff target, and the hard halt specific to that stage.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
