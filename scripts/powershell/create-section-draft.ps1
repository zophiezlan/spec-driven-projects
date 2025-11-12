# create-section-draft.ps1
# Creates section directory and file, updates plan status

param(
    [string]$Initiative = "",
    [string]$Section = "",
    [switch]$Json
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$scriptDir\common.ps1"

function Find-Initiative {
    param([string]$name)

    if ([string]::IsNullOrEmpty($name)) {
        # Find most recently modified initiative
        if (-not (Test-Path "initiatives")) {
            throw "No initiatives directory found"
        }

        $initiatives = Get-ChildItem -Path "initiatives" -Directory |
            Sort-Object LastWriteTime -Descending

        if ($initiatives.Count -eq 0) {
            throw "No initiatives found"
        }
        $name = $initiatives[0].Name
    }

    if (-not (Test-Path "initiatives\$name")) {
        throw "Initiative not found: $name"
    }

    return $name
}

function New-SectionFile {
    param(
        [string]$initiative,
        [string]$sectionName
    )

    $sectionsDir = "initiatives\$initiative\sections"
    New-Item -ItemType Directory -Path $sectionsDir -Force | Out-Null

    # Convert section name to filename (lowercase, hyphens)
    $filename = $sectionName.ToLower() -replace ' ', '-'
    $sectionFile = "$sectionsDir\$filename.md"

    if (Test-Path $sectionFile) {
        throw "Section file already exists: $sectionFile"
    }

    # Get section info from plan
    $planFile = "initiatives\$initiative\plan.md"
    if (-not (Test-Path $planFile)) {
        throw "Plan file not found: $planFile"
    }

    $planContent = Get-Content $planFile -Raw

    # Extract gate number (simplified regex)
    $gate = "?"
    if ($planContent -match "###[^\n]*:\s+$sectionName\s*\n(?:.|\n)*?\*\*Gate\*\*:\s*Gate\s+(\d)") {
        $gate = $Matches[1]
    }

    # Extract purpose (simplified regex)
    $purpose = "[Purpose not found in plan]"
    if ($planContent -match "###[^\n]*:\s+$sectionName\s*\n(?:.|\n)*?\*\*Purpose\*\*:\s*([^\n]+)") {
        $purpose = $Matches[1]
    }

    # Get current date
    $date = Get-Date -Format "yyyy-MM-dd"

    # Read template
    $templateFile = "nuaa-kit\templates\section-template.md"
    if (-not (Test-Path $templateFile)) {
        throw "Template not found: $templateFile"
    }

    # Create section file from template
    $content = Get-Content $templateFile -Raw
    $content = $content -replace '\[SECTION_NAME\]', $sectionName
    $content = $content -replace '\[INITIATIVE_NUMBER\]-\[SLUG\]', $initiative
    $content = $content -replace '\[N\]', $gate
    $content = $content -replace '\[Gate Name\]', "Gate $gate"
    $content = $content -replace '\[DATE\]', $date
    $content = $content -replace '\[Clear statement.*?\]', $purpose

    Set-Content -Path $sectionFile -Value $content -NoNewline

    return $sectionFile
}

function Update-PlanStatus {
    param(
        [string]$planFile,
        [string]$sectionName,
        [string]$newStatus
    )

    $lines = Get-Content $planFile
    $output = @()
    $inSection = $false

    foreach ($line in $lines) {
        if ($line -match "^###\s+.*:\s+$sectionName\s*$") {
            $inSection = $true
            $output += $line
        }
        elseif ($inSection -and $line -match '^\*\*Status\*\*:\s*') {
            $output += "**Status**: $newStatus"
            $inSection = $false
        }
        elseif ($inSection -and $line -match '^###\s+') {
            # Hit next section without finding status
            $inSection = $false
            $output += $line
        }
        else {
            $output += $line
        }
    }

    Set-Content -Path $planFile -Value ($output -join "`n") -NoNewline
}

# Main execution
try {
    if ([string]::IsNullOrEmpty($Section)) {
        throw "Section name required (-Section)"
    }

    $initiativeName = Find-Initiative -name $Initiative
    $sectionFile = New-SectionFile -initiative $initiativeName -sectionName $Section

    # Update plan status
    $planFile = "initiatives\$initiativeName\plan.md"
    Update-PlanStatus -planFile $planFile -sectionName $Section -newStatus "In Progress"

    if ($Json) {
        $output = @{
            initiative = $initiativeName
            section = $Section
            section_file = $sectionFile
            plan_updated = $true
        }
        $output | ConvertTo-Json -Compress
    }
    else {
        Write-Host "✓ Created section: $sectionFile" -ForegroundColor Green
        Write-Host "✓ Updated plan status: In Progress" -ForegroundColor Green
        Write-Host ""
        Write-Host "Next steps:"
        Write-Host "  1. Have AI draft content using /nuaa.draft `"$Section`"" -ForegroundColor Cyan
        Write-Host "  2. Review the draft in $sectionFile"
        Write-Host "  3. Validate with: nuaa gate-check `"$Section`"" -ForegroundColor Cyan
    }

    exit 0
}
catch {
    Write-Error $_.Exception.Message
    exit 1
}
