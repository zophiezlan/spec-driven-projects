# GitHub Agent Implementation Prompt: NUAA-CLI Evolution Phase 1

## Context

You are implementing Phase 1 (Specify & Clarify) of the NUAA-CLI evolution plan. Phase 0 (Mission Constitution) is complete and working.

**Key Documentation Available:**

- `SPEC-KIT-EVOLUTION-PLAN.md` - Complete technical specifications
- `SPEC-KIT-EVOLUTION-SUMMARY.md` - Executive overview
- `SPEC-KIT-QUICK-REFERENCE.md` - Command mappings and quick reference
- `SPEC-KIT-VISUAL-GUIDE.md` - Visual diagrams and workflows

**Phase 0 Completion Status:**

- ✅ Mission constitution system implemented
- ✅ `/nuaa.mission` command working
- ✅ `nuaa mission` CLI commands functional
- ✅ Agent context injection operational
- ✅ Documentation updated

**Important Context:**

- This builds on the mission constitution foundation
- We're creating a specification workflow for NGO programs (not software)
- Users will specify program ideas at a high level
- AI will identify ambiguities and ask clarifying questions
- Goal: Reduce AI guesswork and increase accuracy

## Phase 1 Objective

Implement the Specify → Clarify workflow that allows users to create high-level program specifications with interactive ambiguity resolution before detailed planning begins.

## Your Tasks

### Task 1: Create Specify Command Template

**File:** `nuaa-kit/commands/specify.md`

**Requirements:**

- Create a command template for AI agents to understand
- Command should guide AI to generate a program specification from natural language input
- Specification should include:
  - Program overview (what, why, who benefits)
  - Target population (demographics, needs, location)
  - Duration and timeline
  - Evidence base (research supporting the approach)
  - Key activities (3-5 core activities)
  - Expected outcomes
  - NUAA alignment (how it fits mission/values)
- **Critical**: AI must mark ambiguities with `[NEEDS CLARIFICATION: specific question]` markers
  - Maximum 5 clarification markers allowed
  - Each marker must ask a specific, answerable question
  - Questions should be multiple-choice where possible
- Format should match existing command templates
- Reference the mission constitution automatically

**Reference:**

- Review existing commands in `nuaa-kit/commands/` for format
- See `SPEC-KIT-EVOLUTION-PLAN.md` Section 4, Phase 1 for detailed requirements
- Example specification output is shown in Phase 1 section

### Task 2: Create Program Specification Template

**File:** `nuaa-kit/templates/program-specification-template.md`

**Requirements:**

- Create a markdown template for program specifications
- Include clear section structure:
  - Program Overview
  - Target Population (with placeholder for `[NEEDS CLARIFICATION]`)
  - Duration (with placeholder)
  - Evidence Base (with placeholder)
  - Key Activities
  - Expected Outcomes
  - NUAA Alignment
  - Next Steps
- Use `[PLACEHOLDER]` markers for content to be filled
- Use `[NEEDS CLARIFICATION: question]` markers for ambiguous areas
- Include metadata: Initiative number, created date, status

**Reference:**

- See example in `SPEC-KIT-EVOLUTION-PLAN.md` Section 4, Phase 1
- Review existing templates for formatting consistency

### Task 3: Create Clarify Command Template

**File:** `nuaa-kit/commands/clarify.md`

**Requirements:**

- Create a command template for interactive clarification
- Command should:
  - Find all `[NEEDS CLARIFICATION: ...]` markers in the spec
  - Present each as a numbered question
  - Provide suggested answers (Option A, B, C, Custom)
  - Include context (what section, why it matters)
  - Show implications of each option
  - Wait for user response
  - Update spec with user's answers
  - Remove `[NEEDS CLARIFICATION]` markers
- Format questions as interactive tables (markdown)
- Reference the mission constitution for guidance on defaults

**Reference:**

- See `SPEC-KIT-EVOLUTION-PLAN.md` Section 4, Phase 1 for example interaction
- Review spec-kit clarification workflow from documentation

### Task 4: Create Initiative Management Script (Bash)

**File:** `scripts/bash/create-new-initiative.sh`

**Requirements:**

- Create a script that manages initiative creation (like spec-kit's `create-new-feature.sh`)
- Script should:
  1. Scan `initiatives/` directory for existing initiatives
  2. Determine next initiative number (001, 002, 003, etc.)
  3. Generate slug from description (e.g., "Peer Naloxone" → "peer-naloxone")
  4. Create directory: `initiatives/NNN-slug/`
  5. Copy `program-specification-template.md` to `initiatives/NNN-slug/spec.md`
  6. Populate template with initial content from user description
  7. Set environment variable: `NUAA_INITIATIVE=NNN-slug`
  8. Return JSON with paths and metadata
- Output format: `{"initiative": "001-name", "spec_file": "/path/to/spec.md", "initiative_dir": "/path/"}`
- Handle edge cases (no description, existing initiative, etc.)

**Reference:**

- Review spec-kit's `create-new-feature.sh` for patterns
- See `SPEC-KIT-EVOLUTION-PLAN.md` Section 6.2 for specifications
- Study existing scripts in `scripts/bash/` for style

### Task 5: Create Initiative Management Script (PowerShell)

**File:** `scripts/powershell/create-new-initiative.ps1`

**Requirements:**

- Mirror the bash script functionality in PowerShell
- Same logic and output format as bash version
- Use PowerShell best practices and conventions
- Ensure cross-platform compatibility (Windows, Linux, macOS)
- Handle file paths correctly for Windows

**Reference:**

- Review bash version for logic
- Study existing PowerShell scripts for style
- Ensure JSON output matches exactly

### Task 6: Add CLI Command Support

**File:** `src/nuaa_cli/__init__.py`

**Requirements:**

- Add a new `specify` command to the typer-based CLI
- Command signature: `nuaa specify "Description of program/proposal"`
- Implementation:
  - Call `create-new-initiative.sh` (or `.ps1`) with description
  - Parse JSON output
  - Display success message with initiative number and path
  - Provide guidance on next steps (`nuaa clarify` if markers present)
- Also add a `clarify` command:
  - `nuaa clarify` - Auto-detect active initiative (from env var or last created)
  - `nuaa clarify 001-name` - Specify which initiative to clarify
  - Read spec file, find `[NEEDS CLARIFICATION]` markers
  - Present interactive questions (similar to what AI does)
  - Update spec with answers
- Use rich console for formatted output
- Provide clear error messages

**Reference:**

- Review existing CLI commands for patterns
- See `SPEC-KIT-EVOLUTION-PLAN.md` Section 6.1 for specifications

### Task 7: Update Documentation

**File:** `nuaa-kit/README.md`

**Requirements:**

- Add a new section: "Creating Program Specifications"
- Place after Mission Constitution section
- Explain:
  - What is a program specification
  - How to create one (`/nuaa.specify` or `nuaa specify`)
  - What `[NEEDS CLARIFICATION]` markers mean
  - How to resolve ambiguities (`/nuaa.clarify` or `nuaa clarify`)
  - How specifications feed into planning
- Include example workflow with code blocks
- Use accessible language for NGO staff

**Reference:**

- Review existing README structure
- See `SPEC-KIT-EVOLUTION-SUMMARY.md` for example walkthroughs

### Task 8: Create Clarification Interaction Script (Optional Enhancement)

**File:** `scripts/bash/interactive-clarify.sh` (and PowerShell version)

**Requirements:**

- Optional: Create a helper script for interactive CLI clarification
- Script reads spec file, extracts questions, presents them interactively
- Uses dialog, whiptail, or simple read/echo prompts
- Updates spec file with answers
- Can be called by `nuaa clarify` command

**Reference:**

- Study interactive shell scripting patterns
- Ensure graceful fallback if interactive tools not available

## Acceptance Criteria

Your implementation is complete when:

- [ ] `/nuaa.specify` command works in AI agents and creates `initiatives/NNN-name/spec.md`
- [ ] Spec includes all required sections with proper structure
- [ ] AI automatically marks ambiguities with `[NEEDS CLARIFICATION: question]` (max 5)
- [ ] `/nuaa.clarify` command presents interactive questions to resolve ambiguities
- [ ] User answers update spec and remove markers
- [ ] `nuaa specify "description"` CLI command creates new initiative
- [ ] `nuaa clarify` CLI command resolves ambiguities interactively
- [ ] Initiative numbering is automatic and sequential (001, 002, 003...)
- [ ] Scripts output valid JSON for programmatic use
- [ ] Documentation clearly explains the workflow
- [ ] All existing functionality remains working (backward compatibility)
- [ ] Code follows existing style and conventions

## Implementation Guidelines

### 1. Start with Templates

- Create command and specification templates first
- Test them with an AI agent manually
- Ensure `[NEEDS CLARIFICATION]` system is clear

### 2. Build Scripts Incrementally

- Start with basic initiative creation (numbering, directory)
- Add template copying and population
- Add JSON output last
- Test each piece independently

### 3. CLI Commands Last

- Once scripts work, wrap them in CLI commands
- Focus on error handling and user feedback
- Make error messages actionable

### 4. Test the Full Workflow

- Create a specification with ambiguities
- Run clarify to resolve them
- Verify spec is updated correctly
- Check that it feeds into next phase properly

## Example User Flow to Validate

After implementation, this flow should work:

```bash
# Create a new program specification
nuaa specify "Create a peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney"

# Output:
# ✓ Created initiative 001-naloxone-distribution
# ✓ Specification: initiatives/001-naloxone-distribution/spec.md
# ⚠ Specification has 4 clarification markers - run 'nuaa clarify' to resolve

# View the spec
cat initiatives/001-naloxone-distribution/spec.md
# Should show spec with [NEEDS CLARIFICATION: ...] markers

# Resolve ambiguities
nuaa clarify

# Interactive prompts:
# Q1: Target age range?
#   A) All adults (18+)
#   B) Young adults (18-35)
#   C) No age restriction
# Your choice: A
#
# Q2: Engagement level?
#   A) People in treatment
#   B) Harder-to-reach populations
# Your choice: B
# ... (continues for all questions)

# Output:
# ✓ Updated specification
# ✓ All ambiguities resolved
# → Next: Run 'nuaa plan' to create implementation plan

# Or using AI agent
/nuaa.specify Create a peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney

# AI generates spec with markers

/nuaa.clarify

# AI asks questions interactively
# User answers
# AI updates spec
```

## Technical Implementation Notes

### Initiative Numbering Logic (Bash)

```bash
#!/bin/bash

# Find highest existing initiative number
find_next_number() {
    local initiatives_dir="$REPO_ROOT/initiatives"

    if [[ ! -d "$initiatives_dir" ]]; then
        echo "001"
        return
    fi

    # Find all directories matching NNN-*
    local highest=0
    for dir in "$initiatives_dir"/[0-9][0-9][0-9]-*; do
        if [[ -d "$dir" ]]; then
            local num=$(basename "$dir" | cut -d'-' -f1)
            if [[ "$num" =~ ^[0-9]{3}$ ]] && [[ $num -gt $highest ]]; then
                highest=$num
            fi
        fi
    done

    # Increment and format
    local next=$((10#$highest + 1))
    printf "%03d" $next
}

# Generate slug from description
generate_slug() {
    local description="$1"
    echo "$description" | \
        tr '[:upper:]' '[:lower:]' | \
        sed 's/[^a-z0-9]/-/g' | \
        sed 's/-\+/-/g' | \
        sed 's/^-//' | \
        sed 's/-$//' | \
        cut -c1-50
}

# Main logic
DESCRIPTION="$1"
NUMBER=$(find_next_number)
SLUG=$(generate_slug "$DESCRIPTION")
INITIATIVE="${NUMBER}-${SLUG}"
INITIATIVE_DIR="$REPO_ROOT/initiatives/$INITIATIVE"

# Create directory
mkdir -p "$INITIATIVE_DIR"

# Copy template
cp "$REPO_ROOT/nuaa-kit/templates/program-specification-template.md" \
   "$INITIATIVE_DIR/spec.md"

# Populate template (basic)
sed -i "s/\[INITIATIVE_NUMBER\]/$NUMBER/g" "$INITIATIVE_DIR/spec.md"
sed -i "s/\[INITIATIVE_NAME\]/$SLUG/g" "$INITIATIVE_DIR/spec.md"
sed -i "s/\[CREATED_DATE\]/$(date +%Y-%m-%d)/g" "$INITIATIVE_DIR/spec.md"

# Set environment variable
export NUAA_INITIATIVE="$INITIATIVE"

# Output JSON
cat <<EOF
{
  "initiative": "$INITIATIVE",
  "spec_file": "$INITIATIVE_DIR/spec.md",
  "initiative_dir": "$INITIATIVE_DIR",
  "number": "$NUMBER",
  "slug": "$SLUG"
}
EOF
```

### Clarification Marker System

**In spec.md:**

```markdown
## Target Population

People who use opioids in Western Sydney, particularly those [NEEDS CLARIFICATION: Are we targeting people already engaged with health services, or harder-to-reach populations not in treatment?]

Age range: [NEEDS CLARIFICATION: What specific age range? All adults (18+), young adults (18-35), or no age restriction?]
```

**In clarify command:**

```markdown
## Question 1: Population Engagement Level

**Context**: "Target Population" (spec.md line 12)  
**What we need to know**: Are we targeting people already engaged with health services, or harder-to-reach populations not in treatment?

**Suggested Answers**:
| Option | Answer | Implications |
|--------|--------|--------------|
| A | People in treatment | Easier to reach, existing partnerships, may miss high-risk populations |
| B | Harder-to-reach populations | Higher impact, aligns with NUAA mission, requires street outreach |
| C | Both populations | Broadest reach, more complex logistics, higher budget |
| Custom | Your own answer | [Provide your specific target] |

**Your choice**: \_
```

### CLI Interactive Clarification

```python
@app.command()
def clarify(initiative: Optional[str] = None):
    """Resolve ambiguities in program specification."""
    show_banner()

    # Find initiative
    if not initiative:
        # Auto-detect from env or last created
        initiative = os.getenv("NUAA_INITIATIVE")
        if not initiative:
            console.print("[yellow]No active initiative. Specify one: nuaa clarify 001-name[/yellow]")
            raise typer.Exit(1)

    spec_path = Path(f"initiatives/{initiative}/spec.md")
    if not spec_path.exists():
        console.print(f"[red]Specification not found: {spec_path}[/red]")
        raise typer.Exit(1)

    # Read and parse spec
    content = spec_path.read_text(encoding="utf-8")

    # Find all [NEEDS CLARIFICATION: ...] markers
    import re
    pattern = r'\[NEEDS CLARIFICATION: ([^\]]+)\]'
    matches = list(re.finditer(pattern, content))

    if not matches:
        console.print("[green]✓ No ambiguities to clarify[/green]")
        return

    console.print(f"[yellow]Found {len(matches)} ambiguities to resolve[/yellow]\n")

    # For each marker, ask user
    for i, match in enumerate(matches, 1):
        question = match.group(1)
        console.print(f"[bold]Question {i}:[/bold] {question}")
        answer = typer.prompt("Your answer")

        # Replace marker with answer
        content = content.replace(match.group(0), answer, 1)
        console.print()

    # Write updated spec
    spec_path.write_text(content, encoding="utf-8")
    console.print("[green]✓ Updated specification[/green]")
    console.print("[blue]→ Next: Run 'nuaa plan' to create implementation plan[/blue]")
```

## Questions or Issues?

If you encounter any ambiguities or need clarification:

1. Refer to `SPEC-KIT-EVOLUTION-PLAN.md` Section 4, Phase 1
2. Review spec-kit's clarification system for patterns
3. Check existing code for style conventions
4. Ask for clarification before making assumptions

## Success Metrics

Phase 1 is successful when:

- ✅ Specifications can be created in < 2 minutes
- ✅ AI identifies 3-5 meaningful ambiguities automatically
- ✅ Clarification questions are clear and actionable
- ✅ Spec updates are accurate and complete
- ✅ Initiative numbering is consistent and automatic
- ✅ Documentation is clear to non-technical staff
- ✅ No existing functionality is broken

## Next Steps After Phase 1

Once Phase 1 is complete and tested:

1. Tag the release as `v0.4.0-phase1`
2. Demo the specify→clarify workflow
3. Gather feedback from NUAA staff
4. Begin Phase 2 (Planning & Gates) implementation

---

**Implementation Phase:** Phase 1 - Specify & Clarify  
**Estimated Time:** 1-2 weeks  
**Priority:** High (enables planning workflow)  
**Dependencies:** Phase 0 complete ✓  
**Status:** Ready to start

Good luck! This phase establishes the foundation for high-quality program specifications that feed into all subsequent planning and documentation.
