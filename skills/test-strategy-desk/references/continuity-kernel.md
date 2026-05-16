# Continuity Kernel

Shared machine-readable state packet for cross-desk SDLC continuity.

```yaml
continuity_packet:
  workflow_id: "user-or-generated-id"
  suite_version: "v0.2.0-rc.1"
  workflow_mode: "single_stage | workflow_run | resume | halt"
  target_outcome: "plain-language user outcome"
  current_stage: "stage-name"
  completed_stages:
    - "stage-name"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  repo_context:
    repository: "owner/name-or-unknown"
    default_branch: "branch-or-unknown"
    base_ref: "branch-sha-or-unknown"
    target_branch: "branch-or-unknown"
    selected_repos:
      - "owner/name"
  source_facts:
    - id: "SF-001"
      fact: "source-backed fact"
      source_type: "github | docs | issue | communication | user | web | unknown"
      source_ref: "path, issue, PR, URL, doc name, or pasted context"
      freshness: "current | stale | unknown"
      confidence: "high | medium | low"
      used_by:
        - "stage-name"
  decisions:
    - id: "DEC-001"
      decision: "decision made"
      rationale: "why"
      alternatives_rejected:
        - "option"
      approval_required: false
  assumptions:
    - id: "ASM-001"
      assumption: "assumption text"
      risk: "low | medium | high"
      can_continue: true
      validation_needed: "how to validate"
  open_questions:
    - id: "Q-001"
      question: "question text"
      owner: "user | repo | docs | unknown"
      blocks:
        - "stage-name"
  blockers:
    - id: "BLK-001"
      blocker_type: "HARD_HALT_CONNECTOR | HARD_HALT_SOURCE_CONFLICT | HARD_HALT_APPROVAL | HARD_HALT_SECURITY | HARD_HALT_PRODUCTION | HARD_HALT_RELEASE_INTEGRITY | CODEX_BLOCKER"
      reason: "why continuation is unsafe"
      required_to_resume:
        - "specific fact or action"
  approval_gates:
    - id: "APP-001"
      gate: "approval needed"
      approver: "user | maintainer | release owner | unknown"
      status: "not_required | pending | approved | rejected | unknown"
  allowed_scope:
    - "files, modules, systems, or stages allowed"
  forbidden_scope:
    - "files, modules, systems, or stages forbidden"
  validation_commands:
    - command: "command"
      purpose: "why it matters"
      required_before: "implementation | review | release | deployment"
  evidence_inventory:
    - id: "EV-001"
      evidence_type: "test | ci | review | doc | PR | issue | log | metric | manual"
      reference: "path, PR, issue, job, or artifact"
      status: "present | missing | stale | conflicting | not_applicable"
  artifacts:
    - "artifact name or path"
  halt_conditions:
    - "plain-language halt condition"
  readiness:
    current_stage_status: "ready | partial | blocked | unknown"
    next_stage_status: "ready | partial | blocked | unknown"
    missing_required_inputs:
      - "input"
    soft_gaps:
      - "gap"
  codex_handoff:
    ready: false
    prompt_file: "path-or-none"
    max_context_policy: "execution_packet_only"
  ready_to_continue: true
```

Rules:
- Preserve source facts across desks rather than rediscovering them.
- Missing facts, missing decisions, and missing approvals are distinct categories.
- Auto-route upstream for recoverable missing detail.
- Use typed hard halts for connector, source conflict, approval, security/privacy, production, and release integrity risks.
- Child desks must emit both desk artifact output and an updated packet.

