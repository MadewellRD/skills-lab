# Android Game Development Baseline

Use this reference when an Android game workflow needs implementation or review defaults and the repo does not supply a stronger local convention.

## Supported game lanes
- Native/AGDK/NDK lane for C/C++, CMake, native libraries, frame pacing, and Android-specific performance work.
- Engine integration lane for Unity, Unreal, Godot, custom engines, Play services, packaging, and Android wrapper concerns.
- Release/package lane for AAB/APK, Play Asset Delivery, signing, versioning, Play Games Services, store listing, staged rollout, and rollback.

## Evidence to collect
- engine/runtime and version, native toolchain, CMake/NDK facts, Gradle packaging, plugin configuration
- target devices, graphics/API assumptions, frame budget, input modes, controller requirements, orientation, lifecycle expectations
- asset pipeline, install size, Play Asset Delivery needs, expansion-file legacy status, cloud saves, multiplayer, leaderboards, billing
- profiling/QA evidence such as Android GPU Inspector, system traces, frame pacing data, gameplay smoke tests, device matrix, CI/build output

## Halt triggers
- engine/runtime or native toolchain is unknown
- gameplay scope, frame budget, target devices, or input model is missing
- build/package/release path is unknown
- requested Play, live-ops, economy, multiplayer, or production-impacting action lacks approval
