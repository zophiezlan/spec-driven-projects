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
```

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

```markdown
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

[Continue with detailed steps for each section needing revision...]
```

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
```
