# Publish SDLC Command Desk v0.1.0 release assets.
# Run from the directory containing this script and the 19 skill zip archives.
# ASCII-only to avoid PowerShell parser issues on systems with non-UTF-8 defaults.

$ErrorActionPreference = "Stop"

gh release create v0.1.0 `
  000-sdlc-command-desk-skill.zip `
  001-product-requirements-desk-skill.zip `
  002-technical-discovery-desk-skill.zip `
  003-architecture-design-desk-skill.zip `
  004-issue-planning-desk-skill.zip `
  005-implementation-handoff-desk-skill.zip `
  006-review-quality-desk-skill.zip `
  007-test-strategy-desk-skill.zip `
  008-verification-desk-skill.zip `
  009-docs-traceability-desk-skill.zip `
  010-security-threat-desk-skill.zip `
  011-ci-failure-desk-skill.zip `
  012-release-operations-desk-skill.zip `
  013-deployment-desk-skill.zip `
  014-observability-readiness-desk-skill.zip `
  015-incident-response-desk-skill.zip `
  016-maintenance-refactor-desk-skill.zip `
  017-retrospective-desk-skill.zip `
  018-decommissioning-desk-skill.zip `
  CHECKSUMS.txt `
  --repo MadewellRD/skills-lab `
  --title "v0.1.0 - Initial SDLC Command Desk Suite" `
  --notes-file RELEASE_BODY.md
