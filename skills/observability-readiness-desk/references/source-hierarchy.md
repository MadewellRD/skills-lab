# Source Hierarchy

Use this truth order when sources conflict:

1. Current user instruction in the active conversation.
2. Live monitoring or incident evidence for production state.
3. GitHub source files, configuration, deployment manifests, commits, PRs, and checks.
4. Current architecture, deployment, release, incident, and runbook docs.
5. Historical issues, PR discussions, and incident notes.
6. Pasted context and model inference, clearly marked as unverified.

Production state and code state are distinct. A dashboard may show current impact, but repo/config determines what can be changed. If both are needed and one is missing, state the missing evidence.
