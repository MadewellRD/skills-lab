# Retrospective Desk

`retrospective-desk` creates connector-grounded retrospectives and continuous-improvement artifacts for software delivery.

## Lifecycle coverage

This skill covers SDLC stage 24: retrospective and continuous improvement. It also supports post-release, post-incident, post-PR-train, CI-quality, migration, and workflow retrospectives.

## Intended inputs

- Sprint or milestone summaries.
- GitHub PRs, commits, issues, milestones, checks, and release history.
- Incident reports, deployment notes, CI failures, and halt reports.
- Product requirements, architecture docs, test plans, release notes, and runbooks.
- Team decisions from communication sources when available.

## Intended outputs

- Retrospective report.
- Lessons-learned memo.
- Cycle-metrics summary.
- Process-improvement plan.
- Action-item tracker.
- Follow-up issue or PR handoff notes.
- Open-question and unresolved-risk log.

## Required connectors

Use GitHub when the retrospective depends on repository, PR, issue, milestone, review, commit, or CI facts. Use documentation connectors when the retrospective depends on plans, specs, release notes, runbooks, prior retrospectives, or audit evidence. Use communication connectors when recent decisions or halt reports are needed.

## Composition with other SDLC skills

`retrospective-desk` produces improvement actions and routes follow-up work to the right downstream desk. Implementation follow-ups go to `implementation-handoff-desk`; requirement gaps go to `product-requirements-desk`; design gaps go to `architecture-design-desk`; planning gaps go to `issue-planning-desk`; test and CI gaps go to `test-strategy-desk` or `ci-failure-desk`; documentation gaps go to `docs-traceability-desk`.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
