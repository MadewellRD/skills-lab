# Doc-Code Consistency

Classify documentation drift with this rubric.

## Drift classes

- `missing-code-proof`: documentation claims behavior that no source path or test currently proves.
- `missing-doc-proof`: code or tests implement behavior that docs do not mention.
- `stale-path`: documentation cites moved, renamed, or deleted files.
- `stale-status`: documentation claims a status contradicted by current PR/issue/release state.
- `stale-test`: documentation cites missing, renamed, ignored, or failing tests.
- `partial-proof`: evidence exists but does not prove the full claim.
- `conflicting-source`: two trusted sources disagree.

## Severity

- `blocker`: release, audit, compliance, or user-facing claim would be misleading.
- `major`: important project state or acceptance evidence is wrong or incomplete.
- `minor`: wording, path, or context needs cleanup but does not mislead materially.

## Required output

Always include affected files, exact claim text when available, current source fact, severity, and recommended correction.
