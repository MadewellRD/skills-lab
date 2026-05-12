# Source Hierarchy

Use this truth order for deployment artifacts:

1. Current user instruction in this conversation.
2. Live GitHub repo, PR, commit, check, workflow, and deployment configuration facts.
3. Issue/project tracker facts for scope, owner, and blockers.
4. Canonical release, deployment, architecture, and operations documents.
5. Decision-bearing communication messages.
6. Public vendor documentation for external deployment platforms or services.
7. Explicit assumptions marked as unverified.

When sources conflict, preserve the conflict in the output and halt any go/no-go or deployment execution recommendation until the conflict is resolved.
