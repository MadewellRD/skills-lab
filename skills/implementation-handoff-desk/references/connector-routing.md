# Connector Routing

Use this routing table before drafting. The route determines which sources are required, which facts to extract, and when to halt rather than guess.

## Routing table

| Request family | Required sources | Facts to retrieve | Halt or diagnostic trigger |
|---|---|---|---|
| New implementation implementation handoff | GitHub code, PRs, commits; issue/project connector when ticket-derived | repo, default/base branch, baseline SHA, target branch, worktree path, open predecessor PRs, relevant files/functions/tests, validation commands, CI/check policy | Missing repo state, unresolved predecessor PR, unknown base branch/SHA, named tests/files not verified |
| Halt-resume prompt | GitHub branch/PR/commits; pasted halt report; CI/check logs when available | current branch, worktree path, commits already in place, dirty state, failed command, failed tests, changed files, prior stop line | Missing branch/commit state when the prompt would edit an existing branch; halt report conflicts with repo state |
| Halt-response narrowing prompt | Halt report, GitHub code/PR state, prior prompt exemplar | exact failure shape, affected commit, allowed next action, forbidden broadening, diagnostic command sequence | Failure cause cannot be localized; proposed next step would weaken original guardrails |
| Merge-train / branch landing | GitHub branches, commits, PRs, checks | main HEAD, target branch tip, rebase/merge strategy, conflicts, push policy, PR URL/compare URL, check results | Conflicts, rejected force-with-lease, red validation, unknown remote movement |
| Post-merge re-rank / diagnostic | GitHub commits/code; docs/artifacts; generated reports if available | merge SHA, regenerated metrics, pass-set diff, failure clusters, candidate next scopes | HEAD mismatch, metrics drift, missing source artifact, cluster expansion beyond stated tolerance |
| Docs/proof-map/parity prompt | GitHub docs/code/tests; document connector for canonical docs when outside repo | exact rows, row counts, named tests verified by grep/search, scripts to run, files allowed/forbidden | Test names not found, markdown/json sync unknown, allowed file set unclear |
| Repo audit to PR pack | GitHub code/issues/PRs; docs/spec connector | hotspots, stale docs, TODOs, untested modules, open issues, dependency risks, build commands | Audit depends on unavailable repo selection or stale docs with no content confirmation |
| Product/spec implementation prompt | Notion/Drive/SharePoint/docs plus GitHub | spec acceptance criteria, design constraints, owner, target files, implementation boundaries | Spec missing, multiple conflicting specs, current user has not resolved priority |
| Decision-derived prompt | Slack/Teams/email/user transcript plus GitHub/docs as needed | latest decision-bearing messages, speaker/date, policy choices, blockers | Chat/email conflicts with current repo truth or with user's current instruction |
| Scheduling/coordination runbook | Calendar/email/project connector | release window, stakeholder availability, owner, deadline, dependency timing | Timing is required but calendar/email access unavailable |

## Selection rules

1. Prefer the narrowest connector set that can verify the load-bearing facts.
2. Always include GitHub for repository work unless the user explicitly says to draft from pasted facts only.
3. Use issue/project connectors when the prompt references tickets, labels, assignees, milestones, sprints, or acceptance criteria not present in chat.
4. Use document connectors for canonical plans, scoreboards, parity maps, completion packs, architecture docs, and design specs.
5. Use communication connectors only for decisions, halt reports, and human policy context. Do not treat chat as proof of code state.
6. Use public web only for external package, API, vendor, or platform facts not represented in repo/docs.

## Prompt implications

A connector-grounded prompt must include the verified facts directly in the prompt or a companion source-notes file. A connector-missing prompt must say which facts are unverified and must add pre-flight verification/halt instructions for the implementation agent.
