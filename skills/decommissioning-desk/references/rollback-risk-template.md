# Rollback and Risk Template

## Risk rubric

Classify risks as:

- Critical: customer-impacting outage, data loss, security/privacy violation, unrecoverable cutover, legal/compliance breach.
- High: significant consumer breakage, hard rollback, incomplete migration, missing owner, uncertain usage.
- Medium: local regression, doc inconsistency, delayed migration, limited support burden.
- Low: isolated cleanup with clear ownership and passing validation.

## Risk table

| Risk | Class | Evidence | Mitigation | Owner | Halt trigger |
|---|---|---|---|---|---|

## Rollback plan

- What can be restored:
- How to restore it:
- Who can approve rollback:
- Maximum rollback window:
- Data restore considerations:
- Verification after rollback:

## No-go criteria

- Unknown active consumers.
- Retention/compliance ambiguity.
- Replacement not verified.
- Monitoring absent.
- Rollback not tested for high-risk changes.
