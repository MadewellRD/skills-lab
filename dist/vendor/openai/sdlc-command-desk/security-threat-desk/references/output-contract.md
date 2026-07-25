# Output Contract

Default artifact names:

- `threat-model.md`
- `security-review.md`
- `trust-boundary-review.md`
- `dependency-secret-review.md`
- `security-mitigation-backlog.md`
- `security-connector-diagnostic.md`

When output is intended for another agent, include:

```markdown
# <Artifact Title>

## How to use this file
Use this artifact to review risks, create mitigation issues, verify controls, or prepare a PR handoff. Preserve source facts, halt conditions, and unresolved questions.

## Artifact
...
```

Every artifact must include source facts and unverified assumptions. If source facts are missing, label the artifact as `connector diagnostic required` or `user-fact-only`.
