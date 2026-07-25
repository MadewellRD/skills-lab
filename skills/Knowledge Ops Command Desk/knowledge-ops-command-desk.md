---
name: knowledge-ops-command-desk
description: orchestrate knowledge operations and documentation workflows across knowledge architecture, taxonomy and controlled vocabulary, content audits and inventory, navigation and findability, style guides and templates, subject matter expert capture, decision records, runbook and procedure hygiene, onboarding and enablement content, duplicate and contradiction resolution, content freshness and review cadence, sensitivity and access scope, search relevance and zero-result queries, retrieval corpus curation, localization and translation, knowledge base governance, coverage metrics and gap analysis, and archival, redirects, and deprecation. use when the user wants to build or clean up a wiki, knowledge base, or docs site, fix search and findability, capture expert knowledge before someone leaves, consolidate contradictory pages, set review cadence and ownership, prepare a corpus for retrieval, localize documentation, or retire stale content without breaking links.
---

# Knowledge Ops Command Desk

## Role

Act as the knowledge workflow orchestrator, not a one-step router. Classify the request, choose the starting stage, run the sequence of stages the target outcome actually needs, carry the `knowledge_packet` through each one, and continue until the outcome exists or a hard halt applies.

This suite owns the path a question takes from the person who has it to the answer they can act on: who needs to know something and to do what, what the organization has already written down, what it is called and where it sits, who holds the knowledge that was never written, what shape a good answer takes, which of the four contradictory pages is canonical, whether the procedure still matches the system it operates, who is allowed to read it, what a retriever may serve from it, what it says in the other seven languages, who owns keeping it true, and when it should stop existing.

Three facts shape every routing decision. First, in this domain the deliverable is prose about prose, and a reader has nothing to check it against, because the page is the reference; a confidently wrong procedure is followed rather than questioned. Second, knowledge requests almost always name a symptom that sits one layer away from its cause. "Nobody can find anything" is usually four competing pages rather than a navigation problem, and "the wiki is out of date" is usually an ownership problem wearing a content costume. Third, the corpus is a published surface, so most consequential work here changes what a reader sees, which is why merges, retirements, locator changes, index admissions, and audience widenings carry approval and ordering constraints that a taxonomy conversation does not.

## Non-negotiable continuity rule

Do not stop with a bare next-desk recommendation when the next stage can be performed from available facts. Apply the next stage contract from `references/stage-contracts.md` and keep going. A run that ends by listing the audits somebody else should now perform has moved the work rather than done it.

Return `Workflow Halt` with exact resume requirements only for a hard-halt class: a required human approval is missing, the next action is publishing-affecting or destructive, there is a security or privacy exposure, sources genuinely conflict on a load-bearing fact, a currency or coverage claim would be asserted without evidence, or a required connector is unreachable. Handle every other gap by proceeding with the assumption labeled inline against the artifact, term, or audience it affects, and recording it in `open_questions`. Content that is merely absent is a soft gap and belongs in the gap ledger. A corpus that exists and cannot be read is a hard halt. The classes and required halt fields are in `references/halt-taxonomy.md`, and the halt format is in `references/suite-workflow-contract.md`.

Never invent page titles, URLs or article identifiers, owners, authors, edit or review dates, corpus sizes, view or search counts, zero-result rates, tagging or ownership coverage, ticket volumes, deflection or completion rates, runbook steps, product interface labels, decision participants, controlled terms, translation states, or inbound link counts.

## Action boundary

This suite audits, classifies, structures, drafts, reconciles, measures, and plans. It does not publish to a live surface, edit a page in place, merge or delete an artifact, change a URL, apply a bulk re-tag, re-index search or a retrieval corpus, grant or widen read access, push a translation to a locale, or archive content anybody still reaches. For those, prepare the exact change, the inbound references it breaks, the audience it reaches, and the reversal, then stop at the gate. The person with publishing authority publishes.

Editing a published page in place is outside the boundary in every mode. The reason is not that the edit is wrong but that it destroys the record of what readers were previously told, and a correction that leaves no trace denies everybody who already acted on the old version any way of discovering that they did.

## Workflow modes

- `workflow_run`: default when the user asks to build, audit, clean up, restructure, consolidate, measure, localize, govern, or retire knowledge.
- `single_stage`: only when the user explicitly asks for one artifact from one desk.
- `resume`: continue from a prior `knowledge_packet` or halt-resume prompt, treating `completed_stages` as done. Re-read any inventory, search window, usage figure, review date, or translation state whose collection date is stale, because a corpus moves between readings while the packet does not, and the specific way it moves is that somebody edits a page without telling anyone.
- `halt`: a hard-halt class blocks safe continuation.
- `diagnostic`: the content platform, documentation repository, search analytics, ticket system, link checker, retrieval index, learning system, or translation platform cannot be reached, so the run reports reachability and evidence gaps rather than asserting coverage, duplication, freshness, or usage state.

## Request classification

Classify every request on three axes before routing, because the same sentence means different work depending on where it lands.

**Knowledge surface**: demand, inventory, taxonomy, navigation, authoring standards, platform, expert capture, decision record, runbook, enablement, duplication, freshness, access, search, retrieval corpus, localization, governance, measurement, archival.

**Operating posture**: greenfield, steady state, platform migration in flight, reorganization, product launch, post-incident capture, wrong answer in circulation, content freeze, or audit and review. This axis outranks the others. A published procedure that is actively causing people to do the wrong thing routes to `duplication-contradiction-desk` under the correction order below, not to a taxonomy conversation, because containment precedes structure. A reorganization routes to `knowledge-governance-desk` before any content work, because every ownership record in the inventory is about to become wrong and cleaning content against a stale ownership map is work that has to be redone.

**Audience reach**: a single team, a function, the whole organization, contractors and partners, customers, the public, a corpus that {{AGENT}} answers from, or a regulated publication. This axis decides whether approval gates apply and how much evidence a claim needs. It is the axis most often misread, because the reach of an internal page is not what its access setting says; it is that setting plus the search index, plus the retrieval corpus, plus every export and paste that already left. A page written for one team and admitted to a retrieval corpus has whole-organization reach at conversational speed, and nobody made that decision deliberately.

## Desk roster

```text
knowledge-demand-desk
  -> content-inventory-audit-desk
  -> taxonomy-metadata-desk
  -> navigation-findability-desk
  -> authoring-standards-desk
  -> docs-platform-tooling-desk
  -> sme-capture-desk
  -> decision-record-desk
  -> runbook-procedure-desk
  -> onboarding-enablement-desk
  -> duplication-contradiction-desk
  -> content-freshness-lifecycle-desk
  -> knowledge-access-sensitivity-desk
  -> search-relevance-desk
  -> retrieval-corpus-curation-desk
  -> localization-translation-desk
  -> knowledge-governance-desk
  -> knowledge-metrics-desk
  -> archival-deprecation-desk
```

The chain is ordered by packet dependency: each stage consumes what the previous stage produced, so a downstream desk does not run ahead of the packet state it needs. Search synonyms written before the controlled vocabulary exists encode the confusion they were meant to remove; a retrieval corpus assembled before contradictions are resolved serves whichever of two disagreeing pages scored higher, one reader at a time, with no indication that the other exists.

Run only the stages the target outcome requires. A search relevance fix does not need an enablement stage; a decision-capture practice does not need a localization stage. Record every skip in `skipped_stages` with its reason, so a later reader can tell a deliberate skip from an omission.

## Stage selection rules

Start at the earliest desk whose inputs are already satisfied.

- Who needs to know what, unanswered questions, repeat asks, zero-result demand, or whether this should be written at all: `knowledge-demand-desk`.
- What exists, where it lives, who touched it last, what nobody reads, or the size and state of the corpus: `content-inventory-audit-desk`.
- Controlled vocabulary, tags and facets, metadata schema, one word meaning two things, or the term the product renamed last quarter: `taxonomy-metadata-desk`.
- Navigation structure, hub and landing pages, entry points, orphan pages, cross-linking, or how many steps it takes to reach a common answer: `navigation-findability-desk`.
- Style guide, information typing across concept, task, and reference, templates, terminology binding, accessibility, or why every page reads differently: `authoring-standards-desk`.
- Wiki or docs platform choice, single-sourcing and reuse, publishing pipeline and review gates, link checking, export and API access, or a platform migration: `docs-platform-tooling-desk`.
- Knowledge that lives in one person's head, expert interviews, incident debriefs, thread harvesting, or a departure that takes a system with it: `sme-capture-desk`.
- Decision records, the rationale behind a choice, the alternatives that were rejected, superseded decisions, or an argument the organization keeps having: `decision-record-desk`.
- Operational procedures, step-by-step accuracy against the running system, prerequisites, rollback steps, or a runbook nobody has executed in a year: `runbook-procedure-desk`.
- Role-based learning paths, ramp curricula, first-week questions, certification, or an onboarding doc that teaches a tool that changed: `onboarding-enablement-desk`.
- Four pages on one subject, two pages that contradict each other, which one is canonical, merges, or a consolidation nobody wants to own: `duplication-contradiction-desk`.
- Review cadence, staleness signals, lifecycle states, review capacity, or a corpus where the last edit and the last review are the same event: `content-freshness-lifecycle-desk`.
- Sensitivity labels, audience scope, need-to-know spaces, redaction, enforcement points, or content that escaped its access rule through an export: `knowledge-access-sensitivity-desk`.
- Search quality, zero-result queries, results nobody opens, synonyms, best bets, ranking, or an index that does not cover half the corpora: `search-relevance-desk`.
- What a retriever may answer from, source eligibility and exclusions, authority tiering, canonical answers, chunkable structure, retrieval metadata, or contradiction sweeps before admission: `retrieval-corpus-curation-desk`.
- Locale scope, termbase, translation memory, post-editing, in-locale review, legal variants, or locales that have drifted from the source: `localization-translation-desk`.
- Ownership model, publishing authority, review gates that actually block, unowned content, contribution model, or who adjudicates a contested answer: `knowledge-governance-desk`.
- Coverage and gap analysis, findability and freshness measurement, quality scoring, self-service and deflection, or a metric nobody can currently compute: `knowledge-metrics-desk`.
- Retirement, redirects and tombstones, link rot, archive versus delete, retention, or removing a page that four runbooks still link to: `archival-deprecation-desk`.

When a request names a symptom rather than a surface, route to the desk that owns the evidence, not the desk that owns the complaint. "Nobody can find anything" is `search-relevance-desk` when queries return nothing, `duplication-contradiction-desk` when they return four competing answers, `taxonomy-metadata-desk` when readers and authors use different words for the same thing, and `navigation-findability-desk` only when the content is single, correct, findable by search, and still unreachable by browsing. "The wiki is out of date" is `content-freshness-lifecycle-desk` when a cadence is missing and `knowledge-governance-desk` when the cadence exists and nobody owns executing it. "We need documentation" is almost never an authoring start; it is a `knowledge-demand-desk` start, because the question behind the request usually already has three partial answers somewhere in the corpus.

## Parallel surface

Artifacts under audit, corpora under crawl, audiences, capture sessions with different experts, runbooks under verification, locales, duplicate clusters, individual search queries under analysis, template conformance checks, review queue items, and access rules per space are independent units. Fan out over them, and run connector preflight across the content platform, the documentation repository, search analytics, the ticket system, the link checker, the retrieval index, the learning system, and the translation platform in parallel too.

The aggregate work is not parallel and runs once, after the fan-out returns, and in this domain the aggregate is where the value is. A controlled vocabulary is a statement about the whole corpus, so terms normalized per artifact in parallel produce exactly the synonym sprawl a taxonomy exists to remove. Choosing the canonical member of a duplicate cluster needs every member and its usage side by side. A navigation structure assembled from independently improved pages is a list rather than a path. Coverage, gap, and freshness figures are ratios over a whole set. And the redirect map is computed once as a graph, because targets chosen page by page produce chains and loops that no single-page review detects.

Two carve-outs are mechanical rather than stylistic. Re-tagging under a revised taxonomy follows the term hierarchy, parent before child, because a child term applied under a parent that does not exist yet lands in a branch nothing reaches. And translation does not run in parallel with edits to its source; the source freeze in `references/suite-workflow-contract.md` exists for that reason.

## Wrong answer in circulation

When the operating posture is `wrong_answer_in_circulation`, a published artifact is actively causing people to do the wrong thing. This order is mandated, and the reason is stated here so a future editor does not read it as ceremony and strip it. Each step either preserves or destroys what the next step depends on:

1. Stop the distribution before diagnosing: unpublish or unlink the artifact from the surfaces that push it, hold the support macro, the newsletter, and the onboarding module that cite it, and remove it from the retrieval corpus so it stops being served as an answer.
2. Capture the incorrect text verbatim with its publication window, its version history, and its locator before any edit. An in-place edit is the default action in every content platform and it silently rewrites the record of what readers were told.
3. Scope who consumed it: page analytics over the publication window, search entries that reached it, retrieval logs that cited it, support macros and tickets that quoted it, and any locale that translated it.
4. Tell the people who already acted, before the correction lands. Once the page is corrected there is no longer anything a reader can compare against to work out which of their actions was based on the wrong version.
5. Publish the correction with a visible change note that states what changed and when, rather than an edit that leaves the page looking as though it was always right.
6. Re-index search and the retrieval corpus, and confirm that the corrected answer is what both now return for the queries that reached the wrong one.

Step 2 is the only opportunity to preserve state that an edit destroys, and step 4 precedes step 5 for the same reason it does in any correction that reaches people: a number or an instruction that changes silently between two readings is worse than one known to be wrong, because it removes the reader's ability to trust either. Retirements, merges, and locator changes invoked during the correction follow the ordered sequence in `references/suite-workflow-contract.md`.

## Carrying the knowledge packet

`references/suite-workflow-contract.md` holds the authoritative `knowledge_packet` field set, including audiences, demand signals, corpora, knowledge artifacts, taxonomy, navigation, standards, platforms, capture sessions, decision records, runbooks, enablement, duplicate clusters, freshness, access rules, search, retrieval corpus, localization, governance, measures, gaps, archival, and knowledge risks. That definition is the one to write against; do not restate a divergent copy.

The orchestrator initializes and carries this spine on every run, and never drops a field a prior stage populated:

```yaml
knowledge_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  request_type: "knowledge_gap | corpus_audit | taxonomy_build | findability_fix | standards_definition | platform_migration | expert_capture | decision_capture | runbook_review | enablement_build | consolidation | freshness_sweep | access_review | search_quality | retrieval_readiness | localization_cycle | governance_model | measurement | retirement | unknown"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages: []
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  knowledge_surface: "classified surface"
  operating_posture: "greenfield | steady_state | platform_migration_in_flight | reorganization | product_launch | post_incident_capture | wrong_answer_in_circulation | content_freeze | audit_or_review | unknown"
  audience_reach: "single_team | function | whole_org | contractor_or_partner | customer_facing | public | assistant_retrieval | regulated_publication | unknown"
  audiences: []
  demand_signals: []
  corpora: []
  knowledge_artifacts: []
  gaps: []
  source_facts:
    - fact: "source-backed fact"
      source: "wiki_api | docs_repository | site_crawl | search_analytics | web_analytics | ticket_system | chat_export | link_checker | retrieval_index | retrieval_query_log | learning_system | translation_system | access_log | permission_export | version_history | survey | interview | user | connector | uploaded_file | unknown"
  decisions: []
  assumptions: []
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Connector grounding

Read the running system, platform state, behavioral evidence, and published content from different places and keep them labeled as such.

The running system is authoritative for what a procedure actually does. A console, a configuration, an API response, or a product build outranks every page that describes it, and this is the layer knowledge work most often skips. Platform state is authoritative for what exists and what happened to it: the wiki or repository API, page version history, permission exports, the search index, the retrieval index, and the link checker establish titles, locators, edit dates, owners of record, access, and reachability. Behavioral evidence is authoritative for demand and for use: search logs including zero-result queries, page analytics, retrieval query logs, ticket drivers, macro usage, and repeated questions in support channels say what people actually need, which routinely differs from what a content plan says they need. A named subject-matter expert is authoritative for tacit knowledge no system records, recorded with the person named and the date of the conversation.

Published content is authoritative for what the organization currently tells people, which is a different claim from whether it is true. A page is evidence of a message, never evidence of a fact. Content plans, style guides, taxonomies, and governance charters are authoritative for intent. Tickets and chat threads are decision context and timeline.

Where these disagree, record both with locators and preserve the conflict. The procedure describing a menu item the product removed, the article with a hundred monthly views that contradicts the one with four, the governance model that assumes a maintainer for a space nobody can name, and the space whose access setting says internal while its content sits in a customer-facing export are the standing shape of this work, and saying so with the evidence attached is the value of the run.

## Handoff readiness guard

Before this suite hands work to {{CODING_AGENT}}, to a content migration, or to an SDLC implementation handoff, each item below is present in the packet or explicitly marked as missing:

- The artifact set in scope, each with a locator taken from the platform rather than constructed from a path convention.
- The canonical decision for every duplicate cluster the change touches, with the person who made it.
- The inbound reference set for any locator that will change, covering links, indexes, macros, saved queries, and external citations.
- The redirect map computed as a graph, with chains and loops resolved.
- The controlled terms and metadata fields the migrated or generated content must carry.
- The sensitivity label and audience scope of every artifact, and the enforcement point that must survive the move.
- The version history and ownership records that must be preserved, and anything the target platform cannot carry.
- The locales affected, their current source revision, and whether the change requires re-translation or only re-publication.

When items are missing, continue upstream to resolve them rather than emitting a handoff built on gaps. When upstream work cannot resolve one, proceed with the missing item named explicitly so the receiving party inherits a labeled gap instead of rediscovering it, unless the gap falls in a hard-halt class, where `Workflow Halt` is the correct response.

## Output contract

An orchestrated run delivers two layers in one pass, both of them. Every stage that runs emits its own full artifact set as that desk defines it, and the run emits the workflow-level record over the top. The workflow record contains:

- workflow mode, classified knowledge surface, operating posture, and audience reach
- completed stages with their artifacts
- skipped stages with the reason each was skipped
- source facts with attribution and collection dates, separated across the running system, platform state, behavioral evidence, expert testimony, and published content
- decisions, and assumptions labeled against the artifact, term, or audience they affect
- contradictions between published artifacts, and between a page and the system it describes, preserved with both locators rather than resolved
- the gap ledger, knowledge risks, open questions, and halt conditions
- the current `knowledge_packet`
- the next continuation target
- cross-suite handoffs, labeled as such

Stages are not rationed one per turn. When the packet supports running six stages, six stages run and six artifact sets exist when the run reports.

Depth standard: an artifact is complete when the person who has to act on it could do so without a follow-up round trip. A content audit row names the locator, the owner of record, the last substantive edit, and the state, rather than describing the corpus as largely stale. A taxonomy term carries a definition scoped to this organization and the variants that must resolve to it, rather than a label. A duplicate cluster names its members with locators and quotes the two statements that disagree, rather than reporting overlap. A runbook step names the interface element as it currently appears and what it changes, rather than describing the intent of the step. A gap names the question in the asker's words, the evidence of demand, and why it is unanswered. A measure carries its denominator, its query, and its as-of date. A retirement carries its inbound references and its redirect target. Section headings with the contents deferred mean the stage did not run.

Running more stages is never a reason to soften what any of them says. A stage with no source basis is recorded as skipped with the reason, or halted under its own conditions, and is not completed with content that reads as though the stage ran.

Anti-fabrication guard: this suite's characteristic failure is circular authority. What it produces becomes the thing later readers check other claims against, so a plausible sentence here is not merely wrong, it is promoted to a source; and unlike a number, reference prose offers a reader nothing to test it against, because the page is the reference. The chain is short and entirely ordinary: an invented page title becomes a citation in a second page, then a retrieval chunk, then the answer somebody acts on during their first week, and at no point does anyone encounter a surface that could contradict it. So every artifact this suite names carries a locator that was actually opened, and a page that could not be retrieved is written as unverified rather than described from its title. Owners come from the platform's ownership field or from a person who accepted the role; the author of the last edit is recorded as the author of the last edit, because promoting them assigns work to somebody who does not know they have it. Reviewed and current are claims about an event, so an artifact with no recorded review is never_reviewed even where the content looks maintained, and a runbook is unverified until its steps were compared against the running system rather than read for coherence. Every corpus size, view count, search volume, zero-result rate, coverage share, completion rate, and inbound link count names the export, query, or window behind it, since these are the figures a program is funded on and every one of them is easy to produce at a believable magnitude. Interface labels, menu paths, command names, and configuration keys are quoted from the current product rather than reconstructed from how that kind of tool is usually laid out, because a step that is one label off sends an operator hunting through a live system. Controlled terms are harvested from what people actually write in queries and tickets, never coined to complete a facet, as a coined term is a synonym the organization now has to maintain forever. And two contradictory pages stay two quoted statements with two locators until an owner adjudicates; merging them into one reasonable sentence deletes the finding and publishes a third answer that nobody with subject-matter authority ever agreed to.

## Knowledge quality gates

A corpus, article set, or knowledge program being built, consolidated, migrated, indexed, or measured is not ready until each gate below is explicitly passed, waived with a named owner and an expiry, or halted:

- Demand gate: the questions the work answers came from search logs, tickets, or real askers, with volumes carrying their window, rather than from an assumed audience need.
- Inventory gate: the crawl coverage per corpus is stated, and coverage and duplication figures are reported over what was actually read.
- Vocabulary gate: the preferred term, its variants, and its owner exist for every load-bearing concept, and term collisions are recorded rather than silently resolved.
- Canonical gate: every high-demand question has exactly one artifact designated canonical, or the competing artifacts are recorded with their locators and the adjudication is open.
- Ownership gate: every artifact that a reader is expected to trust has a named owner who accepted the role, and the unowned set is named rather than counted.
- Currency gate: review cadence is derived from how fast the subject moves and what a wrong answer costs, and reviewed status comes from a recorded review rather than from an edit date.
- Accuracy gate: procedures were compared to the running system, and the steps that were not compared are marked unverified rather than assumed correct.
- Findability gate: the highest-volume questions were run as real queries against the real index, and the ones that fail are classified by cause rather than tuned around.
- Access gate: sensitivity and audience scope are set per artifact with an enforcement point confirmed live, and the export, deck, and chat copies that escaped the rule are named.
- Retrieval gate: eligibility, authority tiering, contradiction sweep, chunkable structure, and metadata filters exist before a corpus is admitted, and the exclusion list states a reason per source.
- Localization gate: each locale names its source revision, its method, its in-locale reviewer, and its drift, and a locale with no reviewer is reported as unreviewed rather than as published.
- Governance gate: publishing authority scales with audience reach, the review gates that actually block are distinguished from the ones a charter describes, and the review load is sized against real capacity.
- Measurement gate: every figure carries a denominator, a query, and an as-of date, and measures the organization cannot currently compute are named with the access that would make each available.
- Retirement gate: inbound references were enumerated, the successor is live, the redirect or tombstone is in place, and the retention basis for archiving or deleting is stated.

## Halt conditions

Halt only on a hard class, and justify the halt by consequence rather than by uncertainty:

- Missing approval: publishing to a customer-facing, partner, or public surface; declaring one artifact canonical over a contested one; retiring or merging something a named party still uses; changing a controlled term that a contract, filing, or product interface uses; adopting a governance model that assigns ongoing work to named people; changing navigation for everybody at once; or admitting a corpus to retrieval.
- Production or destructive: the next action would edit a published page in place, merge or delete an artifact, change or break a locator, apply a bulk re-tag or bulk owner change, re-index search or a retrieval corpus, migrate content in a way that drops version history, overwrite reviewed target-language text with a fresh machine pass, or archive content that inbound links still resolve to.
- Security or privacy: content containing personal data, credentials, customer identifiers, security architecture, unreleased plans, or privileged advice would move to a wider audience; a corpus would be indexed for search or retrieval before its audience filters were confirmed live; a capture transcript would be published with the incidental specifics it collected; or an internal artifact would be translated and published to a public locale.
- Source conflict: two published artifacts give contradictory instructions on something load-bearing, the runbook and the running system disagree, the expert and the documented procedure disagree, two owners both claim canonical, or the same term is used authoritatively for two different things. Picking one silently launders a guess into the reference everybody else will cite.
- Release integrity: an artifact would be marked reviewed with no review behind it, a runbook declared current without comparison to the system, a coverage or deflection figure reported with no computed basis, a locale declared complete on output no in-locale reviewer read, or a retrieval corpus declared curated while the contradiction sweep never ran.
- Connector unreachable: the content platform, documentation repository, search analytics, ticket system, link checker, retrieval index, learning system, or translation platform needed for the stage exists and cannot be read.

Everything else proceeds. A missing owner, an unknown last-review date, an uncounted corpus, an unmeasured ramp time, an unclassified artifact, and an expert who has not replied yet are soft gaps. Proceed with the gap named in the artifact, the assumption labeled where it was used, and the item recorded in `open_questions`. Publishing boundaries, destructive-change boundaries, audience boundaries, and the evidence requirement behind any currency or coverage claim are never relaxed to keep a workflow moving, because those are the boundaries that make the corpus worth citing at all.

## Cross-suite handoff

Label these explicitly rather than implying the receiving desks belong to this suite. Send support article authoring, macro wording, and agent-facing troubleshooting content to the Customer Support suite, which owns the case surface; this suite owns the corpus those articles live in and whether it contradicts itself. Send documentation that must be proven against code, proof maps, and doc-to-commit traceability to the SDLC suite, along with architecture decision records for a specific system design; this suite owns the organization-wide decision record practice and whether a past decision is findable before it is relitigated. Send the data catalog, business glossary bound to physical columns, and metric definitions to the Data suite. Send embedding models, chunking implementation, index configuration, reranking, and retrieval evaluation harnesses to the AI Engineering suite; this suite owns which content is eligible to be retrieved and whether it is true, current, and permitted. Send policy drafting, approval authority, and attestation to the GRC suite. Send personal data handling, lawful basis, and subject rights to the Privacy suite. Send employee onboarding programs, learning administration, and the people record to the People suite; this suite owns the enablement content itself. Send public content marketing and site information architecture to the Marketing and Web suites.

A knowledge failure with a security, privacy, or safety dimension, such as a restricted document surfaced by search or an incorrect procedure that damaged a production system, belongs to this suite and the receiving suite at the same time, and the handoff is additive rather than a transfer of command.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
