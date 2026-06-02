# Releases

This directory contains release notes, release helper scripts, and artifact guidance for Skills-Lab Desk Suites.

GitHub Releases are the public download surface for published suites. The repository `dist/packages/` tree remains the staging surface for generated package artifacts.

## Current GitHub Release state

| Release | Suite | GitHub state | Assets |
|---|---|---|---|
| `web-development-command-desk-v0.3.0` | Web Development Command Desk | Published and marked GitHub `Latest` | 14 skill zips + manifest/checksum assets |
| `ai-engineering-command-desk-v0.1.0` | AI Engineering Command Desk | Published | 18 skill zips + manifest/checksum assets |
| `product-command-desk-v0.1.0` | Product Command Desk | Published | 16 skill zips + release/source bundles + checksums |
| `sales-command-desk-v0.1.0` | Sales Command Desk | Published | 13 skill zips + release/source bundles + checksums |
| `v0.2.0-rc.1` | SDLC Command Desk | Published release candidate | 19 skill zips + `CHECKSUMS.txt` |
| `v0.1.1` | SDLC Command Desk | Published historical release | Workflow-linked bundle + checksums |
| `v0.1.0` | SDLC Command Desk | Published historical release | Initial 19 skill zips + checksums |

## Artifact policy

Packaged skill archives should be published through GitHub Releases when stable. Repository-facing artifact names should be deterministic and suite-scoped. Upload-facing archives may be renamed to `skill.zip` when uploading a single skill to ChatGPT.

## Checksums

Every published artifact set must have SHA256 checksums. Before finalizing a release:

1. Regenerate or collect all packaged archives.
2. Compute SHA256 checksums for every archive or release bundle.
3. Run `python tools/validate_release_assets.py`.
4. Confirm the manifest, install guide, release notes, and GitHub Release assets reference the same artifact set.
5. Attach archives and checksum files to the GitHub Release.

## Versioning

Use semantic-ish release tags for global bundle releases, for example `v0.2.0`, `v0.3.0`, or `v1.0.0`.

Use suite-scoped tags when publishing one suite independently, for example `web-development-command-desk-v0.3.0` or `product-command-desk-v0.1.0`.

Use prerelease markers such as `-rc.1` only when the GitHub Release is also marked as a prerelease.