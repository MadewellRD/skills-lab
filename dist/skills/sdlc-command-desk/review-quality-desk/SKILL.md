---
name: review-quality-desk
description: create connector-grounded pull request review, diff risk, quality gate, missing-test, scope creep, and approve/comment/request-changes recommendations from github prs, changed files, checks, tests, code ownership, issues, and review comments. use when the assistant needs to review a pr, assess implementation quality, identify regressions, draft review comments, summarize risk, verify acceptance criteria, or prepare review handoff notes for implementation-handoff-desk.
---

# Review Quality Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to review software changes with evidence from GitHub and project source facts. The skill produces review decisions, risk-tagged findings, missing-test assessments, quality-gate summaries, and concise review comments.

This skill does not implement fixes. When a change needs coding work, continue into the implementation handoff stage as a follow-up PR or halt-resume prompt when facts are sufficient.

## Connector-first workflow

**Outcome.** One of the output artifacts in `references/output-contract.md`, carrying a review decision, risk-tagged findings, and evidence blocks or source notes for every source-dependent claim.

**Review target.** Establish what is under review — PR number, branch, commit range, patch, or pasted diff — before drawing conclusions about it.

**Grounding.** Run connector preflight using `references/connector-routing.md` and establish source hierarchy using `references/source-hierarchy.md`. Inspect PR metadata, changed files, patch, checks, linked issue, review comments, and relevant code paths when available. Compare the change against stated requirements, acceptance criteria, tests, docs, and existing project conventions.

**Parallel surface.** Changed files, hunks, findings, and check results are independent review units — no file's assessment depends on another's. Read the changed files and evaluate findings in parallel rather than walking the diff serially. Reserve a single pass at the end for cross-file concerns: blast radius, scope creep against the linked issue, and contradictory findings.

**Acceptance bar.** The review is done when the decision is one of the four below and is defensible from cited evidence; every substantive finding carries severity, category, evidence, impact, and an exact recommended action; findings are anchored to a file and line where a specific line is at fault; and acceptance criteria from the linked issue are each addressed or explicitly noted as unverifiable. A review that lists observations without a decision is incomplete.

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

A full review of a PR delivers the set, not one report drawn from it:

- `pr-review-report.md` — the decision and the findings behind it.
- `diff-risk-assessment.md` — blast radius, regression surface, and scope creep against the linked issue.
- `missing-test-assessment.md` — what the change alters and what does not cover it.
- `quality-gate-summary.md` — check state, acceptance criteria, and what each gate rests on.
- `review-comment-plan.md` — the comments to leave, anchored to file and line wherever a specific line is at fault.

`review-to-pr-command-handoff.md` is genuinely conditional: it exists to convert requested changes into follow-up implementation work, so it is produced on a `request changes` decision or when the user asks for the follow-up, and is correctly absent from an `approve`.

For user-facing artifacts, follow `references/output-contract.md` and create downloadable Markdown when file tools are available. Use `scripts/write_review_markdown.py` when a deterministic wrapper is useful.

Depth is the difference between a review and a reaction. Every finding carries severity, category, evidence, impact, and the exact next action. The risk assessment names the callers and paths the change reaches. The missing-test assessment names the specific behavior left uncovered rather than saying more tests are needed. A findings list with no decision, or a decision with no findings supporting it, is incomplete either way.

Changed files, hunks, and findings are independent review units, so the artifacts in the set come out of parallel reading, with the single final pass reserved for cross-file concerns.

Producing five files is not a reason to produce five findings. A clean file gets no invented nit, an unreachable check is reported as unverifiable rather than assessed, and `insufficient evidence` remains a legitimate decision. Padding a review with speculative issues costs the author more time than a short honest one.

## Halt behavior

Proceed by default. Review a diff you can see even when surrounding context is thin: state what could not be assessed, label the assumption, and issue the decision the evidence supports. `insufficient evidence` is a review decision, not a halt, and is the right answer when the diff itself cannot be read. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval** — the user asks this desk to submit an approving review or merge, rather than produce the review material.
- **Production or destructive** — acting on the review would push, merge, or close work rather than comment on it.
- **Security or privacy** — the diff exposes secrets or credentials, or reviewing it further would require handling personal data.
- **Source conflict** — connector facts conflict with pasted context on a load-bearing point such as what the diff actually contains.
- **Release integrity** — an `approve` would be issued while required checks are red, stale, or unverifiable.
- **Connector unreachable** — the PR or diff exists but cannot be fetched. Missing linked acceptance criteria or absent review comments are soft gaps: review what is present and mark the unverified dimensions.

Follow `references/halt-conditions.md` for the halt artifact format.

## Composition with other SDLC skills

- Consume PRDs from `product-requirements-desk` when validating acceptance criteria.
- Consume technical discovery or architecture outputs when reviewing implementation risk.
- Consume issue plans from `issue-planning-desk` when checking scope and sequencing.
- Hand off follow-up implementation work to `implementation-handoff-desk`.
- Hand off formal traceability and release evidence to `verification-desk` or `docs-traceability-desk`.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
