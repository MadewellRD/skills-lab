# Retrieval Quality Checklist

## Required validation slices

- Precision: retrieved chunks are relevant to the query and answer.
- Recall: expected source material is retrievable.
- Grounding: answer claims are supported by retrieved sources.
- Citation accuracy: citations point to the source that supports the claim.
- Freshness: stale sources are filtered, flagged, or ranked appropriately.
- Permission filtering: users cannot retrieve unauthorized or cross-tenant content.
- Source conflict: conflicting sources are disclosed or escalated.
- Abstention: the system refuses or defers when retrieved evidence is insufficient.
- Prompt injection in retrieved content: malicious retrieved instructions do not override system/tool boundaries.
- Observability: query, selected chunks, scores, filters, citations, latency, and token usage are traceable with privacy controls.

## Red flags

Return `Workflow Halt` when corpus ownership, access rules, freshness policy, or retrieval eval requirements are unknown for release-bound work.
