---
name: release-operations-desk
description: create connector-grounded release readiness, release notes, version and tag plans, rollback plans, deployment handoff notes, and post-release verification artifacts from merged pull requests, changelogs, ci evidence, deployment configuration, issue milestones, and release history. use when chatgpt needs to prepare a release runbook, assess release blockers, package change summaries, define rollback or go/no-go gates, or hand off verified release work to implementation-handoff-desk, deployment-desk, verification-desk, ci-failure-desk, docs-traceability-desk, or incident-response-desk workflows.
---

# Release Operations Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Use this skill to prepare release operations artifacts for software delivery. The skill turns merged work, validation evidence, release scope, deployment context, and risk signals into release-ready Markdown artifacts.

This skill does not deploy, tag, publish, or merge by itself. It creates release decision and handoff material.

## Workflow

1. Classify the release request.
   Determine whether the user needs release readiness, release notes, a version or tag plan, a rollback plan, a go/no-go checklist, a post-release verification plan, or a downstream handoff.

2. Run connector preflight.
   Use GitHub for merged pull requests, commits, branches, tags, releases, CI checks, changed files, issues, milestones, and release history. Use document sources for roadmap, changelog, policy, runbooks, and compliance context. Use communication sources only for decision history and incident/release coordination when available.

3. Resolve source truth.
   Apply `references/source-hierarchy.md`. If repo facts, release docs, or user-provided facts conflict, preserve the conflict in the output and halt before giving a go decision unless the current user explicitly resolves it.

4. Select the artifact contract.
   Use `references/output-contract.md` to choose the right Markdown artifact. Load the corresponding template only when needed.

5. Produce a release artifact.
   Include source facts, scope, exclusions, evidence, risks, rollback path, gates, owners when known, and downstream handoff notes.

6. Hand off when execution is required.
   If implementation, merge, tag, deployment, or hotfix work is required, prepare handoff notes for `implementation-handoff-desk`, `deployment-desk`, `verification-desk`, `ci-failure-desk`, or `incident-response-desk`.

## Connector rules

GitHub is required for repo-specific release facts: commits, tags, PRs, issues, merged state, checks, branches, release artifacts, and compare ranges. Document connectors are required when the release depends on roadmap, policy, changelog, compliance, or customer-facing language. Communication connectors are optional and only support decision context.

If required release facts are unavailable, produce a connector diagnostic or a source-limited draft. Do not invent release versions, tags, commit SHAs, merged PRs, CI status, deployment status, owners, rollback commands, or release approvals.

## Output rules

Default to downloadable Markdown artifacts when the user asks for a runbook, release notes, plan, checklist, evidence packet, or handoff. Use concise prose and decision tables. Keep assumptions explicit.

For release notes, separate user-facing changes from internal changes. For readiness reports, classify each gate as pass, fail, blocked, unknown, or not applicable. For rollback plans, distinguish verified rollback steps from unverified fallback ideas.

## Halt rules

Halt or produce a diagnostic when:

- release scope is unclear or conflicts across sources
- target version, tag, branch, or commit range cannot be verified
- CI or verification evidence is missing for a gated release
- deployment or rollback path is requested but the deployment surface is unknown
- the user asks for actual deployment, tagging, publishing, or merging without explicit execution authority and available tooling
- a release decision depends on unresolved security, compliance, or incident risk

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

Use `references/continuity-kernel.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/codex-conservation-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `CODEX_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
