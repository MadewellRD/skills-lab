# Governance Profile Example

A complete profile for a governed repository, shown as the reference shape. The values are illustrative: a Rust workspace with a local gate, a decision ledger, and an operator who ratifies decisions and retains merge veto. Bind a real profile from the target repository's own files; do not copy these values into another repository.

| Field | Value |
|---|---|
| `ledger.path` | `docs/decisions/LEDGER.md` |
| `ledger.entry_format` | `## D-NNN: <title>`; `Date`, `Status`, `Relates to`; sections `### Decision`, `### Rationale`, `### Alternatives rejected`, `### Scope note` (drafts add `### Security implications`, `### Affected invariants`) |
| `ledger.numbering` | sequential; a commission names the number; reserved ranges are declared in the ledger header |
| `gate.of_record` | `local_receipt` (no hosted CI, by recorded decision) |
| `gate.command` | `cargo run -p xtask -- gate` |
| `gate.receipt_path` | `target/gate-receipt.json` |
| `gate.receipt_fields` | `result`, `git_head`, `working_tree_dirty`, `toolchain`, `toolchain_matches_pin`, `steps`, `gating_steps_failed`, `timestamp_utc` |
| `gate.merge_rule` | squash merge only, through the hosting API, pinned to the reviewed head sha; a pre-push hook refuses a push whose commit has no passing clean-tree receipt |
| `gate.certification` | pre-merge: head is 0 commits behind base; post-merge: `git diff --quiet <receipt sha> <merge sha>` empty; deploy artifact copied to `work/artifacts/<sha>/` and hash-checked against the gate build before use |
| `invariants[]` | network listeners bind localhost by default with origins exactly allowlisted; every externally reachable action routes through policy before it runs; no general file-erasure capability is exposed; service lifecycle operations are never exposed as callable tools; command execution rejects destructive shapes; secrets never appear in policy, results, or audit output; the audit log is append-only; publish is a distinct permission from execute; public tool names match `^[a-zA-Z0-9_-]{1,64}$`; line endings per `.gitattributes`; no hosted CI; no history rewriting; no model-vendor API usage inside the product |
| `authority.issuer` | the PM session (an agent) |
| `authority.drafter` | a separate architecture session (an agent), by recorded decision |
| `authority.ratifier` | the operator (human) |
| `authority.recorder` | the PM session, verbatim after ratification |
| `authority.merger` | the PM session, delegated by the operator, who retains veto |
| `authority.state_writer` | the PM session only (`PROJECT_STATE.md`, untracked) |
| `packet.convention` | scope, exact crates or files, acceptance criteria, invariants in force, required tests with watched-fail, expected receipt, branch convention, report-back fields |
| `branch.convention` | one branch per packet from the integration branch tip; one commit; no rebase, squash, or force-push; rework is a second commit on the same PR; order is commit, gate, push |
| `deploy.model` | `operator_run`; evidence written to `work/<packet>-field/` and verified by the PM from disk |
| `worktree.rule` | agents and operator deploy blocks must not share a checkout (a deploy block that switches branches under in-progress agent work loses nothing only by luck) |
| `style` | PowerShell, batch, cmd CRLF; everything else LF; no em dashes |
| `state.path` | `PROJECT_STATE.md`, PM-only, mirrored to the project workspace |

## What a profile like this changes about a default suite run

- Release readiness cannot cite a hosted check; it cites the receipt by sha and the clean-tree flag.
- A squash merge creates a commit nobody gated; certification by tree-equality to the receipted head is the only way to call it green.
- A design-stage output in ADR form is rejected; the ledger has its own format and its own ratifier.
- A deploy cannot be run by the agent at all when policy refuses both the process query and the script launch by invariant. The two-block operator pattern replaces it.
- Review misses that come from reading code paths without running the real entry point, from tests that run client and server as the same identity, and from a shared registry wired at one construction site but not the others become standing review checks.
