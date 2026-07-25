---
name: security-threat-desk
description: create connector-grounded security and threat-modeling artifacts for software delivery. use when Gemini needs to assess security risk, build threat models, identify trust boundaries, review authentication or authorization surfaces, evaluate dependency and secret exposure, map mitigations to requirements, or prepare downstream handoff notes for architecture-design-desk, issue-planning-desk, verification-desk, review-quality-desk, ci-failure-desk, or implementation-handoff-desk workflows.
---

# Security Threat Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


Use this skill to turn requirements, architecture, repo state, dependency context, and delivery plans into security review artifacts that are traceable, actionable, and safe to hand off.

## Core workflow

**Outcome.** The smallest sufficient security artifact: threat model, review report, trust-boundary map, dependency/secrets review, mitigation backlog, or downstream handoff.

**Artifact selection.** Threat models use `references/threat-model-template.md`. Security reviews use `references/security-review-template.md`. Trust-boundary or data-flow reviews use `references/trust-boundary-template.md`. Dependency, secret, or supply-chain reviews use `references/dependency-secret-review.md`. Downstream implementation handoff uses `references/handoff-rules.md`.

**Grounding.** Run connector preflight per `references/connector-routing.md` before making claims about code, branches, PRs, issues, dependencies, CI, or policy. GitHub is source of truth for code, dependency manifests, workflow files, PRs, commits, issues, and checks. Specs and docs are source of truth for requirements, architecture, compliance, privacy, and business policy. Communication sources are decision context only.

**Source hierarchy.** Apply `references/source-hierarchy.md`. Current user instruction can set priority. GitHub controls repo facts. Product, architecture, and compliance docs control intent. Public sources can only support external framework or library facts.

**Parallel surface.** Trust boundaries, entry points, authentication surfaces, dependency manifests, and individual findings are independent analysis units. Examine them in parallel rather than iterating serially, then reconcile into a single ranked risk set.

**Acceptance bar.** The artifact is done when every risk names its affected assets, actors, entry points, and trust boundaries; carries severity, likelihood, and impact; and maps to at least one mitigation with an owner where the owner is known from sources. Confirmed findings, plausible risks, and open questions must be visibly separated, and missing evidence called out rather than filled in. Do not invent code paths, auth behavior, data classes, secrets exposure, dependency versions, compliance obligations, or CI status. When required connector facts are absent, mark the artifact user-fact-only and continue.

## Security analysis rules

- Prefer concrete attack surfaces over generic advice.
- Separate confirmed findings from plausible risks and open questions.
- Map each risk to affected assets, actors, entry points, trust boundaries, and mitigations.
- Call out missing evidence explicitly.
- Do not provide exploit instructions that increase harm. Keep remediation practical and defensive.
- When a finding requires code changes, prepare handoff notes for `issue-planning-desk` or `implementation-handoff-desk` rather than drafting unbounded implementation work.
- When a finding blocks release, prepare evidence for `verification-desk` or `release-operations-desk`.

## Halt policy

Proceed by default. An unresolved security question is normally a finding to record, not a reason to stop: state the assumption inline and continue the assessment. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval**: a mitigation, exception, or risk acceptance needs human authorization.
- **Production or destructive**: the recommended action touches production systems, credentials, or live access control.
- **Security or privacy**: proceeding would expose secrets, credentials, or personal data, or the request asks for material that increases attacker capability.
- **Source conflict**: repo state and policy or compliance documentation genuinely disagree on a load-bearing control.
- **Release integrity**: a security gate would be reported as cleared when its result cannot be established.
- **Connector unreachable**: a required source exists but cannot be read. Evidence that is merely absent is a soft gap: produce a connector-needed diagnostic or a user-fact-only artifact and continue.

## Output requirements

A security run delivers the set: the trust-boundary and data-flow picture, the threat model built on it, the dependency and secrets review, the ranked findings with severity and likelihood, and the mitigation backlog mapped to those findings, plus handoff notes when code changes follow. A threat model without a mitigation backlog leaves the reader holding risk and no route out of it; a findings list with no boundary map cannot be checked for what it missed.

Depth is where security artifacts fail quietly. A finding names the asset, the actor, the entry point, and the boundary crossed, and its mitigation names the control and where it is enforced. A dependency review names the package, the version observed, and the exposure, rather than saying dependencies should be updated. Advice that would apply to any system is not a finding about this one.

Trust boundaries, entry points, auth surfaces, and dependency manifests are independent analysis units, so the pieces of the set are examined and drafted in parallel, then reconciled into one ranked risk set.

Completing the set never justifies asserting a control. Code paths, auth behavior, data classes, secret exposure, dependency versions, compliance obligations, and CI status come from sources or are marked absent, and a control whose state could not be established is `unverified` rather than in place. When required connector facts are missing, mark the artifact user-fact-only and let it be short; a confidently wrong security claim gets a real risk closed on paper.

Default to downloadable Markdown artifacts when producing reports, models, checklists, handoffs, or diagnostics. Include a `How to use this file` section when the artifact is intended for another agent or reviewer.

For deterministic file wrapping, use `scripts/write_security_markdown.py` when a local artifact file is requested.

## References

- `references/threat-model-template.md`: threat model structure.
- `references/security-review-template.md`: security review report structure.
- `references/trust-boundary-template.md`: trust boundary and data-flow review.
- `references/dependency-secret-review.md`: dependency, secrets, and supply-chain checklist.
- `references/risk-rubric.md`: severity, likelihood, and release-blocking rubric.
- `references/connector-routing.md`: connector requirements by task.
- `references/source-hierarchy.md`: source precedence and conflict handling.
- `references/output-contract.md`: artifact names and output rules.
- `references/handoff-rules.md`: downstream SDLC handoffs.
- `references/halt-conditions.md`: mandatory stop conditions.
- `references/suite-workflow-contract.md`: shared workflow packet, continuation, and halt contract for SDLC Command Desk suite orchestration.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
