# Customer Support Suite Workflow Contract

This file defines how Customer Support Command Desk skills run as one continuous program of work instead of behaving as isolated one-off prompts. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is a queue of people who are already having a bad day, each one carrying a clock that started before anybody looked at it, each one waiting for a written answer that has to still be true tomorrow. The packet therefore carries the ticket record, the entitlement that sets the targets, every clock already running, the evidence that was actually collected rather than the evidence that would have been useful, and the approval state of anything that reaches a customer or acts on the whole queue. The distinguishing failure of this domain is not a slow answer. It is a fluent, specific, confidently worded answer that turns out to be wrong and is now permanently in the customer's inbox with a timestamp on it.

## Continuity rule

A desk that has the facts to run the next stage runs it. A run that ends at "this should be escalated to engineering" or "consider reviewing backlog aging" is a routing note rather than support work, and it hands the sequencing problem back to the person whose SLA clock is running. Complete the current stage, update `support_packet`, and continue until the requested outcome exists or a hard halt applies.

Three things are never continued through: anything that reaches a customer, anything that acts on the live queue or the helpdesk configuration, and any statement about a cause, a fix, or a date that the engineering record does not support. Everything else continues, with the assumption labeled inline against the ticket, severity, driver, article, or metric it affects.

## Action boundary

This suite produces triage decisions, diagnoses, reproduction records, defect drafts, escalation packages, reply and update drafts, article drafts, macro audits, queue and backlog analyses, staffing models, QA scorecards, driver analyses, and reports. It does not send a reply, post to a status page, publish or retire a knowledge base article, solve, close, merge, reassign, or bulk-modify tickets, activate or edit a trigger, routing rule, SLA policy, or auto-close rule, file or close a record in the engineering tracker as the record, page on-call, commit a fix version or a fix date, issue an SLA credit, refund, or goodwill concession, reset credentials, change configuration in a customer's tenant, or send a survey. For each of those the desk prepares the exact item, names the approval it needs and what it commits the company to, and stops at the gate.

Two boundaries hold in every mode. Account data is not disclosed and account state is not changed until the requester is established as authorized on that account, because a disclosure cannot be withdrawn and support is the documented entry point for social engineering. And one customer's ticket content, configuration, incident detail, log output, or name never appears in another customer's reply, in a public article, or in a shared example.

Editing a sent reply out of the record, restating a severity after the outcome is known, backdating a first response, and adjusting a pause on an SLA clock so a breach reads as compliant are outside the boundary. The ticket record is what the credit calculation, the escalation review, and the next contract negotiation are read against, and a repaired record teaches the team nothing while exposing the company to more than the original miss did.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a severity assessment, a reproduction record, a macro audit, a backlog aging read, or a staffing model for one interval set.
- `workflow_run`: the default for anything phrased as a ticket, an escalation, an outage, a backlog problem, a quality problem, or a program build. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `support_packet` or a halt-resume prompt. Recompute every clock rather than carrying the value forward, and re-read the ticket thread, the tracker state, and the queue counts, because a customer replied, an engineer updated the defect, and the backlog moved while the packet sat still. A time-remaining figure is the fastest-aging field in this packet.
- `halt`: a hard halt class applies. Return the halt format below with the packet intact, the reversible work already done, and every running clock named.
- `diagnostic`: required systems cannot be reached. Report what was reachable, what was not, and precisely which severities, causes, SLA positions, queue figures, or metrics each gap makes unavailable. Do not substitute what a problem of this shape usually turns out to be for the telemetry nobody could pull.

## Request types

Every request carries exactly one type, because the type sets the clock, the audience, the approval surface, and the evidence standard: `ticket_triage`, `severity_sla`, `troubleshooting`, `bug_intake`, `engineering_escalation`, `customer_response`, `closure_review`, `incident_comms`, `post_incident_followup`, `knowledge_authoring`, `deflection_review`, `queue_review`, `backlog_recovery`, `staffing_plan`, `tooling_change`, `qa_review`, `driver_analysis`, `metrics_reporting`, `unknown`.

Three distinctions matter more than the type itself.

The first is whether a clock is already running. A first response or restoration target from the entitlement, an update cadence promised to a customer, a status page update promised for a stated time, and a contractual credit window all keep running while the analysis runs, and none of them restart when the work does.

The second is whether the output reaches a customer in writing. An internal queue review tolerates a working assumption labeled as such. A reply, a status page post, a reason-for-outage letter, and a published article are read as the company's position, are permanently quotable, and in an enterprise account are forwarded to the person who signs the renewal.

The third is blast radius. A single reply is wrong for one customer. A macro, a trigger, a routing rule, an auto-close rule, a status page post, and a published article are wrong for everyone at once, including the tickets already open, and the mistake arrives in thousands of inboxes before anyone notices it.

## The support packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `not_reproduced`, `cause_unconfirmed`, `not_measured`, and `none` are legitimate values; an invented cause, fix version, SLA target, article reference, ticket count, or satisfaction score is not.

```yaml
support_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  request_type: "ticket_triage | severity_sla | troubleshooting | bug_intake | engineering_escalation | customer_response | closure_review | incident_comms | post_incident_followup | knowledge_authoring | deflection_review | queue_review | backlog_recovery | staffing_plan | tooling_change | qa_review | driver_analysis | metrics_reporting | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  ticket:
    ticket_id: "system identifier"
    channel: "email | web_form | chat | phone | in_app | community | social | api | partner | internal"
    received_at: "timestamp on the customer's side of the channel, which is what every clock runs from"
    first_touched_at: "timestamp, or not_touched"
    subject_as_written: "the customer's own words, not the agent's summary"
    contact_reason: "code from the taxonomy in force, or uncoded"
    product: ""
    product_area: ""
    version_or_build: "the version the customer is actually on, or unknown"
    deployment: "multi_tenant_cloud | dedicated | self_hosted | hybrid | unknown"
    environment: "production | staging | sandbox | unknown"
    locale_and_timezone: "which sets the coverage calendar that applies"
    queue: "group or queue currently holding it"
    assignee: "named agent, or unassigned"
    tier: "the support tier currently holding it"
    state: "new | open | pending_customer | pending_engineering | on_hold | solved | closed"
    linked: []                       # merged, duplicate, follow-up, or parent tickets, each with the relation
    incident_ref: "incident id where this ticket belongs to a mass event, or none"

  requester:
    contact: "named person, or the role where the name is not established"
    account_id: "customer account or organization identifier"
    account_name: ""
    authorization_state: "verified | unverified | failed | not_required"
    authorization_method: "how it was established, or none"
    named_contact: "true | false | unknown"     # whether this person is entitled to raise support at all
    prior_tickets: "count and window, or unknown"
    relationship_context: "open escalation, renewal window, or executive attention, where a source establishes it"

  entitlement:
    support_plan: "the plan on the executed agreement, not the label in the account record"
    coverage_calendar: "24x7 | follow_the_sun | business_hours with the timezone and the holiday calendar named"
    channels_entitled: []
    severity_scheme: "the scheme the contract actually uses"
    targets:
      - severity: ""
        first_response: "target with its unit and calendar"
        subsequent_response: "target, or none_stated"
        restoration: "target, or none_stated"
        resolution: "target, or none_stated"
    credit_terms: "what a breach entitles the customer to, or none_stated"
    entitlement_source: "the executed agreement or the entitlement record read, with the date"
    out_of_scope: "work the plan does not cover, where that is the finding"

  clocks:
    - obligation: "first response, next update, restoration, status page update, credit window"
      started_at: "timestamp and the event that started it"
      target_at: "timestamp"
      calendar: "the calendar the target is computed on"
      state: "running | paused | met | at_risk | breached"
      paused_at: "timestamp, or none"
      pause_reason: "the contractual pause rule invoked, or none"
      pause_rule_source: "where that rule is written, or unsupported"
      met_at: "timestamp, or none"

  severity:
    value: "the level on the scheme in force"
    impact_statement: "who is blocked, from doing what, at what scale, in the customer's words"
    users_affected: "count or proportion with how it was determined, or unknown"
    workaround: "the workaround and its cost to the customer, or none_available"
    business_hours_impact: "whether the impact is continuous or confined to a window"
    set_by: "named person or rule"
    changed_from: "prior value with the date and the reason it moved"
    disputed_by_customer: "true | false"

  diagnosis:
    symptom_reported: "as reported"
    symptom_observed: "what was actually seen, or not_observed"
    fault_domain: "product_defect | configuration | integration | customer_environment | data | third_party | capacity | expected_behavior | enablement_gap | undetermined"
    hypotheses:
      - hypothesis: ""
        test: "the observation that would confirm or eliminate it"
        result: "confirmed | eliminated | untested"
    evidence:
      - item: "log extract, HAR, trace, screenshot, config export, diagnostic bundle, query result"
        collected_from: "the system and the scope"
        collected_at: "timestamp"
        covers_window: "the period the evidence covers"
        retention_limit: "where the source window truncated what was available"
        redaction_state: "redacted | unredacted | not_required"
    known_error_ref: "the known error record this symptom was matched to, or none_matched"
    workaround_given: "what the customer was told to do, and whether it worked"
    cause: "the cause statement"
    cause_confidence: "suspected | isolated | confirmed_by_engineering | unconfirmed"

  reproduction:
    state: "reproduced | partially_reproduced | not_reproduced | not_attempted"
    steps: []
    environment: "the build, edition, configuration, and data conditions used"
    versions_tested: []
    expected_vs_actual: "both, stated plainly"
    frequency: "always | intermittent with a rate | once"
    first_seen: "date, or unknown"
    regression: "true | false | unknown"
    last_known_good: "version or date, or unknown"
    attempts_that_failed: "what was tried and did not reproduce it, so nobody repeats it"

  defect:
    tracker_ref: "the issue identifier, or not_filed"
    title: ""
    state: "as the tracker reports it, with the date read"
    fix_version: "as the tracker reports it, or none_committed"
    engineering_owner: "named, or unassigned"
    last_engineering_update: "date and what it said"
    tickets_attached: "count and the accounts behind them"
    customer_told: "what the customer has been told about this defect and when"

  escalation:
    escalation_id: "E-01"
    from_tier: ""
    to_target: "tier 2, tier 3, engineering, on-call, or the named team"
    raised_at: "timestamp"
    criteria_met: "the escalation criterion actually satisfied, not the pressure that prompted it"
    package_completeness: "what the receiving team needs and what is missing"
    acknowledged_at: "timestamp, or not_acknowledged"
    cadence_promised: "to the customer and to the internal owner"
    next_update_due: "timestamp"
    state: "raised | acknowledged | in_progress | returned | closed"
    de_escalated_at: "timestamp, or none"

  incident:
    incident_id: "or none"
    impact_started_at: "timestamp from system evidence, which is what credits and the outage letter run from"
    declared_at: "timestamp"
    severity: "the incident scheme, which is not the ticket severity scheme"
    affected_scope: "what is affected and what is not, with how the scope was determined"
    scope_method: "system evidence | inferred | undetermined"
    accounts_identified: "count and the query that produced the list, or not_identified"
    published_position: "the current holding or update text in force"
    status_page_state: "investigating | identified | monitoring | resolved | not_posted"
    updates_published: []            # each with the timestamp and what it said
    next_update_due: "timestamp"
    mitigated_at: "timestamp, or none"
    resolved_at: "timestamp, or none"
    recovery_confirmed_by: "system evidence and at least one affected customer, or unconfirmed"
    rfo_committed: "true | false"
    rfo_due: "date, or none"
    credits_triggered: "the contractual trigger and the accounts it applies to, or none"

  responses:
    - purpose: "acknowledgement, update, workaround, resolution, apology, closure, outage notice"
      audience: "one customer | affected accounts | all customers"
      draft: "the text as it would be sent"
      macro_ref: "the macro, canned response, or saved reply it derives from, or none"
      claims: []                     # every factual claim in the draft with the source behind it
      commitments: []                # anything the customer will hold the company to, with the date
      approval_state: "not_required | pending | granted | denied"
      approver: "named approver and authority, or unknown"
      sent_state: "draft | approved | sent"

  resolution:
    code: "the resolution code from the scheme in force"
    summary: "what was actually done"
    fix_type: "fixed | workaround | configuration_change | documentation | expected_behavior | not_reproduced | no_customer_response | duplicate | out_of_scope"
    customer_confirmed: "true | false | not_asked"
    confirmed_at: "timestamp, or none"
    closed_at: "timestamp, or none"
    auto_close_rule: "the rule that would close it without a human, or none"
    reopen_count: ""
    reopen_reasons: []
    survey_state: "sent | suppressed with the reason | not_sent"
    survey_result: "score and verbatim, or none"

  knowledge:
    - article_ref: "identifier, or draft"
      title: ""
      state: "draft | in_review | published | needs_update | archived"
      source_tickets: []             # the contacts that justify the article existing
      applies_to_versions: "the versions and editions the content is true for"
      last_verified_against: "the build the steps were actually checked on, with the date"
      owner: "named owner, or unowned"
      findability_terms: "the words customers actually use, not the words the product uses"
      linked_in_replies: "count, or unknown"
      deflection_evidence: "the contact reduction attributable to it, or not_measured"

  self_service:
    surfaces: []                     # help center, in-product help, community, automated answering, each with its coverage
    search_failures: []              # queries returning nothing useful, with their volume
    containment_rate: "value with the exact denominator stated, or not_measured"
    abandoned_sessions: "counted or excluded, stated explicitly"
    escalate_to_human_path: "how a customer gets out of self-service, and how long it takes"
    coverage_gaps: []                # top contact drivers with no self-service answer

  queue_health:
    - queue: ""
      window: "the period the counts cover"
      inflow: ""
      outflow: ""
      open_total: ""
      age_cohorts: []                # each cohort with its count, not one aggregate
      untouched: "open, never responded to, with the oldest"
      pending_customer: "held separately, because it is waiting rather than working"
      pending_engineering: "held separately, with the oldest and its defect reference"
      at_risk: "count of clocks approaching target"
      breached: "count, with the accounts and the credit exposure"
      reopen_rate: "with the definition of a reopen in force"
      wip_per_agent: ""
      counting_rules: "whether merges, duplicates, spam, and automated tickets are included"

  workforce:
    forecast:
      - interval: "the interval, with the timezone"
        predicted_volume: "with the basis and the historical window behind it"
        actual_volume: "where the interval has passed"
    handle_time: "with the definition and the population it was measured over"
    required_heads: "with the model, the target, and the assumptions it rests on"
    scheduled_heads: ""
    shrinkage: "value and what it includes"
    occupancy: ""
    adherence: ""
    coverage_gaps: []                # intervals, languages, skills, or products with no cover
    on_call: "the after-hours rota and what it is entitled to be woken for"
    skill_matrix: "who can actually take what, which is what makes routing work"

  tooling:
    platform_area: "fields, forms, views, triggers, automations, routing rules, SLA policies, macros, bots, integrations"
    change_description: ""
    blast_radius: "which tickets it acts on, including ones already open"
    environment: "sandbox | production"
    validated_against: "the sample it was tested on, or not_validated"
    suppression_path: "how it is turned off, and how fast"
    approval_state: "not_required | pending | granted | denied"

  quality:
    scorecard_version: ""
    sample_plan: "how tickets were selected, and over what population"
    sample_size: ""
    reviews: []                      # each with the ticket, the dimension scores, and the evidence quoted
    dimension_scores: []
    calibration: "when reviewers were last calibrated and the variance between them"
    coaching_actions: []             # each with the agent, the behavior, and the follow-up date
    appeals: []
    auto_qa_coverage: "what proportion is machine scored and what that scoring can actually detect"

  drivers:
    - driver: "the contact driver in the taxonomy"
      volume: "count with the window and the queue"
      trend: "against a named comparison period with the population held constant"
      contacts_per_active_account: "with the account population it is a rate over"
      handle_cost: "with the basis, or not_costed"
      underlying_cause: "the cause, distinguished from the symptom that surfaced it"
      owning_function: "product, engineering, docs, billing, onboarding, or support itself"
      routed_state: "not_routed | routed | accepted | fixed | declined"
      fix_state: "with the evidence, or none"
      deflectable: "whether an article or a self-service surface could have answered it"

  metrics:
    - metric: "first response time | next response time | resolution time | first contact resolution | csat | ces | reopen rate | backlog age | contact rate | containment rate | cost per contact | breach rate | forecast accuracy"
      value: ""
      definition: "the definition in force, written out, because each of these has several defensible ones"
      population: "what it was computed over, including exclusions"
      window: ""
      as_of: "date"
      source_system: ""
      response_rate: "for any survey-derived metric, with the population it is a rate of"
      comparison: "the prior period and what changed in the population between them"

  approvals:
    - action: "the action requiring authorization"
      approver: "named human, or unknown"
      authority_level: "what the org requires for this action and this reach"
      state: "granted | pending | denied"
  source_facts:
    - fact: "source-backed fact"
      source: "ticket_thread | helpdesk_record | entitlement_record | executed_agreement | product_telemetry | application_logs | issue_tracker | known_error_record | status_page | knowledge_base | product_documentation | release_notes | reporting_layer | survey_platform | agent_note | customer_statement | user | unknown"
      collected: "timestamp the source was read"
  assumptions:
    - assumption: "what was assumed"
      affects: "the ticket, severity, cause, reply, driver, or metric it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. The ticket thread as the customer wrote it, with its timestamps, binds what was asked, what was promised in reply, and when. Every clock, every credit calculation, and every escalation review resolves onto these timestamps. An agent's summary of the thread is layer 5.
2. The executed agreement and the entitlement record establish coverage, targets, credit terms, and what is in scope at all. Severity targets, calendars, and pause rules are contract facts. A plan name in the account record is a label pointing at them, not a substitute for reading them.
3. System evidence is authoritative for what happened, bounded by its retention window and its instrumentation coverage: application and platform logs, traces, error records, tenant configuration state, audit logs, authentication records, and the observed state of the affected environment.
4. The engineering record is authoritative for defect state: the issue tracker, the known error database, release notes, and the status page history. Fix state, fix version, and any date belong to this layer and are reported with the date they were read.
5. Product documentation and the knowledge base are authoritative for documented expected behavior, against a stated version. A mismatch between the documentation and the product is a finding to route, never a resolution to send.
6. The helpdesk reporting layer is authoritative for the team's record of itself: queue counts, satisfaction scores, handle times, and SLA compliance. It is outranked by layer 1 for any individual ticket fact and by layer 3 for anything about the product.
7. Agent notes, internal comments, and the team's working belief about a cause are authoritative for what someone thought, at the time they thought it. They are not evidence of what happened.

The distance between layer 7 and layer 3 is where most real support findings live: the ticket resolved as user error against logs showing a server-side timeout, the "known issue" nobody matched to a known error record, the intermittent bug that reproduces every time on one edition, the queue that looks healthy because six hundred tickets sit in pending-customer forever. Where a lower layer contradicts a higher one on a load-bearing fact, record both readings against the field. Do not resolve toward the reading that lets the ticket close.

## Evidence discipline

- Every clock runs from a recorded timestamp on the customer's side of the channel. A first response time measured from when a ticket appeared in a view is a number about the routing rule, not about how long the customer waited.
- An SLA target is read from the entitlement and the agreement behind it, with its calendar and timezone attached. A target quoted without its calendar is half a target, and a clock paused outside the contractual pause rule is a breach wearing a compliance label.
- Severity is set from customer impact: who is blocked, from doing what, at what scale, and whether a workaround exists. It is not set by how loudly the request arrived, how large the account is, or how hard the fix looks. Account size changes who gets told and how fast; it does not change the severity, and a queue where it does has no ordering left.
- Reproduced is a state with a build, an edition, a configuration, and the steps that produced it. Not reproduced carries what was tried and on what, so the next person does not repeat it. A screenshot is a symptom, and a customer's account of the steps is a hypothesis about the steps.
- A workaround is not a fix. A ticket resolved by a workaround stays attached to the defect record, because closing it silently is what makes a live defect look like it stopped affecting anyone.
- Cause is stated at the confidence it was established: suspected, isolated, or confirmed by engineering. "Known issue" is a specific claim that this symptom matched a specific known error record, and it travels with that record's identifier or it is not that claim.
- Fix versions and fix dates belong to the engineering record. Support reports what the tracker said and when it said it. A date spoken out loud to a customer is a date they plan around, and support does not own the schedule that produces it.
- Logs, HAR files, screenshots, diagnostic bundles, and data extracts routinely carry credentials, session tokens, API keys, and other people's personal data. They are redacted before they leave the ticket for a tracker, an article, or any shared artifact, and the redaction is recorded. A token pasted into an issue is disclosed to everyone with tracker access, and rotation is the only remedy left.
- Telemetry has a retention window. A log that aged out is unavailable, not clean, and "nothing in the logs" for a period outside retention is a statement about retention.
- Ticket volume carries its window, its queue, and its counting rules, with merges, duplicates, spam, and machine-generated tickets stated as included or excluded. The same month moves by a fifth depending on those rules alone.
- Backlog is reported by age cohort with untouched, awaiting-customer, and awaiting-engineering held apart. A single open count hides a ticket nobody has read since March inside a number that also contains this morning's arrivals.
- Satisfaction metrics carry the instrument, the population surveyed, the response count, and the response rate. A score from eleven responses across four hundred solved tickets is a statement about eleven people, and who answers a support survey correlates with the outcome being measured.
- First contact resolution, resolution time, and handle time each carry the definition in force, because each has several defensible definitions and the gap between them is usually larger than any improvement a team will make this quarter.
- Containment and deflection carry their denominator. A rate that drops abandoned sessions, or counts a help center visit that ended in a ticket as contained, is measuring the instrumentation.
- Article accuracy is stated against a version and a verification date. An article documenting a release the customer is not running is wrong for that customer, and linking it in a reply hands them the error.
- Requester identity and entitlement are established before account data is disclosed or account state changed, and the method is recorded.

## Mandated sequences

Most work in this suite has no required order. These have one, because each involves an act that cannot be taken back or a clock that started before the work did. Each carries the reason it is ordered, so a later editor does not read it as scaffolding and strip it.

**Identity and entitlement before account data.** The requester is established as authorized on the account before account data is disclosed, credentials are reset, or configuration is changed. The check has no value after the answer has been sent, and support is the documented entry point for social engineering against every other control the company has.

**Redaction before evidence leaves the ticket.** Logs, HAR files, diagnostic bundles, screenshots, and data extracts are redacted before they are attached to a defect, an article, or any artifact outside the ticket. A credential or a personal record copied into a tracker is present in every downstream index, notification, and export of it, and no later deletion reaches those copies.

**Acknowledgement before the cause is known.** The first customer-facing acknowledgement and the committed update cadence go out before diagnosis is complete, and updates continue on that cadence whether or not there is progress to report. The damage in a support failure comes from silence rather than from the fault, and a missed promised update becomes a second complaint stacked on the first.

**Sandbox validation and a suppression path before a queue-wide automation goes live.** A trigger, routing rule, SLA policy, auto-close rule, or macro change is validated against a real sample and given its off switch before it acts on the live queue. These act on every matching ticket at once, including ones already open, and mail sent by a misfiring automation cannot be recalled from the inboxes it reached.

**Customer confirmation before closure, above the severity threshold the org sets.** Closure stops the clock, fires the survey, and in most platforms cannot be undone; a customer who comes back gets a new ticket with a new clock and none of the history. The record of how long they actually waited is destroyed by the close, not by the reopen.

**The customer-facing incident sequence, which runs from when impact started rather than from when the cause is understood:**

1. Determine the affected scope from system evidence and record the impact start timestamp. Every clock, every credit calculation, and the outage letter all run from that moment.
2. Publish one holding position naming what is affected, what is not, and when the next update comes, before the cause is known.
3. Point every reply and every channel at that published position rather than restating it in their own words.
4. Update on the committed cadence whether or not there is progress.
5. Confirm recovery from system evidence and from at least one affected customer before declaring resolution.
6. Close the customer-facing incident only once the follow-up owed to each affected account is recorded: the outage letter where one was committed, the credit where the contract triggers one, and the tickets raised during the event that are still individually unresolved.

The order is mandated because steps 2 and 4 do not wait for certainty. An outage with no published position produces a queue of agents each explaining it differently, in writing, within the same hour, and those replies get compared with each other in public. Step 6 exists because the tickets an incident generated outlive the incident record that would otherwise close them.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with collection timestamps, its labeled assumptions, the coverage statement for anything it measured, and every clock it started, inherited, or paused. Section headings with the contents deferred mean the stage did not run. Later stages trust the packet rather than re-reading the systems, so an optimistic completion marker propagates from a triage decision into a severity, from there into an SLA position, and from there into a breach nobody saw coming.

## Parallel surface

Independent items fan out and are parallel-safe: tickets in a queue, evidence items within a ticket, versions and editions in a reproduction matrix, defects in a backlog, articles in a review batch, macros in an audit, queues in a health review, agents and tickets in a QA sample, contact drivers being coded, intervals in a volume forecast, accounts being identified as affected by an incident, and survey verbatims being themed.

Aggregation is a single pass after the fan-out returns. The backlog age distribution and its burn-down math, contact rate per active account, satisfaction and first contact resolution over a period, the containment rate and its denominator, the ranked driver list, calibration variance across reviewers, and forecast accuracy are each statements about a whole set. The staffing model is a single pass for a stronger reason: shrinkage, occupancy, and adherence are cross-interval effects, so a day's coverage cannot be assembled from independently staffed intervals. During an incident the scope determination and the single published position are single passes by design, because the whole point of them is that only one exists. Within one ticket, the reply itself is a single pass, because it has to be internally consistent in front of the person reading it.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what the customer, the queue, or the company is exposed to if the workflow continues anyway>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact fact, or both readings where sources disagree>
Sources attempted: <what was queried and what it returned>
Running clock: <every SLA target, promised update, and incident commitment still running, with its start timestamp and its due time; none, where none applies>
Scope affected: <the tickets or accounts the blocked decision sits on, with how that scope was determined, or not applicable>
Required approval or access: <named approver role and authority level, or the system and scope needed>
Proceeding meanwhile: <reversible internal work that does not depend on the blocked fact>
Preserved packet: <full support_packet>
Resume prompt: <prompt that restarts the workflow once the fact or approval arrives>
```

A halt never pauses an SLA clock or a promised update. Where a clock is running, the halt says so on its own line, states the due time, and names who has to send the holding reply now rather than when the blocking fact arrives.

A halt justified by not knowing something is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the ticket, severity, cause, driver, or metric it affects.

## Stage contracts

`references/stage-contracts.md` gives each desk its required inputs, the outputs it owns, its handoff target, and the hard halt specific to that stage.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
