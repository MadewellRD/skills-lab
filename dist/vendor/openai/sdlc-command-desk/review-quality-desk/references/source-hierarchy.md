# Source Hierarchy

Use this truth order for reviews:

1. Current user instruction.
2. Live GitHub PR metadata, diff, changed files, commits, checks, and comments.
3. Linked GitHub issues, milestones, labels, and acceptance criteria.
4. Repository source files, tests, build scripts, and docs.
5. Product, architecture, security, release, or policy docs from connected sources.
6. Decision-bearing team messages or halt reports.
7. Public documentation for external dependencies.
8. Pasted context or model inference, clearly labeled as unverified when not connector-backed.

When sources conflict, preserve the conflict in the review. Do not smooth it over. Use `insufficient evidence` if the conflict affects merge safety.
