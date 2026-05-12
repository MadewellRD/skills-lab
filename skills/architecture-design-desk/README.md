# Architecture Design Desk

`architecture-design-desk` creates connector-grounded architecture artifacts for SDLC workflows.

## Lifecycle coverage

- System and solution architecture
- Software design specifications
- Architecture decision records
- Interface contracts
- Migration planning
- Design handoff notes for implementation and verification

## Typical inputs

- PRDs, SRS docs, discovery memos, roadmap notes, and stakeholder decisions
- GitHub repository structure, code, dependency manifests, tests, prior PRs, and issues
- Existing architecture docs, ADRs, API contracts, database schemas, and integration docs

## Typical outputs

- Architecture/design spec
- ADR set
- Interface contract
- Migration plan
- Risk and tradeoff summary
- Verification implications
- Downstream handoff notes for `issue-planning-desk`, `security-threat-desk`, `verification-desk`, and `implementation-handoff-desk`

## Required connectors

GitHub is required for repo-aware design. Document connectors are required for PRD/SRS/discovery-grounded design. Issue/project connectors are required for ticket-derived scope.

## Packaging

The packaged skill archive must be named exactly `skill.zip`.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
