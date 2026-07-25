---
name: release-operations-desk
description: create connector-grounded release readiness, release notes, version and tag plans, rollback plans, deployment handoff notes, and post-release verification artifacts from merged pull requests, changelogs, ci evidence, deployment configuration, issue milestones, and release history. use when ChatGPT needs to prepare a release runbook, assess release blockers, package change summaries, define rollback or go/no-go gates, or hand off verified release work to implementation-handoff-desk, deployment-desk, verification-desk, ci-failure-desk, docs-traceability-desk, or incident-response-desk workflows.
---

# Release Operations Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Use this skill to prepare release operations artifacts for software delivery. The skill turns merged work, validation evidence, release scope, deployment context, and risk signals into release-ready Markdown artifacts.

This skill does not deploy, tag, publish, or merge by itself. It creates release decision and handoff material.

## Workflow

**Outcome.** The release artifact the request calls for — release readiness, release notes, a version or tag plan, a rollback plan, a go/no-go checklist, a post-release verification plan, or a downstream handoff — containing source facts, scope, exclusions, evidence, risks, rollback path, gates, owners where known, and handoff notes.

**Grounding.** Use GitHub for merged pull requests, commits, branches, tags, releases, CI checks, changed files, issues, milestones, and release history. Use document sources for roadmap, changelog, policy, runbooks, and compliance context. Use communication sources only for decision history and incident/release coordination when available.

**Source truth.** Apply `references/source-hierarchy.md`. If repo facts, release docs, or user-provided facts conflict, preserve the conflict in the output and halt before giving a go decision unless the current user explicitly resolves it.

**Artifact contract.** Use `references/output-contract.md` to choose the right Markdown artifact. Load the corresponding template only when needed.

**Ordered content is not scaffolding.** Version-and-tag sequences, gate ordering in a go/no-go checklist, and rollback steps are externally mandated order. Emit them as ordered, numbered steps and never reorder or collapse them.

**Parallel surface.** Merged pull requests, individual changelog entries, closed issues in a milestone, and per-gate evidence checks are independent of one another. Retrieve and classify them in parallel, then assemble into the ordered release artifact.

**Handoff.** If implementation, merge, tag, deployment, or hotfix work is required, prepare handoff notes for `implementation-handoff-desk`, `deployment-desk`, `verification-desk`, `ci-failure-desk`, or `incident-response-desk`.

**Acceptance bar.** The artifact is done when the release scope is bounded by a verifiable commit range, tag, or branch; every gate is classified as pass, fail, blocked, unknown, or not applicable with the evidence that supports the classification; user-facing and internal changes are separated in release notes; rollback steps are marked verified or unverified rather than presented uniformly; and any go decision is traceable to gate evidence rather than to absence of known problems. Do not invent release versions, tags, commit SHAs, merged PRs, CI status, deployment status, owners, rollback commands, or release approvals.

## Connector rules

GitHub is required for repo-specific release facts: commits, tags, PRs, issues, merged state, checks, branches, release artifacts, and compare ranges. Document connectors are required when the release depends on roadmap, policy, changelog, compliance, or customer-facing language. Communication connectors are optional and only support decision context.

If required release facts are unavailable, produce a connector diagnostic or a source-limited draft. Do not invent release versions, tags, commit SHAs, merged PRs, CI status, deployment status, owners, rollback commands, or release approvals.

## Output rules

Default to downloadable Markdown artifacts when the user asks for a runbook, release notes, plan, checklist, evidence packet, or handoff. Use concise prose and decision tables. Keep assumptions explicit.

For release notes, separate user-facing changes from internal changes. For readiness reports, classify each gate as pass, fail, blocked, unknown, or not applicable. For rollback plans, distinguish verified rollback steps from unverified fallback ideas.

## Halt rules

Proceed by default when drafting notes, plans, and readiness reports: an unknown gate is classified `unknown` with the missing evidence named, not turned into a stop. Release decisions are different — a go decision is a release-integrity act. Reserve hard halts for these consequence classes from `references/halt-taxonomy.md`:

- **Approval** — a release, tag, publish, or merge is requested without explicit execution authority.
- **Production or destructive** — the user asks this desk to actually deploy, tag, publish, or merge rather than produce the decision material. This desk does not execute.
- **Security or privacy** — a release decision depends on unresolved security, compliance, or privacy risk.
- **Source conflict** — release scope conflicts across sources, or the target version, tag, branch, or commit range cannot be established from repo state.
- **Release integrity** — a go decision would be issued while CI or verification evidence is missing for a gated release, or a rollback path is requested and the deployment surface is unknown.
- **Connector unreachable** — GitHub or a required release-doc source exists but cannot be read. A merely absent source is a soft gap: produce a source-limited draft marked as such and continue.

## References

- `references/release-readiness-template.md` for release readiness reports.
- `references/release-notes-template.md` for release notes.
- `references/version-tag-plan-template.md` for version and tag plans.
- `references/rollback-plan-template.md` for rollback plans.
- `references/post-release-verification.md` for post-release validation.
- `references/connector-routing.md` for required sources.
- `references/source-hierarchy.md` for truth precedence.
- `references/output-contract.md` for artifact selection.
- `references/handoff-rules.md` for downstream skill routing.
- `references/halt-conditions.md` for hard stop conditions.

## Script

Use `scripts/write_release_markdown.py` when a wrapped Markdown artifact file is needed. The script writes a title, usage instruction, prompt or report body, and optional source facts.
- `references/suite-workflow-contract.md`: shared workflow packet, continuation, and halt contract for SDLC Command Desk suite orchestration.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
