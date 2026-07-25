# Output Contract

Default artifact names:

- `test-strategy.md`
- `qa-scenario-matrix.md`
- `regression-plan.md`
- `fixture-plan.md`
- `coverage-gap-report.md`
- `verification-handoff.md`
- `pr-test-handoff.md`
- `connector-diagnostic.md`

When the artifact is meant for another agent, include:

```markdown
# <artifact title>

## How to use this file
Paste or attach this file to the target SDLC skill or implementation agent. Preserve source facts, assumptions, halt conditions, and downstream handoff instructions.

## Source facts
- ...

## Unverified assumptions
- ...

## Artifact
...
```

A test artifact must not claim that a test exists, passes, or covers a behavior unless source evidence supports it.
