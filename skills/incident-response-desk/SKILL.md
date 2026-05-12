---
name: incident-response-desk
description: create connector-grounded incident response, bug triage, severity classification, root cause analysis, hotfix handoff, follow-up issue, post-incident review, and production-support artifacts from incidents, alerts, logs, metrics, traces, recent deploys, github issues, pull requests, ci evidence, runbooks, and stakeholder updates. use when chatgpt needs to triage a production failure, summarize an incident, draft an rca, plan a hotfix, map remediation work, or prepare downstream handoff notes for implementation-handoff-desk, ci-failure-desk, deployment-desk, observability-readiness-desk, release-operations-desk, verification-desk, or docs-traceability-desk workflows.
---

# Incident Response Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


Use this skill to create incident-response and production-support artifacts that are grounded in connector evidence. The skill owns triage, severity, impact, timeline, root cause, mitigation, hotfix planning, and follow-up work. It does not invent telemetry, deploy state, customer impact, ownership, or remediation proof.

## Operating workflow

1. Classify the request.
   - Live incident or active degradation: produce an incident triage brief and action plan.
   - Resolved incident: produce an RCA or post-incident review.
   - Bug report or regression: produce a bug triage and reproduction plan.
   - Hotfix needed: produce a hotfix handoff for `implementation-handoff-desk`.
   - Follow-up work: produce remediation issues and verification gates.

2. Run connector preflight before producing operational claims.
   - GitHub: issues, PRs, recent commits, release tags, CI/checks, changed files, hotfix branches.
   - Observability sources, if available: alerts, dashboards, logs, metrics, traces, SLO/SLA status.
   - Deployment/release docs: recent deploys, feature flags, rollback plans, release notes.
   - Incident/comms sources: Slack, Teams, email, status page notes, paging context, stakeholder decisions.
   - Product/docs sources: runbooks, support docs, architecture docs, known-issues docs.

3. Separate facts from inference.
   State confirmed impact, suspected impact, confirmed cause, suspected cause, mitigations attempted, and unknowns separately. Do not collapse gaps into conclusions.

4. Choose the artifact type.
   Use `references/output-contract.md` and the relevant template:
   - `incident-triage-template.md`
   - `rca-template.md`
   - `bug-triage-template.md`
   - `hotfix-handoff-template.md`
   - `post-incident-review-template.md`
   - `follow-up-issues-template.md`

5. Add handoff notes.
   When remediation requires code, continue into the implementation handoff stage if facts are sufficient. When CI is failing, continue into the CI failure stage. When monitoring or runbooks are missing, continue into observability readiness or docs traceability as appropriate.

6. Package artifact output.
   For downloadable markdown artifacts, use `scripts/write_incident_markdown.py` or the wrapper in `references/output-contract.md`.

## Severity policy

Use the severity rubric in `references/severity-rubric.md`. If severity cannot be determined from evidence, classify as `severity unknown` and list required facts. Do not downgrade severity because a root cause is unknown.

## Source hierarchy

Apply `references/source-hierarchy.md`. Current user instruction can set priority and desired output, but GitHub and telemetry connectors remain source of truth for code, deploy, check, and runtime evidence. Communication sources can confirm timeline and decisions, but should not override code or telemetry facts without explicit explanation.

## Halt rules

Use `references/halt-conditions.md`. Halt or produce a connector diagnostic when required facts are unavailable, when the incident is still active but no current status can be verified, when proposed remediation could increase blast radius, when rollback or hotfix authority is unclear, or when security/privacy exposure is suspected but not bounded.

## Output standards

Every incident artifact must include:

- Source facts used.
- Confidence level per major claim.
- Unknowns and required follow-up.
- Clear owner/action mapping when available.
- Verification gates for recovery or remediation.
- Downstream handoff notes when the next step belongs to another SDLC desk skill.

Never state that an incident is resolved unless the recovery evidence is present.
