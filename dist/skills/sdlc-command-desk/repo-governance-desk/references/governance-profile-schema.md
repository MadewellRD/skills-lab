# Governance Profile Schema

A governance profile is the repository's own statement of what counts as authority, evidence, and permission. Read it from, in order: `GOVERNANCE.md` at the repository root; a `## Governance` section in `AGENTS.md`, `CONTRIBUTING.md`, or `CLAUDE.md`; a profile supplied in the chat. Record which source was used. Fields not found are soft gaps: carry the suite default and label it.

## Fields

| Field | What it declares | Suite default when absent |
|---|---|---|
| `ledger.path` | The decision ledger file (for example `engineering-spec/DECISIONS.md`) | none; decisions are ADRs under the design stage |
| `ledger.entry_format` | Heading pattern, required sections, numbering rule, status vocabulary | kernel `adr-template.md` |
| `ledger.numbering` | Next-number rule and any reserved numbers | sequential |
| `gate.of_record` | What proves a commit passed: `hosted_ci`, `local_receipt`, or both | `hosted_ci` |
| `gate.command` | The command that runs the gate (for example `cargo run -p xtask -- gate`) | repository CI config |
| `gate.receipt_path` | Where the receipt is written | none |
| `gate.receipt_fields` | Fields the receipt must carry: head sha, clean-tree flag, result, toolchain, steps, artifact hashes | result and head sha |
| `gate.merge_rule` | How protected branches are reached (for example squash merge only, via the hosting API, pinned to the reviewed sha) | hosting default |
| `gate.certification` | How an ungated merge commit is certified (tree-equality to a receipted commit; pre-merge 0-behind check; post-merge empty diff) | hosted check on the merge commit |
| `invariants[]` | Hard rules no stage may work around, each in its own declared wording | none |
| `authority.issuer` | Who writes work packets | the orchestrator |
| `authority.drafter` | Who drafts decisions | the design stage |
| `authority.ratifier` | Who ratifies decisions; always a named human | the user |
| `authority.recorder` | Who writes ratified text into the ledger | the drafter |
| `authority.merger` | Who executes merges | the user |
| `authority.state_writer` | Who writes the project state file, if one exists | none |
| `authority.veto` | Who may veto any of the above | the user |
| `packet.convention` | Required fields of a work packet (see `packet-convention.md`) | implementation-handoff prompt |
| `branch.convention` | Branch naming, one-commit rule, no rebase or force-push, base pinning | hosting default |
| `deploy.model` | `agent_run` or `operator_run`; for operator_run, where evidence lands | `agent_run` |
| `worktree.rule` | Whether agents must work in their own git worktree, separate from operator deploy checkouts | shared tree |
| `style` | Line-ending policy, forbidden characters, prose rules | repository `.gitattributes` and editorconfig |
| `state.path` | A project state file maintained outside git, if any, and who writes it | none |

## Reading rules

- Quote invariants verbatim. Do not paraphrase them into the artifact; paraphrase is how a rule gets weakened.
- Where the profile and the hosting platform disagree (the profile says no hosted CI, the platform shows a green check), the profile wins for its own domain and the disagreement is recorded.
- A profile that names a ratifier who is not a human is an error to report, not to follow.
- The profile version is the commit sha of the file it was read from. Record it in every artifact.
