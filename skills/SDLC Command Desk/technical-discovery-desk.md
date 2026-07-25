---
name: technical-discovery-desk
description: create connector-grounded technical discovery memos, repo reconnaissance reports, feasibility assessments, spike plans, risk registers, unknowns lists, and downstream handoff notes before architecture or implementation work. use when the user asks to investigate technical feasibility, inspect a repo before planning, research dependencies or integrations, compare implementation options, identify unknowns, map risks, plan a spike, or prepare technical input for architecture-design-desk, issue-planning-desk, or implementation-handoff-desk.
---

# Technical Discovery Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Use this skill to turn early product or engineering intent into a grounded technical discovery package. The skill is pre-architecture and pre-implementation: it investigates what exists, what is feasible, what is risky, what remains unknown, and what must be decided before design or PR work begins.

Do not write implementation prompts with this skill. When the user is ready for branch/PR execution, continue into the implementation handoff stage with a clear discovery summary and source facts when implementation-readiness facts are present.

## Workflow

**Outcome.** The discovery artifact the request calls for:

- Repo reconnaissance report: code structure, build system, tests, dependencies, ownership, and recent change history. Default for unfamiliar codebases.
- Feasibility assessment: whether a product requirement can be implemented under current constraints. Default for "can we build this?" questions.
- Integration discovery: external APIs, SDKs, service boundaries, auth, rate limits, and failure modes.
- Spike plan: a bounded investigation with questions, commands, expected artifacts, and stop conditions. Default when implementation is premature.
- Risk and unknowns analysis: proven facts separated from assumptions, blockers, and decisions needed.
- Technical discovery memo: default for broad investigation.
- Connector diagnostic: when required sources are unreachable.

**Grounding.** Use GitHub for repo facts, files, commits, PRs, issues, CI checks, dependency manifests, tests, and build scripts. Use docs connectors or uploaded docs for PRDs, roadmaps, architecture docs, design notes, audit packs, and decisions. Use issue/project connectors for ticket scope, acceptance criteria, priority, labels, owners, and blockers. Use communication connectors only for recent decision context or agent halt reports. Use public web only for external APIs, SDKs, standards, vendor docs, or current tool behavior not present in repo or docs.

**Source hierarchy.** Prefer current user instruction, then live GitHub state, then live issue/project state, then canonical docs, then decision-bearing communications, then public web for external facts, then explicit assumptions. If sources conflict, preserve the conflict rather than smoothing it over.

**Parallel surface.** Discovery is the widest fan-out stage in the lifecycle. Repository areas, dependency manifests, build scripts, test suites, external API surfaces, and individual open questions are independent lines of investigation. Pursue them in parallel rather than walking a serial checklist, then reconcile findings into one memo. Only reconciliation and conflict resolution need a single pass.

**Downstream handoff.** End with one explicit decision: ready for `architecture-design-desk`, ready for `issue-planning-desk`, ready for `implementation-handoff-desk`, needs product clarification, needs spike, or blocked by unreachable connector facts.

**Acceptance bar.** Discovery is done when the next stage can act without re-investigating: every load-bearing claim about the codebase names the file, path, manifest, or commit it came from; unknowns are stated as questions with the investigation that would answer them; risks carry likelihood and impact; and the handoff decision above is stated unambiguously. Do not invent file paths, dependency versions, test names, architecture decisions, CI status, owners, or issue IDs.

## Output rules

A discovery run delivers the memo and everything it rests on, together: the reconnaissance detail behind it, the risk and unknowns analysis with likelihood and impact, and the explicit handoff decision. Three artifact types stay genuinely their own scope rather than joining that set; a feasibility assessment answers a specific can-we-build-this question, a spike plan is produced when the memo's own conclusion is that implementation is premature, and a connector diagnostic replaces the set when required sources are unreachable.

When producing a discovery artifact, create a downloadable Markdown file when tools allow it. Use the wrapper in `references/output-contract.md`. Include source facts, unverified assumptions, risks, open questions, and explicit next-step routing.

The set is finished when the next stage does not have to repeat the investigation. Every load-bearing claim names the file, path, manifest, or commit behind it. Every unknown is stated as a question with the investigation that would answer it. A spike plan carries its bounding conditions and its stop rule. A memo describing the repository in general terms has not done discovery, it has summarized an impression of one.

Repository areas, manifests, test suites, external API surfaces, and open questions are independent lines of investigation; the widest fan-out in the lifecycle; so the artifacts in the set are built from parallel work and reconciled once.

Do not cite or claim code facts that were not retrieved from connectors or supplied by the user. Do not invent file paths, dependency versions, test names, architecture decisions, CI status, owners, or issue IDs.

A complete set does not mean a complete picture and must not be made to look like one. An area that could not be read is named as unread, and a risk register with three sourced risks beats one with ten plausible ones. Discovery that honestly reports what it could not reach is more useful than discovery that reads finished, because the next stage will plan against whatever it is handed.

## Reference loading

Load these references when relevant:

- `references/discovery-template.md` for the default technical discovery memo structure.
- `references/repo-recon-template.md` for codebase inspection and repo topology work.
- `references/connector-routing.md` for required source selection.
- `references/source-hierarchy.md` for truth precedence and conflict handling.
- `references/risk-register.md` for risk scoring and unknowns classification.
- `references/output-contract.md` for downloadable Markdown artifact rules.
- `references/handoff-rules.md` for routing to later SDLC skills.
- `references/halt-conditions.md` when connector facts are missing or scope is unsafe.

## Halt conditions

Proceed by default. Discovery exists to surface unknowns, so an unknown is the expected output, not a stop: record it, label the working assumption, and continue investigating. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval**: the investigation would require credentials, access, or spend that a human must grant.
- **Production or destructive**: the request asks to run commands against production systems or data to establish a fact.
- **Security or privacy**: the memo would require security, legal, privacy, or production-risk assumptions that no source supports.
- **Source conflict**: live repo state conflicts with pasted facts on a load-bearing point. Preserve the conflict and halt rather than choosing.
- **Release integrity**: a feasibility verdict would be presented as established when the evidence cannot support it.
- **Connector unreachable**: GitHub or a required spec source exists but cannot be read, or external API behavior is current-sensitive and the source is unreachable. A source that is merely absent, or a repo that has not been selected yet, is a soft gap: proceed on user-provided facts, mark the artifact source-limited, and name what would confirm it.

When the user asks for implementation before discovery is bounded, route upstream or narrow the scope and say so; that is a routing decision, not a halt.

## Composition with other SDLC skills

- Use `product-requirements-desk` outputs as upstream product truth when available.
- Hand architectural decisions and viable options to `architecture-design-desk`.
- Hand decomposed work themes and constraints to `issue-planning-desk`.
- Hand bounded implementation-ready facts to `implementation-handoff-desk` only after discovery is complete.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `{{BLOCKER_TAG}}` when implementation handoff facts are insufficient for a coding agent.
