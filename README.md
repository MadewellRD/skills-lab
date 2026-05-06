# Skills Lab

Public lab for Agentic skill creations, packaged skills, references, and release artifacts.

## Current skills

- `pr-command-desk`: connector-grounded PR, repo-operations, halt-resume, merge-train, docs/proof, and agent handoff prompt generator.

## Repository layout

- `skills/` — unpacked skill source directories and control-plane instructions.
- `releases/` — release notes and packaged skill artifact instructions.
- `docs/` — usage notes, changelogs, connector policy, and design notes.

## Skill packaging rule

Packaged Agentic skills should always be distributed as `skill.zip`. Keep source under `skills/<skill-name>/` and publish packaged archives through GitHub Releases or `releases/<skill-name>/` notes.
