# Source Hierarchy

Use this precedence order when sources conflict:

1. Current user instruction in the active conversation.
2. Live GitHub state for code, branches, PRs, issues, workflows, tests, and release tags.
3. Current production or observability evidence for usage, health, traffic, and errors.
4. Current canonical product, API, architecture, runbook, and retention docs.
5. Issue/project tracker data for ownership, commitments, labels, and milestones.
6. Recent communication sources for decision context.
7. Public web documentation for external APIs and third-party behavior.
8. Model inference, only when clearly labeled as an assumption.

Conflict handling:

- Do not hide conflicts.
- Prefer halt conditions for conflicts affecting consumers, data retention, rollback, or public contracts.
- If the user resolves a conflict explicitly, preserve that decision in source facts.
