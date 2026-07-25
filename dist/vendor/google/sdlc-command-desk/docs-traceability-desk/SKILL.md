---
name: docs-traceability-desk
description: create connector-grounded documentation traceability, proof maps, claim maps, knowledge indexes, doc-code consistency reports, evidence packets, and downstream handoff notes from repositories, product docs, architecture specs, tests, pull requests, issues, and status documents. use when Gemini needs to prove documentation claims against source facts, map requirements to docs and code, identify stale or unsupported docs, prepare proof-map updates, or generate audit-ready documentation artifacts for sdlc workflows.
---

# Docs Traceability Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to turn scattered documentation, repository facts, requirements, tests, issues, and pull requests into traceable documentation artifacts. The skill verifies claims against source evidence, identifies unsupported or stale docs, builds proof maps, and prepares downstream handoff notes for `implementation-handoff-desk`, `verification-desk`, `review-quality-desk`, or `issue-planning-desk`.

This skill is evidence-first. It must not invent source facts, test names, file paths, PR numbers, issue IDs, status claims, or implementation coverage.

## Workflow

**Outcome.** The documentation artifact the request calls for: a proof map or claim map, a documentation update plan, a doc-code consistency report, a knowledge index or source catalog, an audit evidence packet, or a downstream handoff note for a PR, verification, or issue-planning workflow.

**Grounding.** Use GitHub for repo files, commits, PRs, issues, tests, code paths, and CI facts. Use docs connectors or uploaded docs for product, roadmap, architecture, status, parity, audit, and decision documents. Use communication connectors only for decision history or halt reports that are not captured in repo or docs.

**Claim extraction.** Use `references/claim-map-template.md` for claim-level mapping and `references/proof-map-template.md` for source-backed proof tables. Every claim must be assigned exactly one of `supported`, `partially supported`, `unsupported`, `stale`, `conflicting`, or `unverified`.

**Doc-code consistency.** Compare documentation claims against source files, tests, issue/PR state, and current repository structure. Use `references/doc-code-consistency.md` to classify drift and impact.

**Parallel surface.** Individual claims are independent units of work: each is checked against its own evidence and no claim's status depends on another's. Extract and evaluate claims in parallel, and retrieve the documents and repository paths backing them in parallel too. Fan out across documents rather than walking them one at a time.

**Artifact production.** Follow `references/output-contract.md`. For prompts, reports, plans, indexes, and handoff notes, create a downloadable Markdown artifact when file-writing tools are available. Include source facts and unverified assumptions.

**Downstream handoff.** Do not write implementation PR prompts unless asked. Produce handoff notes with target files, source evidence, risk, acceptance gates, and halt conditions that `implementation-handoff-desk` can convert into a PR prompt.

**Acceptance bar.** The artifact is done when every extracted claim carries a status and a named source artifact for that status; unsupported, stale, and conflicting claims are visible rather than smoothed over; conflicts are preserved instead of resolved silently; and each unsupported or unverified claim names the next evidence-gathering step. Do not invent source facts, test names, file paths, PR numbers, issue IDs, status claims, or implementation coverage.

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

## Halt policy

Proceed by default. A claim that cannot be proven is a result, not a blocker: mark it `unsupported` or `unverified`, name the missing evidence, and continue mapping the rest. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval** — the request would publish, overwrite, or retire documentation that a human owner must authorize.
- **Production or destructive** — the plan would delete or rewrite canonical source-of-truth documents rather than propose changes.
- **Security or privacy** — proving a claim would require reproducing secrets, credentials, or personal data in the artifact.
- **Source conflict** — documentation and repository state genuinely disagree on a load-bearing fact. Record it as `conflicting` and halt rather than picking a side.
- **Release integrity** — an audit or evidence packet would assert coverage that available evidence cannot establish.
- **Connector unreachable** — a required repo or doc source exists but cannot be read. Evidence that is merely absent is a soft gap: produce a connector diagnostic or continue with the claim marked `unverified`.

## Quality bar

Every traceability artifact must separate facts from inference, cite or name source artifacts, mark unsupported claims clearly, and preserve conflicts rather than smoothing them over. When a doc says something that the repo cannot prove, label it as unsupported or unverified and recommend the next evidence-gathering step.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
