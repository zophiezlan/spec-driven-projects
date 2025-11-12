# check-gate-status.ps1
# Validates section gate status and dependencies

param(
    [string]$Initiative = "",
    [string]$Section = "",
    [switch]$Json
)

# Source common functions
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$scriptDir\common.ps1"

# Find initiative directory
function Find-Initiative {
    param([string]$initiativeName)
    
    if ([string]::IsNullOrEmpty($initiativeName)) {
        # Find most recent initiative
        if (-not (Test-Path "initiatives")) {
            throw "initiatives directory not found"
        }
        
        $initiatives = Get-ChildItem -Path "initiatives" -Directory |
            Sort-Object LastWriteTime -Descending
        
        if ($initiatives.Count -eq 0) {
            throw "No initiatives found"
        }
        
        $initiativeName = $initiatives[0].Name
    }
    
    $path = "initiatives\$initiativeName"
    if (-not (Test-Path $path)) {
        throw "Initiative not found: $initiativeName"
    }
    
    return $initiativeName
}

# Extract section info from plan
function Get-SectionInfo {
    param(
        [string]$planFile,
        [string]$sectionName
    )
    
    $content = Get-Content $planFile -Raw
    $lines = $content -split "`r?`n"
    
    $inSection = $false
    $gate = ""
    $deps = ""
    $status = ""
    
    foreach ($line in $lines) {
        if ($line -match "^###\s+Section.*:\s+$sectionName$") {
            $inSection = $true
            continue
        }
        
        if ($inSection) {
            if ($line -match '^\*\*Gate\*\*:\s*Gate\s+(\d)') {
                $gate = $Matches[1]
            }
            elseif ($line -match '^\*\*Dependencies\*\*:\s*(.+)$') {
                $deps = $Matches[1]
            }
            elseif ($line -match '^\*\*Status\*\*:\s*(.+)$') {
                $status = $Matches[1]
            }
            elseif ($line -match '^###') {
                # Hit next section
                break
            }
        }
    }
    
    return @{
        Gate = $gate
        Dependencies = $deps
        Status = $status
    }
}

# Check if dependencies are satisfied
function Test-Dependencies {
    param(
        [string]$planFile,
        [string]$deps
    )
    
    if ($deps -eq "None" -or [string]::IsNullOrEmpty($deps)) {
        return @{
            Satisfied = $true
            Failed = @()
        }
    }
    
    $depArray = $deps -split ',' | ForEach-Object { $_.Trim() }
    $failedDeps = @()
    
    foreach ($dep in $depArray) {
        $depInfo = Get-SectionInfo -planFile $planFile -sectionName $dep
        
        if ($depInfo.Status -ne "Passed") {
            $failedDeps += "$dep (status: $($depInfo.Status))"
        }
    }
    
    return @{
        Satisfied = ($failedDeps.Count -eq 0)
        Failed = $failedDeps
    }
}

# Main execution
try {
    $initiative = Find-Initiative -initiativeName $Initiative
    $planFile = "initiatives\$initiative\plan.md"
    
    if (-not (Test-Path $planFile)) {
        throw "Plan file not found: $planFile"
    }
    
    if ([string]::IsNullOrEmpty($Section)) {
        if ($Json) {
            Write-Error '{"error": "Section name required in JSON mode"}'
            exit 1
        }
        
        Write-Host "Initiative: $initiative"
        Write-Host "Plan: $planFile"
        Write-Host ""
        Write-Host "Use -Section to check a specific section"
        exit 0
    }
    
    # Get section info
    $sectionInfo = Get-SectionInfo -planFile $planFile -sectionName $Section
    
    if ([string]::IsNullOrEmpty($sectionInfo.Gate)) {
        throw "Section not found in plan: $Section"
    }
    
    # Check dependencies
    $depsResult = Test-Dependencies -planFile $planFile -deps $sectionInfo.Dependencies
    
    if ($Json) {
        $output = @{
            initiative = $initiative
            section = $Section
            gate = [int]$sectionInfo.Gate
            status = $sectionInfo.Status
            dependencies = $sectionInfo.Dependencies
            dependencies_satisfied = $depsResult.Satisfied
        }
        
        $output | ConvertTo-Json -Compress
    }
    else {
        Write-Host "Section: $Section"
        Write-Host "Gate: $($sectionInfo.Gate)"
        Write-Host "Status: $($sectionInfo.Status)"
        Write-Host "Dependencies: $($sectionInfo.Dependencies)"
        Write-Host ""
        
        if ($depsResult.Satisfied) {
            Write-Host "✓ Ready to proceed" -ForegroundColor Green
        }
        else {
            Write-Host "✗ Blocked by dependencies:" -ForegroundColor Red
            foreach ($failed in $depsResult.Failed) {
                Write-Host "  - $failed" -ForegroundColor Yellow
            }
        }
    }
    
    exit $(if ($depsResult.Satisfied) { 0 } else { 1 })
}
catch {
    Write-Error $_.Exception.Message
    exit 1
}
