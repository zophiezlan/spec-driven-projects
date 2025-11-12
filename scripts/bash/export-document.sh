#!/usr/bin/env bash
# export-document.sh
# Export assembled markdown documents to various formats

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

INITIATIVE=""
FORMAT="docx"
OUTPUT=""
JSON_MODE=false

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Export assembled documents to Word, PDF, or other formats.

Options:
    --initiative INIT   Initiative to export (default: most recent)
    --format FORMAT     Export format: docx, pdf, html (default: docx)
    --output FILE       Output filename (default: auto-generated)
    --json              Output JSON result
    --help, -h          Show this help message

Examples:
    $0 --format docx
    $0 --initiative 001-naloxone --format pdf --output proposal.pdf

Requirements:
    - pandoc must be installed for format conversion
    - For PDF: xelatex or pdflatex must be available
EOF
}

check_pandoc() {
    if ! command -v pandoc &> /dev/null; then
        echo "Error: pandoc is required for document export" >&2
        echo "Install: https://pandoc.org/installing.html" >&2
        exit 1
    fi
}

check_latex() {
    if ! command -v xelatex &> /dev/null && ! command -v pdflatex &> /dev/null; then
        echo "Error: LaTeX is required for PDF export" >&2
        echo "Install: https://www.latex-project.org/get/" >&2
        exit 1
    fi
}

find_latest_document() {
    local initiative="$1"
    local final_dir="initiatives/$initiative/final"

    if [[ ! -d "$final_dir" ]]; then
        echo "Error: No final directory found for initiative: $initiative" >&2
        exit 1
    fi

    # Find latest version markdown file (exclude assembly-report)
    local latest=$(ls -t "$final_dir"/*.md 2>/dev/null | grep -v "assembly-report.md" | head -n 1)

    if [[ -z "$latest" ]]; then
        echo "Error: No assembled document found in $final_dir" >&2
        exit 1
    fi

    echo "$latest"
}

export_to_docx() {
    local input_file="$1"
    local output_file="$2"
    local template="nuaa-kit/templates/nuaa-word-template.docx"

    local pandoc_args=(
        "$input_file"
        "-o" "$output_file"
        "--standalone"
    )

    # Use reference doc if available
    if [[ -f "$template" ]]; then
        pandoc_args+=("--reference-doc=$template")
    fi

    pandoc "${pandoc_args[@]}"

    if [[ $? -eq 0 ]]; then
        echo "$output_file"
    else
        echo "Error: pandoc conversion to DOCX failed" >&2
        exit 1
    fi
}

export_to_pdf() {
    local input_file="$1"
    local output_file="$2"
    local template="nuaa-kit/templates/nuaa-pdf-template.tex"

    local pandoc_args=(
        "$input_file"
        "-o" "$output_file"
        "--pdf-engine=xelatex"
        "--standalone"
    )

    # Use template if available
    if [[ -f "$template" ]]; then
        pandoc_args+=("--template=$template")
    fi

    pandoc "${pandoc_args[@]}"

    if [[ $? -eq 0 ]]; then
        echo "$output_file"
    else
        echo "Error: pandoc conversion to PDF failed" >&2
        exit 1
    fi
}

export_to_html() {
    local input_file="$1"
    local output_file="$2"

    pandoc "$input_file" \
        -o "$output_file" \
        --standalone \
        --toc \
        --css="nuaa-kit/templates/nuaa-style.css"

    if [[ $? -eq 0 ]]; then
        echo "$output_file"
    else
        echo "Error: pandoc conversion to HTML failed" >&2
        exit 1
    fi
}

main() {
    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --initiative) INITIATIVE="$2"; shift 2 ;;
            --format) FORMAT="$2"; shift 2 ;;
            --output) OUTPUT="$2"; shift 2 ;;
            --json) JSON_MODE=true; shift ;;
            --help|-h) usage; exit 0 ;;
            *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
        esac
    done

    # Check pandoc
    check_pandoc

    # Check LaTeX if exporting to PDF
    if [[ "$FORMAT" == "pdf" ]]; then
        check_latex
    fi

    # Find initiative
    if [[ -z "$INITIATIVE" ]]; then
        INITIATIVE=$(ls -t initiatives/ 2>/dev/null | head -n 1)
    fi

    if [[ ! -d "initiatives/$INITIATIVE" ]]; then
        echo "Error: Initiative not found: $INITIATIVE" >&2
        exit 1
    fi

    # Find latest document
    local input_file=$(find_latest_document "$INITIATIVE")
    local basename=$(basename "$input_file" .md)

    # Determine output filename
    if [[ -z "$OUTPUT" ]]; then
        OUTPUT="initiatives/$INITIATIVE/final/$basename.$FORMAT"
    fi

    # Export based on format
    local exported_file
    case "$FORMAT" in
        docx) exported_file=$(export_to_docx "$input_file" "$OUTPUT") ;;
        pdf) exported_file=$(export_to_pdf "$input_file" "$OUTPUT") ;;
        html) exported_file=$(export_to_html "$input_file" "$OUTPUT") ;;
        *) echo "Error: Unsupported format: $FORMAT" >&2; exit 1 ;;
    esac

    if [[ $JSON_MODE == true ]]; then
        echo "{"
        echo "  \"initiative\": \"$INITIATIVE\","
        echo "  \"input_file\": \"$input_file\","
        echo "  \"output_file\": \"$exported_file\","
        echo "  \"format\": \"$FORMAT\","
        echo "  \"success\": true"
        echo "}"
    else
        echo "✓ Exported: $exported_file"
        echo ""
        echo "Document details:"
        echo "  Initiative: $INITIATIVE"
        echo "  Format: $FORMAT"
        echo "  Size: $(du -h "$exported_file" | cut -f1)"
    fi
}

main "$@"
