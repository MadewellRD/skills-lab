# Work Packet Convention

A packet replaces a bare coding-agent prompt in a governed repository. It is small enough to review in one pass and to gate as one gate run. Required fields:

| Field | Content |
|---|---|
| Id and title | the packet id in the repository's vocabulary |
| Base | branch and exact base sha; branch name for the work |
| Order of operations | commit, then gate in the foreground, then push, then open a held PR; never two gate runs at once; never rebase, squash, or force-push; rework is a new commit on the same PR |
| Scope | exact crates, apps, or files; what is explicitly out of scope |
| Survey facts | file and line references the issuer verified, marked "verify, do not trust" |
| Required change | numbered, implementable, with the fail-closed behavior stated for every failure path |
| Tests | each test named, with "write first, watch fail, paste the output" |
| Invariants in force | quoted from the profile, with any the change may not touch called out |
| Expected evidence | receipt naming the new head with a clean tree; gating step list; any census or ceiling that must not move |
| Deviations allowed | none, or the exact ones the issuer pre-approved |
| Report-back fields | head sha, receipt sha, gating steps, watched-fail output, tests added, files changed, PR number, any criterion not met as written |
| Worktree | the agent works in its own worktree when the profile requires it, and re-checks out its branch before resuming after any pause |

A packet that cannot state its invariants in force is not ready to issue; the issuer goes back to the profile first.
