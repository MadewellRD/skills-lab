# Repo Reconnaissance Template

Use this when the user asks to inspect an unfamiliar repository, identify implementation surfaces, or determine where a future change belongs.

```markdown
# Repo Reconnaissance: <repo or area>

## How to use this file

Use this report to decide whether work is ready for architecture design, issue planning, or PR handoff.

## Repository baseline

- Repository:
- Default branch:
- Baseline commit or ref:
- Relevant issues or PRs:
- CI/check status:

## Topology

- Entry points:
- Core modules:
- Tests:
- Build/deploy files:
- Docs:

## Relevant code surfaces

| Surface | Files | Why it matters | Confidence |
|---|---|---|---|

## Dependency and integration surface

- Runtime dependencies:
- Dev/test dependencies:
- External services:
- Configuration/secrets boundaries:

## Test and validation surface

- Existing tests:
- Missing tests:
- Local commands:
- CI gates:

## Change impact

- Likely touched areas:
- Downstream effects:
- Migration needs:
- Backward compatibility concerns:

## Unknowns and next inspection

List only actionable unknowns. Include the connector or command needed to resolve each one.
```
