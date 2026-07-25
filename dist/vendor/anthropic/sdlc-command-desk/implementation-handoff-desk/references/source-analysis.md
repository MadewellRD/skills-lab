# Source Analysis Summary

This skill was originally derived from MilkDropX prompt packs and transcripts, then updated with seven canonical prompt exemplars supplied by the user. The new exemplars are authoritative for implementation handoffs and halt-resume prompts.

## Canonical source set

1. `references/canonical/pr-exp-01-merge-train.md`
   - Branch landing and merge-train prompt.
   - Establishes `Current state`, `Working directory`, `Branch target`, `Branch to land`, numbered `Sequence`, force-with-lease push rules, PR fallback URL, and first-anomaly halt behavior.

2. `references/canonical/pr-exp-02-legacy-import-tests.md`
   - Comprehensive test-module implementation handoff.
   - Establishes state summary, WIP isolation/stash rules, public API under test, exact numbered test inventory, fixture-builder helper signature, cargo guardrails, exact commit message, PR title/body, and stop line.

3. `references/canonical/pr-exp-03-parity-amendment.md`
   - Docs-only parity/proof amendment prompt.
   - Establishes exact files-to-touch lists, row/status update instructions, proof citation discipline, sync-check requirements, row-count verification, docs-only guardrails, and multi-line commit message format.

4. `references/canonical/pr-exp-04-translator-regressions.md`
   - Runtime/translator regression implementation handoff.
   - Establishes diagnostic snippet preservation, diagnosis paragraphs, RED/GREEN commit sequencing, exact test names and assertions, structural-fix halt behavior, and local verification requirements.

5. `references/canonical/pr-exp-05-corpus-catalog.md`
   - Tooling/catalog baseline prompt.
   - Establishes command invocation, deterministic output requirements, JSON and Markdown output schemas, support-table cross-reference rules, separate commits for tool and snapshot output, and PR body requirements sourced from generated artifacts.

6. `references/canonical/pr-halt-resume-01.md`
   - Halt-resume continuation prompt.
   - Establishes branch/worktree continuation, preserving already-correct tests, replacing weak reproductions with ordered candidates, using the first true failing candidate, and halting if no candidate reproduces.

7. `references/canonical/pr-halt-response-01.md`
   - Halt response / narrowed continuation prompt.
   - Same canonical halt-resume language preserved as a separate source because the user supplied it as a distinct perfect-output artifact.

## Most reusable extraction

The central reusable form is a bounded operational handoff, not a generic PR template. Strong prompts include:

- exact repo path and job statement;
- base branch/commit and branch/worktree instructions;
- dirty-state or stash/worktree isolation policy;
- exact files to touch and files not to touch;
- diagnostic snippets or source facts when relevant;
- named tests, fixtures, schemas, or rows when relevant;
- exact command sequences;
- specific commit messages and PR title/body instructions;
- hard validation gates;
- first-anomaly halt behavior;
- an exact stop line.
- live GitHub repo grounding when repository access is available.

## Distinct output families

1. Branch landing / merge-train runbook.
2. Test-module implementation handoff.
3. Docs-only parity/proof amendment prompt.
4. Runtime/corpus regression fix prompt.
5. Tooling/catalog baseline implementation handoff.
6. Halt-resume or weakened-repro replacement prompt.
7. Post-merge re-rank or diagnostic prompt.
8. Plan review approval/correction response.

## Output packaging update

The user now requires each generated prompt to be delivered as a downloadable Markdown file. The skill therefore wraps every generated prompt with a title, `How to use this file`, and `## Prompt` section. The chat response should link the file and tell the user to paste the `## Prompt` content into Claude Code, Codex, or the target implementation agent.

## Style notes

- Preserve canonical wording when a supplied exemplar matches the job shape.
- Use crisp operational language.
- Lead with the prompt file, not commentary.
- Do not bury halt conditions.
- Carry forward user-specific operating rules.
- Avoid broad instructions such as `fix related issues`.
- Prefer `STOP`, `halt and report`, and `Do not proceed past...` over permissive remediation.
- Do not invent test names, proof artifacts, metrics, commits, or branch names.


## Connector-policy update

The current skill revision adds connector-aware grounding as a first-class step. The canonical prompts are operational enough that stale branch state, missing PR state, invented tests, or unverified row counts are materially harmful. Future prompts should therefore route through GitHub, issue/project systems, docs, and communication connectors before drafting whenever those sources carry load-bearing facts.

The important design choice is not merely `use GitHub`. It is: select the connector route, extract the exact facts required by the prompt family, preserve conflicts as halt conditions, and produce a diagnostic instead of an implementation prompt when grounding is insufficient.
