# export-document.ps1
# Export assembled markdown documents to various formats

param(
    [string]$Initiative = "",
    [string]$Format = "docx",
    [string]$Output = "",
    [switch]$Json
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
. "$scriptDir\common.ps1"

function Test-Pandoc {
    $pandoc = Get-Command pandoc -ErrorAction SilentlyContinue
    if (-not $pandoc) {
        throw "pandoc is required for document export. Install: https://pandoc.org/installing.html"
    }
}

function Test-LaTeX {
    $xelatex = Get-Command xelatex -ErrorAction SilentlyContinue
    $pdflatex = Get-Command pdflatex -ErrorAction SilentlyContinue

    if (-not $xelatex -and -not $pdflatex) {
        throw "LaTeX is required for PDF export. Install: https://www.latex-project.org/get/"
    }
}

function Find-LatestDocument {
    param([string]$initiative)

    $finalDir = "initiatives\$initiative\final"
    if (-not (Test-Path $finalDir)) {
        throw "No final directory found for initiative: $initiative"
    }

    $latest = Get-ChildItem -Path "$finalDir\*.md" |
        Where-Object { $_.Name -notlike "*assembly-report.md" } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if (-not $latest) {
        throw "No assembled document found in $finalDir"
    }

    return $latest.FullName
}

function Export-ToDocx {
    param(
        [string]$inputFile,
        [string]$outputFile
    )

    $template = "nuaa-kit\templates\nuaa-word-template.docx"
    $args = @($inputFile, "-o", $outputFile, "--standalone")

    if (Test-Path $template) {
        $args += "--reference-doc=$template"
    }

    & pandoc $args

    if ($LASTEXITCODE -ne 0) {
        throw "pandoc conversion to DOCX failed"
    }

    return $outputFile
}

function Export-ToPdf {
    param(
        [string]$inputFile,
        [string]$outputFile
    )

    $template = "nuaa-kit\templates\nuaa-pdf-template.tex"
    $args = @($inputFile, "-o", $outputFile, "--pdf-engine=xelatex", "--standalone")

    if (Test-Path $template) {
        $args += "--template=$template"
    }

    & pandoc $args

    if ($LASTEXITCODE -ne 0) {
        throw "pandoc conversion to PDF failed"
    }

    return $outputFile
}

function Export-ToHtml {
    param(
        [string]$inputFile,
        [string]$outputFile
    )

    & pandoc $inputFile -o $outputFile --standalone --toc --css="nuaa-kit/templates/nuaa-style.css"

    if ($LASTEXITCODE -ne 0) {
        throw "pandoc conversion to HTML failed"
    }

    return $outputFile
}

# Main execution
try {
    # Check pandoc
    Test-Pandoc

    # Check LaTeX if exporting to PDF
    if ($Format -eq "pdf") {
        Test-LaTeX
    }

    # Find initiative
    if ([string]::IsNullOrEmpty($Initiative)) {
        $initiatives = Get-ChildItem -Path "initiatives" -Directory |
            Sort-Object LastWriteTime -Descending

        if ($initiatives.Count -eq 0) {
            throw "No initiatives found"
        }

        $Initiative = $initiatives[0].Name
    }

    if (-not (Test-Path "initiatives\$Initiative")) {
        throw "Initiative not found: $Initiative"
    }

    # Find latest document
    $inputFile = Find-LatestDocument -initiative $Initiative
    $basename = [System.IO.Path]::GetFileNameWithoutExtension($inputFile)

    # Determine output filename
    if ([string]::IsNullOrEmpty($Output)) {
        $Output = "initiatives\$Initiative\final\$basename.$Format"
    }

    # Export based on format
    $exportedFile = switch ($Format) {
        "docx" { Export-ToDocx -inputFile $inputFile -outputFile $Output }
        "pdf" { Export-ToPdf -inputFile $inputFile -outputFile $Output }
        "html" { Export-ToHtml -inputFile $inputFile -outputFile $Output }
        default { throw "Unsupported format: $Format" }
    }

    if ($Json) {
        $result = @{
            initiative = $Initiative
            input_file = $inputFile
            output_file = $exportedFile
            format = $Format
            success = $true
        }
        $result | ConvertTo-Json -Compress
    }
    else {
        Write-Host "✓ Exported: $exportedFile" -ForegroundColor Green
        Write-Host ""
        Write-Host "Document details:"
        Write-Host "  Initiative: $Initiative"
        Write-Host "  Format: $Format"
        $size = (Get-Item $exportedFile).Length / 1KB
        Write-Host "  Size: $([math]::Round($size, 2)) KB"
    }

    exit 0
}
catch {
    Write-Error $_.Exception.Message
    exit 1
}
