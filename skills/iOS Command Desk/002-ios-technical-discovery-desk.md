---
name: ios-technical-discovery-desk
description: inspect iOS repo, Xcode, Swift, package manager, dependency, device, engine, CI, feasibility, constraint, and unknown facts before implementation.
---

# iOS Technical Discovery Desk

## Status

Planned source stub.

## Role

Collect iOS source truth: repo layout, targets, schemes, Xcode/Swift versions, deployment target, SPM/CocoaPods/Carthage state, game engine, dependencies, entitlements, CI, tests, device assumptions, and unknowns.

## SDLC alignment

Use `technical-discovery-desk` patterns for feasibility, constraints, evidence, spikes, and halt conditions.

## Output contract

Produce a discovery memo with source facts, feasible paths, risks, unknowns, validation commands, and `ios_delivery_packet` updates.

## Halt behavior

Halt when repo access, project/workspace files, SDK versions, engine facts, dependency state, or validation commands are unavailable.
