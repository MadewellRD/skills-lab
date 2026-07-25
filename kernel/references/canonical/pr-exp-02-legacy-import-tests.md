You are operating on the MilkDropX repo at c:\opt\milkdropx (working folder /mnt/opt--MilkDropX from the agent's perspective). Your job is to add a comprehensive test module to hosts/player-desktop/src/legacy_import.rs, which currently ships 518 LOC with zero test coverage.

State summary:
- Current branch should be a fresh branch off origin/main at e6574da (or later if newer commits have landed when you start). Create it as: chore/legacy-import-tests
- Do not touch or commit the uncommitted shader translator work (typed_pass.rs and the modified legacy_shader.rs) — those belong in their own commit, not this one. If they're in your working tree when you branch, stash them first: git stash push -m "shader-translator-wip" -- engine/crates/md-render-wgpu/ assets/
- After tests land and CI is green, you can git stash pop to restore the shader work.

What needs testing:

The public surface in legacy_import.rs:
- pub fn inspect_install(root) -> Result<LegacyInstallManifest, String>
- pub fn is_preset_path(path: &Path) -> bool
- pub fn resolve_install_relative(install_root, content_dir, base_dir, entry) -> PathBuf
- pub fn coverage_timestamp() -> u64  (skip — trivial)
- pub fn default_coverage_output_dir() -> PathBuf  (skip — trivial)

The internal behavior exercised by inspect_install (test through the public API):
- resolve_install_dirs (root-vs-content-dir disambiguation)
- looks_like_content_dir (heuristic: presets/ + playlist/ + (textures/ OR sprites/))
- inspect_playlist (.txt/.m3u/.m3u8/.pls parsing)
- inspect_sprite_refs (sprites.ini section parsing for [img*])
- bucket_for (per-bucket file enumeration, extension map, total_bytes)
- collect_files_recursive (tree walk, missing-dir tolerance)
- parse_ini_sections (case-insensitive section/key, comment lines, malformed lines)

Add tempfile to hosts/player-desktop/Cargo.toml under [dev-dependencies]:
    tempfile = "3"

Add a #[cfg(test)] mod tests at the bottom of legacy_import.rs. Build a small fixture-builder helper inside the test module that takes a tempfile::TempDir and lays down a canonical legacy install layout. Then write the following tests against it:

UNIT TESTS (no fixture needed):

1. is_preset_path_accepts_canonical_extensions
   Verify .milk, .milk2, .mdx, .milkx all return true. Verify .MILK and .Milk2 (case-insensitive) return true.

2. is_preset_path_rejects_non_preset_extensions
   Verify .txt, .png, .ini, .m3u, no-extension all return false.

3. resolve_install_relative_returns_absolute_path_unchanged
   Pass an absolute path; verify it returns as-is regardless of install_root or content_dir.

4. resolve_install_relative_prefers_install_root_when_file_exists_there
   Build a tempdir with install_root/foo.txt. Resolve "foo.txt"; verify the returned path points at install_root/foo.txt.

5. resolve_install_relative_falls_through_to_content_dir
   Build install_root and content_dir as siblings. Place foo.txt only in content_dir. Resolve "foo.txt"; verify it returns content_dir/foo.txt.

6. resolve_install_relative_uses_base_dir_when_provided_and_others_miss
   Place foo.txt only in a base_dir. Resolve with base_dir = Some(...); verify it resolves there.

7. resolve_install_relative_falls_back_to_install_root_join_when_nothing_exists
   Resolve "missing.txt" with no file present anywhere. Verify it returns install_root/missing.txt (the documented fallback).

8. resolve_install_relative_trims_whitespace
   Resolve "  foo.txt  "; verify leading/trailing whitespace is stripped.

INTEGRATION TESTS (use fixture builder):

9. inspect_install_returns_err_when_root_is_not_a_directory
   Pass a path to a regular file. Verify Err containing "not a directory".

10. inspect_install_returns_err_when_directory_does_not_look_like_install
    Pass an empty directory. Verify Err containing "does not look like a legacy MilkDrop install".

11. inspect_install_accepts_root_as_install_dir_with_content_subdir
    Build install_root/Milkdrop2/{presets,playlist,textures}. Pass install_root. Verify manifest.root == install_root and manifest.content_dir == install_root/Milkdrop2.

12. inspect_install_accepts_content_dir_directly
    Build content_dir/{presets,playlist,textures}. Pass content_dir directly. Verify manifest.content_dir == content_dir and manifest.root == parent of content_dir.

13. inspect_install_discovers_presets_recursively_and_filters_by_extension
    Place presets/a.milk, presets/sub/b.milk2, presets/sub/c.txt, presets/d.png. Verify manifest.presets contains exactly a.milk and sub/b.milk2 (sorted), and the .txt and .png are excluded.

14. inspect_install_skips_optional_dirs_without_error
    Build only presets/ and playlist/ and textures/. Omit shapes/, waves/, data/, cache/, docs/. Verify inspect_install succeeds and the corresponding buckets have file_count == 0 and total_bytes == 0.

15. inspect_install_resolves_start_preset_from_settings_ini
    Write settings.ini with [settings] StartPreset=presets/start.milk. Place that file. Verify manifest.start_preset == Some(content_dir/presets/start.milk).

16. inspect_install_returns_none_start_preset_when_settings_ini_missing
    No settings.ini; verify manifest.start_preset is None and settings_ini is None.

17. inspect_install_parses_playlist_entries_and_marks_missing
    Write playlist/main.txt with three lines: one valid (relative), one missing, one empty. Verify the playlist manifest has 2 entries (empty filtered out), with missing_entries containing the one whose resolved_path doesn't exist. Verify is_preset is true for valid preset paths.

18. inspect_install_handles_m3u8_playlists_alongside_txt
    Write playlist/list.m3u8 with valid entries. Verify it's discovered (extension match is case-insensitive: also try .M3U).

19. inspect_install_parses_sprites_ini_image_refs
    Write sprites.ini with [img01] img=sprites/foo.png, [img02] img=sprites/bar.png, [other] (non-img section). Place sprites/foo.png. Verify sprite_image_refs has 2 entries, sorted by raw, with foo.png exists=true and bar.png exists=false. Verify the [other] section is excluded.

20. inspect_install_skips_sprite_entries_with_empty_img_value
    Write sprites.ini with [img01] img=  (whitespace only). Verify that ref is skipped (not in sprite_image_refs).

21. inspect_install_buckets_count_files_and_extensions_correctly
    Place known counts in each bucket dir: 3x .milk in presets/, 2x .png + 1x .jpg in textures/, 1x file with no extension in data/. Verify each bucket's file_count, extensions map, and total_bytes are correct. The extensionless file should land under "<none>" in the extensions map.

22. inspect_install_aggregates_total_file_count_and_bytes_across_buckets
    Sum up the per-bucket counts in the assertion. Verify manifest.total_file_count and manifest.total_bytes are the sums.

23. inspect_install_handles_unicode_paths
    Place presets/日本語.milk. Verify it appears in manifest.presets and is included in the presets bucket. (If the host filesystem can't store this name, gate on cfg(unix) or tolerate skip — comment the rationale.)

24. inspect_install_treats_ini_keys_and_sections_case_insensitively
    Write settings.ini with [SETTINGS] StartPreset=foo.milk (uppercase section, mixed-case key). Verify start_preset still resolves correctly. The parser lowercases section and key names; this is the regression test for that behavior.

25. inspect_install_ini_parser_skips_comments_and_malformed_lines
    Write settings.ini containing: a ; comment line, a # comment line, a section header [settings], a malformed line with no = sign, and a valid StartPreset=foo.milk. Verify the valid entry is parsed and the others are silently ignored.

Fixture-builder helper signature (write this near the top of the test module):

    fn build_install(root: &Path) -> PathBuf {
        // Returns content_dir. Caller owns the TempDir.
        let install_root = root.join("Milkdrop2-install");
        let content_dir = install_root.join("Milkdrop2");
        for sub in ["presets", "playlist", "sprites", "textures", "shapes", "waves", "data", "cache", "docs"] {
            std::fs::create_dir_all(content_dir.join(sub)).unwrap();
        }
        content_dir
    }

Use std::fs::write for placing files. Pass the install_root (parent of content_dir) to inspect_install for the standard-layout tests; pass content_dir directly for the variant test.

Per-PR guardrails:

- cargo build -p player-desktop must exit zero
- cargo test -p player-desktop must exit zero (run with --nocapture if a test panics so you can see the diagnostic)
- cargo clippy -p player-desktop --all-targets -- -D warnings must exit zero — no allow-attribute additions
- cargo fmt -p player-desktop --check must exit zero
- Every test must run without #[ignore]
- No mocks of std::fs — use real tempfile directories
- Do not edit legacy_import.rs production code in this commit. If a test reveals a real bug, STOP and report it before touching the production code; that's a separate change
- Do not touch any other crate
- Do not modify the parity scoreboard, claim-proof map, or status-parity in this PR

Commit message:

    test: add coverage for legacy install import module
    
    Adds 25 tests covering inspect_install, is_preset_path, and resolve_install_relative.
    Fixture-builder helper lays down canonical legacy MilkDrop install layouts in
    tempfile dirs. Tests cover root-vs-content-dir disambiguation, recursive preset
    discovery with extension filtering, optional-bucket tolerance, sprites.ini and
    settings.ini parsing edges, unicode paths, case-insensitive ini lookup, and
    bucket aggregation correctness.
    
    Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Open the PR with title: "test: cover legacy install import module" and base: main. PR body should list the 25 test names by group (unit / integration / edge-case) and note that this closes the test-coverage gap surfaced in the post-e6574da audit.

Stop at "PR opened, CI running." Do not merge. If any cargo command fails, halt and report — do not paper over.