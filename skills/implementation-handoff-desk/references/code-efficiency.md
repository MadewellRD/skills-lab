# Code Efficiency Rules

Use this reference when drafting implementation handoffs for Codex, Claude Code, or other coding agents. The goal is to spend fewer agent tokens on invention and more on editing, testing, and verification.

## Principle

Do not make the coding agent rediscover design intent that upstream SDLC desks have already produced. Convert requirements, discovery, architecture, issues, tests, and repo facts into concrete execution constraints.

## Include in the handoff when available

- Exact repository, branch, base SHA, target branch, and worktree path.
- Exact files, modules, functions, classes, routes, schemas, migrations, and tests that are in scope.
- Exact files and directories that are out of scope.
- Existing APIs or interfaces that must not change.
- Planned commit sequence with purpose per commit.
- Required validation commands and expected success criteria.
- Required PR title/body, issue links, and evidence notes.
- Halt conditions for baseline drift, missing files, unknown tests, failing gates, or conflicting sources.

## Prefer code-heavy structure

Use deterministic structure before prose:

1. File-by-file implementation plan.
2. Function/class/interface anchors.
3. Example call signatures or schemas.
4. Patch-shaped instructions when a change is mechanical.
5. Command blocks for setup, test, lint, build, and verification.
6. Tables for source facts, assumptions, and validation evidence.

## Keep out of the coding-agent prompt

- Long product background that does not affect implementation.
- Full upstream documents when only requirement IDs and acceptance criteria are needed.
- Speculative alternatives after the chosen design is known.
- Repeated connector citations that belong in a companion source-notes file.

## Split context when needed

If the handoff needs extensive provenance, write a companion source-notes file and keep the agent-facing prompt focused on execution. The source-notes file can preserve evidence, citations, alternatives rejected, and decision history.

## Ownership across SDLC suite

All SDLC desks should produce structured artifacts that reduce downstream ambiguity. This skill owns the final compression step: selecting the smallest sufficient context for a coding agent to implement safely.
