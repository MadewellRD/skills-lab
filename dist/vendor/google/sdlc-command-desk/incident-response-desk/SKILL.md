---
name: incident-response-desk
description: create connector-grounded incident response, bug triage, severity classification, root cause analysis, hotfix handoff, follow-up issue, post-incident review, and production-support artifacts from incidents, alerts, logs, metrics, traces, recent deploys, github issues, pull requests, ci evidence, runbooks, and stakeholder updates. use when Gemini needs to triage a production failure, summarize an incident, draft an rca, plan a hotfix, map remediation work, or prepare downstream handoff notes for implementation-handoff-desk, ci-failure-desk, deployment-desk, observability-readiness-desk, release-operations-desk, verification-desk, or docs-traceability-desk workflows.
---

# Incident Response Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


Use this skill to create incident-response and production-support artifacts that are grounded in connector evidence. The skill owns triage, severity, impact, timeline, root cause, mitigation, hotfix planning, and follow-up work. It does not invent telemetry, deploy state, customer impact, ownership, or remediation proof.

## Operating workflow

**Outcome.** The artifact the situation calls for: an incident triage brief and action plan for a live incident or active degradation; an RCA or post-incident review for a resolved incident; a bug triage and reproduction plan for a bug report or regression; a hotfix handoff for `implementation-handoff-desk`; or remediation issues and verification gates for follow-up work.

**Grounding.** Run connector preflight before producing operational claims. GitHub carries issues, PRs, recent commits, release tags, CI/checks, changed files, and hotfix branches. Observability sources, when available, carry alerts, dashboards, logs, metrics, traces, and SLO/SLA status. Deployment and release docs carry recent deploys, feature flags, rollback plans, and release notes. Incident and communication sources carry status page notes, paging context, and stakeholder decisions. Product and docs sources carry runbooks, support docs, architecture docs, and known-issues docs.

**Fact separation.** State confirmed impact, suspected impact, confirmed cause, suspected cause, mitigations attempted, and unknowns separately. Do not collapse gaps into conclusions.

**Templates.** Use `references/output-contract.md` with the matching template: `incident-triage-template.md`, `rca-template.md`, `bug-triage-template.md`, `hotfix-handoff-template.md`, `post-incident-review-template.md`, or `follow-up-issues-template.md`.

**Parallel surface.** Evidence collection across independent sources — alerts, dashboards, log streams, recent deploys, affected services, linked issues and PRs — has no ordering dependency. Gather them in parallel and reconcile into one timeline. Building the timeline itself stays a single ordered narrative.

**Handoff.** When remediation requires code, continue into the implementation handoff stage if facts are sufficient. When CI is failing, continue into the CI failure stage. When monitoring or runbooks are missing, continue into observability readiness or docs traceability as appropriate.

**Packaging.** For downloadable markdown artifacts, use `scripts/write_incident_markdown.py` or the wrapper in `references/output-contract.md`.

**Acceptance bar.** The artifact is done when it satisfies `Output standards` below, impact and cause each carry an explicit confirmed-versus-suspected label, and the timeline is anchored to retrieved evidence rather than recollection.

## Severity policy

Use the severity rubric in `references/severity-rubric.md`. If severity cannot be determined from evidence, classify as `severity unknown` and list required facts. Do not downgrade severity because a root cause is unknown.

## Source hierarchy

Apply `references/source-hierarchy.md`. Current user instruction can set priority and desired output, but GitHub and telemetry connectors remain source of truth for code, deploy, check, and runtime evidence. Communication sources can confirm timeline and decisions, but should not override code or telemetry facts without explicit explanation.

## Halt rules

Proceed by default. An incomplete picture is normal during an incident: state what is unknown, label the working hypothesis as a hypothesis, and continue the triage. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval** — rollback, hotfix, or customer-communication authority is unclear or unassigned.
- **Production or destructive** — the proposed remediation could increase blast radius, touch production data, or is otherwise irreversible.
- **Security or privacy** — security or privacy exposure is suspected but not bounded.
- **Source conflict** — telemetry, deploy state, and incident reports genuinely disagree on a load-bearing fact such as what shipped or when impact began.
- **Release integrity** — the incident would be declared resolved or mitigated without recovery evidence.
- **Connector unreachable** — the incident is still active and the status source exists but cannot be read. Evidence that is merely absent is a soft gap: mark the artifact's confidence accordingly and continue.

Use `references/halt-conditions.md` for the diagnostic and resume format a halt must take.

## Output standards

Every incident artifact must include:

- Source facts used.
- Confidence level per major claim.
- Unknowns and required follow-up.
- Clear owner/action mapping when available.
- Verification gates for recovery or remediation.
- Downstream handoff notes when the next step belongs to another SDLC desk skill.

Never state that an incident is resolved unless the recovery evidence is present.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
