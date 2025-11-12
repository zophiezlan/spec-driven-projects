# NUAA CLI Evolution - Phase 2 Implementation Prompt

## Phase 2: Planning & Quality Gates System

**Duration**: 3 weeks  
**Prerequisites**: Phase 1 complete (specify/clarify workflow operational)  
**Objective**: Implement structured document planning with 5-gate quality system

---

## Context & Foundation

You are implementing Phase 2 of the NUAA CLI evolution based on GitHub's spec-kit methodology. This phase introduces:

1. **Document Planning System**: Break programs into sections with dependencies and validation
2. **Quality Gates**: 5-gate validation system ensuring each section meets standards before progression
3. **Gate-Aware Commands**: Enhanced commands that check gate status before proceeding

### Domain Translation Reminder

| Software (spec-kit) | NGO (NUAA)    |
| ------------------- | ------------- |
| Feature             | Program       |
| Implementation Plan | Document Plan |
| Code Task           | Section Draft |
| Pull Request        | Draft Review  |
| CI/CD Pipeline      | Quality Gate  |

---

## Phase 2 Tasks

### Task 1: Create Document Plan Template

**File**: `nuaa-kit/templates/document-plan-template.md`

**Purpose**: Template for planning document structure with sections, dependencies, and gates

**Structure**:

```markdown
# Document Plan: [INITIATIVE_NAME]

**Initiative**: [INITIATIVE_NUMBER]-[SLUG]  
**Created**: [DATE]  
**Status**: Planning

---

## Planning Metadata

- **Document Type**: [Proposal | Program Design | Evaluation Report | Impact Report]
- **Target Length**: [X] pages / [Y] words (estimate)
- **Target Audience**: [Funding bodies | Board | Community | Government]
- **Deadline**: [DATE or TBD]
- **Review Process**: [Internal | External | Both]

---

## Document Structure

### Section 1: [SECTION_NAME]

**Gate**: Gate 1 - Initial Structure  
**Dependencies**: None (foundation section)  
**Estimated Length**: [X] paragraphs / [Y] words  
**Purpose**: [Why this section exists and what it accomplishes]

**Content Requirements**:

- [Bullet point 1: what must be included]
- [Bullet point 2: key information to cover]
- [Bullet point 3: specific data or examples needed]

**Quality Criteria** (for Gate 1):

- [ ] Section has clear purpose statement
- [ ] Key content requirements listed
- [ ] Length estimate provided
- [ ] No dependencies on incomplete sections

**Status**: Not Started

---

### Section 2: [SECTION_NAME]

**Gate**: Gate 2 - Core Content  
**Dependencies**: Section 1 (must be drafted first)  
**Estimated Length**: [X] paragraphs / [Y] words  
**Purpose**: [Why this section exists and what it accomplishes]

**Content Requirements**:

- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]

**Quality Criteria** (for Gate 2):

- [ ] All Gate 1 criteria met
- [ ] Core information present and complete
- [ ] Evidence cited for key claims
- [ ] Aligns with mission constitution
- [ ] Dependencies satisfied

**Status**: Not Started

---

[... Continue for all sections ...]

---

## Gate Definitions

### Gate 1: Initial Structure ✓

**Purpose**: Ensure foundational sections have clear purpose and structure  
**Applies To**: First 1-2 sections that establish context  
**Criteria**:

- Section has clear purpose statement
- Key content requirements identified
- Length estimate provided
- No dependencies or dependencies satisfied

### Gate 2: Core Content ✓

**Purpose**: Validate that essential program information is complete  
**Applies To**: Sections describing the program itself  
**Criteria**:

- All Gate 1 criteria met
- Core information present and complete
- Evidence cited for key claims
- Aligns with mission constitution

### Gate 3: Evidence & Justification ✓

**Purpose**: Ensure claims are supported by data and research  
**Applies To**: Sections making claims about effectiveness or need  
**Criteria**:

- All Gate 2 criteria met
- All claims have supporting evidence
- Evidence sources properly cited
- Logical reasoning connects evidence to conclusions

### Gate 4: Integration & Coherence ✓

**Purpose**: Verify sections work together as a cohesive document  
**Applies To**: Later sections that build on earlier content  
**Criteria**:

- All Gate 3 criteria met
- References to earlier sections are accurate
- No contradictions with other sections
- Consistent terminology and tone

### Gate 5: Review & Polish ✓

**Purpose**: Final quality check before submission  
**Applies To**: Completed document ready for review  
**Criteria**:

- All Gate 4 criteria met
- Grammar and spelling checked
- Formatting consistent throughout
- All placeholders resolved
- Ready for external review

---

## Section Progress Tracker

| Section   | Gate | Status      | Dependencies  | Blocker |
| --------- | ---- | ----------- | ------------- | ------- |
| 1. [Name] | 1    | Not Started | None          | -       |
| 2. [Name] | 2    | Not Started | Section 1     | -       |
| 3. [Name] | 2    | Not Started | Section 1     | -       |
| 4. [Name] | 3    | Not Started | Sections 2, 3 | -       |
| ...       | ...  | ...         | ...           | -       |

**Status Values**: Not Started | In Progress | Blocked | Gate Review | Passed | Failed

---

## Gate Progression Rules

1. **Cannot skip gates**: Section must pass Gate N before attempting Gate N+1
2. **Dependencies first**: All dependency sections must pass their gates first
3. **Gate failure**: If section fails a gate, it returns to "In Progress" status
4. **Re-review**: After fixing issues, section can be re-submitted to the gate
5. **Document completion**: All sections must pass Gate 5 before document is complete

---

## Notes & Decisions

[Space for documenting planning decisions, scope changes, timeline adjustments]

---

## Review History

| Date   | Reviewer | Section   | Gate   | Result      | Notes      |
| ------ | -------- | --------- | ------ | ----------- | ---------- |
| [DATE] | [NAME]   | [SECTION] | [GATE] | [Pass/Fail] | [Comments] |
```

**Key Design Elements**:

- Each section has a **gate assignment** (Gate 1-5)
- Each section has **dependencies** (which sections must be complete first)
- Each section has **quality criteria** specific to its gate
- **Progress tracker** shows document-wide status
- **Gate definitions** are clearly documented with criteria
- **Review history** tracks all gate validations

---

### Task 2: Create Plan Command Template

**File**: `nuaa-kit/commands/plan.md`

**Purpose**: AI agent command for creating document plans from specifications

**Content Structure**:

````markdown
---
description: "Create a document plan from a program specification"
---

# /nuaa.plan - Document Planning Command

Template: See [document-plan-template.md](../templates/document-plan-template.md).

## Description

Create a structured document plan from a program specification. This command takes the completed specification, determines the appropriate document type, breaks it into logical sections with dependencies, and assigns quality gates to each section.

---

## Purpose

The Document Plan:

- Transforms specifications into structured document outlines
- Breaks work into manageable, ordered sections
- Establishes dependencies between sections
- Assigns appropriate quality gates to each section
- Provides clear progression path through document creation
- Ensures quality validation at each stage

---

## Usage

```bash
/nuaa.plan [INITIATIVE] [--type TYPE]
```
````

**Examples**:

- `/nuaa.plan` - Plan the active/most recent initiative (auto-detect type)
- `/nuaa.plan 001-naloxone-distribution` - Plan a specific initiative
- `/nuaa.plan 002-mentorship --type proposal` - Plan with explicit document type

---

## Inputs Required

### From Specification File

The AI will read `initiatives/NNN-slug/spec.md` and extract:

1. **Program Overview**: What the program does
2. **Target Population**: Who benefits
3. **Evidence Base**: Research supporting the program
4. **Expected Outcomes**: What success looks like
5. **Resource Requirements**: Budget, staff, materials
6. **Risk Factors**: Potential challenges

### Document Type Detection

The AI will determine the appropriate document type based on:

- **Proposal**: If specification emphasizes funding needs, budget details, or uses proposal language
- **Program Design**: If specification focuses on implementation details, workflows, or operational procedures
- **Evaluation Report**: If specification mentions existing program, data collection, or outcome measurement
- **Impact Report**: If specification describes completed program and community impact

User can override with `--type` flag.

---

## Output Generated

The AI will create **initiatives/NNN-slug/plan.md** containing:

### 1. Planning Metadata

- Document type (detected or specified)
- Target length estimate (based on complexity)
- Target audience (based on document type)
- Deadline (if mentioned in spec, else TBD)
- Review process requirements

### 2. Section Breakdown

For each section, the AI will:

1. **Name the section** (e.g., "Executive Summary", "Program Description", "Budget Justification")
2. **Assign a gate** (1-5 based on section purpose and dependencies)
3. **Identify dependencies** (which sections must be complete first)
4. **Estimate length** (paragraphs/words based on content requirements)
5. **List content requirements** (what information must be included)
6. **Define quality criteria** (how to know the section meets its gate standards)

### 3. Logical Section Ordering

The AI will order sections to:

- Start with foundational/contextual sections (Gate 1)
- Progress to core program content (Gate 2)
- Add evidence and justification (Gate 3)
- Integrate with earlier content (Gate 4)
- Conclude with summary/polish (Gate 5)

### 4. Gate Assignments

**Gate 1** - Foundation sections with no dependencies:

- Executive Summary
- Background/Context
- Problem Statement

**Gate 2** - Core program content:

- Program Description
- Target Population
- Service Delivery Model
- Staffing Model

**Gate 3** - Evidence-based sections:

- Literature Review
- Theory of Change
- Evaluation Framework
- Budget Justification

**Gate 4** - Integration sections:

- Implementation Timeline
- Risk Management
- Sustainability Plan

**Gate 5** - Final sections:

- Conclusion
- Appendices
- References

### 5. Progress Tracker

A table showing all sections with:

- Gate assignment
- Current status (all start as "Not Started")
- Dependencies
- Blockers (initially empty)

---

## Gate Assignment Logic

The AI uses this logic to assign gates:

```
IF section has NO dependencies AND is foundational:
    ASSIGN Gate 1

ELSE IF section describes core program elements:
    ASSIGN Gate 2

ELSE IF section makes claims requiring evidence:
    ASSIGN Gate 3

ELSE IF section references multiple earlier sections:
    ASSIGN Gate 4

ELSE IF section is final polish (conclusion, appendices):
    ASSIGN Gate 5
```

---

## Dependency Detection

The AI automatically detects dependencies:

- **"Program Description" depends on "Problem Statement"**: Can't describe solution without defining problem
- **"Budget Justification" depends on "Program Description"**: Can't justify costs without knowing activities
- **"Evaluation Framework" depends on "Expected Outcomes"**: Can't measure without knowing goals
- **"Sustainability Plan" depends on "Budget Justification"**: Can't plan long-term without knowing costs

---

## Example Output

For a naloxone distribution program, the AI might create:

**Document Type**: Proposal (detected from funding emphasis in spec)  
**Sections**: 12 sections  
**Gates**: 3 × Gate 1, 4 × Gate 2, 3 × Gate 3, 1 × Gate 4, 1 × Gate 5

**Section Flow**:

1. Executive Summary (Gate 1, no deps) ← Start here
2. Opioid Crisis Context (Gate 1, no deps)
3. Naloxone Evidence Base (Gate 1, no deps)
4. Program Description (Gate 2, deps: 1, 2)
5. Peer-Led Model Justification (Gate 3, deps: 4)
6. Target Population (Gate 2, deps: 2)
7. Distribution Strategy (Gate 2, deps: 4, 6)
8. Training Program (Gate 2, deps: 4)
9. Evaluation Framework (Gate 3, deps: 4, 6)
10. Budget & Resources (Gate 3, deps: 4, 7, 8)
11. Implementation Timeline (Gate 4, deps: all above)
12. Conclusion (Gate 5, deps: all above)

---

## Validation & Checks

Before creating the plan, the AI will:

1. **Check specification status**: Ensure spec has no `[NEEDS CLARIFICATION]` markers
2. **Verify mission alignment**: Check spec references mission constitution
3. **Assess completeness**: Ensure spec has all required sections filled
4. **Warn if incomplete**: If spec has `[PLACEHOLDER]` markers, suggest completing spec first

After creating the plan, the AI will:

1. **Verify gate distribution**: Ensure balanced gate assignments (not all Gate 5)
2. **Check dependency cycles**: Ensure no circular dependencies (A depends on B, B depends on A)
3. **Validate progression**: Ensure logical flow from Gate 1 → Gate 5
4. **Confirm tractability**: Ensure no section has too many dependencies (max 3-4)

---

## Mission Constitution Integration

The AI will ensure the document plan:

- Includes sections addressing harm reduction principles
- Plans for lived experience integration (if relevant)
- Incorporates evidence-based practice requirements
- Addresses community self-determination
- Considers anti-stigma language throughout

---

## Next Steps After Planning

After the plan is created, the user can:

1. **Review the plan**: Check section ordering and gate assignments
2. **Adjust if needed**: Manually edit plan.md to refine structure
3. **Begin drafting**: Use `/nuaa.draft [SECTION_NAME]` to start writing sections
4. **Track progress**: Use `nuaa status` to see which sections are complete
5. **Validate gates**: Use `nuaa gate-check [SECTION]` to validate section quality

---

## Technical Notes for AI

**File Locations**:

- Input: `initiatives/NNN-slug/spec.md`
- Output: `initiatives/NNN-slug/plan.md`
- Template: `nuaa-kit/templates/document-plan-template.md`

**Section Count Guidelines**:

- Proposals: 10-15 sections
- Program Designs: 12-18 sections
- Evaluation Reports: 8-12 sections
- Impact Reports: 8-12 sections

**Length Estimates**:

- Short section: 1-2 paragraphs (150-300 words)
- Medium section: 3-5 paragraphs (400-800 words)
- Long section: 6-10 paragraphs (1000-1500 words)

**Gate Distribution**:

- Gate 1: 15-20% of sections (foundation)
- Gate 2: 30-40% of sections (core content)
- Gate 3: 25-35% of sections (evidence)
- Gate 4: 10-15% of sections (integration)
- Gate 5: 5-10% of sections (polish)

````

---

### Task 3: Create Gate Check Command Template

**File**: `nuaa-kit/commands/gate-check.md`

**Purpose**: AI agent command for validating sections against gate criteria

**Content Structure**:

```markdown
---
description: "Validate a section against its quality gate criteria"
---

# /nuaa.gate-check - Quality Gate Validation Command

## Description

Validate that a drafted section meets all criteria for its assigned quality gate. This command reads the section content, reviews it against the gate's standards, and provides a pass/fail result with specific feedback.

---

## Purpose

Gate Validation:

- Ensures sections meet quality standards before progression
- Provides specific, actionable feedback on failures
- Prevents compound errors by catching issues early
- Maintains document quality throughout drafting
- Enforces dependency and coherence requirements

---

## Usage

```bash
/nuaa.gate-check [INITIATIVE] [SECTION_NAME]
````

**Examples**:

- `/nuaa.gate-check "Program Description"` - Check the Program Description section in active initiative
- `/nuaa.gate-check 001-naloxone-distribution "Budget Justification"` - Check specific section in specific initiative

---

## How It Works

### Step 1: Load Context

The AI will:

1. Identify the initiative (from argument or active initiative)
2. Read `initiatives/NNN-slug/plan.md` to find the section
3. Extract the section's **gate assignment** (1-5)
4. Extract the section's **quality criteria** from the plan
5. Extract the section's **dependencies** from the plan
6. Read `initiatives/NNN-slug/sections/[SECTION_NAME].md` for content

### Step 2: Check Dependencies

Before validating content, the AI will:

1. Identify all dependency sections
2. Check the status of each dependency in plan.md
3. **FAIL** if any dependency has not passed its gate
4. Provide specific feedback: "Section X depends on [Y] which has not passed Gate [N]"

### Step 3: Validate Against Gate Criteria

The AI will review the section content against its gate's criteria:

#### Gate 1 Validation

- [ ] Section has clear purpose statement (first paragraph states why this section exists)
- [ ] Key content requirements identified (all bullets from plan are addressed)
- [ ] Length estimate reasonable (within 20% of plan estimate)
- [ ] No placeholder markers remaining (`[PLACEHOLDER]` or `[TODO]`)

#### Gate 2 Validation

All Gate 1 criteria PLUS:

- [ ] Core information present and complete (all required facts/details included)
- [ ] Evidence cited for key claims (at least 1 citation per major claim)
- [ ] Aligns with mission constitution (uses harm reduction language, acknowledges lived experience)
- [ ] Writing is clear and accessible (no jargon without explanation)

#### Gate 3 Validation

All Gate 2 criteria PLUS:

- [ ] All claims have supporting evidence (every assertion backed by data or research)
- [ ] Evidence sources properly cited (APA format, complete references)
- [ ] Logical reasoning connects evidence to conclusions (clear "because X, therefore Y" structure)
- [ ] Evidence quality is appropriate (peer-reviewed > grey literature > anecdotal)

#### Gate 4 Validation

All Gate 3 criteria PLUS:

- [ ] References to earlier sections are accurate (section numbers, facts, figures match)
- [ ] No contradictions with other sections (consistent numbers, dates, descriptions)
- [ ] Consistent terminology and tone (same terms for same concepts, same voice)
- [ ] Builds on earlier content (doesn't repeat, extends or applies previous information)

#### Gate 5 Validation

All Gate 4 criteria PLUS:

- [ ] Grammar and spelling checked (no errors)
- [ ] Formatting consistent throughout (headings, bullets, spacing match document style)
- [ ] All placeholders resolved (no `[PLACEHOLDER]`, `[TODO]`, `[TBD]`)
- [ ] Ready for external review (professional appearance, complete content)

### Step 4: Provide Feedback

The AI will generate a validation report:

```markdown
# Gate Validation Report: [SECTION_NAME]

**Initiative**: [NNN-slug]  
**Gate**: Gate [N] - [Gate Name]  
**Date**: [DATE]  
**Result**: [PASS / FAIL]

---

## Criteria Results

### Gate [N] Criteria

1. [Criterion 1]: ✓ PASS / ✗ FAIL

   - [Explanation of pass/fail]
   - [Specific examples from content]

2. [Criterion 2]: ✓ PASS / ✗ FAIL
   - [Explanation]
   - [Examples]

[... all criteria ...]

---

## Dependencies

- [Dependency 1]: ✓ Passed Gate [N]
- [Dependency 2]: ✗ Blocked - has not passed Gate [N]

---

## Feedback Summary

**Strengths**:

- [What the section does well]
- [Specific positive examples]

**Issues to Address**:

- [Specific problem 1 with location in section]
- [Specific problem 2 with location in section]
- [Actionable fixes for each issue]

---

## Recommendation

[PASS]: Section meets all Gate [N] criteria and is ready to proceed.

[FAIL]: Section does not meet [X] of [Y] criteria. Address the issues above and resubmit for validation.

---

## Next Steps

[If PASS]:

- Update plan.md to mark section as "Passed"
- If this section is a dependency for others, those sections can now proceed
- Continue to next section or submit section to Gate [N+1] if higher gate needed

[If FAIL]:

- Review feedback and address all failing criteria
- Make necessary revisions to section content
- Resubmit to `/nuaa.gate-check` for re-validation
```

---

## Validation Strictness

The AI will be **strict but fair**:

- **Minor issues** (1-2 small problems): Can still pass with notes
- **Major issues** (missing evidence, contradictions): Automatic fail
- **Dependency violations**: Automatic fail, no content review
- **Placeholder markers**: Automatic fail for Gate 2+

---

## Example Validations

### Example 1: Gate 2 Pass

**Section**: Program Description  
**Gate**: 2 (Core Content)  
**Result**: PASS

**Feedback**:

- ✓ Clear purpose statement in first paragraph
- ✓ All content requirements addressed (peer model, distribution strategy, training)
- ✓ Evidence cited (3 references to naloxone research)
- ✓ Mission alignment (harm reduction language throughout)
- Minor note: Consider expanding training details in future draft

### Example 2: Gate 3 Fail

**Section**: Budget Justification  
**Gate**: 3 (Evidence & Justification)  
**Result**: FAIL (2 of 4 criteria failed)

**Issues**:

- ✗ Claim "Peer educators are more cost-effective" lacks supporting data
- ✗ Equipment costs not justified with market research or quotes
- ✓ Staff salary reasoning is solid with industry benchmarks cited
- ✓ Logic connecting budget to outcomes is clear

**Actionable fixes**:

1. Add cost comparison data between peer vs. professional models (line 45)
2. Include quotes from suppliers for equipment costs (line 78)
3. Consider adding ROI calculation for harm reduction outcomes

---

## Technical Notes for AI

**File Locations**:

- Plan: `initiatives/NNN-slug/plan.md`
- Section: `initiatives/NNN-slug/sections/[SECTION_NAME].md`
- Constitution: `memory/constitution.md` (for mission alignment checks)

**Status Updates**:
After validation, the AI should suggest updating the plan:

- PASS: Change section status to "Passed" in plan.md tracker
- FAIL: Change section status to "Gate Review" with blocker note

**Gate Criteria Inheritance**:
Remember that higher gates **include all lower gate criteria**. Gate 4 must pass all of Gate 1, 2, 3, and 4 criteria.

**Common Failure Patterns**:

- Gate 2: Missing evidence citations (most common issue)
- Gate 3: Weak evidence sources (grey literature when peer-reviewed available)
- Gate 4: Contradictions with earlier sections (numbers don't match)
- Gate 5: Formatting inconsistencies (different heading styles)

````

---

### Task 4: Create Status Command Template

**File**: `nuaa-kit/commands/status.md`

**Purpose**: AI agent command for showing initiative progress and gate status

**Content Structure**:

```markdown
---
description: "Show initiative progress and section gate status"
---

# /nuaa.status - Initiative Status Command

## Description

Display the current status of an initiative, showing which sections have been drafted, their gate validation status, and any blockers preventing progress.

---

## Purpose

Status Reporting:

- Provides quick overview of initiative progress
- Shows which sections are complete vs. in progress
- Identifies blockers and dependencies
- Highlights next available sections to work on
- Tracks overall gate passage rates

---

## Usage

```bash
/nuaa.status [INITIATIVE]
````

**Examples**:

- `/nuaa.status` - Show status of active/most recent initiative
- `/nuaa.status 001-naloxone-distribution` - Show status of specific initiative

---

## Output Format

```markdown
# Initiative Status: [INITIATIVE_NAME]

**Initiative**: [NNN-slug]  
**Document Type**: [Proposal | Program Design | etc.]  
**Last Updated**: [DATE]  
**Overall Progress**: [X]% ([Y] of [Z] sections complete)

---

## Section Progress

| #   | Section Name          | Gate | Status         | Dependencies | Blocker              |
| --- | --------------------- | ---- | -------------- | ------------ | -------------------- |
| 1   | Executive Summary     | 1    | ✓ Passed       | None         | -                    |
| 2   | Opioid Crisis Context | 1    | ✓ Passed       | None         | -                    |
| 3   | Program Description   | 2    | 🔄 In Progress | 1, 2         | -                    |
| 4   | Budget Justification  | 3    | ⏸ Blocked      | 3            | Section 3 incomplete |
| 5   | Evaluation Framework  | 3    | ⭕ Not Started | 3            | Section 3 incomplete |

**Status Legend**:

- ✓ Passed: Section complete and validated
- 🔄 In Progress: Currently being drafted
- ⏸ Blocked: Dependencies not met
- ⭕ Not Started: Ready to start (no blockers)
- ❌ Failed: Gate validation failed

---

## Gate Summary

| Gate | Passed | In Progress | Not Started | Pass Rate |
| ---- | ------ | ----------- | ----------- | --------- |
| 1    | 3      | 0           | 0           | 100%      |
| 2    | 1      | 2           | 1           | 25%       |
| 3    | 0      | 0           | 3           | 0%        |
| 4    | 0      | 0           | 1           | 0%        |
| 5    | 0      | 0           | 1           | 0%        |

---

## Next Actionable Sections

**Ready to Draft** (no blockers):

1. Program Description (Gate 2) - dependencies satisfied
2. Target Population (Gate 2) - dependencies satisfied

**Blocked**:

- Budget Justification (Gate 3) - waiting for Program Description
- Evaluation Framework (Gate 3) - waiting for Program Description
- Timeline (Gate 4) - waiting for multiple sections

---

## Timeline Estimate

**Completed**: [X] sections in [Y] weeks  
**Average**: [Z] days per section  
**Remaining**: [A] sections  
**Estimated Completion**: [B] weeks from now ([DATE])

_Note: Estimate assumes consistent pace and no major blockers_

---

## Recent Activity

- [DATE]: Section "Executive Summary" passed Gate 1
- [DATE]: Section "Context" passed Gate 1
- [DATE]: Section "Program Description" started
- [DATE]: Section "Budget" marked as blocked

---

## Warnings & Recommendations

[AI will check for common issues and suggest]:

⚠ **Dependency Chain**: 4 sections blocked by "Program Description" - prioritize completing this section  
⚠ **Gate Imbalance**: No sections have attempted Gate 3 yet - ensure evidence gathering is underway  
✓ **On Track**: Foundation sections (Gate 1) are complete - good progress  
💡 **Suggestion**: Consider drafting "Target Population" next - it's ready and has no dependencies
```

---

## Technical Notes for AI

**File Locations**:

- Plan: `initiatives/NNN-slug/plan.md` (read section tracker table)
- Sections: `initiatives/NNN-slug/sections/` (check for file existence)

**Progress Calculation**:

```
Sections Complete = Count of "Passed" status
Total Sections = All sections in plan
Progress % = (Complete / Total) × 100
```

**Blocker Detection**:

- Section is blocked if ANY dependency has not passed its gate
- List the first failing dependency as the blocker
- If multiple, note "Multiple: [list]"

**Timeline Estimation**:

```
If >= 3 sections complete:
    Average days = (Today - Plan Created Date) / Sections Complete
    Remaining days = Average × Remaining Sections
    Estimated completion = Today + Remaining days
Else:
    Show "Not enough data for estimate"
```

````

---

### Task 5: Create Gate Management Script (Bash)

**File**: `scripts/bash/check-gate-status.sh`

**Purpose**: Validate gate status and dependencies programmatically

**Key Functions**:

```bash
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
        initiative=$(ls -t initiatives/ | head -n 1)
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
    # - Quality criteria

    # Look for section header: ### Section N: [SECTION_NAME]
    # Extract gate from: **Gate**: Gate N - Name
    # Extract deps from: **Dependencies**: Section X, Section Y
    # Extract status from: **Status**: [Status]

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
            echo "{\"satisfied\": false, \"failed\": [\"${failed_deps[*]}\"]}"
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
````

**Key Features**:

- Parses plan.md to extract section metadata
- Validates dependencies are satisfied
- Supports JSON output for CLI integration
- Returns exit codes for scripting (0 = dependencies ok, 1 = blocked)

---

### Task 6: Create Gate Management Script (PowerShell)

**File**: `scripts/powershell/check-gate-status.ps1`

**Purpose**: PowerShell mirror of bash gate checking script

**Key Functions**:

```powershell
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
```

---

### Task 7: Integrate Gate Checking into CLI

**File**: `src/nuaa_cli/__init__.py`

**Add new commands**:

```python
@app.command()
def plan(
    initiative: Optional[str] = typer.Argument(None, help="Initiative to plan (e.g., '001-naloxone-distribution'). If not provided, uses most recent."),
    doc_type: Optional[str] = typer.Option(None, "--type", help="Document type: proposal, design, evaluation, impact"),
):
    """Create a document plan from a program specification."""
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

    # Check spec exists and is complete
    spec_file = Path(f"initiatives/{initiative}/spec.md")
    if not spec_file.exists():
        console.print(f"[red]Error: Specification not found: {spec_file}[/red]")
        console.print("[yellow]Run 'nuaa specify' first to create a specification[/yellow]")
        raise typer.Exit(1)

    # Check for clarification markers
    spec_content = spec_file.read_text()
    if "[NEEDS CLARIFICATION:" in spec_content:
        console.print("[yellow]Warning: Specification has unresolved clarifications[/yellow]")
        console.print("[yellow]Consider running 'nuaa clarify' first[/yellow]")

        if not typer.confirm("Continue anyway?"):
            raise typer.Exit(0)

    # Success message
    plan_file = Path(f"initiatives/{initiative}/plan.md")
    console.print(Panel(
        f"[green]✓[/green] Initiative: [cyan]{initiative}[/cyan]\n"
        f"[green]✓[/green] Specification: [cyan]{spec_file}[/cyan]\n"
        f"[green]✓[/green] Document type: [cyan]{doc_type or 'auto-detect'}[/cyan]\n\n"
        f"[bold]AI will create:[/bold]\n"
        f"  • Document plan with section breakdown\n"
        f"  • Gate assignments for each section\n"
        f"  • Dependency mapping between sections\n"
        f"  • Quality criteria for validation\n\n"
        f"[bold]Next steps:[/bold]\n"
        f"  1. Have AI create the plan using [cyan]/nuaa.plan[/cyan]\n"
        f"  2. Review the plan in [cyan]{plan_file}[/cyan]\n"
        f"  3. Start drafting with [cyan]nuaa draft [SECTION][/cyan]",
        title="Ready to Plan",
        border_style="green"
    ))


@app.command()
def gate_check(
    section: str = typer.Argument(..., help="Section name to validate (e.g., 'Program Description')"),
    initiative: Optional[str] = typer.Option(None, "--initiative", help="Initiative to check (uses most recent if not specified)"),
):
    """Validate a section against its quality gate criteria."""
    show_banner()

    # Call the check-gate-status script
    script_path = Path("scripts/bash/check-gate-status.sh")
    if sys.platform == "win32":
        script_path = Path("scripts/powershell/check-gate-status.ps1")

    if not script_path.exists():
        console.print(f"[red]Error: Script not found: {script_path}[/red]")
        raise typer.Exit(1)

    # Build command
    cmd_args = ["--json", "--section", section]
    if initiative:
        cmd_args.extend(["--initiative", initiative])

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
            # Dependencies not satisfied
            data = json.loads(result.stdout)
            console.print(Panel(
                f"[yellow]⚠[/yellow] Section: [cyan]{data['section']}[/cyan]\n"
                f"[yellow]⚠[/yellow] Gate: [cyan]Gate {data['gate']}[/cyan]\n"
                f"[yellow]⚠[/yellow] Status: [cyan]{data['status']}[/cyan]\n\n"
                f"[red]✗ Dependencies not satisfied[/red]\n\n"
                f"[bold]This section cannot proceed until dependencies are complete.[/bold]",
                title="Gate Check Failed",
                border_style="red"
            ))
            raise typer.Exit(1)

        # Dependencies satisfied
        data = json.loads(result.stdout)
        console.print(Panel(
            f"[green]✓[/green] Section: [cyan]{data['section']}[/cyan]\n"
            f"[green]✓[/green] Gate: [cyan]Gate {data['gate']}[/cyan]\n"
            f"[green]✓[/green] Status: [cyan]{data['status']}[/cyan]\n"
            f"[green]✓[/green] Dependencies: [cyan]{data['dependencies']}[/cyan]\n\n"
            f"[bold]Next steps:[/bold]\n"
            f"  1. Have AI validate content with [cyan]/nuaa.gate-check {section}[/cyan]\n"
            f"  2. Address any feedback from validation\n"
            f"  3. Update plan.md with validation result",
            title="Gate Check Passed",
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
def status(
    initiative: Optional[str] = typer.Argument(None, help="Initiative to check (uses most recent if not specified)"),
):
    """Show initiative progress and section gate status."""
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

    console.print(Panel(
        f"[green]✓[/green] Initiative: [cyan]{initiative}[/cyan]\n"
        f"[green]✓[/green] Plan: [cyan]{plan_file}[/cyan]\n\n"
        f"[bold]AI will show:[/bold]\n"
        f"  • Section progress and gate status\n"
        f"  • Blocked sections and dependencies\n"
        f"  • Next available sections to work on\n"
        f"  • Overall completion percentage\n\n"
        f"[bold]Have AI run:[/bold] [cyan]/nuaa.status[/cyan]",
        title="Status Check Ready",
        border_style="blue"
    ))
```

---

### Task 8: Update Documentation

**Files to Update**:

1. **nuaa-kit/README.md** - Add Phase 2 workflow section:

````markdown
### The Plan → Draft → Gate-Check Workflow

After your specification is complete and clarified, create a structured document plan:

#### 1. Create the Plan

**CLI**:

```bash
nuaa plan
# or
nuaa plan 001-naloxone-distribution --type proposal
```
````

**AI Agent**:

```
/nuaa.plan Create a document plan for this naloxone distribution program
```

This generates `initiatives/001-naloxone-distribution/plan.md` with:

- Section breakdown with gate assignments
- Dependencies between sections
- Quality criteria for each gate
- Progress tracking table

#### 2. Draft Sections

Work through sections in order, respecting dependencies:

```
/nuaa.draft "Program Description"
```

The AI will create `initiatives/001-naloxone-distribution/sections/program-description.md`.

#### 3. Validate Gates

Before moving to dependent sections, validate the current section:

**CLI**:

```bash
nuaa gate-check "Program Description"
```

**AI Agent**:

```
/nuaa.gate-check "Program Description"
```

The AI provides pass/fail with specific feedback.

#### 4. Track Progress

**CLI**:

```bash
nuaa status
```

**AI Agent**:

```
/nuaa.status
```

Shows overall progress, blocked sections, and next available work.

#### 5. The Five Gates

**Gate 1 - Initial Structure**: Foundation sections with clear purpose  
**Gate 2 - Core Content**: Essential program information complete  
**Gate 3 - Evidence & Justification**: Claims supported by research  
**Gate 4 - Integration & Coherence**: Sections work together cohesively  
**Gate 5 - Review & Polish**: Final quality check before submission

Each gate has specific validation criteria. Higher gates include all lower gate criteria.

````

2. **CHANGELOG.md** - Add Phase 2 entries

3. **Update version in pyproject.toml** if warranted

---

## Acceptance Criteria

Phase 2 is complete when:

### Templates & Commands

- [ ] `nuaa-kit/templates/document-plan-template.md` exists with all 5 gates defined
- [ ] `nuaa-kit/commands/plan.md` exists with planning logic documented
- [ ] `nuaa-kit/commands/gate-check.md` exists with all 5 gate validation criteria
- [ ] `nuaa-kit/commands/status.md` exists with progress tracking format

### Scripts

- [ ] `scripts/bash/check-gate-status.sh` exists and validates dependencies
- [ ] `scripts/powershell/check-gate-status.ps1` mirrors bash functionality
- [ ] Both scripts support `--json` flag for programmatic output
- [ ] Scripts correctly parse plan.md section tracker table

### CLI Integration

- [ ] `nuaa plan` command exists and calls AI appropriately
- [ ] `nuaa gate-check [SECTION]` command validates dependencies
- [ ] `nuaa status` command shows initiative progress
- [ ] All commands handle missing files gracefully with helpful errors
- [ ] Commands update `pyproject.toml` version and `CHANGELOG.md`

### Documentation

- [ ] `nuaa-kit/README.md` includes Phase 2 workflow section
- [ ] README explains all 5 gates with examples
- [ ] README shows complete plan → draft → gate-check → status workflow
- [ ] Examples demonstrate dependency management

### Validation

- [ ] Can create a plan for a completed specification
- [ ] Plan correctly assigns gates to sections (balanced distribution)
- [ ] Plan identifies logical dependencies between sections
- [ ] Gate check blocks sections with unsatisfied dependencies
- [ ] Status command shows accurate progress tracking
- [ ] Gate validation provides specific, actionable feedback

---

## Technical Implementation Notes

### Gate Assignment Logic

The AI should assign gates based on section purpose:

- **Gate 1**: Foundational sections with no dependencies (context, background)
- **Gate 2**: Core program description sections
- **Gate 3**: Sections requiring evidence (literature review, justification)
- **Gate 4**: Integration sections referencing multiple earlier sections
- **Gate 5**: Final polish sections (conclusion, appendices)

### Dependency Detection

The AI should identify dependencies when:
- Section B describes details of concepts introduced in Section A
- Section B requires data or information from Section A
- Section B builds on conclusions from Section A
- Section B references specific content from Section A

### Quality Criteria Inheritance

Remember: Higher gates include all lower gate criteria!
- Gate 2 checks: All Gate 1 criteria + Gate 2 criteria
- Gate 3 checks: All Gate 1, 2, and 3 criteria
- Gate 4 checks: All Gate 1, 2, 3, and 4 criteria
- Gate 5 checks: ALL criteria from all gates

---

## Example User Flow

```bash
# User has completed Phase 1
$ nuaa clarify 001-naloxone-distribution
# AI resolves all [NEEDS CLARIFICATION] markers

# User starts Phase 2
$ nuaa plan
✓ Created document plan: initiatives/001-naloxone-distribution/plan.md
✓ 12 sections identified
✓ Gates assigned: 3×Gate1, 4×Gate2, 3×Gate3, 1×Gate4, 1×Gate5

# User asks AI to draft first section
/nuaa.draft "Executive Summary"
# AI creates sections/executive-summary.md

# User validates the section
$ nuaa gate-check "Executive Summary"
✓ Dependencies satisfied (none required)
✓ Ready for AI validation

/nuaa.gate-check "Executive Summary"
# AI provides detailed validation report
✓ PASS - Section meets all Gate 1 criteria

# User checks overall progress
$ nuaa status
# Shows: 1 of 12 sections complete (8%)
# Next available: "Opioid Crisis Context", "Naloxone Evidence Base"

# User continues drafting...
````

---

## Questions for Clarification

If anything is unclear during implementation:

1. **Gate criteria specifics**: Refer to SPEC-KIT-EVOLUTION-PLAN.md for detailed gate definitions
2. **Section types**: Common sections include Executive Summary, Background, Program Description, Budget, Timeline, Evaluation
3. **Dependency logic**: If unsure whether Section B depends on Section A, ask: "Can Section B be fully written without reading Section A?"
4. **Template structure**: Follow the exact format in this prompt for consistency

---

## Post-Implementation

After Phase 2 is complete, we'll move to:

**Phase 3**: Section-by-Section Drafting (interactive drafting workflow)  
**Phase 4**: Assembly & Review (combining sections into final documents)  
**Phase 5**: Backward Compatibility (migration tools for existing projects)

---

**Ready to implement Phase 2? Let's build the planning and quality gate system!** 🚀
