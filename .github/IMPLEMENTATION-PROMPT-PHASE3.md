# NUAA CLI Evolution - Phase 3 Implementation Prompt

## Phase 3: Section-by-Section Drafting System

**Duration**: 3 weeks  
**Prerequisites**: Phase 2 complete (planning & gate validation operational)  
**Objective**: Implement interactive AI-assisted section drafting with context awareness

---

## Context & Foundation

You are implementing Phase 3 of the NUAA CLI evolution based on GitHub's spec-kit methodology. This phase introduces:

1. **Section Drafting Workflow**: AI-assisted content creation for individual sections
2. **Context Injection**: Automatic loading of related sections and mission constitution
3. **Placeholder Management**: Smart handling of missing information with resolution tracking
4. **Draft Iterations**: Support for revisions based on feedback and new information
5. **Progress Integration**: Automatic status updates in the plan

### Domain Translation Reminder

| Software (spec-kit) | NGO (NUAA)                     |
| ------------------- | ------------------------------ |
| Code Task           | Section Draft                  |
| Task Context        | Section Dependencies + Mission |
| Implementation      | Drafting Content               |
| Code Review         | Section Gate Validation        |
| Revision            | Draft Iteration                |

---

## Phase 3 Tasks

### Task 1: Create Section Template

**File**: `nuaa-kit/templates/section-template.md`

**Purpose**: Template structure for all section drafts

**Structure**:

```markdown
# [SECTION_NAME]

**Initiative**: [INITIATIVE_NUMBER]-[SLUG]  
**Gate**: Gate [N] - [Gate Name]  
**Status**: Draft  
**Last Updated**: [DATE]

---

## Section Purpose

[Clear statement of why this section exists and what it accomplishes in 1-2 sentences]

---

## Content

[Main content of the section goes here]

[For proposals, program designs, reports, etc.]

[Multiple paragraphs as needed]

---

## References

[If applicable - citations, sources, evidence]

---

## Notes for Reviewers

[Optional - areas needing particular attention, questions for review, known limitations]

---

## Revision History

- **[DATE]**: Initial draft created
- **[DATE]**: [Description of changes made]
```

**Key Design Elements**:

- Clear metadata (initiative, gate, status)
- Section purpose explicitly stated
- Main content area clearly demarcated
- References section for evidence tracking
- Reviewer notes for collaboration
- Revision history for tracking iterations

---

### Task 2: Create Draft Command Template

**File**: `nuaa-kit/commands/draft.md`

**Purpose**: AI agent command for drafting sections with full context

**Content Structure**:

````markdown
---
description: "Draft a document section with context awareness"
---

# /nuaa.draft - Section Drafting Command

Template: See [section-template.md](../templates/section-template.md).

## Description

Draft a document section using the program specification, document plan, mission constitution, and related sections as context. This command creates well-structured, evidence-based content that aligns with NUAA principles and meets the section's gate requirements.

---

## Purpose

Section Drafting:

- Creates content that fulfills the section's purpose from the plan
- Incorporates context from related sections and dependencies
- Aligns with mission constitution principles
- Meets the quality criteria for the section's assigned gate
- Uses appropriate tone and language for the document type
- Cites evidence and provides justifications

---

## Usage

```bash
/nuaa.draft [SECTION_NAME] [--initiative INITIATIVE]
```
````

**Examples**:

- `/nuaa.draft "Program Description"` - Draft Program Description in active initiative
- `/nuaa.draft "Budget Justification" --initiative 001-naloxone-distribution`
- `/nuaa.draft "Executive Summary"` - Draft the Executive Summary

---

## How It Works

### Step 1: Load Planning Context

The AI will:

1. Identify the initiative (from argument or most recent)
2. Read `initiatives/NNN-slug/plan.md` to find the section
3. Extract:
   - Section purpose
   - Content requirements (bullet points)
   - Gate assignment
   - Quality criteria
   - Dependencies
   - Estimated length

### Step 2: Load Related Context

The AI will read and incorporate:

**Always Load**:

- `initiatives/NNN-slug/spec.md` - Program specification
- `memory/constitution.md` - Mission constitution for alignment

**Dependency Sections** (if they exist):

- For each dependency in the plan, read `initiatives/NNN-slug/sections/[dependency].md`
- Extract key information referenced by this section
- Note any data, dates, or facts that must be consistent

**Related Sections** (if they exist):

- Sections in the same gate level
- Sections that reference similar content
- Earlier sections that establish context

### Step 3: Draft Content

The AI will create content that:

**Meets Section Purpose**:

- Addresses the purpose statement from the plan
- Covers all content requirements (bullets)
- Stays within estimated length (±20%)

**Incorporates Context**:

- References information from dependency sections
- Maintains consistency with earlier sections
- Uses the same terminology and definitions
- Avoids contradictions or redundancy

**Aligns with Mission**:

- Uses harm reduction language appropriately
- Acknowledges lived experience where relevant
- Follows evidence-based practice principles
- Promotes self-determination and anti-stigma approaches

**Meets Gate Standards**:

- For Gate 1: Clear purpose, structured outline, key points identified
- For Gate 2: Complete information, evidence citations, mission alignment
- For Gate 3: Strong evidence base, proper citations, logical reasoning
- For Gate 4: Integration with earlier sections, consistency, coherence
- For Gate 5: Professional polish, formatting, completeness

### Step 4: Handle Missing Information

If the AI cannot complete a section due to missing information:

**Use Placeholder Markers**:

```markdown
[PLACEHOLDER: Information needed - specific question]
```

**Examples**:

- `[PLACEHOLDER: What is the exact geographic coverage area?]`
- `[PLACEHOLDER: Confirmed budget allocation for peer educator training?]`
- `[PLACEHOLDER: Citation needed for naloxone effectiveness in community settings]`

**Document Placeholders**:
The AI will list all placeholders at the end of the draft:

```markdown
## Placeholders to Resolve

1. **Line 45**: [PLACEHOLDER: Geographic coverage]

   - Context: Target population section
   - Question: What is the exact geographic coverage area?
   - Impact: Affects participant estimates and distribution strategy

2. **Line 78**: [PLACEHOLDER: Budget allocation]
   - Context: Training program description
   - Question: Confirmed budget allocation for peer educator training?
   - Impact: Determines number of educators we can train
```

### Step 5: Save and Update Status

The AI will:

1. Create `initiatives/NNN-slug/sections/[section-name].md` using the template
2. Suggest updating plan.md status to "Draft Complete"
3. List any placeholders that need resolution
4. Recommend next steps (validate with gate-check or draft next section)

---

## Content Guidelines by Document Type

### Proposals

**Tone**: Persuasive, professional, mission-aligned  
**Focus**: Demonstrating need, justifying budget, showing capability  
**Evidence**: Strong citations, data-driven, community-centered  
**Length**: Detailed but concise (funding bodies have limited time)

**Key Sections**:

- Executive Summary (compelling 1-page overview)
- Needs Statement (data showing the problem)
- Program Description (clear methodology)
- Budget Justification (every dollar explained)
- Evaluation Plan (measurable outcomes)

### Program Designs

**Tone**: Operational, detailed, implementable  
**Focus**: How things will actually work on the ground  
**Evidence**: Best practices, implementation research, pilot data  
**Length**: Comprehensive and thorough (internal use)

**Key Sections**:

- Service Model (step-by-step processes)
- Staffing Structure (roles, responsibilities, FTE)
- Workflows (who does what when)
- Quality Assurance (how we ensure good practice)
- Risk Mitigation (what could go wrong and how we prevent it)

### Evaluation Reports

**Tone**: Analytical, objective, data-focused  
**Focus**: What happened, what was learned, what changes  
**Evidence**: Program data, participant feedback, outcome measures  
**Length**: Data-rich with narrative context

**Key Sections**:

- Methodology (how data was collected)
- Findings (what the data shows)
- Analysis (what the findings mean)
- Recommendations (what should change)
- Limitations (what we couldn't measure)

### Impact Reports

**Tone**: Storytelling, compelling, achievement-focused  
**Focus**: Community outcomes, lives changed, broader impact  
**Evidence**: Quantitative + qualitative, stories + statistics  
**Length**: Accessible narrative with supporting data

**Key Sections**:

- Program Overview (what we did)
- Outcomes Achieved (numbers that matter)
- Participant Stories (lived experience voices)
- Community Impact (ripple effects)
- Lessons Learned (what worked, what didn't)

---

## Context Injection Examples

### Example 1: Budget Justification (Gate 3)

**Dependencies**: Program Description, Staffing Model

**Context Loaded**:

- From Program Description: "20 peer educators will conduct 2 training sessions per week"
- From Staffing Model: "Each peer educator works 15 hours/week at $35/hour"

**AI Uses Context**:

```markdown
## Peer Educator Costs

The program requires 20 peer educators working 15 hours per week each
(as detailed in the Staffing Model section). At the community-standard
rate of $35/hour for credentialed peer workers, this represents:

- Weekly cost: 20 educators × 15 hours × $35 = $10,500
- Annual cost (48 weeks): $504,000

This staffing level enables the delivery of 40 training sessions per week
(20 educators × 2 sessions each), sufficient to reach our target of 2,000
participants annually (see Program Description).
```

**Note How AI**:

- References specific numbers from dependencies
- Maintains consistency (20 educators, 15 hours, $35/hour)
- Shows calculations transparently
- Links back to program goals

### Example 2: Evaluation Framework (Gate 3)

**Dependencies**: Program Description, Expected Outcomes

**Mission Context**: Evidence-based practice, lived experience

**Context Loaded**:

- From Expected Outcomes: "Reduce overdose mortality by 25% in target area"
- From Expected Outcomes: "Increase naloxone carriage by peer network"
- From Mission: "Lived experience must inform all evaluation"

**AI Uses Context**:

```markdown
## Outcome Measurement

### Primary Outcome: Overdose Mortality Reduction

We will measure changes in overdose mortality rates in the target area
compared to baseline, with a goal of 25% reduction (as specified in
Expected Outcomes). Data will be obtained through:

- NSW Ambulance Service fatal overdose reports
- Coroner's data (with appropriate approvals)
- Hospital emergency department presentations

### Process Outcome: Naloxone Distribution

We will track naloxone carriage rates within peer networks through:

- Anonymous surveys with people who use drugs (every 6 months)
- Peer educator distribution logs
- Pharmacy refill data (aggregated, de-identified)

### Lived Experience in Evaluation

Following our mission commitment to lived experience leadership, the
evaluation framework was co-designed with people who use drugs. Our
Peer Advisory Committee will:

- Review all survey instruments for appropriateness
- Conduct peer-to-peer data collection (reducing stigma)
- Participate in data analysis and interpretation
- Co-author the evaluation report
```

**Note How AI**:

- Directly references the 25% goal from dependencies
- Addresses both outcomes mentioned in the plan
- Incorporates mission constitution principle
- Provides concrete methods

---

## Placeholder Resolution Workflow

When a draft has placeholders:

### Step 1: Document Placeholders

AI creates a placeholder summary:

```markdown
## Placeholders to Resolve

This draft has 3 placeholders requiring additional information:

1. **Geographic Coverage** (Line 45)

   - Question: Exact geographic area (LGAs, suburbs, postcodes)?
   - Why needed: Affects participant estimates and service planning
   - Who can answer: Program Manager or Funding Body

2. **Budget Amount** (Line 78)

   - Question: Final confirmed budget allocation for training?
   - Why needed: Determines trainer capacity and session frequency
   - Who can answer: Finance Team or Funding Body

3. **Partnership Status** (Line 120)
   - Question: Has MOU with NSW Health been signed?
   - Why needed: Affects service delivery model and data sharing
   - Who can answer: Executive Director
```

### Step 2: User Resolves Placeholders

User gathers missing information through:

- Consulting with team members
- Checking with funding bodies
- Reviewing existing documents
- Making program design decisions

### Step 3: AI Updates Draft

```bash
/nuaa.draft "Program Description" --resolve
```

The AI:

1. Reads the current draft
2. Identifies all `[PLACEHOLDER: ...]` markers
3. Asks user for each piece of information
4. Updates the draft with resolved information
5. Removes placeholder markers
6. Updates revision history

---

## Draft Iteration Support

Drafts often need multiple iterations:

### Iteration Types

**Type 1: Placeholder Resolution**

- Original draft had missing information
- User provides missing details
- AI updates specific sections

**Type 2: Feedback Incorporation**

- Section failed gate validation
- AI revises based on feedback
- Addresses specific failing criteria

**Type 3: New Information**

- Specification or plan updated
- Earlier sections revised
- AI updates to maintain consistency

**Type 4: Quality Enhancement**

- Section passed but could be stronger
- AI improves evidence, clarity, or alignment
- Voluntary improvement iteration

### Revision Command

````markdown
---
description: "Revise a drafted section based on feedback or new information"
---

# /nuaa.revise - Section Revision Command

## Usage

```bash
/nuaa.revise [SECTION_NAME] [--type TYPE] [--feedback "..."]
```
````

**Examples**:

- `/nuaa.revise "Program Description" --type placeholder` - Resolve placeholders
- `/nuaa.revise "Budget" --type feedback --feedback "Need more detail on equipment costs"`
- `/nuaa.revise "Evaluation" --type consistency` - Update based on changed dependencies

## How It Works

The AI will:

1. Read the current draft
2. Based on revision type:
   - **placeholder**: Ask for missing information
   - **feedback**: Address specific feedback points
   - **consistency**: Re-read dependencies and align
   - **enhancement**: Strengthen evidence and clarity
3. Make targeted revisions (not full rewrite)
4. Update revision history
5. Suggest re-validation with gate-check

````

---

### Task 3: Create Draft Management Script (Bash)

**File**: `scripts/bash/create-section-draft.sh`

**Purpose**: Create section file structure and track drafting progress

**Key Functions**:

```bash
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
        initiative=$(ls -t initiatives/ 2>/dev/null | head -n 1)
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

    # Extract gate and purpose from plan (simplified - real implementation more robust)
    local gate=$(grep -A 5 "^### .*: $section$" "$plan_file" | grep "^\*\*Gate\*\*:" | sed 's/.*Gate \([0-9]\).*/\1/')
    local purpose=$(grep -A 10 "^### .*: $section$" "$plan_file" | grep "^\*\*Purpose\*\*:" | sed 's/^\*\*Purpose\*\*: //')

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
    # This is a simplified version - real implementation would be more robust

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
            # Hit next section without finding status
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
````

**Key Features**:

- Creates sections directory structure
- Generates section file from template
- Updates plan.md status automatically
- Supports JSON output for CLI integration
- Handles errors gracefully

---

### Task 4: Create Draft Management Script (PowerShell)

**File**: `scripts/powershell/create-section-draft.ps1`

**Purpose**: PowerShell mirror of bash draft creation script

**Key Functions**:

```powershell
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

    # Convert section name to filename
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

    # Extract gate number (simplified)
    if ($planContent -match "### .*?: $sectionName(?:.|\n)*?\*\*Gate\*\*:\s*Gate\s+(\d)") {
        $gate = $Matches[1]
    } else {
        $gate = "?"
    }

    # Extract purpose (simplified)
    if ($planContent -match "### .*?: $sectionName(?:.|\n)*?\*\*Purpose\*\*:\s*([^\n]+)") {
        $purpose = $Matches[1]
    } else {
        $purpose = "[Purpose not found in plan]"
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

    $content = Get-Content $planFile -Raw

    # Find section and update status (simplified regex)
    $pattern = "(### .*?: $sectionName(?:.|\n)*?\*\*Status\*\*:\s*)[^\n]+"
    $replacement = "`${1}$newStatus"

    $content = $content -replace $pattern, $replacement

    Set-Content -Path $planFile -Value $content -NoNewline
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
```

---

### Task 5: Integrate Drafting into CLI

**File**: `src/nuaa_cli/__init__.py`

**Add new commands**:

```python
@app.command()
def draft(
    section: str = typer.Argument(..., help="Section name to draft (e.g., 'Program Description')"),
    initiative: Optional[str] = typer.Option(None, "--initiative", help="Initiative to draft in (uses most recent if not specified)"),
    resolve: bool = typer.Option(False, "--resolve", help="Resolve placeholders in existing draft"),
):
    """Draft a document section with AI assistance."""
    show_banner()

    # Determine initiative
    if initiative is None:
        initiatives_dir = Path("initiatives")
        if not initiatives_dir.exists():
            console.print("[red]Error: No initiatives directory found[/red]")
            raise typer.Exit(1)

        initiatives = sorted(initiatives_dir.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)
        if not initiatives:
            console.print("[red]Error: No initiatives found[/red]")
            raise typer.Exit(1)

        initiative = initiatives[0].name

    # Check plan exists
    plan_file = Path(f"initiatives/{initiative}/plan.md")
    if not plan_file.exists():
        console.print(f"[red]Error: Plan not found: {plan_file}[/red]")
        console.print("[yellow]Run 'nuaa plan' first to create a document plan[/yellow]")
        raise typer.Exit(1)

    # Check if section exists in plan
    plan_content = plan_file.read_text()
    if section not in plan_content:
        console.print(f"[red]Error: Section '{section}' not found in plan[/red]")
        console.print(f"[yellow]Check section names in {plan_file}[/yellow]")
        raise typer.Exit(1)

    # Check if we're resolving an existing draft
    section_filename = section.lower().replace(' ', '-')
    section_file = Path(f"initiatives/{initiative}/sections/{section_filename}.md")

    if resolve:
        if not section_file.exists():
            console.print(f"[red]Error: Section draft not found: {section_file}[/red]")
            console.print("[yellow]Use without --resolve to create initial draft[/yellow]")
            raise typer.Exit(1)

        # Check for placeholders
        section_content = section_file.read_text()
        placeholder_count = section_content.count('[PLACEHOLDER:')

        if placeholder_count == 0:
            console.print("[yellow]No placeholders found in section[/yellow]")
            console.print(f"[yellow]Section appears complete: {section_file}[/yellow]")
            raise typer.Exit(0)

        console.print(Panel(
            f"[green]✓[/green] Section: [cyan]{section}[/cyan]\n"
            f"[green]✓[/green] File: [cyan]{section_file}[/cyan]\n"
            f"[yellow]⚠[/yellow] Placeholders: [yellow]{placeholder_count}[/yellow]\n\n"
            f"[bold]AI will:[/bold]\n"
            f"  • Identify all placeholder markers\n"
            f"  • Ask for missing information\n"
            f"  • Update the draft with resolved content\n"
            f"  • Remove placeholder markers\n\n"
            f"[bold]Have AI run:[/bold] [cyan]/nuaa.draft \"{section}\" --resolve[/cyan]",
            title="Resolve Placeholders",
            border_style="yellow"
        ))
        return

    # Creating new draft
    if section_file.exists():
        console.print(f"[yellow]Warning: Section draft already exists: {section_file}[/yellow]")
        if not typer.confirm("Overwrite existing draft?"):
            raise typer.Exit(0)

    # Call create-section-draft script
    script_path = Path("scripts/bash/create-section-draft.sh")
    if sys.platform == "win32":
        script_path = Path("scripts/powershell/create-section-draft.ps1")

    if not script_path.exists():
        console.print(f"[red]Error: Script not found: {script_path}[/red]")
        raise typer.Exit(1)

    # Build command
    cmd_args = ["--json", "--initiative", initiative, "--section", section]

    try:
        if sys.platform == "win32":
            result = subprocess.run(
                ["pwsh", "-File", str(script_path)] + cmd_args,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=Path.cwd()
            )
        else:
            result = subprocess.run(
                ["bash", str(script_path)] + cmd_args,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=Path.cwd()
            )

        if result.returncode != 0:
            console.print(f"[red]Error:[/red]")
            console.print(result.stderr)
            raise typer.Exit(1)

        data = json.loads(result.stdout)

        console.print(Panel(
            f"[green]✓[/green] Initiative: [cyan]{data['initiative']}[/cyan]\n"
            f"[green]✓[/green] Section: [cyan]{data['section']}[/cyan]\n"
            f"[green]✓[/green] File: [cyan]{data['section_file']}[/cyan]\n"
            f"[green]✓[/green] Plan updated: In Progress\n\n"
            f"[bold]AI will create:[/bold]\n"
            f"  • Load specification and dependencies\n"
            f"  • Load mission constitution for alignment\n"
            f"  • Draft content meeting gate criteria\n"
            f"  • Use [PLACEHOLDER] for missing info\n"
            f"  • Save to {data['section_file']}\n\n"
            f"[bold]Next steps:[/bold]\n"
            f"  1. Have AI draft with [cyan]/nuaa.draft \"{section}\"[/cyan]\n"
            f"  2. Review and resolve any placeholders\n"
            f"  3. Validate with [cyan]nuaa gate-check \"{section}\"[/cyan]",
            title="Ready to Draft",
            border_style="green"
        ))

    except json.JSONDecodeError:
        console.print(f"[red]Error: Could not parse script output[/red]")
        console.print(result.stdout)
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def revise(
    section: str = typer.Argument(..., help="Section name to revise"),
    initiative: Optional[str] = typer.Option(None, "--initiative", help="Initiative (uses most recent if not specified)"),
    revision_type: str = typer.Option("feedback", "--type", help="Revision type: placeholder, feedback, consistency, enhancement"),
    feedback: Optional[str] = typer.Option(None, "--feedback", help="Specific feedback to address"),
):
    """Revise a drafted section based on feedback or new information."""
    show_banner()

    # Determine initiative
    if initiative is None:
        initiatives_dir = Path("initiatives")
        if not initiatives_dir.exists():
            console.print("[red]Error: No initiatives directory found[/red]")
            raise typer.Exit(1)

        initiatives = sorted(initiatives_dir.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True)
        if not initiatives:
            console.print("[red]Error: No initiatives found[/red]")
            raise typer.Exit(1)

        initiative = initiatives[0].name

    # Check section exists
    section_filename = section.lower().replace(' ', '-')
    section_file = Path(f"initiatives/{initiative}/sections/{section_filename}.md")

    if not section_file.exists():
        console.print(f"[red]Error: Section not found: {section_file}[/red]")
        console.print("[yellow]Use 'nuaa draft' to create initial draft first[/yellow]")
        raise typer.Exit(1)

    # Validate revision type
    valid_types = ["placeholder", "feedback", "consistency", "enhancement"]
    if revision_type not in valid_types:
        console.print(f"[red]Error: Invalid revision type: {revision_type}[/red]")
        console.print(f"[yellow]Valid types: {', '.join(valid_types)}[/yellow]")
        raise typer.Exit(1)

    # Check for feedback if type is feedback
    if revision_type == "feedback" and not feedback:
        console.print("[yellow]Warning: No feedback provided for feedback revision[/yellow]")
        console.print("[yellow]Consider using --feedback \"your specific feedback\"[/yellow]")

    console.print(Panel(
        f"[green]✓[/green] Section: [cyan]{section}[/cyan]\n"
        f"[green]✓[/green] File: [cyan]{section_file}[/cyan]\n"
        f"[green]✓[/green] Revision type: [cyan]{revision_type}[/cyan]\n" +
        (f"[green]✓[/green] Feedback: [cyan]{feedback}[/cyan]\n" if feedback else "") +
        f"\n[bold]AI will:[/bold]\n" +
        (f"  • Resolve placeholder markers\n" if revision_type == "placeholder" else "") +
        (f"  • Address specific feedback points\n" if revision_type == "feedback" else "") +
        (f"  • Re-read dependencies and align content\n" if revision_type == "consistency" else "") +
        (f"  • Strengthen evidence and clarity\n" if revision_type == "enhancement" else "") +
        f"  • Update revision history\n"
        f"  • Maintain existing content structure\n\n"
        f"[bold]Have AI run:[/bold] [cyan]/nuaa.revise \"{section}\" --type {revision_type}" +
        (f" --feedback \"{feedback}\"" if feedback else "") + "[/cyan]",
        title="Ready to Revise",
        border_style="blue"
    ))
```

---

### Task 6: Update Documentation

**Files to Update**:

1. **nuaa-kit/README.md** - Add Phase 3 workflow section:

````markdown
### The Draft → Validate → Revise Workflow

After creating your document plan, work through sections systematically:

#### 1. Draft a Section

**CLI**:

```bash
nuaa draft "Program Description"
```
````

**AI Agent**:

```
/nuaa.draft "Program Description"
```

The AI will:

- Load specification, plan, and dependencies
- Incorporate mission constitution principles
- Create content meeting gate criteria
- Use `[PLACEHOLDER]` markers for missing info
- Save to `initiatives/NNN-slug/sections/program-description.md`

#### 2. Review the Draft

Check the draft for:

- **Content completeness**: All requirements from plan addressed?
- **Placeholders**: Any `[PLACEHOLDER: ...]` markers that need resolution?
- **Evidence**: Are claims supported with citations?
- **Mission alignment**: Harm reduction language, lived experience acknowledged?

#### 3. Resolve Placeholders (if needed)

If the draft has placeholders:

```bash
nuaa draft "Program Description" --resolve
```

The AI will ask for each missing piece of information and update the draft.

#### 4. Validate with Gate Check

```bash
nuaa gate-check "Program Description"
```

The AI validates against all gate criteria and provides specific feedback.

#### 5. Revise Based on Feedback (if needed)

If the section fails validation:

**CLI**:

```bash
nuaa revise "Program Description" --type feedback --feedback "Need more detail on training methodology"
```

**AI Agent**:

```
/nuaa.revise "Program Description" --type feedback --feedback "Need more detail on training methodology"
```

Revision types:

- **placeholder**: Resolve missing information
- **feedback**: Address specific gate validation feedback
- **consistency**: Update based on changed dependencies
- **enhancement**: Strengthen evidence or clarity

#### 6. Mark Section Complete

After passing gate validation, update the plan:

1. Open `initiatives/NNN-slug/plan.md`
2. Find the section in the progress tracker
3. Change status from "In Progress" to "Passed"
4. Move to next section

#### Context Awareness

The AI automatically loads:

- **Specification**: Full program details
- **Mission Constitution**: Ethical principles and standards
- **Dependencies**: Earlier sections this section builds on
- **Related Sections**: Sections at same gate level

This ensures:

- Consistency across the document
- Mission alignment throughout
- No contradictions or redundancy
- Appropriate cross-referencing

````

2. **CHANGELOG.md** - Add Phase 3 entries

3. **Update version in pyproject.toml** if warranted

---

## Acceptance Criteria

Phase 3 is complete when:

### Templates & Commands

- [ ] `nuaa-kit/templates/section-template.md` exists with proper structure
- [ ] `nuaa-kit/commands/draft.md` exists with context loading logic
- [ ] `nuaa-kit/commands/draft.md` documents placeholder handling
- [ ] `nuaa-kit/commands/draft.md` includes content guidelines by document type
- [ ] Draft command explains revision workflow

### Scripts

- [ ] `scripts/bash/create-section-draft.sh` creates section files from template
- [ ] `scripts/bash/create-section-draft.sh` updates plan.md status
- [ ] `scripts/powershell/create-section-draft.ps1` mirrors bash functionality
- [ ] Both scripts support `--json` flag
- [ ] Scripts handle existing files gracefully

### CLI Integration

- [ ] `nuaa draft [SECTION]` command exists
- [ ] `nuaa draft [SECTION] --resolve` handles placeholders
- [ ] `nuaa revise [SECTION]` command exists with revision types
- [ ] All commands provide clear next-step guidance
- [ ] Commands update `pyproject.toml` version and `CHANGELOG.md`

### Documentation

- [ ] `nuaa-kit/README.md` includes Phase 3 workflow
- [ ] README explains placeholder resolution
- [ ] README documents all revision types
- [ ] Examples show complete draft → validate → revise cycle

### Validation

- [ ] Can draft a section from a plan
- [ ] Draft includes proper metadata and structure
- [ ] Placeholder markers work correctly
- [ ] Revision types produce appropriate changes
- [ ] Plan status updates automatically
- [ ] Section files are saved in correct location

---

## Technical Implementation Notes

### Context Loading Priority

The AI should load context in this order:

1. **Plan** - Get section purpose, requirements, gate, dependencies
2. **Specification** - Get program details
3. **Mission Constitution** - Get ethical principles
4. **Dependency Sections** - Get information this section builds on
5. **Related Sections** - Get parallel content for consistency

### Placeholder Best Practices

**Good Placeholders**:
- `[PLACEHOLDER: Exact geographic coverage area (LGAs or postcodes)?]`
- `[PLACEHOLDER: Final confirmed budget for peer educator training?]`
- `[PLACEHOLDER: Citation for naloxone effectiveness in peer-led programs]`

**Bad Placeholders**:
- `[PLACEHOLDER: More info needed]` (too vague)
- `[PLACEHOLDER: Data]` (not specific)
- `[PLACEHOLDER: Check with team]` (doesn't explain what's needed)

### Document Type Adaptation

The AI should adjust writing style based on document type:

- **Proposals**: Persuasive, future-focused ("will deliver", "aims to")
- **Program Designs**: Procedural, present-focused ("peer educators conduct", "the process involves")
- **Evaluation Reports**: Analytical, past-focused ("data showed", "participants reported")
- **Impact Reports**: Narrative, achievement-focused ("delivered X services", "reached Y people")

---

## Example User Flow

```bash
# User has completed Phase 2 (plan created)
$ nuaa status
# Shows: 12 sections, 0 complete, "Program Description" ready to draft

# User starts drafting first section
$ nuaa draft "Program Description"
✓ Created section file
✓ Plan status: In Progress

# User asks AI to draft content
/nuaa.draft "Program Description"
# AI loads spec, mission, dependencies
# AI creates comprehensive draft
# AI notes: "Draft has 2 placeholders - exact budget and training timeline"

# User reviews draft, sees placeholders
$ cat initiatives/001-naloxone/sections/program-description.md
# [PLACEHOLDER: Confirmed budget allocation for training?]
# [PLACEHOLDER: Timeline for initial training sessions?]

# User gathers missing info from team
# User resolves placeholders
$ nuaa draft "Program Description" --resolve
/nuaa.draft "Program Description" --resolve
# AI asks: "What is the confirmed budget allocation?"
# User: "$75,000"
# AI asks: "What is the timeline for initial training?"
# User: "First session in March 2025"
# AI updates draft, removes placeholders

# User validates section
$ nuaa gate-check "Program Description"
# Checks dependencies: ✓ All satisfied
# AI validates content
✓ PASS - Section meets all Gate 2 criteria

# User manually updates plan.md status to "Passed"
# User moves to next section
$ nuaa draft "Target Population"
````

---

## Questions for Clarification

If anything is unclear during implementation:

1. **Context loading**: Refer to SPEC-KIT-EVOLUTION-PLAN.md for detailed context requirements
2. **Placeholder format**: Use `[PLACEHOLDER: specific question]` consistently
3. **Revision scope**: Revisions should be targeted, not complete rewrites
4. **Document types**: See Phase 3 content guidelines for tone and structure by type

---

## Post-Implementation

After Phase 3 is complete, we'll move to:

**Phase 4**: Assembly & Review (combining sections into final documents)  
**Phase 5**: Backward Compatibility (migration tools for existing projects)

---

**Ready to implement Phase 3? Let's build the section drafting system!** 🚀
