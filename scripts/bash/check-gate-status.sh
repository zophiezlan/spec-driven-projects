#!/usr/bin/env bash
# check-gate-status.sh
# Validates section gate status and dependencies

set -e

# Source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Parse arguments
INITIATIVE=""
SECTION=""
JSON_MODE=false

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --json)
                JSON_MODE=true
                shift
                ;;
            --initiative)
                INITIATIVE="$2"
                shift 2
                ;;
            --section)
                SECTION="$2"
                shift 2
                ;;
            *)
                echo "Unknown option: $1" >&2
                exit 1
                ;;
        esac
    done
}

# Find initiative directory
find_initiative() {
    local initiative="$1"
    
    if [[ -z "$initiative" ]]; then
        # Find most recent initiative
        if [[ ! -d "initiatives" ]]; then
            echo "Error: initiatives directory not found" >&2
            exit 1
        fi
        initiative=$(ls -t initiatives/ 2>/dev/null | head -n 1)
    fi
    
    if [[ ! -d "initiatives/$initiative" ]]; then
        echo "Error: Initiative not found: $initiative" >&2
        exit 1
    fi
    
    echo "$initiative"
}

# Extract section info from plan
get_section_info() {
    local plan_file="$1"
    local section_name="$2"
    
    # Parse plan.md to extract:
    # - Gate assignment
    # - Dependencies
    # - Status
    
    local in_section=false
    local gate=""
    local deps=""
    local status=""
    
    while IFS= read -r line; do
        if [[ $line =~ ^###[[:space:]]Section.*:[[:space:]]$section_name$ ]]; then
            in_section=true
            continue
        fi
        
        if [[ $in_section == true ]]; then
            if [[ $line =~ ^\*\*Gate\*\*:[[:space:]]*Gate[[:space:]]([0-9]) ]]; then
                gate="${BASH_REMATCH[1]}"
            elif [[ $line =~ ^\*\*Dependencies\*\*:[[:space:]]*(.+)$ ]]; then
                deps="${BASH_REMATCH[1]}"
            elif [[ $line =~ ^\*\*Status\*\*:[[:space:]]*(.+)$ ]]; then
                status="${BASH_REMATCH[1]}"
            elif [[ $line =~ ^### ]]; then
                # Hit next section, stop
                break
            fi
        fi
    done < "$plan_file"
    
    echo "$gate|$deps|$status"
}

# Check if dependencies are satisfied
check_dependencies() {
    local plan_file="$1"
    local deps="$2"
    
    if [[ "$deps" == "None" ]] || [[ -z "$deps" ]]; then
        return 0
    fi
    
    # Parse deps (format: "Section 1, Section 2" or "Section 1")
    IFS=',' read -ra dep_array <<< "$deps"
    
    local failed_deps=()
    
    for dep in "${dep_array[@]}"; do
        dep=$(echo "$dep" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
        
        # Get status of dependency section
        local dep_info=$(get_section_info "$plan_file" "$dep")
        local dep_status=$(echo "$dep_info" | cut -d'|' -f3)
        
        if [[ "$dep_status" != "Passed" ]]; then
            failed_deps+=("$dep (status: $dep_status)")
        fi
    done
    
    if [[ ${#failed_deps[@]} -gt 0 ]]; then
        if [[ $JSON_MODE == true ]]; then
            # Build JSON array of failed dependencies
            local json_failed="["
            for i in "${!failed_deps[@]}"; do
                if [[ $i -gt 0 ]]; then
                    json_failed+=","
                fi
                json_failed+="\"${failed_deps[$i]}\""
            done
            json_failed+="]"
            echo "{\"satisfied\": false, \"failed\": $json_failed}"
        else
            echo "Dependencies not satisfied:"
            for failed in "${failed_deps[@]}"; do
                echo "  - $failed"
            done
        fi
        return 1
    else
        if [[ $JSON_MODE == true ]]; then
            echo "{\"satisfied\": true}"
        else
            echo "All dependencies satisfied"
        fi
        return 0
    fi
}

# Main execution
main() {
    parse_args "$@"
    
    local initiative=$(find_initiative "$INITIATIVE")
    local plan_file="initiatives/$initiative/plan.md"
    
    if [[ ! -f "$plan_file" ]]; then
        echo "Error: Plan file not found: $plan_file" >&2
        exit 1
    fi
    
    if [[ -z "$SECTION" ]]; then
        # No section specified, show all sections
        if [[ $JSON_MODE == true ]]; then
            echo '{"error": "Section name required in JSON mode"}' >&2
            exit 1
        fi
        
        echo "Initiative: $initiative"
        echo "Plan: $plan_file"
        echo ""
        echo "Use --section to check a specific section"
        exit 0
    fi
    
    # Get section info
    local section_info=$(get_section_info "$plan_file" "$SECTION")
    local gate=$(echo "$section_info" | cut -d'|' -f1)
    local deps=$(echo "$section_info" | cut -d'|' -f2)
    local status=$(echo "$section_info" | cut -d'|' -f3)
    
    if [[ -z "$gate" ]]; then
        echo "Error: Section not found in plan: $SECTION" >&2
        exit 1
    fi
    
    # Check dependencies
    check_dependencies "$plan_file" "$deps"
    local deps_ok=$?
    
    if [[ $JSON_MODE == true ]]; then
        echo "{"
        echo "  \"initiative\": \"$initiative\","
        echo "  \"section\": \"$SECTION\","
        echo "  \"gate\": $gate,"
        echo "  \"status\": \"$status\","
        echo "  \"dependencies\": \"$deps\","
        echo "  \"dependencies_satisfied\": $([ $deps_ok -eq 0 ] && echo true || echo false)"
        echo "}"
    else
        echo "Section: $SECTION"
        echo "Gate: $gate"
        echo "Status: $status"
        echo "Dependencies: $deps"
        echo ""
        
        if [[ $deps_ok -eq 0 ]]; then
            echo "✓ Ready to proceed"
        else
            echo "✗ Blocked by dependencies"
        fi
    fi
    
    exit $deps_ok
}

main "$@"
