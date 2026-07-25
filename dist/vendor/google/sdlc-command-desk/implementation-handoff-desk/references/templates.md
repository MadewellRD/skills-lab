# Implementation Handoff Templates

Before using any template, run the connector route in `connector-routing.md`, apply the truth order in `source-hierarchy.md`, and choose an output mode from `output-files.md`. The canonical exemplar files in `references/canonical/` remain the source of truth for wording.

Use the canonical files in `references/canonical/` as the primary templates. They are not loose examples; they are the wording and sequencing standard. When a template is used for a real repository, ground bracketed fields with GitHub connector facts whenever available before writing the downloadable markdown prompt.

## GitHub-grounded drafting pass

Before choosing a template for any real repo request, inspect GitHub when available. Verify the repo, base branch, target branch, PR state, commit SHAs, touched files, named tests, and validation conventions. If GitHub is unavailable, keep placeholders explicit and require the implementation agent to verify them in pre-flight.

## Template selection map

| Request shape | Canonical file | Required style characteristics |
|---|---|---|
| Land or rebase an existing branch, then push/open PR | `references/canonical/pr-exp-01-merge-train.md` | Start with `You are operating on...`; include `Current state`, exact branch target, sequence steps, push rules, PR fallback URL, and first-anomaly halt behavior. |
| Add a comprehensive test module | `references/canonical/pr-exp-02-legacy-import-tests.md` | Include state summary, stash/isolation rules, public surface under test, exact numbered test list, fixture helper signature, guardrails, commit message, PR title/body, and stop line. |
| Docs-only parity/proof amendment | `references/canonical/pr-exp-03-parity-amendment.md` | Include exact files allowed, exact row/status changes, verification scripts, row-count expectations, docs-only guardrails, commit message, PR title/body, and sync-green stop line. |
| Runtime/translator regression fix | `references/canonical/pr-exp-04-translator-regressions.md` | Include diagnostic snippets, failure diagnoses, RED/GREEN commit plan, exact test names/assertions, per-PR guardrails, local validation, and structural-change halt conditions. |
| Build a repo tool and commit generated baseline output | `references/canonical/pr-exp-05-corpus-catalog.md` | Include tool invocation, output schema, analysis categories, support-table cross-reference rules, deterministic output rules, separate commits for tool and snapshot, and baseline snapshot PR body requirements. |
| Resume from a halted PR or replace a weak repro | `references/canonical/pr-halt-resume-01.md` and `references/canonical/pr-halt-response-01.md` | Start with `Continue work on branch...`; preserve existing passing work; list candidate repros in order; require first failing candidate; forbid synthetic passing tests; halt if no candidate reproduces. |

## Canonical full PR handoff pattern

Prefer this pattern for new implementation prompts unless a more specific canonical file applies:

```markdown
You are operating on [repo path]. Job: [single bounded job sentence].

State summary:
- [base branch/commit]
- [branch/worktree to create or continue]
- [dirty state or isolation rule]
- [critical prior PR or runtime/corpus fact]

[Optional domain-specific section: What needs testing / What changes / What to build / Tool location / Output format]

[Commit plan]

Commit 1 - [title]:
  [exact work]

Commit 2 - [title]:
  [exact work]

Per-PR guardrails:
- [validation command] must exit zero
- [validation command] must exit zero
- [forbidden files/modules]
- [do not merge]
- [halt condition]

Commit message:

    [exact commit message]

PR title: "[exact title]"
PR base: main
PR body: [exact required contents]

Stop at "[exact stop line]." Do not merge.
```

## Canonical sequence/runbook pattern

Use for branch landing, rebase, repo hygiene, and merge-train prompts:

```markdown
You are operating on [repo path]. Your job is to [land branch / clean worktrees / bank WIP / amend docs].

Current state: [exact main/base state]
Working directory: [path]
Branch target: [base]
Branch to land: [branch]

Sequence:

1. [Fetch and sync]
   [commands]

   If [conflict/anomaly], STOP. [report requirement]. Do not continue to step 2.

2. [Build and verify]
   [commands]

   Every command must exit zero. If [specific allowed failure], [allowed fix]. Otherwise STOP and report.

3. [Push]
   [command]

   If push is rejected, STOP and report.

4. [Open PR]
   [gh command or fallback compare URL]

5. Report back with:
   - [rebase/sync outcome]
   - [validation result]
   - [push result]
   - [PR URL or compare URL]

Guardrails:
- [forbidden branches/files/actions]
- [credential policy]
- Do not merge the PR yourself. Stop at "[exact stop line]."

Do not proceed past step 1 if [condition]. Do not proceed past step 2 if [condition]. Halt and report at the first anomaly.
```

## Canonical halt-resume pattern

Use for halted branches, weak repro replacement, or narrowed continuation:

```markdown
Continue work on branch [branch] in worktree [path]. [Preserve existing known-good work]. [Replace/narrow the failed part].

The runtime failure shape was:
  [verbatim diagnostic]

[Diagnosis paragraph with confidence level and concrete suspected mechanism.]

Try these minimal repros against the unfixed [subsystem], in order of likelihood, and use the FIRST one that fails:

CANDIDATE A - [description]:
  "[exact repro input]"

[additional candidates]

Run each through [exact helper]. For each candidate, check whether [specific expected failure signal]. The FIRST candidate whose output:
  - [condition]
  - [condition]
is your true minimal repro.

Use that exact [input] in the test:
  [exact_test_name]

Assert the translated/output result:
  - [assertion]
  - [assertion]
  - [assertion]

If NO candidate reproduces: stop and report. Do not invent a synthetic test that passes on the unfixed [subsystem] just to have something committed. [State what user must provide next].

If a candidate reproduces: proceed with the original commit plan - [exact allowed commits]. [Update PR body requirement].

All other guardrails from the original prompt remain in force: [guardrails].
```

## Canonical docs-only proof amendment pattern

Use for scoreboard/proof/status updates:

```markdown
You are operating on [repo]. Job: amend [docs] to reflect [landed PRs]. This is a docs-only change. Single commit. Single PR.

State summary:
- [base]
- Branch off [base] as: [branch]
- Use the worktree pattern: [command]
- If branch or worktree path exists, halt and report.

Files to touch - exactly these, nothing else:
- [file]
- [file]

What changes:

ONE - [change group]
[exact row/text/test names]

TWO - [change group]
[exact insertion placement and fields]

THREE - sync checks must pass.
[commands]

Guardrails:
- Docs-only change. Do not modify [source files].
- [taxonomy/status constraints]
- Do not invent test names. Verify by grep before committing.

Commit message:

    [exact multi-line message]

PR title: "[exact title]"
PR base: main
PR body: [exact required contents]

Stop at "PR opened, sync checks green locally." Do not merge.
```

## Plan review response

Use only when the user asks whether to approve an agent's plan. Do not create a prompt file unless the user asks for a rewritten prompt.

```markdown
Approve with [zero/one/two] refinements.

[Brief judgment of why the plan is structurally right or wrong.]

Refinement 1 - [specific correction]. [Why it matters.]

Refinement 2 - [specific correction]. [Why it matters.]

Tell the agent: "[exact approval/correction sentence]."
```

If the plan is unsafe, start with `Do not approve it.` Then list the blocking issue and the exact revised instruction.


## Template G: Connector diagnostic

Use when required repo/project/doc facts are missing and safe prompt generation would require guessing.

```markdown
# Connector diagnostic: [theme]

## How to use this file

Resolve the missing connector context below, then ask for the implementation handoff again. Do not paste this file into an implementation agent as an execution prompt.

## Requested prompt

[summary]

## Missing or unverified sources

- [connector/source]: [missing fact]

## Why this blocks safe prompt generation

[reason]

## Safe fallback

[what can be drafted from pasted facts only, if anything]

## Next action

Connect/select [source], provide [facts], or authorize a pasted-facts-only prompt.
```
