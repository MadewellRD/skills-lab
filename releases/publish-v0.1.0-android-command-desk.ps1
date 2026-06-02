$ErrorActionPreference = "Stop"

$Tag = "android-command-desk-v0.1.0"
$Title = "Android Command Desk v0.1.0"
$Notes = "releases/android-command-desk-v0.1.0.md"
$PackageRoot = "dist/packages/android-command-desk"

Write-Host "Validating release assets..."
python tools/validate_release_assets.py

Write-Host "Publishing $Tag"
gh release create $Tag `
  --title $Title `
  --notes-file $Notes `
  "$PackageRoot/000-android-command-desk-skill.zip" `
  "$PackageRoot/001-android-product-requirements-desk-skill.zip" `
  "$PackageRoot/002-android-technical-discovery-desk-skill.zip" `
  "$PackageRoot/003-android-architecture-design-desk-skill.zip" `
  "$PackageRoot/004-android-ui-ux-desk-skill.zip" `
  "$PackageRoot/005-android-app-engineering-desk-skill.zip" `
  "$PackageRoot/006-android-game-engineering-desk-skill.zip" `
  "$PackageRoot/007-android-backend-integration-desk-skill.zip" `
  "$PackageRoot/008-android-security-privacy-desk-skill.zip" `
  "$PackageRoot/009-android-performance-optimization-desk-skill.zip" `
  "$PackageRoot/010-android-testing-qa-desk-skill.zip" `
  "$PackageRoot/011-android-release-store-ops-desk-skill.zip" `
  "$PackageRoot/012-android-observability-liveops-desk-skill.zip" `
  "$PackageRoot/013-android-maintenance-growth-desk-skill.zip" `
  "$PackageRoot/android-command-desk-v0.1.0-skill-bundles.zip" `
  "$PackageRoot/android-command-desk-v0.1.0-source.zip" `
  "$PackageRoot/android-command-desk-v0.1.0-CHECKSUMS.txt" `
  "dist/manifests/android-command-desk-v0.1.0.json" `
  "dist/manifests/android-command-desk-CHECKSUMS.txt" `
  "CHECKSUMS-android-command-desk-v0.1.0.txt"

Write-Host "Published $Tag"
