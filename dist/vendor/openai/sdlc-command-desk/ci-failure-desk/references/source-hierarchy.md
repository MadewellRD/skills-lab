# Source Hierarchy

Apply this precedence when sources conflict:

1. Current user instruction for requested scope and priority.
2. GitHub Actions, commit status, PR, branch, issue, workflow, and log state for CI facts.
3. Repository files for workflow definitions, build scripts, test configuration, and dependency state.
4. Test strategy, release policy, deployment policy, and operations docs for expected gates.
5. Communication sources and agent halt reports for recent decisions and reproduction notes.
6. Public web for external service or tool facts only.
7. Model inference only when labeled as inference.

If GitHub check state and a pasted report disagree, preserve the conflict and treat it as a halt or verification condition. Do not silently choose the more convenient source.
