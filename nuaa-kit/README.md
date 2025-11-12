# NUAA Kit - AI-Assisted Project Management for NUAA

## Overview

NUAA Kit is a specialized adaptation of Spec-Driven Development methodology designed specifically for NSW Users and AIDS Association. It transforms program design, proposal writing, and impact measurement into systematic, AI-assisted workflows integrated with Microsoft 365.

## Quick Start (Deploy in Weeks)

### Phase 1: Core Setup (Week 1)

1. Install dependencies
2. Configure Microsoft 365 integration
3. Import NUAA-specific templates
4. Train staff on first command: `/nuaa.design`

### Phase 2: Initial Use (Week 2-3)

- Create first program design using logic model generator
- Generate proposal for upcoming funding opportunity
- Test impact measurement framework

### Phase 3: Iteration (Week 4+)

- Refine based on staff feedback
- Expand to additional commands
- Full Microsoft 365 automation deployment

## Mission Constitution - The Foundation

### What is the Mission Constitution?

The **Mission Constitution** is NUAA's foundational document that defines organizational values, ethical principles, and programmatic standards. It ensures every program design, proposal, and report aligns with NUAA's mission and ethics.

Think of it as NUAA's "organizational DNA" - it guides all AI-generated content to reflect your values:

- **Core Mission**: What NUAA exists to do
- **Ethical Principles**: Non-negotiable values (lived experience leadership, harm reduction, cultural safety, data ethics)
- **Programmatic Standards**: Quality benchmarks (evidence-based practice, evaluation rigor, budget integrity)
- **Governance**: How these principles apply to all NUAA work

### Why Does It Matter?

The constitution ensures that:

- Every document reflects NUAA's commitment to peer leadership and harm reduction
- AI tools don't "hallucinate" content that conflicts with NUAA's values
- Proposals consistently demonstrate mission alignment to funders
- Program designs automatically embed ethical principles
- Quality standards are maintained across all deliverables

**In practical terms**: Once you create your constitution, every `/nuaa.design`, `/nuaa.propose`, and other command will automatically reference it - ensuring consistency and mission alignment without extra effort.

### How to Create Your Mission Constitution

#### Option 1: Using the CLI

```bash
# Create a new constitution with your mission statement
nuaa mission --set "NUAA exists to support the health and wellbeing of people who use drugs in NSW through peer-led advocacy, education, and support services grounded in harm reduction principles."

# View your current constitution
nuaa mission --show

# Edit your constitution
nuaa mission --edit
```

#### Option 2: Using AI Commands

```bash
# In your AI assistant (Claude, Copilot, etc.)
/nuaa.mission "NUAA exists to support the health and wellbeing of people who use drugs in NSW through peer-led advocacy, education, and support services grounded in harm reduction principles."
```

The AI will:
1. Ask clarifying questions about your specific principles
2. Generate a complete constitution with all required sections
3. Save it to `memory/constitution.md`
4. Automatically inject it into all agent context files

### What's Included in the Constitution

The generated constitution includes:

#### 1. Core Mission
Your organization's primary purpose - clear, compelling, 1-2 sentences

#### 2. Four Ethical Principles

- **Lived Experience Leadership**: Peer workers lead design and delivery, fair remuneration ($300/session)
- **Harm Reduction**: Non-judgmental, meet people where they are, evidence-based
- **Cultural Safety**: Trauma-informed, LGBTIQ+ inclusive, culturally responsive
- **Data Ethics**: Informed consent, secure storage, participant control, Indigenous data sovereignty

#### 3. Three Programmatic Standards

- **Evidence-Based Practice**: Research-informed, pilot-informed scale-up, built-in evaluation
- **Evaluation Rigor**: Clear indicators, mixed methods, community-shared findings
- **Budget Integrity**: Justified costs, transparent overheads, sustainability planning

#### 4. Governance Rules

How the constitution applies to all NUAA work and what happens if principles are violated

### How It Influences Your Work

Once created, the constitution is **automatically referenced** by all NUAA commands:

- **`/nuaa.design`** - Program designs explicitly embed ethical principles
- **`/nuaa.propose`** - Proposals demonstrate mission alignment
- **`/nuaa.measure`** - Impact frameworks reflect programmatic standards
- **Every AI interaction** - The constitution is in the AI's context

You don't need to manually reference it - it just works.

### Example Output

Here's a snippet of what your constitution might look like:

```markdown
# NUAA Mission Constitution

## Core Mission

NUAA exists to support the health and wellbeing of people who use drugs 
in NSW through peer-led advocacy, education, and support services grounded 
in harm reduction principles.

## Ethical Principles

### Principle I: Lived Experience Leadership

People with lived experience of drug use are the experts on their own lives 
and must lead the design, delivery, and evaluation of programs that affect them.

**Commitments**:
- People with lived experience lead program design, delivery, and evaluation
- Peer workers are valued, supported, and fairly compensated for their expertise
- Consumer advisory groups have meaningful decision-making power, not just consultation
- Peer workers receive fair remuneration (minimum $300/session for advisory participation)

[... continues with all sections ...]
```

### Best Practices

1. **Start Early**: Create your constitution before beginning program designs or proposals
2. **Get Buy-In**: Review with staff, board, and consumer advisory before finalizing
3. **Keep It Current**: Schedule annual reviews to ensure it reflects your work
4. **Reference It**: Explicitly cite the constitution in proposals to demonstrate alignment
5. **Use It**: Let it guide decision-making - "Does this align with our constitution?"

### Need Help?

- Review the example in `nuaa-kit/commands/mission.md` for detailed guidance
- Contact NUAA management for support on organizational values
- Update your constitution anytime with `nuaa mission --edit`

---

## Creating Program Specifications

### What is a Program Specification?

A **Program Specification** is a high-level document that captures the essence of a program idea before detailed planning begins. It serves as the foundation for all subsequent work - proposals, implementation plans, and documentation.

Think of it as the "concept note" phase - where you articulate:

- **What** the program will do
- **Why** it's needed
- **Who** will benefit
- **How** it aligns with NUAA's mission

Unlike detailed proposals or implementation plans, specifications are intentionally high-level, focusing on the core concept and identifying ambiguities that need resolution before moving forward.

### Why Use Specifications?

The specification phase offers critical benefits:

1. **Reduces AI Guesswork**: By explicitly marking ambiguities, you control what the AI assumes vs. what you decide
2. **Faster Iteration**: Clarify the concept before investing time in detailed planning
3. **Better Alignment**: Ensure mission alignment from the very start
4. **Team Clarity**: Creates a shared understanding before diving into details
5. **Funder Targeting**: Helps identify which funders and opportunities are the best fit

### The Specify → Clarify Workflow

#### Step 1: Create the Specification

Use either the CLI or AI commands to create a new program specification:

**Using the CLI:**

```bash
nuaa specify "Peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney"
```

**Using AI Commands:**

```bash
/nuaa.specify Create a peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney
```

This creates a new **initiative** directory (e.g., `initiatives/001-naloxone-distribution/`) with a `spec.md` file.

#### Step 2: AI Fills the Specification

The AI will:

1. Parse your description
2. Generate all specification sections (overview, target population, duration, evidence, activities, outcomes, alignment)
3. **Mark ambiguities** with `[NEEDS CLARIFICATION: specific question?]`
4. Reference the mission constitution to ensure initial alignment

**Example Output:**

```markdown
## Target Population

People who use opioids in Western Sydney, particularly those [NEEDS CLARIFICATION: Are we targeting people already engaged with health services, or harder-to-reach populations not in treatment?]

Age range: [NEEDS CLARIFICATION: What specific age range? All adults (18+), young adults (18-35), or no age restriction?]

## Duration

[NEEDS CLARIFICATION: Is this a 6-month pilot, 12-month implementation, or ongoing service?]
```

**Important**: The AI will mark a **maximum of 5 ambiguities**. These are the most critical questions that affect program scope, scale, or approach.

#### Step 3: Resolve Ambiguities

Use the clarify command to answer the marked questions:

**Using the CLI:**

```bash
nuaa clarify
```

**Using AI Commands:**

```bash
/nuaa.clarify
```

The AI will present each ambiguity as a structured question with suggested options:

```
Question 1: Target Age Range

Context: Target Population section
What we need to know: What specific age range should this program target?

Suggested Answers:
| Option | Answer | Implications |
|--------|--------|--------------|
| A | All adults (18+) | Broadest reach; simpler eligibility; may need age-specific materials |
| B | Young adults (18-35) | Focused on higher-risk demographic; peer educators same age range |
| C | Custom | Provide your specific answer |

Your choice: _
```

Your answers are directly inserted into the specification, replacing the `[NEEDS CLARIFICATION]` markers.

#### Step 4: Review and Plan

Once all ambiguities are resolved:

```bash
nuaa plan  # Create detailed implementation plan (Phase 2 feature)
```

### Understanding Clarification Markers

**What are they?**

Markers look like: `[NEEDS CLARIFICATION: specific question?]`

They indicate where the AI needs your input to avoid making incorrect assumptions.

**What gets marked?**

- Target population specifics (age range, engagement level, location)
- Program duration and timeline
- Scope of activities (pilot vs. full implementation)
- Implementation approach (one-time vs. ongoing, individual vs. group)
- Evidence requirements (local data needs)

**What doesn't get marked?**

- Budget details (handled in planning phase)
- Staff allocation (determined in implementation)
- Detailed evaluation methods (addressed in planning)
- Specific partnerships (identified during planning)

**Maximum 5 markers**: The AI prioritizes the most critical ambiguities that affect overall program direction.

### Example Workflow

Here's a complete workflow from idea to clarified specification:

```bash
# 1. Create specification from natural language
nuaa specify "Establish a lived experience mentorship program connecting people in early recovery with long-term peer mentors"

# Output:
# ✓ Created initiative 002-lived-experience-mentorship
# ✓ Specification: initiatives/002-lived-experience-mentorship/spec.md
# ⚠ Specification has 3 clarification markers

# 2. View the specification
cat initiatives/002-lived-experience-mentorship/spec.md

# 3. Resolve ambiguities interactively
nuaa clarify

# Interactive prompts:
# Question 1: How will mentors and mentees be matched?
#   A) By age and background similarity
#   B) By shared substance use experience
#   C) By geographic proximity
# Your choice: B
#
# Question 2: What is the mentorship duration?
#   A) 3-month program
#   B) 6-month program
#   C) Ongoing (no set end date)
# Your choice: B
#
# Question 3: Mentor support level?
#   A) Weekly check-ins (high touch)
#   B) Fortnightly check-ins (moderate)
#   C) Monthly check-ins (low touch)
# Your choice: A

# Output:
# ✓ Updated specification
# ✓ All ambiguities resolved
# → Next: Run 'nuaa plan' to create implementation plan

# 4. Create implementation plan
nuaa plan  # (Phase 2 feature)
```

### Best Practices

1. **Start Simple**: Use 1-2 sentences in your initial description; the AI will expand it
2. **Be Specific**: Include key details like target population and location if known
3. **Review Carefully**: Check that the AI understood your intent correctly
4. **Answer Honestly**: If none of the suggested options fit, choose "Custom" and provide your answer
5. **Think Mission First**: Ensure your answers align with NUAA's mission and values
6. **Iterate**: You can always refine the specification after clarification

### Directory Structure

When you create a specification, NUAA Kit creates this structure:

```
initiatives/
  001-naloxone-distribution/
    spec.md                    # Program specification (created by nuaa specify)
    plan.md                    # Implementation plan (created later by nuaa plan)
    sections/                  # Document sections (created later during drafting)
    CHANGELOG.md               # Initiative history
  002-peer-mentorship/
    spec.md
    ...
```

Each initiative gets an auto-incrementing number (001, 002, 003...) and a slug derived from the description.

### Tips for Good Specifications

**Clear Program Descriptions Help:**

✅ **Good**: "Create a peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney"

- Includes: what (naloxone distribution), who (people at risk), where (Western Sydney), approach (peer-led)

❌ **Too Vague**: "Help people with drugs"

- Missing: specifics about what, who, where, how

**The AI Can Clarify:**

Even if your description is incomplete, the AI will identify what's missing and ask. But starting with more detail reduces the number of clarification questions needed.

### Integration with Planning

Once your specification is clarified, it becomes the input for:

- **Implementation Planning** (`/nuaa.plan`) - Detailed document outline and structure
- **Gate Validation** - Quality checks against mission, ethics, and evidence standards
- **Section Drafting** - Creating individual proposal or document sections
- **Document Generation** - Producing final Word/PDF deliverables

The specification ensures everyone - staff, AI, funders - starts with the same understanding of what the program is about.

---

## The Plan → Draft → Gate-Check → Status Workflow

After your specification is complete and clarified, Phase 2 introduces the structured document planning and quality validation system. This workflow breaks document creation into manageable sections, each validated through quality gates before progression.

### What is a Document Plan?

A **Document Plan** transforms your completed specification into a structured outline with:

- **Section breakdown**: Logical division of the document into manageable parts
- **Gate assignments**: Each section is assigned a quality gate (1-5) based on its purpose
- **Dependencies**: Clear ordering showing which sections must be complete before others
- **Quality criteria**: Specific validation requirements for each gate
- **Progress tracking**: Dashboard showing what's done, what's next, and what's blocked

### The Five Quality Gates

Quality gates ensure each section meets standards before you move forward:

#### Gate 1: Initial Structure ✓

**Purpose**: Ensure foundational sections have clear purpose and structure  
**Applies To**: First 1-2 sections that establish context (Executive Summary, Background)  
**Criteria**:

- Section has clear purpose statement
- Key content requirements identified
- Length estimate provided
- No dependencies or dependencies satisfied

#### Gate 2: Core Content ✓

**Purpose**: Validate that essential program information is complete  
**Applies To**: Sections describing the program itself (Program Description, Target Population)  
**Criteria**:

- All Gate 1 criteria met
- Core information present and complete
- Evidence cited for key claims
- Aligns with mission constitution

#### Gate 3: Evidence & Justification ✓

**Purpose**: Ensure claims are supported by data and research  
**Applies To**: Sections making claims about effectiveness or need (Literature Review, Budget Justification)  
**Criteria**:

- All Gate 2 criteria met
- All claims have supporting evidence
- Evidence sources properly cited
- Logical reasoning connects evidence to conclusions

#### Gate 4: Integration & Coherence ✓

**Purpose**: Verify sections work together as a cohesive document  
**Applies To**: Later sections that build on earlier content (Implementation Timeline, Risk Management)  
**Criteria**:

- All Gate 3 criteria met
- References to earlier sections are accurate
- No contradictions with other sections
- Consistent terminology and tone

#### Gate 5: Review & Polish ✓

**Purpose**: Final quality check before submission  
**Applies To**: Completed document ready for review (Conclusion, Appendices)  
**Criteria**:

- All Gate 4 criteria met
- Grammar and spelling checked
- Formatting consistent throughout
- All placeholders resolved
- Ready for external review

**Important**: Higher gates include all lower gate criteria. A Gate 4 section must pass Gates 1, 2, 3, AND 4.

### Step-by-Step Workflow

#### 1. Create the Plan

Once your specification is clarified, create a document plan:

**Using the CLI:**

```bash
nuaa plan
# or specify initiative and document type
nuaa plan 001-naloxone-distribution --type proposal
```

**Using AI Commands:**

```bash
/nuaa.plan
# or
/nuaa.plan 001-naloxone-distribution --type proposal
```

This generates `initiatives/001-naloxone-distribution/plan.md` with:

- Section breakdown with gate assignments (typically 10-15 sections)
- Dependencies between sections clearly marked
- Quality criteria for each gate
- Progress tracking table

**Example Plan Output:**

```markdown
## Document Structure

### Section 1: Executive Summary
**Gate**: Gate 1 - Initial Structure
**Dependencies**: None (foundation section)
**Estimated Length**: 2-3 paragraphs (300-400 words)
**Purpose**: Provide high-level overview of program and funding request
**Status**: Not Started

### Section 2: Opioid Crisis Context
**Gate**: Gate 1 - Initial Structure
**Dependencies**: None
**Estimated Length**: 4-5 paragraphs (600-800 words)
**Purpose**: Establish the need and urgency for this program
**Status**: Not Started

### Section 3: Program Description
**Gate**: Gate 2 - Core Content
**Dependencies**: Section 1, Section 2
**Estimated Length**: 5-7 paragraphs (800-1000 words)
**Purpose**: Detail the peer-led naloxone distribution model
**Status**: Not Started
```

#### 2. Draft Sections

Work through sections in order, respecting dependencies. The AI will help draft each section with full context awareness.

##### 2a. Prepare to Draft

**Using the CLI:**

```bash
nuaa draft "Program Description"
```

This creates the section file structure and updates plan.md status to "In Progress".

**Using AI Commands:**

```bash
/nuaa.draft "Program Description"
```

##### 2b. How AI Drafts with Context

The AI automatically loads:

- **Specification** (`initiatives/NNN-slug/spec.md`) - Full program details
- **Mission Constitution** (`memory/constitution.md`) - Ethical principles and standards
- **Dependencies** - Earlier sections this section builds on
- **Related Sections** - Sections at same gate level for consistency

This ensures:
- Consistency across the document
- Mission alignment throughout
- No contradictions or redundancy
- Appropriate cross-referencing

##### 2c. Placeholder Handling

If the AI cannot complete a section due to missing information, it uses placeholder markers:

```markdown
[PLACEHOLDER: What is the exact geographic coverage area?]
```

The AI documents all placeholders at the end of the draft:

```markdown
## Placeholders to Resolve

1. **Line 45**: [PLACEHOLDER: Geographic coverage]
   - Context: Target population section
   - Question: What is the exact geographic coverage area?
   - Impact: Affects participant estimates and distribution strategy
```

To resolve placeholders later:

**Using the CLI:**

```bash
nuaa draft "Program Description" --resolve
```

**Using AI Commands:**

```bash
/nuaa.draft "Program Description" --resolve
```

The AI asks for each missing piece of information and updates the draft.

##### 2d. Content Guidelines by Document Type

The AI adapts writing style based on document type:

**Proposals:**
- Tone: Persuasive, professional, mission-aligned
- Focus: Demonstrating need, justifying budget, showing capability
- Evidence: Strong citations, data-driven, community-centered

**Program Designs:**
- Tone: Operational, detailed, implementable
- Focus: How things will actually work on the ground
- Evidence: Best practices, implementation research

**Evaluation Reports:**
- Tone: Analytical, objective, data-focused
- Focus: What happened, what was learned, what changes
- Evidence: Program data, participant feedback

**Impact Reports:**
- Tone: Storytelling, compelling, achievement-focused
- Focus: Community outcomes, lives changed, broader impact
- Evidence: Quantitative + qualitative, stories + statistics

##### 2e. Work Flow

- Start with Gate 1 sections (no dependencies)
- Draft multiple Gate 1 sections in parallel if desired
- Move to Gate 2 sections only after their dependencies pass
- Continue through Gates 3, 4, 5 in order

#### 3. Validate Gates

Before moving to dependent sections, validate the current section passes its gate:

**Using the CLI:**

```bash
nuaa gate-check "Program Description"
```

**Using AI Commands:**

```bash
/nuaa.gate-check "Program Description"
```

The CLI first checks dependencies are satisfied, then hands off to the AI for content validation.

**Example Validation Output:**

```markdown
# Gate Validation Report: Program Description

**Gate**: Gate 2 - Core Content
**Result**: PASS

## Criteria Results

1. Clear purpose statement: ✓ PASS
   - First paragraph clearly states section purpose
   - Establishes what will be covered

2. Core information complete: ✓ PASS
   - Peer-led model explained
   - Distribution strategy detailed
   - Training program outlined

3. Evidence cited: ✓ PASS
   - 3 references to naloxone effectiveness
   - Peer model research cited

4. Mission alignment: ✓ PASS
   - Harm reduction language throughout
   - Lived experience leadership emphasized

## Recommendation

✓ PASS: Section meets all Gate 2 criteria and is ready to proceed.

## Next Steps

- Update plan.md to mark section as "Passed"
- Sections 5, 7, 8 can now proceed (they depend on this section)
```

If the validation **fails**, you'll receive specific, actionable feedback:

```markdown
## Issues to Address

1. Missing evidence for cost-effectiveness claim (line 45)
   - Add citation comparing peer vs. professional educator costs
   - Consider including ROI data from similar programs

2. Training program lacks detail (line 78)
   - Specify training duration and curriculum
   - Include certification or competency assessment
```

#### 4. Revise Based on Feedback (if needed)

If a section fails validation, use the revise command to address feedback:

**Using the CLI:**

```bash
nuaa revise "Program Description" --type feedback --feedback "Need more detail on training methodology"
```

**Using AI Commands:**

```bash
/nuaa.revise "Program Description" --type feedback --feedback "Need more detail on training methodology"
```

**Revision Types:**

- **placeholder**: Resolve missing information markers
- **feedback**: Address specific gate validation feedback
- **consistency**: Update based on changed dependencies
- **enhancement**: Strengthen evidence or clarity

After revision, re-validate with `nuaa gate-check` to ensure the section now passes.

#### 5. Track Progress

Check overall initiative progress at any time:

**Using the CLI:**

```bash
nuaa status
```

**Using AI Commands:**

```bash
/nuaa.status
```

**Example Status Output:**

```markdown
# Initiative Status: 001-naloxone-distribution

**Document Type**: Proposal
**Overall Progress**: 33% (4 of 12 sections complete)

## Section Progress

| #   | Section Name          | Gate | Status         | Dependencies | Blocker              |
| --- | --------------------- | ---- | -------------- | ------------ | -------------------- |
| 1   | Executive Summary     | 1    | ✓ Passed       | None         | -                    |
| 2   | Opioid Crisis Context | 1    | ✓ Passed       | None         | -                    |
| 3   | Naloxone Evidence     | 1    | ✓ Passed       | None         | -                    |
| 4   | Program Description   | 2    | ✓ Passed       | 1, 2         | -                    |
| 5   | Peer-Led Model        | 3    | 🔄 In Progress | 4            | -                    |
| 6   | Target Population     | 2    | ⭕ Not Started | 2            | -                    |
| 7   | Distribution Strategy | 2    | ⏸ Blocked      | 4, 6         | Section 6 incomplete |
| 8   | Training Program      | 2    | ⏸ Blocked      | 4            | -                    |

## Next Actionable Sections

**Ready to Draft** (no blockers):
1. Target Population (Gate 2) - dependencies satisfied
2. Training Program (Gate 2) - dependencies satisfied

**Blocked**:
- Distribution Strategy (Gate 2) - waiting for Target Population
- Budget Justification (Gate 3) - waiting for multiple sections
```

### Gate Progression Rules

1. **Cannot skip gates**: Section must pass Gate N before attempting Gate N+1
2. **Dependencies first**: All dependency sections must pass their gates first
3. **Gate failure**: If section fails, it returns to "In Progress" status for revision
4. **Re-review**: After fixes, resubmit to `/nuaa.gate-check` for re-validation
5. **Document completion**: All sections must pass Gate 5 before document is complete

### Document Type Detection

The AI automatically detects document type based on specification content:

- **Proposal**: Emphasizes funding needs, budget details, donor language
- **Program Design**: Focuses on implementation details, workflows, operations
- **Evaluation Report**: Describes existing program, data collection, outcomes
- **Impact Report**: Documents completed program and community impact

You can override with `--type` flag: `nuaa plan --type proposal`

### Section Count Guidelines

Different document types have different complexity:

- **Proposals**: 10-15 sections
- **Program Designs**: 12-18 sections
- **Evaluation Reports**: 8-12 sections
- **Impact Reports**: 8-12 sections

### Gate Distribution

A well-balanced plan distributes sections across gates:

- **Gate 1**: 15-20% (foundation sections)
- **Gate 2**: 30-40% (core content)
- **Gate 3**: 25-35% (evidence-based)
- **Gate 4**: 10-15% (integration)
- **Gate 5**: 5-10% (polish)

The AI automatically balances gate assignments when creating the plan.

### Complete Example Workflow

Here's a complete workflow from specification through validation:

```bash
# Phase 1: Specification (completed)
nuaa specify "Peer-led naloxone distribution program"
nuaa clarify
# → initiatives/001-naloxone-distribution/spec.md (clarified)

# Phase 2: Planning & Drafting
nuaa plan
# → initiatives/001-naloxone-distribution/plan.md (12 sections, gates assigned)

# Check what to work on first
nuaa status
# → Shows 3 Gate 1 sections ready (no dependencies)

# Draft foundation sections (can do in parallel)
# AI: /nuaa.draft "Executive Summary"
# AI: /nuaa.draft "Opioid Crisis Context"
# AI: /nuaa.draft "Naloxone Evidence Base"

# Validate each section
nuaa gate-check "Executive Summary"
# → ✓ Passes Gate 1

nuaa gate-check "Opioid Crisis Context"
# → ✓ Passes Gate 1

nuaa gate-check "Naloxone Evidence Base"
# → ✓ Passes Gate 1

# Check progress and next steps
nuaa status
# → 25% complete, 4 Gate 2 sections now ready

# Draft core content sections
# AI: /nuaa.draft "Program Description"
nuaa gate-check "Program Description"
# → ✓ Passes Gate 2

# AI: /nuaa.draft "Target Population"
nuaa gate-check "Target Population"
# → ✗ Fails Gate 2 - missing evidence citation

# Revise and revalidate
# AI: Add citation to Target Population section
nuaa gate-check "Target Population"
# → ✓ Passes Gate 2

# Continue through all sections...
nuaa status
# → Track progress, identify blockers, plan next work
```

### Best Practices

1. **Complete Gate 1 First**: Finish all foundational sections before moving to Gate 2
2. **Work Dependencies**: Focus on sections that unblock others
3. **Batch Similar Gates**: Draft multiple Gate 2 sections together for consistency
4. **Validate Early**: Check sections as soon as drafted, don't accumulate unvalidated work
5. **Use Status Often**: Check `nuaa status` regularly to stay oriented
6. **Accept Failures**: Gate failures are learning opportunities, not setbacks
7. **Iterate**: Use feedback from failures to improve other sections

### Integration with Mission Constitution

All gate validations check for mission alignment:

- Gate 2+ requires harm reduction language
- Evidence must consider lived experience
- Budget justification must show fair peer worker compensation
- All content reviewed against constitutional principles

### Tips for Success

**Starting Out:**

- Let the AI create the plan - it knows the patterns
- Trust the gate assignments - they're based on best practices
- Don't skip dependency validation - it prevents compound errors

**During Drafting:**

- Draft in dependency order, even if tempting to skip ahead
- Keep sections focused - don't merge sections to "save time"
- Use validation feedback to improve future sections

**When Blocked:**

- Check `nuaa status` to see what's blocking progress
- Prioritize sections that unblock the most dependents
- Consider parallel work on independent sections

**Before Finalizing:**

- Ensure all sections pass their assigned gate
- Review Gate 5 criteria for document-wide consistency
- Use `/nuaa.status` one final time to confirm 100% complete

---

### Need Help?

- Review examples in `nuaa-kit/commands/specify.md` for detailed guidance
- Check `nuaa-kit/commands/clarify.md` for clarification process details
- Contact NUAA management for support on program concepts

---

## Core Features

### 1. **Program Design & Logic Models**

- `/nuaa.design` - Generate comprehensive program designs
- Automatic logic model creation (Inputs → Activities → Outputs → Outcomes → Impact)
- Stakeholder journey mapping
- Risk assessment integration
- Built-in NUAA principles and ethics

### 2. **Proposal & Grant Writing**

- `/nuaa.propose` - Generate funding proposals
- Automatic budget table generation
- Methodology breakdown from program design
- Timeline chart creation
- NUAA capability statement integration
- Export to Word with professional formatting

### 3. **Impact Measurement & Evaluation**

- `/nuaa.measure` - Define impact frameworks
- Indicator development (process, output, outcome, impact)
- Evaluation planning
- Data collection template generation
- Export to Excel for tracking

## Output Formatting (Context-Aware)

### Professional (External)

- Formal language for government, funders
- Full technical detail
- Policy-ready formatting
- Word document export with NUAA branding

### Professional/Peer (Internal)

- Clear, direct language for NUAA staff
- Balance of detail and accessibility
- SharePoint integration
- Teams collaboration features

### Peer-Friendly (Community)

- Plain language
- Visual emphasis (infographics, diagrams)
- Accessible formats
- Community consultation materials

## Microsoft 365 Integration

### Word

- Branded proposal templates
- Auto-generated sections
- Track changes workflow
- Co-authoring support

### Excel

- Budget calculators
- Impact tracking dashboards
- Logic model visualizations
- Indicator monitoring sheets

### SharePoint

- Centralized template library
- Version control
- Staff collaboration workspace
- Document approval workflows

### Teams

- Command access via Teams bot (future)
- Notification for reviews
- Collaboration channels
- File sharing integration

### Power Automate

- Auto-save to SharePoint
- Approval workflows
- Email notifications
- Calendar integration for timelines

## Directory Structure

Below tree reflects current state. Items marked (planned) are placeholders for upcoming work and may have stub or empty directories only.

```text
nuaa-kit/
├── README.md                      # This file
├── QUICKSTART.md                  # Staff training guide
├── STATUS.md                      # Implemented vs planned artifact matrix
├── templates/                     # Core templates
│   ├── program-design.md
│   ├── proposal.md
│   ├── logic-model.md
│   ├── impact-framework.md
│   └── budget-calculator.md       # (planned stub)
├── commands/                      # NUAA command docs
│   ├── design.md                  # /nuaa.design
│   ├── propose.md                 # /nuaa.propose
│   ├── measure.md                 # /nuaa.measure
│   ├── report.md                  # (planned) /nuaa.report
│   └── refine.md                  # (planned) /nuaa.refine
├── microsoft365/                  # (planned) M365 integration scaffolding
│   ├── README.md                  # Overview & roadmap
│   ├── word-templates/            # (planned)
│   ├── excel-dashboards/          # (planned)
│   └── powerautomate-flows/       # (planned)
└── examples/                      # (planned) Real NUAA examples library
    └── README.md                  # Placeholder roadmap
```

For actual historical NUAA examples see top-level `NUAA-examples/` outside of this kit.

## First Command to Try: `/nuaa.design`

**Purpose**: Design a new program with full logic model, stakeholder journeys, and impact framework.

**Usage**:

```bash
/nuaa.design Design a peer-led workshop series on stigma reduction in healthcare settings, \
    targeting 50 people who use drugs in Western Sydney, with 6 monthly sessions over 12 months.
```

**Output**: Complete program design document including:

- Program overview and rationale
- Stakeholder journey maps
- Logic model (inputs, activities, outputs, outcomes, impact)
- Risk assessment
- Preliminary budget estimate
- Impact measurement framework
- Export to Word for review

## NUAA-Specific Principles Built-In

Every command and template incorporates:

- **Peer-led approach** - Lived experience at center
- **Harm reduction philosophy** - Non-judgmental, evidence-based
- **Consumer remuneration** - Fair payment for contributions ($300/session standard)
- **Cultural safety** - Respectful of diverse communities
- **Transparency** - Open processes and decision-making
- **Impact focus** - Outcomes over outputs
- **Ethical practice** - Do no harm, informed consent

## Next Steps

1. Review `QUICKSTART.md` for staff training
2. Try first command: `/nuaa.design`
3. Customize templates for specific NUAA needs
4. Set up Microsoft 365 integration
5. Provide feedback for iteration

## Pre-Submission Checks (Placeholder Linter)

Before marking any NUAA document `status: final` in its front matter, run one of the placeholder linter scripts to ensure no raw placeholder tokens like `[Amount]` or `[Name]` remain:

```pwsh
pwsh scripts/powershell/check-placeholders.ps1 -Path nuaa-kit
```

```bash
./scripts/bash/check-placeholders.sh nuaa-kit
```

Both scripts exit non-zero if unresolved bracketed placeholders are detected in files whose front matter contains `status: final`.

## Documentation

### Getting Started

- **[QUICKSTART.md](QUICKSTART.md)** - Week-by-week onboarding guide for new users
- **[STATUS.md](STATUS.md)** - Current implementation status of all features

### Methodology Guides

- **[docs/workflow-diagram.md](docs/workflow-diagram.md)** - Visual guide to the complete program lifecycle
- **[docs/evolution-guide.md](docs/evolution-guide.md)** - How to maintain and update program designs over time
- **[docs/multi-agent-setup.md](docs/multi-agent-setup.md)** - Using multiple AI agents in one project
- **[docs/update-guide.md](docs/update-guide.md)** - How to update NUAA-Kit itself

### Technical References

- **[accessibility-guidelines.md](accessibility-guidelines.md)** - Making outputs accessible to all
- **[evaluation-data-dictionary.md](evaluation-data-dictionary.md)** - Standard indicators and measures
- **[glossary.md](glossary.md)** - NUAA-specific terminology

### Review & Analysis

- **[REVIEW-FINDINGS.md](REVIEW-FINDINGS.md)** - Comprehensive review and analysis findings

## Support

Contact: [NUAA IT/Project Lead]
Documentation: `/nuaa-kit/docs/`
Training: [Schedule sessions with staff]

---

**Built for NUAA by NUAA principles** 🌱
