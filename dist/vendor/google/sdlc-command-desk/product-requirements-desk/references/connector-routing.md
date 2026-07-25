# Connector routing

## GitHub

Use GitHub for issue titles/bodies/comments, labels, milestones, linked PRs, repo docs, existing code boundaries, and implementation history.

Required facts when GitHub is relevant:

- repo name
- issue or milestone IDs
- current issue status
- linked PRs or blockers
- relevant files/modules when known

## Docs and uploaded files

Use docs or uploaded files for roadmap, strategy, product briefs, user research, prior PRDs, policy, compliance, architecture, and release scope.

Required facts:

- document title or filename
- date or recency signal when available
- decision or requirement-bearing excerpts
- conflict notes

## Communication sources

Use Slack, Teams, email, or equivalent only for decision-bearing context.

Required facts:

- speaker
- date or relative recency
- decision or unresolved question
- whether the message is authoritative or informal

## Missing connector behavior

If the user asks for a grounded PRD but required connectors are unavailable, produce `connector-diagnostic.md` or a clearly scoped draft from provided facts only.
