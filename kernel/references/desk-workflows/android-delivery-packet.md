# Android Delivery Packet

Preserve this packet shape across Android Command Desk stages.

```yaml
android_delivery_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  current_stage: "stage-name"
  completed_stages:
    - "stage-name"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"
  target_surface: "native_app | hybrid_app | android_tv | wear_os | android_auto | game | game_service | play_release | maintenance | unknown"
  app_or_game_lane: "app | game | mixed | unknown"
  business_goal: "source-backed goal or unknown"
  audience_segments: []
  supported_devices: []
  min_sdk: "source-backed value or unknown"
  target_sdk: "source-backed value or unknown"
  compile_sdk: "source-backed value or unknown"
  package_name: "source-backed value or unknown"
  application_id: "source-backed value or unknown"
  repo:
    owner: "owner-or-unknown"
    name: "repo-or-unknown"
    branch: "branch-or-unknown"
  modules: []
  build_system: []
  gradle: []
  kotlin_java: []
  ndk_cmake: []
  engine_runtime: []
  architecture_lane: "modern_native | legacy_native | modularization | native_game | engine_integration | mixed | unknown"
  screens: []
  user_flows: []
  navigation: []
  ui_framework: "compose | view_xml | hybrid | engine_ui | unknown"
  backend_integrations: []
  api_contracts: []
  permissions: []
  privacy_requirements: []
  security_controls: []
  performance_budgets: []
  benchmark_commands: []
  profiling_tools: []
  test_matrix: []
  device_matrix: []
  validation_commands: []
  release_target: []
  signing_state: "source-backed value or unknown"
  play_track: "internal | closed | open | production | unknown"
  rollout_plan: []
  rollback_plan: []
  observability_requirements: []
  analytics_events: []
  feature_flags: []
  remote_config: []
  liveops_controls: []
  maintenance_trigger: "source-backed trigger or unknown"
  source_facts:
    - fact: "source-backed fact"
      source: "github | docs | user | connector | uploaded_file | ci | benchmark | play_console | unknown"
  decisions:
    - "decision made at this stage"
  open_questions:
    - "question blocking later work"
  artifacts:
    - "artifact name or path"
  halt_conditions:
    - "condition that requires stopping"
  ready_to_continue: true
```

## Packet discipline
- Keep packet entries compact and source-backed.
- Do not paste entire files, benchmark reports, Play policy pages, or traces into the packet.
- Store bulky evidence as artifact paths or source references.
- Update only fields touched by the current stage.
- Set `ready_to_continue: false` when a halt condition blocks downstream work.
