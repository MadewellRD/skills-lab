# Knowledge Ops Command Desk

Source Markdown suite for knowledge operations, documentation, and information management. One orchestrator routes and runs; nineteen member desks own a real stage of the work.

The subject is the path a question takes from the person who has it to the answer they can act on: who needs to know something and to do what, what the organization has already written down, what it is called and where it sits, who holds the knowledge that was never written, what shape a good answer takes, which of the four contradictory pages is canonical, whether the procedure still matches the system it operates, who is allowed to read it, what a retriever may serve from it, what it says in the other seven languages, who owns keeping it true, and when it should stop existing.

Support article authoring and macro wording belong to the Customer Support suite; this suite owns the corpus those articles live in and whether it contradicts itself. Documentation proven against code, proof maps, and architecture decision records for a specific system belong to the SDLC suite. The data catalog and business glossary bound to physical columns belong to the Data suite. Embedding models, chunking implementation, index configuration, and retrieval evaluation harnesses belong to the AI Engineering suite; this suite owns which content is eligible to be retrieved and whether it is true, current, and permitted.

## Desks in workflow order

- `knowledge-ops-command-desk.md` (orchestrator)
- `knowledge-demand-desk.md`
- `content-inventory-audit-desk.md`
- `taxonomy-metadata-desk.md`
- `navigation-findability-desk.md`
- `authoring-standards-desk.md`
- `docs-platform-tooling-desk.md`
- `sme-capture-desk.md`
- `decision-record-desk.md`
- `runbook-procedure-desk.md`
- `onboarding-enablement-desk.md`
- `duplication-contradiction-desk.md`
- `content-freshness-lifecycle-desk.md`
- `knowledge-access-sensitivity-desk.md`
- `search-relevance-desk.md`
- `retrieval-corpus-curation-desk.md`
- `localization-translation-desk.md`
- `knowledge-governance-desk.md`
- `knowledge-metrics-desk.md`
- `archival-deprecation-desk.md`

## Workflow backbone

```text
knowledge demand
  -> content inventory and audit
  -> taxonomy and metadata
  -> navigation and findability
  -> authoring standards
  -> docs platform and tooling
  -> subject-matter-expert capture
  -> decision records
  -> runbooks and procedures
  -> onboarding and enablement
  -> duplication and contradiction
  -> content freshness and lifecycle
  -> access and sensitivity
  -> search relevance
  -> retrieval corpus curation
  -> localization and translation
  -> knowledge governance
  -> knowledge metrics
  -> archival and deprecation
```

The chain is ordered by packet dependency, not by calendar. Few workflows need every stage: a search relevance fix does not need an enablement stage, and a decision-capture practice does not need a localization stage. One entry point ignores the order entirely, because a published answer that is actively causing people to do the wrong thing enters at duplication and contradiction wherever it started. The orchestrator selects the stage path, carries the `knowledge_packet`, and records every skip with its reason.

Two dependencies are load-bearing rather than conventional. Everything downstream of taxonomy assumes a declared term set, because search synonyms, navigation facets, retrieval metadata filters, and the localization termbase all key off the same vocabulary, and two labels for one concept splits the corpus in all four at once. And nothing in search, retrieval, or localization is safe before sensitivity and audience scope are resolved per artifact, because a retriever answers from whatever it was permitted to index, and a published translation is a second copy of the same disclosure in a place the original access rule does not reach.

## How to start

Ask the command desk for the outcome, not the stage. Name the corpus, the question, or the audience; say what state things are in (greenfield, steady, mid-migration, mid-reorganization, a launch, a content freeze, or a wrong answer currently in circulation); and say how far it reaches (one team, a function, the whole organization, partners, customers, the public, a corpus an assistant answers from, or a regulated publication).

Examples: "audit the engineering wiki against what people actually search for and tell me what is missing", "four pages describe the deploy process and two of them disagree, work out which is canonical and who has to decide", "verify the on-call runbooks against the systems they operate and flag every step that has drifted", "our staff engineer leaves in six weeks, capture what only she knows", "search returns nothing for half the questions new hires ask, tell me which are content gaps and which are vocabulary", "get the policy corpus ready to be retrieved from without it answering out of a superseded page", "retire the legacy product docs without breaking the links in customer tickets".

Enter a member desk directly when you already know the stage: a taxonomy before a migration, a content audit before a platform decision, a contradiction sweep before a corpus is indexed, an access review before a space is opened to partners, or a redirect map before a retirement.

This suite audits, classifies, structures, drafts, reconciles, measures, and plans. It does not publish to a live surface, edit a page in place, merge or delete an artifact, change a URL, re-index, widen access, or push a translation; it prepares the exact change with the inbound references it breaks, the audience it reaches, and the reversal, then stops at the gate.

## Suite references

- `references/suite-workflow-contract.md`: continuity rule, action boundary, operating modes, request types, the full `knowledge_packet` field set, the source hierarchy, evidence discipline, the ordered sequences for retiring published knowledge and for a source change during a localization cycle, halt format, parallel surface, and cross-suite boundaries.
- `references/stage-contracts.md`: per-desk inputs, owned outputs, handoff target, and stage-specific hard halt.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.
