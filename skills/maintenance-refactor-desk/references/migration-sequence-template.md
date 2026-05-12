# Migration Sequence Template

## Migration scope

Define source, target, affected systems, and compatibility window.

## Migration driver

Deprecation, architecture decision, platform change, cost, security, reliability, or performance.

## Current-state evidence

List current implementation, dependencies, consumers, data, configs, docs, and tests.

## Target-state design

Summarize desired end state and link to architecture decisions when available.

## Sequence

1. Preparation and compatibility layer.
2. Dual-write, dual-read, adapter, or feature-flag stage when needed.
3. Consumer migration.
4. Cutover.
5. Cleanup.
6. Documentation and runbook update.

## Validation and rollback

Define stage gates, rollback points, observability needs, and data-safety checks.

## Downstream routing

Use `architecture-design-desk`, `deployment-desk`, `release-operations-desk`, or `observability-readiness-desk` when migration affects those boundaries.
