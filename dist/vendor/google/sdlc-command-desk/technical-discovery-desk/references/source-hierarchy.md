# Source Hierarchy

Use this truth order:

1. Current explicit user instruction.
2. Live GitHub repo state for code, files, commits, branches, PRs, issues, checks, and tests.
3. Live issue/project state for acceptance criteria, priority, owner, labels, blockers, and linked PRs.
4. Canonical docs for product, roadmap, architecture, design, audit, and policy truth.
5. Decision-bearing communications for recent context.
6. Public web for external APIs, SDKs, standards, and vendor behavior.
7. Explicitly labeled assumptions.

Conflict handling:

- If GitHub contradicts pasted code facts, GitHub wins for repo state unless the user explicitly says the pasted facts are newer.
- If docs contradict issues, preserve both and ask for resolution or mark as a decision needed.
- If communications contradict canonical docs, treat communications as potential newer context and label the conflict.
- Never merge conflicting facts into a false consensus.
