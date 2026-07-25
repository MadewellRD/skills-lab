# Source Hierarchy

Use this truth order for architecture work:

1. Current user instruction in this chat.
2. Live GitHub repo state for code, files, tests, branches, commits, and dependency manifests.
3. Current PRD/SRS/discovery/design docs from connected document sources or uploads.
4. GitHub issues, milestones, projects, and acceptance criteria.
5. Existing architecture docs, ADRs, READMEs, and code comments.
6. Decision-bearing Slack/Teams/email messages.
7. Public docs for external APIs and frameworks.
8. Inference, clearly labeled as inference.

Conflict rules:

- User priority can choose direction, but cannot rewrite repo facts.
- GitHub wins for what the code currently does.
- Requirements docs win for intended product behavior unless superseded by current user instruction.
- Communication sources explain decisions but do not prove code state.
- Public docs explain external tools but do not prove this repo uses them.

When conflict affects architecture, include it under `Open questions` or halt until resolved.
