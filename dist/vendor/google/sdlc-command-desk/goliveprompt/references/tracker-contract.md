# Tracker Contract

The tracker artifact reads from `{SPEC_DIR}/tracker.json`. The file is the state, the artifact is only a view. Build to this schema even when the visual design changes, because a tracker built off-schema breaks the next session's artifact.

## tracker.json schema

```json
{
  "project": "EXAMPLE-APP",
  "generated_at": "2026-07-24T00:00:00Z",
  "milestones": [
    { "id": "M1", "name": "Milestone name", "sprint": 1 }
  ],
  "tasks": [
    {
      "id": "GL-01",
      "title": "Short imperative description of the work",
      "milestone": "M1",
      "sprint": 1,
      "status": "in_progress",
      "acceptance": "A verifiable gate, stated as observable behaviour",
      "depends_on": [],
      "source": "recon",
      "blocked_on": null,
      "pr": null,
      "evidence": "the command that ran, its result, and what is still outstanding"
    }
  ],
  "commits": [
    {
      "sha": "a1b2c3d",
      "message": "conventional commit subject",
      "date": "2026-07-24T00:00:00Z",
      "task": "GL-01"
    }
  ]
}
```

## Field rules

`status` is one of `todo`, `in_progress`, `blocked`, `done`. Nothing else.

`done` means the acceptance gate passed. Code complete with an unverified gate is `in_progress`, and `evidence` says what is outstanding. This distinction is the whole point of the field; collapsing it turns the tracker into a to-do list.

`blocked` requires `blocked_on` naming the exact human action needed, such as a credential, a production flag flip, or a browser verify. A blocked task without that string is unactionable.

`source` is `recon` or the audit suite that raised the item, for example `sdlc:security-threat-desk`. This is what lets anyone confirm the Phase 3 findings all landed in the plan.

`id` values are permanent. Extend the sequence, never renumber, never reuse.

`acceptance` states a verifiable gate, not a description of the work. "Approvals page renders" is not a gate. "Stale session blocks, re-auths, and completes" is.

## Artifact requirements

The artifact is named `{PROJECT}-golive-tracker` and pinned. One per project, forever. If it is missing but `tracker.json` survives, rebuild it under the same name against the same file rather than creating a second one.

It shows:

- overall progress across the full backlog
- per-milestone progress bars, clickable to filter the backlog
- the full backlog with status chips, never a truncated or paginated subset
- the commit and PR feed, most recent first

It reads live from `tracker.json` and the repo through whatever connector reaches the machine, so reopening the panel shows current truth without a chat turn. It never hardcodes task state into the artifact source, because a hardcoded tracker silently goes stale and is worse than no tracker.

## Update cadence

Update `tracker.json` in the merge commit or immediately after, then refresh the artifact. Every merged PR, no exceptions. The tracker falling behind the repo by even one PR breaks the guarantee that it reflects repo truth, and after that nobody trusts it.
