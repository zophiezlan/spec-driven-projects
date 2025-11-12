# NUAA CLI Evolution - Phase 4 Implementation Prompt

## Phase 4: Assembly & Review System

**Duration**: 2-3 weeks  
**Prerequisites**: Phase 3 complete (section drafting operational)  
**Objective**: Implement document assembly, review workflows, and final output generation

---

## Context & Foundation

You are implementing Phase 4 of the NUAA CLI evolution based on GitHub's spec-kit methodology. This phase introduces:

1. **Document Assembly**: Combining validated sections into complete documents
2. **Review Workflows**: Structured feedback and approval processes
3. **Export Formats**: Generating final documents in multiple formats
4. **Quality Assurance**: Final validation before submission
5. **Version Management**: Tracking document versions and changes

### Domain Translation Reminder

| Software (spec-kit) | NGO (NUAA)            |
| ------------------- | --------------------- |
| Pull Request        | Draft Document Review |
| Code Review         | Document Review       |
| CI/CD Pipeline      | Final Quality Check   |
| Merge to Main       | Document Approval     |
| Release             | Final Submission      |

---

## Phase 4 Tasks

### Task 1: Create Document Assembly Template

**File**: `nuaa-kit/templates/final-document-template.md`

**Purpose**: Template structure for assembled documents with proper formatting

**Structure**:

```markdown
# [DOCUMENT_TITLE]

**Initiative**: [INITIATIVE_NUMBER]-[SLUG]  
**Document Type**: [Proposal | Program Design | Evaluation Report | Impact Report]  
**Version**: [VERSION]  
**Date**: [DATE]  
**Status**: [Draft | Under Review | Approved | Final]

---

## Document Metadata

- **Organization**: NSW Users and AIDS Association (NUAA)
- **Authors**: [AUTHOR_NAMES]
- **Reviewers**: [REVIEWER_NAMES]
- **Target Audience**: [Funding bodies | Board | Community | Government]
- **Submission Deadline**: [DATE or N/A]

---

<!-- BEGIN ASSEMBLED CONTENT -->

[Section 1 content]

---

[Section 2 content]

---

[Section 3 content]

---

[... all sections in order ...]

<!-- END ASSEMBLED CONTENT -->

---

## Document History

| Version   | Date   | Changes   | Author   |
| --------- | ------ | --------- | -------- |
| [VERSION] | [DATE] | [CHANGES] | [AUTHOR] |

---

## Approval

| Role                     | Name | Date | Signature |
| ------------------------ | ---- | ---- | --------- |
| **Program Manager**      |      |      |           |
| **Executive Director**   |      |      |           |
| **Board Representative** |      |      |           |

---

## Assembly Metadata

- **Assembled from**: [N] sections
- **Total word count**: [WORDS]
- **Gate validation**: All sections passed
- **Generated**: [TIMESTAMP]
- **Tool**: NUAA CLI v[VERSION]
```

**Key Design Elements**:

- Professional document header with metadata
- Clear separation of assembled content
- Version history tracking
- Approval signature section
- Assembly metadata for transparency

---

### Task 2: Create Assemble Command Template

**File**: `nuaa-kit/commands/assemble.md`

**Purpose**: AI agent command for assembling sections into final documents

**Content Structure**:

````markdown
---
description: "Assemble validated sections into a final document"
---

# /nuaa.assemble - Document Assembly Command

Template: See [final-document-template.md](../templates/final-document-template.md).

## Description

Assemble all validated sections from a document plan into a complete, formatted final document. This command verifies that all sections have passed their gates, combines them in proper order, adds necessary transitions, and generates the final output.

---

## Purpose

Document Assembly:

- Combines validated sections into cohesive document
- Adds transitions between sections for flow
- Includes proper document metadata and headers
- Verifies all gates passed before assembly
- Generates table of contents automatically
- Produces final document ready for review

---

## Usage

```bash
/nuaa.assemble [INITIATIVE] [--format FORMAT]
```
````

**Examples**:

- `/nuaa.assemble` - Assemble the active/most recent initiative
- `/nuaa.assemble 001-naloxone-distribution` - Assemble specific initiative
- `/nuaa.assemble --format pdf` - Assemble and export as PDF

---

## How It Works

### Step 1: Pre-Assembly Validation

The AI will:

1. Read `initiatives/NNN-slug/plan.md`
2. Check that ALL sections have "Passed" status
3. If any section has not passed:
   - List which sections are incomplete
   - Show their current status (In Progress, Blocked, etc.)
   - Exit with error message
4. Verify all sections have passed their assigned gates
5. Check for any remaining `[PLACEHOLDER]` markers in sections

**Assembly Prerequisites**:

- ✓ All sections must have "Passed" status in plan
- ✓ No sections can be "In Progress" or "Blocked"
- ✓ All sections must pass gate validation
- ✓ No placeholder markers allowed

### Step 2: Load Section Content

The AI will:

1. Read all section files from `initiatives/NNN-slug/sections/`
2. Load sections in the order specified in plan.md
3. Extract section content (excluding metadata)
4. Note section word counts and lengths

### Step 3: Add Transitions

The AI will review section boundaries and add transitions where needed:

**When Transitions Are Needed**:

- Topic shifts between sections
- Moving from context to program description
- Shifting from description to justification
- Transitioning to budget or implementation details

**Example Transitions**:

```markdown
<!-- Between Background and Program Description -->

With this understanding of the opioid crisis context, we now turn to
the proposed peer-led naloxone distribution program.

---

<!-- Between Program Description and Budget Justification -->

Having outlined the program model and service delivery approach, the
following section details the resources required for implementation.

---

<!-- Between Evaluation Framework and Conclusion -->

This comprehensive evaluation approach will enable us to measure impact
and continuously improve program delivery, as summarized in the conclusion.
```

**Transition Guidelines**:

- Keep transitions brief (1-2 sentences)
- Use forward references ("the following section...")
- Maintain professional tone
- Don't repeat content from adjacent sections

### Step 4: Generate Table of Contents

The AI will:

1. Extract all section headings (## level and below)
2. Create hierarchical table of contents
3. Number sections appropriately
4. Add page number placeholders (if format supports)

**Example TOC**:

```markdown
## Table of Contents

1. Executive Summary ..................................................... 1
2. Background and Context ............................................... 3
   2.1 The Opioid Crisis in NSW ......................................... 3
   2.2 Gaps in Current Services ......................................... 5
3. Proposed Program ..................................................... 7
   3.1 Program Description .............................................. 7
   3.2 Target Population ................................................ 9
   3.3 Service Delivery Model .......................................... 11
4. Evidence Base ....................................................... 14
   4.1 Literature Review ............................................... 14
   4.2 Best Practices in Peer-Led Programs ............................. 16
5. Implementation Plan ................................................. 19
   5.1 Timeline and Milestones ......................................... 19
   5.2 Staffing and Governance ......................................... 21
6. Budget and Resources ................................................ 24
   6.1 Budget Breakdown ................................................ 24
   6.2 Budget Justification ............................................ 26
7. Evaluation Framework ................................................ 29
8. Conclusion .......................................................... 32
9. References .......................................................... 34
10. Appendices ......................................................... 36
```

### Step 5: Add Document Metadata

The AI will populate the final document template with:

**Header Information**:

- Document title (from initiative name + document type)
- Initiative number and slug
- Document type from plan.md
- Version number (1.0 for initial assembly)
- Current date
- Status (Draft for first assembly)

**Document Metadata**:

- Organization: "NSW Users and AIDS Association (NUAA)"
- Authors: Extract from section revision histories
- Reviewers: Leave blank for manual completion
- Target audience: From plan.md
- Deadline: From plan.md

**Assembly Metadata**:

- Number of sections assembled
- Total word count (sum of all sections)
- Confirmation that all sections passed gates
- Generation timestamp
- NUAA CLI version

### Step 6: Save Final Document

The AI will:

1. Create `initiatives/NNN-slug/final/[document-name]-v[VERSION].md`
2. Save assembled document using the template
3. Update plan.md with assembly metadata
4. Mark initiative as "Ready for Review"

---

## Output Generated

### Primary Output: Assembled Markdown

**File**: `initiatives/NNN-slug/final/[document-name]-v1.0.md`

- Complete document with all sections
- Professional formatting throughout
- Transitions between sections
- Table of contents
- Document metadata
- Ready for review

### Supporting Files

**Assembly Report**: `initiatives/NNN-slug/final/assembly-report.md`

```markdown
# Assembly Report: [INITIATIVE_NAME]

**Date**: [DATE]
**Status**: Success

## Sections Assembled

1. Executive Summary (Gate 1) - 450 words - ✓ Passed
2. Background (Gate 1) - 680 words - ✓ Passed
3. Program Description (Gate 2) - 1,200 words - ✓ Passed
4. Budget Justification (Gate 3) - 890 words - ✓ Passed
5. Evaluation Framework (Gate 3) - 750 words - ✓ Passed
6. Implementation Timeline (Gate 4) - 560 words - ✓ Passed
7. Conclusion (Gate 5) - 340 words - ✓ Passed

**Total**: 7 sections, 4,870 words

## Quality Checks

- ✓ All sections passed gate validation
- ✓ No placeholder markers remaining
- ✓ All dependencies satisfied
- ✓ Consistent terminology throughout
- ✓ Mission alignment verified
- ✓ References properly formatted

## Next Steps

1. Review assembled document: `final/naloxone-distribution-proposal-v1.0.md`
2. Conduct peer review with team
3. Address any feedback with section revisions
4. Re-assemble if sections change
5. Export to final format when approved
```

---

## Format Export Options

### Markdown (Default)

- Native format, fully editable
- Maintains all formatting and metadata
- Compatible with version control
- Easy to diff and track changes

### Microsoft Word (.docx)

The AI should suggest using pandoc for conversion:

```bash
pandoc initiatives/001-naloxone/final/proposal-v1.0.md \
  -o initiatives/001-naloxone/final/proposal-v1.0.docx \
  --reference-doc=nuaa-kit/templates/nuaa-word-template.docx
```

**Word Template Requirements**:

- NUAA branding and logo
- Standard heading styles
- Consistent fonts and spacing
- Header/footer with page numbers

### PDF

The AI should suggest using pandoc with LaTeX:

```bash
pandoc initiatives/001-naloxone/final/proposal-v1.0.md \
  -o initiatives/001-naloxone/final/proposal-v1.0.pdf \
  --pdf-engine=xelatex \
  --template=nuaa-kit/templates/nuaa-pdf-template.tex
```

**PDF Template Requirements**:

- Professional appearance
- NUAA branding
- Page numbers and headers
- Proper typography

---

## Validation & Quality Checks

Before assembly, the AI performs these checks:

### Completeness Check

```python
def check_completeness(plan):
    incomplete_sections = []
    for section in plan.sections:
        if section.status != "Passed":
            incomplete_sections.append({
                "name": section.name,
                "status": section.status,
                "blocker": section.blocker
            })
    return incomplete_sections
```

### Consistency Check

```python
def check_consistency(sections):
    issues = []

    # Extract all numbers/dates/facts mentioned
    mentioned_facts = {}
    for section in sections:
        facts = extract_facts(section.content)
        for fact in facts:
            if fact.key in mentioned_facts:
                if fact.value != mentioned_facts[fact.key]:
                    issues.append({
                        "type": "inconsistency",
                        "fact": fact.key,
                        "section1": mentioned_facts[fact.key].section,
                        "value1": mentioned_facts[fact.key].value,
                        "section2": section.name,
                        "value2": fact.value
                    })
            else:
                mentioned_facts[fact.key] = fact

    return issues
```

### Placeholder Check

```python
def check_placeholders(sections):
    placeholders_found = []
    for section in sections:
        if "[PLACEHOLDER:" in section.content:
            placeholders = extract_placeholders(section.content)
            for placeholder in placeholders:
                placeholders_found.append({
                    "section": section.name,
                    "placeholder": placeholder
                })
    return placeholders_found
```

---

## Example: Successful Assembly

```
User: /nuaa.assemble

AI performs validation:
✓ All 7 sections have "Passed" status
✓ No placeholders remaining
✓ All gate validations complete
✓ Dependencies satisfied

AI loads sections in order:
1. Executive Summary (450 words)
2. Background and Context (680 words)
3. Program Description (1,200 words)
4. Budget Justification (890 words)
5. Evaluation Framework (750 words)
6. Implementation Timeline (560 words)
7. Conclusion (340 words)

AI adds transitions:
- Between Background → Program Description
- Between Program Description → Budget
- Between Evaluation → Timeline
- Between Timeline → Conclusion

AI generates TOC with 7 main sections, 15 subsections

AI assembles final document:
✓ Created: initiatives/001-naloxone/final/naloxone-proposal-v1.0.md
✓ Word count: 4,870 words
✓ Sections: 7
✓ Status: Ready for Review

Assembly report saved to:
initiatives/001-naloxone/final/assembly-report.md

Next steps:
1. Review the assembled document
2. Share with team for feedback
3. Run "nuaa review" to manage feedback
4. Export to Word/PDF when approved
```

---

## Example: Failed Assembly (Incomplete Sections)

```
User: /nuaa.assemble

AI performs validation:
✗ Assembly cannot proceed - incomplete sections found

Incomplete sections:
1. Budget Justification - Status: In Progress
   - Still being drafted

2. Evaluation Framework - Status: Blocked
   - Blocked by: Budget Justification not complete

3. Timeline - Status: Not Started
   - Ready to draft but not started

Please complete these sections before assembly:
1. Complete "Budget Justification" and validate with gate-check
2. "Evaluation Framework" will unblock automatically
3. Draft and validate "Timeline"

Current progress: 4 of 7 sections complete (57%)

Run "nuaa status" to see full initiative status.
```

---

## Example: Failed Assembly (Placeholders Found)

```
User: /nuaa.assemble

AI performs validation:
✓ All 7 sections have "Passed" status
✗ Assembly cannot proceed - placeholders found

Placeholders detected:
1. Program Description (line 45)
   - [PLACEHOLDER: Exact number of peer educators to be trained?]

2. Budget Justification (line 78)
   - [PLACEHOLDER: Final equipment cost quote?]

Please resolve these placeholders before assembly:
1. Run: nuaa draft "Program Description" --resolve
2. Run: nuaa draft "Budget Justification" --resolve

After resolving placeholders, re-validate:
1. nuaa gate-check "Program Description"
2. nuaa gate-check "Budget Justification"

Then retry assembly.
```

````

---

### Task 3: Create Review Command Template

**File**: `nuaa-kit/commands/review.md`

**Purpose**: AI agent command for managing document review workflows

**Content Structure**:

```markdown
---
description: "Manage document review process and feedback"
---

# /nuaa.review - Document Review Command

## Description

Manage the document review process, collect feedback from reviewers, track changes, and generate revision plans. This command supports both internal peer review and external stakeholder review workflows.

---

## Purpose

Review Management:

- Tracks review status and reviewer assignments
- Collects and organizes feedback by section
- Prioritizes feedback by severity
- Generates revision plans from feedback
- Maintains review history
- Supports multiple review rounds

---

## Usage

```bash
/nuaa.review [INITIATIVE] [--action ACTION]
````

**Actions**:

- `start` - Start a review round
- `add-feedback` - Add reviewer feedback
- `summarize` - Summarize all feedback
- `plan-revisions` - Create revision plan from feedback
- `complete` - Mark review round complete

**Examples**:

- `/nuaa.review --action start` - Start review for active initiative
- `/nuaa.review --action add-feedback` - Add feedback to current review
- `/nuaa.review --action summarize` - Show all feedback organized by section
- `/nuaa.review 001-naloxone --action plan-revisions` - Generate revision plan

---

## How It Works

### Action: Start Review

**Purpose**: Initialize a new review round

The AI will:

1. Check that document is assembled
2. Create review directory: `initiatives/NNN-slug/reviews/review-[N]/`
3. Generate review template for each reviewer
4. Create feedback tracking file
5. Set initiative status to "Under Review"

**Generated Files**:

**Review Tracking**: `initiatives/NNN-slug/reviews/review-1/review-tracking.md`

```markdown
# Review Round 1: [INITIATIVE_NAME]

**Started**: [DATE]
**Status**: In Progress
**Document Version**: v1.0
**Reviewers**: [To be assigned]

## Review Instructions

Please review the assembled document and provide feedback using the template below.

### What to Review

- **Content accuracy**: Are facts, figures, and citations correct?
- **Mission alignment**: Does content reflect NUAA principles?
- **Clarity**: Is writing clear and accessible?
- **Completeness**: Is anything missing or unclear?
- **Evidence**: Are claims well-supported?

### How to Provide Feedback

For each issue, please specify:

- **Section**: Which section has the issue?
- **Severity**: Critical, Major, Minor, Suggestion
- **Issue**: What is the problem?
- **Suggestion**: How to fix it?

---

## Feedback Summary

| Section             | Critical | Major | Minor | Suggestions | Total |
| ------------------- | -------- | ----- | ----- | ----------- | ----- |
| Executive Summary   | 0        | 0     | 0     | 0           | 0     |
| Background          | 0        | 0     | 0     | 0           | 0     |
| Program Description | 0        | 0     | 0     | 0           | 0     |
| ...                 | ...      | ...   | ...   | ...         | ...   |

**Total Feedback Items**: 0

---

## Reviewer Status

| Reviewer | Role                | Assigned | Completed | Status  |
| -------- | ------------------- | -------- | --------- | ------- |
| [Name]   | Program Manager     | [DATE]   | -         | Pending |
| [Name]   | Executive Director  | [DATE]   | -         | Pending |
| [Name]   | Peer Representative | [DATE]   | -         | Pending |
```

**Reviewer Template**: `initiatives/NNN-slug/reviews/review-1/feedback-template.md`

```markdown
# Feedback Template

**Reviewer**: [Your Name]
**Role**: [Your Role]
**Date**: [DATE]
**Document**: [INITIATIVE_NAME] v1.0

---

## Feedback Items

### Item 1

**Section**: [Section Name]
**Severity**: [Critical | Major | Minor | Suggestion]
**Line/Location**: [Approximate location in section]
**Issue**: [Describe the problem]
**Suggestion**: [How to address it]

---

### Item 2

[Continue for each feedback item...]

---

## Overall Assessment

**Strengths**:

- [What the document does well]
- [Positive aspects]

**Areas for Improvement**:

- [Key issues to address]
- [Suggestions for enhancement]

**Recommendation**:

- [ ] Approve as-is
- [ ] Approve with minor revisions
- [ ] Requires major revisions
- [ ] Not ready - significant changes needed
```

---

### Action: Add Feedback

**Purpose**: Record reviewer feedback systematically

The AI will:

1. Ask for feedback items interactively
2. Organize feedback by section and severity
3. Update review tracking file
4. Highlight critical/major issues
5. Track which reviewer provided which feedback

**Interactive Feedback Collection**:

```
AI: Let's collect feedback. For each item, I'll ask for details.

AI: Feedback Item 1
Section name?
User: Program Description

AI: Severity? (Critical/Major/Minor/Suggestion)
User: Major

AI: What's the issue?
User: The number of peer educators (20) doesn't match the budget section (25)

AI: Suggested fix?
User: Verify correct number and update both sections for consistency

AI: ✓ Recorded. Add another item? (y/n)
User: y

[Continues until user says 'n']

AI: Summary:
- 1 Major issue recorded in Program Description
- Issue: Inconsistency in peer educator numbers

Feedback saved to: initiatives/001-naloxone/reviews/review-1/feedback-jane-smith.md

Run /nuaa.review --action summarize to see all feedback organized.
```

---

### Action: Summarize Feedback

**Purpose**: Organize all feedback for review

The AI will:

1. Read all feedback files from current review
2. Group feedback by section
3. Sort by severity (Critical → Major → Minor → Suggestion)
4. Identify patterns (multiple reviewers mentioning same issue)
5. Generate summary report

**Summary Report Format**:

```markdown
# Feedback Summary: Review Round 1

**Initiative**: 001-naloxone-distribution
**Document**: Naloxone Distribution Proposal v1.0
**Review Started**: 2025-10-15
**Reviewers**: 3
**Total Feedback Items**: 12

---

## Critical Issues (2)

### 1. Budget-Program Mismatch

**Section**: Program Description, Budget Justification
**Reviewers**: Jane Smith (Program Manager), Bob Jones (Finance)
**Issue**: Inconsistent peer educator numbers - Program Description says 20, Budget says 25
**Suggested Fix**: Verify actual staffing plan and update both sections
**Priority**: Must fix before approval

### 2. Missing Evaluation Data

**Section**: Evaluation Framework
**Reviewers**: Alice Chen (Evaluation Lead)
**Issue**: No clear data collection timeline specified
**Suggested Fix**: Add specific dates/frequencies for data collection activities
**Priority**: Must fix before approval

---

## Major Issues (4)

### 3. Evidence Gap - Peer Model

**Section**: Program Description
**Reviewers**: Jane Smith
**Issue**: Claims about peer-led effectiveness lack peer-reviewed citations
**Suggested Fix**: Add 2-3 citations from recent literature on peer-led naloxone programs
**Priority**: Should fix for stronger proposal

[Continue for all major issues...]

---

## Minor Issues (3)

[Continue for minor issues...]

---

## Suggestions (3)

[Continue for suggestions...]

---

## Feedback by Section

### Executive Summary

- No feedback items

### Background and Context

- 1 Minor: Consider adding NSW-specific overdose statistics
- 1 Suggestion: Could mention recent policy changes

### Program Description

- 1 Critical: Peer educator number mismatch
- 1 Major: Evidence gap for peer model
- 2 Minor: [details...]

[Continue for all sections...]

---

## Next Steps

1. Address 2 Critical issues immediately
2. Address 4 Major issues for quality improvement
3. Consider 3 Minor issues if time allows
4. Review 3 Suggestions for enhancement

Run: /nuaa.review --action plan-revisions
This will generate a detailed revision plan addressing all feedback.
```

---

### Action: Plan Revisions

**Purpose**: Create actionable revision plan from feedback

The AI will:

1. Read summarized feedback
2. Group related feedback items
3. Identify which sections need revision
4. Estimate revision scope (minor tweaks vs. major rewrite)
5. Generate step-by-step revision plan

**Revision Plan Format**:

````markdown
# Revision Plan: Review Round 1

**Initiative**: 001-naloxone-distribution
**Based on**: 12 feedback items from 3 reviewers
**Estimated effort**: 6-8 hours

---

## Revision Priority Order

### Phase 1: Critical Issues (Must Fix)

**Issue 1: Budget-Program Mismatch**

- **Sections to revise**: Program Description, Budget Justification
- **Action**: Verify actual staffing plan with team
- **Changes needed**: Update peer educator number in both sections
- **Estimated time**: 30 minutes
- **Command**: `nuaa revise "Program Description" --type consistency`
- **Command**: `nuaa revise "Budget Justification" --type consistency`

**Issue 2: Missing Evaluation Data**

- **Sections to revise**: Evaluation Framework
- **Action**: Add data collection timeline
- **Changes needed**: Specify dates and frequencies for each data collection activity
- **Estimated time**: 1 hour
- **Command**: `nuaa revise "Evaluation Framework" --type feedback --feedback "Add data collection timeline"`

---

### Phase 2: Major Issues (Should Fix)

**Issue 3: Evidence Gap - Peer Model**

- **Sections to revise**: Program Description
- **Action**: Literature review for peer-led naloxone citations
- **Changes needed**: Add 2-3 peer-reviewed citations
- **Estimated time**: 2 hours (including research)
- **Command**: `nuaa revise "Program Description" --type enhancement`

[Continue for all major issues...]

---

### Phase 3: Minor Issues (If Time Allows)

[Continue for minor issues...]

---

### Phase 4: Suggestions (Optional Enhancements)

[Continue for suggestions...]

---

## Revision Workflow

1. **Start with Phase 1** (Critical issues)

   - These block approval
   - Must be addressed before re-assembly

2. **Move to Phase 2** (Major issues)

   - These significantly improve quality
   - Recommended before submission

3. **Phase 3 & 4** (Minor/Suggestions)

   - Time permitting
   - Can be deferred to future versions

4. **After revisions**:
   - Re-run gate-check for each revised section
   - Re-assemble document with: `/nuaa.assemble`
   - Start new review round if needed: `/nuaa.review --action start`

---

## Detailed Revision Steps

### For "Program Description" Section

**Changes needed**:

1. Update peer educator count from 20 to [CORRECT_NUMBER]
2. Add evidence citations for peer-led model
3. Ensure consistency with Budget section

**Process**:

```bash
# First, verify correct number with team
# Then revise for consistency
nuaa revise "Program Description" --type consistency

# After fixing number, enhance evidence
nuaa revise "Program Description" --type enhancement

# Validate changes
nuaa gate-check "Program Description"
```
````

[Continue with detailed steps for each section needing revision...]

````

---

### Action: Complete Review

**Purpose**: Mark review round complete and prepare for next steps

The AI will:

1. Check that revision plan exists
2. Verify critical issues have been addressed
3. Archive review files
4. Update document status
5. Suggest next steps (re-assemble, new review, or approve)

---

## Review Workflow Example

```bash
# 1. Start review after initial assembly
$ nuaa assemble
✓ Document assembled: proposal-v1.0.md

$ nuaa review --action start
✓ Review round 1 started
✓ Created reviewer templates

# 2. Team provides feedback (offline or via AI)
/nuaa.review --action add-feedback
# AI collects feedback interactively

# 3. Summarize all feedback
/nuaa.review --action summarize
# Shows 2 critical, 4 major, 3 minor, 3 suggestions

# 4. Generate revision plan
/nuaa.review --action plan-revisions
✓ Revision plan created
✓ 3 phases, estimated 6-8 hours

# 5. Execute revisions
$ nuaa revise "Program Description" --type consistency
$ nuaa revise "Budget Justification" --type consistency
$ nuaa revise "Evaluation Framework" --type feedback --feedback "Add timeline"
# Continue for all critical and major issues...

# 6. Re-validate and re-assemble
$ nuaa gate-check "Program Description"
✓ PASS
$ nuaa gate-check "Budget Justification"
✓ PASS
$ nuaa gate-check "Evaluation Framework"
✓ PASS

$ nuaa assemble
✓ Document re-assembled: proposal-v1.1.md

# 7. Complete review
/nuaa.review --action complete
✓ Review round 1 complete
✓ All critical issues addressed
✓ Document ready for approval or next review round
````

````

---

### Task 4: Create Export Script (Bash)

**File**: `scripts/bash/export-document.sh`

**Purpose**: Export assembled documents to Word/PDF formats

**Key Functions**:

```bash
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

    # Find latest version markdown file
    local latest=$(ls -t "$final_dir"/*.md 2>/dev/null | head -n 1)

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
````

---

### Task 5: Create Export Script (PowerShell)

**File**: `scripts/powershell/export-document.ps1`

**Purpose**: PowerShell mirror of bash export script

**Key Functions**:

```powershell
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
```

---

### Task 6: Integrate Assembly & Review into CLI

**File**: `src/nuaa_cli/__init__.py`

**Add new commands**:

```python
@app.command()
def assemble(
    initiative: Optional[str] = typer.Argument(None, help="Initiative to assemble (uses most recent if not specified)"),
    output_format: str = typer.Option("markdown", "--format", help="Output format: markdown, docx, pdf, html"),
):
    """Assemble validated sections into final document."""
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
        raise typer.Exit(1)

    # Pre-assembly validation would go here
    # For now, show instructions for AI

    final_dir = Path(f"initiatives/{initiative}/final")
    final_dir.mkdir(exist_ok=True)

    console.print(Panel(
        f"[green]✓[/green] Initiative: [cyan]{initiative}[/cyan]\n"
        f"[green]✓[/green] Plan: [cyan]{plan_file}[/cyan]\n"
        f"[green]✓[/green] Output directory: [cyan]{final_dir}[/cyan]\n\n"
        f"[bold]AI will:[/bold]\n"
        f"  • Validate all sections have 'Passed' status\n"
        f"  • Check for remaining placeholders\n"
        f"  • Load all sections in proper order\n"
        f"  • Add transitions between sections\n"
        f"  • Generate table of contents\n"
        f"  • Create final document in {final_dir}/\n\n"
        f"[bold]Have AI run:[/bold] [cyan]/nuaa.assemble[/cyan]",
        title="Ready to Assemble",
        border_style="green"
    ))


@app.command()
def review(
    initiative: Optional[str] = typer.Argument(None, help="Initiative to review (uses most recent if not specified)"),
    action: str = typer.Option("start", "--action", help="Action: start, add-feedback, summarize, plan-revisions, complete"),
):
    """Manage document review process."""
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

    # Check final document exists (for most actions)
    if action != "start":
        final_dir = Path(f"initiatives/{initiative}/final")
        if not final_dir.exists() or not list(final_dir.glob("*.md")):
            console.print(f"[red]Error: No assembled document found[/red]")
            console.print("[yellow]Run 'nuaa assemble' first[/yellow]")
            raise typer.Exit(1)

    # Create reviews directory if needed
    reviews_dir = Path(f"initiatives/{initiative}/reviews")
    reviews_dir.mkdir(exist_ok=True)

    # Action-specific messages
    if action == "start":
        console.print(Panel(
            f"[green]✓[/green] Initiative: [cyan]{initiative}[/cyan]\n"
            f"[green]✓[/green] Reviews directory: [cyan]{reviews_dir}[/cyan]\n\n"
            f"[bold]AI will:[/bold]\n"
            f"  • Create new review round directory\n"
            f"  • Generate review tracking file\n"
            f"  • Create feedback templates for reviewers\n"
            f"  • Set initiative status to 'Under Review'\n\n"
            f"[bold]Have AI run:[/bold] [cyan]/nuaa.review --action start[/cyan]",
            title="Start Review",
            border_style="blue"
        ))

    elif action == "add-feedback":
        console.print(Panel(
            f"[green]✓[/green] Initiative: [cyan]{initiative}[/cyan]\n\n"
            f"[bold]AI will:[/bold]\n"
            f"  • Collect feedback items interactively\n"
            f"  • Organize by section and severity\n"
            f"  • Update review tracking file\n"
            f"  • Save feedback to reviewer file\n\n"
            f"[bold]Have AI run:[/bold] [cyan]/nuaa.review --action add-feedback[/cyan]",
            title="Add Feedback",
            border_style="blue"
        ))

    elif action == "summarize":
        console.print(Panel(
            f"[green]✓[/green] Initiative: [cyan]{initiative}[/cyan]\n\n"
            f"[bold]AI will:[/bold]\n"
            f"  • Read all feedback files\n"
            f"  • Group by section and severity\n"
            f"  • Identify patterns across reviewers\n"
            f"  • Generate comprehensive summary\n\n"
            f"[bold]Have AI run:[/bold] [cyan]/nuaa.review --action summarize[/cyan]",
            title="Summarize Feedback",
            border_style="blue"
        ))

    elif action == "plan-revisions":
        console.print(Panel(
            f"[green]✓[/green] Initiative: [cyan]{initiative}[/cyan]\n\n"
            f"[bold]AI will:[/bold]\n"
            f"  • Analyze all feedback\n"
            f"  • Create prioritized revision plan\n"
            f"  • Estimate revision effort\n"
            f"  • Provide step-by-step commands\n\n"
            f"[bold]Have AI run:[/bold] [cyan]/nuaa.review --action plan-revisions[/cyan]",
            title="Plan Revisions",
            border_style="blue"
        ))

    elif action == "complete":
        console.print(Panel(
            f"[green]✓[/green] Initiative: [cyan]{initiative}[/cyan]\n\n"
            f"[bold]AI will:[/bold]\n"
            f"  • Verify critical issues addressed\n"
            f"  • Archive review files\n"
            f"  • Update document status\n"
            f"  • Suggest next steps\n\n"
            f"[bold]Have AI run:[/bold] [cyan]/nuaa.review --action complete[/cyan]",
            title="Complete Review",
            border_style="blue"
        ))

    else:
        console.print(f"[red]Error: Unknown action: {action}[/red]")
        console.print("[yellow]Valid actions: start, add-feedback, summarize, plan-revisions, complete[/yellow]")
        raise typer.Exit(1)


@app.command()
def export(
    initiative: Optional[str] = typer.Argument(None, help="Initiative to export (uses most recent if not specified)"),
    output_format: str = typer.Option("docx", "--format", help="Export format: docx, pdf, html"),
    output: Optional[str] = typer.Option(None, "--output", help="Output filename"),
):
    """Export assembled document to Word, PDF, or HTML."""
    show_banner()

    # Check export script exists
    script_path = Path("scripts/bash/export-document.sh")
    if sys.platform == "win32":
        script_path = Path("scripts/powershell/export-document.ps1")

    if not script_path.exists():
        console.print(f"[red]Error: Export script not found: {script_path}[/red]")
        raise typer.Exit(1)

    # Build command
    cmd_args = ["--json", "--format", output_format]
    if initiative:
        cmd_args.extend(["--initiative", initiative])
    if output:
        cmd_args.extend(["--output", output])

    try:
        if sys.platform == "win32":
            result = subprocess.run(
                ["pwsh", "-File", str(script_path)] + cmd_args,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=Path.cwd()
            )
        else:
            result = subprocess.run(
                ["bash", str(script_path)] + cmd_args,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=Path.cwd()
            )

        if result.returncode != 0:
            console.print(f"[red]Error:[/red]")
            console.print(result.stderr)
            raise typer.Exit(1)

        data = json.loads(result.stdout)

        console.print(Panel(
            f"[green]✓[/green] Initiative: [cyan]{data['initiative']}[/cyan]\n"
            f"[green]✓[/green] Format: [cyan]{data['format'].upper()}[/cyan]\n"
            f"[green]✓[/green] Exported: [cyan]{data['output_file']}[/cyan]\n\n"
            f"[bold]Document ready for:[/bold]\n"
            f"  • Distribution to stakeholders\n"
            f"  • Printing and submission\n"
            f"  • Archive and record keeping",
            title="Export Complete",
            border_style="green"
        ))

    except json.JSONDecodeError:
        console.print(f"[red]Error: Could not parse export output[/red]")
        console.print(result.stdout)
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)
```

---

### Task 7: Update Documentation

**Files to Update**:

1. **nuaa-kit/README.md** - Add Phase 4 workflow section
2. **CHANGELOG.md** - Add Phase 4 entries
3. **Update version in pyproject.toml**

---

## Acceptance Criteria

Phase 4 is complete when:

### Templates & Commands

- [ ] `nuaa-kit/templates/final-document-template.md` exists with metadata structure
- [ ] `nuaa-kit/commands/assemble.md` exists with validation and assembly logic
- [ ] `nuaa-kit/commands/review.md` exists with all review actions documented
- [ ] All commands include example workflows

### Scripts

- [ ] `scripts/bash/export-document.sh` exports to DOCX/PDF/HTML
- [ ] `scripts/powershell/export-document.ps1` mirrors bash functionality
- [ ] Both scripts check for pandoc/LaTeX dependencies
- [ ] Scripts support `--json` flag

### CLI Integration

- [ ] `nuaa assemble` command validates completeness before assembly
- [ ] `nuaa review` command supports all 5 actions
- [ ] `nuaa export` command calls export scripts correctly
- [ ] All commands provide helpful error messages
- [ ] Commands update `pyproject.toml` version and `CHANGELOG.md`

### Documentation

- [ ] `nuaa-kit/README.md` includes complete assembly → review → export workflow
- [ ] Examples show multi-round review process
- [ ] Export format options documented

### Validation

- [ ] Can assemble document from validated sections
- [ ] Assembly blocks if sections incomplete
- [ ] Review workflow tracks feedback systematically
- [ ] Revision plans are actionable
- [ ] Export produces readable DOCX/PDF/HTML

---

## Post-Implementation

After Phase 4 is complete, we'll move to:

**Phase 5**: Backward Compatibility & Migration (tools for existing projects, legacy support)

---

**Ready to implement Phase 4? Let's build the assembly and review system!** 🚀
