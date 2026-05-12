You are operating on the MilkDropX repo at c:\opt\milkdropx. Job: build a corpus-catalog tool that statically analyzes a preset library and produces a structured frequency report of every HLSL intrinsic, type constructor, swizzle pattern, ternary nesting depth, EEL builtin, register reference, and section-presence pattern actually used. Then run it against the production library at C:\Users\TWSTD\Desktop\MilkDrop 3.33\Milkdrop3\presets and commit the resulting snapshot as a baseline.

Branch off origin/main as fix/corpus-catalog-tool. Use the worktree pattern:
  git worktree add -b fix/corpus-catalog-tool C:\opt\worktrees\corpus-catalog origin/main
Halt and report if branch or path exists.

Tool location: add as a new subcommand on engine/tools/md-compat-harness, invoked as:
  cargo run -p md-compat-harness -- corpus-catalog --root <PRESET_DIR> --output <DIR>

Output: writes <DIR>/corpus-catalog.json (machine-readable) and <DIR>/corpus-catalog.md (human-readable summary). Both files written deterministically — same input always produces identical output (sort keys, stable iteration order, no timestamps).

What the tool analyzes per preset:

PRESET STRUCTURE (use md-core's parser):
- File extension (.milk vs .milk2)
- Sections present (warp_1, comp_1, custom_wave_N, custom_shape_N, etc.)
- Section count distribution

EEL SCRIPTS (use md-eel parser + analysis):
For each per_frame, per_pixel, custom_wave init/per_frame/per_point, custom_shape init/per_frame script:
- All function calls observed
- All variable reads
- All variable writes
- megabuf and gmegabuf access (counts)
- Maximum AST depth
- Maximum line count

HLSL SHADER SOURCES (use existing inspect_legacy_shader_source from md-render-wgpu/src/legacy_shader/intrinsics.rs):
For each warp_1 and comp_1 source:
- Observed intrinsics (Rewrite-mode and Helper-mode classification)
- Unknown function calls (the LegacyShaderInstrumentation.unknown_function_calls field)
- Type constructors used (float, float2, float3, float4, float2x2, float3x3, float4x3, float4x4) — write a small tokenizer that finds these as call-shape identifiers
- Swizzle patterns (count distinct swizzle masks: .x, .xy, .xyz, .xyzw, .rgb, .yzx, etc.)
- Ternary nesting depth (parse expressions and find max nesting of ?: operators)
- Preprocessor directives (#define, #ifdef, #pragma, etc.)
- Static const declarations
- For loop count

REGISTERS:
Across all EEL scripts and HLSL sources combined, tally references to:
- q1..q64 (per-bank usage; report which banks are touched and frequency)
- t1..t8
- mouse_x, mouse_y, mouse_z, mouse_w (per-axis frequency)
- rand_frame.{x,y,z,w}
- rand_preset.{x,y,z,w}
- iMouse, iTime, iResolution (shadertoy-style aliases if present)

CROSS-REFERENCE AGAINST SUPPORT TABLES:
After aggregation, generate gap reports:
- HLSL function calls in corpus but NOT in legacy_shader_intrinsic_specs() Rewrite/Helper catalog AND not in ALLOWED_FUNCTION_CALLS pass-through list AND not in ALLOWED_TYPE_CONSTRUCTORS — these are the unknown intrinsics that need translator coverage. List with frequency and example preset path.
- EEL function calls in corpus but NOT in md-eel's evaluator function table — these are unknown EEL builtins. List with frequency and example preset path.
- Q-bank references where any preset uses q33..q64 — flags presets that require extended q profile.
- Any preset that fails md-core parsing — list with file path and parse error.

OUTPUT FORMAT for corpus-catalog.json:
{
  "corpus_root": "<absolute path>",
  "preset_count": N,
  "extension_breakdown": { "milk": M, "milk2": K },
  "parse_failures": [{"path": "...", "error": "..."}],
  "eel_function_frequency": { "sin": 4123, "cos": 4011, ... } (sorted by frequency desc),
  "eel_unknown_functions": [{"name": "...", "frequency": N, "example_preset": "..."}],
  "hlsl_intrinsic_frequency": { "tex2D": 392, "lerp": 210, ... },
  "hlsl_unknown_calls": [{"name": "...", "frequency": N, "example_preset": "..."}],
  "hlsl_type_constructors": { "float3": 412, "float4x4": 89, ... },
  "swizzle_patterns": { ".xyz": 4012, ".rgb": 891, ... },
  "ternary_depth_distribution": { "1": 3891, "2": 218, "3": 17, "4": 4 },
  "preprocessor_directives": { "#define": 234, "#ifdef": 41 },
  "register_q_bank_usage": { "q1": 4217, ..., "q33": 0, ..., "q64": 0 },
  "register_t_usage": { "t1": 2891, ... },
  "register_mouse_usage": { "mouse_x": 89, "mouse_y": 87, ... },
  "register_rand_frame_usage": { "rand_frame.x": ... },
  "register_rand_preset_usage": { "rand_preset.x": ... },
  "max_eel_ast_depth": K,
  "max_hlsl_ternary_depth": M,
  "section_presence": { "warp_1": 4012, "comp_1": 4019, "custom_wave_0": 891, "custom_shape_0": 412 }
}

OUTPUT FORMAT for corpus-catalog.md:
Human-readable rendering of the above, with frequency-sorted top-N lists for each category, gap callouts in their own ## section, and an executive summary at top showing corpus size + the count of unknown HLSL calls, unknown EEL functions, and parse failures.

Tool implementation should reuse, in order of preference:
1. Existing primitives in md-core, md-eel, md-render-wgpu (especially inspect_legacy_shader_source).
2. Small additional tokenizers ONLY when the existing primitives don't cover what's needed (type constructors, swizzles, ternary depth, preprocessor, registers).
3. Do NOT pull in heavy parser dependencies. Regex + manual string walking is fine for the additional patterns.

After the tool builds, run it against the actual library:
  cargo run -p md-compat-harness --release -- corpus-catalog --root "C:\Users\TWSTD\Desktop\MilkDrop 3.33\Milkdrop3\presets" --output docs/corpus-catalog/

Commit the tool + the snapshot output as separate logical commits:

Commit 1:
  feat: add corpus-catalog subcommand to md-compat-harness
  
  Statically analyzes a preset library to produce a frequency-counted catalog
  of EEL builtins, HLSL intrinsics, type constructors, swizzles, ternary
  nesting depth, preprocessor directives, and register usage. Cross-references
  against support tables to surface unknown calls and gap candidates. Writes
  deterministic JSON + Markdown reports.

Commit 2:
  chore: add corpus catalog baseline for production preset library
  
  Snapshot from C:\Users\TWSTD\Desktop\MilkDrop 3.33\Milkdrop3\presets
  (457 presets, 311 .milk + 146 .milk2, 8.4 MB). Establishes the baseline
  against which future translator/runtime changes can be diffed.

Files written to: docs/corpus-catalog/corpus-catalog.json and docs/corpus-catalog/corpus-catalog.md.

Per-PR guardrails:
- cargo build -p md-compat-harness must exit zero
- cargo test -p md-compat-harness must exit zero
- cargo clippy -p md-compat-harness --all-targets -- -D warnings must exit zero
- cargo fmt --all -- --check must exit zero
- The tool must be deterministic — running twice on the same input produces byte-identical JSON output (this is testable: in the test suite, run on a small fixture corpus twice and assert hash equality)
- Add at least 3 unit tests:
  1. corpus_catalog_aggregates_eel_function_frequencies_across_presets
  2. corpus_catalog_surfaces_unknown_hlsl_calls_with_example_preset_path
  3. corpus_catalog_output_is_deterministic
- Do not modify any other crate's source. md-eel and md-render-wgpu primitives are imported, not edited.
- If the actual catalog run produces parse errors against any preset, capture them in parse_failures (don't crash).
- Do not modify the parity scoreboard, claim-proof map, or status-parity.

PR title: "feat: corpus-catalog tool for static preset library analysis"
PR base: main
PR body: include a brief executive summary pulled from the generated corpus-catalog.md (corpus size, unknown HLSL call count, unknown EEL function count, ternary depth distribution, q-bank usage). Note that the snapshot in docs/corpus-catalog/ establishes a baseline diff target for future translator/runtime PRs.

Stop at "PR opened, all md-compat-harness tests pass locally, snapshot committed." Do not merge.