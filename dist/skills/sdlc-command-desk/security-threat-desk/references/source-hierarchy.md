# Source Hierarchy

Apply this precedence when sources conflict:

1. Current user instruction for requested scope and priority.
2. GitHub repo state for code, configs, branches, commits, PRs, issues, tests, and CI facts.
3. Product, architecture, security, privacy, and compliance docs for intent and policy.
4. Ticket systems for acceptance criteria, priority, and workflow state.
5. Communication sources for recent decisions and halt reports.
6. Public web for external documentation only.
7. Model inference only when labeled as inference.

If code and docs disagree, state the disagreement and treat it as a risk or halt condition. Do not silently choose the more convenient source.
