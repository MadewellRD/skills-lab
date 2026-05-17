# Halt Conditions

Halt or produce `architecture-diagnostic.md` when:

- the design is repo-aware and GitHub context is unavailable;
- the design depends on PRD/SRS/discovery artifacts that are missing;
- code paths, APIs, schemas, or tests are named but cannot be verified;
- current repo state conflicts with requirements or user-provided facts;
- security, privacy, data retention, or compliance behavior would require speculation;
- implementation scope is requested before architecture questions are resolved;
- the user asks for a design that crosses too many systems for a single reviewable artifact;
- source material is stale and no current source can confirm it.

When halting, return:

```markdown
# Architecture Diagnostic

## Blocking reason

[Why design cannot proceed safely]

## Missing facts

- [Fact]

## Sources checked

- [Source]

## Safe next step

[Specific action needed]
```
