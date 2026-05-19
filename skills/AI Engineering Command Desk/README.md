# AI Engineering Command Desk

Status: source-only suite authoring pass.

The AI Engineering Command Desk suite defines workflow-linked desk source specs for designing, evaluating, releasing, and operating AI systems. It covers model selection, prompt systems, tool schemas, agent architecture, retrieval and RAG, evals, datasets, fine-tuning, safety, red-team work, inference operations, observability, cost and latency optimization, release readiness, and AI incident response.

## Repository role

This folder is the human-authored source layer for AI Engineering Command Desk desk specs:

```text
skills/AI Engineering Command Desk/
  *.md
```

Packaged ChatGPT-compatible skills are generated later under:

```text
dist/skills/ai-engineering-command-desk/<skill-slug>/
```

Do not place generated package output in this folder.

## Desk inventory

- `ai-engineering-command-desk.md` — suite orchestrator and workflow entrypoint.
- `model-selection-desk.md` — model choice, routing constraints, fallback posture, and model tradeoff evidence.
- `prompt-systems-desk.md` — prompt architecture, instruction hierarchy, context assembly, and prompt test fixtures.
- `tool-schema-design-desk.md` — tool and resource contracts, argument validation, permission boundaries, and error semantics.
- `agent-architecture-desk.md` — agent loop, planning boundary, state strategy, approval gates, and halt behavior.
- `retrieval-rag-design-desk.md` — indexing, chunking, retrieval, citation, freshness, and permission-filtered grounding.
- `eval-design-desk.md` — evaluation objectives, datasets, rubrics, thresholds, slices, and review protocol.
- `eval-run-analysis-desk.md` — completed eval analysis, failure taxonomy, regression deltas, and release implications.
- `dataset-curation-desk.md` — dataset sourcing, labeling, splits, privacy, provenance, consent, and retention.
- `synthetic-data-desk.md` — synthetic data generation, diversity controls, contamination prevention, and validation gates.
- `fine-tuning-desk.md` — fine-tuning justification, training data readiness, eval gates, rollout, and rollback.
- `inference-ops-desk.md` — production inference topology, quotas, retries, caching, secrets, logging, and SLOs.
- `ai-safety-review-desk.md` — misuse, privacy, security, hallucination harm, autonomy, and launch mitigation review.
- `red-team-eval-desk.md` — adversarial testing for jailbreaks, prompt injection, data exfiltration, and tool misuse.
- `agent-observability-desk.md` — traces, prompts, model calls, tool calls, retrieval events, state transitions, and alerts.
- `cost-latency-optimization-desk.md` — model routing, caching, context pruning, batching, retrieval tuning, and quality-preserving optimization.
- `ai-release-readiness-desk.md` — go/no-go gate for evals, safety, ops, observability, rollback, docs, and support readiness.
- `ai-incident-response-desk.md` — production AI incident triage, containment, rollback, evidence preservation, and follow-up.

## Workflow path

Default AI Engineering flow:

```text
AI capability intake
  -> model selection
  -> prompt systems
  -> tool schema design
  -> agent architecture
  -> retrieval/RAG design when grounding is required
  -> dataset curation or synthetic data when data work is required
  -> eval design
  -> eval run analysis
  -> fine-tuning only when evidence justifies it
  -> safety review and red-team eval
  -> inference ops
  -> agent observability
  -> cost/latency optimization
  -> AI release readiness
  -> AI incident response when production behavior fails
```

Not every workflow needs every stage. The orchestrator should run the shortest safe stage sequence and halt when evidence, approval, source access, or risk gates block continuation.

## Authoring rules

- Desk files are kebab-case and end in `.md`.
- Each desk source file starts with `name` and `description` frontmatter.
- Each desk defines role, evidence requirements, workflow, outputs, packet fields, halt conditions, handoffs, source hierarchy, and quality bar.
- Source specs must preserve halt behavior instead of inventing missing facts.
- Source specs should be useful for later packaging but must not contain generated package output.

## Relationship to SDLC Command Desk

AI Engineering Command Desk follows the workflow-linked suite pattern proven by SDLC Command Desk, but it does not replace SDLC. SDLC remains the canonical software-delivery lifecycle suite. AI Engineering specializes in AI system design, evaluation, safety, operation, and incident workflows, and can hand off implementation-ready work to SDLC when software changes are required.
