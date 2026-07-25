# Halt Conditions

Halt or produce a connector diagnostic when:

- The target service, repo, environment, or deployment is unknown.
- The request asks for production readiness but monitoring or incident evidence is unavailable.
- The request asks for code-backed findings but GitHub source context is unavailable.
- Repo code, docs, dashboards, or incident notes conflict and the user has not resolved the conflict.
- SLOs, alert thresholds, owners, or escalation routes are required for the decision but missing.
- The user asks for implementation work rather than readiness analysis.
- Sensitive data logging or privacy risk is suspected but cannot be verified.

A diagnostic should list missing sources, why they matter, and the safest partial output that can still be produced.
