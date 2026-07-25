# AI Engineering Stage Routing Checklist

## Routing checks

- Model unclear or disputed: route to `model-selection-desk`.
- Prompt behavior unclear: route to `prompt-systems-desk`.
- Tools, MCP resources, connectors, or external actions involved: route to `tool-schema-design-desk`.
- Autonomous loop, memory, state, delegation, or approval behavior involved: route to `agent-architecture-desk`.
- Private, changing, cited, or permission-filtered knowledge involved: route to `retrieval-rag-design-desk`.
- Dataset source, labels, splits, rights, privacy, or provenance involved: route to `dataset-curation-desk`.
- Synthetic examples, diversity targets, or contamination controls involved: route to `synthetic-data-desk`.
- Acceptance gates or regression coverage missing: route to `eval-design-desk`.
- Completed eval results need interpretation: route to `eval-run-analysis-desk`.
- Fine-tuning proposed: route to `fine-tuning-desk` only after alternatives and eval evidence are explicit.
- Safety, misuse, privacy, data leakage, or high-impact behavior involved: route to `ai-safety-review-desk`.
- Jailbreak, prompt injection, exfiltration, or tool misuse risk involved: route to `red-team-eval-desk`.
- Production runtime, quotas, retries, caching, fallbacks, or SLOs involved: route to `inference-ops-desk`.
- Traces, prompts, tool calls, retrieval events, dashboards, or alerts involved: route to `agent-observability-desk`.
- Cost, latency, throughput, or quota optimization involved: route to `cost-latency-optimization-desk`.
- Launch or rollout decision involved: route to `ai-release-readiness-desk`.
- Production failure or user harm report involved: route to `ai-incident-response-desk`.

## Hard halts

Return `Workflow Halt` when the target repo, source evidence, approval owner, risk tier, validation gate, or required connector is missing and cannot be inferred safely.
