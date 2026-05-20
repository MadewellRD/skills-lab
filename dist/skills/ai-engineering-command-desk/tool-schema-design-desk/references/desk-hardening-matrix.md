# AI Engineering Desk Hardening Matrix

## Purpose

This matrix defines the minimum hardening expectations for the AI Engineering Command Desk suite. It keeps the suite aligned to SDLC Command Desk taxonomy while allowing AI-specific evidence, safety, eval, and operations terms.

## Suite-level requirements

Every desk must include:

- SDLC-style source hierarchy.
- Required evidence before action.
- Workflow packet fields.
- Hard halt and soft gap behavior.
- Downstream handoff targets.
- Low-token execution policy.
- Continuity Kernel Adoption.
- Validation gates when the desk emits implementation or release work.

## Design and architecture desk expectations

- `model-selection-desk`: compare model candidates, routing, fallback, context, modality, latency, cost, safety, and provider constraints.
- `prompt-systems-desk`: define prompt hierarchy, context assembly, prompt contracts, refusal/defer behavior, prompt fixtures, and regression expectations.
- `tool-schema-design-desk`: define schemas, auth, permission boundaries, destructive-action gates, idempotency, retries, audit, and error contracts.
- `agent-architecture-desk`: choose deterministic pipeline, assistant, single-agent, or multi-agent architecture; define state, memory, approvals, observability, and halts.
- `retrieval-rag-design-desk`: define corpus, permissions, chunking, embeddings, retrieval/ranking, citations, freshness, grounding, and evals.

## Validation expectation

A desk is not hardened if a downstream coding agent must infer:

- target repo or base branch
- source facts
- allowed and forbidden files
- validation commands
- acceptance criteria
- safety gates
- report paths
- PR title/body expectations
- stop line

Desk output must make those items explicit or return `Workflow Halt`.
