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
