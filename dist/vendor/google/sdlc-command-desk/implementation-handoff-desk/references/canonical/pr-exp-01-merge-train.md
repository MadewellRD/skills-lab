You are operating on the MilkDropX repo at c:\opt\milkdropx. Your job is to land branch s2/pr6-rating onto main. This branch holds all of Sprint 2 (legacy file management — ratings, save/save-as, rename/delete, mash-up) as a single squashed commit representing what would have been PR6, PR7, PR8, PR9. Do not split it. Merge as-is.

Current state: origin/main is at commit ab0d86c (Merge PR #28, s4/pr14). s2/pr6-rating was authored before the S3/S4 merges landed but touches different files (ratings.rs, writer.rs, mash.rs, and related glue). A clean rebase is expected.

Working directory: c:\opt\milkdropx
Branch target: origin/main
Branch to land: s2/pr6-rating

Sequence:

1. Fetch and sync.
   git fetch origin
   git checkout main
   git pull --ff-only
   git checkout s2/pr6-rating
   git rebase main

   If conflicts appear: STOP. Do not resolve them. Write a short note listing the conflict files and the commits involved (base / ours / theirs) and halt. Do not continue to step 2.

2. Build and verify against the rebased state.
   cargo build --workspace
   cargo test --workspace
   cargo clippy --workspace --all-targets -- -D warnings
   cargo fmt --all -- --check

   Every command must exit zero. If clippy surfaces new warnings introduced by the rebase (versus the unrebased branch tip), fix them in a single follow-up commit on this branch titled "chore(s2): resolve post-rebase clippy warnings" — do not disable lints, do not add allow attributes. If the failure is a real regression in S2 logic, STOP and report it.

3. Push the rebased branch.
   git push --force-with-lease origin s2/pr6-rating

   Do not use plain --force. If --force-with-lease is rejected because the remote moved, stop and report — that means someone else pushed while you were working and a human needs to adjudicate.

4. Open the PR. Use the gh CLI if available:
   gh pr create --base main --head s2/pr6-rating --title "S2: Legacy file management (PR6–PR9 consolidated)" --body-file -
   
   PR body should describe the four logical units that got squashed:
   - PR6: F6 rating system (ratings.rs — read/write rating metadata, UI wiring)
   - PR7: Save and Save-As (writer.rs — preset serialization, file dialog integration via rfd)
   - PR8: Rename and Delete (file-ops glue — confirmation flow, error surfacing)
   - PR9: Mash-up (mash.rs — cross-preset parameter merge)
   
   Note in the PR body that the commit was collapsed for timing reasons, reference the parity scoreboard cells this PR satisfies, and list the exact S2 acceptance-criteria items from PLATFORM_COMPLETION_PACK.md that this branch closes.

   If gh is not installed, push and output the compare URL (https://github.com/MadewellRD/MilkDrop3/compare/main...s2/pr6-rating) for Will to open manually, along with the PR title and body text.

5. Report back with: the rebase outcome (clean or N commits replayed), cargo check results (all green or which command failed), push result, and the PR URL (or compare URL if gh unavailable).

Guardrails:
- Do not touch any other branch. Do not rebase s4/pr15, s4/pr16, s5/pr17, s5/pr18, s5/pr19, s5/pr20, or s6/pr21.
- Do not modify .github/, do not touch cargo workspace configuration, do not add or remove crates.
- Do not modify the scoreboard or parity-matrix.json — post-S4 audit will handle that.
- Do not rotate or touch git credentials / remote URLs. PAT rotation is explicitly deferred.
- Do not merge the PR yourself. Stop at "PR opened, CI running."

Do not proceed past step 1 if rebase has conflicts. Do not proceed past step 2 if any cargo check fails. Do not proceed past step 3 if push is rejected. Halt and report at the first anomaly.