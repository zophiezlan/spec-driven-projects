#!/usr/bin/env bash
# create-section-draft.sh
# Creates section directory and file, updates plan status

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

INITIATIVE=""
SECTION=""
JSON_MODE=false

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --json) JSON_MODE=true; shift ;;
            --initiative) INITIATIVE="$2"; shift 2 ;;
            --section) SECTION="$2"; shift 2 ;;
            *) echo "Unknown option: $1" >&2; exit 1 ;;
        esac
    done
}

find_initiative() {
    local initiative="$1"
    if [[ -z "$initiative" ]]; then
        # Find most recently modified initiative
        if [[ ! -d "initiatives" ]]; then
            echo "Error: No initiatives directory found" >&2
            exit 1
        fi
        initiative=$(ls -t initiatives/ 2>/dev/null | head -n 1)
        if [[ -z "$initiative" ]]; then
            echo "Error: No initiatives found" >&2
            exit 1
        fi
    fi
    if [[ ! -d "initiatives/$initiative" ]]; then
        echo "Error: Initiative not found: $initiative" >&2
        exit 1
    fi
    echo "$initiative"
}

create_section_file() {
    local initiative="$1"
    local section="$2"
    local sections_dir="initiatives/$initiative/sections"

    # Create sections directory if it doesn't exist
    mkdir -p "$sections_dir"

    # Convert section name to filename (lowercase, hyphens)
    local filename=$(echo "$section" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
    local section_file="$sections_dir/${filename}.md"

    # Check if file already exists
    if [[ -f "$section_file" ]]; then
        echo "Error: Section file already exists: $section_file" >&2
        exit 1
    fi

    # Get section info from plan
    local plan_file="initiatives/$initiative/plan.md"
    if [[ ! -f "$plan_file" ]]; then
        echo "Error: Plan file not found: $plan_file" >&2
        exit 1
    fi

    # Extract gate and purpose from plan
    # Look for section header and extract gate number
    local gate=$(grep -A 10 "^###.*: $section$" "$plan_file" | grep "^\*\*Gate\*\*:" | head -1 | sed 's/.*Gate \([0-9]\).*/\1/')
    if [[ -z "$gate" ]]; then
        gate="?"
    fi

    # Extract purpose
    local purpose=$(grep -A 15 "^###.*: $section$" "$plan_file" | grep "^\*\*Purpose\*\*:" | head -1 | sed 's/^\*\*Purpose\*\*: //')
    if [[ -z "$purpose" ]]; then
        purpose="[Purpose not found in plan]"
    fi

    # Get current date
    local date=$(date +%Y-%m-%d)

    # Read template
    local template_file="nuaa-kit/templates/section-template.md"
    if [[ ! -f "$template_file" ]]; then
        echo "Error: Template not found: $template_file" >&2
        exit 1
    fi

    # Create section file from template with replacements
    sed -e "s/\[SECTION_NAME\]/$section/g" \
        -e "s/\[INITIATIVE_NUMBER\]-\[SLUG\]/$initiative/g" \
        -e "s/\[N\]/$gate/g" \
        -e "s/\[Gate Name\]/Gate $gate/g" \
        -e "s/\[DATE\]/$date/g" \
        -e "s/\[Clear statement.*\]/$purpose/" \
        "$template_file" > "$section_file"

    echo "$section_file"
}

update_plan_status() {
    local plan_file="$1"
    local section="$2"
    local new_status="$3"

    # Find the section in the plan and update its status
    # This uses a temporary file for safe in-place editing
    local temp_file=$(mktemp)
    local in_section=false

    while IFS= read -r line; do
        if [[ $line =~ ^###[[:space:]].*:[[:space:]]$section$ ]]; then
            in_section=true
            echo "$line"
        elif [[ $in_section == true ]] && [[ $line =~ ^\*\*Status\*\*: ]]; then
            echo "**Status**: $new_status"
            in_section=false
        elif [[ $in_section == true ]] && [[ $line =~ ^### ]]; then
            # Hit next section without finding status - just output
            in_section=false
            echo "$line"
        else
            echo "$line"
        fi
    done < "$plan_file" > "$temp_file"

    mv "$temp_file" "$plan_file"
}

main() {
    parse_args "$@"

    if [[ -z "$SECTION" ]]; then
        echo "Error: Section name required (--section)" >&2
        exit 1
    fi

    local initiative=$(find_initiative "$INITIATIVE")
    local section_file=$(create_section_file "$initiative" "$SECTION")

    # Update plan status
    local plan_file="initiatives/$initiative/plan.md"
    update_plan_status "$plan_file" "$SECTION" "In Progress"

    if [[ $JSON_MODE == true ]]; then
        echo "{"
        echo "  \"initiative\": \"$initiative\","
        echo "  \"section\": \"$SECTION\","
        echo "  \"section_file\": \"$section_file\","
        echo "  \"plan_updated\": true"
        echo "}"
    else
        echo "✓ Created section: $section_file"
        echo "✓ Updated plan status: In Progress"
        echo ""
        echo "Next steps:"
        echo "  1. Have AI draft content using /nuaa.draft \"$SECTION\""
        echo "  2. Review the draft in $section_file"
        echo "  3. Validate with: nuaa gate-check \"$SECTION\""
    fi
}

main "$@"
