# Halt Conditions

Halt or produce a connector diagnostic when:

- The user asks for live incident status but no current status source is available.
- Recovery or resolution cannot be verified.
- Severity depends on unverified customer impact, data loss, security exposure, or revenue impact.
- Root cause is unknown but the requested artifact requires final RCA language.
- The remediation path could increase blast radius.
- Rollback, hotfix, or deploy authority is unclear.
- Recent deploy or commit state conflicts across sources.
- Logs, metrics, traces, or CI evidence are unavailable but essential to the claim.
- A security/privacy exposure is suspected but not bounded.
- The user asks to merge, deploy, or close the incident without validation evidence.

Diagnostic output must list missing sources, why they matter, and the safest next artifact that can be produced from available facts.
