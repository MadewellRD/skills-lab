---
name: decommissioning-desk
description: create connector-grounded decommissioning, api sunset, migration cutover, data retention, archive, rollback, and stakeholder communication artifacts for software delivery. use when Gemini needs to retire a feature, service, api, dependency, integration, repository, job, flag, environment, data store, or product surface safely using github evidence, usage context, docs, release history, observability signals, compliance constraints, and downstream handoff notes for implementation-handoff-desk, deployment-desk, release-operations-desk, incident-response-desk, docs-traceability-desk, or verification-desk workflows.
---

# Decommissioning Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to plan safe retirement of software assets. The output must be connector-grounded and operational: it should identify what is being retired, who or what depends on it, how traffic/data/users move away, what must be retained, which rollback paths remain, and what downstream implementation handoff is required.

## Workflow

**Outcome.** A retirement plan for the identified target, grounded in connector evidence, with staged gates and a rollback path.

**Target classification.** Establish exactly what is being retired: a feature flag or feature surface; an API endpoint, webhook, event, schema, or SDK surface; a service, job, worker, repository, package, environment, or infrastructure component; a data store, table, topic, bucket, artifact, or report; or a third-party integration or dependency.

**Grounding.** Run connector preflight using `references/connector-routing.md`. Use GitHub for source truth: code references, owners, commits, issues, PRs, tests, deployment config, workflow files, and release history. Use docs sources for product promises, runbooks, API docs, retention policies, roadmap status, and migration instructions. Use observability or incident sources when runtime usage, error budget, traffic, logs, or alerts affect the plan. Use issue/project sources for customer commitments, owners, blockers, and sunset milestones.

**Artifact selection.** Decommission plans use `references/decommission-plan-template.md`. API sunset plans use `references/api-sunset-template.md`. Migration and cutover plans use `references/cutover-plan-template.md`. Data retention and archive plans use `references/data-retention-template.md`. Communication plans use `references/communication-plan-template.md`. Risk and rollback checklists use `references/rollback-risk-template.md`.

**Parallel surface.** Consumer discovery fans out: code references, dependent services, API callers, docs mentions, dashboards, and open issues touching the target are independent searches. Run them in parallel to build the dependency picture. The cutover sequence the plan produces is not parallel, see below.

**Cutover order is content, not scaffolding.** Pre-cutover, cutover, post-cutover, and rollback gates are externally mandated order and the consequence of getting them wrong is irreversible. Emit them as ordered, numbered steps in the artifact. Never reorder, merge, or collapse them, and never present deletion before the traffic-absence and dependency-absence gates that authorize it.

**Downstream handoff.** Use `references/handoff-rules.md` when the plan needs follow-up implementation prompts, docs updates, verification work, release or deploy gates, or incident-support readiness.

**Acceptance bar.** The plan is done when every known consumer is named with the evidence that found it; retention and compliance obligations are stated or explicitly flagged as undetermined; each gate has an owner and an observable pass condition; the rollback path is stated and marked verified or unverified; and deletion scope is enumerated file-by-file or resource-by-resource rather than described in general terms. Do not invent consumers, owners, usage volume, policy requirements, or cutover dates. When dependency, usage, retention, or rollback facts are absent, produce an assumptions-explicit draft rather than a confident plan.

## Required behavior

- Separate confirmed source facts from assumptions.
- Treat active usage, unresolved consumers, unknown retention requirements, and unclear rollback paths as blocking risks.
- Prefer staged retirement over hard deletion when usage or ownership is uncertain.
- Include explicit pre-cutover, cutover, post-cutover, and rollback gates.
- Include docs, support, and stakeholder communication work when users or external consumers are affected.
- Include verification gates for absence of traffic, absence of dependent references, passing tests, and clean monitoring after removal.
- Keep deletion scope narrow and auditable.

## Output rules

A retirement run delivers a set, not a single plan: the retirement plan itself, the consumer and dependency map that justifies it, the communication plan for whoever depends on the target, the retention and archive decision for its data, and the rollback and risk checklist. They belong to the same run because a plan without its consumer map cannot be evaluated and a cutover without its rollback cannot be approved.

Two things in that set are genuinely conditional rather than optional. The plan shape follows the target classification: an API, webhook, event, or SDK surface takes the sunset shape in `references/api-sunset-template.md`, and every other target takes `references/decommission-plan-template.md`; one or the other, never both. A cutover plan joins the set when a replacement exists to migrate onto, and is correctly absent when nothing is replacing the target.

Each piece is finished when an operator could run it. Deletion scope is enumerated resource by resource. Each gate has an owner and an observable pass condition. The communication plan names the audience, the channel, the notice period, and who sends it. The rollback checklist states what is reversible, for how long, and by whom. Cutover ordering stays exactly as the workflow requires.

Consumer discovery fans out across independent searches, so the evidence behind these artifacts is gathered in parallel; the cutover sequence inside the plan is not.

None of this authorizes filling a gap to finish the set. Consumers, usage volume, retention obligations, owners, and cutover dates are sourced or named as unknown, and a retention decision with no policy behind it is flagged undetermined rather than assumed. An invented consumer list is the failure that gets a live dependency deleted.

For final user-facing artifacts, produce downloadable Markdown whenever tools allow. Use `scripts/write_decommissioning_markdown.py` to wrap a generated plan into a file with a `How to use this file` section. Include source facts and unverified assumptions either in the artifact or in a companion source-notes section.

## Composition with other desks

- Use `implementation-handoff-desk` after this skill when the decommissioning plan must become implementation-agent PR prompts.
- Use `deployment-desk` for rollout and cutover gates.
- Use `release-operations-desk` for release notes, version tags, and rollback plans.
- Use `verification-desk` to prove acceptance gates and post-retirement checks.
- Use `docs-traceability-desk` for API docs, runbooks, proof maps, and stale-doc cleanup.
- Use `incident-response-desk` if decommissioning follows a production incident or requires support readiness.

## Halt conditions

This desk plans irreversible work, so its halt surface is deliberately wide. Proceed and label the assumption for planning-level unknowns; an ambiguous naming question or an undetermined sunset date is a soft gap. Hard-halt for these consequence classes from `references/halt-taxonomy.md`, and do not soften them:

- **Approval**: retirement affects customers, external consumers, or contractual commitments and no human has authorized it.
- **Production or destructive**: rollback paths are impossible or unproven, deletion scope reaches unrelated files, systems, or dependencies, or the request asks to execute the retirement rather than plan it.
- **Security or privacy**: data retention or compliance obligations for the affected data are unknown.
- **Source conflict**: the requested retirement conflicts with public docs, API contracts, customer commitments, or active issues.
- **Release integrity**: the plan would declare the target safe to remove while live consumers or owners cannot be determined, or usage and traffic evidence is required and unavailable.
- **Connector unreachable**: a source needed to establish consumers or usage exists but cannot be read. Absence of evidence is not evidence of no consumers: treat unproven non-use as blocking, and prefer staged retirement over deletion whenever usage or ownership is uncertain.

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

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
