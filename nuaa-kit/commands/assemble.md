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
