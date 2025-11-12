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
```

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
