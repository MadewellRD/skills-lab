# Docs Traceability Desk

`docs-traceability-desk` creates source-backed documentation traceability artifacts for SDLC workflows.

## Lifecycle coverage

- Documentation, knowledge management, and proof maps.
- Compliance, audit, and governance evidence support.
- Verification and review support when docs must match implementation.

## Intended inputs

- Product requirements and acceptance criteria.
- Architecture, design, status, parity, roadmap, and audit docs.
- GitHub repository files, tests, issues, pull requests, commits, and CI status.
- Existing documentation that may be stale, unsupported, or incomplete.
- User-provided notes or uploaded docs.

## Intended outputs

- Proof maps.
- Claim maps.
- Doc-code consistency reports.
- Knowledge indexes.
- Documentation update plans.
- Audit evidence packets.
- Handoff notes for `implementation-handoff-desk`, `verification-desk`, `review-quality-desk`, or `issue-planning-desk`.

## Required connectors

GitHub is required when claims depend on repository state, code paths, tests, issues, pull requests, commits, or CI. Document connectors or uploaded docs are required when claims depend on product, roadmap, architecture, status, parity, compliance, or audit material. Communication connectors are optional and should be used only for decision history that is not captured elsewhere.

## Composition with Implementation Handoff Desk

This skill prepares evidence and scoped documentation change notes. Use `implementation-handoff-desk` after this skill when a documentation update, proof-map amendment, parity doc correction, or code-backed documentation PR prompt must be created.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
