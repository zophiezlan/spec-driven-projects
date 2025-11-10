param(
    [string]$Path = "nuaa-kit"
)

$ErrorFound = $false

# Get all markdown files under provided path
$files = Get-ChildItem -Path $Path -Recurse -Include *.md -File

foreach ($file in $files) {
    $content = Get-Content -Raw -Path $file.FullName

    # Detect front matter and status: final
    $isFinal = $false
    if ($content -match "(?s)^---\s*(.*?)\s*---") {
        $frontMatter = $Matches[1]
        if ($frontMatter -match "(?im)^status:\s*final\b") {
            $isFinal = $true
        }
    }

    if (-not $isFinal) { continue }

    # Strip fenced code blocks to reduce false positives
    $segments = $content -split "```"
  $outside = @()
  for ($i = 0; $i -lt $segments.Count; $i += 2) { $outside += $segments[$i] }
  $scanText = ($outside -join "\n")

  # Find bracket placeholders that are not markdown links [text](...) using negative lookahead
  $pattern = "\[[^\]]+\](?!\()"
  $matches = [System.Text.RegularExpressions.Regex]::Matches($scanText, $pattern)

  if ($matches.Count -gt 0) {
    Write-Error "Placeholder tokens found in FINAL document: $($file.FullName)"
    $ErrorFound = $true
  }
}

if ($ErrorFound) { exit 1 } else { Write-Host "No placeholder tokens found in final documents."; exit 0 }
