# Security Risk Rubric

Use this rubric to classify security findings consistently.

## Severity

Critical: likely unauthorized access to sensitive data, privilege escalation, remote code execution, production secret exposure, cross-tenant isolation failure, or release-blocking compliance violation.

High: exploitable auth/authz gap, sensitive data disclosure, material supply-chain risk, destructive action without adequate authorization, or missing control on a high-value entry point.

Medium: plausible abuse path requiring constraints, missing defense-in-depth on moderate-risk surface, weak validation, incomplete logging, or dependency risk without immediate exploit evidence.

Low: documentation gap, minor hardening item, limited-scope misconfiguration, or weak evidence risk that does not block delivery.

## Confidence

High: verified in code, config, tests, logs, or official docs.

Medium: strongly implied by multiple sources but missing one direct proof point.

Low: plausible concern requiring more evidence.

## Release blocking

Mark a finding as release-blocking when exploitation could materially compromise confidentiality, integrity, availability, compliance posture, tenant isolation, or credential safety before a mitigation can be shipped.
