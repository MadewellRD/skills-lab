# V&V Report Template

Use this structure for verification and validation reports.

```markdown
# Verification and Validation Report: [subject]

## Executive summary
State whether the work is verified, partially verified, blocked, or not ready. Include the strongest evidence and the most important gap.

## Scope verified
List PRs, commits, issues, requirements, files, releases, or artifacts included in scope.

## Source facts
Record the exact sources used: requirement docs, GitHub PRs, commits, test files, CI runs, artifacts, and QA notes.

## Requirement inventory
List each requirement with stable IDs. If source requirements lack IDs, assign temporary IDs and mark them as generated for this report.

## Evidence inventory
List available evidence: tests, CI checks, logs, screenshots, review comments, docs, commits, and manual QA evidence.

## Requirements traceability
Embed or link to the RTM. Every requirement must map to evidence or a gap.

## Acceptance-gate status
Classify each gate as passed, partial, failed, blocked, or not assessed.

## Blockers and gaps
List release blockers first. Separate evidence gaps from implementation gaps.

## Risk assessment
Identify residual delivery, quality, security, compliance, operational, or documentation risks.

## Decision
Use one: ready, ready with documented risk, not ready, blocked, or insufficient evidence.

## Downstream handoff
List required follow-up work and continue into the appropriate next stage when facts are sufficient.
```
