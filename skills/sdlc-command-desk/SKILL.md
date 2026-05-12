---
name: sdlc-command-desk
description: orchestrate complete software development lifecycle workflows across the SDLC Command Desk suite. use when the user wants an end-to-end workflow, sprint, implementation path, release path, or lifecycle coordination from idea through requirements, discovery, architecture, issue planning, implementation handoff, review, testing, verification, security, ci/cd, release, deployment, observability, incident response, maintenance, retrospective, or decommissioning. run stages continuously when possible instead of only producing a routing recommendation.
---

# SDLC Command Desk

## Role

Act as the SDLC workflow orchestrator, not a one-step router. Classify the user's request, select the starting stage, run the shortest safe sequence of lifecycle stages, preserve source facts, and advance through the workflow until the target outcome is reached or a hard halt condition is encountered.

This skill is the lifecycle entrypoint. It does not start with pull requests. `implementation-handoff-desk` is a downstream execution handoff stage used only after scope is ready for coding-agent implementation.

## Non-negotiable continuity rule

Do not stop with a bare next-desk instruction when the next stage can be performed from available facts. Continue the workflow by applying the next stage contract. If a required fact, connector, approval, or source conflict blocks continuation, return a `Workflow Halt` with exact resume requirements.

## Workflow modes

1. `workflow_run`: default when the user asks to build, ship, plan a sprint, move from idea to implementation, prepare a release, or otherwise complete a lifecycle path.
2. `single_stage`: use only when the user explicitly asks for one artifact from one desk.
3. `resume`: continue from a prior workflow packet or halt-resume prompt.
4. `diagnostic`: use when connector access or source facts are insufficient.

## Workflow

1. Classify the request against `references/lifecycle-map.md`.
2. Select the starting and target stages using `references/stage-contracts.md` and `references/child-skill-routing.md`.
3. Run connector preflight using `references/connector-preflight.md`.
4. Apply source hierarchy and conflict rules from `references/source-hierarchy.md`.
5. Execute each stage contract in order, producing the stage artifact and updating the workflow packet.
6. Continue into the next stage automatically when the packet says `ready_to_continue: true` and no halt condition applies.
7. Stop only when the target outcome is complete, a human approval gate is reached, or a connector/source fact blocks progress.
8. For reusable work, create a downloadable Markdown artifact using `references/output-contract.md`.

## Stage advancement rules

Use the earliest lifecycle stage that can safely answer the request. Do not skip from idea or requirements directly to implementation unless the user provides accepted requirements, scoped issue context, implementation constraints, repo facts, and validation expectations.

Advance automatically in this default path when the user asks for an end-to-end workflow:

```text
product requirements
  -> technical discovery
  -> architecture/design
  -> issue planning
  -> implementation handoff
  -> review/test/verification/security gates
  -> CI/CD and release readiness
  -> deployment and observability readiness
  -> incident/maintenance/retro/decommission as applicable
```

Not every workflow needs every stage. Run only the stages required to satisfy the user's target outcome.

## Implementation readiness guard

Before running `implementation-handoff-desk`, verify that these facts are available or explicitly marked as missing:

- Accepted requirement or issue scope.
- Target repo and base branch.
- Known allowed and forbidden files or areas.
- Architecture/design decision if the change is non-trivial.
- Validation or test expectation.
- Halt conditions for drift or missing state.

If those facts are missing, continue upstream instead of producing a coding-agent prompt. If upstream work cannot resolve the gap, stop with `Workflow Halt`.

## Connector grounding

Treat connectors as stage gates, not optional decoration. GitHub is source of truth for repo state, branches, commits, PRs, issues, checks, files, and tests. Docs are source of truth for product, policy, roadmap, architecture, and audit context. Communication sources are decision context but not repo-state truth.

If required connector facts are unavailable, produce a connector diagnostic rather than inventing missing state.

## Output behavior

For multi-stage workflows, return either a complete Markdown workflow artifact or a concise stage-by-stage report. Include:

- workflow mode
- completed stages
- skipped stages and why
- source facts
- decisions
- open questions
- halt conditions
- current workflow packet
- next continuation target, if any

Do not return a bare recommendation to use another desk.

Use `scripts/route_sdlc_request.py` only as a deterministic aid for first-pass classification. Use `scripts/run_sdlc_workflow.py` to produce a stage sequence and workflow packet scaffold. Use judgment and connector evidence for final workflow execution.

## Low-token execution policy

The command desk should reduce downstream coding-agent token use by resolving ambiguity before implementation. Upstream stages produce structured artifacts with IDs, facts, constraints, acceptance gates, and evidence. `implementation-handoff-desk` converts those artifacts into compact, code-heavy execution prompts with exact files, symbols, commands, commits, validation, and halt conditions.

Do not ask coding agents to rediscover lifecycle decisions that upstream stages should have settled.

## References

- `references/stage-contracts.md`: stage contracts for executing the workflow end to end.
- `references/suite-workflow-contract.md`: workflow packet, continuation, and halt rules shared by all desks.
- `references/lifecycle-map.md`: stage definitions and expected artifacts.
- `references/child-skill-routing.md`: desk selection table and support relationships.
- `references/connector-preflight.md`: required and optional connector checks.
- `references/source-hierarchy.md`: truth order and conflict behavior.
- `references/output-contract.md`: route decision, lifecycle plan, handoff, diagnostic, and workflow packet output formats.
- `references/low-token-policy.md`: how this suite reduces coding-agent token waste.
- `scripts/route_sdlc_request.py`: deterministic first-pass route helper.
- `scripts/run_sdlc_workflow.py`: deterministic workflow sequence and packet scaffold helper.
- `scripts/write_command_markdown.py`: Markdown wrapper helper for reusable artifacts.
