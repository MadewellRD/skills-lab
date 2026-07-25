# Issue Plan Template

Use this structure for a full planning artifact.

```markdown
# Issue Plan: <initiative or feature name>

## Source facts

- Product sources:
- Technical sources:
- GitHub sources:
- Communication sources:

## Planning assumptions

- Assumption:
- Confidence:
- Validation needed:

## Objective

State the outcome the issue set must deliver.

## Scope

### In scope

- Work item:

### Out of scope

- Deferred work:

## Issue batch

### Issue 1: <imperative title>

Type: feature | bug | test | docs | migration | infrastructure | security | observability
Priority: p0 | p1 | p2 | p3
Suggested labels:
Suggested milestone:
Dependencies:

Problem or requirement source:

Implementation scope:

Acceptance criteria:

- Criterion 1
- Criterion 2

Validation:

- Command or evidence requirement

Out of scope:

- Boundary

## Dependency order

1. Foundation issue
2. Follow-on issue
3. Verification issue

## Parallelizable work

- Issue A can run with Issue B because there is no file or contract dependency.

## Risks and mitigations

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| Unknown contract | Blocks implementation | Confirm before PR | assigned planner |

## Open questions

- Question:
- Blocking status:

## Downstream handoff to implementation-handoff-desk

Use these issue IDs, acceptance gates, validation commands, and out-of-scope boundaries when generating implementation prompts.
```
