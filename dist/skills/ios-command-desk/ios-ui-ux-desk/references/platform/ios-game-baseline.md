# iOS Game Baseline

Use for game-focused iOS work.

- SpriteKit is the fast 2D prototype and production lane when custom rendering is not the main risk.
- SceneKit remains useful for lightweight 3D scenes when repo facts already support it.
- Metal and MetalFX are the performance-critical rendering, GPU control, upscaling, and frame pacing lane.
- Unity, Unreal, Godot, or custom engines require explicit engine/runtime, plugin, native bridge, and asset-pipeline evidence.
- Game Center/GameKit covers identity, achievements, leaderboards, multiplayer, matchmaking, and saved games.
- StoreKit covers purchases, subscriptions, consumables, and monetization flows.

Required checks: engine/runtime version, target devices, frame budget, memory budget, thermal expectations, controller/input support, asset pipeline, shaders/render path, binary size, Game Center, StoreKit, multiplayer, privacy labels, age rating, gameplay smoke tests, profiling, TestFlight groups, and rollback.
