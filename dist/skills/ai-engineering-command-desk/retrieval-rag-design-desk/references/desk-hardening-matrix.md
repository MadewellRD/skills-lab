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

## Retrieval/RAG expectations

`retrieval-rag-design-desk` must define corpus, permissions, chunking, embeddings, retrieval/ranking, citations, freshness, grounding, and evals.

## Validation expectation

A desk is not hardened if a downstream coding agent must infer target repo, source facts, allowed files, validation commands, acceptance criteria, safety gates, report paths, PR title/body expectations, or stop line.

Desk output must make those items explicit or return `Workflow Halt`.
