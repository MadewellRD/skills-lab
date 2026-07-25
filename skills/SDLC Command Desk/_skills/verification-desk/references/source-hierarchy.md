# Source Hierarchy

Use this precedence order when sources conflict.

1. Current user instruction in the active conversation.
2. Live GitHub state for code, branches, commits, PRs, issues, checks, and test files.
3. Canonical requirement sources: PRD, SRS, issue acceptance criteria, approved design specs.
4. CI logs, test reports, artifacts, and QA evidence.
5. Review comments and stakeholder decisions.
6. Public docs for external platform behavior.
7. Inference, clearly marked as assumption.

Conflict handling:

- If GitHub state conflicts with pasted repo facts, trust GitHub and report the drift.
- If requirements sources conflict, preserve both and ask for resolution unless the current user resolves it.
- If CI evidence conflicts with manual claims, mark the gate as blocked or insufficient evidence.
