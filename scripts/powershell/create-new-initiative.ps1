# create-new-initiative.ps1
# Creates a new NUAA initiative directory with auto-incrementing number and specification template

param(
    [Parameter(Mandatory=$false)]
    [switch]$Json,
    
    [Parameter(Mandatory=$false)]
    [string]$ShortName = "",
    
    [Parameter(Mandatory=$false)]
    [int]$Number = 0,
    
    [Parameter(Mandatory=$false)]
    [switch]$Help,
    
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Description
)

if ($Help) {
    Write-Host "Usage: .\create-new-initiative.ps1 [OPTIONS] <initiative_description>"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -Json               Output in JSON format"
    Write-Host "  -ShortName <name>   Provide a custom short name (2-4 words) for the initiative"
    Write-Host "  -Number N           Specify initiative number manually (overrides auto-detection)"
    Write-Host "  -Help               Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "  .\create-new-initiative.ps1 'Peer-led naloxone distribution program' -ShortName 'naloxone-distribution'"
    Write-Host "  .\create-new-initiative.ps1 'Mobile harm reduction van for regional NSW' -Number 5"
    exit 0
}

$DescriptionText = $Description -join ' '
if ([string]::IsNullOrWhiteSpace($DescriptionText)) {
    Write-Error "Usage: .\create-new-initiative.ps1 [OPTIONS] <initiative_description>"
    exit 1
}

# Function to find the repository root
function Find-RepoRoot {
    param([string]$StartPath)
    
    $dir = $StartPath
    while ($dir -ne [System.IO.Path]::GetPathRoot($dir)) {
        if ((Test-Path (Join-Path $dir '.git')) -or 
            (Test-Path (Join-Path $dir '.nuaa')) -or 
            (Test-Path (Join-Path $dir 'nuaa-kit'))) {
            return $dir
        }
        $dir = Split-Path $dir -Parent
    }
    return $null
}

# Function to get highest initiative number from initiatives directory
function Get-HighestFromInitiatives {
    param([string]$InitiativesDir)
    
    $highest = 0
    
    if (Test-Path $InitiativesDir) {
        $dirs = Get-ChildItem -Path $InitiativesDir -Directory -ErrorAction SilentlyContinue
        foreach ($dir in $dirs) {
            if ($dir.Name -match '^(\d{3})-') {
                $num = [int]$matches[1]
                if ($num -gt $highest) {
                    $highest = $num
                }
            }
        }
    }
    
    return $highest
}

# Function to clean and format an initiative slug
function Clean-Slug {
    param([string]$Name)
    
    $slug = $Name.ToLower()
    $slug = $slug -replace '[^a-z0-9]', '-'
    $slug = $slug -replace '-+', '-'
    $slug = $slug.Trim('-')
    
    return $slug
}

# Function to generate slug from description with stop word filtering
function Generate-Slug {
    param([string]$Description)
    
    # Common stop words to filter out
    $stopWords = @(
        'i', 'a', 'an', 'the', 'to', 'for', 'of', 'in', 'on', 'at', 'by', 'with', 
        'from', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 
        'had', 'do', 'does', 'did', 'will', 'would', 'should', 'could', 'can', 
        'may', 'might', 'must', 'shall', 'this', 'that', 'these', 'those', 'my', 
        'your', 'our', 'their', 'want', 'need', 'add', 'get', 'set'
    )
    
    # Convert to lowercase and split into words
    $cleanName = $Description.ToLower() -replace '[^a-z0-9]', ' '
    $words = $cleanName -split '\s+' | Where-Object { $_ -ne '' }
    
    # Filter words: remove stop words and words shorter than 3 chars
    $meaningfulWords = @()
    foreach ($word in $words) {
        if ($word.Length -ge 3 -and $stopWords -notcontains $word) {
            $meaningfulWords += $word
        }
    }
    
    # Use first 3-4 meaningful words
    if ($meaningfulWords.Count -gt 0) {
        $maxWords = if ($meaningfulWords.Count -eq 4) { 4 } else { 3 }
        $selectedWords = $meaningfulWords | Select-Object -First $maxWords
        return ($selectedWords -join '-')
    }
    else {
        # Fallback: use original logic
        $cleaned = Clean-Slug $Description
        $parts = $cleaned -split '-' | Where-Object { $_ -ne '' } | Select-Object -First 3
        return ($parts -join '-')
    }
}

# Resolve repository root
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

try {
    $gitRoot = git rev-parse --show-toplevel 2>$null
    if ($LASTEXITCODE -eq 0) {
        $repoRoot = $gitRoot
    }
    else {
        throw "Git not available"
    }
}
catch {
    $repoRoot = Find-RepoRoot $scriptDir
    if ($null -eq $repoRoot) {
        Write-Error "Could not determine repository root. Please run this script from within the repository."
        exit 1
    }
}

Set-Location $repoRoot

$initiativesDir = Join-Path $repoRoot 'initiatives'
if (-not (Test-Path $initiativesDir)) {
    New-Item -ItemType Directory -Path $initiativesDir -Force | Out-Null
}

# Generate slug
if (-not [string]::IsNullOrWhiteSpace($ShortName)) {
    $slug = Clean-Slug $ShortName
}
else {
    $slug = Generate-Slug $DescriptionText
}

# Determine initiative number
if ($Number -eq 0) {
    $highest = Get-HighestFromInitiatives $initiativesDir
    $Number = $highest + 1
}

$initiativeNum = "{0:D3}" -f $Number
$initiativeName = "${initiativeNum}-${slug}"

# Validate length (conservative limit for directory names)
$maxNameLength = 100
if ($initiativeName.Length -gt $maxNameLength) {
    # Truncate slug
    $maxSlugLength = $maxNameLength - 4  # Account for NNN-
    $truncatedSlug = $slug.Substring(0, [Math]::Min($slug.Length, $maxSlugLength)).TrimEnd('-')
    
    $originalName = $initiativeName
    $initiativeName = "${initiativeNum}-${truncatedSlug}"
    $slug = $truncatedSlug
    
    if (-not $Json) {
        Write-Warning "[nuaa] Initiative name exceeded length limit"
        Write-Warning "[nuaa] Original: $originalName ($($originalName.Length) chars)"
        Write-Warning "[nuaa] Truncated to: $initiativeName ($($initiativeName.Length) chars)"
    }
}

$initiativeDir = Join-Path $initiativesDir $initiativeName

# Check if directory already exists
if (Test-Path $initiativeDir) {
    Write-Error "Initiative directory already exists: $initiativeDir"
    exit 1
}

# Create directory
New-Item -ItemType Directory -Path $initiativeDir -Force | Out-Null

# Copy template
$templatePath = Join-Path $repoRoot 'nuaa-kit/templates/program-specification-template.md'
$specFile = Join-Path $initiativeDir 'spec.md'

if (-not (Test-Path $templatePath)) {
    Write-Error "Template not found at $templatePath"
    Write-Error "Please ensure you're running this script from a NUAA project."
    exit 1
}

Copy-Item -Path $templatePath -Destination $specFile

# Populate template with metadata
$createdDate = Get-Date -Format 'yyyy-MM-dd'

$content = Get-Content -Path $specFile -Raw
$content = $content -replace '\[INITIATIVE_NUMBER\]', $initiativeNum
$content = $content -replace '\[INITIATIVE_SLUG\]', $slug
$content = $content -replace '\[CREATED_DATE\]', $createdDate
$content = $content -replace '\[PROGRAM_NAME\]', $DescriptionText
Set-Content -Path $specFile -Value $content -NoNewline

# Set environment variable for the current session
$env:NUAA_INITIATIVE = $initiativeName

# Output JSON or human-readable format
if ($Json) {
    $output = @{
        initiative = $initiativeName
        spec_file = $specFile
        initiative_dir = $initiativeDir
        number = $initiativeNum
        slug = $slug
    }
    $output | ConvertTo-Json -Compress
}
else {
    Write-Host "INITIATIVE: $initiativeName"
    Write-Host "SPEC_FILE: $specFile"
    Write-Host "INITIATIVE_DIR: $initiativeDir"
    Write-Host "NUMBER: $initiativeNum"
    Write-Host "SLUG: $slug"
    Write-Host "NUAA_INITIATIVE environment variable set to: $initiativeName"
}
