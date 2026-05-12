# Suite Workflow Contract

This file defines how SDLC Command Desk skills participate in one continuous workflow instead of behaving as isolated one-off prompts.

## Core rule

Do not end with only a bare next-desk instruction when enough context exists to continue. Complete the current stage, create a workflow packet, and continue to the next stage contract in the same response or artifact until a target stage, approval gate, connector limit, or hard missing fact stops the workflow.

## Operating modes

- `single_stage`: complete only the current desk's stage when the user explicitly asks for one artifact.
- `workflow_run`: move through multiple lifecycle stages in order, using each desk's contract.
- `resume`: continue from a prior workflow packet.
- `halt`: stop only because required facts, connector access, or human approval are missing.

## Workflow packet

Every stage handoff must preserve this packet, either inline or in a Markdown artifact.

```yaml
workflow_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt"
  current_stage: "stage-name"
  completed_stages:
    - "stage-name"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  source_facts:
    - fact: "source-backed fact"
      source: "github | docs | user | connector | unknown"
  decisions:
    - "decision made at this stage"
  open_questions:
    - "question blocking later work"
  artifacts:
    - "artifact name or path"
  halt_conditions:
    - "condition that requires stopping"
  ready_to_continue: true
```

## Autocontinuation rule

Continue automatically when all of the following are true:

1. The user asked for an end-to-end plan, build path, sprint, implementation path, release path, or workflow completion.
2. The next stage can be performed from available user-provided facts and connector-grounded facts.
3. Continuing will not invent repo state, branch names, issue IDs, CI status, release state, owners, or approvals.
4. The next stage does not require a human approval gate.

Stop with `Workflow Halt` when a required fact is missing, a connector is unavailable, or an approval gate is reached.

## Halt format

When stopping, do not merely recommend another desk. Return:

```markdown
## Workflow Halt

Current stage: <stage>
Completed stages: <list>
Blocked next stage: <stage>
Reason: <missing fact, connector, approval, or conflict>
Required to resume:
- <specific fact or action>
Resume prompt:
<copy/paste prompt that includes the workflow packet>
```

## Child-desk behavior

Each child desk must produce its normal artifact plus a compact workflow packet. If the next stage is obvious and source facts are sufficient, continue into the next stage contract rather than stopping at a recommendation. If the next stage requires a different specialist skill that is installed, ChatGPT may invoke it. If it is not available, use the stage contract summarized by `sdlc-command-desk`.
