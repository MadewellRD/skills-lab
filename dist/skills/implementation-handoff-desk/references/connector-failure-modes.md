# Connector Failure Modes

Use this file when a required connector is unavailable, incomplete, stale, or contradictory.

## Output decision

Produce a normal implementation prompt only when all load-bearing facts are either verified or safely delegated to pre-flight checks.

Produce a connector diagnostic when any of these are true:

- the requested prompt requires a live repo, branch, PR, issue, commit, or CI status and GitHub is unavailable;
- the selected repo does not match the requested repo;
- the prompt depends on a ticket/spec/doc that cannot be found;
- named tests, files, scripts, rows, or command names are load-bearing and cannot be verified;
- multiple sources conflict and the current user has not resolved the conflict;
- generating the prompt would require inventing branch state, commit SHAs, PR numbers, issue IDs, CI results, owners, or metrics.

## Diagnostic file format

Name diagnostics as `connector-diagnostic-<theme>.md`.

```markdown
# Connector diagnostic: <theme>

## How to use this file

Resolve the missing connector context below, then ask for the implementation handoff again. Do not paste this file into an implementation agent as an execution prompt.

## Requested prompt

<short summary>

## Missing or unverified sources

- <connector/source>: <missing fact>

## Why this blocks safe prompt generation

<concise explanation>

## Safe fallback

<what can be drafted from pasted facts only, if anything>

## Next action

Connect/select <source>, provide <specific missing facts>, or authorize a pasted-facts-only prompt.
```

## Partial prompt language

Use this exact language inside a prompt when user-provided facts are sufficient to draft but live verification was unavailable:

`Connector state was not available to verify live repo/project facts. This prompt is grounded only in the provided conversation context. Before editing, verify branch, PR, commit, file, test, issue, and CI state. If any verified state differs from this prompt, STOP and report the drift.`

## Never invent

Never invent or guess:

- repository owner/name;
- selected repo scope;
- branch existence;
- baseline SHA;
- target branch tip;
- PR number, title, merge state, or check status;
- issue ID, label, milestone, or assignee;
- test names or function names;
- row counts, corpus counts, pass/fail counts, or CI results;
- document title, author, or recency;
- Slack/Teams/email decision history.
