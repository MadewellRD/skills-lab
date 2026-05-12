# Test Strategy Desk

`test-strategy-desk` creates connector-grounded SDLC test artifacts: test strategies, QA scenario matrices, regression plans, fixture plans, coverage-gap reports, and downstream verification or PR handoff notes.

## Lifecycle coverage

Primary stage: test planning and QA strategy.

Adjacent stages: requirements, architecture, issue planning, review quality, verification, CI failure triage, release readiness, and maintenance/regression work.

## Intended inputs

- Product requirements, acceptance criteria, PRDs, SRS, or issue scopes.
- Architecture specs, interface contracts, migration plans, and risk notes.
- GitHub repository test tree, changed files, PR diffs, commits, issues, and CI checks.
- Bug reports, regression notes, incident summaries, and release constraints.
- Uploaded QA plans, audit notes, or manual-test instructions.

## Intended outputs

- Test strategy document.
- QA scenario matrix.
- Regression plan.
- Fixture plan.
- Coverage-gap report.
- Verification handoff notes.
- Implementation Handoff Desk handoff notes for test implementation.

## Required connectors

- GitHub when repository files, PRs, issues, commits, tests, or CI results are part of the plan.
- Document/uploaded-file sources when requirements, design specs, QA plans, or release constraints are source-of-truth.
- Communication connectors only when recent decisions, halt reports, or bug triage context are required.

## Composition with Implementation Handoff Desk

This skill defines what must be tested and why. `implementation-handoff-desk` converts the selected test work into executable implementation-agent prompts with branch, commit, validation, and PR instructions.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
