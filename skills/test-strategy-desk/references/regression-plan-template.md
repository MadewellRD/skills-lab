# Regression Plan Template

```markdown
# Regression Plan: <change or release>

## Regression objective
Describe the behavior that must remain stable.

## Baseline behavior
List verified current behavior and where it is proven: tests, docs, issues, screenshots, logs, or user statements.

## Areas at risk
- UI/API behavior
- Data compatibility
- Permission/auth flows
- Performance
- Error handling
- Migration/rollback
- Integrations

## Existing tests to preserve
List known test files or commands only after connector verification.

## New regression coverage required
List new tests, fixtures, scenarios, or manual checks.

## Pass/fail criteria
Define observable pass criteria.

## Halt triggers
State conditions that require stopping: missing baseline, conflicting facts, no reproducible bug, failing validation, or regression ambiguity.
```
