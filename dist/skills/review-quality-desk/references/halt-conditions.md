# Halt Conditions

Halt, request more context, or mark the decision `insufficient evidence` when:

- The PR, branch, commit range, or diff cannot be fetched.
- Changed files are unavailable or incomplete.
- CI/check status is missing, stale, or for a different head SHA.
- Linked issue or acceptance criteria are required but unavailable.
- PR body claims verification that cannot be confirmed.
- Source facts conflict with pasted context.
- Review comments indicate unresolved blocking discussion.
- The PR changes security, auth, data migration, or release behavior without enough tests or docs.
- The user asks for approval but only pasted a partial diff.

Do not fabricate missing PR state, file paths, test names, checks, issue IDs, or review outcomes.
