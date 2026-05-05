# Sprint 01: Bootstrap SDLC Skill Suite

## How to use this file

Paste everything under `## Prompt` into Claude Code, Codex, or the target implementation agent. Keep the guardrails, halt conditions, commit instructions, PR title, PR body requirements, and final stop line intact.

## Prompt

You are operating on the `MadewellRD/skills-lab` repo. Your job is to bootstrap the SDLC Skill Suite source tree from the accepted lifecycle matrix without packaging or releasing any skills yet.

This is a source-and-docs foundation PR. Create the shared policy infrastructure, stage index, validation script, and initial skill source skeletons for the SDLC suite. Do not attempt to fully author every final skill behavior in this PR. The goal is a clean, reviewable foundation that future PRs can refine stage by stage.

State summary:

- GitHub repo: `MadewellRD/skills-lab`
- Default branch: `main`
- Baseline commit: `dfb1f42435cdd2e5f23f2c9c4293ec26ca7e3478` (`docs: add complete SDLC stage skill matrix`)
- Project tracker: GitHub Issue #1, `Project: build SDLC skill suite from public GitHub research`
- Completed anchor skill: `skills/pr-command-desk`
- Accepted matrix: `docs/sdlc-stage-skill-matrix.md`
- Initial research map: `docs/sdlc-skills-research-map.md`

Branch off `origin/main` as `feat/sdlc-skill-suite-bootstrap`.

Use this worktree pattern:

```bash
git fetch origin
git worktree add -b feat/sdlc-skill-suite-bootstrap C:\opt\worktrees\skills-lab-sdlc-suite-bootstrap origin/main
cd C:\opt\worktrees\skills-lab-sdlc-suite-bootstrap
```

If the branch or worktree path already exists, halt and report. Do not reuse a dirty worktree.

Pre-flight verification:

```bash
git log -1 --oneline
```

Expected HEAD must be `dfb1f424 docs: add complete SDLC stage skill matrix` or a later `origin/main` commit that still contains both:

- `docs/sdlc-stage-skill-matrix.md`
- `skills/pr-command-desk/README.md`

If either file is missing, or if the stage matrix no longer says no individual skill should be created before the Sprint plan is reviewed, halt and report baseline drift.

Scope:

Group A: Add shared SDLC suite standards

Create a new documentation directory:

```text
docs/sdlc-suite/
```

Add these files:

```text
docs/sdlc-suite/README.md
docs/sdlc-suite/stage-to-skill-index.md
docs/sdlc-suite/skill-quality-standard.md
docs/sdlc-suite/connector-grounding-standard.md
docs/sdlc-suite/artifact-output-standard.md
docs/sdlc-suite/build-roadmap.md
docs/sdlc-suite/research-source-catalog.md
```

Content requirements:

- `README.md` explains the suite purpose, relationship to `pr-command-desk`, and the rule that all operational outputs must be connector-grounded and artifact-backed.
- `stage-to-skill-index.md` maps all 26 lifecycle stages from `docs/sdlc-stage-skill-matrix.md` to candidate skills.
- `skill-quality-standard.md` defines required files, frontmatter rules, description quality, no-placeholder policy, packaging expectations, and review checklist.
- `connector-grounding-standard.md` defines source hierarchy, connector preflight, GitHub source-of-truth rules, docs/communication connector roles, and conflict behavior.
- `artifact-output-standard.md` defines Markdown output modes, evidence blocks, companion source notes, and downloadable artifact conventions.
- `build-roadmap.md` preserves Sprint A through Sprint D build order from the matrix.
- `research-source-catalog.md` lists the seed sources used so far: local research map, Ed-Fi Alliance OSS AI Tools for Ed-Fi SDLC, kcenon AD-SDLC, and VoltAgent Awesome Agent Skills. Do not copy their content wholesale; summarize why each is relevant.

Group B: Add shared skill reference templates

Create:

```text
skills/_shared/references/source-hierarchy.md
skills/_shared/references/connector-routing.md
skills/_shared/references/evidence-blocks.md
skills/_shared/references/output-files.md
skills/_shared/references/halt-conditions.md
skills/_shared/references/skill-quality-checklist.md
```

These shared references are source templates for future skill packaging. They are not themselves a packaged skill.

Rules:

- Keep each shared reference concise and operational.
- Do not include generic SDLC theory.
- Make each reference reusable across all `*-desk` skills.
- Include explicit halt behavior for missing repo state, missing docs, conflicting connector facts, stale baselines, and unknown acceptance criteria.

Group C: Scaffold the SDLC desk skills

Create source skeletons for these skill directories:

```text
skills/product-requirements-desk/
skills/technical-discovery-desk/
skills/architecture-design-desk/
skills/issue-planning-desk/
skills/review-quality-desk/
skills/test-strategy-desk/
skills/verification-desk/
skills/docs-traceability-desk/
skills/security-threat-desk/
skills/ci-failure-desk/
skills/release-operations-desk/
skills/deployment-desk/
skills/observability-readiness-desk/
skills/incident-response-desk/
skills/maintenance-refactor-desk/
skills/retrospective-desk/
skills/decommissioning-desk/
```

Do not overwrite or rename `skills/pr-command-desk/`.

Each new skill directory must contain:

```text
SKILL.md
README.md
agents/openai.yaml
references/connector-routing.md
references/output-contract.md
references/evidence-blocks.md
references/halt-conditions.md
```

For each `SKILL.md`:

- Use YAML frontmatter with only `name` and `description`.
- `name` must exactly match the directory name.
- `description` must be lowercase and specific enough to trigger the skill.
- Body must describe the skill's role, connector preflight, output artifacts, source hierarchy, and halt behavior.
- Body must not claim full implementation maturity if the skill is only scaffolded.
- Include a `Status` section that says: `initial source skeleton; refine before packaging`.

For each `README.md`:

- State the lifecycle stage(s) covered.
- State intended inputs.
- State intended outputs.
- State required connectors.
- State how the skill composes with `pr-command-desk`.

For each `agents/openai.yaml`:

- Set a human-readable display name.
- Set a short description.
- Use consistent naming and no marketing copy.

For each `references/connector-routing.md`:

- Define required connectors for that stage.
- Define optional connectors.
- Define what facts must be retrieved before producing an operational artifact.
- Define what to do when those facts are missing.

For each `references/output-contract.md`:

- Define the canonical Markdown artifacts for that skill.
- Include `How to use this file` wrapper rules when the output is intended for another agent.

Group D: Add validation tooling

Create:

```text
scripts/validate_sdlc_skills.py
```

The script must validate:

- Every new skill directory under `skills/` except `_shared` and `pr-command-desk` has `SKILL.md`, `README.md`, and `agents/openai.yaml`.
- Every `SKILL.md` has YAML frontmatter with only `name` and `description`.
- `name` equals the directory basename.
- `description` is lowercase.
- No file contains `TODO`, `TBD`, `lorem ipsum`, or placeholder bracket text such as `[fill in]`.
- No `skill.zip` files are committed.
- Each skill has the four required reference files.
- `docs/sdlc-suite/stage-to-skill-index.md` mentions all 26 lifecycle stages from the matrix.

The script must exit non-zero on validation failure and print actionable errors.

Add a small usage section for the script in `docs/sdlc-suite/skill-quality-standard.md`.

Group E: Update repository index docs

Update root `README.md` to include:

- A pointer to `docs/sdlc-stage-skill-matrix.md`.
- A pointer to `docs/sdlc-suite/README.md`.
- A short list of scaffolded SDLC suite skills.
- A note that `pr-command-desk` is the completed anchor skill and the remaining suite skills are initial source skeletons until refined and packaged.

Update `docs/sdlc-skills-research-map.md` only if needed to point to the new suite docs. Do not rewrite the existing research map.

Commit structure:

Commit 1:

```text
docs: add SDLC suite standards and stage index
```

Includes `docs/sdlc-suite/*` only.

Commit 2:

```text
feat: scaffold SDLC desk skill source trees
```

Includes `skills/_shared/*` and all new `skills/*-desk/*` skeletons. Does not modify `skills/pr-command-desk/`.

Commit 3:

```text
tooling: add SDLC skill validation script
```

Includes `scripts/validate_sdlc_skills.py` and any docs updates needed to describe validation.

Commit 4:

```text
docs: update Skills Lab index for SDLC suite
```

Includes root `README.md` and any minimal research-map linking update.

Acceptance gates:

Run:

```bash
python3 scripts/validate_sdlc_skills.py
git status --short
git diff --check
```

All must pass before pushing.

Manual acceptance checks:

- `skills/pr-command-desk/` still exists and is not renamed.
- No `skill.zip` files are committed.
- No generated file contains `TODO`, `TBD`, or placeholder bracket text.
- Every new skill has `SKILL.md`, `README.md`, `agents/openai.yaml`, and four reference files.
- `docs/sdlc-suite/stage-to-skill-index.md` covers stages 0 through 25.
- The PR body clearly states this is a foundation/scaffolding PR, not final packaged skill delivery.

Out of scope (do not touch):

- Do not create, modify, or upload packaged `skill.zip` artifacts.
- Do not publish GitHub Releases.
- Do not delete or rename `pr-command-desk`.
- Do not create fully mature production skill behavior for every stage in this PR.
- Do not copy full external repo content into this repository.
- Do not create CI workflows unless explicitly requested later.
- Do not change repository visibility, permissions, branch protections, or GitHub settings.
- Do not close Issue #1.

Halt conditions:

- Baseline files missing or materially changed -> halt and report drift.
- Branch or worktree path exists -> halt and report.
- Validation script cannot be made deterministic without adding dependencies -> halt and report.
- Any scaffold would require committing binary assets or packaged zips -> halt and report.
- Any external source appears license-incompatible for direct reuse -> summarize the issue and avoid copying content.
- Root README update would overwrite user-authored content -> halt and report instead of replacing it.
- Push is rejected -> halt and report.

Push and PR:

```bash
git push -u origin feat/sdlc-skill-suite-bootstrap
```

Open a PR against `main`.

PR title:

```text
feat: bootstrap SDLC skill suite foundation
```

PR body must include:

- Summary of the four change groups.
- List of all scaffolded skills.
- Note that `pr-command-desk` remains the completed anchor skill.
- Note that this PR does not package or release any skills.
- Validation evidence from `python3 scripts/validate_sdlc_skills.py` and `git diff --check`.
- Link/reference to Issue #1.

Stop at:

```text
PR opened, SDLC suite foundation scaffolded, validation green locally.
```

Do not merge.
