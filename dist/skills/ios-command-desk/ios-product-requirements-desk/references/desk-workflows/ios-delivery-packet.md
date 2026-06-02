# iOS Delivery Packet

The `ios_delivery_packet` is the shared state object carried across iOS Command Desk stages. Keep it compact, source-grounded, and safe for low-token handoff.

```yaml
ios_delivery_packet:
  workflow_mode:
  target_surface:
  app_or_game_lane:
  source_facts: []
  open_questions: []
  decisions: []
  risks: []
  acceptance_gates: []
  repo_facts:
    repository:
    branch:
    xcode_projects: []
    workspaces: []
    targets: []
    schemes: []
    bundle_ids: []
    validation_commands: []
  platform:
    supported_devices: []
    minimum_os:
    swift_version:
    frameworks: []
    entitlements: []
    signing_state:
    provisioning_state:
  game:
    engine_runtime:
    frame_budget:
    asset_pipeline:
    rendering_path:
    game_center:
    storekit:
  release:
    testflight_groups: []
    app_store_connect:
    rollout_plan:
    rollback_plan:
  ready_to_continue:
  ready_for_sdlc_handoff:
```
