---
name: verification-desk
description: create connector-grounded verification and validation artifacts for software delivery. use when Gemini needs to prove implemented work satisfies requirements, build requirements traceability matrices, assess acceptance gates, validate test and ci evidence, identify release blockers, or prepare downstream handoff notes for release, docs, review, or implementation-handoff-desk workflows.
---

# Verification Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to turn requirements, implementation evidence, test results, CI/check status, pull requests, commits, and manual QA notes into verification and validation artifacts. The skill answers: what was required, what was built, what evidence proves it, what remains unverified, and what blocks release.

## Operating rules

- Run connector preflight before making claims.
- Treat GitHub as source of truth for PRs, commits, changed files, checks, test names, and code evidence.
- Treat PRDs, SRS docs, architecture/design specs, issue bodies, and acceptance criteria as requirement sources.
- Treat CI logs, test output, screenshots, QA notes, and artifacts as evidence sources, not as requirements.
- Separate verified facts from assumptions and gaps.
- Never invent requirement IDs, test results, PR status, commit SHAs, CI outcomes, or release readiness. An unprovable requirement is classified `unverified`, not guessed at.
- Produce downloadable Markdown artifacts when the user asks for a report, checklist, matrix, or handoff.

## Workflow

**Outcome.** The verification artifact the request calls for: a V&V report, requirements traceability matrix, acceptance-gate review, release readiness verification, test evidence review, blocker/gap analysis, or downstream handoff for `implementation-handoff-desk`.

**Inputs.** Load source requirements from PRD, SRS, issue bodies, design docs, acceptance criteria, or user-provided scope. Load implementation evidence from GitHub PRs, commits, changed files, check status, test files, CI artifacts, and manual QA notes. Requirements and evidence are separate inventories and must stay separate in the artifact.

**Mapping.** Build the requirement-to-evidence mapping using `references/rtm-template.md`. Classify each requirement as `verified`, `partially verified`, `unverified`, `blocked`, or `not applicable`. Identify release blockers and evidence gaps using `references/blocker-rubric.md`. Produce the artifact using `references/vv-report-template.md` and `references/output-contract.md`, with downstream handoff notes when additional implementation, documentation, testing, or release work is required.

**Parallel surface.** Each requirement is verified against its own evidence and no requirement's status depends on another's. Retrieve evidence and classify requirements in parallel across the requirement set rather than walking the matrix row by row. Blocker aggregation and the overall release verdict are a single pass at the end, once every row is classified.

**Acceptance bar.** The artifact is done when every requirement in the inventory has exactly one status and every non-`not applicable` status names the specific evidence supporting it, a test name, check, commit, PR, or QA note. Blockers must state what would clear them. Passing CI alone is not proof that every requirement is satisfied, and a merged PR alone is not proof of validation; a `verified` status that rests on either without a requirement-specific link is not acceptable.

## Connector requirements

Use `references/connector-routing.md` to determine required sources.

Default requirements:

- GitHub is required for repo-aware verification, PR validation, changed-file review, commit evidence, test discovery, and check status.
- Document sources or uploaded files are required when the verification depends on PRD, SRS, SDS, architecture, release, or audit documents.
- Issue/project connectors are required when acceptance criteria live in tickets.
- CI/log/artifact access is required when the user asks whether a gate passed.
- Communication sources are optional and should only be used for decision context or manual QA notes.

## Output artifacts

A verification run produces these together, not one of them:

- `verification-report.md`: the verdict and what it rests on.
- `requirements-traceability-matrix.md`: every requirement with exactly one status.
- `evidence-map.md`: each piece of evidence and the requirements it actually supports.
- `acceptance-gate-review.md`: each gate assessed against that evidence.
- `release-blocker-report.md`: what blocks release and what would clear it, or an explicit statement that nothing does.

`verification-handoff.md` is the conditional one: it is produced when verification finds work another desk has to pick up, and is correctly absent when everything verified clean.

Use `scripts/write_verification_markdown.py` when a wrapped Markdown file is useful.

Depth here is the difference between traceability and a table. Every non-`not applicable` status names the specific test, check, commit, PR, or QA note behind it. Every blocker states what would clear it and who can. A matrix whose evidence column reads "CI passing" on every row has recorded one fact many times, not verified many requirements.

Requirements are verified independently of one another, so the artifacts in the set come out of parallel classification, with blocker aggregation and the release verdict as the single pass at the end.

Producing all five is never a reason to resolve one. A requirement with no evidence is `unverified` or `blocked`, and the report says so at the top rather than burying it in a row. Completing the set is the easy part; the set is worth nothing unless `verified` means verified.

## Quality bar

Every verification artifact must include:

- source facts used
- requirement inventory
- evidence inventory
- requirement-to-evidence mapping
- pass/fail/partial status
- gaps and blockers
- assumptions explicitly marked
- recommended next action

Do not mark work as verified unless there is direct evidence. Passing CI alone is not proof that every requirement is satisfied. A merged PR alone is not proof of validation.

## Composition with other SDLC skills

- Consume PRD output from `product-requirements-desk`.
- Consume technical and architecture evidence from `technical-discovery-desk` and `architecture-design-desk`.
- Consume issue plans from `issue-planning-desk`.
- Consume review findings from `review-quality-desk`.
- Consume test strategy and gap findings from `test-strategy-desk`.
- Send implementation follow-ups to `implementation-handoff-desk`.
- Send release-ready outputs to `release-operations-desk`.
- Send proof/doc updates to `docs-traceability-desk`.

## Halt behavior

Proceed by default. A requirement that cannot be proven is classified `unverified` or `blocked` with the missing evidence named; that is this desk's product, not a reason to stop. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval**: accepting a gap, waiving a gate, or signing off on partial coverage needs a human owner.
- **Production or destructive**: establishing evidence would require running against production systems or data.
- **Security or privacy**: the evidence trail would require reproducing secrets, credentials, or personal data in the artifact.
- **Source conflict**: requirement sources and evidence genuinely disagree, or requirement identity is ambiguous across sources such that the same ID means different things.
- **Release integrity**: a release-readiness verdict is requested and would rest on unsupported assumptions, or CI status that gates the release cannot be established. This is the primary halt class for this desk: do not issue a ready verdict that the evidence cannot carry.
- **Connector unreachable**: a required requirement or evidence source exists but cannot be read. A merely absent source is a soft gap: classify the affected requirements `unverified`, note the limitation, and complete the matrix.

Use `references/halt-conditions.md` for the halt artifact format.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
