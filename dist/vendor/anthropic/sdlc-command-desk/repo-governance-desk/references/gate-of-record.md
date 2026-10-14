# Gate of Record

Use when `gate.of_record` is `local_receipt` or `both`. The question each check answers is: what is the evidence that this exact content passed, and does the evidence name this content and nothing else.

## Receipt checks (every merge, every release claim)

| Check | Pass condition | Failure handling |
|---|---|---|
| Receipt exists | file present at `gate.receipt_path` | not performed; verdict withheld |
| Result | `result == pass`, zero failing gating steps | fail |
| Commit binding | `git_head` equals the exact sha under review (full sha, not a prefix match) | fail: a receipt for another commit is evidence about another commit |
| Clean tree | `working_tree_dirty == false`; absent field means unknown, not clean | fail or unknown |
| Toolchain | `toolchain_matches_pin == true` | fail |
| Freshness | the receipt postdates the commit; environment-dependent steps (advisory databases, tool versions) are within the profile's freshness window or re-run | re-run those steps |
| Single-writer | the receipt was not overwritten by a later run before it was read; capture its content at review time, by value, into the packet | re-gate if clobbered |

## Squash-merge certification (tree-equality)

A squash merge on the hosting platform creates a commit no local gate ran against. It is certified when its tree is byte-identical to a receipted commit's tree.

Pre-merge, required:
1. The receipt binds the PR head sha (checks above).
2. The PR head is 0 commits behind the base (hosting compare API `behind_by == 0`, or `git merge-base --is-ancestor <base tip> <head>`). If the base moved, the merge is not certified; re-gate on an updated head. Never merge on the assumption the merge will be clean.
3. The merge is executed pinned to the reviewed head sha (the hosting API's `sha` parameter), so a push after review cannot slip in.

Post-merge, required:
4. `git diff --quiet <receipt sha> <merge sha>` is empty. Record the exit code.

A PR whose history contains a merge commit from the base is acceptable when, and only when, the receipt binds the PR head (whose tree already includes the merge) and checks 2 and 4 pass; the receipt then certifies the merged tree, not any earlier commit.

## Artifact binding (every deploy)

The deploy artifact is the gate build, not a rebuild.
1. Copy the gate-built artifacts out of the build directory to a per-sha folder immediately after the receipt is read; a later gate run on another branch rebuilds the build directory.
2. Hash the copies and record the hashes beside the receipt sha in the packet.
3. The deploy script consumes the copies by path and refuses a hash mismatch before touching anything.
4. After deploy, the running software reports its own build identity (a version string or health endpoint carrying the commit) and it must equal the receipt sha.

## Known gaps a profile should decide

- One receipt file is overwritten by every run; per-sha receipt files or git notes close it.
- Receipts are unsigned; a multi-operator host needs the runner's identity and a signature.
- A hook bypass (`--no-verify`) leaves no record; the profile should say whether it is forbidden or must be declared in the PR.
- Tree-equal is not environment-equal; the receipt should carry enough environment to make a re-run reproducible.
