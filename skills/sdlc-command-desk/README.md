# SDLC Command Desk

`SDLC Command Desk` is the lifecycle entrypoint for the SDLC skill suite. It classifies a software-development request, identifies the current lifecycle stage, selects the correct specialized desk, enforces connector grounding, and prevents premature implementation handoffs.

## Position in the suite

This skill sits above the stage-specific desk skills. It does not replace them. It routes work to them.

`implementation-handoff-desk` is a downstream execution desk. It is used when scoped work is ready to become branch, commit, pull request, halt-resume, or coding-agent instructions.

## Primary outputs

- Inline route decision.
- Downloadable lifecycle route plan.
- Cross-desk handoff plan.
- Connector diagnostic.
- Implementation-readiness assessment.

## Required context

The skill can operate from user-provided context, but it should use connectors whenever the route depends on repo state, issue state, source documents, or team decisions.

## Core rule

Route to the earliest lifecycle stage that can safely answer the request. Do not move into implementation handoff until requirements, constraints, repo facts, and validation expectations are sufficiently grounded.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
