$ErrorActionPreference = "Stop"

$Tag = "ios-command-desk-v0.1.0"
$Title = "iOS Command Desk v0.1.0"
$Notes = "releases/ios-command-desk-v0.1.0.md"
$PackageRoot = "dist/packages/ios-command-desk"

Write-Host "Validating release assets..."
python tools/validate_release_assets.py

Write-Host "Publishing $Tag"
gh release create $Tag `
  --title $Title `
  --notes-file $Notes `
  "$PackageRoot/000-ios-command-desk-skill.zip" `
  "$PackageRoot/001-ios-product-requirements-desk-skill.zip" `
  "$PackageRoot/002-ios-technical-discovery-desk-skill.zip" `
  "$PackageRoot/003-ios-architecture-design-desk-skill.zip" `
  "$PackageRoot/004-ios-ui-ux-desk-skill.zip" `
  "$PackageRoot/005-ios-app-engineering-desk-skill.zip" `
  "$PackageRoot/006-ios-game-engineering-desk-skill.zip" `
  "$PackageRoot/007-ios-backend-integration-desk-skill.zip" `
  "$PackageRoot/008-ios-security-privacy-desk-skill.zip" `
  "$PackageRoot/009-ios-performance-optimization-desk-skill.zip" `
  "$PackageRoot/010-ios-testing-qa-desk-skill.zip" `
  "$PackageRoot/011-ios-release-app-store-ops-desk-skill.zip" `
  "$PackageRoot/012-ios-observability-liveops-desk-skill.zip" `
  "$PackageRoot/013-ios-maintenance-growth-desk-skill.zip" `
  "$PackageRoot/ios-command-desk-v0.1.0-skill-bundles.zip" `
  "$PackageRoot/ios-command-desk-v0.1.0-source.zip" `
  "$PackageRoot/ios-command-desk-v0.1.0-CHECKSUMS.txt" `
  "dist/manifests/ios-command-desk-v0.1.0.json" `
  "dist/manifests/ios-command-desk-CHECKSUMS.txt" `
  "CHECKSUMS-ios-command-desk-v0.1.0.txt"

Write-Host "Published $Tag"
