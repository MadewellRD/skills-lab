# Review Checks for Returned Work

Apply every check to every returned packet. Each check is here because a reviewer who read the code carefully still missed the defect; the check is the thing that would have caught it. Order of review: invariant compliance, correctness against acceptance criteria, security, tests, traceability and receipt, style policy, then the rest. The verdict is accept, accept-with-required-changes, or reject, naming the receipt sha checked.

## R1. Entry-point smoke

Any change to a script or a program's entry point must include a run through the real entry point (actual imports, real parameter binding) to a safe stopping point, plus a static check that every function the script calls from a module is actually exported.
Defect it caught: a merged upgrade script called a module function missing from the module's export list; the harness had extracted function text and dot-sourced it, bypassing the export list, so 29 of 29 checks passed against code the script could not reach. First real run aborted.

## R2. Watched-fail tests

Every test added for a behavior must be shown failing before the fix and passing after, with the output pasted in the report. A test that passes on the broken code is not a test of the fix.
Defect it caught: a breakaway-refusal test passed with containment disabled because the host already ran tests inside an ambient job object; without watched-fail it would have shipped as coverage.

## R3. A different principal

When code makes a security decision about who is connecting (token, SID, user, process owner), tests that run client and server as the same user cannot exercise the refusal and admission paths for a different user. Require either a test with a genuinely different principal or an explicit statement that one cannot be constructed, plus a field check with a real different user before closure.
Defect it caught: an agent attribution routine opened the client's process token, which the service account cannot do for another user's process; every client of the operator was refused on first use. Same-user tests were green.

## R4. Every construction site

When a packet introduces a shared registry, context, or handle that must be the same instance everywhere, enumerate every production site that constructs the owning object and show each one receives the shared instance. Prefer a constructor that requires it over a builder that can be omitted, and add a source guard that fails if the omitting constructor is used outside tests.
Defect it caught: a job registry was wired into the MCP tool path but the console and control-pipe exec paths built their own brokers with a private registry, so their jobs were invisible to the rest of the host.

## R5. Running state, not the file

A check described as verifying the running service must read the running service (its health endpoint, its reported build identity), not the installed file, which after a swap is the new build whether or not the old process still serves.
Defect it caught: a git-sha verdict ran `--version` on the installed binary and so could never detect a stale service; it only duplicated the file hash check.

## R6. Loosened assertions

Any test or guard whose assertion was broadened to accommodate the change is listed in the report with the before and after. The reviewer decides whether the broader assertion still asserts the property.
Defect class: a guard that allowlists a whole file to let one historical line through no longer catches a reintroduced violation in that file.

## R7. The report versus the tree

Verify every claim in the agent's report against the tree: files changed, tests present, receipt sha equals head, clean tree, line endings per policy, forbidden characters absent, census or ceiling values unchanged unless the packet allowed a change. An agent report that lists a criterion as met when the code does not implement it is a deviation to record, not a style note.
Defect it caught: a report listed "records the running git sha" as met when nothing on the upgrade path read it.

## R8. Deploy evidence from disk

Accept a deploy as done only from evidence files the operator's blocks wrote (plan output, upgrade JSON, before and after process lists, hashes, build identity), read by the reviewer. Never from the operator's or the agent's description of what happened.

## R9. Nothing resumed before it is governed

For any change that must contain, attribute, or gate a process before it runs: show the ordering in code (create, assign, register, then resume; on any failure terminate and deregister) and a test for the failure path. A window in which a governed process runs unattributed is a defect even if it is short.
