# Source Hierarchy

Use this truth order when sources conflict.

1. Current user instruction for requested artifact, urgency, and business priority.
2. Live telemetry or incident-management data for runtime status, alerts, impact, and recovery evidence.
3. GitHub repo state for code, commits, branches, PRs, issues, checks, releases, and changed files.
4. Deployment and release systems for rollout, rollback, feature-flag, version, and environment state.
5. Runbooks, architecture docs, support docs, and known-issues docs.
6. Slack, Teams, email, status-page, or paging messages for timeline and decision context.
7. Public web only for external service facts or vendor status pages when relevant.
8. Model inference only when clearly marked as a hypothesis.

Do not convert a hypothesis into a root cause without evidence. If communications conflict with telemetry or GitHub, preserve the conflict in the artifact and list the source that must be checked next.
