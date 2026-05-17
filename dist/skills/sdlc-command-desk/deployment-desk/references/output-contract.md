# Output Contract

Deployment Desk outputs should be Markdown artifacts unless the user asks for a short inline answer.

## File wrapper

Use this wrapper for downloadable files:

```markdown
# <Artifact Title>

## How to use this file

Use this file as the deployment, rollout, change-management, or go/no-go source of truth. Preserve source facts, assumptions, validation gates, rollback triggers, and halt conditions.

## Artifact

<content>

## Source facts

<verified facts>

## Unverified assumptions

<assumptions or none>
```

## Default filenames

- `deployment-plan.md`
- `rollout-plan.md`
- `change-management-plan.md`
- `go-no-go-review.md`
- `post-deploy-checklist.md`
- `deployment-diagnostic.md`

## Quality bar

Each artifact must include:

- target environment or a missing-environment warning
- deployment scope
- preconditions
- validation gates
- rollback or mitigation path
- owners or owner gaps
- source facts
- assumptions
- halt conditions when safety is not knowable
