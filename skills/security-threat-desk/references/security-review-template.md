# Security Review Template

Use this for PR, design, release, dependency, or feature security reviews.

## Required structure

```markdown
# Security Review: <subject>

## How to use this file
Use this review to decide whether the change can proceed, needs mitigation work, or must halt until missing evidence is supplied.

## Review decision
Decision: proceed | proceed with mitigations | request changes | block release | connector diagnostic required

## Scope reviewed
- Repo/PR/branch/docs:
- Files/components:
- Requirements or acceptance criteria:

## Source facts
- GitHub facts:
- Requirement/design facts:
- Security/compliance facts:
- Unverified assumptions:

## Findings
| ID | Finding | Severity | Confidence | Affected surface | Evidence | Recommended action |
|---|---|---:|---:|---|---|---|

## Positive controls observed
- Control:

## Missing evidence
- Missing fact:

## Required mitigations
| Mitigation | Priority | Linked finding | Suggested owner | Verification method |
|---|---:|---|---|---|

## Release blockers
- Blocker:

## Downstream handoff
- Issue-planning notes:
- Verification notes:
- PR-command notes:
```

## Review discipline

Do not present plausible concerns as confirmed vulnerabilities. Mark them as risks or open questions. A confirmed finding needs evidence from source, docs, configuration, tests, logs, or a reproducible observation.
