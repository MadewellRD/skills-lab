# Incident Triage Template

```markdown
# Incident Triage: [short incident name]

## Status
- Current state: [active / mitigated / resolved / unknown]
- Severity: [SEV0 / SEV1 / SEV2 / SEV3 / unknown]
- Confidence: [high / medium / low]

## Impact
- Affected systems:
- Affected users/customers:
- User-visible symptoms:
- Business impact:
- Data/security/privacy exposure:

## Timeline
| Time | Source | Event | Confidence |
|---|---|---|---|

## Current evidence
- Telemetry:
- GitHub/release/deploy state:
- Communication/status evidence:
- Runbook/doc evidence:

## Suspected cause
- Confirmed cause:
- Hypotheses:
- Evidence needed:

## Actions taken
| Time | Owner | Action | Result |
|---|---|---|---|

## Recommended next actions
| Priority | Owner | Action | Verification gate |
|---|---|---|---|

## Downstream handoff
- implementation-handoff-desk:
- ci-failure-desk:
- deployment-desk:
- observability-readiness-desk:
- docs-traceability-desk:

## Source facts used

## Unknowns and halt conditions
```
