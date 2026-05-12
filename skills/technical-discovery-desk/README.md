# Technical Discovery Desk

`technical-discovery-desk` is a connector-grounded SDLC skill for early technical investigation. It creates technical discovery memos, repo reconnaissance reports, feasibility assessments, spike plans, risk registers, and downstream handoff notes.

## Lifecycle coverage

Primary stage: technical discovery and feasibility.

Adjacent stages:

- Product requirements refinement
- Architecture and solution design
- Issue planning
- Implementation handoff
- Verification planning

## Intended inputs

- Product brief, PRD, user story, feature idea, or issue set
- GitHub repository, branch, PR, issue, or file context
- Architecture docs, roadmap docs, design notes, audit docs, or uploaded files
- External API, SDK, dependency, or integration target
- Agent halt report or uncertainty report

## Intended outputs

- Technical discovery memo
- Repo reconnaissance report
- Feasibility assessment
- Spike plan
- Risk register
- Open questions and decision log
- Downstream handoff notes for `architecture-design-desk`, `issue-planning-desk`, or `implementation-handoff-desk`

## Required connectors

Use GitHub when the request depends on code, repo topology, dependency manifests, tests, build scripts, commits, PRs, issues, or CI status.

Use document connectors or uploaded docs when the request depends on PRDs, roadmaps, architecture docs, design notes, or audit materials.

Use public web only for external APIs, SDKs, vendor docs, standards, or current tool behavior not present in internal sources.

## Composition with Implementation Handoff Desk

This skill does not draft implementation-agent PR prompts. It produces the discovery evidence and constraints that `implementation-handoff-desk` uses later to generate scoped, branch-ready PR handoffs.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
