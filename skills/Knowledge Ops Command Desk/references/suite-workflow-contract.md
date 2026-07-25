# Knowledge Ops Suite Workflow Contract

## Purpose

This reference defines how the Knowledge Ops Command Desk suite runs as one continuous program of work rather than as a set of isolated prompts. Every desk in the suite reads it, updates the `knowledge_packet`, and hands that packet to the next stage.

The subject of this suite is the path a question takes from the person who has it to the answer they can act on: who needs to know something and to do what, what the organization has already written down, what it is called and where it sits, who has the knowledge that was never written, what shape a good answer takes, which of the four contradictory pages is canonical, whether the procedure still matches the system it operates, who is allowed to read it, what a retriever is permitted to serve from it, what it says in the other seven languages, who owns keeping it true, and when it should stop existing.

The packet carries lifecycle state and provenance side by side, because the two things this domain fabricates most easily are a page that does not exist and a review that never happened. Both are invisible in the artifact and both become load-bearing the moment somebody cites them.

## Continuity rule

A desk that has the facts to run the next stage runs it. A run that ends at "you should now audit the wiki" or "consider defining a taxonomy" is a routing note, not knowledge work; it hands the sequencing problem back to the person who asked for the answer. Complete the current stage, update `knowledge_packet`, and continue until the requested outcome exists or a hard halt applies.

A stage is complete when the next desk can act on its output without rediscovering the audience, the canonical term, the owner, the locator, or the evidence behind a figure. A stage that emitted headings and deferred their contents is incomplete, because every later stage trusts the packet rather than re-crawling the corpus.

Three things are never continued through: an action that changes what a reader sees on a published surface, a statement about coverage or freshness that no source establishes, and a resolution of two contradictory published answers into one without the person who owns the subject matter. Everything else continues, with the assumption labeled inline against the artifact, term, or audience it affects.

## Action boundary

This suite audits, classifies, structures, drafts, reconciles, measures, and plans. It does not publish to a live surface, edit a page in place, merge or delete an artifact, change a URL, apply a bulk re-tag, re-index search or a retrieval corpus, grant or widen read access, push a translation to a locale, or archive content anybody still reaches. For those the desk prepares the exact change, the inbound references it breaks, the audience it reaches, and the reversal, then stops at the gate. The person with publishing authority publishes.

Editing a published page in place is outside the boundary in every mode, not because the edit is wrong but because it destroys the record of what readers were previously told. A correction that leaves no trace of the incorrect version denies every person who already acted on it the ability to work out that they did.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a taxonomy, a content audit, a runbook review, a search relevance analysis, or a retirement plan.
- `workflow_run`: the default for anything phrased as a knowledge base build, a migration, a cleanup, a documentation program, a search or retrieval quality push, a localization effort, or an onboarding refresh. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `knowledge_packet` or a halt-resume prompt, treating `completed_stages` as done. Re-read any page inventory, search log window, usage figure, review date, or translation state whose collection date is stale, because a corpus changes between readings while the packet does not, and the specific way it changes is that somebody edits a page without telling anyone.
- `halt`: a hard halt class applies. Return the halt format below with the packet intact and the reversible work already done.
- `diagnostic`: the wiki or content platform, the documentation repository, search analytics, the ticket system, the link checker, the retrieval index, the learning system, or the translation platform cannot be reached. Report what was reachable, what was not, and precisely which coverage, freshness, usage, or contradiction claims each gap makes unavailable. Do not backfill an unreachable corpus with the pages it probably contains.

## Request types

Every request carries exactly one type, because the type sets the audience, the approval surface, and the evidence standard: `knowledge_gap`, `corpus_audit`, `taxonomy_build`, `findability_fix`, `standards_definition`, `platform_migration`, `expert_capture`, `decision_capture`, `runbook_review`, `enablement_build`, `consolidation`, `freshness_sweep`, `access_review`, `search_quality`, `retrieval_readiness`, `localization_cycle`, `governance_model`, `measurement`, `retirement`, `unknown`.

The distinction that matters most is whether the output reaches a reader who cannot see how it was made. An internal gap ledger tolerates working assumptions labeled as such. A published procedure, a customer-facing article, an onboarding path, and a corpus admitted to assistant retrieval do not, because each is consumed as an instruction by somebody with no way to check it and no reason to doubt it.

## The knowledge packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `unowned`, `unmeasured`, `never_reviewed`, and `not_crawled` are legitimate values; an invented page title, locator, owner, or review date is not.

```yaml
knowledge_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  request_type: "knowledge_gap | corpus_audit | taxonomy_build | findability_fix | standards_definition | platform_migration | expert_capture | decision_capture | runbook_review | enablement_build | consolidation | freshness_sweep | access_review | search_quality | retrieval_readiness | localization_cycle | governance_model | measurement | retirement | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  knowledge_surface: "demand | inventory | taxonomy | navigation | authoring_standards | platform | expert_capture | decision_record | runbook | enablement | duplication | freshness | access | search | retrieval_corpus | localization | governance | measurement | archival | unknown"
  operating_posture: "greenfield | steady_state | platform_migration_in_flight | reorganization | product_launch | post_incident_capture | wrong_answer_in_circulation | content_freeze | audit_or_review | unknown"
  audience_reach: "single_team | function | whole_org | contractor_or_partner | customer_facing | public | assistant_retrieval | regulated_publication | unknown"

  audiences:
    - name: "the group, named as the organization names it"
      tasks: []                       # what they are trying to do, not what they are interested in
      entry_tool: "where they look first, from evidence rather than from design intent"
      entitlement: "what this audience is permitted to read"
      languages: []
      ramp_state: "new_hire | experienced | external | mixed | unknown"

  demand_signals:
    - question: "the question as the asker phrases it, not as the taxonomy phrases it"
      evidence: "search_log | zero_result_query | ticket_driver | chat_thread | onboarding_survey | interview | support_macro_usage | retrieval_query_log | unknown"
      volume: "measured count with the query and window it came from, or unmeasured"
      answer_state: "answered | partial | contradicted | scattered | unanswered | unknown"
      cost_of_no_answer: "who is blocked, how often, and what they do instead"

  corpora:
    - name: ""
      system: "wiki | docs_site | repository | ticket_knowledge_base | shared_drive | learning_system | intranet | chat_channel | spreadsheet | unknown"
      steward: "named steward, or unowned"
      artifact_count: "measured count with the export or API call it came from, or uncounted"
      crawl_state: "crawled | partially_crawled | not_crawled"
      search_indexed: "yes | no | partially | unknown"
      retrieval_indexed: "yes | no | unknown"
      export_path: "how content leaves this system, or none"
      migration_state: "not_applicable | planned | in_flight | cut_over | frozen"

  knowledge_artifacts:
    - id: ""
      title: "title as it actually appears"
      locator: "the URL, path, or article identifier a reader can open"
      information_type: "concept | task | reference | policy | runbook | decision_record | faq | glossary_entry | training_module | template | announcement | unclassified"
      corpus: ""
      owner: "named owner, or unowned"
      author_of_record: "who last substantively changed it, or unknown"
      last_substantive_edit: "date from the system history, or unknown"
      last_reviewed: "date a review was recorded, or never_reviewed"
      review_due: "date, or unset"
      lifecycle_state: "draft | in_review | published | stale | contested | superseded | archived | orphaned"
      canonical: "yes | no | contested | undetermined"
      sensitivity: "public | customer | partner | internal | need_to_know | restricted | unclassified"
      locales: []                     # each with its own translation state
      usage: "measured views, search entries, or citations with the source and window, or unmeasured"
      inbound_links: "measured count and where they come from, or untraced"
      verification_state: "verified_against_system | verified_by_sme | unverified"

  taxonomy:
    scheme: "the classification in force, or none"
    facets: []                        # each with its permitted values and who may add one
    controlled_terms:
      - term: "preferred label"
        definition: "what it means here, which is often not what it means elsewhere"
        variants: []                  # synonyms, abbreviations, and legacy names that must resolve to this term
        owner: "named term owner, or unowned"
        used_in: []                   # search synonyms, navigation facets, retrieval metadata, termbase, product UI
    term_conflicts:
      - conflict: "one label with two meanings, or two labels with one meaning"
        readings: []                  # each with the source that uses it
        adjudicated_by: "named person, or open"
    tagging_coverage: "share of artifacts carrying required metadata, with the denominator, or unmeasured"

  navigation:
    entry_points: []                  # where readers actually arrive, from analytics rather than from the sitemap
    structure: "the hierarchy or graph in force, or undefined"
    orphan_pages: "artifacts no navigation path reaches, with how the set was derived, or untraced"
    depth_to_answer: "measured clicks or queries to a common answer, or unmeasured"
    wayfinding_evidence: "card_sort | tree_test | analytics | observation | none"

  standards:
    style_guide: "locator of the guide in force, or none"
    information_types: []             # the typed templates authors are expected to use
    templates: []                     # each with what it is for and whether it is enforced anywhere
    terminology_rules: "how the controlled vocabulary binds prose, or unenforced"
    accessibility_rules: "structure, alt text, heading order, and plain-language requirements, or unstated"
    conformance: "measured share of artifacts meeting the standard, with how it was measured, or unmeasured"

  platforms:
    - system: ""
      role: "authoring | publishing | search | learning | translation | ticket_knowledge_base | retrieval_source"
      source_of_truth_for: "what this system is authoritative for, or nothing declared"
      single_sourcing: "what content is reused rather than copied, and by what mechanism, or none"
      publishing_pipeline: "how a change reaches a reader, including any review gate that actually blocks"
      link_checking: "in place and running, in place and unrun, or absent"
      api_or_export: "what can be read programmatically, or none"
      known_limits: "what this system cannot express, which is where content debt accumulates"

  capture_sessions:
    - sme: "named expert, or unassigned"
      topic: ""
      method: "interview | pair_observation | incident_debrief | thread_harvest | draft_and_review | none_yet"
      review_burden: "what this asks of the expert, in time, per cycle"
      transcript_ref: "locator, or none"
      validated_by: "the expert who confirmed the written version, or unvalidated"
      state: "requested | scheduled | captured | drafted | validated | blocked"

  decision_records:
    - id: ""
      decision: "what was decided, stated so a reader two years later can apply it"
      status: "proposed | accepted | superseded | reversed"
      decided_on: "date from a source, or unknown"
      deciders: "named, or unknown"
      alternatives_rejected: []       # each with the reason, because that is the part that stops relitigation
      consequences: "what this commits the organization to"
      supersedes: "prior decision id, or none"
      evidence: "the record the decision was read from, such as minutes, a thread, or a merged proposal"

  runbooks:
    - procedure: ""
      system_touched: ""
      trigger: "when a human runs this"
      prerequisites: "access, tooling, and state the runbook assumes"
      destructive_steps: []           # steps that cannot be undone, named individually
      rollback: "the documented reversal, or none"
      last_executed: "date with the source it came from, or unknown"
      drift: "the steps that no longer match the system, each with what was compared, or unchecked"
      owner: "named owner, or unowned"

  enablement:
    - path: "the named learning path or curriculum"
      role: ""
      modules: []
      prerequisite_knowledge: "what it assumes the learner already has"
      ramp_target: "the time-to-productivity target and who set it, or unset"
      ramp_actual: "measured, with the source, or unmeasured"
      assessment: "how competence is checked, or none"
      completion: "measured rate with its denominator, or unmeasured"

  duplicate_clusters:
    - cluster_id: ""
      members: []                     # each with its locator, usage, and last substantive edit
      overlap_basis: "how the cluster was identified, such as title similarity, shared query, or manual review"
      contradiction:
        - statement_a: "quoted, with its locator"
          statement_b: "quoted, with its locator"
          load_bearing: "yes | no"
      canonical_choice: "the artifact selected, or undecided"
      decided_by: "named person, or open"
      resolution: "merge | redirect | deprecate | scope_and_coexist | undecided"
      state: "identified | proposed | approved | executed"

  freshness:
    - artifact: ""
      review_cadence: "the cadence and the policy or risk basis that sets it, or unset"
      last_reviewed: "date, or never_reviewed"
      decay_signal: "what suggests it is stale, such as a shipped change, a renamed system, or a failed step"
      state: "current | due | overdue | stale | unknown"
      reviewer: "named reviewer, or unassigned"

  access_rules:
    - scope: "artifact, corpus, or space"
      audience_scope: "public | customer | partner | internal | need_to_know | restricted"
      sensitivity_basis: "what makes it sensitive, such as personal data, credentials, unreleased plans, security detail, or privileged advice"
      enforcement_point: "the platform permission, space restriction, or index filter that actually enforces it"
      enforcement_evidence: "how it was confirmed live, or unverified"
      exceptions: []                  # copies that escaped the rule, such as exports, decks, and chat pastes

  search:
    engine: "the system serving queries, or unknown"
    window: "the analytics window every figure below is measured over"
    top_queries: []                   # each with its count and its outcome
    zero_result_queries: []           # each with its count; this is the demand ledger the organization already owns
    low_success_queries: []           # queries that return results nobody opens
    synonym_rules: "configured synonyms and variants, or none"
    best_bets: "curated results pinned to a query, or none"
    ranking_signals: "what the engine actually weights, or unknown"
    scope_gaps: "corpora the index does not cover"

  retrieval_corpus:
    purpose: "what an assistant is expected to answer from this corpus"
    eligible_sources: []              # each with the authority tier that decides which wins on a conflict
    exclusions:
      - source: ""
        reason: "sensitivity, staleness, contradiction, unclear ownership, or format"
    chunking_basis: "the document structure the corpus relies on, and where that structure does not exist"
    metadata_filters: "the fields a retriever can filter on, and which artifacts lack them"
    canonical_answer_coverage: "questions with exactly one authoritative answer, over the question set, or unmeasured"
    contradiction_sweep: "date and method, or never_run"
    refresh: "how the corpus learns a source changed, or manual"
    evaluation_set: "the questions with known correct answers used to judge it, or none"

  localization:
    - locale: ""
      scope: "the artifact set in scope for this locale"
      source_state: "frozen | moving | unknown"
      translation_state: "not_started | in_translation | in_review | published | drifted"
      method: "human | machine_with_post_edit | machine_raw | unknown"
      termbase: "locator of the approved terminology, or none"
      translation_memory: "locator, or none"
      legal_variant: "content that differs by locale for legal reasons rather than by translation, or none"
      drift: "source revisions published since this locale was translated, with the count and its source"
      reviewer: "named in-locale reviewer, or unreviewed"

  governance:
    roles: []                         # author, reviewer, approver, steward, and who holds each
    publishing_authority: "who may publish to each audience reach"
    review_gates: "the gates that actually block a publish, distinguished from the ones a document describes"
    ownership_registry: "coverage of artifacts with a named owner, with the denominator, or unmeasured"
    unowned: []                       # artifacts and corpora with no owner, named rather than counted
    contribution_model: "how knowledge gets written and by whom, including whether capture is part of the work or after it"
    escalation: "who resolves a contested canonical answer"

  measures:
    - name: ""
      value: "measured value"
      denominator: "what it was measured over"
      computed_from: "the query, export, or log it came from"
      as_of: "date"

  gaps:
    - question: "the unanswered question, phrased as the asker phrases it"
      evidence: "what establishes the demand"
      why_unanswered: "never_written | written_and_unfindable | written_and_wrong | written_and_restricted | contradicted"
      candidate_owner: "named, or unassigned"
      priority_basis: "the volume, blast radius, or risk that sets it"

  archival:
    - artifact: ""
      reason: "superseded | obsolete_system | duplicate | never_used | retention_expiry | reorganization"
      successor: "the artifact that now answers the question, or none"
      inbound_references: "links, bookmarks, tickets, macros, retrieval chunks, and external citations that resolve here, with how they were found"
      redirect_target: "where the URL will point, or none"
      tombstone: "what a reader arriving at the old locator will see"
      retention_basis: "the policy that requires keeping or permits deleting it, or none"
      state: "proposed | approved | redirected | archived | deleted"

  knowledge_risks:
    - risk: ""
      artifacts_affected: []
      exposure: "what a reader does wrong if this stands"
      current_control: "what exists today, or none"
      owner: "named owner, or unowned"

  source_facts:
    - fact: "source-backed fact"
      source: "wiki_api | docs_repository | site_crawl | search_analytics | web_analytics | ticket_system | chat_export | link_checker | retrieval_index | retrieval_query_log | learning_system | translation_system | access_log | permission_export | version_history | survey | interview | user | connector | uploaded_file | unknown"
      collected: "when it was read"
  decisions:
    - "decision made at this stage"
  assumptions:
    - assumption: "what was assumed"
      affects: "the artifact, term, audience, or figure it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. The running system is authoritative for what a procedure does. A console, a configuration, a schema, an API response, or a product build outranks every page that describes it. This is the layer most knowledge work never consults, and it is where runbook drift is found.
2. Platform state is authoritative for what exists and what happened to it: the wiki or repository API, page version history, permission exports, the search index, the retrieval index, and the link checker. These establish titles, locators, edit dates, owners of record, access, and reachability.
3. Behavioral evidence is authoritative for demand and for use: search logs including zero-result queries, page analytics, retrieval query logs, ticket drivers, macro usage, and repeated questions in support and chat channels. What people ask for outranks what a content plan says they need.
4. The named subject-matter expert is authoritative for tacit knowledge that no system records, and that authority is recorded with the expert named and the date of the conversation. It is a source fact with a person attached, never an inference.
5. Published content is authoritative for what the organization currently tells people, which is a different claim from whether it is true. A page is evidence of a message, not evidence of a fact.
6. Content plans, style guides, taxonomies, governance charters, and migration decks are authoritative for intent. Tickets and chat threads are decision context and timeline.

The distance between layer 5 and layers 1 and 3 is where nearly every real finding in this domain comes from: the procedure that describes a menu item the product removed, the article with a hundred monthly views that contradicts the one with four, the space nobody can reach that the governance model assumes is maintained. Where a lower layer contradicts a higher one on a load-bearing fact, record both readings with their locators. Do not resolve toward whichever page is better written.

## Evidence discipline

- Every artifact this suite names carries a locator a reader can open. A page referred to by title alone is a claim that it exists, and titles are the easiest thing in this domain to construct correctly by accident.
- Every count, rate, share, and ranking names the export, query, or log window it came from. Corpus size, view counts, search volume, zero-result rate, tagging coverage, ownership coverage, completion rate, and translation drift are all figures somebody will quote in a plan, and all of them are trivially easy to produce at a plausible magnitude.
- Reviewed and current are claims about an event. A review date comes from a recorded review, and an artifact whose history shows no review is `never_reviewed` rather than assumed current because it looks maintained.
- A runbook is verified against the system it operates or it is `unverified`. Reading a procedure and finding it coherent establishes that it is coherent.
- Coverage figures carry their denominator and their crawl state. A corpus that was partially crawled produces a coverage figure over the crawled part, stated as such, rather than over the corpus.
- Contradictions are recorded as two quoted statements with two locators, preserved until the accountable owner adjudicates. Merging them into a single reasonable sentence destroys the finding and publishes a third answer nobody agreed to.
- Owners are recorded because a source names them. The person who wrote a page three years ago is the author of record and is frequently not its owner; promoting one into the other assigns work to somebody who does not know they have it.
- Content containing personal data, credentials, customer identifiers, security detail, unreleased plans, or privileged advice is referenced by locator. Quoting it into an audit artifact creates a second copy in a place with a wider audience and no access rule.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with collection dates, its labeled assumptions, and the gaps it could not close. Later stages trust the packet rather than re-crawling the corpus, so an optimistic completion marker propagates into a coverage figure, then into a governance model sized against it, and then into a headcount conversation.

## Parallel surface

Independent items fan out and are parallel-safe: artifacts under audit, corpora under crawl, audiences, capture sessions with different experts, runbooks under verification, locales, duplicate clusters, individual search queries under analysis, template conformance checks, review queue items, and access rules per space each stand on their own inputs. Connector preflight across the content platform, the documentation repository, search analytics, the ticket system, the link checker, the retrieval index, the learning system, and the translation platform is likewise parallel-safe.

The aggregate work is a single pass after the fan-out returns, and in this domain the aggregate is where the value is. A controlled vocabulary is a statement about the whole corpus; terms normalized per artifact in parallel produce a synonym set nobody merges, which is the exact defect a taxonomy exists to remove. Choosing the canonical member of a duplicate cluster requires all members and their usage side by side. A navigation structure assembled from independently improved pages is a list rather than a path. Coverage, gap, and freshness figures are ratios over a whole set. And the redirect map is computed once as a graph, because redirect targets chosen independently produce chains and loops that break in a way no single-page review detects.

Two carve-outs are mechanical rather than stylistic. Re-tagging under a revised taxonomy follows the term hierarchy, parent before child, because a child term applied under a parent that has not been created yet lands in an unreachable branch. And translation does not run in parallel with edits to its source; the source freeze below exists for that reason.

## Halt behavior

The default posture is to proceed with the assumption labeled inline against the artifact it affects. Hard halts are justified by consequence, never by uncertainty, and belong to the six classes in `references/halt-taxonomy.md`. Content that is merely absent is a soft gap and belongs in the gap ledger; a corpus that exists and cannot be read is a hard halt, because every coverage and contradiction claim built over it would describe a set nobody enumerated.

### Ordered sequence for retiring, merging, or moving published knowledge

Retirement, consolidation, and any change to a locator run in this order:

1. Enumerate every inbound reference before touching anything: internal links, the search index, the retrieval index and its cached chunks, saved queries, support macros, tickets and chat messages that cite the page, learning modules that link it, and external citations where the link checker or referrer data can see them.
2. Publish the successor and confirm it answers the question the retiring artifact was actually used for, taken from search entries and usage rather than from its title.
3. Put the redirect or tombstone in place at the old locator, so a reader who arrives by an old path lands somewhere that tells them where the answer moved.
4. Remove the retiring artifact from the search index and the retrieval corpus, and confirm both now return the successor for the queries that used to reach it.
5. Archive the original with its full version history and its retention basis, and record the inbound references that could not be updated and where they now point.

This order is mandated because each step preserves what the next one needs. Once the artifact is gone its inbound reference set cannot be reconstructed, so a redirect map built after removal is built from memory. Removing an answer before the successor is live does not create a gap that readers notice; it creates a gap that search and retrieval fill with the next best match, which is usually the stale duplicate the consolidation was meant to kill. And archiving before the redirect exists leaves live links resolving to nothing, which readers experience as the organization losing the answer rather than moving it. Do not compress these steps, and do not reorder them if a later edit makes the sequence look redundant.

### Ordered sequence for a source change during a localization cycle

A source-language change while translation is in flight runs in this order:

1. Freeze the source artifacts in scope and record the exact revision each locale is being translated from.
2. Agree the termbase entries for any new or changed term before translation starts, because a term rendered inconsistently across locales cannot be corrected by a diff.
3. Translate and post-edit against the frozen revision, with an in-locale reviewer named per locale.
4. Publish the locales, then release the freeze and record the source revision each locale now corresponds to.
5. Where the source had to change mid-cycle, re-issue the affected segments against the new revision rather than patching the published target, and record the drift for every locale that did not take the change.

The order is mandated because a target translated from a revision that moved underneath it is wrong in a language nobody on the authoring team reads, which means the error is not detected by review but by a reader in that locale acting on it. Recovery costs a full re-review rather than a diff, and the discovery is public.

### Halt format

```markdown
## Workflow Halt

Halt class: <one of the six hard classes>
Consequence: <what a reader, a customer, or a retrieval answer is exposed to if this proceeds>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact artifact, locator, term, permission, or both readings when sources disagree>
Sources attempted: <what was crawled, queried, or requested, and what each returned>
Required approval or access: <named owner and the authority they hold, or the connector and scope needed>
Proceeding meanwhile: <reversible work that does not depend on the blocked fact>
Preserved packet: <full knowledge_packet>
Resume prompt: <prompt that restarts the workflow once the fact or approval arrives>
```

A halt that only reports being stuck is incomplete. Name the exact crawl, export, permission, expert, or approver that unblocks it. A halt justified by uncertainty rather than by consequence is not a halt; it is a labeled assumption that belonged in the artifact, recorded against the page, term, or figure it affects.

## Cross-suite handoffs

Label cross-suite work explicitly rather than implying those desks belong to this suite. Send support article authoring for ticket deflection, macro wording, and agent-facing troubleshooting content to the Customer Support suite, which owns the case surface; this suite owns the corpus those articles live in and whether it contradicts itself. Send documentation that must be proven against code, proof maps, and doc-to-commit traceability to the SDLC suite. Send architecture decision records for a specific system design to the SDLC suite; this suite owns the organization-wide decision record practice and whether a past decision is findable before it is relitigated. Send the data catalog, business glossary bound to physical columns, and metric definitions to the Data suite. Send embedding models, chunking implementation, index configuration, reranking, and retrieval evaluation harnesses to the AI Engineering suite; this suite owns which content is eligible to be retrieved and whether it is true, current, and permitted. Send policy drafting, approval authority, and attestation to the GRC suite. Send personal data handling, lawful basis, and subject rights to the Privacy suite. Send employee onboarding programs, learning administration, and the people record to the People suite; this suite owns the enablement content itself. Send public content marketing, campaign copy, and site information architecture to the Marketing and Web suites.

A knowledge failure with a security, privacy, or safety dimension, such as a restricted document surfaced by search or an incorrect procedure that damaged a production system, belongs to this suite and the receiving suite at the same time, and the handoff is additive rather than a transfer of command.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model, including context budget, native self-verification, long-horizon continuation, and parallel fan-out, along with the governance invariants that do not relax as models improve.
