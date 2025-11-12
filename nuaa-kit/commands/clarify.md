# /nuaa.clarify - Clarification Command

## Description

Resolve ambiguities in a program specification through interactive questions and answers. This command finds all `[NEEDS CLARIFICATION: ...]` markers in the specification, presents them as structured questions with suggested options, and updates the spec with user-provided answers.

---

## Purpose

The Clarification Process:

- Identifies all ambiguities marked in the specification
- Presents each as a clear, structured question
- Provides suggested answer options with implications
- Captures user decisions in context
- Updates the specification with resolved information
- Removes clarification markers to indicate completion
- Ensures the specification is ready for planning

---

## Usage

```bash
/nuaa.clarify [INITIATIVE]
```

**Examples**:

- `/nuaa.clarify` - Clarify the active/most recent initiative
- `/nuaa.clarify 001-naloxone-distribution` - Clarify a specific initiative

---

## How It Works

### Step 1: Load Specification

The AI will:
1. Identify the initiative to clarify (from argument or active initiative)
2. Read `initiatives/NNN-slug/spec.md`
3. Scan for all `[NEEDS CLARIFICATION: ...]` markers
4. Extract the question text from each marker

### Step 2: Present Questions

For each clarification marker, the AI will present:

**Question Format**:

```markdown
## Question N: [Short Title]

**Context**: [Section name] (line X of spec.md)
**What we need to know**: [The actual question from the marker]

**Suggested Answers**:
| Option | Answer | Implications |
|--------|--------|--------------|
| A | [Answer option 1] | [What this choice means for the program] |
| B | [Answer option 2] | [What this choice means for the program] |
| C | [Answer option 3] | [What this choice means for the program] |
| Custom | Your own answer | [Provide your specific answer] |

**Your choice**: [Wait for user input]
```

### Step 3: Collect Answers

The AI will:
- Present questions one at a time
- Wait for user to select an option (A, B, C, Custom)
- If Custom selected, ask for specific text
- Provide brief confirmation and any implications
- Move to the next question

### Step 4: Update Specification

After all questions are answered, the AI will:
1. Replace each `[NEEDS CLARIFICATION: ...]` marker with the user's answer
2. Ensure the answer reads naturally in context
3. Preserve all other specification content
4. Save the updated spec.md
5. Confirm completion

---

## Question Presentation Guidelines

### Context Information

Each question should include:
- **Section name**: Where in the spec this appears
- **Line number** (optional): Helps users locate if reviewing in editor
- **Why it matters**: Brief explanation of how this affects planning

### Answer Options

**Good options are**:
- ✅ Specific and actionable
- ✅ Mutually exclusive
- ✅ Cover the most likely scenarios
- ✅ Include implications that help decision-making

**Poor options are**:
- ❌ Vague or overlapping
- ❌ Too many (more than 4 including Custom)
- ❌ Missing implications
- ❌ Don't actually resolve the ambiguity

### Implications

Each answer option should explain:
- What this choice means for program scope or scale
- Resource implications (if significant)
- Alignment with NUAA mission/values
- Any risks or considerations

**Example Implications**:

| Option | Answer | Implications |
|--------|--------|--------------|
| A | All adults (18+) | Broadest reach; simpler eligibility; may need age-specific materials; aligns with NUAA's inclusive approach |
| B | Young adults (18-35) | Focused on higher-risk demographic; peer educators same age range; easier to build cohesive group; may miss older people who use drugs |
| C | No age restriction | Most inclusive; requires diverse peer educator cohort; aligns strongly with harm reduction values; more complex logistics |

---

## Prompt for AI Agent

When `/nuaa.clarify` is invoked, use this system prompt:

```text
You are facilitating clarification of a NUAA program specification.

Your task is to:

1. FIND all [NEEDS CLARIFICATION: ...] markers in the spec
2. PRESENT each as a structured question with clear options
3. WAIT for the user to provide an answer
4. UPDATE the spec by replacing the marker with the answer
5. CONFIRM completion when all ambiguities are resolved

QUESTION PRESENTATION:

For each clarification marker, create a structured question that includes:
- Clear context (what section, why it matters)
- 2-4 answer options (including "Custom")
- Implications for each option
- Professional, neutral tone

ANSWER OPTIONS:

Generate options that are:
- Specific and actionable
- Aligned with NUAA values (harm reduction, peer leadership, cultural safety)
- Based on typical program approaches in the NGO sector
- Realistic given NUAA's capacity and mission

IMPLICATIONS:

For each option, explain:
- How it affects program scope, scale, or approach
- Alignment with mission/values
- Resource or capacity considerations
- Any risks or benefits

UPDATING THE SPEC:

When replacing markers:
- Ensure the answer reads naturally in the sentence
- Preserve the rest of the specification exactly
- Remove the [NEEDS CLARIFICATION: ...] marker completely
- Maintain markdown formatting

TONE:
- Professional and helpful
- Non-judgmental about any answer choice
- Clear about implications without being prescriptive
- Supportive of user decision-making

MISSION ALIGNMENT:
Always frame options and implications through the lens of:
- Lived experience leadership
- Harm reduction principles
- Cultural safety
- Evidence-based practice
- NUAA's capacity and strengths

If a user's answer conflicts with harm reduction values or NUAA's mission,
gently note this and ask if they'd like to reconsider.

Target audience: NUAA staff, program managers
Output format: Structured markdown tables with clear questions and options
```

---

## Example Workflow

**User**: `/nuaa.clarify`

**AI Response**:

```text
I'll help clarify the specification for initiative 001-naloxone-distribution.

Reading spec.md...
Found 4 ambiguities to resolve.

Let's work through each one:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Question 1: Target Age Range

**Context**: Target Population section (spec.md line 28)
**What we need to know**: What specific age range should this program target?

**Suggested Answers**:
| Option | Answer | Implications |
|--------|--------|--------------|
| A | All adults (18+) | Broadest reach; simpler eligibility; may need age-specific materials; aligns with NUAA's inclusive approach |
| B | Young adults (18-35) | Focused on higher-risk demographic; peer educators same age range; easier to build cohesive group |
| C | Older adults (35+) | Addresses underserved population; different training needs; peer educators with more life experience |
| D | No age restriction | Most inclusive; requires diverse peer educator cohort; aligns strongly with harm reduction values |
| Custom | Your own answer | Provide your specific age range |

**Your choice**: [User types: B]

✓ Selected: Young adults (18-35)

This focuses the program on a higher-risk demographic and allows for age-matched
peer educators, which often increases program effectiveness and participant comfort.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Question 2: Population Engagement Level

**Context**: Target Population section (spec.md line 30)
**What we need to know**: Are we targeting people already engaged with health 
services, or harder-to-reach populations not in treatment?

**Suggested Answers**:
| Option | Answer | Implications |
|--------|--------|--------------|
| A | People in treatment programs | Easier to reach; existing partnerships; established access points; may miss highest-risk people |
| B | Harder-to-reach populations | Aligns with NUAA mission; higher impact potential; requires street outreach; more resource-intensive |
| C | Both populations | Broadest reach; more complex logistics; requires different engagement strategies |
| Custom | Your own answer | Describe your target population approach |

**Your choice**: [User types: B]

✓ Selected: Harder-to-reach populations not in treatment

This aligns strongly with NUAA's mission and harm reduction values by reaching
people who are often excluded from traditional health services.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Questions 3 and 4 continue in same format...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

All questions answered. Updating specification...

✓ Replaced 4 clarification markers
✓ Specification updated
✓ All ambiguities resolved

Updated specification saved to: initiatives/001-naloxone-distribution/spec.md

Next steps:
→ Review the updated specification
→ Run /nuaa.plan to create the implementation plan
```

---

## Integration with Other Commands

The clarification workflow fits into the larger process:

1. **Before clarify**: `/nuaa.specify` creates spec with markers
2. **Clarify**: This command resolves ambiguities
3. **After clarify**: `/nuaa.plan` creates implementation plan

---

## Quality Checks

Before finalizing the clarification, the AI should verify:

✓ **All markers found**: Every `[NEEDS CLARIFICATION: ...]` marker identified  
✓ **Clear questions**: Each question is specific and answerable  
✓ **Good options**: 2-4 options plus Custom for each question  
✓ **Implications provided**: Each option includes clear implications  
✓ **Answers captured**: User selections are recorded  
✓ **Natural reading**: Answers flow naturally in the spec  
✓ **Markers removed**: No `[NEEDS CLARIFICATION]` markers remain  
✓ **Spec preserved**: All other content unchanged  
✓ **File saved**: Updated spec.md written to disk  

---

## CLI Usage

In addition to the AI command, staff can use the NUAA CLI directly:

```bash
# Clarify the active/most recent initiative
nuaa clarify

# Clarify a specific initiative
nuaa clarify 001-naloxone-distribution

# Output shows:
# Found 4 ambiguities to resolve
# [Interactive questions...]
# ✓ Updated specification
# ✓ All ambiguities resolved
# → Next: Run 'nuaa plan' to create implementation plan
```

---

## Handling Edge Cases

### No Clarification Markers

If the spec has no markers:

```text
No ambiguities found in specification.
The spec is ready for planning.

→ Run /nuaa.plan to create the implementation plan
```

### Invalid Initiative

If the initiative doesn't exist:

```text
Error: Initiative not found.

Available initiatives:
- 001-naloxone-distribution
- 002-peer-mentorship

Specify which to clarify: /nuaa.clarify 001-naloxone-distribution
```

### Custom Answer Handling

When user selects "Custom":

```text
You selected: Custom

Please provide your specific answer:
[User types their answer]

✓ Recorded: [User's answer]

[Shows implications if relevant, then continues to next question]
```

---

## Tips for Best Results

1. **Read questions carefully**: Consider implications before answering
2. **Choose Custom when needed**: Don't force-fit into predefined options
3. **Think about capacity**: Consider NUAA's resources and strengths
4. **Stay mission-aligned**: Ensure choices align with harm reduction values
5. **Review the updated spec**: Check that answers read naturally
6. **Document reasoning**: Note why particular choices were made

---

## Support & Resources

**Questions?** Contact NUAA management if you're uncertain about program direction or capacity.

**Related Commands**:

- `/nuaa.specify` - Create initial program specification
- `/nuaa.plan` - Create implementation plan from specification
- `/nuaa.mission` - Review mission constitution for guidance

---

**This command ensures all critical ambiguities are resolved before planning begins, reducing AI guesswork and increasing accuracy in subsequent phases.**
