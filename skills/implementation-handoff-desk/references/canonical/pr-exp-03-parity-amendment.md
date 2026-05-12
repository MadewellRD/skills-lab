You are operating on the MilkDropX repo at c:\opt\milkdropx. Job: amend the parity scoreboard, the claim-proof map, and (if it cites the affected rows) the parity-truth doc to reflect the test surface that landed in PR #85 and PR #86. This is a docs-only change. Single commit. Single PR.

State summary:
- origin/main is at f191c55 (PR #86 merged into clean main)
- Branch off origin/main as: docs/parity-amendment-post-pr86
- Use the worktree pattern: git worktree add -b docs/parity-amendment-post-pr86 C:\opt\worktrees\parity-amendment-post-pr86 origin/main
- If branch or worktree path exists, halt and report.

Files to touch — exactly these, nothing else:
- docs/parity-scoreboard.md
- docs/parity-scoreboard.json
- docs/compatibility-claim-proof-map.md
- docs/status-parity.md (only if its remaining-gaps section needs to mention legacy install import; check before editing)

What changes:

ONE — strengthen the warp_shader_execution and composite_shader_execution rows.

Current state: both rows cite legacy_shader.rs by file path with no named tests. After PR #86, the translator now has 29 named tests in legacy_shader.rs plus a new typed_pass.rs module plus an intrinsics.rs module with its own tests.

For BOTH rows in parity-scoreboard.md and parity-scoreboard.json, append the following named translator tests to the proof_artifacts column. Don't replace what's there; add to it. Group them with a phrase like "translator suite (legacy_shader.rs):" so the citation reads cleanly.

Translator tests in engine/crates/md-render-wgpu/src/legacy_shader.rs:
  legacy_shader_corpus_reports_translation_fallbacks
  translator_broadcasts_scalar_lum_to_vec3_declarations
  translator_broadcasts_scalar_rhs_for_multi_swizzle_assignments
  translator_coerces_helper_returns_to_declared_vector_width
  translator_coerces_vec4_assignments_to_vec3_targets
  translator_disambiguates_mul_with_typed_pass
  translator_expands_macro_aliases_and_renames_reserved_identifiers
  translator_extracts_function_body_and_rewrites_tex2d_returns
  translator_handles_000_style_static_consts_and_defines
  translator_handles_helper_function_and_for_loop_syntax
  translator_handles_reported_raymarch_shader_shape
  translator_handles_shader_body_blocks
  translator_instrumentation_tracks_intrinsics_and_unknown_calls
  translator_keeps_swizzled_rand_preset_scalars_as_scalars
  translator_lifts_prelude_globals_for_helper_visibility
  translator_lowers_numeric_masks_and_not_operator
  translator_lowers_numeric_not_lexer_edges
  translator_returns_none_for_empty_shader_source
  translator_rewrites_rand_frame_member_aliases
  translator_rewrites_return_ternaries
  translator_rewrites_typed_locals_and_aspect_aliases_to_valid_wgsl
  translator_rewrites_vector_vector_mul_to_dot
  translator_supports_bare_rand_frame_and_q_bank_matrix_constructors
  translator_supports_plain_static_locals_and_float2x3_constructors
  translator_treats_comment_only_body_as_passthrough
  translator_typed_pass_coerces_scalar_vector_expressions_and_calls
  translator_validates_carnival_ride_regression
  translator_validates_fire1_comp_regression
  translator_widens_simple_scalar_declarations_to_vectors_when_needed

Also cite the new modules by path: engine/crates/md-render-wgpu/src/legacy_shader/typed_pass.rs and engine/crates/md-render-wgpu/src/legacy_shader/intrinsics.rs. Grep those two files for their internal #[test] functions and cite them too — I haven't enumerated them; you'll find them yourself.

Note in the row text that the translator now performs a typed pass with WgslType inference and includes corpus regression tests against named real presets (fire1_comp, carnival_ride). Two named-preset regressions are the strongest signal in the citation list — make sure they're surfaced in the row description, not just buried in the test list.

The current_status text for both rows should be updated to reflect that translation now includes typed-pass disambiguation and named corpus regressions, not just generic compile-or-fallback diagnostics.

Update docs/compatibility-claim-proof-map.md row "Warp/composite shader source-backed execution path" to cite the same new tests and modules. Same proof citations, same expanded current-state language.

TWO — add a new row for legacy install import coverage.

Insert a new row in BOTH parity-scoreboard.md and parity-scoreboard.json. Place it AFTER host_window_monitor_device_behaviors and BEFORE studio_host_editor_product_parity_surface. The new row matches the scoreboard's existing tone and structure.

Suggested fields:
- id: legacy_install_import_coverage
- domain: "Legacy install layout import and coverage reporting"
- legacy_source: "legacy/upstream-milkdrop3/README.md" (install layout description) and "legacy/upstream-milkdrop3/code/vis_milk2/plugin.cpp" (runtime install discovery)
- current_status: describe what hosts/player-desktop/src/legacy_import.rs does — discovers a legacy install root, distinguishes content-dir-as-root from parent-dir-as-root, recursively enumerates presets by extension, parses settings.ini for StartPreset, parses sprites.ini for [img*] sections with case-insensitive lookup, parses .txt/.m3u/.m3u8/.pls playlists with missing-entry tracking, builds typed asset buckets (presets, playlist, sprites, textures, shapes, waves, data, cache, docs) with extension histograms and byte totals, resolves install-relative references with install_root → content_dir → base_dir fallback chain. Coverage reports extend with per-preset issue classification (parse, load, render, warp-translation, comp-translation, visual-drift) and severity (error, degraded), plus capture-checksum + diagnostic-snapshot artifacts.
- parity_status: pick "exact" if the import faithfully reads the canonical legacy layout as documented in the README; pick "intentionally modernized" if the coverage-report layer is positioned as additive modernization. Read the code and decide. Document the decision in the row text.
- proof_artifacts: cite hosts/player-desktop/src/legacy_import.rs, the 25 named tests from PR #85 (listed below), and any coverage-report-extension tests added in commit 952b84a (grep hosts/player-desktop/src/lib.rs and main.rs for new tests touching coverage; cite what you find).
- resolution_path: "n/a" if exact, or "Maintain alignment with legacy install layout as documented in upstream README" if a soft hedge is needed.

The 25 import tests in hosts/player-desktop/src/legacy_import.rs:
  inspect_install_accepts_content_dir_directly
  inspect_install_accepts_root_as_install_dir_with_content_subdir
  inspect_install_aggregates_total_file_count_and_bytes_across_buckets
  inspect_install_buckets_count_files_and_extensions_correctly
  inspect_install_discovers_presets_recursively_and_filters_by_extension
  inspect_install_handles_m3u8_playlists_alongside_txt
  inspect_install_handles_unicode_paths
  inspect_install_ini_parser_skips_comments_and_malformed_lines
  inspect_install_parses_playlist_entries_and_marks_missing
  inspect_install_parses_sprites_ini_image_refs
  inspect_install_resolves_start_preset_from_settings_ini
  inspect_install_returns_err_when_directory_does_not_look_like_install
  inspect_install_returns_err_when_root_is_not_a_directory
  inspect_install_returns_none_start_preset_when_settings_ini_missing
  inspect_install_skips_optional_dirs_without_error
  inspect_install_skips_sprite_entries_with_empty_img_value
  inspect_install_treats_ini_keys_and_sections_case_insensitively
  is_preset_path_accepts_canonical_extensions
  is_preset_path_rejects_non_preset_extensions
  resolve_install_relative_falls_back_to_install_root_join_when_nothing_exists
  resolve_install_relative_falls_through_to_content_dir
  resolve_install_relative_prefers_install_root_when_file_exists_there
  resolve_install_relative_returns_absolute_path_unchanged
  resolve_install_relative_trims_whitespace
  resolve_install_relative_uses_base_dir_when_provided_and_others_miss

Add a corresponding row to docs/compatibility-claim-proof-map.md following the existing column structure (Claim Domain | Legacy Source | Code Path Proof | Test/Fixture Proof | Known Exclusions). Place it adjacent to the host-window/audio-device row for consistency with the scoreboard ordering.

THREE — sync checks must pass.

After edits:

  python3 scripts/check_parity_scoreboard_sync.py
  python3 scripts/check_parity_truth_consistency.py

Both must exit zero. The sync script verifies markdown and JSON have matching rows, statuses, and ordering. The truth-consistency script verifies status-parity.md text agrees with scoreboard outcomes — if it complains, you may need to update status-parity.md's gaps or status sections to mention the new row.

Also confirm row count went from 17 to 18 in both .md and .json.

Guardrails:

- Docs-only change. Do not modify any .rs file. Do not modify any test. Do not modify Cargo.toml/Cargo.lock.
- Status taxonomy is exactly one of: exact, partial, missing, intentionally modernized. No other strings allowed.
- Do not change any existing row's parity_status. The two shader rows stay "exact" — you're only enriching their proof citations and current_status text.
- Do not invent test names. Only cite tests that exist on origin/main as fn definitions. Verify every name you cite by grep before committing.
- Do not touch other rows or other files. The blast radius is the four files listed above.
- No #[ignore]; no allow-attributes; n/a — this is docs-only.
- Run cargo fmt --check and cargo clippy --workspace --all-targets -- -D warnings as a final smoke. Both should be clean since you didn't touch source — if either fails, that's a sign you did touch source by mistake. Halt and investigate.

Commit message:

    docs: amend parity scoreboard for translator and install-import coverage
    
    Adds 29 translator test citations to warp_shader_execution and
    composite_shader_execution proof columns, and notes the typed-pass
    module and named corpus regressions (fire1_comp, carnival_ride).
    
    Adds a new legacy_install_import_coverage row citing the 25 tests
    in hosts/player-desktop/src/legacy_import.rs and the LegacyInstallManifest
    + LegacyCoverageReport surface.
    
    Sync check (check_parity_scoreboard_sync.py) and truth consistency check
    (check_parity_truth_consistency.py) both pass.
    
    Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

PR title: "docs: amend parity scoreboard for translator and install-import coverage"
PR base: main
PR body: list the three change groups (warp citations, composite citations, new install-import row), note that both Python sync checks pass locally, note that hosted CI may be unstable due to ongoing GitHub Actions billing — local docs-only verification is sufficient evidence for this PR.

Stop at "PR opened, sync checks green locally." Do not merge.