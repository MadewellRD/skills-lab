---
name: retrieval-rag-design-desk
description: design retrieval augmented generation systems with indexing, chunking, embeddings, ranking, filters, citations, freshness policy, permission filtering, and grounding behavior.
---

# Retrieval RAG Design Desk

## Role

Design knowledge grounding for AI systems. Specify corpora, ingestion, chunking, embeddings, indexes, ranking, filters, freshness, citations, permission filtering, and answer-grounding behavior.

## Use when

- The AI capability must answer from private, changing, or cited knowledge.
- A RAG system needs design or remediation.
- Retrieval quality, freshness, or permissions are causing failures.

## Do not use when

- The model can answer safely without external knowledge.
- The corpus owner or data access policy is unknown.
- The problem is primarily prompt, model, or tool behavior.

## Required evidence

- Corpus list, owners, permissions, formats, and freshness requirements.
- Expected query types and answer citation rules.
- Embedding, index, ranking, and filter constraints.
- Eval set for retrieval precision, recall, grounding, and citation quality.

## Workflow

Produce a grounding design an implementer can build: which corpora are in scope and who owns them, how content is ingested, chunked, embedded, indexed, and ranked, how permissions filter results, and what the system must do when retrieval returns nothing usable.

Constraints:

- Permission filtering happens at retrieval time against the asking identity. Never rely on ranking, prompt wording, or post-hoc filtering to keep private or cross-tenant content out of an answer.
- Citation and freshness policy are part of the contract: state what must be cited, what staleness is tolerable, and how stale results are detected.
- Define grounding failure behavior explicitly — what the system says when evidence is absent, conflicting, or below the relevance floor. Never let an ungrounded answer pass as a grounded one.
- Never invent corpus ownership, document counts, permission models, or freshness guarantees.
- Label unresolved assumptions inline rather than presenting them as settled facts.

Corpora are independent. Per-corpus ingestion design, chunking strategy, permission mapping, freshness assessment, and format handling are parallel-safe across corpora, as is scoring retrieval eval queries. The shared ranking policy, citation contract, and relevance floor are single decisions across the system.

## Outputs

- RAG design spec
- corpus map
- retrieval eval plan
- citation policy
- freshness policy

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- corpora
- index_strategy
- ranking_policy
- permission_filters
- citation_rules
- freshness_policy

## Halt conditions

Default posture is to proceed and label the assumption inline. An undecided chunk size, embedding model, or index parameter is a soft gap: state the assumed value, mark it, and name the eval that would settle it. Halt only when one of the six hard-halt classes applies.

- Approval — a corpus would be indexed or exposed to a user population its owner has not authorized.
- Production or destructive — a reindex, schema change, or corpus migration would overwrite or invalidate an index that production traffic depends on.
- Security or privacy — the design could surface private, regulated, or cross-tenant content, or permission filtering cannot be enforced at retrieval time.
- Source conflict — corpus ownership, access policy, or freshness guarantees are documented inconsistently across sources.
- Release integrity — the system would ship with no eval capable of establishing retrieval quality, grounding, or citation correctness.
- Connector unreachable — the corpus, its permission model, or the existing index definition exists but cannot be read.

## Downstream handoffs

- eval-design-desk
- dataset-curation-desk
- agent-observability-desk
- ai-safety-review-desk
- SDLC Command Desk for implementation

## Source hierarchy

- User-provided objective, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository, issue, eval, dataset, telemetry, and release evidence are authoritative for implementation state.
- Provider documentation and external model documentation are used for model or API capabilities when internal evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of production behavior.

## Quality bar

- Preserve traceability from recommendation to source evidence.
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means every corpus carries an owner and a permission rule enforced at retrieval time, the citation and freshness policy is stated, grounding failure behavior is defined, and retrieval quality has a named eval — each traced to a source fact or a labeled assumption.
