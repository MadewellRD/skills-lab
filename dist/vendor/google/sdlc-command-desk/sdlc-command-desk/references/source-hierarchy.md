# Source Hierarchy

Apply this truth order when sources disagree.

1. Explicit user instruction in the current chat.
2. Live GitHub state for code, branches, commits, PRs, issues, checks, files, and tests.
3. Live issue/project tracker state for acceptance criteria, priority, labels, owner, and blockers.
4. Canonical docs for product, architecture, roadmap, compliance, and policy.
5. Communication context for recent decisions and halt reports.
6. Public web or external docs for third-party API/tool facts.
7. Model memory or inference, only if clearly labeled as unverified.

## Conflict rule

Do not silently reconcile conflicts. State the conflict, identify the higher-trust source, and include a halt condition if downstream execution depends on the unresolved fact.

## Freshness rule

Do not rely only on modified timestamps. Prefer document content and live connector state for recency.
