# Sprint 01: Generate SDLC Skill-Creator Prompt Queue

## How to use this file

Paste everything under `## Prompt` into Claude Code, Codex, or the target implementation agent. Keep the guardrails, halt conditions, commit instructions, PR title, PR body requirements, and final stop line intact.

## Prompt

You are operating on the `MadewellRD/skills-lab` repo. Your job is to replace the prior scaffold-by-hand approach with a complete `skill-creator` prompt queue for every SDLC desk skill in the accepted lifecycle matrix.

This is a planning-and-prompt-generation PR. Do not create the individual skill directories yet, except for the already completed `skills/pr-command-desk/`. Do not hand-author final skill skeletons. The explicit strategy is: every future SDLC skill must be created through a dedicated `@skill-creator` prompt that captures expected input, expected output, connectors, reusable contents, validation requirements, and packaging expectations.

State summary:

- GitHub repo: `MadewellRD/skills-lab`
- Default branch: `main`
- Project tracker: GitHub Issue #1, `Project: build SDLC skill suite from public GitHub research`
- Completed anchor skill: `skills/pr-command-desk`
- Accepted matrix: `docs/sdlc-stage-skill-matrix.md`
- Initial research map: `docs/sdlc-skills-research-map.md`
- Corrected execution model: use `skill-creator` to create each SDLC skill one by one; do not bypass that workflow by manually scaffolding final skill directories.

Branch off `origin/main` as `docs/sdlc-skill-creator-prompt-queue`.

Use this worktree pattern:

```bash
git fetch origin
git worktree add -b docs/sdlc-skill-creator-prompt-queue C:\opt\worktrees\skills-lab-skill-creator-queue origin/main
cd C:\opt\worktrees\skills-lab-skill-creator-queue
```

If the branch or worktree path already exists, halt and report. Do not reuse a dirty worktree.

Pre-flight verification:

```bash
git log -1 --oneline
test -f docs/sdlc-stage-skill-matrix.md
test -f docs/sdlc-skills-research-map.md
test -f skills/pr-command-desk/README.md
```

Read `docs/sdlc-stage-skill-matrix.md` before editing. Confirm it contains lifecycle stages 0 through 25 and candidate skills for each stage. If the stage matrix is missing, materially changed, or no longer represents the accepted complete lifecycle map, halt and report baseline drift.

Scope:

Group A: Add skill-creator queue standards

Create a new directory:

```text
docs/skill-creator/
```

Add these files:

```text
docs/skill-creator/README.md
docs/skill-creator/skill-creation-standard.md
docs/skill-creator/prompt-format.md
docs/skill-creator/build-sequence.md
docs/skill-creator/source-reuse-policy.md
```

Content requirements:

- `README.md` explains that the SDLC suite will be created by feeding one prompt per skill into `@skill-creator`.
- `skill-creation-standard.md` summarizes the expected `skill-creator` workflow: clarify inputs/outputs/connectors, plan reusable contents, initialize, edit, validate, package as `skill.zip`, and iterate.
- `prompt-format.md` defines the mandatory structure for every generated skill-creator prompt.
- `build-sequence.md` preserves the matrix build order but makes clear that no skill should be created outside its own skill-creator prompt.
- `source-reuse-policy.md` says public GitHub sources are pattern sources only. Do not copy large external content verbatim. Preserve attribution in research notes. Avoid license-incompatible direct reuse.

Group B: Generate a complete skill-creator prompt queue

Create:

```text
docs/skill-creator/sdlc-skill-creation-queue.md
docs/skill-creator/prompts/
```

From `docs/sdlc-stage-skill-matrix.md`, extract every candidate skill listed under every lifecycle stage. Do not limit this to the minimum viable suite. Do not limit this to Sprint A-D. The queue must cover each candidate skill from stages 0 through 25.

For each candidate skill, create one prompt file:

```text
docs/skill-creator/prompts/<skill-name>.md
```

Each prompt file must be written to be pasted into ChatGPT with `@skill-creator`. The first line must follow this form:

```text
@skill-creator Create a skill named <skill-name>.
```

Each prompt file must include these sections:

```markdown
# <Display Name> Skill-Creator Prompt

## Prompt

@skill-creator Create a skill named <skill-name>.

Expected input:
- ...

Expected output:
- ...

Required connectors:
- ...

Optional connectors:
- ...

Lifecycle stage coverage:
- ...

Skill behavior requirements:
- ...

Reusable contents to plan:
- references/...
- scripts/... only if deterministic validation or artifact generation requires code
- assets/... only if final artifacts require bundled templates

Artifact/output rules:
- ...

Halt conditions:
- ...

Composition with pr-command-desk:
- ...

Packaging expectations:
- Return a complete validated `skill.zip` when the skill is created.
```

Rules for prompt generation:

- Do not create generic prompts. Each prompt must be stage-specific and skill-specific.
- Do not use placeholders such as `[fill in]`, `TODO`, or `TBD`.
- Use concrete expected inputs and outputs derived from the lifecycle stage in the matrix.
- Include connector requirements for each skill.
- Include a halt condition for missing required connector facts.
- Include how the skill composes with `pr-command-desk` when the output eventually becomes implementation work.
- Do not claim that the skill already exists.
- Do not package any skills in this PR.

Group C: Add a queue index

In `docs/skill-creator/sdlc-skill-creation-queue.md`, include:

- A summary of the queue purpose.
- A table with columns: stage number, stage name, skill name, prompt file path, build priority, required connectors, primary outputs.
- A marker for the completed anchor skill `pr-command-desk`, but do not generate a new creation prompt for it unless the matrix explicitly lists it as a candidate. If listed, mark it as `completed anchor; no creation prompt required`.
- A recommended execution order.
- A note that every prompt should be run through `@skill-creator` in a separate conversation or separate creation pass.

Build priority rules:

- Priority 0: completed anchor (`pr-command-desk`).
- Priority 1: minimum viable suite skills from the matrix.
- Priority 2: Sprint A-D recommended build order skills not already priority 1.
- Priority 3: remaining candidate skills from stages 0 through 25.

Group D: Add validation tooling for the prompt queue

Create:

```text
scripts/validate_skill_creator_prompt_queue.py
```

The script must validate:

- `docs/skill-creator/sdlc-skill-creation-queue.md` exists.
- `docs/skill-creator/prompts/` exists.
- Every candidate skill extracted from `docs/sdlc-stage-skill-matrix.md` has a corresponding prompt file, except `pr-command-desk` if marked as completed anchor.
- Every prompt file starts with a heading and contains `@skill-creator Create a skill named`.
- Every prompt file includes the required sections: Expected input, Expected output, Required connectors, Optional connectors, Lifecycle stage coverage, Skill behavior requirements, Reusable contents to plan, Artifact/output rules, Halt conditions, Composition with pr-command-desk, Packaging expectations.
- No prompt file contains `TODO`, `TBD`, `lorem ipsum`, `[fill in]`, or empty placeholder bracket text.
- No `skill.zip` files are committed.
- The queue index references every prompt file that exists.

The script must exit non-zero on validation failure and print actionable errors.

Group E: Correct the repository docs

Update root `README.md` only as needed to say:

- `docs/sdlc-stage-skill-matrix.md` is the accepted lifecycle map.
- `docs/skill-creator/sdlc-skill-creation-queue.md` is the queue of skill-creator prompts.
- `pr-command-desk` is the completed anchor.
- Other SDLC skills are not created yet; they will be created individually via `@skill-creator` prompts.

Update `docs/sdlc-skills-research-map.md` only if needed to point to the new queue. Do not rewrite the research map.

If `docs/sprints/sprint-01-bootstrap-sdlc-skill-suite.md` still contains instructions to hand-author skill skeletons directly, replace those instructions with this corrected skill-creator queue approach. Do not leave contradictory instructions in the repo.

Commit structure:

Commit 1:

```text
docs: add SDLC skill-creator queue standards
```

Includes `docs/skill-creator/README.md`, `skill-creation-standard.md`, `prompt-format.md`, `build-sequence.md`, and `source-reuse-policy.md`.

Commit 2:

```text
docs: add SDLC skill-creator prompt queue
```

Includes `docs/skill-creator/sdlc-skill-creation-queue.md` and every prompt file under `docs/skill-creator/prompts/`.

Commit 3:

```text
tooling: validate SDLC skill-creator prompt queue
```

Includes `scripts/validate_skill_creator_prompt_queue.py`.

Commit 4:

```text
docs: correct SDLC suite index for skill-creator workflow
```

Includes root `README.md`, minimal research-map links if needed, and this corrected Sprint prompt if it needed replacement.

Acceptance gates:

Run:

```bash
python3 scripts/validate_skill_creator_prompt_queue.py
git status --short
git diff --check
```

All must pass before pushing.

Manual acceptance checks:

- No individual new SDLC skill directory is created in this PR.
- No packaged `skill.zip` files are committed.
- `skills/pr-command-desk/` still exists and is not renamed.
- Every candidate skill in stages 0 through 25 has a prompt file, except completed anchor handling for `pr-command-desk`.
- Every prompt file is ready to paste into `@skill-creator`.
- The queue index clearly states that skills must be created one by one through `skill-creator`.
- There are no contradictory scaffold-by-hand instructions left in the Sprint file.

Out of scope (do not touch):

- Do not create final skill directories for the new SDLC skills.
- Do not package or release any new skills.
- Do not publish GitHub Releases.
- Do not delete or rename `pr-command-desk`.
- Do not copy full external repo content into this repository.
- Do not create CI workflows unless explicitly requested later.
- Do not change repository visibility, permissions, branch protections, or GitHub settings.
- Do not close Issue #1.

Halt conditions:

- The accepted matrix cannot be parsed into candidate skills -> halt and report the ambiguous sections.
- Candidate skill names collide after normalization -> halt and report the collisions.
- The repo contains contradictory instructions telling agents to hand-author final skills directly -> halt after identifying the file and proposed correction.
- Validation script cannot reliably match matrix candidates to prompt files -> halt and report.
- Any external source appears license-incompatible for direct reuse -> summarize the issue and avoid copying content.
- Root README update would overwrite user-authored content -> halt and report instead of replacing it.
- Push is rejected -> halt and report.

Push and PR:

```bash
git push -u origin docs/sdlc-skill-creator-prompt-queue
```

Open a PR against `main`.

PR title:

```text
docs: add SDLC skill-creator prompt queue
```

PR body must include:

- Summary of the corrected approach: use `@skill-creator` for each SDLC skill instead of hand-authored scaffolding.
- Count of lifecycle stages covered.
- Count of candidate skill prompts generated.
- Note that `pr-command-desk` remains the completed anchor skill.
- Note that this PR does not create, package, or release any new skills.
- Validation evidence from `python3 scripts/validate_skill_creator_prompt_queue.py` and `git diff --check`.
- Link/reference to Issue #1.

Stop at:

```text
PR opened, SDLC skill-creator prompt queue complete, validation green locally.
```

Do not merge.
