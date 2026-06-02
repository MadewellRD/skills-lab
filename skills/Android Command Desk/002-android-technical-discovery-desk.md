---
name: android-technical-discovery-desk
description: inspect Android repo, Gradle, SDK, NDK, dependency, device, engine, CI, feasibility, constraint, and unknown facts before implementation.
---

# Android Technical Discovery Desk

## Status

Planned source stub.

## Role

Collect Android source truth: repo layout, modules, Gradle state, Kotlin/Java versions, compile/min/target SDK, NDK/CMake use, game engine, dependencies, permissions, CI, tests, device assumptions, and unknowns.

## SDLC alignment

Use `technical-discovery-desk` patterns for feasibility, constraints, evidence, spikes, and halt conditions.

## Output contract

Produce a discovery memo with source facts, feasible paths, risks, unknowns, validation commands, and `android_delivery_packet` updates.

## Halt behavior

Halt when repo access, Gradle files, SDK versions, engine facts, dependency state, or validation commands are unavailable.
