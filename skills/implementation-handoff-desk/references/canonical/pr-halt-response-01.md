Continue work on branch fix/translator-ternary-and-tex2d in worktree C:\opt\worktrees\translator-ternary-and-tex2d. Keep your existing nested-ternary regression test (it correctly reproduces). Replace the tex2D regression test with stronger candidates.

The runtime failure shape was:
  ret = (legacy_tex2d(uv).xyz * .xyz
                                ^ expected ')'

Two rewriter calls were almost certainly side-by-side. The first survived as `legacy_tex2d(uv)`. The second's identifier got consumed; only its `.xyz` swizzle remained. Try these minimal repros against the unfixed translator, in order of likelihood, and use the FIRST one that fails:

CANDIDATE A — two tex2D calls multiplied:
  "ret = (tex2D(sampler_main, uv).xyz * tex2D(sampler_pw_main, uv).xyz);"

CANDIDATE B — tex2D times helper-mode intrinsic (GetMain):
  "ret = (tex2D(sampler_main, uv).xyz * GetMain(uv).xyz);"

CANDIDATE C — tex2D times helper-mode intrinsic (GetBlur1):
  "ret = (tex2D(sampler_main, uv).xyz * GetBlur1(uv).xyz);"

CANDIDATE D — two tex2D calls in subtraction (rule out commutativity assumption):
  "ret = tex2D(sampler_main, uv).xyz - tex2D(sampler_blur1, uv).xyz;"

CANDIDATE E — tex2D plus another in addition:
  "ret = tex2D(sampler_main, uv).xyz + tex2D(sampler_blur2, uv).xyz;"

Run each through the translator's translated/translate_and_validate helper. For each candidate, check whether the output WGSL parses under naga::front::wgsl. The FIRST candidate whose output:
  - Fails to parse, AND
  - Produces the failure shape "* .xyz" or analogous "<operator> .xyz" with a missing left-hand identifier
is your true minimal repro.

Use that exact HLSL string in the test:
  translator_preserves_operand_when_two_rewriter_calls_share_an_expression

Assert the translated output:
  - parses cleanly under naga::front::wgsl
  - does NOT contain a swizzle preceded by an operator with no identifier between them (regex: r"[+\-*/]\s*\.[a-zA-Z]+")
  - contains BOTH expected call sites in the output (e.g., for candidate A, two `legacy_tex2d` calls)

If NO candidate reproduces: stop and report. Do not invent a synthetic test that passes on the unfixed translator just to have something committed. The expectation is that one of A-E reproduces; if none do, the bug is in a shape we haven't predicted and we need the actual failing preset source to proceed. In that case, halt the PR and tell Will to share the offending preset file (or grep his library for "* tex2D" / "* GetMain" / "* GetBlur" patterns and dump the shader source from the matching preset).

If a candidate reproduces: proceed with the original commit plan — RED test (commit 1), then fix in legacy_shader.rs (commit 3, since commit 2 is the ternary fix you already have queued). The commit messages I gave originally still apply; just update the test name and the description in the PR body to reflect which candidate shape ended up being the true minimal repro.

All other guardrails from the original prompt remain in force: no scoreboard edits, no other crates touched, no #[ignore], halt if any fix turns out to require structural pipeline rewriting.