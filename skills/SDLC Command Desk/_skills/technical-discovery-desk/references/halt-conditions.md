# Halt Conditions

Halt or produce a connector diagnostic when:

- Required GitHub repo context is unavailable.
- Required docs or product truth are unavailable.
- The selected repo does not match the user's stated project.
- The requested implementation path depends on unverified assumptions.
- External API or SDK behavior may have changed and cannot be verified.
- Security, privacy, compliance, production, or migration risk is material and unsupported by source facts.
- The user asks for PR execution before discovery can identify target files, risks, and validation gates.
- Source facts conflict and the user has not resolved the conflict.

A halt report must include:

- The blocking missing or conflicting fact
- The source needed to resolve it
- The safest partial conclusion
- The recommended next action
