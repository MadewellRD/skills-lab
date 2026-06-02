# Releases

This directory contains release notes, release helper scripts, and artifact guidance for Skills-Lab Desk Suites.

GitHub Releases are the public download surface for published suites. The repository `dist/packages/` tree is the staging surface for packaged suites that have not been published as GitHub Releases yet.

## Current GitHub Release state

| Release | Suite | GitHub state | Assets |
|---|---|---|---|
| `v0.2.0-rc.1` | SDLC Command Desk | Published; not marked GitHub `Latest` | 19 skill zips + `CHECKSUMS.txt` |
| `v0.1.1` | SDLC Command Desk | Published and currently marked GitHub `Latest` | Workflow-linked bundle + checksums |
| `v0.1.0` | SDLC Command Desk | Published historical release | Initial 19 skill zips + checksums |

## Packaged release candidates pending GitHub Release publication

| Release notes | Suite | Package root | Checksum file |
|---|---|---|---|
| `v0.3.0-web-development-command-desk.md` | Web Development Command Desk | `dist/packages/web-development-command-desk/` | `dist/manifests/web-development-command-desk-CHECKSUMS.txt` |
| `sales-command-desk-v0.1.0.md` | Sales Command Desk | `dist/packages/sales-command-desk/` | `CHECKSUMS-sales-command-desk-v0.1.0.txt` |
| `product-command-desk-v0.1.0.md` | Product Command Desk | `dist/packages/product-command-desk/` | `CHECKSUMS-product-command-desk-v0.1.0.txt` |
| manifest only | AI Engineering Command Desk | `dist/packages/ai-engineering-command-desk/` | `dist/manifests/ai-engineering-command-desk-CHECKSUMS.txt` |

## Artifact policy

Packaged skill archives should be published through GitHub Releases when stable. Repository-facing artifact names should be deterministic and suite-scoped. Upload-facing archives may be renamed to `skill.zip` when uploading a single skill to ChatGPT.

## Checksums

Every published or publishable artifact set must have SHA256 checksums. Before finalizing a release:

1. Regenerate or collect all packaged archives.
2. Compute SHA256 checksums for every archive or release bundle.
3. Run `python tools/validate_release_assets.py`.
4. Confirm the manifest, install guide, release notes, and GitHub Release assets reference the same artifact set.
5. Attach archives and checksum files to the GitHub Release.

## Versioning

Use semantic-ish release tags for global bundle releases, for example `v0.2.0`, `v0.3.0`, or `v1.0.0`.

Use suite-scoped tags when publishing one suite independently, for example `web-development-command-desk-v0.3.0` or `product-command-desk-v0.1.0`.

Use prerelease markers such as `-rc.1` only when the GitHub Release is also marked as a prerelease.
