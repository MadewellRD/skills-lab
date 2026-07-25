# Marketing Growth Suite Workflow Contract

## Purpose

This reference defines how the Marketing Growth Command Desk suite runs as one continuous program of work instead of a set of isolated prompts. Every desk in the suite reads it, updates the `growth_packet`, and hands that packet to the next stage.

The subject of this suite is the distance between what the market is told and what the company can prove: who the buyer is, what is claimed to them, where that claim is repeated, what it costs to put it in front of them, whether it moved anyone, and how much revenue the movement is entitled to be credited with.

The packet therefore carries claim state and measurement state side by side, because the two things this domain fabricates most easily are a claim nobody substantiated and a pipeline figure nobody can tie back to a record. Both read as confident on the page, and both are repeated downstream by people who were not in the room when they were written.

## Continuity rule

Do not stop with a bare next-desk recommendation when the next stage can be completed from available facts. Complete the current stage, update the `growth_packet`, and continue until the target outcome is reached or a hard halt applies. A run that ends at "you should now build a nurture sequence" or "consider testing the landing page" hands the sequencing problem back to the person who asked for the campaign.

A stage is complete when the next desk can act on its output without rediscovering the segment definition, the approved claim, the offer, the measurement basis, or the owner. A stage that emitted headings and deferred their contents is incomplete, because every later stage trusts the packet rather than re-reading the ad account.

## Operating modes

- `single_stage`: run one desk because the user asked for one specific marketing artifact, such as a positioning statement, a battlecard, a nurture sequence, or a channel read.
- `workflow_run`: default. Run the stage path the target outcome needs, carrying the packet through each stage.
- `resume`: continue from a prior `growth_packet` or a halt-resume prompt, treating `completed_stages` as done rather than redoing them. Re-read any spend figure, conversion rate, ranking position, deliverability metric, pipeline number, or competitor claim whose collection date is stale, because auctions reprice daily, rankings move weekly, opportunities change stage continuously, and a competitor rewrote their pricing page since the battlecard was last opened.
- `halt`: stop on a hard-halt class from `references/halt-taxonomy.md` and emit the halt format below.
- `diagnostic`: the web analytics property, ad accounts, marketing automation platform, CRM, search console, CMS, or event and community platforms cannot be reached, so the run reports reachability and evidence gaps instead of asserting traffic, spend, conversion, deliverability, ranking, or pipeline state.

## Action boundary

This suite researches, positions, writes, briefs, designs programs, and measures. It does not send a message to a live list, publish a page or a press release, post to an owned brand channel, activate or pause a paid campaign, change a bid or a budget in an ad account, alter a live pricing page, redirect or delete a URL, submit a marketplace listing, distribute a customer reference, or brief an analyst on the record. For those, the desk prepares the exact asset, the audience and reach it would touch, the approvals it requires, the measurement that will read it, and the correction path, then stops at the gate. The person holding the authority executes.

The correction path deserves its own sentence, because in this domain most of these actions have no rollback. A published page can be edited and a campaign can be paused, but a message that reached an inbox, an announcement that reached a journalist, and a price that reached a customer's screen are corrected only by a second message to the same audience, which costs more attention than the delay of getting the first one approved.

## Growth packet

Every desk preserves and updates this packet. Unmeasured, unsubstantiated, unapproved, and unknown are legitimate values; a plausible conversion rate and an invented customer count are not. A field with no source basis stays empty rather than being filled with something that fits the pattern.

```yaml
growth_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  current_stage: "stage-name"
  completed_stages:
    - "stage-name"
  skipped_stages:
    - stage: "stage-name"
      reason: "why it was not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  marketing_surface: "audience_segmentation | positioning | competitive | brand_creative | launch | pricing_communication | sales_enablement | demand_generation | content | organic_search | paid_acquisition | lifecycle_email | conversion_optimization | experimentation | partner_channel | community_advocacy | events_field | measurement | budget_pipeline | unknown"
  motion: "product_led | sales_led | channel_led | community_led | hybrid | unknown"
  operating_posture: "pre_launch | launch_window | steady_state | campaign_in_flight | quarter_close | budget_reset | rebrand_in_flight | site_or_domain_migration | pipeline_shortfall | brand_or_press_incident | audit_or_review | freeze | unknown"
  exposure: "internal_only | named_customer_list | opted_in_prospect_list | purchased_or_rented_list | paid_audience | public_web | in_product_surface | press_and_analyst | partner_distributed | regulated_market | unknown"

  segments:
    - name: ""
      definition: "the observable attributes that place an account or person in it, not the adjective"
      firmographics: "industry, size, and geography with the field they are read from, or unqualified"
      technographics: "the stack or usage signals that qualify it, or none"
      buying_committee:
        - role: ""
          cares_about: "the outcome this role is measured on"
          disqualifier: "what makes this role say no, where evidence establishes it"
      trigger: "the event that makes this segment in-market, or none identified"
      size_basis: "the count with the list, query, or market source it came from, or unsized"
      tier: "tier1 | tier2 | tier3 | untiered"
      observed_performance: "measured win rate, conversion, or retention with its source, or unmeasured"

  positioning:
    category_frame: "the category the buyer already shops in, or the frame being proposed with what it costs to teach"
    for_whom: "the segment this position is written against"
    competitive_alternative: "what the buyer does instead today, including doing nothing"
    differentiators:
      - claim: ""
        proof: "the capability, benchmark, audit, or customer result that substantiates it"
        proof_state: "substantiated | asserted | contested | unsubstantiated"
        durability: "how long this stays true if a competitor copies it"
    message_house:
      pillars: []
      supporting_points: []
      proof_points: []
    anti_positioning: "what the company deliberately does not claim, and who it is deliberately not for"
    approver: "named approver, or unapproved"
    last_reviewed: "date, or unknown"

  claims:
    - claim: "the sentence as it would appear externally"
      claim_type: "superiority | quantified_outcome | customer_count | performance | security_or_compliance | availability | pricing | regulated_category"
      substantiation: "the study, benchmark, report, contract, or query that supports it, with its date"
      substantiation_state: "substantiated | stale | contested | none"
      required_approver: "the function the claim commits, such as legal, security, finance, or clinical"
      approval_state: "granted | pending | not_sought"
      surfaces: []                     # every asset, page, deck, and channel the claim currently appears on

  brand:
    voice: "the stated voice attributes with the source that defines them, or undefined"
    visual_system: "logo, lockup, palette, and type rules with their source, or undefined"
    restricted_usage: "trademark, co-branding, and partner logo rules, or none stated"
    required_disclaimers: []
    review_path: "who reviews creative before it goes live, or none"
    localization: "markets in scope and what is translated versus transcreated, or single market"
    consistency_state: "the surfaces audited against the standard and the drift found, or unaudited"

  competitors:
    - name: ""
      alternative_type: "direct | adjacent | incumbent_process | in_house_build | do_nothing"
      where_we_win: "the evidenced pattern with its source, usually win_loss or deal review"
      where_we_lose: "the evidenced pattern with its source"
      their_public_claim: "quoted from their material, with the date the material was read"
      our_response: "the counter and the proof behind it"
      pricing_posture: "what their public pricing shows, with the date, or opaque"
      battlecard_state: "current | stale | none"
      last_verified: "the date their material was actually read, or never"

  launches:
    - name: ""
      tier: "tier1 | tier2 | tier3, with the rule that set the tier"
      release_state: "alpha | beta | limited_availability | general_availability | unknown"
      ga_date: "date from a product source, or unconfirmed"
      narrative: "the one sentence reason the market should care"
      destinations: "pricing page, docs, in-product surface, signup path, and support readiness, each with its state"
      embargo: "the lift time and who is briefed under it, or none"
      audiences: []                    # each with its channel, owner, and send or publish time
      readiness_gaps: []

  pricing_communication:
    change_type: "new_pricing | price_increase | repackaging | plan_retirement | discount_policy | none"
    effective_date: "date from an approved source, or unset"
    notice_window: "the contractual or policy notice period with the source that sets it"
    affected_cohorts: []               # each with contract terms that constrain the schedule
    grandfathering: "who keeps existing terms and for how long, or none"
    migration_path: "what an affected customer has to do, or none"
    internal_readiness: "support, success, and sales briefed, or not yet"
    approver: "named approver for the external wording, or unapproved"

  enablement_assets:
    - asset: ""
      audience: "the selling or partner role that uses it"
      moment_used: "the conversation or deal stage it belongs in"
      claims_used: []                  # references into the claims list so a retraction is traceable
      owner: "named owner, or unowned"
      last_updated: "date, or unknown"
      adoption: "measured usage with its source, or unmeasured"

  campaigns:
    - name: ""
      objective: "awareness | demand_creation | demand_capture | expansion | retention | reactivation"
      segments: []
      offer: "what the audience is actually asked to do and what they get for it"
      channels: []
      budget: "committed spend with the source that approved it, or unbudgeted"
      target: "the response, pipeline, or revenue number with the basis it was set from"
      measured_result: "with the report and date it came from, or unmeasured"
      lead_handling: "scoring, routing, and the follow-up commitment sales actually agreed to, or undefined"
      state: "planned | in_market | paused | complete"

  content_assets:
    - asset: ""
      pillar: "the topic pillar or cluster it belongs to"
      reader_question: "the question the reader is actually asking at this moment"
      gated: "yes | no"
      target_query: "the query or topic it is written against, or none"
      subject_matter_source: "the expert, customer, or dataset the substance came from, or none"
      owner: ""
      published: "date, or unpublished"
      performance: "measured traffic, engagement, or conversion with its source, or unmeasured"
      decay_state: "growing | flat | declining | never_measured"
      refresh_trigger: "the date or condition that puts it back in the queue, or none set"

  organic_search:
    property_access: "the search console, crawl, or rank source available, or none"
    query_set: "queries with measured impressions, clicks, and position, and the date range they cover"
    index_state: "indexed, excluded, and blocked counts with their source, or unmeasured"
    canonical_and_duplication: "the canonical rules in force and the duplication actually observed"
    cannibalization: "queries where several pages compete, with the evidence"
    internal_linking: "the hub and cluster structure that exists, or unmapped"
    authority_signals: "referring domains with the source they were counted from, or unmeasured"
    serp_composition: "what occupies the result for the target queries, including answer surfaces that resolve the query without a click"
    migration_state: "none | inventory_captured | redirect_map_drafted | cutover_pending | cutover_done | recovering"

  paid_channels:
    - channel: ""
      objective: ""
      buying_model: "cpc | cpm | cpa_target | roas_target | reserved | unknown"
      budget: "committed and spent to date, with the account it was read from"
      audience: "the targeting definition, including any customer list uploaded and the consent basis for uploading it"
      creative_set: "the variants live, how long each has run, and the frequency against the audience"
      measured_cost_per: "actual cost per click, lead, opportunity, or acquisition with its source, or unmeasured"
      platform_reported_conversions: "as the platform counts them, with the attribution window and model the platform applies"
      matched_conversions: "the same outcomes matched to records in the system of record, or unmatched"
      brand_safety: "placement, exclusion, and adjacency controls in force, or unmanaged"
      incrementality_evidence: "holdout or geo test result with its date, or none"

  lifecycle_programs:
    - program: ""
      trigger: "the behavior, lifecycle stage, or date that enrolls someone"
      audience_source: "the list or segment query, and where those records originally came from"
      consent_basis: "opt_in | contractual | legitimate_interest | none_recorded, with the jurisdictions in scope"
      suppression: "unsubscribe, do-not-contact, active-deal, open-escalation, and recent-send suppressions applied, or none"
      cadence: "message count, spacing, and the global frequency cap across programs, or uncapped"
      sending_identity: "the domain and subdomain used and its authentication state"
      deliverability: "measured delivery, bounce, and complaint rates with their source, or unmeasured"
      exit_criteria: "what removes someone from the program, or none"

  funnel:
    definition_owner: "who owns the stage definitions this funnel uses, or undefined"
    steps:
      - step: ""
        volume: "measured count with its source, or unmeasured"
        conversion_to_next: "measured rate with the denominator it was computed over, or unmeasured"
        measurement_source: "web_analytics | marketing_automation | crm | ad_platform | mixed"
        observed_leakage: "the drop-off and the evidence pointing at its cause, or undiagnosed"

  experiments:
    - hypothesis: "the change, the expected direction, and the mechanism"
      unit: "visitor | session | account | recipient | geography | channel"
      primary_metric: "one metric, defined with its denominator"
      guardrail_metrics: []
      baseline: "measured baseline rate with the period it came from, or unmeasured"
      mde: "the smallest effect this test can detect, and the traffic and duration that buys it"
      allocation: "the split, and any holdout deliberately held back"
      duration: "planned run length including whole business cycles"
      state: "designed | running | read | shipped | reverted | abandoned"
      result: "measured effect with its interval and the sample it was read on, or unread"
      decision: "ship | revert | iterate | inconclusive, with who decided"

  partners:
    - partner: ""
      motion: "co_marketing | co_sell | reseller | referral | marketplace_listing | integration_only"
      tier: "the tier and the source that assigns it"
      agreement_terms: "logo rights, claim rights, and lead-sharing terms in force, or none confirmed"
      mdf: "committed funds, the claim process, and spend to date, or none"
      lead_flow: "how leads are shared, registered, and credited, or undefined"
      joint_assets: []
      measured_contribution: "sourced or influenced pipeline with its source, or unmeasured"

  community_and_advocacy:
    programs: []
    forums: "the owned and unowned places customers already talk, each with moderation ownership"
    advocates:
      - customer: "named only where a permission record exists"
        permission_state: "written_approval | verbal_only | none"
        usable_for: "logo | quote | case_study | reference_call | analyst_reference | press"
        expiry: "the date the permission lapses, or none stated"
        usage_history: "how often and how recently this reference has been used, or untracked"
    reviews: "volume, rating, and recency with the site they were read from, or unmeasured"
    escalation_path: "who responds to a negative public thread and at what threshold, or none"

  events:
    - event: ""
      type: "trade_show | owned_conference | field_dinner | roadshow | webinar | sponsorship | community_meetup"
      cost: "committed cost including sponsorship, build, travel, and staff time, with what is excluded"
      target_audience: "the segment and the accounts actually expected to attend"
      capture_mechanism: "badge scan, form, meeting booking, or none"
      capture_consent: "what the attendee actually agreed to at the moment of capture"
      follow_up: "the owner, the sequence, and the timing commitment"
      measured_result: "meetings, opportunities, and pipeline with the date the record was read, and the lag still outstanding"

  measurement:
    tracking_plan: "the events, parameters, and naming rules actually enforced, or ad hoc"
    link_parameter_governance: "who sets campaign parameters and what enforces the convention, or unenforced"
    identity_resolution: "how an anonymous visitor becomes a known record, and where the join breaks"
    consent_and_blocking: "consent state, blocked traffic, and the share of sessions that cannot be measured, or unquantified"
    attribution_models_in_use: []      # each with where it is computed and who reads it as truth
    known_double_count: "where the same outcome is claimed by more than one channel report"
    incrementality_evidence: "holdout, geo, or media mix results with their dates, or none"
    self_reported_attribution: "the question asked and its response rate, or not collected"
    reconciliation: "platform-reported outcomes compared against the system of record, with the variance, or not reconciled"

  budget:
    period: ""
    total: "approved budget with the source that approved it, or unapproved"
    allocation: []                     # program, committed, and spent to date, each with its source
    working_versus_nonworking: "measured split, or unmeasured"
    pacing: "spend to date against plan, with the date it was read"
    commitments: "contracted spend that cannot be reallocated within the period"
    reallocation_authority: "who can move money between programs and above what threshold"

  pipeline_contribution:
    sourced_definition: "the definition in force and who owns it"
    influenced_definition: "the definition in force and who owns it"
    agreed_with_sales: "yes | no | disputed"
    coverage_ratio: "pipeline against target with the report and date it came from, or unmeasured"
    sourced_pipeline: "value with the report and date, or unmeasured"
    influenced_pipeline: "value with the report and date, or unmeasured"
    stage_conversion: "measured conversion by stage with its source, or unmeasured"
    acquisition_cost: "measured cost of acquisition, stating what is inside the numerator"
    payback: "measured payback period with its source, or unmeasured"
    lag: "typical time from first touch to closed won, and how much of the current period is still unresolved"

  compliance_constraints:
    jurisdictions: []
    messaging_rules: "the consent, identification, and unsubscribe rules that bind the sending programs, with their source"
    list_provenance: "how each mailable list was built; a list with no provenance is treated as unmailable"
    claim_review_rules: "which claims require review and by whom, with the source that requires it"
    regulated_categories: "products, markets, or audiences carrying additional restrictions, or none"
    personal_data_handling: "what the programs collect, where it flows, and what the retention commitment is"

  approvals:
    - action: "the action requiring authorization"
      approver: "named human, or unknown"
      authority: "what the policy requires for this action"
      state: "granted | pending | denied"

  source_facts:
    - fact: "source-backed fact"
      source: "web_analytics | ad_platform | marketing_automation | crm | cms_or_live_site | search_console | seo_crawl | keyword_tool | email_platform | event_platform | community_platform | review_site | partner_portal | billing_or_finance | bi_dashboard | brand_guidelines | approved_messaging_doc | campaign_brief | win_loss_record | customer_interview | competitor_public_material | press_or_analyst_coverage | legal_review | contract | user | connector | uploaded_file | unknown"
      collected: "when the source was actually read"
  decisions:
    - "decision made at this stage"
  assumptions:
    - "assumption made to continue, labeled where it was used"
  open_questions:
    - "question blocking later work"
  artifacts:
    - "artifact name or path"
  halt_conditions:
    - "condition that requires stopping"
  ready_to_continue: true
```

## Stage advancement

Advance when the current desk's output would survive being handed to the next desk without a follow-up round trip. `references/stage-contracts.md` states what each desk requires on input and owns on output.

Run only the stages the target outcome needs. A deliverability problem does not need a positioning stage; a battlecard refresh does not need a budget stage. Record every skip in `skipped_stages` with its reason, so a later reader can tell a deliberate skip from an omission.

Two dependencies in this chain are load-bearing rather than conventional. Nothing downstream of positioning is safe to produce until the differentiators carry their proof, because an unsubstantiated claim does not stay in the document that created it: it propagates into the launch narrative, the ad copy, the sales deck, and the partner listing, and the retraction reaches a fraction of the surfaces the claim reached. And nothing in the paid, lifecycle, experimentation, attribution, or pipeline stages means anything until the tracking plan and the funnel stage definitions exist, because every number those stages produce is a ratio whose denominator is a definition somebody chose.

## Source discipline

Read what actually happened and what was intended to happen from different places, and keep them labeled as such.

What actually happened: web analytics states sessions and on-site behavior for the traffic it can see. Ad platforms state spend, delivery, and the conversions they are willing to claim, each under their own attribution window. The marketing automation platform states what was sent, to whom, what bounced, and what consent record exists. The CRM states which records became opportunities and what they are worth. Search console states impressions, clicks, and position for queries the property actually appeared on. A crawl states what a search engine can reach. The live site states what a visitor actually reads right now, which is frequently not what the messaging document says. The billing or finance system states revenue. Review sites and press coverage state what third parties have published.

What was intended: campaign briefs, messaging documents, positioning frameworks, brand guidelines, editorial calendars, media plans, launch plans, and enablement material state what was supposed to be said, spent, and shipped. Interviews, win and loss records, and customer conversations are evidence about buyers rather than about performance.

The gap between the two is usually the finding. A message house nobody uses, a persona document no campaign targets, an editorial calendar three months behind the last publish, a battlecard citing a competitor capability that shipped eighteen months ago, a superiority claim whose supporting study was retired, a nurture program running against a list with no consent record, and a channel report claiming pipeline that the CRM also credits to two other channels are the recurring shape of this domain. Record both sides, attribute both, and preserve the conflict rather than resolving it into whichever source is easier to reach.

One conflict class is structural rather than accidental and should never be silently averaged. Every ad platform is measuring its own contribution using its own window and its own view of the user, so the platforms in aggregate will claim more conversions than the system of record contains. Record each platform figure with the window that produced it and record the system-of-record total separately. The difference is a finding about measurement, not an error to be reconciled by scaling everything down until the total fits.

Keep source facts separate from assumptions and from inference in every artifact. Never invent conversion rates, traffic figures, spend, cost per acquisition, ranking positions, deliverability rates, list sizes, customer counts, win rates, competitor pricing, review scores, event attendance, pipeline values, or the name of anyone who approved anything.

## Halt behavior

The default posture is to proceed with the assumption labeled inline where it was used. Hard halts are justified by consequence, never by uncertainty, and belong to the six classes in `references/halt-taxonomy.md`. Evidence that is merely absent is a soft gap; evidence that exists and cannot be read is a hard halt.

### Ordered sequence for irreversible external release

Sending to a live list, publishing to a public surface, announcing under embargo, activating paid spend, and pushing an asset into partner distribution run in this order:

1. Establish that the audience is contactable and the words are cleared: consent basis and list provenance per recipient segment, every suppression applied, and every claim in the asset carrying its substantiation and its named approver.
2. Confirm every destination the asset points at exists and is live in the state the asset describes: the pricing page, the documentation, the in-product surface, the signup path, the offer itself, and the tracking on each.
3. Release to a bounded slice first and read it: a seed list and a small percentage for a send, a capped budget or a single geography for paid, a staged publish for a page, and confirm rendering, links, merge fields, and tracking before the full audience sees it.
4. Release to the full audience, then hold the correction path open with the named person who can pause the send or the campaign, the person who publishes a correction, and the audience the correction has to reach.

This order is mandated because there is no unsend. Step 1 comes first because a message delivered to a list with no consent basis leaves a permanent record of the violation in the recipient's own inbox, and because a claim retracted after distribution has to be chased across every surface it was copied onto. Step 2 comes before any release because the most common launch failure in this domain is an announcement that points at a page which is not live yet, and the traffic arrives within minutes of the send. Step 3 is the only cheap place to find a broken link, a wrong merge field, a truncated subject line, or a destination with no tracking on it; the alternative is finding it in front of the entire list. Do not compress these steps to make a launch date, and do not reorder them if a later edit makes the list look redundant.

### Ordered sequence for URL, domain, or tracking cutover

Site migrations, domain changes, rebrands that move URLs, CMS replacements, and analytics re-implementations run in this order:

1. Capture the current state before anything moves: the URL inventory with measured traffic, query positions, and referring domains per page, and the current tracking implementation with the events it actually fires.
2. Build the redirect map at the individual URL level for every page carrying measured traffic, position, or inbound links, and record an explicit decision for every page being retired rather than redirected.
3. Preserve measurement continuity across the boundary: the property, the filters, the goal and conversion definitions, and the parameter conventions that make before and after comparable at all.
4. Cut over, then re-crawl and compare against the captured inventory rather than against expectation, and monitor index coverage and query-level position for the full period recovery actually takes rather than for the first week.

The order is mandated because step 1 is unrepeatable. Once the old URLs stop resolving, the list of which ones carried value cannot be reconstructed, the referring domains point at pages that no longer answer, and a redirect map built after cutover is a guess about traffic that has already gone. Step 3 is placed before cutover because a measurement break makes the recovery unreadable; without it, nobody can distinguish a migration that lost rankings from one that only lost tracking.

### Ordered sequence for pricing or packaging change communication

1. Establish the contractual notice period per affected cohort and what each agreement actually permits, because the shortest notice period in the set governs the whole schedule.
2. Brief support, customer success, sales, and any partner who resells, with the change, the objection set, and the escalation path, before a customer can ask them about it.
3. Notify affected existing customers directly, with the effective date, what changes for them specifically, and the migration or grandfathering path.
4. Update the public pricing surface, the sales materials, and the partner materials inside one window, so a customer and a prospect never read two different numbers.

The order is mandated because a schedule that violates the shortest contractual notice period is a breach that no quality of wording repairs, a customer who learns about their own price change from a public page, a partner, or a competitor churns over the surprise rather than over the amount, and a support representative who first hears about it from an inbound ticket gives an answer that contradicts the notice.

### Halt format

```markdown
## Workflow Halt

Halt class: <one of the six hard classes>
Current stage: <stage>
Completed stages: <list>
Blocked next stage: <stage>
Consequence if we proceeded: <what would be sent, published, spent, promised, exposed, or asserted without basis>
Audience at risk: <who would receive or read it, and how many, where the reach is known>
Missing fact, approval, or access: <the exact substantiation, consent record, approver, budget authority, or connector>
Already attempted: <the platforms queried, the documents read, and what each returned>
Proceeding meanwhile: <reversible work that does not depend on the blocked item, including drafts held unpublished>
Required to resume:
- <the specific approval, record, or access, with the owner who can supply it>
Resume prompt:
<copy-paste prompt carrying the current growth_packet>
```

A halt that only reports being stuck is incomplete. Name the exact study, consent record, contract clause, budget authority, platform, or approver that unblocks it.

## Parallel surface

Segments, roles within a buying committee, competitors, channels, campaigns, content assets, query clusters, landing pages, ad creatives, lifecycle programs, partner accounts, events, enablement assets, review sites, and localized markets are independent units and are parallel-safe. Connector preflight across web analytics, ad accounts, marketing automation, CRM, search console, CMS, event platforms, and community platforms is likewise parallel-safe.

The aggregate work is not parallel and runs once, after the fan-out returns: reconciling one claim across every surface it appears on, deduplicating pipeline credit so the channel reports do not sum past what the system of record holds, composing the channel mix and the budget allocation, which is a single constrained decision over a fixed total, ranking the experiment queue against shared traffic, setting the global frequency cap across programs that each look reasonable in isolation, and sequencing the launch run of show, where the ordering between the announcement and its destinations is itself the artifact. A per-channel picture assembled in parallel and never composed is how this domain produces four dashboards that each show the plan being met while the pipeline number is short.

Two carve-outs are structural rather than stylistic. Experiments that share a surface or an audience are not parallel-safe however independent their hypotheses look, because a second test on the same page or the same recipient contaminates the read of the first and neither result survives. And a rebrand rollout does not parallelize across surfaces: the logo, the site, the ad creative, the partner materials, and the sales deck change on one date or the market sees two identities at once and reads the older one as the current one.

## Cross-suite handoffs

Label cross-suite work explicitly rather than implying those desks belong to this suite. Send product strategy, roadmap, requirements, feature prioritization, and the decision of what the price actually is to the Product suite; this suite owns how price and packaging are explained to the market, never what they are set at. Send individual deal execution, rep-owned outbound, forecasting, and proposals to the Sales suite; this suite owns the collateral and the claims inside it, and the rep runs the deal. Send adoption programs, health scoring, renewal plays, and the customer relationship to the Customer Success suite; this suite owns the advocacy asset that relationship makes possible. Send site implementation, page performance, CMS build, and the engineering of tracking instrumentation to the Web Development suite; this suite owns the intent, the requirements, and the measurement plan that instrumentation serves. Send warehouse modeling, the marketing data model, and metric semantics to the Data suite. Send lawful basis, consent architecture, cross-border transfer, and subject requests to the Privacy suite; this suite carries the operational consequence in its sending and targeting programs. Send trademark, partner agreements, and formal legal review of a claim to the Legal suite. Send budget approval, purchase orders, and revenue recognition to the Finance suite. Send employer brand and recruitment marketing to the People suite.

A brand or press incident belongs to this suite and to the Legal or Security suite at the same time, and the handoff is additive rather than a transfer of command.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model, including context budget, native self-verification, long-horizon continuation, and parallel fan-out, along with the governance invariants that do not relax as models improve.
