---
name: review-quality-desk
description: create connector-grounded pull request review, diff risk, quality gate, missing-test, scope creep, and approve/comment/request-changes recommendations from github prs, changed files, checks, tests, code ownership, issues, and review comments. use when chatgpt needs to review a pr, assess implementation quality, identify regressions, draft review comments, summarize risk, verify acceptance criteria, or prepare review handoff notes for implementation-handoff-desk.
---

# Review Quality Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to review software changes with evidence from GitHub and project source facts. The skill produces review decisions, risk-tagged findings, missing-test assessments, quality-gate summaries, and concise review comments.

This skill does not implement fixes. When a change needs coding work, continue into the implementation handoff stage as a follow-up PR or halt-resume prompt when facts are sufficient.

## Connector-first workflow

1. Identify the review target: PR number, branch, commit range, patch, or pasted diff.
2. Run connector preflight using `references/connector-routing.md`.
3. Establish source hierarchy using `references/source-hierarchy.md`.
4. Inspect the PR metadata, changed files, patch, checks, linked issue, review comments, and relevant code paths when available.
5. Compare the change against stated requirements, acceptance criteria, tests, docs, and existing project conventions.
6. Produce one of the output artifacts in `references/output-contract.md`.
7. Include evidence blocks or source notes for all source-dependent claims.

## Review decision model

Use one of these final decisions:

- `approve`: changes are correct, scoped, tested, and low risk.
- `comment`: changes are mostly acceptable but need non-blocking clarification or follow-up.
- `request changes`: changes contain correctness, safety, regression, security, data-loss, test-coverage, or scope-control issues that should block merge.
- `insufficient evidence`: required connector facts, tests, or acceptance criteria are missing.

Do not approve a PR from style preference alone. Do not request changes for speculative issues without evidence.

## Required review dimensions

Assess these dimensions when relevant:

- Scope alignment against linked issue, prompt, PR body, or acceptance criteria.
- Correctness and edge cases.
- Regression risk and changed-file blast radius.
- Test adequacy, including missing unit, integration, regression, fixture, or manual validation coverage.
- Security, privacy, authorization, secrets, and dependency risk.
- Performance and reliability impact.
- Data/schema/API compatibility.
- Documentation and migration requirements.
- CI/check status and local verification evidence.
- Maintainability, readability, and project convention alignment.

## Finding format

Every substantive finding must include:

- Severity: `blocking`, `major`, `minor`, or `note`.
- Category: correctness, test coverage, security, performance, compatibility, maintainability, docs, process, or scope.
- Evidence: file, line, diff hunk, check, issue, or source fact.
- Impact: why it matters.
- Recommendation: exact next action.

Use inline review comments only when the finding points to a specific changed line. Otherwise use a top-level review summary.

## Output rules

For user-facing artifacts, follow `references/output-contract.md` and create downloadable Markdown when file tools are available. Use `scripts/write_review_markdown.py` when a deterministic wrapper is useful.

Default artifact names:

- `pr-review-report.md`
- `diff-risk-assessment.md`
- `missing-test-assessment.md`
- `review-comment-plan.md`
- `quality-gate-summary.md`
- `review-to-pr-command-handoff.md`

## Halt behavior

Follow `references/halt-conditions.md`. Halt or mark the review as `insufficient evidence` when required source facts are unavailable, the PR cannot be fetched, the diff is missing, linked acceptance criteria are unavailable, checks are stale, or connector facts conflict with pasted context.

## Composition with other SDLC skills

- Consume PRDs from `product-requirements-desk` when validating acceptance criteria.
- Consume technical discovery or architecture outputs when reviewing implementation risk.
- Consume issue plans from `issue-planning-desk` when checking scope and sequencing.
- Hand off follow-up implementation work to `implementation-handoff-desk`.
- Hand off formal traceability and release evidence to `verification-desk` or `docs-traceability-desk`.
