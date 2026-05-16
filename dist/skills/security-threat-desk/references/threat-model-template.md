# Threat Model Template

Use this for architecture, feature, API, auth, data-flow, or deployment threat models.

## Required structure

```markdown
# Threat Model: <system or feature>

## How to use this file
Use this model to review security risk, decide mitigations, and create downstream issues or PR prompts. Treat unresolved questions as blockers until answered or accepted.

## Scope
- In scope:
- Out of scope:
- Assessed version, branch, PR, or doc set:

## Source facts
- GitHub:
- Requirements/docs:
- Decisions/messages:
- External references:

## Assets and data classes
| Asset/data | Sensitivity | Storage/transit location | Owner | Evidence |
|---|---:|---|---|---|

## Actors and trust levels
| Actor | Trust level | Capabilities | Constraints |
|---|---:|---|---|

## Entry points
| Entry point | Auth required | Inputs | Downstream systems | Evidence |
|---|---|---|---|---|

## Trust boundaries and data flows
| Boundary | Crossing data | Controls | Missing controls | Evidence |
|---|---|---|---|---|

## Threat scenarios
| ID | Scenario | Category | Likelihood | Impact | Severity | Evidence | Mitigation |
|---|---|---|---:|---:|---:|---|---|

## Required mitigations
| Mitigation ID | Threat IDs | Action | Owner | Verification evidence |
|---|---|---|---|---|

## Release blockers
- Blocker:

## Open questions
- Question:

## Downstream handoff
- For architecture-design-desk:
- For issue-planning-desk:
- For verification-desk:
- For implementation-handoff-desk:
```

## Category guide

Prefer categories that fit the system. STRIDE is useful for general systems:

- Spoofing
- Tampering
- Repudiation
- Information disclosure
- Denial of service
- Elevation of privilege

Add privacy, supply-chain, abuse, or compliance categories when those are material.
