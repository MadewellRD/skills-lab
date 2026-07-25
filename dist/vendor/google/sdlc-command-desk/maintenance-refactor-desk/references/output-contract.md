# Output Contract

## Artifact types

Default artifact names:

- `maintenance-assessment.md`
- `refactor-plan.md`
- `dependency-upgrade-plan.md`
- `migration-sequence.md`
- `dead-code-cleanup-plan.md`
- `regression-control-plan.md`
- `maintenance-handoff.md`

## Required wrapper

Each downloadable artifact should include:

1. Title.
2. How to use this file.
3. Source facts used.
4. Unverified assumptions.
5. Main artifact body.
6. Halt conditions.
7. Downstream handoff notes.

## Implementation handoff

Do not write implementation prompts directly unless the user asks. When implementation is needed, produce handoff notes for `implementation-handoff-desk` with scope, allowed files, forbidden files, validation gates, commit shape, and stop line requirements.
