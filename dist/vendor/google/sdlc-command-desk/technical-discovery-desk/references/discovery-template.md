# Technical Discovery Memo Template

Use this template for broad discovery and feasibility work. Adapt section depth to the request, but preserve the distinction between verified facts, assumptions, risks, and decisions.

```markdown
# Technical Discovery: <topic>

## How to use this file

Use this memo as the technical input for architecture, issue planning, spike planning, or implementation handoff. Do not treat assumptions as verified facts.

## Executive summary

One concise paragraph covering feasibility, major constraints, and recommended next action.

## Request and scope

- Requested outcome:
- In scope:
- Out of scope:
- Current decision needed:

## Source facts

| Source | Fact | Confidence | Notes |
|---|---|---|---|

## Existing system observations

- Repo/module topology:
- Relevant files or components:
- Build/test surface:
- Dependencies and integrations:
- Recent related work:

## Feasibility assessment

- Feasibility: high, medium, low, or blocked
- Why:
- Constraints:
- Required decisions:

## Options considered

| Option | Summary | Benefits | Risks | Recommendation |
|---|---|---|---|---|

## Risks and unknowns

| Item | Type | Severity | Evidence | Mitigation or owner |
|---|---|---|---|---|

## Spike plan, if needed

- Question to answer:
- Files or systems to inspect:
- Commands or checks:
- Expected artifact:
- Stop condition:

## Downstream handoff

- Recommended next skill:
- Inputs to pass forward:
- Do not proceed until:
```
