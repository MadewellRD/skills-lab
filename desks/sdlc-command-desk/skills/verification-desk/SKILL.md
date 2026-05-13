---
schema_version: "1.0"
name: verification-desk
description: >-
  Creates connector-grounded verification and validation artifacts. Maps
  requirements to evidence, assesses acceptance gates, identifies release
  blockers, and prepares downstream handoff notes for implementation, docs,
  or release work.
version: "1.0.0"

desk: sdlc-command-desk
lifecycle_stage:
  number: 8
  name: verification
role: leaf

inputs:
  - id: prd
    type: markdown
    required: true
    description: Product requirements document with acceptance criteria.
  - id: srs
    type: markdown
    required: false
    description: Software requirements specification, when produced separately from the PRD.
  - id: pr_diff
    type: github_pr
    required: false
    description: Pull request under verification (diff, checks, conversation).
  - id: ci_status
    type: ci_artifact
    required: false
    description: CI run results and logs for gate-status assessment.
  - id: test_strategy
    type: markdown
    required: false
    description: Test strategy document from test-strategy-desk.

outputs:
  - id: vv_report
    type: markdown
    filename: vv-report.md
    description: Verification and validation report summarizing evidence-to-requirement mapping.
  - id: rtm
    type: markdown
    filename: requirements-traceability-matrix.md
    description: Traceability matrix mapping each requirement to artifacts, tests, and PRs.
  - id: acceptance_gate_review
    type: markdown
    filename: acceptance-gate-review.md
    description: Review of acceptance gates, pass/fail status with evidence.
  - id: release_blockers
    type: markdown
    filename: release-blockers.md
    description: Identified blockers preventing release with severity and owner.
  - id: connector_diagnostic
    type: diagnostic
    filename: connector-diagnostic.md
    description: Emitted only when required connectors are missing or unauthorized.

connectors_required:
  - github
  - filesystem
connectors_optional:
  - drive
  - slack
  - linear

composes_from:
  - ref: product-requirements-desk
    version: "^1.0.0"
    reason: PRD and acceptance criteria are the verification anchor.
  - ref: architecture-design-desk
    version: "^1.0.0"
    reason: Design specs constrain what counts as adequate evidence.
  - ref: issue-planning-desk
    version: "^1.0.0"
    reason: Issue IDs anchor traceability matrix rows.
  - ref: test-strategy-desk
    version: "^1.0.0"
    reason: Test strategy defines coverage expectations.
  - ref: review-quality-desk
    version: "^1.0.0"
    reason: Review findings feed acceptance-gate decisions.

hands_off_to:
  - ref: implementation-handoff-desk
    version: "^1.0.0"
    reason: Verification gaps become implementation-agent prompts.
  - ref: release-operations-desk
    version: "^1.0.0"
    reason: Pass/fail readiness drives release decisions.
  - ref: docs-traceability-desk
    version: "^1.0.0"
    reason: Durable evidence maps live in docs/traceability.

capability_requirements:
  file_io: required
  script_execution: none
  tool_calling: required
  long_context: preferred
  multimodal: none
  workflow_packet: required

activation_hints:
  - "verify these requirements"
  - "is this release ready"
  - "build the requirements traceability matrix"
  - "check acceptance gates"
  - "list release blockers"
  - "verification and validation report"

provenance:
  author: MadewellRD
  sources:
    - https://github.com/MadewellRD/skills-lab
    - https://github.com/kcenon/claude_code_agent
    - https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC
  license: Apache-2.0

policy_ref: policy.yaml
---

## Purpose

`verification-desk` produces connector-grounded V&V artifacts that map every requirement to evidence and gate the release decision. It refuses to fabricate evidence: when source facts are missing, it emits a connector diagnostic and halts rather than inventing test coverage or acceptance status. The audience is SDLC orchestration via `sdlc-command-desk`, downstream consumption by `release-operations-desk`, and durable archival via `docs-traceability-desk`.

## Activation

Route to `verification-desk` when the user asks about release readiness, requirements verification, traceability matrices, acceptance-gate status, V&V reporting, or release blockers. Also activate when an upstream stage (review-quality-desk, test-strategy-desk) hands off completed work and the next lifecycle step is verification.

## Procedure

Run the following sequence on every invocation. Halt at the first stage where required source facts are missing and emit the corresponding diagnostic.

1. **Connector preflight.** Confirm `connectors_required` are wired and authorized. If `github` or `filesystem` is missing, emit `connector-diagnostic.md` and halt.

2. **Source-fact gathering.** Read the workflow packet's `source_facts` array. Identify which of the following are present: PRD/SRS, acceptance criteria, PR diff, CI status, test files, review findings, test strategy. Append a `source-facts-inventory` entry to `decisions` with what is present and what is missing.

3. **Requirements extraction.** From the PRD/SRS, extract every requirement with a stable id (e.g., REQ-001). For each, identify acceptance criteria. If no requirements can be extracted, halt with a `missing_requirements` diagnostic.

4. **Evidence mapping.** For each requirement id, search the available evidence sources for traces — test files matching the requirement, PR descriptions referencing the requirement, CI checks linked to the requirement. Record matches with source path and confidence.

5. **Traceability matrix construction.** Produce `requirements-traceability-matrix.md` with one row per requirement: id, statement, acceptance criteria, mapped evidence, gap. Order by requirement id.

6. **Acceptance-gate review.** For each requirement, classify the gate status: PASS (evidence sufficient), FAIL (evidence missing or contradictory), DEFERRED (out of scope for this release). Produce `acceptance-gate-review.md`.

7. **Release-blocker identification.** Filter FAIL rows whose requirements are in-scope for this release. Each is a blocker. Produce `release-blockers.md` with severity, owner (if known from GitHub PR/issue assignment), and remediation suggestion.

8. **V&V report.** Synthesize the above into `vv-report.md` covering: scope verified, evidence summary, gate decisions, open blockers, recommended next actions. Cite source facts inline; no claim without a source.

9. **Workflow packet update.** Append produced artifacts to `artifacts`. Append an `audit_trail` entry. Set `ready_to_continue` to true if no blockers remain or if all blockers are explicitly accepted; false otherwise. Set `next_stage` based on outcome.

## Output Contract

Every output artifact follows the same shape: a single H1 title, a `## Source facts` section listing facts grounding the artifact (with citations to workflow packet `source_facts` ids), the substantive content with inline citations, and an `## Audit` block with the producing skill name, version, and timestamp.

The `vv-report.md` artifact template:

```markdown
# V&V Report — <release or scope identifier>

## Source facts
- <fact-id>: <source>

## Scope verified
<prose>

## Evidence summary
<table or prose>

## Gate decisions
<table>

## Open blockers
<list>

## Recommended next actions
<list>

## Audit
- Skill: @MadewellRD/sdlc-command-desk/verification-desk@1.0.0
- Produced at: <ISO-8601 timestamp>
- Workflow packet: <packet id>
```

The `release-blockers.md` artifact must include for each blocker: id, requirement, severity (CRITICAL/HIGH/MEDIUM), owner, evidence gap, remediation suggestion.

The workflow packet must be updated with `ready_to_continue: false` whenever any CRITICAL or HIGH blocker remains unresolved.

## Halt Conditions

Halt and emit a connector-diagnostic or workflow-halt artifact (do not fabricate) when any of the following:

- `connectors_required` (github, filesystem) are missing or unauthorized.
- No requirements can be extracted from any provided source. The skill cannot verify what it cannot enumerate.
- Contradictory source facts about the same requirement appear without a tiebreaker (e.g., PRD says requirement is in-scope; release operations message says deferred). Surface the contradiction; let the architect resolve.
- Confidence in any individual gate decision falls below the policy threshold (default 0.6).
- Policy violation (e.g., a filesystem write attempted outside `allowed_paths`).

Each halt emits a workflow-halt entry to `halt_conditions` and an audit-trail entry with `halt: true`.

## Workflow Packet

`verification-desk` consumes and produces a workflow packet conforming to `ir-schema/v1.0/workflow-packet.schema.json`.

Required keys consumed:
- `source_facts` — the grounding facts the skill operates over.
- `completed_stages` — must include upstream stages this skill composes from when those upstreams exist in the active Desk run.

Keys produced or updated:
- `artifacts` — appended with the produced outputs.
- `decisions` — appended with `source-facts-inventory` and any tiebreaker decisions made.
- `open_questions` — populated with unresolved contradictions or missing-evidence questions.
- `halt_conditions` — appended on halt.
- `audit_trail` — appended with one entry per invocation, including `policy_decisions`.
- `ready_to_continue` — set per the rule in Output Contract.
- `next_stage` — set to `release-operations-desk` on success, or the relevant remediation skill on blockers.

## Composition

Upstream: `product-requirements-desk` (PRD anchor), `architecture-design-desk` (design constraints on evidence), `issue-planning-desk` (issue-id anchors for traceability), `test-strategy-desk` (coverage expectations), `review-quality-desk` (review findings feed gate decisions).

Downstream: `implementation-handoff-desk` (verification gaps become implementation prompts), `release-operations-desk` (readiness signal), `docs-traceability-desk` (durable evidence map).

This skill participates in cross-Desk composition: when invoked from `@MadewellRD/security-command-desk` for security-gate verification, it reads `inter_desk_context.shared_facts` to scope verification to security requirements only.

## References

- `references/output-templates/vv-report-template.md`
- `references/output-templates/rtm-template.md`
- `references/acceptance-gate-rubric.md`
