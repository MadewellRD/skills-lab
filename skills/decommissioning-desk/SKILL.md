---
name: decommissioning-desk
description: create connector-grounded decommissioning, api sunset, migration cutover, data retention, archive, rollback, and stakeholder communication artifacts for software delivery. use when chatgpt needs to retire a feature, service, api, dependency, integration, repository, job, flag, environment, data store, or product surface safely using github evidence, usage context, docs, release history, observability signals, compliance constraints, and downstream handoff notes for implementation-handoff-desk, deployment-desk, release-operations-desk, incident-response-desk, docs-traceability-desk, or verification-desk workflows.
---

# Decommissioning Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to plan safe retirement of software assets. The output must be connector-grounded and operational: it should identify what is being retired, who or what depends on it, how traffic/data/users move away, what must be retained, which rollback paths remain, and what downstream implementation handoff is required.

## Workflow

1. Classify the decommissioning target.
   - feature flag or feature surface
   - api endpoint, webhook, event, schema, or SDK surface
   - service, job, worker, repository, package, environment, or infrastructure component
   - data store, table, topic, bucket, artifact, or report
   - third-party integration or dependency

2. Run connector preflight using `references/connector-routing.md`.
   - Use GitHub for source truth: code references, owners, commits, issues, PRs, tests, deployment config, workflow files, and release history.
   - Use docs sources for product promises, runbooks, API docs, retention policies, roadmap status, and migration instructions.
   - Use observability or incident sources when runtime usage, error budget, traffic, logs, or alerts affect the plan.
   - Use issue/project sources for customer commitments, owners, blockers, and sunset milestones.

3. Decide whether a full plan is safe.
   If dependency, usage, retention, or rollback facts are missing, produce a connector diagnostic or an assumptions-explicit draft. Do not invent consumers, owners, usage volume, policy requirements, or cutover dates.

4. Produce the right artifact.
   - Decommission plan: use `references/decommission-plan-template.md`.
   - API sunset plan: use `references/api-sunset-template.md`.
   - Migration/cutover plan: use `references/cutover-plan-template.md`.
   - Data retention/archive plan: use `references/data-retention-template.md`.
   - Communication plan: use `references/communication-plan-template.md`.
   - Risk/rollback checklist: use `references/rollback-risk-template.md`.

5. Create downstream handoff notes.
   Use `references/handoff-rules.md` when the decommissioning plan needs follow-up implementation prompts, docs updates, verification work, release/deploy gates, or incident-support readiness.

## Required behavior

- Separate confirmed source facts from assumptions.
- Treat active usage, unresolved consumers, unknown retention requirements, and unclear rollback paths as blocking risks.
- Prefer staged retirement over hard deletion when usage or ownership is uncertain.
- Include explicit pre-cutover, cutover, post-cutover, and rollback gates.
- Include docs, support, and stakeholder communication work when users or external consumers are affected.
- Include verification gates for absence of traffic, absence of dependent references, passing tests, and clean monitoring after removal.
- Keep deletion scope narrow and auditable.

## Output rules

For final user-facing artifacts, produce downloadable Markdown whenever tools allow. Use `scripts/write_decommissioning_markdown.py` to wrap a generated plan into a file with a `How to use this file` section. Include source facts and unverified assumptions either in the artifact or in a companion source-notes section.

## Composition with other desks

- Use `implementation-handoff-desk` after this skill when the decommissioning plan must become implementation-agent PR prompts.
- Use `deployment-desk` for rollout and cutover gates.
- Use `release-operations-desk` for release notes, version tags, and rollback plans.
- Use `verification-desk` to prove acceptance gates and post-retirement checks.
- Use `docs-traceability-desk` for API docs, runbooks, proof maps, and stale-doc cleanup.
- Use `incident-response-desk` if decommissioning follows a production incident or requires support readiness.

## Halt conditions

Halt or produce a connector diagnostic when:

- the target to retire is ambiguous;
- live consumers or owners cannot be determined;
- usage/traffic evidence is unavailable but required;
- data retention or compliance obligations are unknown;
- the requested retirement conflicts with public docs, API contracts, customer commitments, or active issues;
- rollback paths are impossible or unproven;
- deletion scope reaches unrelated files, systems, or dependencies;
- required source facts cannot be verified through available connectors.

## References

- `references/decommission-plan-template.md`: full retirement plan structure.
- `references/api-sunset-template.md`: API and integration sunset planning.
- `references/cutover-plan-template.md`: migration and staged cutover planning.
- `references/data-retention-template.md`: data retention, archive, and deletion controls.
- `references/communication-plan-template.md`: stakeholder, customer, support, and docs communication.
- `references/rollback-risk-template.md`: risks, gates, and rollback criteria.
- `references/connector-routing.md`: connector requirements by decommissioning target.
- `references/source-hierarchy.md`: truth precedence and conflict handling.
- `references/output-contract.md`: artifact formats and source-fact requirements.
- `references/handoff-rules.md`: downstream SDLC handoff rules.
- `references/halt-conditions.md`: stop conditions and diagnostic behavior.
- `references/suite-workflow-contract.md`: shared workflow packet, continuation, and halt contract for SDLC Command Desk suite orchestration.
