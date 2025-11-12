#!/usr/bin/env bash

# create-new-initiative.sh
# Creates a new NUAA initiative directory with auto-incrementing number and specification template

set -e

JSON_MODE=false
SHORT_NAME=""
INITIATIVE_NUMBER=""
ARGS=()
i=1

while [ $i -le $# ]; do
    arg="${!i}"
    case "$arg" in
        --json) 
            JSON_MODE=true 
            ;;
        --short-name)
            if [ $((i + 1)) -gt $# ]; then
                echo 'Error: --short-name requires a value' >&2
                exit 1
            fi
            i=$((i + 1))
            next_arg="${!i}"
            if [[ "$next_arg" == --* ]]; then
                echo 'Error: --short-name requires a value' >&2
                exit 1
            fi
            SHORT_NAME="$next_arg"
            ;;
        --number)
            if [ $((i + 1)) -gt $# ]; then
                echo 'Error: --number requires a value' >&2
                exit 1
            fi
            i=$((i + 1))
            next_arg="${!i}"
            if [[ "$next_arg" == --* ]]; then
                echo 'Error: --number requires a value' >&2
                exit 1
            fi
            INITIATIVE_NUMBER="$next_arg"
            ;;
        --help|-h) 
            echo "Usage: $0 [--json] [--short-name <name>] [--number N] <initiative_description>"
            echo ""
            echo "Options:"
            echo "  --json              Output in JSON format"
            echo "  --short-name <name> Provide a custom short name (2-4 words) for the initiative"
            echo "  --number N          Specify initiative number manually (overrides auto-detection)"
            echo "  --help, -h          Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0 'Peer-led naloxone distribution program' --short-name 'naloxone-distribution'"
            echo "  $0 'Mobile harm reduction van for regional NSW' --number 5"
            exit 0
            ;;
        *) 
            ARGS+=("$arg") 
            ;;
    esac
    i=$((i + 1))
done

DESCRIPTION="${ARGS[*]}"
if [ -z "$DESCRIPTION" ]; then
    echo "Usage: $0 [--json] [--short-name <name>] [--number N] <initiative_description>" >&2
    exit 1
fi

# Function to find the repository root
find_repo_root() {
    local dir="$1"
    while [ "$dir" != "/" ]; do
        if [ -d "$dir/.git" ] || [ -d "$dir/.nuaa" ] || [ -d "$dir/nuaa-kit" ]; then
            echo "$dir"
            return 0
        fi
        dir="$(dirname "$dir")"
    done
    return 1
}

# Function to get highest initiative number from initiatives directory
get_highest_from_initiatives() {
    local initiatives_dir="$1"
    local highest=0
    
    if [ -d "$initiatives_dir" ]; then
        for dir in "$initiatives_dir"/*; do
            [ -d "$dir" ] || continue
            dirname=$(basename "$dir")
            # Extract number from pattern NNN-*
            if [[ "$dirname" =~ ^([0-9]{3})- ]]; then
                number="${BASH_REMATCH[1]}"
                number=$((10#$number))
                if [ "$number" -gt "$highest" ]; then
                    highest=$number
                fi
            fi
        done
    fi
    
    echo "$highest"
}

# Function to clean and format an initiative slug
clean_slug() {
    local name="$1"
    echo "$name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/-\+/-/g' | sed 's/^-//' | sed 's/-$//'
}

# Function to generate slug from description with stop word filtering
generate_slug() {
    local description="$1"
    
    # Common stop words to filter out
    local stop_words="^(i|a|an|the|to|for|of|in|on|at|by|with|from|is|are|was|were|be|been|being|have|has|had|do|does|did|will|would|should|could|can|may|might|must|shall|this|that|these|those|my|your|our|their|want|need|add|get|set)$"
    
    # Convert to lowercase and split into words
    local clean_name=$(echo "$description" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/ /g')
    
    # Filter words: remove stop words and words shorter than 3 chars
    local meaningful_words=()
    for word in $clean_name; do
        [ -z "$word" ] && continue
        
        # Keep words that are NOT stop words AND length >= 3
        if ! echo "$word" | grep -qiE "$stop_words"; then
            if [ ${#word} -ge 3 ]; then
                meaningful_words+=("$word")
            fi
        fi
    done
    
    # Use first 3-4 meaningful words
    if [ ${#meaningful_words[@]} -gt 0 ]; then
        local max_words=3
        if [ ${#meaningful_words[@]} -eq 4 ]; then max_words=4; fi
        
        local result=""
        local count=0
        for word in "${meaningful_words[@]}"; do
            if [ $count -ge $max_words ]; then break; fi
            if [ -n "$result" ]; then result="$result-"; fi
            result="$result$word"
            count=$((count + 1))
        done
        echo "$result"
    else
        # Fallback: use original logic
        local cleaned=$(clean_slug "$description")
        echo "$cleaned" | tr '-' '\n' | grep -v '^$' | head -3 | tr '\n' '-' | sed 's/-$//'
    fi
}

# Resolve repository root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if git rev-parse --show-toplevel >/dev/null 2>&1; then
    REPO_ROOT=$(git rev-parse --show-toplevel)
else
    REPO_ROOT="$(find_repo_root "$SCRIPT_DIR")"
    if [ -z "$REPO_ROOT" ]; then
        echo "Error: Could not determine repository root. Please run this script from within the repository." >&2
        exit 1
    fi
fi

cd "$REPO_ROOT"

INITIATIVES_DIR="$REPO_ROOT/initiatives"
mkdir -p "$INITIATIVES_DIR"

# Generate slug
if [ -n "$SHORT_NAME" ]; then
    SLUG=$(clean_slug "$SHORT_NAME")
else
    SLUG=$(generate_slug "$DESCRIPTION")
fi

# Determine initiative number
if [ -z "$INITIATIVE_NUMBER" ]; then
    HIGHEST=$(get_highest_from_initiatives "$INITIATIVES_DIR")
    INITIATIVE_NUMBER=$((HIGHEST + 1))
fi

INITIATIVE_NUM=$(printf "%03d" "$INITIATIVE_NUMBER")
INITIATIVE_NAME="${INITIATIVE_NUM}-${SLUG}"

# Validate length (GitHub has a 255-byte limit for filenames)
MAX_NAME_LENGTH=100  # Conservative limit for directory names
if [ ${#INITIATIVE_NAME} -gt $MAX_NAME_LENGTH ]; then
    # Truncate slug
    MAX_SLUG_LENGTH=$((MAX_NAME_LENGTH - 4))  # Account for NNN-
    TRUNCATED_SLUG=$(echo "$SLUG" | cut -c1-$MAX_SLUG_LENGTH | sed 's/-$//')
    
    ORIGINAL_NAME="$INITIATIVE_NAME"
    INITIATIVE_NAME="${INITIATIVE_NUM}-${TRUNCATED_SLUG}"
    SLUG="$TRUNCATED_SLUG"
    
    if [ "$JSON_MODE" = false ]; then
        >&2 echo "[nuaa] Warning: Initiative name exceeded length limit"
        >&2 echo "[nuaa] Original: $ORIGINAL_NAME (${#ORIGINAL_NAME} chars)"
        >&2 echo "[nuaa] Truncated to: $INITIATIVE_NAME (${#INITIATIVE_NAME} chars)"
    fi
fi

INITIATIVE_DIR="$INITIATIVES_DIR/$INITIATIVE_NAME"

# Check if directory already exists
if [ -d "$INITIATIVE_DIR" ]; then
    echo "Error: Initiative directory already exists: $INITIATIVE_DIR" >&2
    exit 1
fi

# Create directory
mkdir -p "$INITIATIVE_DIR"

# Copy template
TEMPLATE_PATH="$REPO_ROOT/nuaa-kit/templates/program-specification-template.md"
SPEC_FILE="$INITIATIVE_DIR/spec.md"

if [ ! -f "$TEMPLATE_PATH" ]; then
    echo "Error: Template not found at $TEMPLATE_PATH" >&2
    echo "Please ensure you're running this script from a NUAA project." >&2
    exit 1
fi

cp "$TEMPLATE_PATH" "$SPEC_FILE"

# Populate template with metadata
CREATED_DATE=$(date +%Y-%m-%d)

# Use a more robust sed approach that works on both macOS and Linux
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s/\[INITIATIVE_NUMBER\]/${INITIATIVE_NUM}/g" "$SPEC_FILE"
    sed -i '' "s/\[INITIATIVE_SLUG\]/${SLUG}/g" "$SPEC_FILE"
    sed -i '' "s/\[CREATED_DATE\]/${CREATED_DATE}/g" "$SPEC_FILE"
    sed -i '' "s/\[PROGRAM_NAME\]/${DESCRIPTION}/g" "$SPEC_FILE"
else
    # Linux
    sed -i "s/\[INITIATIVE_NUMBER\]/${INITIATIVE_NUM}/g" "$SPEC_FILE"
    sed -i "s/\[INITIATIVE_SLUG\]/${SLUG}/g" "$SPEC_FILE"
    sed -i "s/\[CREATED_DATE\]/${CREATED_DATE}/g" "$SPEC_FILE"
    sed -i "s/\[PROGRAM_NAME\]/${DESCRIPTION}/g" "$SPEC_FILE"
fi

# Set environment variable for the current session
export NUAA_INITIATIVE="$INITIATIVE_NAME"

# Output JSON or human-readable format
if $JSON_MODE; then
    cat <<EOF
{
  "initiative": "$INITIATIVE_NAME",
  "spec_file": "$SPEC_FILE",
  "initiative_dir": "$INITIATIVE_DIR",
  "number": "$INITIATIVE_NUM",
  "slug": "$SLUG"
}
EOF
else
    echo "INITIATIVE: $INITIATIVE_NAME"
    echo "SPEC_FILE: $SPEC_FILE"
    echo "INITIATIVE_DIR: $INITIATIVE_DIR"
    echo "NUMBER: $INITIATIVE_NUM"
    echo "SLUG: $SLUG"
    echo "NUAA_INITIATIVE environment variable set to: $INITIATIVE_NAME"
fi
