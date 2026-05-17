---
name: implementation-handoff-desk
description: create, review, refine, and package connector-grounded implementation handoffs for coding agents after requirements, discovery, architecture, and issue planning are complete. use when the user asks for codex or claude code instructions, branch work, commit plans, pull request handoffs, halt-resume prompts, merge-train runbooks, repo cleanup prompts, docs/proof handoffs, or low-token coding-agent execution plans backed by github, issues, docs, ci checks, and source facts.
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

Every generated prompt must be delivered as a downloadable `.md` file.

1. Create a markdown file named with a descriptive slug, such as `pr-prompt-corpus-catalog.md`, `pr-halt-resume-translator-tex2d.md`, or `merge-train-s2-pr6-rating.md`.
2. The file must contain:
   - a title heading,
   - a short `How to use this file` section,
   - the copy-paste-ready implementation prompt under `## Prompt`.
3. The chat response should provide the file link and one direct usage sentence. Do not paste the full prompt in chat unless the user explicitly asks for inline text.
4. When a file-writing tool is unavailable, output the complete markdown file content in a fenced `markdown` block and tell the user to save it as the specified filename.

Use this file wrapper:

```markdown
# prompt title

## How to use this file

Paste everything under `## Prompt` into Claude Code, Codex, or the target implementation agent. Keep the guardrails, halt conditions, commit instructions, PR title, PR body requirements, and final stop line intact.

## Prompt

prompt content
```

## Low-token coding-agent policy

Implementation handoffs must reduce the amount of original design/code structure a coding agent has to invent. Do not ask Codex, Claude Code, or another coding agent to "figure out the architecture" when upstream artifacts should already define it. Instead:

- Carry forward concrete file paths, symbols, modules, interfaces, acceptance criteria, constraints, and validation commands from upstream desks.
- Prefer patch-shaped instructions, file-by-file change plans, command sequences, and exact stop conditions over broad exploratory goals.
- Include code anchors and repo facts discovered through GitHub instead of relying on memory or generic patterns.
- Use `references/code-efficiency.md` when a handoff could be made more deterministic by adding generated scaffolds, templates, helper scripts, or structured implementation plans.
- Keep the final prompt compact enough for the coding agent to spend most of its token budget on editing and validating code, not re-deriving the design.

This skill owns coding-agent token efficiency at the execution boundary. Upstream SDLC desks should contribute structured artifacts, but this skill decides what context belongs in the implementation prompt versus a companion source-notes file.

## Connector access requirements

Use connectors as the grounding layer for every repo-aware or project-aware prompt. GitHub is mandatory when live repository facts are needed. Issue/project connectors are required when the prompt depends on ticket scope. Document connectors are required when the prompt depends on parity docs, audit packs, completion packs, architecture docs, or spec language. Communication connectors are required when the prompt depends on agent halt reports, team decisions, or recent policy choices that are not present in the current chat.

Do not fabricate connector facts. If a required connector is unavailable, the repo is not selected, or the connector cannot return the needed state, produce either a scoped prompt based only on provided facts or a `connector-diagnostic.md` file that lists what is missing. If the user expects live grounding, tell them to connect or select the relevant source before relying on the prompt as fully grounded.

When connector facts are available, carry them into the markdown prompt or companion source-notes section: repo owner/name, base branch, branch/worktree state, PR number and merge state, relevant files, named tests discovered by search, issue IDs, acceptance criteria, commit SHAs, validation status, decision-bearing messages, and canonical docs used. Preserve the canonical halt style: if live connector state conflicts with pasted facts, the generated prompt must instruct the implementation agent to halt and report the drift before editing.

## Workflow

1. Classify the request, select the required connector route, and load the closest canonical exemplar before drafting.
   - Branch landing, rebase, push, and PR creation: use `references/canonical/pr-exp-01-merge-train.md`.
   - Test-coverage PRs with fixture requirements: use `references/canonical/pr-exp-02-legacy-import-tests.md`.
   - Docs-only parity/proof/scoreboard amendments: use `references/canonical/pr-exp-03-parity-amendment.md`.
   - Translator/runtime regression PRs with RED/GREEN commits: use `references/canonical/pr-exp-04-translator-regressions.md`.
   - Tooling/catalog/baseline-generation PRs: use `references/canonical/pr-exp-05-corpus-catalog.md`.
   - Halt resume or narrowed follow-up after an agent stalls: use `references/canonical/pr-halt-resume-01.md` and `references/canonical/pr-halt-response-01.md`.

2. Run connector preflight.
   Use `references/connector-routing.md` to identify required sources. Use GitHub before drafting repository-specific branch, PR, file, test, commit, or CI instructions. Use issue/project connectors before drafting ticket-derived acceptance criteria. Use document connectors before drafting parity/proof/spec/audit prompts. Use communication connectors before incorporating halt reports or team decisions. If a required source is missing, either mark the prompt as user-fact-grounded only or produce a connector diagnostic.

3. Preserve the canonical voice.
   Start with direct operational context such as `You are operating on...`, `Your job is...`, or `Continue work on branch...`. Prefer the canonical sections `State summary`, `Current state`, `Sequence`, `What needs testing`, `What changes`, `What to build`, `Commit N`, `Per-PR guardrails`, `Guardrails`, `Commit message`, `PR title`, `PR base`, `PR body`, and `Stop at...`.

4. Ground the prompt in current facts.
   Prefer live connector facts over memory when the relevant connector is available. Include concrete repository path, GitHub repo, worktree path, base branch or commit, target branch, PR number/state, touched files, existing dirty state, expected command sequence, validation commands, PR title, PR body requirements, commit messages, and exact stop line when known. If facts are missing, use explicit placeholders only for the missing facts and keep the rest concrete.

5. Keep scope narrow and enforce halt behavior.
   Every prompt must define allowed files, forbidden files, validation gates, commit structure, push/PR behavior, and halt conditions. Use `STOP`, `halt and report`, and `Do not proceed past...` language when the exemplar uses it. Do not invite opportunistic fixes.

6. Preserve user policy choices.
   Carry forward user-specific rules such as not rotating credentials, not modifying scoreboards, not touching unrelated branches, using worktrees, not merging PRs, and treating hosted CI instability as a local-verification exception only when the prompt explicitly allows it.

7. Package the output.
   Write the final prompt to a downloadable markdown file using the required wrapper. Return the link and one sentence explaining what to paste into the target agent.

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

Use `references/continuity-kernel.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/codex-conservation-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `CODEX_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
