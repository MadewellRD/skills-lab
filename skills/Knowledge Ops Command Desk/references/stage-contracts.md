# Knowledge Ops Stage Contracts

One entry per desk in the Knowledge Ops Command Desk suite: what it requires on input, what it owns on output, where it hands the `knowledge_packet`, and the hard halt specific to that stage. The orchestrator uses these contracts to route; each member desk uses its own entry as the acceptance boundary for "this stage is done."

## Default sequence

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

The chain is ordered by packet dependency, not by calendar. A request that starts mid-chain starts at the earliest desk whose inputs are already satisfied, and an incorrect answer already in circulation enters at `duplication-contradiction-desk` regardless of what sits upstream of it.

Two dependencies are load-bearing rather than conventional. Everything downstream of the taxonomy stage assumes a declared term set, because search synonyms, navigation facets, retrieval metadata filters, and the localization termbase all key off the same vocabulary, and two labels for one concept splits the corpus in all four at once. And nothing in search, retrieval, or localization is safe before sensitivity and audience scope are resolved per artifact, because a retriever answers from whatever it was permitted to index and a published translation is a second copy of the same disclosure in a place the original access rule does not reach.

## Stage completion rule

Every desk emits: source facts with attribution and collection dates, decisions, its artifact set, the packet fields it updated, assumptions labeled where they were used, open questions, halt conditions, and next-stage readiness. Every artifact named carries a locator. Every count, rate, and share carries its query and denominator. Uncrawled stays uncrawled in the packet, never_reviewed stays never_reviewed, and an owner inferred from an edit history is recorded as inferred rather than as assigned.

---

## knowledge-ops-command-desk

- **Requires**: the user request, the target outcome, the operating posture, the audience reach the work touches, and whatever connector access exists for the content platform, the documentation repository, search analytics, the ticket system, the link checker, the retrieval index, the learning system, and the translation platform.
- **Owns**: request classification across surface, posture, and audience reach; stage path selection; packet initialization and carriage; adjudication between what a page claims and what the running system does; the workflow-level record; and the cross-suite handoff decision.
- **Hands to**: the earliest member desk whose inputs are satisfied, then each successive stage until the target outcome is reached or a hard halt applies.
- **Hard halt**: connector unreachable. A corpus that exists and cannot be crawled makes every coverage, duplication, and freshness figure in the run a statement about a set nobody enumerated.

## knowledge-demand-desk

- **Requires**: the audiences and the tasks they are trying to complete, search logs including zero-result queries, ticket drivers and repeated questions from support and chat, onboarding friction reports, and any existing content plan.
- **Owns**: the audience and task inventory written as what a reader is trying to do rather than what they are interested in; the demand ledger built from questions as askers phrase them, each with its measured volume and the log window behind it; the current answer state per question across answered, partial, contradicted, scattered, unanswered; the cost of the unanswered question stated as who is blocked and what they do instead; the criticality tier that decides how much rigor the answer earns; and the explicit statement of which existing artifacts already answer part of it, so the run does not add a fifth page to a cluster of four.
- **Hands to**: `content-inventory-audit-desk`.
- **Hard halt**: connector unreachable. Search analytics and the ticket queue are the only honest demand signals available; a demand ledger written without them is a list of questions somebody imagined, and everything downstream is prioritized against it.

## content-inventory-audit-desk

- **Requires**: access to every corpus in scope, export or crawl capability, page version history, usage analytics where they exist, and the demand ledger to audit coverage against.
- **Owns**: the census of corpora with their system, steward, counted size, and crawl state; the artifact inventory with title, locator, information type, owner, author of record, last substantive edit, last recorded review, and lifecycle state; usage measured from analytics rather than assumed from importance; the orphan set that no navigation path reaches; coverage of demand against what exists, naming the questions with no artifact and the artifacts with no demand; the content debt baseline including stubs, drafts published by accident, and pages whose only edit is their creation; and the honest crawl coverage figure stating what share of each corpus was actually read.
- **Hands to**: `taxonomy-metadata-desk`.
- **Hard halt**: connector unreachable. A partial crawl reported as an inventory understates duplication and overstates coverage in the same pass, and both errors point the program at the wrong work.

## taxonomy-metadata-desk

- **Requires**: the artifact inventory, the vocabulary readers actually use from search queries and ticket text, existing tags and spaces, product and domain terminology, and the systems that will consume the vocabulary.
- **Owns**: the controlled vocabulary with a preferred label, a definition scoped to this organization, and the variants, abbreviations, and legacy names that must resolve to it; the facet set with permitted values and who may add one; the metadata schema stating which fields are required per information type and which are optional; term conflicts recorded as one label with two meanings or two labels with one meaning, each reading kept with its source until a term owner adjudicates; the mapping of the vocabulary into every consumer, covering search synonyms, navigation facets, retrieval metadata filters, and the localization termbase; term ownership; and tagging coverage measured against a stated denominator.
- **Hands to**: `navigation-findability-desk`.
- **Hard halt**: source conflict. Two authoritative sources use the same label for different things, and the collision is load-bearing. Choosing one silently makes every downstream filter, facet, and synonym rule wrong in the same direction, and the error is invisible because each individual page still reads correctly.

## navigation-findability-desk

- **Requires**: the taxonomy, the artifact inventory with usage, entry-point analytics showing where readers actually arrive, and whatever wayfinding evidence exists from card sorts, tree tests, or observation.
- **Owns**: the navigation structure expressed as the paths a reader takes to a named answer rather than as a hierarchy of topics; entry points ranked by measured arrival rather than by design intent, including the ones outside the content platform such as a search box, a chat answer, or a bookmark; landing and hub pages with what each is responsible for routing to; cross-linking rules including the related-content and next-step patterns that carry a reader through a task; the orphan resolution plan; depth-to-answer measured for the highest-volume questions; breadcrumb and labeling conventions bound to the controlled vocabulary; and the findability defects that navigation cannot fix, handed forward as search or consolidation work rather than absorbed into a redesign.
- **Hands to**: `authoring-standards-desk`.
- **Hard halt**: approval. A navigation change moves every reader's path at once, and readers who have learned a route experience a reorganization as content loss. The owner of the surface approves the structure and the transition.

## authoring-standards-desk

- **Requires**: the information types the corpus needs, sample artifacts across quality levels, the controlled vocabulary, accessibility and plain-language requirements, and the authors who will work to the standard.
- **Owns**: the information typing model separating concept, task, reference, policy, runbook, and decision record, with the rule that a page mixing types is why readers cannot skim it; templates per type with the sections that are mandatory and the reason each exists; the style guide covering voice, tense, person, sentence length, imperative form for procedures, and the treatment of screenshots that age faster than the prose around them; terminology rules binding prose to the controlled vocabulary; title and heading conventions that determine both scannability and retrieval chunk boundaries; accessibility requirements including heading order, alt text, link text, and table structure; the minimum viable artifact for each type so a contributor is not blocked by a template built for a longer document; and conformance measured across a stated sample rather than asserted.
- **Hands to**: `docs-platform-tooling-desk`.
- **Hard halt**: none specific. Standards work is reversible and proceeds with assumptions labeled against the type or template they affect.

## docs-platform-tooling-desk

- **Requires**: the platform inventory with what each system is used for, the authoring population and their tooling, the publishing path from edit to reader, the standards and templates to implement, and any migration already in motion.
- **Owns**: the system-of-truth assignment stating what each platform is authoritative for and, more usefully, what it is not; the authoring and publishing pipeline including the review gate that actually blocks a publish, distinguished from the one a governance document describes; single-sourcing and content reuse design covering snippets, includes, variables, and conditional content, with the explicit statement of what is currently duplicated by copy and paste; template and metadata enforcement at the point of authoring rather than at review; link checking, orphan detection, and build-time validation with whether each is running or merely installed; the API and export surface that every later stage depends on for crawling, measurement, and retrieval; migration design between platforms including locator mapping, history preservation, and what does not survive the move; and the platform limits that generate content debt, stated as constraints rather than as complaints.
- **Hands to**: `sme-capture-desk`.
- **Hard halt**: production or destructive. A platform migration rewrites locators in bulk, and a migration that drops version history destroys the only evidence of who wrote what and when, which is unrecoverable and is exactly what every ownership and freshness claim downstream is built on.

## sme-capture-desk

- **Requires**: the gap ledger with the unanswered questions worth an expert's time, the experts who hold the knowledge and their availability, the incidents, threads, and demonstrations where tacit knowledge is already surfacing, and the templates the captured knowledge will land in.
- **Owns**: the elicitation plan matched to the kind of knowledge, distinguishing what an expert can explain from what they can only demonstrate; the capture method per topic across interview, paired observation, incident debrief, thread harvest, and draft-for-review, with draft-for-review preferred where an expert reviews faster than they write; the review burden stated honestly in hours per cycle, because an unfunded review burden is why capture programs stop; the drafted artifact traced to the session that produced it; expert validation recorded as a named person confirming the written version, which is a different fact from having attended the session; the questions the expert could not answer, which are gaps rather than silence; and the single-point-of-knowledge register naming subjects one person holds, with what happens to each if that person is unavailable.
- **Hands to**: `decision-record-desk`.
- **Hard halt**: security or privacy. Capture sessions surface customer specifics, credentials, security architecture, unreleased plans, and personnel detail as incidental context, and a transcript published into a general corpus carries all of it into an audience the expert never imagined.

## decision-record-desk

- **Requires**: the decisions worth recording and where they were actually made, the participants, the alternatives that were considered, existing decision records and their status, and the questions that keep being relitigated.
- **Owns**: the decision record set with each decision stated so a reader two years later can apply it rather than merely recognize it; the alternatives rejected with the reason, which is the part that stops the relitigation and the part most often omitted; the constraints and assumptions in force at the time, so a reader can tell whether the decision still holds; status across proposed, accepted, superseded, and reversed, with the supersession chain intact rather than the old record edited; consequences stated as what the organization is now committed to; the capture trigger defining which decisions earn a record, since a practice that records everything records nothing; the retrieval path that makes a past decision findable before the same argument restarts; and the decisions that were made and never recorded, named as gaps with the participants who could still reconstruct them.
- **Hands to**: `runbook-procedure-desk`.
- **Hard halt**: source conflict. Participants remember a decision differently, or the record and the implemented outcome disagree. Recording one version resolves an argument by fiat and creates a false precedent that the next reader inherits as settled.

## runbook-procedure-desk

- **Requires**: the procedures in scope, access to the systems they operate or a person who can confirm current behavior, execution history where the platform records it, incident and escalation records that cite the runbook, and the destructive-operation policy in force.
- **Owns**: the procedure set written in imperative steps against the actual current interface, with prerequisites for access, tooling, and system state stated before the first step rather than discovered at step four; drift findings from comparing each step to the running system, recorded per step with what was compared and when; destructive steps named individually with what they cannot undo; the rollback for every procedure or the explicit statement that none exists, which is itself the finding; decision points and branches where an operator has to choose, with what distinguishes the branches; the last-executed record taken from a source rather than from plausibility; the operator this is written for, since a runbook written for its author is a reminder rather than a procedure; and the procedures nobody has run in long enough that they are unverified regardless of how correct they look.
- **Hands to**: `onboarding-enablement-desk`.
- **Hard halt**: release integrity. A procedure declared current on the strength of reading it, without any comparison to the system, is a set of instructions somebody will follow against production at three in the morning. Coherence is not currency, and this is the one artifact in the suite where the reader has no ability to check.

## onboarding-enablement-desk

- **Requires**: the roles being ramped and what they must be able to do unsupervised, the existing curriculum and its completion data, the questions new joiners actually ask in their first weeks, the artifacts the path will point at, and the learning system that delivers it.
- **Owns**: the learning path per role sequenced by capability rather than by topic, with each module stating what the learner can do afterwards; the prerequisite map so a path does not assume knowledge it never delivered; the split between durable enablement content and content that points at the canonical artifact, which is what stops a curriculum becoming a fifth copy of everything it teaches; assessment and the definition of ready to work unsupervised; time-to-productivity target against measured ramp where the data supports it; the first-weeks question set from real joiners, used as the acceptance test for the path; refresh ownership tied to the product and process changes that invalidate a module; and the enablement debt where a path teaches a system that has since changed.
- **Hands to**: `duplication-contradiction-desk`.
- **Hard halt**: none specific. Enablement design is reversible and proceeds with assumptions labeled against the path or module they affect.

## duplication-contradiction-desk

- **Requires**: the artifact inventory with usage and last substantive edit, the controlled vocabulary that reveals which pages are about the same thing under different labels, search queries that return several competing answers, and the subject-matter owners who can adjudicate.
- **Owns**: duplicate clusters with the basis on which each was identified, covering near-identical pages, partial overlaps, and the harder case of pages that agree in substance and differ in one instruction; contradictions recorded as two quoted statements with two locators and a judgment on whether the difference is load-bearing; the canonical choice per cluster with the person who made it, decided from usage, currency, and accuracy rather than from length or polish; the resolution across merge, redirect, deprecate, and scope-and-coexist, with scope-and-coexist reserved for genuine audience or version differences and named as such on both artifacts; the merge plan preserving anything true that exists only in a non-canonical member; and the contradiction ledger for clusters where no owner has adjudicated, kept open rather than resolved by the desk.
- **Hands to**: `content-freshness-lifecycle-desk`.
- **Hard halt**: source conflict. Two published artifacts give contradictory instructions on something load-bearing, and both have plausible authority. Picking the better-written one publishes a third answer that nobody with subject-matter authority agreed to, and it now carries the weight of a consolidation.

## content-freshness-lifecycle-desk

- **Requires**: the artifact inventory with edit and review history, the change signals that invalidate content such as releases, renamed systems, and org changes, the owners who would do the reviewing, and the risk basis that decides how often each type needs review.
- **Owns**: the lifecycle states and the transitions between them, so draft, published, stale, contested, superseded, and archived mean the same thing everywhere; the review cadence per information type derived from how fast the underlying subject moves and what a wrong answer costs, rather than a uniform interval that guarantees the wrong things get reviewed; decay signals that flag content without waiting for a calendar, including a shipped change touching the system a page describes, a renamed term, a departed owner, and a rising rate of follow-up questions on an article; the review queue sized against real reviewer capacity, because a queue larger than capacity is a policy that produces stale content with a compliance record; visible staleness marking so a reader can see the risk they are taking; and the never-reviewed set named rather than counted.
- **Hands to**: `knowledge-access-sensitivity-desk`.
- **Hard halt**: release integrity. Marking content reviewed on the basis of an edit date, a bulk operation, or an assumption that somebody must have looked at it produces a corpus that reports itself as current. That claim is then trusted by search ranking, by retrieval eligibility, and by every reader who checks the review badge instead of the content.

## knowledge-access-sensitivity-desk

- **Requires**: the artifact and corpus inventory, the audience entitlements, the permission model each platform actually enforces, the classification rules in force, and the export and sharing paths content takes out of its home system.
- **Owns**: the sensitivity classification applied to real artifacts rather than to categories, with the basis stated as personal data, credentials, customer identifiers, security detail, unreleased plans, privileged advice, or contractual restriction; the audience scope per artifact and space across public, customer, partner, internal, need-to-know, and restricted; the enforcement point that actually applies each rule, distinguished from the label that describes it; enforcement evidence confirmed live, with unverified rules recorded as unverified; the escape paths where content left its access rule, including exports, decks, chat pastes, learning modules, and copies made during a migration; the joiner and leaver effect on space membership and standing access nobody re-approves; and the redaction requirement per artifact that must exist in more than one audience.
- **Hands to**: `search-relevance-desk`.
- **Hard halt**: security or privacy. Widening an audience, or admitting content to an index whose filters have not been confirmed live, is a disclosure that cannot be withdrawn once a reader has seen it. Restricted content surfaced by a search box or a retrieval answer is exposed by exactly the mechanism the program built to help people find things.

## search-relevance-desk

- **Requires**: the search engine and its configuration, query logs over a stated window, the controlled vocabulary and its variants, the artifact inventory with canonical state, and the access filters that bound what any searcher may see.
- **Owns**: the query analysis over a stated window covering top queries, zero-result queries, and queries that return results nobody opens, which is the more damaging of the two failures because it looks like success; the mapping from failing queries to their cause across missing content, wrong vocabulary, poor titling, unindexed corpus, and access filtering; synonym and variant configuration derived from the vocabulary rather than guessed; title and heading remediation for the artifacts that exist and lose, since most search failures in an internal corpus are retrieval of the wrong existing page rather than absence; best bets curated for the highest-volume questions with an owner and an expiry, because a pinned result outlives the page it points at; ranking signal review covering recency, authority, and usage; index scope naming the corpora the engine does not cover; and the search failures that are content failures, handed back to the gap ledger rather than tuned around.
- **Hands to**: `retrieval-corpus-curation-desk`.
- **Hard halt**: connector unreachable. Search analytics are the only evidence of what readers actually could not find. Relevance tuned without them is tuned against an imagined query set, and the queries that matter most are precisely the ones nobody would think to imagine.

## retrieval-corpus-curation-desk

- **Requires**: the artifact inventory with canonical state, freshness, and sensitivity, the questions an assistant is expected to answer, the access filters that must survive indexing, the structural quality of the source documents, and the retrieval query log where one exists.
- **Owns**: the eligibility decision per source with the reason for every exclusion, covering sensitivity, staleness, unresolved contradiction, unclear ownership, and format the corpus cannot chunk usefully; the authority tier that decides which source wins when two eligible sources disagree, since a retriever with no tier ranking answers from whichever chunk scored higher; the canonical answer set for the highest-volume questions, with coverage stated over the question set; the contradiction sweep across eligible content, run before admission rather than after a wrong answer is reported, because retrieval surfaces contradictions to readers one at a time with no indication that another answer exists; the document structure requirements that make a source chunkable, handed back to authoring standards where the structure is absent; the metadata every chunk must carry for filtering by audience, product, version, and currency, with the artifacts that lack it named; the refresh path by which the corpus learns a source changed, or the explicit statement that it is manual; the evaluation question set with known correct answers and the source each should be answered from; and the standing exclusion list, which is a durable governance artifact rather than a one-time cleanup.
- **Hands to**: `localization-translation-desk`.
- **Hard halt**: approval. Admitting a corpus to assistant retrieval publishes every artifact in it to every person the assistant serves, at conversational speed, without the reader seeing the source's age, its audience, or the fact that another page disagrees. That is a publishing decision at the widest audience reach in this suite, and the owner of the content makes it.

## localization-translation-desk

- **Requires**: the locale scope and the audiences behind it, the source artifacts and their revision state, the termbase and translation memory where they exist, the in-locale reviewers, and the legal or regulatory content that differs by locale rather than merely translating.
- **Owns**: the locale scope decision stating which content is translated, which is left in the source language deliberately, and why, since translating everything is how a localization program produces drift faster than it produces coverage; the source-readiness pass that removes idiom, embedded text in images, and concatenated strings before translation rather than after; the termbase with approved renderings per locale, agreed before translation begins; translation memory use and what it may not be applied to; the method per content class across human translation, machine translation with post-editing, and machine translation served raw, with the last reserved for content where being approximately right is acceptable and named as such to the reader; the in-locale reviewer per locale, because an unreviewed target is a claim in a language nobody on the team can check; legal and regulatory variants kept as separate authored content rather than as translation; and drift measured as source revisions published since each locale was last synchronized, named per locale rather than averaged.
- **Hands to**: `knowledge-governance-desk`.
- **Hard halt**: release integrity. A locale declared complete on machine output that no in-locale reviewer read is an assertion about content the organization cannot read, published to readers who will act on it. In regulated or safety-relevant content this is the failure with the shortest path from an internal shortcut to external harm.

## knowledge-governance-desk

- **Requires**: the inventory with ownership coverage, the review load the freshness stage computed, the publishing paths each platform actually enforces, the contested canonical answers awaiting adjudication, and the capacity the organization is willing to fund.
- **Owns**: the operating model naming author, reviewer, approver, and steward with a real person or role behind each; publishing authority per audience reach, so the gate scales with who reads it rather than applying uniformly; the review gates that actually block a publish, distinguished from the ones a charter describes; the ownership registry with the unowned set named rather than counted, since an unowned artifact is the input to every other failure in this suite; the contribution model stating whether capture is part of the work or an unfunded afterthought, which is the single strongest predictor of whether the corpus stays true; escalation for a contested canonical answer with a named adjudicator; the exception path for content that cannot meet the standard and the expiry on that exception; and the deliberate statement of what the program will not govern, because a model that claims the whole corpus and staffs a tenth of it produces a compliance record instead of accurate content.
- **Hands to**: `knowledge-metrics-desk`.
- **Hard halt**: approval. A governance model assigns ongoing work to named people and constrains who may publish. Both are commitments on somebody else's capacity and authority, and a model adopted without the accountable owner is a document that will be cited and not followed.

## knowledge-metrics-desk

- **Requires**: the inventory and its coverage figures, search and usage analytics with their windows, ticket and deflection data, review and ownership state, retrieval evaluation results where they exist, and the gap ledger.
- **Owns**: the measure set with a value, a denominator, the query it was computed from, and an as-of date on every figure; coverage of demand rather than count of pages, since a corpus grows most easily in the areas already covered; the gap ledger ranked by demand volume and by what a missing answer costs, with each gap classified as never written, written and unfindable, written and wrong, written and restricted, or contradicted, because those four demand different work; findability measured from query success rather than from navigation design; freshness reported as the share reviewed within its own cadence, with never-reviewed shown separately rather than folded in; quality measured against the standards conformance sample; self-service and deflection reported with the contact volume denominator and the confounders named; the measures the organization currently cannot compute and what access would make each available; and the explicit statement that page count, edit count, and contribution count measure activity rather than knowledge, so a program is not steered by the numbers that are easiest to move.
- **Hands to**: `archival-deprecation-desk`.
- **Hard halt**: release integrity. A coverage, deflection, or freshness figure with no computed basis becomes the number a program is funded and judged on, and it is quoted for years after the run that produced it. A missing measure is reported as uncomputable with the reason.

## archival-deprecation-desk

- **Requires**: the artifacts proposed for retirement with their usage and inbound references, the successor content, the link and index state, retention obligations and any legal hold, and the owner with authority over the surface.
- **Owns**: the retirement decision per artifact with its reason across superseded, obsolete system, duplicate, never used, retention expiry, and reorganization; the inbound reference enumeration covering internal links, the search and retrieval indexes, saved queries, support macros, tickets and chat citations, learning modules, and external links where referrer or link-checker data can see them; the redirect map computed as one graph rather than per page, so retirements do not produce chains or loops; the tombstone content a reader arriving at an old locator will see, which states where the answer moved rather than only that the page is gone; the archive destination that preserves version history and the retention basis that requires or permits it; the index removal step and confirmation that search and retrieval now return the successor for the queries that used to reach the retired artifact; the references that could not be updated, named with where they now point; and the deletion decision kept separate from archival, because deletion under a retention rule is irreversible and archival is not.
- **Hands to**: the orchestrator for workflow close, and back to `content-inventory-audit-desk` or `knowledge-governance-desk` where a retirement pattern reveals the corpus or the ownership model that produced the dead content.
- **Hard halt**: production or destructive. Breaking a locator, removing content from an index, or deleting an artifact is irreversible from the reader's side even when the file is recoverable, because the link in somebody's runbook, bookmark, or contract is not. The ordered sequence in `references/suite-workflow-contract.md` governs, and the owner with publishing authority executes.

---

## Packet rule

Every stage updates `knowledge_packet` as defined in `references/suite-workflow-contract.md` before handing off. Audiences, demand signals, artifacts, terms, clusters, gaps, and access rules accumulate across stages and are never dropped to keep an artifact short. An artifact removed from the inventory is removed with a reason and a date, because the inventory is read as a history of the corpus as well as a picture of it.

## Cross-suite boundary

These hand outward rather than to another desk in this suite: support article authoring, macro wording, and agent-facing troubleshooting content go to the Customer Support suite; documentation proven against code, proof maps, and doc-to-commit traceability go to the SDLC suite, along with architecture decision records for a specific system design; the data catalog, business glossary bound to physical columns, and metric definitions go to the Data suite; embedding models, chunking implementation, index configuration, reranking, and retrieval evaluation harnesses go to the AI Engineering suite; policy drafting, approval authority, and attestation go to the GRC suite; personal data handling, lawful basis, and subject rights go to the Privacy suite; employee onboarding programs and learning administration go to the People suite; public content marketing and site information architecture go to the Marketing and Web suites. Label the handoff explicitly so nobody reads those desks as members of this one.
