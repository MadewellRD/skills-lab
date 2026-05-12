# Verification Desk

`verification-desk` is an SDLC skill for creating connector-grounded verification and validation artifacts. It maps requirements to evidence, assesses acceptance gates, identifies release blockers, and prepares handoff notes for implementation, docs, or release work.

## Inputs

- PRD, SRS, SDS, design specs, acceptance criteria, and issue bodies
- GitHub PRs, commits, changed files, checks, and test files
- CI logs, test output, QA notes, screenshots, and release artifacts
- Review findings and test strategy documents

## Outputs

- V&V report
- Requirements traceability matrix
- Acceptance-gate review
- Release-blocker report
- Evidence map
- Downstream handoff notes

## Required connectors

- GitHub for repo, PR, commit, check, and test evidence
- Document or uploaded-file sources for requirements and design artifacts
- Issue/project sources when acceptance criteria are ticket-based
- CI/log/artifact access when gate status is being assessed

## Composition

This skill consumes outputs from `product-requirements-desk`, `technical-discovery-desk`, `architecture-design-desk`, `issue-planning-desk`, `review-quality-desk`, and `test-strategy-desk`. It sends implementation follow-ups to `implementation-handoff-desk`, release readiness outputs to `release-operations-desk`, and durable evidence updates to `docs-traceability-desk`.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
