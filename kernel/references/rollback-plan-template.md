# Rollback Plan Template

Use this when release risk requires a rollback or recovery path.

```markdown
# Rollback Plan: <release name or version>

## Rollback decision trigger

- Trigger condition:
- Detection signal:
- Decision owner:
- Maximum time to decision:

## Verified rollback path

1. ...

## Data and compatibility considerations

- Schema changes:
- Data migrations:
- Backward compatibility:
- Customer-visible effects:

## Validation after rollback

- Health checks:
- Smoke tests:
- Monitoring signals:
- Support/customer comms:

## Risks and caveats

| Risk | Impact | Mitigation |
|---|---|---|

## Source facts

- ...
```
