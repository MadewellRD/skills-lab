# CI Failure Desk

`ci-failure-desk` is a connector-grounded SDLC skill for diagnosing CI/CD failures, classifying flaky tests, reviewing pipeline health, deciding rerun versus fix, and preparing bounded downstream handoffs.

## Lifecycle coverage

Primary stage: CI/CD, build, and pipeline health.

Adjacent stages:

- Code review and change quality
- Test planning and QA strategy
- Verification, validation, and traceability
- Release planning and release operations
- Deployment, rollout, and change management
- Incident response and production support

## Intended inputs

- GitHub Actions workflow runs, jobs, logs, artifacts, checks, branch state, PR diffs, changed files, commits, and issues
- Build logs, test output, linter output, coverage reports, deployment gate failures, and local reproduction notes
- Test strategy, release policy, deployment policy, and operations documentation
- User-provided halt reports from Codex, Claude Code, or another implementation agent

## Intended outputs

- CI failure diagnostic reports
- Flaky-test triage reports
- Pipeline-health reviews
- Rerun versus fix decisions
- Minimal reproduction and evidence notes
- Release-blocking CI evidence
- Downstream handoff notes for review, verification, release, incident, issue-planning, and PR-command workflows

## Required connectors

GitHub is required for repo-specific workflow, check, branch, commit, PR, issue, changed-file, Actions run, job, log, artifact, or status claims. Document connectors or uploaded files are required for release policy, test strategy, required-check policy, and deployment policy claims.

## Composition with Implementation Handoff Desk

Use this skill to diagnose and bound CI failures. Use `implementation-handoff-desk` when the diagnosis needs to become an implementation-agent prompt, halt-resume prompt, merge-train runbook, or fix PR handoff.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
