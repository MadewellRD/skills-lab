# AI Engineering Suite Workflow Contract

## Purpose

This reference defines the shared workflow contract for the AI Engineering Command Desk suite. Use it with every AI Engineering orchestrator or specialist desk.

## Continuity rule

Do not stop with a bare next-desk recommendation when the next stage can be completed from available facts. Complete the current stage, update the workflow packet, and continue when `ready_to_continue: true`.

Return `Workflow Halt` only when a required fact, connector, approval, or source conflict blocks safe continuation.

## Workflow packet

Every AI Engineering desk should preserve and update:

```yaml
workflow_mode:
stage_sequence:
current_stage:
completed_stages:
skipped_stages:
source_facts:
decisions:
assumptions:
open_questions:
risk_tier:
approval_state:
validation_gates:
hard_halts:
soft_gaps:
ready_to_continue:
downstream_handoff_targets:
```

## Stage advancement

Advance only when the current desk output is complete enough that the next desk does not need to rediscover scope, evidence, validation, or halt conditions.

Default path:

```text
capability intake
  -> model selection
  -> prompt systems
  -> tool schema design
  -> agent architecture
  -> retrieval/RAG when grounding is required
  -> dataset curation or synthetic data when data work is required
  -> eval design
  -> eval run analysis
  -> fine-tuning only when evidence justifies it
  -> AI safety review and red-team eval
  -> inference ops
  -> agent observability
  -> cost/latency optimization
  -> AI release readiness
  -> AI incident response when production failure exists
```

## Cross-suite handoffs

Use explicit cross-suite labels for SDLC, Security, Data, Product, Support, or Customer Success handoffs. Do not imply those desks are AI Engineering subdesks.
