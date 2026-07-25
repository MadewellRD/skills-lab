# AI Engineering Standards Source Map

## Purpose

This reference records external standards and industry patterns used to harden the AI Engineering Command Desk suite. It is an authoring map for desk behavior, evidence requirements, halt conditions, and validation gates.

## Safety and risk management

- NIST AI Risk Management Framework: use Govern, Map, Measure, and Manage as the safety-review operating frame.
- OWASP Top 10 for LLM Applications: use prompt injection, sensitive information disclosure, supply-chain risk, excessive agency, system prompt leakage, and model denial-of-service as red-team and safety-review surfaces.
- OWASP Agentic AI guidance: use agent identity, memory, tool access, authorization, and human approval boundaries when designing agent architecture and tool schemas.

## Evaluation and release evidence

- Require representative datasets, rubrics, baseline comparisons, pass/fail thresholds, safety slices, and regression reporting.
- Release-readiness desks must treat eval evidence, safety review, red-team status, inference operations, observability, rollback, and owner approval as launch gates.

## Observability

- Instrument model calls, prompts where safe, completions where safe, token counts, latency, tool calls, retrieval events, errors, and model/provider metadata.
- Observability desks must account for privacy, redaction, access controls, retention, incident forensics, and dashboard ownership.

## Data and retrieval

- Dataset and RAG desks must preserve provenance, rights, privacy classification, splits, contamination controls, freshness, permission filtering, and citation policy.
- Synthetic data is a supplement, not proof of production behavior, unless independently validated.

## Source precedence

1. Repo evidence, eval results, telemetry, issues, PRs, and release records are authoritative for implementation and production state.
2. User-provided goals and approval decisions define scope and risk tolerance.
3. Official standards and vendor docs define domain constraints and current best practice.
4. Practitioner articles can inform heuristics but cannot override repo evidence or official standards.
