# Security Threat Desk

`security-threat-desk` is a connector-grounded SDLC skill for defensive security review and threat modeling.

## Lifecycle coverage

Primary stage: security, privacy, and threat modeling.

Adjacent stages:

- Technical discovery
- Architecture and solution design
- API and integration contract design
- Code review and quality gates
- Verification and release readiness
- CI/CD and dependency health

## Intended inputs

- PRDs, SRS documents, architecture specs, ADRs, and API contracts
- GitHub repositories, PRs, changed files, dependency manifests, workflow files, issues, and commits
- Security, compliance, privacy, and data classification docs
- User-provided incident notes, audit findings, or review concerns

## Intended outputs

- Threat models
- Security review reports
- Trust-boundary and data-flow reviews
- Dependency, secrets, and supply-chain risk reviews
- Mitigation backlogs
- Release blocker notes
- Downstream handoff notes for planning, verification, review, and PR command workflows

## Required connectors

GitHub is required for repo-specific code, dependency, PR, issue, workflow, or CI claims. Document connectors or uploaded files are required for requirements, architecture, compliance, privacy, and policy claims.

## Composition with Implementation Handoff Desk

Use this skill to identify security risks and mitigations. Use `implementation-handoff-desk` when those mitigations need to become implementation-agent PR prompts, halt-resume prompts, merge-train runbooks, or docs/proof handoff files.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
