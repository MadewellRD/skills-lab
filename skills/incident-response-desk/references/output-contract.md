# Output Contract

Default downloadable artifact names:

- `incident-triage.md`
- `incident-rca.md`
- `bug-triage.md`
- `hotfix-handoff.md`
- `post-incident-review.md`
- `incident-follow-up-issues.md`
- `connector-diagnostic.md`

Use this wrapper for agent-facing artifacts:

```markdown
# [artifact title]

## How to use this file

Use this artifact as the source of truth for triage, response coordination, RCA, or downstream SDLC handoff. Preserve severity, evidence, unknowns, halt conditions, and verification gates.

## Artifact

[content]
```

Every output must include source facts used, unknowns, confidence level, and follow-up evidence needed. If code work is required, include a `implementation-handoff-desk` handoff section rather than embedding vague implementation instructions.
