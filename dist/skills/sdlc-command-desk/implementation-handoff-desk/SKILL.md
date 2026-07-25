---
name: implementation-handoff-desk
description: create, review, refine, and package connector-grounded implementation handoffs for coding agents after requirements, discovery, architecture, and issue planning are complete. use when the user asks for the coding agent instructions, branch work, commit plans, pull request handoffs, halt-resume prompts, merge-train runbooks, repo cleanup prompts, docs/proof handoffs, or low-token coding-agent execution plans backed by github, issues, docs, ci checks, and source facts.
---

# Implementation Handoff Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


Use this skill to produce disciplined, connector-grounded implementation handoffs for coding agents. It sits after requirements, discovery, architecture, and issue planning, and turns scoped work into executable branch, commit, pull request, merge-train, halt-resume, repo cleanup, or docs/proof instructions.

The uploaded canonical prompt files are authoritative. Treat their wording, sequencing, stop conditions, guardrails, and PR-body instructions as the style source of truth. Do not fall back to generic placeholder-heavy prompts when one of the canonical files matches the user's requested job shape.


## Connector-first operating model

Treat repo, project, and decision context as evidence, not decoration. Before drafting a prompt, decide which connector family is required and consult `references/connector-routing.md`. Apply the truth order in `references/source-hierarchy.md`. If a connector that is required for safe prompt generation is unavailable, follow `references/connector-failure-modes.md` instead of inventing state.

Default connector roles:

- GitHub: repository source of truth for code, branches, commits, pull requests, issues, CI/checks, files, tests, and changed-file scope.
- Linear or GitHub Issues: ticket source of truth for acceptance criteria, priority, labels, owner, blockers, and linked PRs.
- Slack, Teams, email, or user-provided halt reports: decision and failure-report context, not code-state truth.
- Notion, Drive, SharePoint, or uploaded docs: plans, parity scoreboards, completion packs, architecture docs, design specs, prompt exemplars, and audit artifacts.
- Calendar/email only when scheduling, ownership, or stakeholder timing affects the handoff.
- Public web only for external tool/API facts that are not available in the repo or internal docs.

When multiple sources conflict, do not smooth over the conflict. Preserve the conflict as a pre-flight halt condition in the generated prompt unless the current user explicitly resolves it.

## Required output behavior

A run delivers a prompt for every piece of scoped work it was handed, not the first one. Three issues in scope means three prompt files; a merge train of six PRs means six prompts plus the order they run in. The halt-resume prompt is the genuine exception; it is produced *instead of* the original prompt for the stalled work, not in addition to it.

Every generated prompt must be delivered as a downloadable `.md` file.

- Name the file with a descriptive slug, such as `pr-prompt-corpus-catalog.md`, `pr-halt-resume-translator-tex2d.md`, or `merge-train-s2-pr6-rating.md`.
- The file must contain a title heading, a short `How to use this file` section, and the copy-paste-ready implementation prompt under `## Prompt`.
- The chat response provides the file link and one direct usage sentence. Do not paste the full prompt in chat unless the user explicitly asks for inline text.
- When a file-writing tool is unavailable, output the complete markdown file content in a fenced `markdown` block and tell the user to save it as the specified filename.

Each prompt has to be executable on its own. Files to touch and files not to touch are named. The validation command and its pass condition are stated. Commit structure, PR title, PR base, PR body requirements, and the exact stop line are present. A prompt that tells the agent to "implement the feature described in the issue" has moved the work rather than done it.

Prompts for issues whose file scopes do not overlap are independent and belong to the parallel surface described below. Chained PRs against a shared base do not.

Producing the whole batch is never a reason to invent what one prompt needs. A branch name, PR number, file path, or command that no connector or user supplied is left as an explicit placeholder the executing agent must halt on, not filled with a plausible value so the prompt reads complete. A prompt whose repo could not be reached is reported as blocked: the coding agent has no way to tell an invented fact from a retrieved one and will act on whatever it is given.

Use this file wrapper:

```markdown
# prompt title

## How to use this file

Paste everything under `## Prompt` into the coding agent or the target implementation agent. Keep the guardrails, halt conditions, commit instructions, PR title, PR body requirements, and final stop line intact.

## Prompt

prompt content
```

## Handoff density policy

Implementation handoffs must reduce the amount of original design/code structure a coding agent has to invent. Do not ask the coding agent or another coding agent to "figure out the architecture" when upstream artifacts should already define it. Instead:

- Carry forward concrete file paths, symbols, modules, interfaces, acceptance criteria, constraints, and validation commands from upstream desks.
- Prefer patch-shaped instructions, file-by-file change plans, command sequences, and exact stop conditions over broad exploratory goals.
- Include code anchors and repo facts discovered through GitHub instead of relying on memory or generic patterns.
- Use `references/code-efficiency.md` when a handoff could be made more deterministic by adding generated scaffolds, templates, helper scripts, or structured implementation plans.
- Keep the final prompt compact enough for the coding agent to spend most of its token budget on editing and validating code, not re-deriving the design.

This skill owns coding-agent token efficiency at the execution boundary. Upstream SDLC desks should contribute structured artifacts, but this skill decides what context belongs in the implementation prompt versus a companion source-notes file.

## Connector access requirements

Use connectors as the grounding layer for every repo-aware or project-aware prompt. GitHub is mandatory when live repository facts are needed. Issue/project connectors are required when the prompt depends on ticket scope. Document connectors are required when the prompt depends on parity docs, audit packs, completion packs, architecture docs, or spec language. Communication connectors are required when the prompt depends on agent halt reports, team decisions, or recent policy choices that are not present in the current chat.

Do not fabricate connector facts. If a required connector is unreachable, the repo is not selected, or the connector cannot return the needed state, produce either a scoped prompt based only on provided facts or a `connector-diagnostic.md` file that lists what is missing. State which of the two you produced. If the user expects live grounding, tell them to connect or select the relevant source before relying on the prompt as fully grounded.

When connector facts are available, carry them into the markdown prompt or companion source-notes section: repo owner/name, base branch, branch/worktree state, PR number and merge state, relevant files, named tests discovered by search, issue IDs, acceptance criteria, commit SHAs, validation status, decision-bearing messages, and canonical docs used. Preserve the canonical halt style: if live connector state conflicts with pasted facts, the generated prompt must instruct the implementation agent to halt and report the drift before editing.

## Workflow

**Outcome.** A copy-paste-ready implementation prompt in a downloadable markdown file, grounded in live connector facts, scoped to named files, and carrying its own guardrails and halt conditions. Return the link and one sentence explaining what to paste into the target agent.

**Exemplar selection.** Load the closest canonical exemplar before drafting. Branch landing, rebase, push, and PR creation use `references/canonical/pr-exp-01-merge-train.md`. Test-coverage PRs with fixture requirements use `references/canonical/pr-exp-02-legacy-import-tests.md`. Docs-only parity, proof, or scoreboard amendments use `references/canonical/pr-exp-03-parity-amendment.md`. Translator and runtime regression PRs with RED/GREEN commits use `references/canonical/pr-exp-04-translator-regressions.md`. Tooling, catalog, and baseline-generation PRs use `references/canonical/pr-exp-05-corpus-catalog.md`. Halt resume or narrowed follow-up after an agent stalls uses `references/canonical/pr-halt-resume-01.md` and `references/canonical/pr-halt-response-01.md`.

**Grounding.** Use `references/connector-routing.md` to identify required sources. Use GitHub before drafting repository-specific branch, PR, file, test, commit, or CI instructions. Use issue/project connectors before drafting ticket-derived acceptance criteria. Use document connectors before drafting parity, proof, spec, or audit prompts. Use communication connectors before incorporating halt reports or team decisions. Prefer live connector facts over memory whenever the relevant connector is available.

**Canonical voice.** Start with direct operational context such as `You are operating on...`, `Your job is...`, or `Continue work on branch...`. Prefer the canonical sections `State summary`, `Current state`, `Sequence`, `What needs testing`, `What changes`, `What to build`, `Commit N`, `Per-PR guardrails`, `Guardrails`, `Commit message`, `PR title`, `PR base`, `PR body`, and `Stop at...`.

**Concrete facts.** Include repository path, GitHub repo, worktree path, base branch or commit, target branch, PR number and state, touched files, existing dirty state, expected command sequence, validation commands, PR title, PR body requirements, commit messages, and the exact stop line when known. Where a fact is missing, use an explicit placeholder for that fact alone and keep everything else concrete.

**Scope and guardrails.** Every prompt defines allowed files, forbidden files, validation gates, commit structure, push and PR behavior, and halt conditions. Use `STOP`, `halt and report`, and `Do not proceed past...` language when the exemplar uses it. Do not invite opportunistic fixes.

**User policy.** Carry forward user-specific rules such as not rotating credentials, not modifying scoreboards, not touching unrelated branches, using worktrees, not merging PRs, and treating hosted CI instability as a local-verification exception only when the prompt explicitly allows it.

**Ordered content in the generated prompt.** Commit sequences, `Commit N` ordering, merge-train PR order, and rebase-then-push sequences are externally mandated order inside the artifact this desk produces. Emit them as numbered, ordered steps and never reorder or collapse them for brevity. This constraint governs the generated prompt, not this desk's own procedure.

**Parallel surface.** Connector retrieval is parallel-safe: repo state, PR metadata, check status, issue bodies, and canonical exemplars can be gathered concurrently. Drafting handoffs for separate issues whose file scopes do not overlap is also parallel-safe. Sequenced work is not: merge-train prompts, chained PRs against a shared base, and commit sequences within one prompt are strictly ordered and must be produced and executed in order.

**Acceptance bar.** The prompt is ready when a coding agent can execute it without re-deriving the design: every file it may touch is named, every file it must not touch is named, the validation command and its pass condition are stated, commit and PR structure are specified, and the stop line is explicit. Any fact the agent would otherwise have to guess is either supplied or marked as a placeholder that the agent must halt on rather than invent.

## Halt policy

Two different halts live in this desk. Keep them separate.

**Halts this desk authors into the generated prompt.** These stay as strict as the canonical exemplars. A halt condition is mandatory in every prompt, drift between live state and pasted facts must stop the implementing agent before it edits, and `STOP` lines survive verbatim. Do not relax them.

**Halts this desk itself takes.** Default to producing the prompt. A missing fact becomes an explicit placeholder plus a halt instruction for the implementing agent, not a refusal to draft. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval**: the user asks this desk to execute, push, or merge rather than draft the handoff.
- **Production or destructive**: the prompt would direct irreversible action on a shared branch, production system, or credential without an established rollback.
- **Security or privacy**: grounding the prompt would require embedding secrets, tokens, or personal data in the artifact.
- **Source conflict**: live connector state conflicts with pasted facts on a load-bearing point. Preserve the conflict as a pre-flight halt condition in the generated prompt rather than resolving it.
- **Release integrity**: the request is to chain a prompt against an unmerged or unverified predecessor. Draft a merge/verification prompt, a post-merge re-rank prompt, or a resume-from-halt prompt instead.
- **Connector unreachable**: a required source exists but cannot be read. A source that is merely absent is a soft gap: draft a scoped, user-fact-grounded prompt marked as such, or emit `connector-diagnostic.md`.

Use `HANDOFF_BLOCKER` when the facts available are insufficient for a coding agent to act.

## Core rules

- Do not pre-generate chained implementation prompts against an unmerged predecessor. If the prior PR is open or unverified, draft a merge/verification prompt, a post-merge re-rank prompt, or a resume-from-halt prompt.
- Treat metrics as load-bearing: failure counts, cluster counts, success rate, parse/naga split, pass-set diff, CI status, branch cleanliness, row counts, file counts, and corpus counts must be carried into the prompt when available.
- Use worktrees for dirty or parallel repo states; do not stash unless the canonical exemplar or user explicitly chooses that route.
- A halt condition is mandatory. If a halt triggers, the next prompt must diagnose and narrow; it must not continue blindly.
- Prefer small complete patches with tests, docs, snapshots, and proof updates in the same PR only when that is the stated cadence.
- Never broaden compatibility targets, runtime behavior, repo truth language, allowed files, or validation scope silently.
- Do not invent test names, file paths, branches, commits, metrics, PR numbers, issue IDs, CI statuses, owner names, doc titles, or decision history. Use connectors to verify them when available; otherwise use placeholders, source notes, or connector diagnostics.
- Keep a source-facts trail for generated files. Use `references/evidence-blocks.md` to decide whether the evidence belongs inside the prompt file or in a companion source-notes file.
- Prefer a connector-needed diagnostic over a confident but ungrounded operational prompt.

## References

- `references/templates.md`: canonical template selection and construction rules.
- `references/format-guide.md`: extracted formatting, stop-line, and decision rules.
- `references/source-analysis.md`: summary of source materials and canonical exemplar mapping.
- `references/output-files.md`: downloadable markdown output requirements and output modes.
- `references/connector-routing.md`: connector selection table by request family.
- `references/source-hierarchy.md`: truth precedence and conflict handling.
- `references/connector-failure-modes.md`: missing-source behavior and diagnostic output.
- `references/evidence-blocks.md`: source facts, citation notes, and companion-file rules.
- `references/github-access.md`: GitHub connector usage and grounding requirements.
- `references/code-efficiency.md`: rules for minimizing coding-agent reasoning load with concrete, code-heavy handoffs.
- `references/canonical/`: verbatim canonical PR and halt-resume exemplars.
- `scripts/render_handoff_prompt.py`: optional helper for rendering a full implementation handoff prompt from a JSON spec.
- `scripts/write_prompt_markdown.py`: helper for wrapping any prompt in the required downloadable markdown file format.
- `references/suite-workflow-contract.md`: shared workflow packet, continuation, and halt contract for SDLC Command Desk suite orchestration.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
