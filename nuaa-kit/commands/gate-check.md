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
```

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
