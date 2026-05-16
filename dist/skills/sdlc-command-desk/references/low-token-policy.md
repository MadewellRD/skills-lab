# Low-Token Policy

The suite should reduce downstream coding-agent token use by resolving ambiguity before implementation.

## Split the burden

- Upstream desks produce structured facts, IDs, constraints, and acceptance gates.
- `sdlc-command-desk` routes to the right stage and prevents premature handoffs.
- `implementation-handoff-desk` compresses accepted artifacts into compact execution prompts.
- Coding agents edit and validate code instead of rediscovering requirements, architecture, tests, or release policy.

## Favor code-backed assets where useful

Use scripts for deterministic wrapping, routing, validation, and artifact generation. Do not bloat `SKILL.md`; keep it as the control plane. Put reusable templates in references and deterministic helpers in scripts.

## Good implementation handoff shape

A low-token coding-agent handoff should contain:

- exact repo and branch/base
- exact files or modules
- exact allowed and forbidden scope
- exact requirement IDs and acceptance gates
- exact validation commands
- exact commit sequence
- exact halt conditions
- exact PR title/body expectations

Avoid asking a coding agent to infer these from long prose.
