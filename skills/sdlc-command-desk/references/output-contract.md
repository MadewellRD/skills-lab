# Output Contract

## Inline route decision

Use for simple requests.

```markdown
Selected desk: <desk-name>
Lifecycle stage: <stage number and name>
Reason: <why this desk>
Required context: <missing or present context>
Next action: <what the user or next desk should do>
```

## Lifecycle route plan

Use for multi-stage work.

```markdown
# <title>

## How to use this file
Use this as the routing plan for the next SDLC pass. Run the listed desk skills in order and preserve halt conditions.

## Source facts
- ...

## Current stage
- ...

## Route
| Order | Desk | Purpose | Inputs | Outputs | Halt conditions |
|---:|---|---|---|---|---|

## Implementation readiness
- Ready/not ready
- Missing facts

## Next action
- ...
```

## Connector diagnostic

Use when required source facts are unavailable.

```markdown
# Connector Diagnostic

## Missing required context
- ...

## Why this blocks the request
- ...

## Safe alternatives
- route upstream
- produce user-fact-only plan
- ask user to connect/select source
```

## Handoff format

When routing to another desk, include:

- selected desk
- reason
- required connectors
- source facts already known
- missing facts
- expected output
- halt conditions


## Workflow packet output

For workflow runs, every artifact must include a workflow packet with completed stages, next stage, source facts, decisions, open questions, artifacts, halt conditions, and `ready_to_continue`. If the workflow can continue, continue it. If it cannot, include `Workflow Halt` and a resume prompt.
