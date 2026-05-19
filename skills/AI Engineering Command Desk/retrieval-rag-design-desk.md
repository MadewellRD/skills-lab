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

- Classify knowledge needs and corpus boundaries.
- Design ingestion, chunking, indexing, ranking, and filtering.
- Define citation, freshness, and permission behavior.
- Map retrieval evals and failure cases.
- Document operational update and rollback expectations.

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

- Source permissions, corpus ownership, or freshness rules are unclear.
- No eval data exists for retrieval quality.
- The design could expose private or cross-tenant content.

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
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
