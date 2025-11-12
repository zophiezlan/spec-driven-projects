# /nuaa.specify - Program Specification Command

Template: See [program-specification-template.md](../templates/program-specification-template.md).

## Description

Create a high-level program specification from natural language input. This command generates the initial specification document that captures the core program idea, identifies ambiguities, and provides a foundation for detailed planning.

---

## Purpose

The Program Specification:

- Captures the high-level program concept in structured form
- Identifies target population and program scope
- Documents the evidence base and expected outcomes
- Marks ambiguities that need clarification before planning
- Ensures alignment with NUAA mission from the start
- Provides the foundation for subsequent planning and drafting

---

## Usage

```bash
/nuaa.specify <PROGRAM_DESCRIPTION>
```

**Examples**:

- `/nuaa.specify Create a peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney`
- `/nuaa.specify Develop a lived experience mentorship program for people in early recovery connecting them with long-term peer mentors`
- `/nuaa.specify Establish a mobile harm reduction van providing sterile equipment, testing, and peer support in regional NSW`

---

## Inputs Required

When you invoke this command with a program description, the AI will:

1. **Parse the description** to understand the program concept
2. **Generate a structured specification** with all required sections
3. **Identify ambiguities** and mark them with `[NEEDS CLARIFICATION: specific question]`
4. **Reference the mission constitution** to ensure initial alignment
5. **Create an initiative directory** with the spec file

---

## Output Generated

The AI will create a complete **initiatives/NNN-slug/spec.md** document containing:

### 1. Metadata

- Initiative number (auto-generated: 001, 002, 003...)
- Initiative name (slug from description)
- Created date
- Status (draft)

### 2. Program Overview

- **What**: Clear 2-3 sentence description of the program
- **Why**: The problem or need being addressed
- **Who Benefits**: Primary beneficiaries of the program

### 3. Target Population

- Demographics (age, location, characteristics)
- Specific needs or circumstances
- Estimated reach
- **MUST mark ambiguities** if not clear from description

### 4. Duration and Timeline

- Program duration (pilot, implementation, ongoing)
- Key milestones
- **MUST mark if not specified in description**

### 5. Evidence Base

- Research supporting the approach
- Local data or context
- Similar programs or precedents
- **MUST mark if specific evidence needs to be identified**

### 6. Key Activities

- 3-5 core program activities
- Service delivery approach
- Peer involvement methods

### 7. Expected Outcomes

- Short-term outcomes (immediate benefits)
- Long-term outcomes (sustained impact)
- Measurable indicators

### 8. NUAA Alignment

- How program aligns with NUAA mission
- Which ethical principles it embodies
- Connection to harm reduction values

### 9. Next Steps

- Automatic: "Run /nuaa.clarify to resolve ambiguities"
- After clarification: "Run /nuaa.plan to create implementation plan"

---

## Clarification Marker System

**CRITICAL**: The AI MUST identify ambiguities and mark them appropriately.

### Marker Format

```markdown
[NEEDS CLARIFICATION: Specific, answerable question?]
```

### Requirements

- **Maximum 5 markers** per specification
- Each marker must ask a **specific, answerable question**
- Questions should be **multiple-choice when possible**
- Focus on **high-impact ambiguities** that affect planning
- **Do NOT** mark things that are clearly implied or standard

### Examples of Good Markers

✅ **Good**: `[NEEDS CLARIFICATION: What age range? All adults (18+), young adults (18-35), or no age restriction?]`

✅ **Good**: `[NEEDS CLARIFICATION: Is this a 6-month pilot, 12-month implementation, or ongoing service?]`

✅ **Good**: `[NEEDS CLARIFICATION: Are we targeting people already engaged with health services, or harder-to-reach populations not in treatment?]`

### Examples of Bad Markers

❌ **Bad**: `[NEEDS CLARIFICATION: More details needed]` - Too vague

❌ **Bad**: `[NEEDS CLARIFICATION: How will evaluation be conducted?]` - Too detailed for this phase

❌ **Bad**: `[NEEDS CLARIFICATION: What is the budget?]` - Handled in planning phase

### Where to Place Markers

Place markers **inline** where the ambiguity exists:

```markdown
## Target Population

People who use opioids in Western Sydney, particularly those [NEEDS CLARIFICATION: Are we targeting people already engaged with health services, or harder-to-reach populations not in treatment?]

Age range: [NEEDS CLARIFICATION: What specific age range? All adults (18+), young adults (18-35), or no age restriction?]
```

---

## NUAA Principles Integration

The AI will automatically structure the specification to:

### 1. Center Lived Experience

- Identify peer leadership opportunities
- Plan for consumer participation
- Note where peer expertise is essential

### 2. Embed Harm Reduction

- Use non-judgmental language
- Emphasize meeting people where they are
- Avoid abstinence-based assumptions

### 3. Ensure Cultural Safety

- Note cultural considerations
- Identify diverse population needs
- Plan for cultural competency

### 4. Commit to Evidence

- Cite relevant research
- Reference local context
- Base on harm reduction evidence

---

## Prompt for AI Agent

When `/nuaa.specify` is invoked, use this system prompt:

```text
You are creating a Program Specification for NSW Users & AIDS Association (NUAA),
a peer-led harm reduction organization.

Your task is to:

1. PARSE the program description into a structured specification
2. GENERATE all required sections with clear, specific content
3. IDENTIFY ambiguities and mark EXACTLY those that are critical for planning
4. REFERENCE the mission constitution (memory/constitution.md) to ensure alignment
5. USE professional, accessible language that is non-judgmental and empowering

CRITICAL REQUIREMENTS:

- Mark ambiguities with: [NEEDS CLARIFICATION: specific question?]
- Maximum 5 clarification markers (prioritize the most important)
- Each marker must ask a specific, answerable question
- Prefer multiple-choice format where possible
- Focus on ambiguities that affect program scope, scale, or approach
- Do NOT mark standard details that can be determined in planning phase

STRUCTURE:
Follow the program-specification-template.md structure exactly.

TONE:
- Clear and professional
- Values-affirming (harm reduction, peer leadership, cultural safety)
- Specific and concrete (avoid vague language)
- Empowering (focus on strengths and opportunities)

EVIDENCE:
- Cite general harm reduction evidence where applicable
- Note where local data is needed
- Reference similar NUAA programs if known

MISSION ALIGNMENT:
Always check the specification against:
- Lived experience leadership
- Harm reduction principles
- Cultural safety
- Data ethics
- Evidence-based practice

If the program description contradicts harm reduction values or NUAA's mission,
flag this clearly and ask for clarification rather than proceeding.

Target audience: NUAA staff, program managers, AI planning agents
Output format: Structured markdown with clear sections and inline markers
```

---

## Example Workflow

**User**: `/nuaa.specify Create a peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney`

**AI Response**:

```text
I'll create a program specification for your naloxone distribution program.

Analyzing the description:
- Program type: Peer-led naloxone distribution
- Target: People at risk of opioid overdose
- Location: Western Sydney
- Key approach: Peer-led model

Checking mission constitution alignment:
✓ Centers lived experience (peer-led)
✓ Embodies harm reduction (naloxone = pragmatic harm reduction)
✓ Addresses health & wellbeing

Creating specification with identified ambiguities...

✓ Created initiative 001-naloxone-distribution
✓ Specification saved to initiatives/001-naloxone-distribution/spec.md
⚠ Found 4 ambiguities that need clarification

Key ambiguities identified:
1. Target age range (all adults vs. specific age group)
2. Population engagement level (in treatment vs. harder-to-reach)
3. Program duration (pilot vs. implementation)
4. Follow-up support approach (one-time vs. ongoing)

Next steps:
→ Run /nuaa.clarify to resolve these ambiguities
→ Then run /nuaa.plan to create the implementation plan

[Opens spec.md in editor for review]
```

---

## Integration with Other Commands

After `/nuaa.specify`, the natural workflow is:

1. **Review** the generated spec manually
2. **Run /nuaa.clarify** to resolve ambiguities
3. **Run /nuaa.plan** to create detailed implementation plan
4. Continue with gates and drafting phases

---

## Quality Checks

Before finalizing the specification, the AI should verify:

✓ **Program overview**: Clear what/why/who in 2-3 sentences  
✓ **Target population**: Specific demographics and needs identified  
✓ **Duration**: Timeline indicated (even if marked for clarification)  
✓ **Evidence base**: At least general references to harm reduction research  
✓ **Key activities**: 3-5 concrete activities listed  
✓ **Expected outcomes**: Both short-term and long-term outcomes  
✓ **NUAA alignment**: Explicit connection to mission/values  
✓ **Markers**: 1-5 clarification markers (not 0, not more than 5)  
✓ **Marker quality**: Each asks a specific, answerable question  
✓ **Language**: Professional, non-judgmental, empowering  
✓ **Completeness**: No [PLACEHOLDER] markers remaining  

---

## CLI Usage

In addition to the AI command, staff can use the NUAA CLI directly:

```bash
# Create a new program specification
nuaa specify "Program description here"

# Output shows:
# ✓ Created initiative 001-program-name
# ✓ Specification: initiatives/001-program-name/spec.md
# ⚠ Specification has 4 clarification markers - run 'nuaa clarify' to resolve
```

---

## Troubleshooting

**Issue**: Too many clarification markers (more than 5)

**Solution**: The AI should prioritize the 5 most critical ambiguities that affect program scope, scale, or approach. Other details can be determined in the planning phase.

**Issue**: No clarification markers

**Solution**: The AI should carefully review the description. There are usually some ambiguities around target population specifics, duration, or implementation approach. If truly none exist, that's fine, but rare.

**Issue**: Markers are too vague

**Solution**: Each marker should ask a specific question with clear answer options. Rephrase vague markers as multiple-choice questions.

---

## Tips for Best Results

1. **Be specific in descriptions**: The more detail in the input, the fewer ambiguities
2. **Review the spec carefully**: The AI may make assumptions that need adjustment
3. **Don't skip clarification**: Resolving ambiguities now saves time in planning
4. **Check mission alignment**: Ensure the program fits NUAA's values and capacity
5. **Keep it high-level**: Don't worry about detailed implementation yet
6. **Focus on outcomes**: What will change for participants and community?

---

## Support & Resources

**Questions?** Contact NUAA management for guidance on program concepts and organizational fit.

**Related Templates**:

- `program-specification-template.md` - Template this command fills out

**Related Commands**:

- `/nuaa.mission` - View or update mission constitution
- `/nuaa.clarify` - Resolve specification ambiguities
- `/nuaa.plan` - Create implementation plan from specification

---

**This command establishes the foundation for all subsequent planning and drafting work, ensuring clarity and mission alignment from the start.**
