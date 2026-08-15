<#
  publish-v1.1.1.ps1
  Run from D:\dev\skills-lab after applying the bundle and pushing main.

  This publishes v1.1.1 and removes the three exposed archives from the v1.0.0 and
  v1.1.0 releases. It does not delete tags, releases, or release notes.

  Nothing here is destructive to git history. The only deletions are three release
  ASSETS on each of two published releases, which is the point of the exercise.
#>

$ErrorActionPreference = 'Stop'

# gh prefers GITHUB_TOKEN over the valid keyring token, and the environment sets it to an
# invalid value, so every call returns HTTP 401 until both are cleared.
$env:GITHUB_TOKEN = ''
$env:GH_TOKEN     = ''

gh auth status
if ($LASTEXITCODE -ne 0) { throw 'gh not authenticated' }

# ---------------------------------------------------------------- preflight
Write-Host "`n== preflight ==" -ForegroundColor Cyan
python tools/audit_skills.py            | Select-Object -Last 1
if ($LASTEXITCODE -ne 0) { throw 'audit_skills failed' }
python tools/validate_presets.py        | Select-Object -Last 1
if ($LASTEXITCODE -ne 0) { throw 'validate_presets failed' }
python tools/validate_sdlc_suite.py     | Select-Object -Last 1
if ($LASTEXITCODE -ne 0) { throw 'validate_sdlc_suite failed' }
python tools/validate_release_assets.py | Select-Object -Last 1
if ($LASTEXITCODE -ne 0) { throw 'validate_release_assets failed' }

# Refuse to publish if any internal term survived into the packaged tree.
$leak = Select-String -Path 'dist/skills/**/*.md' -Pattern 'ROGUE|SOCIETY|PROMETHEUS|mrdOS|aitsm|SignalDesk' `
        -SimpleMatch:$false -ErrorAction SilentlyContinue
if ($leak) { $leak | Select-Object -First 5; throw 'internal terms still present in dist; not publishing' }
Write-Host 'scrub verified clean' -ForegroundColor Green

# ---------------------------------------------------------------- publish v1.1.1
Write-Host "`n== publishing 21 suite releases ==" -ForegroundColor Cyan
Get-ChildItem 'dist/packages' -Directory | ForEach-Object {
    $s  = $_.Name
    $mf = "dist/manifests/$s-v1.1.1.json"
    if (-not (Test-Path $mf)) { Write-Warning "no manifest for $s"; return }
    $title = (Get-Content $mf -Raw | ConvertFrom-Json).title
    $assets = @(Get-ChildItem "dist/packages/$s/*.zip" | ForEach-Object FullName) +
              @((Get-Item "dist/manifests/$s-CHECKSUMS.txt").FullName, (Get-Item $mf).FullName)
    gh release create "$s-v1.1.1" --title "$title v1.1.1" --notes-file "releases/$s-v1.1.1.md" @assets
    if ($LASTEXITCODE -eq 0) { Write-Host "  OK   $s ($($assets.Count) assets)" }
    else                     { Write-Warning "  FAIL $s" }
}

Write-Host "`n== repo-level v1.1.1, marked latest ==" -ForegroundColor Cyan
gh release create v1.1.1 --title 'Skills-Lab v1.1.1' --notes-file 'releases/v1.1.1.md' --latest `
    (Get-Item 'CHECKSUMS.txt').FullName (Get-Item 'MANIFEST.md').FullName

# ---------------------------------------------------------------- remediate old releases
# These three archives carry the exposed content. They are REMOVED from the older
# releases rather than replaced: substituting a different build would leave those tags
# advertising checksums that no longer match the assets sitting beside them.
Write-Host "`n== removing exposed assets from v1.0.0 and v1.1.0 ==" -ForegroundColor Cyan
$exposed = @(
  @{ tagBase = 'sdlc-command-desk';           asset = '006-goliveprompt-skill.zip' },
  @{ tagBase = 'ai-engineering-command-desk'; asset = '000-ai-engineering-command-desk-skill.zip' },
  @{ tagBase = 'ai-engineering-command-desk'; asset = '013-prompt-systems-desk-skill.zip' }
)
foreach ($v in @('1.0.0','1.1.0')) {
    foreach ($e in $exposed) {
        $tag = "$($e.tagBase)-v$v"
        gh release delete-asset $tag $e.asset --yes 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) { Write-Host "  removed $tag / $($e.asset)" }
        else                     { Write-Host "  not present $tag / $($e.asset)" -ForegroundColor DarkGray }
    }
}

# ---------------------------------------------------------------- point old releases here
$notice = @'

---

**Notice.** Three archives were removed from this release on 2026-07-25 because they
contained private operational configuration that should never have been published:
`006-goliveprompt-skill.zip`, `000-ai-engineering-command-desk-skill.zip`, and
`013-prompt-systems-desk-skill.zip`.

They were removed rather than replaced, because substituting a different build would leave
this tag advertising checksums that no longer match its assets. Clean equivalents are in
[v1.1.1](https://github.com/MadewellRD/skills-lab/releases/tag/v1.1.1).

If you downloaded any of those three archives before this date, your local copy still
contains the exposed content.
'@

Write-Host "`n== appending notice to affected releases ==" -ForegroundColor Cyan
foreach ($tag in @('v1.0.0','v1.1.0','sdlc-command-desk-v1.0.0','sdlc-command-desk-v1.1.0',
                   'ai-engineering-command-desk-v1.0.0','ai-engineering-command-desk-v1.1.0')) {
    $body = gh release view $tag --json body --jq .body 2>$null
    if ($LASTEXITCODE -ne 0) { Write-Host "  skip $tag (not found)" -ForegroundColor DarkGray; continue }
    if ($body -match 'Three archives were removed') { Write-Host "  skip $tag (already noted)"; continue }
    $tmp = New-TemporaryFile
    Set-Content -Path $tmp -Value ($body + $notice) -Encoding utf8
    gh release edit $tag --notes-file $tmp | Out-Null
    Remove-Item $tmp
    Write-Host "  noted $tag"
}

Write-Host "`n== done ==" -ForegroundColor Green
gh release list --limit 5
