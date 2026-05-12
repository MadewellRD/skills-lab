# Issue Planning Desk

`issue-planning-desk` converts requirements and design artifacts into actionable implementation issues, milestone plans, dependency graphs, and downstream handoff notes.

## Lifecycle coverage

- Planning, decomposition, and issue generation
- Sprint and milestone scoping
- Dependency sequencing
- GitHub issue drafting
- Handoff preparation for implementation prompts

## Intended inputs

- PRDs and requirement IDs
- Technical discovery memos
- Architecture and design specs
- Existing GitHub issues, labels, milestones, and repo state
- Stakeholder decisions or prioritization notes
- Validation and release constraints

## Intended outputs

- Issue plan Markdown artifact
- GitHub issue draft batch
- Dependency graph and sequencing plan
- Milestone or sprint scope plan
- Acceptance gates for each issue
- Handoff notes for `implementation-handoff-desk`

## Required connectors

- GitHub for repo, issue, label, milestone, PR, branch, file, and test facts
- Document sources or uploaded files for product and design truth

## Optional connectors

- Slack, Teams, email, or equivalent communication sources for recent decisions
- Project management tools when issue priority, ownership, or roadmap state lives there

## Composition

This skill comes after `product-requirements-desk`, `technical-discovery-desk`, and `architecture-design-desk`. It feeds issue-backed work into `implementation-handoff-desk` for final implementation-agent prompts.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
