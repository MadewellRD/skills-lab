# Output Contract

Default artifact names:

- `ci-failure-diagnostic.md`
- `flake-triage.md`
- `pipeline-health-review.md`
- `rerun-decision.md`
- `ci-fix-handoff.md`
- `ci-connector-diagnostic.md`

When output is intended for another agent, include:

```markdown
# <Artifact Title>

## How to use this file
Use this artifact to decide rerun, fix, halt, release readiness, or downstream implementation handoff. Preserve source facts, failure signatures, missing evidence, and halt conditions.

## Artifact
...
```

Every artifact must include source facts and unverified assumptions. If source facts are missing, label the artifact as `connector diagnostic required` or `user-fact-only`.
