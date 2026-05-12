# Review Quality Desk

`review-quality-desk` is an SDLC skill for connector-grounded PR review, diff risk assessment, missing-test analysis, and quality-gate summaries.

## Lifecycle coverage

Primary stage: code review and change quality.

Adjacent stages: test planning, verification, CI triage, security review, docs traceability, and PR command handoff.

## Intended inputs

- GitHub PR number, branch, commit range, changed files, or patch.
- Linked GitHub issue, acceptance criteria, or PRD/SRS excerpts.
- CI/check status, test output, review comments, and ownership/style docs.
- Pasted diff or local review notes when connectors are unavailable.

## Intended outputs

- PR review report.
- Approve/comment/request-changes recommendation.
- Risk-tagged findings.
- Missing-test assessment.
- Inline comment plan.
- Quality-gate summary.
- Follow-up handoff notes for `implementation-handoff-desk`.

## Required connectors

GitHub is required for live PR review: PR metadata, diff, changed files, checks, comments, linked issues, and code context.

Document connectors are required when review depends on PRDs, specs, design docs, security policy, release criteria, or architecture decisions.

## Composition

Use `review-quality-desk` before merge. If the review finds follow-up implementation work, pass its findings to `implementation-handoff-desk` to create a bounded PR or halt-resume prompt.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
