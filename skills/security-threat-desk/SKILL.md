---
name: security-threat-desk
description: create connector-grounded security and threat-modeling artifacts for software delivery. use when chatgpt needs to assess security risk, build threat models, identify trust boundaries, review authentication or authorization surfaces, evaluate dependency and secret exposure, map mitigations to requirements, or prepare downstream handoff notes for architecture-design-desk, issue-planning-desk, verification-desk, review-quality-desk, ci-failure-desk, or implementation-handoff-desk workflows.
---

# Security Threat Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


Use this skill to turn requirements, architecture, repo state, dependency context, and delivery plans into security review artifacts that are traceable, actionable, and safe to hand off.

## Core workflow

1. Classify the request.
   - Threat model: use `references/threat-model-template.md`.
   - Security review: use `references/security-review-template.md`.
   - Trust-boundary or data-flow review: use `references/trust-boundary-template.md`.
   - Dependency, secret, or supply-chain review: use `references/dependency-secret-review.md`.
   - Downstream implementation handoff: use `references/handoff-rules.md`.

2. Run connector preflight.
   Use `references/connector-routing.md` before making claims about code, branches, PRs, issues, dependencies, CI, or policy. GitHub is source of truth for code, dependency manifests, workflow files, PRs, commits, issues, and checks. Specs and docs are source of truth for requirements, architecture, compliance, privacy, and business policy. Communication sources are decision context only.

3. Establish the source hierarchy.
   Apply `references/source-hierarchy.md`. Current user instruction can set priority. GitHub controls repo facts. Product, architecture, and compliance docs control intent. Public sources can only support external framework or library facts.

4. Produce the security artifact.
   Use the smallest sufficient artifact: threat model, review report, trust-boundary map, dependency/secrets review, mitigation backlog, or downstream handoff. Include source facts, assumptions, risks, severity, likelihood, impact, mitigations, owners when known, and unresolved questions.

5. Halt rather than invent.
   If required connector facts are unavailable, produce a connector-needed diagnostic or explicitly mark the artifact as user-fact-only. Do not invent code paths, auth behavior, data classes, secrets exposure, dependency versions, compliance obligations, or CI status.

## Security analysis rules

- Prefer concrete attack surfaces over generic advice.
- Separate confirmed findings from plausible risks and open questions.
- Map each risk to affected assets, actors, entry points, trust boundaries, and mitigations.
- Call out missing evidence explicitly.
- Do not provide exploit instructions that increase harm. Keep remediation practical and defensive.
- When a finding requires code changes, prepare handoff notes for `issue-planning-desk` or `implementation-handoff-desk` rather than drafting unbounded implementation work.
- When a finding blocks release, prepare evidence for `verification-desk` or `release-operations-desk`.

## Output requirements

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
