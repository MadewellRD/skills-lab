# Connector Routing

## GitHub

Required when the plan references existing repos, files, issues, labels, milestones, pull requests, branches, tests, CI checks, or code owners.

Retrieve:

- target repo and default branch
- existing issues and duplicates
- labels and milestones
- related PRs and changed files
- relevant source files and test paths
- CI or validation conventions when available

Halt when GitHub facts are required but unavailable.

## Document sources or uploads

Required when deriving requirements, acceptance criteria, non-goals, designs, or release boundaries.

Retrieve:

- PRD or requirement IDs
- architecture or design specs
- technical discovery memo
- roadmap or milestone constraints
- proof or traceability docs when present

Halt when requirement-critical documents conflict or are absent.

## Communication sources

Optional unless recent decisions, ownership, priority, or halt reports are only available there.

Use communication sources as decision context. Do not let them override repo facts.

## Project management sources

Use when issue ownership, roadmap status, priority, or milestone state lives outside GitHub.
