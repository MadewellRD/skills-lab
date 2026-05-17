# Dependency Upgrade Template

## Upgrade target

Name package, SDK, runtime, framework, plugin, toolchain, or lockfile target.

## Current version and target version

Use repo manifests and lockfiles. If unknown, mark as missing evidence.

## Reason for upgrade

Security, compatibility, deprecation, feature need, performance, bug fix, or policy.

## Compatibility review

Summarize breaking changes, migration notes, peer dependencies, runtime constraints, and transitive risk.

## Proposed sequence

1. Read release notes and compatibility docs.
2. Update manifest and lockfile.
3. Fix compile/type/lint failures.
4. Run focused tests.
5. Run broader regression gates.
6. Prepare release/deployment notes if needed.

## Validation

List exact commands and CI gates.

## Rollback plan

State how to revert package and lockfile changes.

## Handoff notes

Continue security-driven upgrades through the security threat stage; continue release-sensitive upgrades through release operations when facts are sufficient.
