---
name: verification-desk
description: create connector-grounded verification and validation artifacts for software delivery. use when chatgpt needs to prove implemented work satisfies requirements, build requirements traceability matrices, assess acceptance gates, validate test and ci evidence, identify release blockers, or prepare downstream handoff notes for release, docs, review, or implementation-handoff-desk workflows.
---

# Verification Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to turn requirements, implementation evidence, test results, CI/check status, pull requests, commits, and manual QA notes into verification and validation artifacts. The skill answers: what was required, what was built, what evidence proves it, what remains unverified, and what blocks release.

## Operating rules

1. Run connector preflight before making claims.
2. Treat GitHub as source of truth for PRs, commits, changed files, checks, test names, and code evidence.
3. Treat PRDs, SRS docs, architecture/design specs, issue bodies, and acceptance criteria as requirement sources.
4. Treat CI logs, test output, screenshots, QA notes, and artifacts as evidence sources, not as requirements.
5. Separate verified facts from assumptions and gaps.
6. Halt rather than inventing requirement IDs, test results, PR status, commit SHAs, CI outcomes, or release readiness.
7. Produce downloadable Markdown artifacts when the user asks for a report, checklist, matrix, or handoff.

## Workflow

1. Classify the request:
   - V&V report
   - requirements traceability matrix
   - acceptance-gate review
   - release readiness verification
   - test evidence review
   - blocker/gap analysis
   - downstream handoff for `implementation-handoff-desk`
2. Load source requirements from PRD, SRS, issue bodies, design docs, acceptance criteria, or user-provided scope.
3. Load implementation evidence from GitHub PRs, commits, changed files, check status, test files, CI artifacts, and manual QA notes.
4. Build a requirement-to-evidence mapping using `references/rtm-template.md`.
5. Classify each requirement as `verified`, `partially verified`, `unverified`, `blocked`, or `not applicable`.
6. Identify release blockers and evidence gaps using `references/blocker-rubric.md`.
7. Produce the requested artifact using `references/vv-report-template.md` and `references/output-contract.md`.
8. Include downstream handoff notes when additional implementation, documentation, testing, or release work is required.

## Connector requirements

Use `references/connector-routing.md` to determine required sources.

Default requirements:

- GitHub is required for repo-aware verification, PR validation, changed-file review, commit evidence, test discovery, and check status.
- Document sources or uploaded files are required when the verification depends on PRD, SRS, SDS, architecture, release, or audit documents.
- Issue/project connectors are required when acceptance criteria live in tickets.
- CI/log/artifact access is required when the user asks whether a gate passed.
- Communication sources are optional and should only be used for decision context or manual QA notes.

## Output artifacts

Default outputs:

- `verification-report.md`
- `requirements-traceability-matrix.md`
- `acceptance-gate-review.md`
- `release-blocker-report.md`
- `evidence-map.md`
- `verification-handoff.md`

Use `scripts/write_verification_markdown.py` when a wrapped Markdown file is useful.

## Quality bar

Every verification artifact must include:

- source facts used
- requirement inventory
- evidence inventory
- requirement-to-evidence mapping
- pass/fail/partial status
- gaps and blockers
- assumptions explicitly marked
- recommended next action

Do not mark work as verified unless there is direct evidence. Passing CI alone is not proof that every requirement is satisfied. A merged PR alone is not proof of validation.

## Composition with other SDLC skills

- Consume PRD output from `product-requirements-desk`.
- Consume technical and architecture evidence from `technical-discovery-desk` and `architecture-design-desk`.
- Consume issue plans from `issue-planning-desk`.
- Consume review findings from `review-quality-desk`.
- Consume test strategy and gap findings from `test-strategy-desk`.
- Send implementation follow-ups to `implementation-handoff-desk`.
- Send release-ready outputs to `release-operations-desk`.
- Send proof/doc updates to `docs-traceability-desk`.

## Halt behavior

Use `references/halt-conditions.md`. Halt or produce a connector diagnostic when required sources are missing, requirement identity is ambiguous, evidence conflicts, CI status cannot be verified, or release readiness would require unsupported assumptions.
