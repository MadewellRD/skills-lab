# Source Hierarchy

Truth order for test planning:

1. Current user instruction in the active conversation.
2. Live GitHub repo, PR, issue, commit, and CI facts.
3. Current requirements, architecture, QA, release, and audit documents.
4. Decision-bearing communication sources.
5. Uploaded or pasted context.
6. Public web facts for external systems.
7. Model inference, only if labeled as an assumption.

Conflict handling:

- If requirements conflict with repo behavior, document both and mark as needs clarification.
- If CI or test status conflicts with a pasted claim, prefer live connector status.
- If a user overrides scope, preserve the override as a source fact and update out-of-scope boundaries.
- If acceptance criteria are absent, do not invent them. Produce assumptions or halt depending on risk.
