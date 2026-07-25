# Source Hierarchy and Conflict Handling

Use this truth order when grounding implementation handoffs.

## Truth order

1. Current user instruction in the active conversation.
2. Live GitHub repository state: selected repo, branches, commits, files, tests, PRs, issues, checks.
3. Live issue/project state from GitHub Issues, Linear, or similar connectors.
4. Canonical repo docs and internal docs: parity scoreboard, proof map, completion pack, roadmap, architecture docs, audit packs.
5. Decision-bearing communication sources: Slack, Teams, email, halt reports, agent transcripts.
6. Uploaded canonical prompt exemplars and skill references.
7. Public web sources for external tools/APIs only.
8. Model memory or inference, only when labeled as unverified and never for operational facts.

## Conflict rules

- Current user instruction can choose priority and desired outcome, but it does not override live repo facts such as branch existence or failing checks.
- GitHub wins for code, file, branch, commit, PR, issue, and CI state.
- Canonical docs win for policy and acceptance criteria unless the current user explicitly supersedes them.
- Communication sources explain intent and recent decisions; they do not prove implementation state.
- Uploaded prompt exemplars define style and canonical wording, not current repo truth.

## Required conflict behavior

When sources conflict, do not silently choose one and draft as if no conflict exists. Use one of these patterns:

1. If the conflict is blocking, produce a connector diagnostic instead of an implementation prompt.
2. If the conflict can be resolved by the implementation agent before editing, include a pre-flight gate that says to halt and report the drift.
3. If the current user explicitly resolves the conflict, state the resolved assumption in the source-facts block.

## Examples

- Pasted text says `origin/main is at abc123`, but GitHub reports `def456`: use `def456` as live state and add a pre-flight halt if the local checkout does not match.
- User asks to update parity rows and lists test names, but GitHub grep cannot find a test: do not cite it; instruct the agent to halt if the test is absent.
- Slack says a PR merged, but GitHub shows it open: treat it as open and draft a merge/verification prompt, not a next implementation prompt.
