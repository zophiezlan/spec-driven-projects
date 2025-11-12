---
description: "Revise a drafted section based on feedback or new information"
---

# /nuaa.revise - Section Revision Command

## Description

Revise a drafted section based on feedback, placeholder resolution, consistency updates, or quality enhancement. This command makes targeted improvements to existing section drafts while maintaining document structure and preserving working content.

---

## Purpose

Section Revision:

- Resolves placeholder markers with actual information
- Addresses specific feedback from gate validation
- Updates content based on changed dependencies
- Strengthens evidence, clarity, or mission alignment
- Maintains revision history for tracking changes
- Avoids unnecessary rewrites (targeted edits only)

---

## Usage

```bash
/nuaa.revise [SECTION_NAME] [--type TYPE] [--feedback "..."]
```

**Examples**:

- `/nuaa.revise "Program Description" --type placeholder` - Resolve placeholders
- `/nuaa.revise "Budget" --type feedback --feedback "Need more detail on equipment costs"`
- `/nuaa.revise "Evaluation" --type consistency` - Update based on changed dependencies
- `/nuaa.revise "Executive Summary" --type enhancement` - Strengthen evidence and clarity

---

## Revision Types

### Type 1: Placeholder Resolution (`--type placeholder`)

**When to Use**:

- Original draft had missing information
- User has gathered the missing details
- Section contains `[PLACEHOLDER: ...]` markers

**How It Works**:

1. AI reads the current draft
2. Identifies all `[PLACEHOLDER: ...]` markers
3. For each placeholder, asks user for the information
4. Replaces placeholder with actual content
5. Ensures new content fits naturally
6. Updates revision history

**Example**:

```markdown
Before:
[PLACEHOLDER: What is the exact geographic coverage area?]

AI asks: "What is the exact geographic coverage area?"
User provides: "Sydney LGAs: City of Sydney, Inner West, Canterbury-Bankstown"

After:
The program will serve three Sydney LGAs: City of Sydney, Inner West, and Canterbury-Bankstown.
```

### Type 2: Feedback Incorporation (`--type feedback`)

**When to Use**:

- Section failed gate validation
- Reviewer provided specific feedback
- Quality criteria not fully met

**How It Works**:

1. AI reads current draft and feedback
2. Identifies specific areas to address
3. Makes targeted revisions to address feedback
4. Preserves working content
5. Re-checks against gate criteria
6. Updates revision history with feedback addressed

**Example**:

```markdown
Feedback: "Budget justification needs more detail on equipment costs"

Before:
Equipment costs total $15,000 for naloxone kits and training materials.

After:
Equipment costs total $15,000, allocated as follows:

- Naloxone nasal spray kits (500 units @ $25): $12,500
- Training materials (manuals, demonstration kits): $2,000
- Storage and distribution supplies: $500

Each kit includes two doses of naloxone, instruction card, and rescue breathing
barrier, meeting NSW Health guidelines for community distribution programs.
```

### Type 3: Consistency Update (`--type consistency`)

**When to Use**:

- Dependency sections were revised
- Specification or plan updated
- Numbers, dates, or facts changed upstream

**How It Works**:

1. AI re-reads all dependency sections
2. Identifies inconsistencies with current draft
3. Updates affected content to align
4. Checks for cascading impacts
5. Maintains internal consistency
6. Updates revision history

**Example**:

```markdown
Change in dependency: Budget revised from $500K to $450K

Before (in Budget Justification):
The program's total budget of $500,000 will be allocated across...

After:
The program's total budget of $450,000 will be allocated across...
[Plus cascading updates to percentages and calculations]
```

### Type 4: Quality Enhancement (`--type enhancement`)

**When to Use**:

- Section passed gate but could be stronger
- New evidence available
- Voluntary quality improvement
- Preparing for final review

**How It Works**:

1. AI reviews current draft critically
2. Identifies opportunities for improvement:
   - Stronger evidence citations
   - Clearer language
   - Better mission alignment
   - More compelling arguments
3. Makes selective enhancements
4. Maintains overall structure
5. Updates revision history

**Example**:

```markdown
Before:
Naloxone distribution is effective at reducing overdose deaths.

After:
Naloxone distribution through peer networks has been shown to reduce fatal
overdoses by 25-30% in comparable Australian settings (Doe et al., 2023),
with community-based programs demonstrating particularly strong outcomes
when delivered by people with lived experience (Smith & Jones, 2024).
```

---

## How It Works

### Step 1: Identify Revision Scope

Based on revision type:

- **Placeholder**: Find all `[PLACEHOLDER: ...]` markers
- **Feedback**: Parse specific feedback points
- **Consistency**: Re-read dependency sections
- **Enhancement**: Identify improvement opportunities

### Step 2: Make Targeted Revisions

The AI will:

- Make minimal necessary changes
- Preserve working content
- Maintain document structure
- Ensure natural flow
- Avoid unnecessary rewrites

### Step 3: Verify Changes

After revision:

- Check gate criteria (for feedback type)
- Verify consistency (for consistency type)
- Ensure placeholders resolved (for placeholder type)
- Confirm improvements (for enhancement type)

### Step 4: Update Metadata

The AI will:

- Update "Last Updated" date
- Add entry to Revision History
- Update status if appropriate
- Note what changed and why

---

## Revision Guidelines

### Do's

✓ Make targeted, specific changes
✓ Preserve working content
✓ Maintain document structure
✓ Document what changed in revision history
✓ Verify consistency after changes
✓ Re-check gate criteria when applicable

### Don'ts

✗ Don't rewrite entire sections unnecessarily
✗ Don't change working content without reason
✗ Don't ignore revision history
✗ Don't introduce new inconsistencies
✗ Don't skip verification steps
✗ Don't lose placeholder context

---

## Revision History Format

Each revision should add an entry:

```markdown
## Revision History

- **2024-01-15**: Initial draft created
- **2024-01-16**: Resolved 3 placeholders (geographic coverage, budget, timeline)
- **2024-01-17**: Updated per Gate 3 feedback - added equipment cost detail
- **2024-01-18**: Consistency update - aligned with revised budget ($450K)
- **2024-01-19**: Enhancement - strengthened evidence citations
```

---

## Integration with Workflow

Typical revision workflow:

1. **Draft** → Create initial section with `/nuaa.draft`
2. **Review** → Check draft, identify placeholders
3. **Resolve** → Use `/nuaa.revise --type placeholder`
4. **Validate** → Run `nuaa gate-check`
5. **Feedback** → If fails, use `/nuaa.revise --type feedback`
6. **Pass** → Move to next section or enhance
7. **Enhance** (optional) → Use `/nuaa.revise --type enhancement`

---

## Examples by Revision Type

### Example 1: Placeholder Resolution

```bash
/nuaa.revise "Target Population" --type placeholder
```

AI identifies 2 placeholders:
1. Geographic coverage → User provides: "Inner Sydney LGAs"
2. Population size → User provides: "Estimated 5,000 PWUD"

AI updates draft, removing markers and incorporating information naturally.

### Example 2: Feedback Incorporation

```bash
/nuaa.revise "Evaluation Plan" --type feedback --feedback "Missing details on data collection frequency and methods"
```

AI adds detailed data collection schedule and methodology section addressing the feedback.

### Example 3: Consistency Update

```bash
/nuaa.revise "Budget Justification" --type consistency
```

AI detects staffing model changed from 20 to 18 peer educators, updates all affected calculations and references.

### Example 4: Quality Enhancement

```bash
/nuaa.revise "Needs Statement" --type enhancement
```

AI strengthens evidence citations, adds recent statistics, improves harm reduction language alignment.

---

## Best Practices

### For Users

1. **Be specific with feedback**: Provide clear, actionable feedback points
2. **Resolve placeholders early**: Gather missing information before gate validation
3. **Check dependencies**: When revising one section, consider impacts on others
4. **Use appropriate type**: Choose revision type that matches your need
5. **Review changes**: Verify revisions achieved the intended improvement

### For AI

1. **Targeted edits**: Change only what needs changing
2. **Preserve structure**: Maintain section organization
3. **Natural integration**: New content should flow seamlessly
4. **Document changes**: Clear revision history entries
5. **Verify alignment**: Ensure changes maintain mission and gate alignment

---

## Troubleshooting

### "No placeholders found"

If `--type placeholder` but no placeholders exist:
- Section may already be complete
- Check if placeholder markers were manually removed
- Consider if different revision type needed

### "Feedback unclear"

If feedback is vague or contradictory:
- Ask user for clarification
- Suggest specific areas that might need attention
- Provide examples of what could be improved

### "Dependencies unchanged"

If `--type consistency` but no changes detected:
- Verify which sections are dependencies
- Check if changes affect this section
- May not need revision after all

### "Enhancement unclear"

If enhancement opportunities aren't obvious:
- Section may already be high quality
- Consider Gate 5 polish (formatting, completeness)
- Suggest specific areas (evidence, clarity, alignment)
