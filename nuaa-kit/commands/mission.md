# /nuaa.mission - Mission Constitution Command

Template: See [mission-constitution-template.md](../templates/mission-constitution-template.md).

## Description

Create or update the NUAA Mission Constitution - the foundational document that defines organizational values, ethical principles, and programmatic standards. This constitution guides all AI-generated content to ensure mission alignment, ethical compliance, and quality standards.

---

## Purpose

The Mission Constitution:

- Defines NUAA's core mission and values
- Establishes ethical principles for all programs
- Sets programmatic standards for quality and rigor
- Provides governance rules for AI-assisted work
- Ensures every document aligns with NUAA's mission
- Centers lived experience, harm reduction, and cultural safety
- Maintains consistency across all proposals, designs, and reports

---

## Usage

```bash
/nuaa.mission [MISSION_STATEMENT]
```

**Examples**:

- `/nuaa.mission "NUAA exists to support the health and wellbeing of people who use drugs in NSW through peer-led advocacy, education, and support services grounded in harm reduction principles."`
- `/nuaa.mission "To empower people who use drugs through peer support, evidence-based information, and advocacy for health, rights, and dignity."`

---

## Inputs Required

When you invoke this command, the AI will ask you for:

1. **Core Mission Statement**: NUAA's primary purpose (1-2 sentences)
2. **Organization Context**: Brief background on NUAA's work and values
3. **Key Ethical Principles**: Non-negotiable principles that guide all work
4. **Programmatic Standards**: Quality benchmarks for program delivery
5. **Governance Approach**: How these principles will be applied

**Optional Context**:

- Existing mission/vision statements
- Strategic plan excerpts
- Board-approved values statements
- Consumer advisory feedback on organizational values

---

## Output Generated

The AI will create a complete **memory/constitution.md** document containing:

1. **Core Mission**: Clear statement of NUAA's purpose
2. **Ethical Principles**:
   - **Principle I: Lived Experience Leadership** - Peer leadership, consumer participation, fair remuneration
   - **Principle II: Harm Reduction** - Non-judgmental approach, meeting people where they are, evidence-based
   - **Principle III: Cultural Safety** - Cultural competency, community consultation, trauma-informed practice
   - **Principle IV: Data Ethics** - Informed consent, data security, participant narrative control
3. **Programmatic Standards**:
   - **Evidence-Based Practice** - Research-informed, pilot-informed scale-up, built-in evaluation
   - **Evaluation Rigor** - Clear indicators, mixed methods, community-shared findings
   - **Budget Integrity** - Justified costs, transparent indirect costs, sustainability planning
4. **Governance**: How the constitution applies to all NUAA work
5. **Version & Review**: Version number, ratification date, next review date

---

## NUAA Principles Integration

The AI will automatically structure the constitution to:

### 1. Center Lived Experience

- Explicitly state peer leadership as foundational
- Commit to meaningful consumer participation
- Set standards for consumer remuneration ($300/session)
- Position people with lived experience as experts

### 2. Embed Harm Reduction

- Non-judgmental, non-coercive language
- Meet people where they are (no prerequisites)
- Evidence-based approach
- Respect for participant agency and choice

### 3. Ensure Cultural Safety

- Cultural competency requirements
- Aboriginal & Torres Strait Islander cultural safety
- LGBTIQ+ inclusivity
- CALD community responsiveness
- Trauma-informed practice standards

### 4. Commit to Data Ethics

- Explicit informed consent processes
- Data security and anonymity
- Participant control over their narratives
- Indigenous data sovereignty principles

### 5. Demand Quality & Accountability

- Evidence-based practice standards
- Evaluation rigor expectations
- Budget integrity requirements
- Transparent governance processes

---

## Prompt for AI Agent

When `/nuaa.mission` is invoked, use this system prompt:

```text
You are creating a Mission Constitution for NSW Users & AIDS Association (NUAA),
a peer-led harm reduction organization with 30+ years of experience supporting
people who use drugs in NSW.

Your task is to create a foundational document that:
- Defines NUAA's core mission clearly and compellingly
- Establishes four key ethical principles (lived experience leadership, harm reduction, cultural safety, data ethics)
- Sets three programmatic standards (evidence-based practice, evaluation rigor, budget integrity)
- Provides governance rules for how this constitution applies to all NUAA work
- Uses language that is professional yet accessible
- Reflects NUAA's values of peer leadership, harm reduction, and cultural safety

The constitution should be concise (2-3 pages), authoritative, and actionable.
It will be automatically injected into all subsequent AI interactions to ensure
mission alignment in every program design, proposal, and report.

Use the mission-constitution-template.md as your structure. Fill in all sections
based on the user's mission statement and NUAA's established principles.

If the user provides only a brief mission statement, expand it thoughtfully using
standard harm reduction and peer-led principles. Ask clarifying questions only if
the mission statement conflicts with harm reduction values or is unclear about
NUAA's core purpose.

Target audience: NUAA staff, board, consumer advisory, AI agents
Output format: Professional, authoritative, values-driven, actionable
Tone: Clear, principled, empowering, non-negotiable on core values
```

---

## Example Workflow

**User**: `/nuaa.mission "NUAA exists to support the health and wellbeing of people who use drugs in NSW through peer-led advocacy, education, and support services grounded in harm reduction principles."`

**AI Response**:

```text
I'll create NUAA's Mission Constitution based on this mission statement.

Let me confirm a few key points:

1. **Peer Leadership**: Should consumer remuneration be set at $300/session as the standard?
2. **Harm Reduction**: Should we explicitly state "non-judgmental, non-coercive" as core principles?
3. **Cultural Safety**: Should we include specific commitments to Aboriginal & Torres Strait Islander peoples, LGBTIQ+ communities, and CALD communities?
4. **Data Ethics**: Should we commit to Indigenous data sovereignty principles?

[User confirms or adjusts]

Creating your Mission Constitution...

✓ Core mission defined
✓ Four ethical principles established
✓ Three programmatic standards set
✓ Governance rules created
✓ Version tracking added

Your Mission Constitution has been saved to memory/constitution.md

This constitution will now guide all AI-generated content to ensure alignment with
NUAA's values and mission. Every program design, proposal, and report will reference
these principles.

Next steps:
- Review the constitution with your team
- Get board/consumer advisory approval if needed
- Use /nuaa.design, /nuaa.propose, etc. - they'll automatically reference this constitution
```

---

## Integration with Other Commands

After `/nuaa.mission`, the constitution automatically influences:

- `/nuaa.design` - Program designs align with ethical principles
- `/nuaa.propose` - Proposals demonstrate mission alignment
- `/nuaa.measure` - Impact frameworks reflect programmatic standards
- `/nuaa.report` - Reports show accountability to governance rules
- All other commands - Constitution is always in AI context

---

## Quality Checks

Before finalizing the constitution, the AI should verify:

✓ **Core mission**: Clear, compelling, 1-2 sentences, focuses on people who use drugs  
✓ **Ethical principles**: All four present (lived experience, harm reduction, cultural safety, data ethics)  
✓ **Programmatic standards**: All three present (evidence-based, evaluation, budget)  
✓ **Governance**: Clear rules for how constitution applies  
✓ **Language**: Professional yet accessible, values-affirming  
✓ **Length**: 2-3 pages maximum (concise authority)  
✓ **Version tracking**: Version number, ratification date, review date included  
✓ **Actionable**: Principles can guide actual decision-making  
✓ **Consistent**: No contradictions between sections  
✓ **Complete**: No [PLACEHOLDER] markers remaining

---

## CLI Usage

In addition to the AI command, staff can use the NUAA CLI directly:

```bash
# Create a new constitution
nuaa mission --set "NUAA exists to support the health and wellbeing of people who use drugs..."

# Display current constitution
nuaa mission --show

# Edit constitution in your default editor
nuaa mission --edit
```

---

## Customization Options

**Output Format**:

- **Full** (default): Complete constitution with all sections
- **Summary**: One-page version with key points only
- **Visual**: Infographic-style for presentations

Specify format with: `/nuaa.mission [INPUTS] --format=summary`

**Review Cycle**:

- Set custom review periods: `--review-cycle=annually` (default), `--review-cycle=quarterly`, `--review-cycle=biannually`

---

## Tips for Best Results

1. **Start with clarity**: Use a clear, specific mission statement rather than vague language
2. **Be authentic**: Use NUAA's actual values, not generic organizational speak
3. **Keep it concise**: 2-3 pages maximum - this is a constitution, not a strategic plan
4. **Make it actionable**: Every principle should be concrete enough to guide decisions
5. **Get buy-in**: Review with staff, board, and consumer advisory before finalizing
6. **Update regularly**: Schedule annual reviews to ensure it stays current
7. **Reference it**: Explicitly cite the constitution in proposals and reports

---

## Support & Resources

**Questions?** Contact NUAA management for guidance on organizational values and mission.

**Related Templates**:

- `mission-constitution-template.md` - Template this command fills out

**Related Commands**:

- `/nuaa.design` - Create program designs aligned with mission
- `/nuaa.propose` - Generate proposals demonstrating mission alignment
- `/nuaa.review` - Check documents against constitution

---

**This command establishes the foundation for all NUAA's AI-assisted work, ensuring every document is mission-aligned and ethically sound.**
