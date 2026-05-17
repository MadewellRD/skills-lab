# Output Contract

## Default artifacts

- `issue-plan.md` for full decomposition
- `github-issue-drafts.md` for issue body batches
- `dependency-graph.md` for sequencing
- `milestone-plan.md` for sprint or release planning
- `pr-command-handoff.md` for downstream implementation prompt preparation
- `connector-diagnostic.md` when required source facts are unavailable

## Artifact wrapper

For downloadable artifacts, include:

```markdown
# <artifact title>

## How to use this file

Use this file as the source of truth for issue creation, sprint planning, or downstream implementation handoff. Preserve source facts, assumptions, dependencies, acceptance criteria, and halt conditions.

## Content

<artifact body>
```

## Quality bar

Every issue must be independently actionable, testable, and bounded. Every batch must expose dependencies and open questions.
