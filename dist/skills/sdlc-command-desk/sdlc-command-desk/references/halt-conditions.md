# Halt Conditions

Halt and report instead of routing confidently when:

- The request depends on repo state but GitHub context is unavailable.
- The request asks for implementation but requirements or issue scope are missing.
- The request asks for release/deployment but verification or CI status is unknown.
- Source facts conflict and the conflict affects downstream execution.
- The user asks to skip a stage that is required for safety, security, or compliance.
- The selected child desk is not installed and no safe parent desk substitution is available.
- The request would require inventing branch names, commits, issue IDs, CI results, tests, owners, or approvals.

A halt response should include the selected blocked stage, missing facts, why the block matters, and the safe next desk.
