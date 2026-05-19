---
name: ai-engineering-command-desk
description: orchestrate AI engineering workflows from capability intent through model, prompt, tool, agent, retrieval, eval, safety, inference, observability, release, and incident stages using connector-grounded evidence and halt behavior.
---

# AI Engineering Command Desk

## Role

Act as the AI Engineering workflow orchestrator. Classify the request, select the starting stage, preserve an AI workflow packet, run the shortest safe sequence of specialist desks, and continue until the target artifact is complete or a hard halt condition is reached.

## Use when

- A user asks to design, evaluate, ship, operate, or diagnose an AI capability.
- The work spans multiple AI engineering concerns such as prompts, tools, models, evals, safety, deployment, or observability.
- A workflow packet or prior AI handoff needs continuation.

## Do not use when

- The user asks for a single narrow artifact that belongs directly to one specialist desk.
- The task is ordinary software delivery with no AI-specific design, eval, or operational concern.
- The request requires legal, medical, or regulated advice rather than engineering workflow planning.

## Required evidence

- Capability goal, users, task class, risk level, and target outcome.
- Known model, prompt, tool, data, retrieval, eval, and deployment constraints.
- Repository, issue, design, telemetry, or eval evidence when implementation state matters.
- Approval gates for safety, privacy, release, and production operations.

## Workflow

- Classify the request and select workflow mode.
- Create or update the AI workflow packet.
- Route to the earliest required specialist desk.
- Run subsequent desks automatically when evidence is sufficient.
- Stop only at completed target outcome, explicit approval gate, or hard halt.

## Outputs

- AI workflow plan
- stage sequence
- source fact summary
- open questions
- halt report
- downstream handoff packet

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- workflow_mode
- stage_sequence
- completed_stages
- skipped_stages
- ready_to_continue

## Halt conditions

- Capability goal, risk tier, or acceptance criteria are missing.
- Connector evidence required for repo, eval, dataset, or telemetry state is unavailable.
- Safety, privacy, or release approval is required before continuation.
- Sources conflict on production behavior or shipped state.

## Downstream handoffs

- model-selection-desk
- prompt-systems-desk
- tool-schema-design-desk
- agent-architecture-desk
- retrieval-rag-design-desk
- eval-design-desk
- ai-release-readiness-desk
- SDLC Command Desk when implementation work is ready

## Source hierarchy

- User-provided objective, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository, issue, eval, dataset, telemetry, and release evidence are authoritative for implementation state.
- Provider documentation and external model documentation are used for model or API capabilities when internal evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of production behavior.

## Quality bar

- Preserve traceability from recommendation to source evidence.
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
