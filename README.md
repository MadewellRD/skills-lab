# Skill-Lab — Phase 0 Deliverable

Status: complete, all tests green
Built in: Claude session, validated end-to-end
Next phase: Phase 1 — Compiler core graph resolver + Claude target adapter (identity)

This directory is the load-bearing foundation for Skill-Lab RC1. It defines the canonical Intermediate Representation that every Desk and every skill conforms to, and provides a working TypeScript parser and validator that the rest of the system builds on.

Everything here has been written, type-checked, tested, and smoke-tested end-to-end before any implementation agent has been invoked.

## What's in Phase 0

The IR schema (`ir-schema/v1.0/`) — four JSON Schema documents that define the IR contract. The skill schema declares the shape of every SKILL.md frontmatter. The desk schema declares the desk-level manifest including capability tags, leaf enumeration, supported targets, and cross-Desk dependencies. The policy schema is the governance contract surface consumed by ROGUE:OPS-compatible runtimes. The workflow packet schema is the runtime state object that flows between leaves (within a Desk) and across Desks (via the inter_desk_context block).

Both semver versioning and cross-Desk composition are baked in from v1.0. Composition references take the form `@org/desk/skill` with semver range constraints (e.g., `^1.0.0`). Workflow packets carry an `inter_desk_context` block that the top-of-house router populates when handoffs cross Desk boundaries.

The compiler core (`compiler/core/`) — a TypeScript module providing the parser, the validator, the IR types, and a command-line entry point. Parser reads SKILL.md files and produces a `ParsedSkill` object with frontmatter and anchor-keyed body sections. Validator runs three layers of validation (JSON Schema, body structure, semantic invariants) and returns either `{ok: true}` or `{ok: false, errors: [...]}`. The validator is code-fence-aware (H2 anchors inside triple-backtick blocks are correctly ignored as content, not structure).

The worked example (`desks/sdlc-command-desk/skills/verification-desk/SKILL.md`) — the existing SDLC v0.1.1 verification-desk converted to the new IR format. Demonstrates the full frontmatter shape including semver-versioned cross-Desk composition references, all required body anchors in canonical order, the workflow packet schema reference, and the policy reference. Parses and validates cleanly under the CLI.

The test suite (`compiler/core/tests/`) — 40 tests across three files. Parser tests cover frontmatter extraction, anchor splitting, code-fence awareness, missing-anchor detection, and out-of-order detection. Validator tests cover schema validation, body structure validation, semver helpers, semantic invariants (capability consistency, orchestrator role rules), and a round-trip test against the converted verification-desk. All 40 pass.

## How to run it

```bash
cd compiler/core
npm install
npx vitest run                                                    # 40 tests
npx tsx src/cli.ts ../../desks/sdlc-command-desk/skills/verification-desk/SKILL.md
# → OK verification-desk@1.0.0
npx tsx src/cli.ts fixtures/bad-skill.md
# → FAIL with 12 enumerated errors across schema, body, and semantic layers
```

## The IR file shape, in one place

A skill is a Markdown file with YAML frontmatter and mandatory body anchors:

```
---
schema_version: "1.0"
name: <kebab-case-name>
description: <20-1024 chars>
version: <semver>
desk: <kebab-case-desk-name>
role: leaf | orchestrator | router
lifecycle_stage:                              # optional, for lifecycle-shaped Desks
  number: <int>
  name: <snake_case>
inputs: [{id, type, required?, description?}]
outputs: [{id, type, filename, description?}]
connectors_required: [enum]
connectors_optional: [enum]
composes_from: [{ref, version?, reason?}]     # cross-Desk and semver-aware
hands_off_to: [{ref, version?, reason?}]
capability_requirements:                       # all six keys required
  file_io: required | preferred | none
  script_execution: required | preferred | none
  tool_calling: required | preferred | none
  long_context: required | preferred | none
  multimodal: required | preferred | none
  workflow_packet: required | preferred | none
activation_hints: [<phrase>]
provenance:
  author: <name>
  sources: [<uri>]
  license: Apache-2.0 | MIT | BSD-3-Clause | CC-BY-4.0 | Proprietary
policy_ref: <path/to/policy.yaml>             # optional
---

## Purpose
## Activation
## Procedure
## Output Contract
## Halt Conditions
## Workflow Packet
## Composition
## References                                 # optional
```

Anchors must appear in this exact order. Anchors inside fenced code blocks are content, not structure.

## What the validator catches

Three layers run in sequence; every layer reports independently so a single broken file produces a complete error inventory rather than failing fast:

Schema layer (Ajv against `skill.schema.json`) — required fields, enum values, regex patterns (kebab-case names, semver versions), additional-property strictness, format checks on URIs.

Body layer (custom) — required anchor presence, anchor order against `REQUIRED_ANCHORS`, unknown anchors surfaced as warnings.

Semantic layer (custom) — semver string validity (stricter than the `semver` library, rejects the `v` prefix to agree with the schema regex), semver range validity in composition references, capability consistency (workflow_packet=required is inconsistent with file_io=none), role invariants (orchestrator must compose with at least one leaf).

Cross-reference validation (composes_from and hands_off_to resolvability against the registry) is deferred to Phase 1's graph resolver, which has access to multi-Desk context.

## Decision log entries from Phase 0

These decisions were made during the build, beyond what the architecture doc specified:

The license enum is closed (Apache-2.0, MIT, BSD-3-Clause, CC-BY-4.0, Proprietary). Open-license-string would allow typos and license-policy violations to slip through; closed enum forces an explicit decision.

The semver regex is strict — no `v` prefix accepted. The `semver` npm library accepts `v1.0.0` and silently strips it. The validator overrides this to match the schema's pattern, so the two layers agree.

The code-fence parser treats unclosed fences conservatively — content from an unclosed fence to end-of-body is treated as fenced. This is the safe default for malformed input; the alternative (lookahead for explicit closing) would accept malformed templates as structure.

Unknown body anchors are warnings, not errors. Some Desks may want additional sections (a `## Examples` anchor, for instance). The validator flags them so the architect knows, but does not block compilation. Target adapters may drop them.

Schema validation uses `strict: true, allErrors: true`. Strict mode catches typos in schema authoring; allErrors gives the architect a complete inventory of failures per file rather than fail-fast behavior that hides downstream problems.

## What Phase 1 picks up

The graph resolver — walking `composes_from` and `hands_off_to` references across a registry of parsed skills, detecting cycles, version-resolving against `desk.yaml` `depends_on` declarations, and producing a topologically-ordered execution graph.

The Claude target adapter — identity-mapping a parsed skill back to a Claude SKILL.md ZIP (frontmatter + body + references/ + scripts/). The byte-for-byte round-trip against the existing v0.1.1 SDLC artifacts is the Phase 1 acceptance test.

The desk manifest parser — `parseDeskFile` reading `desks/<desk>/desk.yaml`, validating against `desk.schema.json`, and resolving leaf skill references against the parsed skills in the same Desk.

The conversion of the remaining 18 SDLC leaves to IR format, each round-trip-validated.

## Repository topology after Phase 0

```
skill-lab/
├── ir-schema/v1.0/
│   ├── skill.schema.json
│   ├── desk.schema.json
│   ├── policy.schema.json
│   └── workflow-packet.schema.json
├── compiler/core/
│   ├── package.json
│   ├── tsconfig.json
│   ├── vitest.config.ts
│   ├── src/
│   │   ├── types.ts
│   │   ├── parser.ts
│   │   ├── validator.ts
│   │   ├── index.ts
│   │   └── cli.ts
│   ├── tests/
│   │   ├── parser.test.ts
│   │   ├── parser-fence.test.ts
│   │   └── validator.test.ts
│   └── fixtures/
│       └── bad-skill.md
├── desks/sdlc-command-desk/skills/verification-desk/
│   ├── SKILL.md
│   ├── references/        (empty, populated in Phase 1)
│   └── evals/             (empty, populated in Phase 3)
└── docs/skill-ir/         (reserved for Phase 1 IR spec doc)
```

## Implementation-agent handoff

The agent does not need to author any code. Its job is to:

1. `git init` the target repository.
2. Create the directory structure shown above.
3. Drop the files in this delivery into the corresponding locations.
4. `cd compiler/core && npm install`.
5. `npx vitest run` — confirm 40/40 pass.
6. `npx tsc --noEmit` — confirm clean type-check.
7. `npx tsx src/cli.ts ../../desks/sdlc-command-desk/skills/verification-desk/SKILL.md` — confirm `OK verification-desk@1.0.0`.
8. `npx tsx src/cli.ts fixtures/bad-skill.md` — confirm exit code 1 with 12 enumerated errors.
9. Commit as `Phase 0: IR schemas, parser, validator, verification-desk converted`.

If any of those steps fails, halt and report — do not attempt to fix.
