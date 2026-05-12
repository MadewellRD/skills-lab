---
name: docs-traceability-desk
description: create connector-grounded documentation traceability, proof maps, claim maps, knowledge indexes, doc-code consistency reports, evidence packets, and downstream handoff notes from repositories, product docs, architecture specs, tests, pull requests, issues, and status documents. use when chatgpt needs to prove documentation claims against source facts, map requirements to docs and code, identify stale or unsupported docs, prepare proof-map updates, or generate audit-ready documentation artifacts for sdlc workflows.
---

# Docs Traceability Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to turn scattered documentation, repository facts, requirements, tests, issues, and pull requests into traceable documentation artifacts. The skill verifies claims against source evidence, identifies unsupported or stale docs, builds proof maps, and prepares downstream handoff notes for `implementation-handoff-desk`, `verification-desk`, `review-quality-desk`, or `issue-planning-desk`.

This skill is evidence-first. It must not invent source facts, test names, file paths, PR numbers, issue IDs, status claims, or implementation coverage.

## Workflow

1. Classify the requested documentation task.
   - Proof map or claim map.
   - Documentation update plan.
   - Doc-code consistency report.
   - Knowledge index or source catalog.
   - Audit evidence packet.
   - Downstream handoff note for a PR, verification, or issue-planning workflow.

2. Run connector preflight.
   Use GitHub for repo files, commits, PRs, issues, tests, code paths, and CI facts. Use docs connectors or uploaded docs for product, roadmap, architecture, status, parity, audit, and decision documents. Use communication connectors only for decision history or halt reports that are not captured in repo/docs. If required facts cannot be retrieved, produce a connector diagnostic instead of a confident proof artifact.

3. Extract claims and evidence.
   Use `references/claim-map-template.md` for claim-level mapping and `references/proof-map-template.md` for source-backed proof tables. Each claim must be assigned one of: `supported`, `partially supported`, `unsupported`, `stale`, `conflicting`, or `unverified`.

4. Check doc-code consistency.
   Compare documentation claims to source files, tests, issue/PR state, and current repository structure. Use `references/doc-code-consistency.md` to classify drift and impact.

5. Produce the requested artifact.
   Follow `references/output-contract.md`. For prompts, reports, plans, indexes, and handoff notes, create a downloadable Markdown artifact when file-writing tools are available. Include source facts and unverified assumptions.

6. Prepare downstream handoff when implementation is required.
   Do not directly write implementation PR prompts unless asked. Instead, produce handoff notes with target files, source evidence, risk, acceptance gates, and halt conditions that `implementation-handoff-desk` can convert into a PR prompt.

## Default artifact types

Use the smallest artifact that satisfies the request:

- `proof-map.md` for claims tied to source evidence.
- `claim-map.md` for claim extraction and status classification.
- `doc-code-consistency-report.md` for stale or unsupported docs.
- `knowledge-index.md` for durable source catalogs.
- `documentation-update-plan.md` for scoped doc changes.
- `audit-evidence-packet.md` for governance or release evidence.
- `docs-handoff-notes.md` for downstream implementation or verification workflows.
- `connector-diagnostic.md` when grounding is insufficient.

## Required references

Load only the reference needed for the current artifact:

- `references/proof-map-template.md` for proof maps.
- `references/claim-map-template.md` for claim classification.
- `references/doc-code-consistency.md` for drift and consistency checks.
- `references/knowledge-index-template.md` for documentation/source indexes.
- `references/audit-evidence-template.md` for audit packets.
- `references/connector-routing.md` for grounding requirements.
- `references/source-hierarchy.md` for truth precedence.
- `references/output-contract.md` for artifact structure.
- `references/handoff-rules.md` for downstream PR/verification handoff.
- `references/halt-conditions.md` for stop conditions.

## Quality bar

Every traceability artifact must separate facts from inference, cite or name source artifacts, mark unsupported claims clearly, and preserve conflicts rather than smoothing them over. When a doc says something that the repo cannot prove, label it as unsupported or unverified and recommend the next evidence-gathering step.
