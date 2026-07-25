# Capability Baseline

Generated from `profiles/frontier-2026-07.yaml`. Do not edit by hand — edit the profile
and rebuild, or the next model release will silently overwrite your changes.

This file tells a desk what it may assume about the model executing it. It exists so that
capability assumptions live in exactly one place instead of being re-litigated inside
every skill body.

## What you may assume

| Capability | Value | What it unlocks |
|---|---|---|
| Context | ~1M input / 128k output | Pass primary evidence whole. Stop pre-compressing. |
| Self-verification | native | State the acceptance bar; do not author verify-steps. |
| Long horizon | multi-file, end-to-end | Carry a workflow across stages in one run. |
| Parallel {{SUBAGENT_TERM}}s | native | Fan out over independent items instead of looping. |
| Programmatic tool calling | available, optional | Accelerator only. Must degrade to plain tool calls. |
| Effort dial | available, optional | May suggest an effort tier per stage. Never require. |

## How this changes authoring

**Scaffolding.** State outcome, constraints, and acceptance bar. Do not decompose into
numbered micro-steps a capable model derives on its own.

Keep numbered steps only where **order is externally mandated and getting it wrong is
unsafe or irreversible** — deploy gates, rollback sequences, approval chains, destructive
cutovers. Ordered procedure is content. Ordered hand-holding is scaffolding. Only the
second one goes.

**Context.** Send the right tokens, not fewer tokens. See `references/handoff-density-policy.md`.

**Halting.** Proceed and label the assumption inline. Reserve halts for the hard classes in
`references/halt-taxonomy.md`. A halt that a competent human would have worked through is
now a defect, not a safeguard.

**Verification.** Never author "add a verification step" or "use a {{SUBAGENT_TERM}} to
verify". Per current vendor guidance this causes over-verification and degrades output.

**Parallelism.** Where a stage operates over independent items, say so explicitly so the
runtime can fan out. Do not prescribe serial iteration over independent work.

**Output ambition.** State the artifact set a complete run delivers, not a menu of
alternatives to pick one from. Output contracts were written when finishing one artifact
per turn was the ceiling; it no longer is. Raise expected depth too: an artifact is complete
when a practitioner could act on it without a follow-up round trip, not when its headings
exist.

This never licenses invention. An artifact with no source basis is reported as
not-applicable or blocked, never filled with plausible text. Completeness of the *set* is
not permission to fabricate the *contents* of one.

## What does NOT change

These are governance boundaries, not model scaffolding. They do not relax as models
improve, because capability raises the fluency of a wrong answer as fast as it raises the
accuracy of a right one:

- Never invent source facts, IDs, owners, dates, commands, metrics, or citations.
- Separate verified fact from assumption from inference.
- Preserve source attribution and the declared source hierarchy.
- Preserve conflicts rather than silently resolving them.
- Respect approval gates and destructive-action boundaries regardless of confidence.
- Emit and carry the continuity packet; never silently drop prior stage state.

A more capable model is a reason to remove *scaffolding*, never a reason to remove
*governance*.
