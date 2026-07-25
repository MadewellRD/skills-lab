You are operating on the MilkDropX repo at c:\opt\milkdropx. Job: turn two real translator failures from a live player run into corpus regressions, then fix the underlying translator bugs. State summary:

origin/main is at c6f40f0 (post PR #87). Working tree on main is clean. Use the worktree pattern from prior agent runs:

  git worktree add -b fix/translator-ternary-and-tex2d C:\opt\worktrees\translator-ternary-and-tex2d origin/main

If the branch or worktree path exists, halt and report.

Background — two failures observed at runtime, captured from [player-diag] / [wgpu-diag] output:

FAILURE 1 — recursive ternary not rewritten:

  [player-diag] composite shader translation failed
  reason=wgsl-parse: error: expected ')', found '?'
  wgsl:448:53
    var rainAmount: f32 = select(0.0, 1.0, iMouse.z>0. ? M.y : sin(T*0.05)*0.3+0.7);
                                                       ^ expected ')'

Diagnosis: the HLSL→WGSL ternary rewriter converted the OUTER `?:` to `select()` but did not recurse into the third argument. The third argument `iMouse.z>0. ? M.y : sin(T*0.05)*0.3+0.7` is itself an HLSL ternary that needs the same rewrite. The WGSL emitted is invalid because WGSL has no `?:` operator — every ternary must become a `select()` call.

FAILURE 2 — right-hand operand lost in tex2D-prefixed multiply:

  [player-diag] composite shader translation failed
  reason=wgsl-parse: error: expected expression, found ')'
  wgsl:319:34
    ret = (legacy_tex2d(uv).xyz * .xyz

Diagnosis: the right-hand operand of the `*` was truncated to bare `.xyz` — the identifier preceding the swizzle was eaten by whichever rewrite produces `legacy_tex2d`. The original HLSL was almost certainly `tex2D(samp, uv).xyz * <something>.xyz` and the `<something>` got consumed during the tex2D-call rewrite.

Naga validation also surfaced `InvalidBinaryOperandTypes(Multiply, [9], [33])` on a separate `mask_rect_angle` expression in the same screenshot — that's likely a vector-width mismatch the typed pass should be broadcasting. Address it if and only if Failure 2's fix doesn't already cover it; otherwise leave it as a follow-up and explicitly note it in the PR body as a known remaining issue.

What to build:

This is a single PR with three commits. Open a worktree as above. Do all work in that worktree.

Commit 1 — failing corpus regressions (RED):

  test: add corpus regressions for ternary recursion and tex2D multiply

Add two new translator tests to engine/crates/md-render-wgpu/src/legacy_shader.rs inside the existing #[cfg(test)] mod tests block:

  translator_recursively_rewrites_nested_ternaries_inside_select_arguments

  Construct minimal HLSL that exercises the failure: a single statement containing a select(...) whose condition expression is itself a ternary. Use the actual repro shape from the diag output:
    "float rainAmount = iMouse.z > 0. ? M.y : (rand_frame.z > 0.5 ? sin(T*0.05)*0.3+0.7 : cos(T*0.05));"
  Pass it through the translator using the existing translate_and_validate or translated test helper. Assert that the translated WGSL output:
    - contains no '?' character outside of comments
    - contains AT LEAST TWO `select(` invocations (one for each ternary)
    - parses successfully under naga::front::wgsl

  translator_preserves_right_hand_operand_of_tex2d_multiply

  Construct minimal HLSL: "ret = tex2D(samp, uv).xyz * baseColor.xyz;"
  Pass it through the translator. Assert that the translated WGSL:
    - parses successfully under naga::front::wgsl
    - contains the substring "baseColor.xyz" or its expected normalized form
    - does NOT contain the malformed pattern "* .xyz" (literal "asterisk space dot")

Both tests should FAIL on the unfixed translator. Confirm this before moving to commit 2: run cargo test -p md-render-wgpu translator_recursively and translator_preserves_right_hand and verify both panic with the expected error shapes. If they pass on the unfixed translator, you have not constructed minimal repros that match the actual bugs — stop and report rather than weakening the asserts.

Commit 2 — fix recursive ternary rewrite (GREEN for test 1):

  fix: recursively rewrite ternaries in HLSL→WGSL translation

Locate the ternary rewriter in engine/crates/md-render-wgpu/src/legacy_shader.rs (the function that converts `cond ? a : b` to `select(b, a, cond)`). Identify why it's not recursing. Two likely causes:

  - Single-pass regex match: only outermost ternary is replaced per call. Fix: loop until no `?` remains outside string/comment context, OR write an actual recursive expression-walk that traverses all sub-expressions of a `select()` it just produced.
  - Argument-extraction stops at the first `:`: the third argument extractor isn't balancing nested `?:` properly. Fix: use a balanced-parens-aware splitter that respects nested ternary depth.

After the fix, translator_recursively_rewrites_nested_ternaries_inside_select_arguments must pass. Confirm. Do not proceed to commit 3 if test 1 is still red.

Commit 3 — fix tex2D multiply operand preservation (GREEN for test 2):

  fix: preserve right-hand operand in tex2D-prefixed multiply rewrites

Locate the tex2D-call rewriter in engine/crates/md-render-wgpu/src/legacy_shader.rs (the function that produces `legacy_tex2d(...)` substitutions). The rewriter is consuming more characters than it should from the right of the call site. Two likely causes:

  - Greedy regex replacement that captures past the closing paren of the tex2D call.
  - Boundary detection that skips over a swizzle (.xyz) to the next non-alphanumeric, eating the next identifier.

After the fix, translator_preserves_right_hand_operand_of_tex2d_multiply must pass. Confirm.

Then run the full md-render-wgpu test suite to confirm no regressions in the existing 29 translator tests:

  cargo test -p md-render-wgpu

All 31+ tests must pass.

Per-PR guardrails:

  cargo build -p md-render-wgpu must exit zero
  cargo test -p md-render-wgpu must exit zero (all existing tests + 2 new ones)
  cargo clippy -p md-render-wgpu --all-targets -- -D warnings must exit zero
  cargo fmt --all -- --check must exit zero
  No #[ignore] on either new test
  Do not modify the parity scoreboard, claim-proof map, or status-parity in this PR — those get amended in a follow-up after the fixes are proven against the broader corpus
  Do not modify any other crate
  Do not silently weaken the failing tests if a fix proves harder than expected; halt and report instead

PR title: "fix: recursive ternaries and tex2D operand preservation in HLSL→WGSL translator"
PR base: main
PR body: list the two corpus regressions by name and the two diag-output snippets they reproduce. Note that both bugs were surfaced by live player runs against real preset libraries, captured via the [player-diag] / [wgpu-diag] stderr stream. Note that hosted CI may be unstable due to the ongoing GitHub Actions billing situation; local verification is sufficient evidence for this PR.

Stop at "PR opened, all md-render-wgpu tests pass locally including the two new corpus regressions." Do not merge.

If during commit 2 or 3 you discover that the underlying bug is more structural than a localized fix can address (e.g., the entire rewrite pipeline needs to switch from regex to AST), STOP and report. Do not silently rewrite the translator architecture inside this PR. That's a separate scoped change.