# SDLC Command Desk v0.2.0

Date: 2026-06-01

## Summary

Publishes the fresh SDLC Command Desk suite release after cleanup of the previous SDLC release candidates and historical releases. The suite includes one orchestrator and eighteen lifecycle desks covering requirements, discovery, architecture, issue planning, implementation handoff, review, testing, verification, documentation, security, CI triage, release operations, deployment, observability, incident response, maintenance, retrospectives, and decommissioning.

## Artifacts

- Source specs: `skills/SDLC Command Desk/`
- Packaged skill directories: `dist/skills/sdlc-command-desk/`
- Skill zip bundles: `dist/packages/sdlc-command-desk/`
- Checksums: `dist/manifests/sdlc-command-desk-CHECKSUMS.txt`

## Validation

Release assets were validated with:

```powershell
python tools/validate_sdlc_suite.py
python tools/validate_release_assets.py
```

## Notes

This replaces the old `v0.2.0-rc.1` release candidate path with a suite-scoped final release tag: `sdlc-command-desk-v0.2.0`.
