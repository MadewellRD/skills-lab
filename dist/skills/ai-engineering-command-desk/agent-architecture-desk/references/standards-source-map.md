# AI Engineering Standards Source Map

## Purpose

This reference records the external standards and industry patterns used to harden the AI Engineering Command Desk suite. It is not a citation store for generated answers; it is an authoring map for desk behavior, evidence requirements, halt conditions, and validation gates.

## Safety and risk management

- NIST AI Risk Management Framework: use Govern, Map, Measure, and Manage as the safety-review operating frame.
- OWASP Top 10 for LLM Applications: use prompt injection, sensitive information disclosure, supply-chain risk, excessive agency, system prompt leakage, and model denial-of-service as red-team and safety-review surfaces.
- OWASP Agentic AI guidance: use agent identity, memory, tool access, authorization, and human approval boundaries when designing agent architecture and tool schemas.

## Evaluation and release evidence

- OpenAI Evals, prompt/model regression testing practice, and contemporary LLM evaluation literature: require representative datasets, rubrics, baseline comparisons, pass/fail thresholds, safety slices, and regression reporting.
- Release-readiness desks must treat eval evidence, safety review, red-team status, inference operations, observability, rollback, and owner approval as launch gates.

## MLOps and LLMOps

- Google MLOps continuous delivery patterns: treat ML/AI systems as pipelines with versioned data, model, code, tests, deployment, monitoring, and rollback.
- Microsoft, Google, and AWS LLMOps guidance: separate prompt, retrieval, tool, model, eval, deployment, and monitoring changes; do not treat a prompt update as ungoverned text editing.

## Observability

- OpenTelemetry generative AI semantic conventions: instrument model calls, prompts where safe, completions where safe, token counts, latency, tool calls, retrieval events, errors, and model/provider metadata.
- Observability desks must account for privacy, redaction, access controls, retention, incident forensics, and dashboard ownership.

## Agent architecture and tool use

- Agent workflows must distinguish deterministic pipelines, assistant workflows, single-agent loops, and multi-agent delegation.
- Tool schemas must define authorization, tenancy, destructive-action gates, idempotency, retry behavior, result semantics, and audit logs.
- Excessive agency is a hard halt unless approvals, tool scope, and observability are explicit.

## Data and retrieval

- Dataset and RAG desks must preserve provenance, rights, privacy classification, splits, contamination controls, freshness, permission filtering, and citation policy.
- Synthetic data is a supplement, not proof of production behavior, unless independently validated.

## Cost and latency

- Cost/latency work must start from baseline metrics and preserve quality, safety, and grounding thresholds.
- Optimization levers include model routing, prompt/context compression, caching, batching, retrieval tuning, streaming, and fallback tiers.

## Source precedence

1. Repo evidence, eval results, telemetry, issues, PRs, and release records are authoritative for implementation and production state.
2. User-provided goals and approval decisions define scope and risk tolerance.
3. Official standards and vendor docs define domain constraints and current best practice.
4. Practitioner articles can inform heuristics but cannot override repo evidence or official standards.
