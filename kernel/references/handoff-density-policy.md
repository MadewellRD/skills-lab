# Handoff Density Policy

{{CODING_AGENT}} is an execution layer, not a discovery layer.

## The premise

This policy was originally written as a *token conservation* rule: send less, because
context was scarce. That premise expired. Frontier models now carry ~1M tokens of context,
so brevity is no longer the constraint and is no longer the goal.

The constraint that remains is **ambiguity**. A handoff fails when the executing agent has
to *invent* something a prior stage already decided. It does not fail for being long.

Judge a handoff by density of decision, not by length:

- **Dense**: every fact the agent needs to act, with nothing it must guess.
- **Sparse**: short, but the agent has to reconstruct scope, intent, or acceptance.

A long handoff that removes all guessing beats a short one that forces invention.

## Required contents of an implementation handoff

- repo and branch/base
- files/modules in scope
- allowed and forbidden scope
- requirement IDs
- acceptance criteria
- validation commands
- commit plan
- PR title and PR body requirements
- halt conditions
- final stop line

## What to include now that context is cheap

Because context is no longer rationed, prefer passing primary evidence over summarising it:

- Include the actual requirement text, not a paraphrase of it.
- Include the relevant file contents or diffs when the decision depends on them.
- Include the conflicting sources when sources conflict, rather than pre-resolving silently.

Summarise only to *add* signal (grouping, sequencing, naming the decision), never to
shrink the payload.

## What still gets cut

Volume is free; noise is not. Cut anything that does not change what the agent does:

- restatement of the same fact in three registers
- narrative recap of how the analysis was reached
- speculative alternatives that were already rejected
- generic best-practice filler the agent already knows

## Verification

State the acceptance bar and the validation commands. Do not author instructions telling
the agent to "verify its work", "double-check the output", or "use a {{SUBAGENT_TERM}} to
verify". Current models self-verify, and added verification scaffolding measurably causes
over-verification. Define *what passing means*; let the agent establish that it passed.

## Blocked handoffs

If implementation handoff facts are missing, emit `{{BLOCKER_TAG}}` and route upstream.
Do not emit a plausible-looking handoff with invented specifics: a confident wrong handoff
costs more than a blocked one.
