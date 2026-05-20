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

## Desk families

### Orchestration

- `ai-engineering-command-desk`: classify workflow mode, build stage sequence, preserve packet, advance stages, halt only on missing facts, connector limits, approvals, or source conflicts.

### Design and architecture

- `model-selection-desk`: compare model candidates, routing, fallback, context, modality, latency, cost, safety, and provider constraints.
- `prompt-systems-desk`: define prompt hierarchy, context assembly, prompt contracts, refusal/defer behavior, prompt fixtures, and regression expectations.
- `tool-schema-design-desk`: define schemas, auth, permission boundaries, destructive-action gates, idempotency, retries, audit, and error contracts.
- `agent-architecture-desk`: choose deterministic pipeline, assistant, single-agent, or multi-agent architecture; define state, memory, approvals, observability, and halts.
- `retrieval-rag-design-desk`: define corpus, permissions, chunking, embeddings, retrieval/ranking, citations, freshness, grounding, and evals.

### Data and evaluation

- `dataset-curation-desk`: define provenance, rights, privacy, labels, splits, deduplication, drift, and retention.
- `synthetic-data-desk`: define generation constraints, diversity, review, contamination prevention, and usage limits.
- `eval-design-desk`: define eval goals, datasets, rubrics, graders, thresholds, slices, safety cases, and reporting.
- `eval-run-analysis-desk`: analyze pass/fail, deltas, failures, grader reliability, release blockers, and reruns.
- `fine-tuning-desk`: justify fine-tuning only after prompt/RAG/tool/routing alternatives and eval evidence are assessed.

### Safety, release, and operations

- `ai-safety-review-desk`: map risks and mitigations using NIST-style Govern/Map/Measure/Manage language and OWASP LLM/agent risk surfaces.
- `red-team-eval-desk`: adversarially test jailbreaks, prompt injection, tool misuse, data exfiltration, harmful actions, and policy evasion.
- `inference-ops-desk`: define runtime topology, quotas, fallbacks, retries, caching, batching, secrets, logging, SLOs, and rollback.
- `agent-observability-desk`: define traces, model calls, prompt/tool/retrieval events, metrics, dashboards, alerts, privacy, and runbooks.
- `cost-latency-optimization-desk`: optimize with baseline metrics and preserve quality, safety, grounding, and release gates.
- `ai-release-readiness-desk`: decide go/no-go using requirements, evals, safety, red team, ops, observability, rollback, docs, support, and approval.
- `ai-incident-response-desk`: triage incidents, preserve evidence, contain, rollback, mitigate, create follow-ups, and feed post-incident review.

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
