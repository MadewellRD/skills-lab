# Install and Use SDLC Command Desk Skills

This guide explains how to use the SDLC Command Desk skill suite from this repository.

## What you need

- ChatGPT with Skills support.
- The packaged skill archives from this repository or a GitHub Release.
- GitHub connector access if you want repository-grounded behavior.
- Optional document or communication connectors for product docs, roadmap docs, decisions, support tickets, or operational evidence.

## Recommended install order

Install the top-level router first, then install the lifecycle desks.

```text
000-sdlc-command-desk-skill.zip
001-product-requirements-desk-skill.zip
002-technical-discovery-desk-skill.zip
003-architecture-design-desk-skill.zip
004-issue-planning-desk-skill.zip
005-implementation-handoff-desk-skill.zip
006-review-quality-desk-skill.zip
007-test-strategy-desk-skill.zip
008-verification-desk-skill.zip
009-docs-traceability-desk-skill.zip
010-security-threat-desk-skill.zip
011-ci-failure-desk-skill.zip
012-release-operations-desk-skill.zip
013-deployment-desk-skill.zip
014-observability-readiness-desk-skill.zip
015-incident-response-desk-skill.zip
016-maintenance-refactor-desk-skill.zip
017-retrospective-desk-skill.zip
018-decommissioning-desk-skill.zip
```

## Upload rule

Each ChatGPT skill upload should contain one valid skill directory with one `SKILL.md` entrypoint.

The upload-facing filename may be `skill.zip`. For repository and release organization, descriptive ordered filenames are used.

## Basic use

Start with `sdlc-command-desk` when you are not sure which lifecycle stage applies.

Example:

```text
Use SDLC Command Desk to classify this work and route me to the right lifecycle desk: I want to add a paid team workspace feature to my app.
```

Use a specific desk when you already know the stage.

Examples:

```text
Use product-requirements-desk to turn this idea into a PRD with requirement IDs and acceptance criteria.
```

```text
Use technical-discovery-desk to inspect this repo and produce a feasibility/risk memo before implementation.
```

```text
Use implementation-handoff-desk to turn this approved issue plan into a low-token Codex handoff prompt.
```

## Connector setup

For best results, enable GitHub access for the target repositories before asking for implementation, review, CI, release, or incident work.

GitHub should be used for:

- repository files
- branches
- commits
- pull requests
- issues
- changed files
- CI/check status
- workflow logs
- test names and source facts

Docs and communication connectors can be used for:

- roadmap context
- product decisions
- architecture notes
- stakeholder decisions
- audit evidence
- support/customer signals
- release and operational context

## Expected behavior

The skills should reduce ambiguity before work reaches a coding agent.

A good implementation handoff should include:

- exact objective
- exact scope
- known files or modules
- allowed and forbidden changes
- validation commands
- halt conditions
- PR title/body requirements
- evidence/source facts

## Halt behavior

The skills should halt or produce a connector diagnostic when required facts are missing.

They should not invent:

- repository state
- branch names
- commit SHAs
- issue IDs
- pull request numbers
- test names
- CI/check status
- acceptance criteria
- release or rollback status

## Verification

If release archives include checksums, verify downloaded artifacts before upload.

PowerShell example:

```powershell
Get-FileHash .\000-sdlc-command-desk-skill.zip -Algorithm SHA256
```

Compare the hash with `CHECKSUMS.txt`.

## Suggested first workflow

1. Use `sdlc-command-desk` to classify the work.
2. Use `product-requirements-desk` for PRD and acceptance criteria.
3. Use `technical-discovery-desk` for feasibility and repo constraints.
4. Use `architecture-design-desk` for design and interfaces.
5. Use `issue-planning-desk` for GitHub-ready issues.
6. Use `implementation-handoff-desk` for the coding-agent prompt.
7. Use review, test, verification, security, CI/CD, release, deployment, and operations desks as the work matures.
