---
description: "Draft a document section with context awareness"
---

# /nuaa.draft - Section Drafting Command

Template: See [section-template.md](../templates/section-template.md).

## Description

Draft a document section using the program specification, document plan, mission constitution, and related sections as context. This command creates well-structured, evidence-based content that aligns with NUAA principles and meets the section's gate requirements.

---

## Purpose

Section Drafting:

- Creates content that fulfills the section's purpose from the plan
- Incorporates context from related sections and dependencies
- Aligns with mission constitution principles
- Meets the quality criteria for the section's assigned gate
- Uses appropriate tone and language for the document type
- Cites evidence and provides justifications

---

## Usage

```bash
/nuaa.draft [SECTION_NAME] [--initiative INITIATIVE]
```

**Examples**:

- `/nuaa.draft "Program Description"` - Draft Program Description in active initiative
- `/nuaa.draft "Budget Justification" --initiative 001-naloxone-distribution`
- `/nuaa.draft "Executive Summary"` - Draft the Executive Summary

---

## How It Works

### Step 1: Load Planning Context

The AI will:

1. Identify the initiative (from argument or most recent)
2. Read `initiatives/NNN-slug/plan.md` to find the section
3. Extract:
   - Section purpose
   - Content requirements (bullet points)
   - Gate assignment
   - Quality criteria
   - Dependencies
   - Estimated length

### Step 2: Load Related Context

The AI will read and incorporate:

**Always Load**:

- `initiatives/NNN-slug/spec.md` - Program specification
- `memory/constitution.md` - Mission constitution for alignment

**Dependency Sections** (if they exist):

- For each dependency in the plan, read `initiatives/NNN-slug/sections/[dependency].md`
- Extract key information referenced by this section
- Note any data, dates, or facts that must be consistent

**Related Sections** (if they exist):

- Sections in the same gate level
- Sections that reference similar content
- Earlier sections that establish context

### Step 3: Draft Content

The AI will create content that:

**Meets Section Purpose**:

- Addresses the purpose statement from the plan
- Covers all content requirements (bullets)
- Stays within estimated length (±20%)

**Incorporates Context**:

- References information from dependency sections
- Maintains consistency with earlier sections
- Uses the same terminology and definitions
- Avoids contradictions or redundancy

**Aligns with Mission**:

- Uses harm reduction language appropriately
- Acknowledges lived experience where relevant
- Follows evidence-based practice principles
- Promotes self-determination and anti-stigma approaches

**Meets Gate Standards**:

- For Gate 1: Clear purpose, structured outline, key points identified
- For Gate 2: Complete information, evidence citations, mission alignment
- For Gate 3: Strong evidence base, proper citations, logical reasoning
- For Gate 4: Integration with earlier sections, consistency, coherence
- For Gate 5: Professional polish, formatting, completeness

### Step 4: Handle Missing Information

If the AI cannot complete a section due to missing information:

**Use Placeholder Markers**:

```markdown
[PLACEHOLDER: Information needed - specific question]
```

**Examples**:

- `[PLACEHOLDER: What is the exact geographic coverage area?]`
- `[PLACEHOLDER: Confirmed budget allocation for peer educator training?]`
- `[PLACEHOLDER: Citation needed for naloxone effectiveness in community settings]`

**Document Placeholders**:
The AI will list all placeholders at the end of the draft:

```markdown
## Placeholders to Resolve

1. **Line 45**: [PLACEHOLDER: Geographic coverage]

   - Context: Target population section
   - Question: What is the exact geographic coverage area?
   - Impact: Affects participant estimates and distribution strategy

2. **Line 78**: [PLACEHOLDER: Budget allocation]
   - Context: Training program description
   - Question: Confirmed budget allocation for peer educator training?
   - Impact: Determines number of educators we can train
```

### Step 5: Save and Update Status

The AI will:

1. Create `initiatives/NNN-slug/sections/[section-name].md` using the template
2. Suggest updating plan.md status to "Draft Complete"
3. List any placeholders that need resolution
4. Recommend next steps (validate with gate-check or draft next section)

---

## Content Guidelines by Document Type

### Proposals

**Tone**: Persuasive, professional, mission-aligned  
**Focus**: Demonstrating need, justifying budget, showing capability  
**Evidence**: Strong citations, data-driven, community-centered  
**Length**: Detailed but concise (funding bodies have limited time)

**Key Sections**:

- Executive Summary (compelling 1-page overview)
- Needs Statement (data showing the problem)
- Program Description (clear methodology)
- Budget Justification (every dollar explained)
- Evaluation Plan (measurable outcomes)

### Program Designs

**Tone**: Operational, detailed, implementable  
**Focus**: How things will actually work on the ground  
**Evidence**: Best practices, implementation research, pilot data  
**Length**: Comprehensive and thorough (internal use)

**Key Sections**:

- Service Model (step-by-step processes)
- Staffing Structure (roles, responsibilities, FTE)
- Workflows (who does what when)
- Quality Assurance (how we ensure good practice)
- Risk Mitigation (what could go wrong and how we prevent it)

### Evaluation Reports

**Tone**: Analytical, objective, data-focused  
**Focus**: What happened, what was learned, what changes  
**Evidence**: Program data, participant feedback, outcome measures  
**Length**: Data-rich with narrative context

**Key Sections**:

- Methodology (how data was collected)
- Findings (what the data shows)
- Analysis (what the findings mean)
- Recommendations (what should change)
- Limitations (what we couldn't measure)

### Impact Reports

**Tone**: Storytelling, compelling, achievement-focused  
**Focus**: Community outcomes, lives changed, broader impact  
**Evidence**: Quantitative + qualitative, stories + statistics  
**Length**: Accessible narrative with supporting data

**Key Sections**:

- Program Overview (what we did)
- Outcomes Achieved (numbers that matter)
- Participant Stories (lived experience voices)
- Community Impact (ripple effects)
- Lessons Learned (what worked, what didn't)

---

## Context Injection Examples

### Example 1: Budget Justification (Gate 3)

**Dependencies**: Program Description, Staffing Model

**Context Loaded**:

- From Program Description: "20 peer educators will conduct 2 training sessions per week"
- From Staffing Model: "Each peer educator works 15 hours/week at $35/hour"

**AI Uses Context**:

```markdown
## Peer Educator Costs

The program requires 20 peer educators working 15 hours per week each
(as detailed in the Staffing Model section). At the community-standard
rate of $35/hour for credentialed peer workers, this represents:

- Weekly cost: 20 educators × 15 hours × $35 = $10,500
- Annual cost (48 weeks): $504,000

This staffing level enables the delivery of 40 training sessions per week
(20 educators × 2 sessions each), sufficient to reach our target of 2,000
participants annually (see Program Description).
```

**Note How AI**:

- References specific numbers from dependencies
- Maintains consistency (20 educators, 15 hours, $35/hour)
- Shows calculations transparently
- Links back to program goals

### Example 2: Evaluation Framework (Gate 3)

**Dependencies**: Program Description, Expected Outcomes

**Mission Context**: Evidence-based practice, lived experience

**Context Loaded**:

- From Expected Outcomes: "Reduce overdose mortality by 25% in target area"
- From Expected Outcomes: "Increase naloxone carriage by peer network"
- From Mission: "Lived experience must inform all evaluation"

**AI Uses Context**:

```markdown
## Outcome Measurement

### Primary Outcome: Overdose Mortality Reduction

We will measure changes in overdose mortality rates in the target area
compared to baseline, with a goal of 25% reduction (as specified in
Expected Outcomes). Data will be obtained through:

- NSW Ambulance Service fatal overdose reports
- Coroner's data (with appropriate approvals)
- Hospital emergency department presentations

### Process Outcome: Naloxone Distribution

We will track naloxone carriage rates within peer networks through:

- Anonymous surveys with people who use drugs (every 6 months)
- Peer educator distribution logs
- Pharmacy refill data (aggregated, de-identified)

### Lived Experience in Evaluation

Following our mission commitment to lived experience leadership, the
evaluation framework was co-designed with people who use drugs. Our
Peer Advisory Committee will:

- Review all survey instruments for appropriateness
- Conduct peer-to-peer data collection (reducing stigma)
- Participate in data analysis and interpretation
- Co-author the evaluation report
```

**Note How AI**:

- Directly references the 25% goal from dependencies
- Addresses both outcomes mentioned in the plan
- Incorporates mission constitution principle
- Provides concrete methods

---

## Placeholder Resolution Workflow

When a draft has placeholders:

### Step 1: Document Placeholders

AI creates a placeholder summary:

```markdown
## Placeholders to Resolve

This draft has 3 placeholders requiring additional information:

1. **Geographic Coverage** (Line 45)

   - Question: Exact geographic area (LGAs, suburbs, postcodes)?
   - Why needed: Affects participant estimates and service planning
   - Who can answer: Program Manager or Funding Body

2. **Budget Amount** (Line 78)

   - Question: Final confirmed budget allocation for training?
   - Why needed: Determines trainer capacity and session frequency
   - Who can answer: Finance Team or Funding Body

3. **Partnership Status** (Line 120)
   - Question: Has MOU with NSW Health been signed?
   - Why needed: Affects service delivery model and data sharing
   - Who can answer: Executive Director
```

### Step 2: User Resolves Placeholders

User gathers missing information through:

- Consulting with team members
- Checking with funding bodies
- Reviewing existing documents
- Making program design decisions

### Step 3: AI Updates Draft

```bash
/nuaa.draft "Program Description" --resolve
```

The AI:

1. Reads the current draft
2. Identifies all `[PLACEHOLDER: ...]` markers
3. Asks user for each piece of information
4. Updates the draft with resolved information
5. Removes placeholder markers
6. Updates revision history

---

## Best Practices

### Good Placeholders

- `[PLACEHOLDER: Exact geographic coverage area (LGAs or postcodes)?]`
- `[PLACEHOLDER: Final confirmed budget for peer educator training?]`
- `[PLACEHOLDER: Citation for naloxone effectiveness in peer-led programs]`

### Bad Placeholders

- `[PLACEHOLDER: More info needed]` (too vague)
- `[PLACEHOLDER: Data]` (not specific)
- `[PLACEHOLDER: Check with team]` (doesn't explain what's needed)

### Document Type Adaptation

The AI should adjust writing style based on document type:

- **Proposals**: Persuasive, future-focused ("will deliver", "aims to")
- **Program Designs**: Procedural, present-focused ("peer educators conduct", "the process involves")
- **Evaluation Reports**: Analytical, past-focused ("data showed", "participants reported")
- **Impact Reports**: Narrative, achievement-focused ("delivered X services", "reached Y people")
