# Source Hierarchy

Use this truth order:

1. Current user instruction in the active conversation.
2. Live GitHub facts: commits, branches, PRs, issues, tags, releases, checks, files.
3. Release docs, changelog, runbooks, policy, roadmap, and compliance docs.
4. Verification, security, CI, deployment, or incident artifacts from adjacent skills.
5. Communication sources such as Slack, Teams, or email for decision history.
6. Public web only for external tooling or platform behavior.
7. Inference, clearly labeled as an assumption.

When sources conflict, do not merge them into a false consensus. Surface the conflict and mark the affected gate blocked or unknown.
