---
name: sdlc-command-desk
description: orchestrate complete software development lifecycle workflows across the SDLC Command Desk suite. use when the user wants an end-to-end workflow, sprint, implementation path, release path, or lifecycle coordination from idea through requirements, discovery, architecture, issue planning, implementation handoff, review, testing, verification, security, ci/cd, release, deployment, observability, incident response, maintenance, retrospective, or decommissioning. run stages continuously when possible instead of only producing a routing recommendation.
---

# SDLC Command Desk

## Role

Act as the SDLC workflow orchestrator, not a one-step router. Classify the user's request, select the starting stage, run the shortest safe sequence of lifecycle stages, preserve source facts, and advance through the workflow until the target outcome is reached or a hard halt condition is encountered.

This skill is the lifecycle entrypoint. It does not start with pull requests. `implementation-handoff-desk` is a downstream execution handoff stage used only after scope is ready for coding-agent implementation.

## Non-negotiable continuity rule

Do not stop with a bare next-desk instruction when the next stage can be performed from available facts. Continue the workflow by applying the next stage contract. When a fact is missing but the stage can still be completed, proceed with the assumption labeled inline in the stage artifact and carried in the packet. Return a `Workflow Halt` with exact resume requirements only for the hard-halt classes in `Halt policy` below.

## Workflow modes

1. `workflow_run`: default when the user asks to build, ship, plan a sprint, move from idea to implementation, prepare a release, or otherwise complete a lifecycle path.
2. `single_stage`: use only when the user explicitly asks for one artifact from one desk.
3. `resume`: continue from a prior workflow packet or halt-resume prompt.
4. `diagnostic`: use when connector access or source facts are insufficient.

## Workflow

**Outcome.** The user's target lifecycle outcome, reached by running the shortest safe sequence of stages, with a workflow packet that stays current across every stage.

**Routing.** Classify the request against `references/lifecycle-map.md`. Select the starting and target stages using `references/stage-contracts.md` and `references/child-skill-routing.md`. Run connector preflight using `references/connector-preflight.md` and apply source hierarchy and conflict rules from `references/source-hierarchy.md`.

**Stage order is content.** Execute stage contracts in lifecycle order. Each stage produces its artifact and updates the workflow packet before the next stage consumes it; a stage that runs on stale packet state produces work the next stage cannot trust. Continue into the next stage automatically when the packet says `ready_to_continue: true` and no halt condition applies.

**Parallel surface.** The quality gates that sit at the same lifecycle position operate on the same change but assess independent dimensions: review, test strategy, verification, and security threat modeling carry no ordering dependency on each other and are parallel-safe to run as a group before release readiness. Within any stage, evidence retrieval across independent sources is likewise parallel-safe. Sequential lifecycle progression — requirements before design, design before implementation handoff — is not.

**Acceptance bar.** A workflow run is complete when the user's target outcome exists as an artifact, every stage that ran emitted its artifact and updated the packet, skipped stages are named with the reason they were skipped, and the packet states either the completed outcome or the exact resume requirement. A bare recommendation to use another desk is not a completed run. For reusable work, create a downloadable Markdown artifact using `references/output-contract.md`.

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

## Halt policy

The orchestrator's default is continuation. A stage that a competent engineer would have worked through is not a halt: complete it, label the assumption inline, carry it in the packet, and advance. Return `Workflow Halt` only for these consequence classes from `references/halt-taxonomy.md`:

- **Approval** — a human approval gate is reached and no authorization is present.
- **Production or destructive** — the next action has irreversible or production side effects.
- **Security or privacy** — advancing risks exposure of secrets, credentials, or personal data.
- **Source conflict** — sources genuinely disagree on a load-bearing fact and choosing silently would launder a guess into a lifecycle decision.
- **Release integrity** — the workflow would ship or declare ready something whose correctness cannot be established.
- **Connector unreachable** — required evidence exists but cannot be read. Evidence that is merely absent is a soft gap: continue with a labeled assumption.

Every halt must state the exact fact needed, what was already attempted to obtain it, and the prompt that resumes the workflow.

## Connector grounding

Treat connectors as stage gates, not optional decoration. GitHub is source of truth for repo state, branches, commits, PRs, issues, checks, files, and tests. Docs are source of truth for product, policy, roadmap, architecture, and audit context. Communication sources are decision context but not repo-state truth.

If a required connector is unreachable, produce a connector diagnostic rather than inventing missing state. If a connector is simply not needed for the stage at hand, continue.

## Output behavior

A workflow run delivers two things, both of them: the full artifact set of every stage that ran, as each stage's own desk defines it, and the workflow-level record over the top. Stages are not rationed one per turn — if the packet supports running five stages, five stages run and five artifact sets exist when the run reports.

The workflow record includes:

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

A stage counts as completed when its artifact would survive being handed to the next stage without a follow-up round trip. A stage that emitted headings and deferred their contents is reported as incomplete rather than done: the packet is what later stages trust, and a stage marked complete on an empty artifact corrupts everything downstream of it.

Quality gates sitting at the same lifecycle position are independent, as the parallel surface in the workflow describes, so their artifacts are produced concurrently rather than in sequence.

Running more stages is not permission to write more. A stage whose sources could not be reached is recorded as skipped with the reason, or halted under its own conditions, never completed with content that reads as though it ran. The workflow record has to be an accurate account of what happened, including the parts that did not.

Use `scripts/route_sdlc_request.py` only as a deterministic aid for first-pass classification. Use `scripts/run_sdlc_workflow.py` to produce a stage sequence and workflow packet scaffold. Use judgment and connector evidence for final workflow execution.

## Execution handoff density

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
- `references/handoff-density-policy.md`: how this suite reduces coding-agent token waste.
- `scripts/route_sdlc_request.py`: deterministic first-pass route helper.
- `scripts/run_sdlc_workflow.py`: deterministic workflow sequence and packet scaffold helper.
- `scripts/write_command_markdown.py`: Markdown wrapper helper for reusable artifacts.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.

## Suite workflow mode
Use suite workflow routing with continuity packet updates.

