# NUAA-CLI Evolution: Applying Spec-Kit's Structured Methodology

**Version**: 1.0  
**Date**: November 12, 2025  
**Purpose**: Detailed plan to evolve NUAA-CLI from a project scaffolder to a comprehensive, principle-driven NGO workflow orchestration tool

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Domain Translation Framework](#2-domain-translation-framework)
3. [Architecture Comparison](#3-architecture-comparison)
4. [Phase-by-Phase Evolution](#4-phase-by-phase-evolution)
5. [Implementation Roadmap](#5-implementation-roadmap)
6. [Technical Specifications](#6-technical-specifications)
7. [Risk Analysis & Mitigation](#7-risk-analysis--mitigation)

---

## 1. Executive Summary

### Current State: NUAA-CLI Today

NUAA-CLI is a **project initialization tool** with strong multi-agent support. It:

- ✅ Bootstraps projects with agent-specific directory structures
- ✅ Provides excellent template scaffolding for NGO deliverables
- ✅ Supports 13+ AI agents with consistent conventions
- ⚠️ **Lacks** a structured, guided workflow for document creation
- ⚠️ **Lacks** principle enforcement and quality gates
- ⚠️ **Lacks** automation of the full NGO documentation lifecycle

### Target State: NUAA-CLI Enhanced

NUAA-CLI will become a **complete NGO workflow orchestration tool**. It will:

- ✅ Retain all existing multi-agent support
- ✅ Add a phased, structured workflow (Constitution → Specify → Clarify → Plan → Draft → Review)
- ✅ Enforce NGO-specific principles through pre-drafting gates
- ✅ Automate the full lifecycle from initial concept to final deliverable
- ✅ Maintain domain focus on NGO initiatives (not code development)

### Why This Evolution Matters

**For NGO Staff:**

- Reduce time spent on proposal writing by 60%
- Increase quality and consistency of all deliverables
- Ensure mission alignment in every document
- Reduce cognitive load through structured guidance

**For Funders:**

- Receive higher-quality, more complete proposals
- See consistent evaluation and impact frameworks
- Get better data for decision-making

**For Communities:**

- Faster program deployment (fewer documentation bottlenecks)
- More programs grounded in community needs
- Better accountability and transparency

---

## 2. Domain Translation Framework

This section translates spec-kit's **software development concepts** into NUAA-CLI's **NGO program development** domain.

### 2.1 Core Concept Mapping

| Spec-Kit Concept             | NUAA-CLI Equivalent       | Purpose in NGO Context                                                                                            |
| ---------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Constitution**             | **Mission Constitution**  | Defines organizational values, ethical principles, and programmatic standards that guide all AI-generated content |
| **Feature Specification**    | **Program Specification** | High-level description of a program idea, grant opportunity, or initiative need                                   |
| **Implementation Plan**      | **Document Plan**         | Structured outline for a proposal, program design, or report                                                      |
| **Tasks**                    | **Section Drafts**        | Sequential generation of document sections (e.g., "Draft Budget Section", "Draft Evaluation Framework")           |
| **Pre-Implementation Gates** | **Pre-Drafting Gates**    | Quality checkpoints ensuring ethical compliance, funder alignment, and mission consistency                        |
| **Code Generation**          | **Document Generation**   | Creation of professional-grade Word/PDF documents from structured outlines                                        |

### 2.2 Workflow Comparison

#### Spec-Kit Workflow (Code Development)

```
1. /speckit.constitution → Define code quality principles
2. /speckit.specify → Describe software feature
3. /speckit.clarify → Ask questions about ambiguities
4. /speckit.plan → Generate technical architecture
5. /speckit.tasks → Break down into coding tasks
6. /speckit.implement → Execute tasks, generate code
```

#### NUAA-CLI Workflow (NGO Programs)

```
1. /nuaa.mission → Define organizational principles
2. /nuaa.specify → Describe program/proposal idea
3. /nuaa.clarify → Ask questions about ambiguities
4. /nuaa.plan → Generate document structure/outline
5. /nuaa.sections → Break down into section drafts
6. /nuaa.draft → Execute drafting, generate document
7. /nuaa.review → Quality check against gates
```

### 2.3 Gate Translation

#### Spec-Kit Gates (Technical)

**Simplicity Gate:**

- Using ≤3 projects?
- No future-proofing?

**Anti-Abstraction Gate:**

- Using framework directly?
- Single model representation?

**Integration-First Gate:**

- Contracts defined?
- Contract tests written?

#### NUAA-CLI Gates (Programmatic)

**Mission Alignment Gate:**

- [ ] Does this initiative directly advance NUAA's core mission?
- [ ] Does it center lived experience and peer leadership?
- [ ] Is harm reduction embedded throughout?

**Ethical Standards Gate:**

- [ ] Are data privacy and confidentiality addressed?
- [ ] Is language inclusive and non-stigmatizing?
- [ ] Is cultural safety ensured for all participants?
- [ ] Is informed consent planned appropriately?

**Funder Alignment Gate:**

- [ ] Does this align with the funder's stated priorities?
- [ ] Is the budget within typical grant ranges?
- [ ] Are all required sections included?
- [ ] Is the timeline realistic?

**Evidence-Based Practice Gate:**

- [ ] Is there a clear evidence base cited?
- [ ] Are outcome measures defined?
- [ ] Is the evaluation approach rigorous?
- [ ] Are assumptions made explicit?

**Feasibility Gate:**

- [ ] Can NUAA deliver this with current capacity?
- [ ] Are partnerships confirmed?
- [ ] Is the budget justified and realistic?
- [ ] Are risks identified and mitigatable?

---

## 3. Architecture Comparison

### 3.1 Current NUAA-CLI Architecture

```
nuaa-cli/
├── src/nuaa_cli/__init__.py     # CLI entry point (typer-based)
├── nuaa-kit/
│   ├── commands/                # Agent command templates
│   │   ├── design.md           # Program design
│   │   ├── propose.md          # Proposal writing
│   │   ├── measure.md          # Impact measurement
│   │   └── ...
│   ├── templates/              # Output templates
│   │   ├── program-design.md
│   │   ├── proposal.md
│   │   ├── impact-framework.md
│   │   └── ...
│   └── microsoft365/           # M365 integrations
├── scripts/
│   ├── bash/
│   │   └── update-agent-context.sh
│   └── powershell/
│       └── update-agent-context.ps1
└── memory/
    └── constitution.md          # Template (not used in workflow)
```

**Current Workflow:**

1. User runs `nuaa init` → project scaffolded
2. User invokes `/nuaa.design` → AI generates full document immediately
3. No intermediate steps, no quality gates, no guided refinement

### 3.2 Target NUAA-CLI Architecture

```
nuaa-cli/
├── src/nuaa_cli/__init__.py     # Enhanced CLI
├── nuaa-kit/
│   ├── commands/                # EXPANDED command set
│   │   ├── mission.md          # NEW: Constitution creation
│   │   ├── specify.md          # NEW: High-level specification
│   │   ├── clarify.md          # NEW: Ambiguity resolution
│   │   ├── plan.md             # NEW: Document structure planning
│   │   ├── sections.md         # NEW: Section-by-section drafting
│   │   ├── draft.md            # NEW: Full document generation
│   │   ├── review.md           # NEW: Quality gate validation
│   │   ├── design.md           # KEPT: Backward compatibility
│   │   ├── propose.md          # KEPT: Backward compatibility
│   │   └── measure.md          # KEPT: Backward compatibility
│   ├── templates/
│   │   ├── [existing templates]
│   │   └── section-prompts/    # NEW: Per-section generation guides
│   ├── checklists/             # NEW: Quality gates
│   │   ├── mission-alignment-gate.md
│   │   ├── ethical-standards-gate.md
│   │   ├── funder-alignment-gate.md
│   │   ├── evidence-based-gate.md
│   │   └── feasibility-gate.md
│   └── microsoft365/
├── scripts/
│   ├── bash/
│   │   ├── create-new-initiative.sh   # NEW: Like create-new-feature.sh
│   │   ├── setup-plan.sh              # NEW: Planning workflow
│   │   ├── check-gates.sh             # NEW: Gate validation
│   │   ├── update-agent-context.sh    # ENHANCED
│   │   └── ...
│   └── powershell/
│       └── [mirrors bash/]
└── memory/
    └── constitution.md          # ACTIVE in workflow
```

**Target Workflow:**

1. User runs `nuaa init` → project scaffolded with ALL new commands
2. User invokes `/nuaa.mission` → Creates mission constitution
3. User invokes `/nuaa.specify "Peer naloxone program"` → High-level spec created
4. AI invokes `/nuaa.clarify` → Asks 3-5 targeted questions
5. User answers → Spec updated with clarifications
6. User invokes `/nuaa.plan` → Document structure/outline generated
7. AI validates plan against gates → Pass/fail feedback
8. User invokes `/nuaa.draft` → Full document generated section-by-section
9. AI invokes `/nuaa.review` → Final quality check
10. Output: Professional-grade document ready for stakeholder review

---

## 4. Phase-by-Phase Evolution

### Phase 0: Foundation (Weeks 1-2)

**Goal:** Establish the Mission Constitution system

**Tasks:**

1. ✅ Create `commands/mission.md` template
2. ✅ Create default `templates/mission-constitution-template.md`
3. ✅ Update `scripts/bash/update-agent-context.sh` to inject constitution into all agent contexts
4. ✅ Add CLI command: `nuaa mission --set "Our mission is..."`
5. ✅ Document the mission constitution concept in `nuaa-kit/README.md`

**Acceptance Criteria:**

- [ ] Running `/nuaa.mission` generates a populated `memory/constitution.md`
- [ ] Constitution includes: Core mission, ethical principles, programmatic standards, governance
- [ ] All subsequent AI interactions reference the constitution
- [ ] Constitution is automatically loaded into agent context

**Example Output (`memory/constitution.md`):**

```markdown
# NUAA Mission Constitution

## Core Mission

NUAA exists to support the health and wellbeing of people who use drugs in NSW through peer-led advocacy, education, and support services grounded in harm reduction principles.

## Ethical Principles

### Principle I: Lived Experience Leadership

- People with lived experience lead program design, delivery, and evaluation
- Consumer advisory groups have meaningful decision-making power
- Peer workers receive fair remuneration ($300/session minimum)

### Principle II: Harm Reduction

- Non-judgmental, non-coercive approaches
- Meet people where they are (no prerequisites)
- Evidence-based information provision
- Respect participant agency and choice

### Principle III: Cultural Safety

- Programs are culturally appropriate for Aboriginal and Torres Strait Islander peoples
- Staff trained in cultural competency
- Community consultation informs design
- No "one size fits all" approaches

### Principle IV: Data Ethics

- Informed consent is explicit and ongoing
- Data is stored securely and anonymously where possible
- Participants control their own narratives
- Aboriginal and Torres Strait Islander data sovereignty respected

## Programmatic Standards

### Evidence-Based Practice

- All programs cite relevant research and data
- Pilot programs inform scale-up
- Evaluation is built-in, not bolt-on

### Evaluation Rigor

- Clear indicators at process, output, outcome, and impact levels
- Mixed methods (quantitative + qualitative + participatory)
- Findings shared with community and contribute to harm reduction evidence base

### Budget Integrity

- All costs justified
- Consumer remuneration budgeted at $300/session
- Indirect costs transparent
- Sustainability planned from day one

## Governance

This constitution guides all NUAA programs, proposals, and reports. Any document generated by AI must demonstrate alignment with these principles. Violations should be flagged immediately for human review.

**Version**: 1.0  
**Ratified**: [Date]  
**Next Review**: [Annually]
```

---

### Phase 1: Specification & Clarification (Weeks 3-4)

**Goal:** Implement the Specify → Clarify workflow

**Tasks:**

1. ✅ Create `commands/specify.md` template
2. ✅ Create `commands/clarify.md` template
3. ✅ Create `scripts/bash/create-new-initiative.sh` (like `create-new-feature.sh` in spec-kit)
   - Scans `initiatives/` directory
   - Creates next initiative number (001, 002, etc.)
   - Creates directory: `initiatives/001-peer-naloxone/`
   - Copies spec template
   - Sets `NUAA_INITIATIVE` environment variable
4. ✅ Update CLI to support: `nuaa specify "Brief description"`
5. ✅ Implement `[NEEDS CLARIFICATION]` marker system in templates

**Acceptance Criteria:**

- [ ] `/nuaa.specify` creates high-level program/proposal spec
- [ ] Spec includes marked ambiguities: `[NEEDS CLARIFICATION: What is the target age range?]`
- [ ] Maximum 5 clarification markers allowed
- [ ] `/nuaa.clarify` presents interactive questions with multiple-choice options
- [ ] User answers update spec, remove markers
- [ ] Initiative directory structure created automatically

**Example Interaction:**

```bash
# User invokes
/nuaa.specify Create a peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney

# AI generates initiatives/001-naloxone-distribution/spec.md with content like:

---
# Program Specification: Peer-Led Naloxone Distribution

**Initiative**: 001-naloxone-distribution
**Created**: 2025-11-12
**Status**: Draft

## Overview
A peer-led program to distribute naloxone kits and provide overdose response training to people at risk of opioid overdose in Western Sydney.

## Target Population
[NEEDS CLARIFICATION: What specific age range? All adults, or focused on youth/young adults?]

People who use opioids in Western Sydney, particularly those [NEEDS CLARIFICATION: Engaged with health services, or harder-to-reach populations not in treatment?]

## Duration
[NEEDS CLARIFICATION: Is this a 6-month pilot, 12-month implementation, or ongoing service?]

## Evidence Base
Naloxone distribution reduces opioid overdose deaths (citation needed).
[NEEDS CLARIFICATION: Are there specific local data (e.g., overdose rates in Western Sydney) we should cite?]

## Key Activities
- Peer educator training
- Naloxone kit distribution
- Overdose response training
- [NEEDS CLARIFICATION: Ongoing support/follow-up with participants?]
---

# User then invokes
/nuaa.clarify

# AI presents:
---
## Question 1: Target Age Range

**Context**: "Target Population" (spec.md line 12)
**What we need to know**: What specific age range should this program target?

**Suggested Answers**:
| Option | Answer | Implications |
|--------|--------|--------------|
| A | All adults (18+) | Broadest reach, simpler eligibility, may need age-specific materials |
| B | Young adults (18-35) | Focused on higher-risk demographic, peer educators same age range |
| C | No age restriction | Most inclusive, requires diverse peer educator cohort |
| Custom | Your own answer | [Describe your preference] |

**Your choice**: _[Waiting for user response]_

## Question 2: Population Engagement Level
...
---
```

---

### Phase 2: Planning & Gates (Weeks 5-7)

**Goal:** Implement the Plan → Gate Validation workflow

**Tasks:**

1. ✅ Create `commands/plan.md` template
2. ✅ Create `scripts/bash/setup-plan.sh`
   - Reads `initiatives/001-naloxone-distribution/spec.md`
   - Reads `memory/constitution.md`
   - Generates `initiatives/001-naloxone-distribution/plan.md` (document outline)
3. ✅ Create all gate checklists in `nuaa-kit/checklists/`
4. ✅ Create `scripts/bash/check-gates.sh`
   - Scans `initiatives/001-naloxone-distribution/plan.md`
   - Validates against each gate
   - Outputs pass/fail for each gate
5. ✅ Update CLI: `nuaa plan "Tech stack / document structure choices"`

**Acceptance Criteria:**

- [ ] `/nuaa.plan` generates a structured document outline with sections
- [ ] Plan references the constitution for alignment
- [ ] Gates automatically validate the plan
- [ ] AI presents gate results in a table format
- [ ] Failed gates block progression with clear remediation steps
- [ ] User can override gate failures with justification

**Example Plan Output (`initiatives/001-naloxone-distribution/plan.md`):**

```markdown
# Document Plan: Peer-Led Naloxone Distribution Proposal

**Initiative**: 001-naloxone-distribution
**For**: NSW Health Grant Application
**Format**: Word document (max 15 pages)
**Sections**: Executive Summary, Background, Program Design, Methodology, Budget, Evaluation

---

## Pre-Drafting Gates

### Mission Alignment Gate

- [x] Centers lived experience leadership (peer educators)
- [x] Embeds harm reduction (naloxone = pragmatic harm reduction)
- [x] Directly advances NUAA mission (health & wellbeing of people who use drugs)

### Ethical Standards Gate

- [x] Data privacy planned (anonymous kit distribution tracking)
- [x] Inclusive language used throughout
- [x] Cultural safety addressed (Aboriginal health worker consultation planned)
- [x] Informed consent approach clear (verbal consent for training, no PII collected for kits)

### Funder Alignment Gate

- [x] Aligns with NSW Health Overdose Prevention Strategy
- [x] Budget within typical range ($50,000 for 12 months)
- [x] All required sections included
- [x] Timeline realistic (3-month setup, 9-month delivery)

### Evidence-Based Practice Gate

- [x] Strong evidence base (Cochrane review cited)
- [x] Outcome measures defined (kits distributed, reversals reported)
- [x] Evaluation approach rigorous (process + outcome evaluation)
- [ ] [NEEDS WORK] Local data for Western Sydney not yet sourced → ACTION: Add reference to NSW Ambulance overdose data

### Feasibility Gate

- [x] NUAA capacity sufficient (similar programs run previously)
- [x] Partnership with WSLHD confirmed (letter of support ready)
- [x] Budget justified (peer educator wages, kit costs, evaluation)
- [x] Risks identified (stigma from pharmacies, supply chain issues)

---

## Document Structure

### 1. Executive Summary (1 page)

- Compelling 3-paragraph overview
- Key stats: Target 300 people, distribute 500 kits, prevent 20+ overdose deaths

### 2. Background & Need (2 pages)

- NUAA's 30+ year track record
- Opioid overdose crisis in Western Sydney (local data)
- Why peer-led approaches work

### 3. Program Design (4 pages)

- Logic model (input → activities → outputs → outcomes → impact)
- Target population & reach
- Key activities (training, distribution, support)
- Innovation (peer-led, culturally safe, no prerequisites)

### 4. Methodology (3 pages)

- Implementation phases
- Peer educator recruitment & training
- Kit distribution protocol
- Cultural safety measures
- Consumer participation

### 5. Budget (2 pages)

- Summary table
- Line-item details with justification
- Peer educator remuneration at $300/session

### 6. Evaluation (2 pages)

- Process indicators (kits distributed, training sessions held)
- Outcome indicators (overdose reversals, participant confidence)
- Data collection methods
- Reporting timeline

### 7. Sustainability (1 page)

- Post-grant funding plan
- Community ownership approach

---

## Gate Status: PASS (1 minor action item)

**Action Required Before Drafting**:

- [ ] Add Western Sydney-specific overdose data (from NSW Ambulance reports)
```

**Gate Validation Output:**

```
Validating plan against quality gates...

| Gate                    | Status | Issues |
|-------------------------|--------|--------|
| Mission Alignment       | ✓ PASS | None   |
| Ethical Standards       | ✓ PASS | None   |
| Funder Alignment        | ✓ PASS | None   |
| Evidence-Based Practice | ⚠ WARN | Missing local data |
| Feasibility             | ✓ PASS | None   |

Overall Status: PASS WITH WARNINGS

Recommendation: Address warning before proceeding to drafting phase.
To proceed anyway, user must confirm: "I acknowledge the warning and choose to proceed."
```

---

### Phase 3: Section-by-Section Drafting (Weeks 8-10)

**Goal:** Implement granular, section-by-section document generation

**Tasks:**

1. ✅ Create `commands/sections.md` template
2. ✅ Create `templates/section-prompts/` directory with prompts for each common section:
   - `executive-summary-prompt.md`
   - `background-need-prompt.md`
   - `program-design-prompt.md`
   - `methodology-prompt.md`
   - `budget-prompt.md`
   - `evaluation-prompt.md`
   - `sustainability-prompt.md`
3. ✅ Create `scripts/bash/generate-sections.sh`
   - Reads plan.md to determine section order
   - For each section, loads appropriate section-prompt
   - Generates section content
   - Saves to `initiatives/001-naloxone-distribution/sections/01-executive-summary.md`
4. ✅ Update CLI: `nuaa sections` (auto-detects active initiative)

**Acceptance Criteria:**

- [ ] `/nuaa.sections` generates one section at a time in dependency order
- [ ] Each section references constitution, spec, and plan
- [ ] User can review and approve each section before next is generated
- [ ] Sections are saved individually for version control
- [ ] AI shows progress: "Section 1/7 complete"

**Example Section Prompt (`templates/section-prompts/program-design-prompt.md`):**

```markdown
# Program Design Section Prompt

You are drafting the **Program Design** section for a NUAA funding proposal.

## Context You Must Reference

1. **Mission Constitution** (`memory/constitution.md`) - Ensure alignment
2. **Program Specification** (`initiatives/{INITIATIVE}/spec.md`) - Core program details
3. **Document Plan** (`initiatives/{INITIATIVE}/plan.md`) - Section requirements

## Section Requirements (from Plan)

{PLAN_SECTION_DETAILS}

## Structure to Follow

1. **Logic Model** (visual + narrative)

   - Inputs (resources needed)
   - Activities (what we'll do)
   - Outputs (immediate results)
   - Outcomes (changes for participants)
   - Impact (broader community/system change)

2. **Target Population & Reach**

   - Demographics and needs
   - Geographic focus
   - Estimated reach (be realistic)

3. **Key Activities** (3-5 core activities)

   - Detailed description of each
   - Why each activity is essential
   - How each embeds harm reduction

4. **Innovation & Differentiation**
   - What makes this peer-led approach effective
   - How it differs from clinical/non-peer approaches
   - Evidence for peer-led effectiveness

## Tone & Style

- **Funder-Facing**: Professional, evidence-based, but not academic jargon
- **Compelling**: Tell the story of how this changes lives
- **Specific**: Use numbers, not vague claims ("300 people" not "many people")

## Quality Checks

Before finalizing, verify:

- [ ] Logic model is complete and logical (each level connects)
- [ ] Target reach is justified (based on capacity and evidence)
- [ ] Activities clearly embed harm reduction principles
- [ ] Innovation is evidence-based, not just claimed
- [ ] Language is inclusive and non-stigmatizing
- [ ] Mission constitution principles are visible throughout

## Output Format

Return markdown with clear headings. Use tables for logic model. Include in-text citations where evidence is referenced.
```

---

### Phase 4: Full Document Assembly & Review (Weeks 11-12)

**Goal:** Implement final document generation and quality review

**Tasks:**

1. ✅ Create `commands/draft.md` template
2. ✅ Create `commands/review.md` template
3. ✅ Create `scripts/bash/assemble-document.sh`
   - Reads all sections from `initiatives/001-naloxone-distribution/sections/`
   - Assembles in order specified by plan
   - Adds table of contents
   - Formats according to funder requirements
   - Exports to Word/PDF
4. ✅ Create `scripts/bash/review-document.sh`
   - Re-runs gate validation on complete document
   - Checks word count / page count limits
   - Validates all citations and references
   - Checks for [PLACEHOLDER] markers
5. ✅ Update CLI: `nuaa draft`, `nuaa review`

**Acceptance Criteria:**

- [ ] `/nuaa.draft` assembles all sections into final document
- [ ] Export formats: Markdown, Word (.docx), PDF
- [ ] Table of contents auto-generated
- [ ] `/nuaa.review` provides final quality report
- [ ] Review identifies any remaining issues
- [ ] Document is ready for human review and submission

**Example Review Output:**

```
Final Document Review: initiatives/001-naloxone-distribution/proposal.md

| Check                        | Status | Details |
|------------------------------|--------|---------|
| All sections present         | ✓ PASS | 7/7 sections included |
| Page count                   | ✓ PASS | 14 pages (limit: 15) |
| Word count                   | ✓ PASS | 4,890 words (estimated) |
| Citations complete           | ✓ PASS | 12 references, all formatted |
| No placeholder markers       | ✓ PASS | All [PLACEHOLDER] text replaced |
| Gate: Mission Alignment      | ✓ PASS | Peer leadership clear throughout |
| Gate: Ethical Standards      | ✓ PASS | Data privacy, cultural safety addressed |
| Gate: Funder Alignment       | ✓ PASS | NSW Health priorities reflected |
| Gate: Evidence-Based         | ✓ PASS | Strong evidence base, local data included |
| Gate: Feasibility            | ✓ PASS | Budget realistic, risks mitigated |

Overall Quality: READY FOR SUBMISSION

Recommendation: Human review for final polish, then submit.

Outputs generated:
- initiatives/001-naloxone-distribution/proposal.md
- initiatives/001-naloxone-distribution/proposal.docx
- initiatives/001-naloxone-distribution/proposal.pdf
```

---

### Phase 5: Backward Compatibility & Migration (Weeks 13-14)

**Goal:** Ensure existing users can continue using legacy commands while gradually adopting new workflow

**Tasks:**

1. ✅ Keep all existing commands (`design.md`, `propose.md`, `measure.md`) as-is
2. ✅ Add deprecation notices to legacy commands: _"This command generates a complete document in one step. For more control and quality assurance, try the new workflow: /nuaa.specify → /nuaa.clarify → /nuaa.plan → /nuaa.draft"_
3. ✅ Create migration guide: `nuaa-kit/docs/workflow-migration-guide.md`
4. ✅ Update README with "Quick Mode vs. Guided Mode" comparison
5. ✅ Add CLI flag: `nuaa init --workflow guided` vs. `nuaa init --workflow quick`

**Acceptance Criteria:**

- [ ] Legacy commands still work exactly as before
- [ ] New users default to guided workflow
- [ ] Existing users can opt-in to guided workflow
- [ ] Clear documentation explains both approaches
- [ ] No breaking changes

**Workflow Comparison:**

| Aspect         | Quick Mode (Legacy)                 | Guided Mode (New)                                                                  |
| -------------- | ----------------------------------- | ---------------------------------------------------------------------------------- |
| Commands       | `/nuaa.design`, `/nuaa.propose`     | `/nuaa.mission` → `/nuaa.specify` → `/nuaa.clarify` → `/nuaa.plan` → `/nuaa.draft` |
| Steps          | 1 command → full document           | 5-6 commands → full document                                                       |
| Quality Gates  | None                                | 5 gates validated                                                                  |
| Customization  | Limited (one-shot generation)       | High (review each section)                                                         |
| Best For       | Experienced users, quick iterations | New users, high-stakes proposals                                                   |
| Learning Curve | Low                                 | Moderate                                                                           |

---

## 5. Implementation Roadmap

### Timeline Overview

| Phase                      | Duration     | Key Deliverables                         |
| -------------------------- | ------------ | ---------------------------------------- |
| Phase 0: Foundation        | Weeks 1-2    | Mission constitution system              |
| Phase 1: Specify & Clarify | Weeks 3-4    | Specification and clarification commands |
| Phase 2: Planning & Gates  | Weeks 5-7    | Document planning and quality gates      |
| Phase 3: Section Drafting  | Weeks 8-10   | Granular section generation              |
| Phase 4: Assembly & Review | Weeks 11-12  | Final document generation and review     |
| Phase 5: Migration         | Weeks 13-14  | Backward compatibility and documentation |
| **Total**                  | **14 weeks** | **Complete system**                      |

### Resource Requirements

**Development:**

- 1 Python developer (familiar with typer, rich)
- 1 Technical writer (for documentation and prompts)
- 1 NGO subject matter expert (NUAA staff member)

**Testing:**

- 3-5 NUAA staff for user acceptance testing
- 2 external grant reviewers for quality validation

**Infrastructure:**

- GitHub repository (existing)
- CI/CD pipeline for automated testing
- Documentation hosting (GitHub Pages or similar)

---

## 6. Technical Specifications

### 6.1 New CLI Commands

#### `nuaa mission`

**Purpose:** Create or update the mission constitution

**Usage:**

```bash
nuaa mission --set "Our mission is to support the health and wellbeing of people who use drugs..."
nuaa mission --edit          # Opens constitution in default editor
nuaa mission --show          # Displays current constitution
```

**Implementation:**

```python
@app.command()
def mission(
    set: Optional[str] = typer.Option(None, "--set", help="Set mission statement"),
    edit: bool = typer.Option(False, "--edit", help="Edit constitution in editor"),
    show: bool = typer.Option(False, "--show", help="Display current constitution")
):
    """Create or update the NUAA mission constitution."""
    constitution_path = Path("memory/constitution.md")

    if show:
        # Display existing constitution
        ...
    elif edit:
        # Open in default editor
        ...
    elif set:
        # Create new constitution from template with provided mission
        ...
```

#### `nuaa specify`

**Purpose:** Create a high-level program specification

**Usage:**

```bash
nuaa specify "Create a peer-led naloxone distribution program for Western Sydney"
```

**Implementation:**

```python
@app.command()
def specify(description: str):
    """Create a high-level program specification."""
    # Run scripts/bash/create-new-initiative.sh or PS equivalent
    # Generate initiatives/NNN-slug/spec.md
    # Insert [NEEDS CLARIFICATION] markers for ambiguities
    ...
```

#### `nuaa clarify`

**Purpose:** Resolve ambiguities in specification

**Usage:**

```bash
nuaa clarify              # Auto-detects active initiative
nuaa clarify 001-naloxone-distribution
```

**Implementation:**

```python
@app.command()
def clarify(initiative: Optional[str] = None):
    """Resolve ambiguities in the program specification."""
    # Find spec.md with [NEEDS CLARIFICATION] markers
    # Present interactive questions
    # Update spec.md with answers
    ...
```

#### `nuaa plan`

**Purpose:** Generate document structure and outline

**Usage:**

```bash
nuaa plan "NSW Health grant application, 15 pages max, Word format"
```

**Implementation:**

```python
@app.command()
def plan(context: str):
    """Generate document structure and outline."""
    # Run scripts/bash/setup-plan.sh
    # Generate initiatives/NNN-slug/plan.md
    # Validate against gates
    ...
```

#### `nuaa sections`

**Purpose:** Generate document sections one-by-one

**Usage:**

```bash
nuaa sections            # Generate all sections in order
nuaa sections --section "Executive Summary"  # Generate specific section
```

**Implementation:**

```python
@app.command()
def sections(section: Optional[str] = None):
    """Generate document sections."""
    # Run scripts/bash/generate-sections.sh
    # For each section in plan.md, generate content
    # Save to initiatives/NNN-slug/sections/NN-section-name.md
    ...
```

#### `nuaa draft`

**Purpose:** Assemble final document from sections

**Usage:**

```bash
nuaa draft               # Assemble and export
nuaa draft --format word  # Export as .docx only
```

**Implementation:**

```python
@app.command()
def draft(format: str = typer.Option("all", help="Output format: md, word, pdf, all")):
    """Assemble final document from sections."""
    # Run scripts/bash/assemble-document.sh
    # Combine sections in order
    # Export to requested formats
    ...
```

#### `nuaa review`

**Purpose:** Final quality check before submission

**Usage:**

```bash
nuaa review
```

**Implementation:**

```python
@app.command()
def review():
    """Perform final quality check on document."""
    # Run scripts/bash/review-document.sh
    # Re-validate gates
    # Check formatting, citations, placeholders
    # Generate review report
    ...
```

### 6.2 Script Specifications

#### `scripts/bash/create-new-initiative.sh`

**Purpose:** Scaffold a new initiative directory structure

**Inputs:**

- `$1`: Description (e.g., "Peer-led naloxone distribution")

**Outputs:**

- Creates `initiatives/NNN-slug/` directory
- Generates `spec.md` from template
- Sets `NUAA_INITIATIVE` environment variable
- Returns JSON: `{"initiative": "001-naloxone-distribution", "spec_file": "..."}`

**Logic:**

```bash
#!/bin/bash
# 1. Scan initiatives/ for highest number
# 2. Increment (001 → 002)
# 3. Generate slug from description
# 4. Create directory structure
# 5. Copy spec template
# 6. Set environment variable
```

#### `scripts/bash/setup-plan.sh`

**Purpose:** Generate document plan from specification

**Inputs:**

- Reads `initiatives/$NUAA_INITIATIVE/spec.md`
- Reads `memory/constitution.md`
- Takes context string (funder, format, etc.)

**Outputs:**

- Creates `initiatives/$NUAA_INITIATIVE/plan.md`
- Returns JSON with plan path

**Logic:**

```bash
#!/bin/bash
# 1. Validate spec.md exists and has no [NEEDS CLARIFICATION] markers
# 2. Load constitution
# 3. Generate document outline based on funder/format
# 4. Populate plan.md template
# 5. Save to initiative directory
```

#### `scripts/bash/check-gates.sh`

**Purpose:** Validate plan against quality gates

**Inputs:**

- Reads `initiatives/$NUAA_INITIATIVE/plan.md`
- Reads `nuaa-kit/checklists/*.md`

**Outputs:**

- Returns JSON: `{"mission_alignment": "pass", "ethical_standards": "pass", ...}`
- Console table display

**Logic:**

```bash
#!/bin/bash
# For each gate checklist:
#   1. Parse checklist items
#   2. Check if plan.md addresses each item
#   3. Mark pass/fail/warn
# 4. Aggregate results
# 5. Output JSON + formatted table
```

#### `scripts/bash/generate-sections.sh`

**Purpose:** Generate document sections sequentially

**Inputs:**

- Reads `initiatives/$NUAA_INITIATIVE/plan.md`
- Reads section prompts from `templates/section-prompts/`

**Outputs:**

- Creates `initiatives/$NUAA_INITIATIVE/sections/01-section-name.md` for each section
- Returns JSON with section paths

**Logic:**

```bash
#!/bin/bash
# 1. Parse plan.md for section order
# 2. For each section:
#    a. Load appropriate section-prompt.md
#    b. Generate content (may invoke AI via API or instruct user)
#    c. Save to sections/ directory
# 3. Return paths to all generated sections
```

#### `scripts/bash/assemble-document.sh`

**Purpose:** Combine sections into final document

**Inputs:**

- Reads `initiatives/$NUAA_INITIATIVE/sections/*.md`
- Reads `initiatives/$NUAA_INITIATIVE/plan.md` for order

**Outputs:**

- Creates `initiatives/$NUAA_INITIATIVE/proposal.md`
- Exports `proposal.docx` (via pandoc or python-docx)
- Exports `proposal.pdf` (via pandoc or weasyprint)

**Logic:**

```bash
#!/bin/bash
# 1. Read section order from plan.md
# 2. Concatenate sections in order
# 3. Add TOC (auto-generated from headings)
# 4. Format according to funder requirements
# 5. Export to Word/PDF
```

#### `scripts/bash/review-document.sh`

**Purpose:** Final quality assurance check

**Inputs:**

- Reads `initiatives/$NUAA_INITIATIVE/proposal.md`
- Re-reads gates from `nuaa-kit/checklists/`

**Outputs:**

- Returns JSON: `{"status": "ready", "issues": []}`
- Console review report

**Logic:**

```bash
#!/bin/bash
# 1. Re-run gate validation
# 2. Check page/word count
# 3. Validate citations and references
# 4. Search for [PLACEHOLDER] markers
# 5. Aggregate issues
# 6. Output review report
```

### 6.3 Gate Checklist Format

Each gate is a markdown file with checklist items. The `check-gates.sh` script parses these.

**Example: `nuaa-kit/checklists/mission-alignment-gate.md`**

```markdown
# Mission Alignment Gate

This gate ensures the proposed program aligns with NUAA's core mission and values.

## Checklist

- [ ] **Lived Experience Leadership**: Does the program explicitly involve people with lived experience in leadership roles (design, delivery, evaluation)?
- [ ] **Harm Reduction**: Are harm reduction principles clearly embedded throughout (non-judgmental, non-coercive, evidence-based)?
- [ ] **Mission Advancement**: Does this initiative directly advance NUAA's mission to support the health and wellbeing of people who use drugs in NSW?
- [ ] **Community-Driven**: Is there evidence of community consultation or co-design?

## Pass Criteria

- All 4 items checked
- Evidence for each item is explicit in the plan (not assumed)

## Fail Criteria

- 2 or more items not addressed
- Evidence is vague or missing

## Warn Criteria

- 1 item not fully addressed (proceed with caution)
```

---

## 7. Risk Analysis & Mitigation

### 7.1 Adoption Risks

| Risk                                                   | Likelihood | Impact | Mitigation                                                                                                                                                   |
| ------------------------------------------------------ | ---------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Staff resist new workflow (prefer legacy commands)** | High       | Medium | - Maintain backward compatibility<br>- Provide both "Quick" and "Guided" modes<br>- Show time savings in guided mode<br>- Offer training sessions            |
| **Learning curve too steep**                           | Medium     | High   | - Create video tutorials<br>- Provide interactive walkthrough<br>- Simplify initial steps<br>- Offer templates for common scenarios                          |
| **AI agents struggle with NGO domain**                 | Medium     | High   | - Invest in comprehensive prompt engineering<br>- Create extensive examples in templates<br>- Iterate on constitution wording<br>- Test with multiple agents |

### 7.2 Technical Risks

| Risk                                           | Likelihood | Impact | Mitigation                                                                                                                   |
| ---------------------------------------------- | ---------- | ------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Script compatibility (Bash vs. PowerShell)** | Low        | Medium | - Develop both in parallel<br>- Use common JSON output format<br>- Automated testing on both platforms                       |
| **Gate validation logic too rigid**            | Medium     | Medium | - Allow manual overrides with justification<br>- Use warn/pass/fail (not just pass/fail)<br>- Iterate based on user feedback |
| **Document export quality issues**             | Medium     | High   | - Use proven libraries (pandoc, python-docx)<br>- Test exports with multiple funders<br>- Provide manual formatting guidance |

### 7.3 Organizational Risks

| Risk                                | Likelihood | Impact | Mitigation                                                                                                             |
| ----------------------------------- | ---------- | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Resource constraints (dev time)** | High       | High   | - Phase implementation (14 weeks is realistic)<br>- Prioritize core workflow first<br>- Accept technical debt for v1.0 |
| **Stakeholder misalignment**        | Low        | High   | - Regular demos to NUAA leadership<br>- Involve staff in UAT<br>- Iterate based on feedback                            |

---

## Appendix A: Comparison Tables

### A.1 Command Mapping

| Spec-Kit Command        | NUAA-CLI Equivalent      | Purpose                               |
| ----------------------- | ------------------------ | ------------------------------------- |
| `specify check`         | `nuaa check`             | Verify prerequisites and agent tools  |
| `specify init`          | `nuaa init`              | Initialize project with agent support |
| `/speckit.constitution` | `/nuaa.mission`          | Define governing principles           |
| `/speckit.specify`      | `/nuaa.specify`          | Create high-level specification       |
| `/speckit.clarify`      | `/nuaa.clarify`          | Resolve ambiguities interactively     |
| `/speckit.plan`         | `/nuaa.plan`             | Generate implementation/document plan |
| `/speckit.tasks`        | `/nuaa.sections`         | Break down into executable units      |
| `/speckit.implement`    | `/nuaa.draft`            | Execute plan and generate deliverable |
| `/speckit.analyze`      | `/nuaa.review`           | Quality assurance check               |
| N/A                     | `/nuaa.design` (legacy)  | Quick program design generation       |
| N/A                     | `/nuaa.propose` (legacy) | Quick proposal generation             |
| N/A                     | `/nuaa.measure` (legacy) | Quick evaluation framework generation |

### A.2 Artifact Mapping

| Spec-Kit Artifact                 | NUAA-CLI Equivalent                     | Location                            |
| --------------------------------- | --------------------------------------- | ----------------------------------- |
| `.specify/memory/constitution.md` | `memory/constitution.md`                | Project root                        |
| `specs/001-feature/spec.md`       | `initiatives/001-program/spec.md`       | Initiative directory                |
| `specs/001-feature/plan.md`       | `initiatives/001-program/plan.md`       | Initiative directory                |
| `specs/001-feature/tasks.md`      | `initiatives/001-program/sections/`     | Initiative directory                |
| `specs/001-feature/checklists/`   | `nuaa-kit/checklists/`                  | Shared across initiatives           |
| N/A                               | `initiatives/001-program/proposal.docx` | Initiative directory (final output) |

---

## Appendix B: Example Walkthrough

### Complete Workflow: Peer Naloxone Program Proposal

**Scenario:** NUAA needs to write a grant proposal to NSW Health for a peer-led naloxone distribution program in Western Sydney. They have 2 weeks until the deadline.

#### Day 1: Initialize and Set Mission

```bash
# Initialize project (if not already done)
nuaa init nuaa-projects --ai copilot --script ps

cd nuaa-projects

# Set mission constitution (one-time setup)
nuaa mission --set "NUAA exists to support the health and wellbeing of people who use drugs in NSW through peer-led advocacy, education, and support services grounded in harm reduction principles."

# AI generates memory/constitution.md with full constitution including ethical principles, programmatic standards, etc.
```

#### Day 2: Specify and Clarify

```bash
# Create high-level specification
/nuaa.specify Create a peer-led naloxone distribution program for people at risk of opioid overdose in Western Sydney. Include training, kit distribution, and follow-up support.

# AI creates initiatives/001-naloxone-distribution/spec.md with 4 [NEEDS CLARIFICATION] markers

# Resolve ambiguities
/nuaa.clarify

# AI asks 4 questions:
# Q1: Target age range? → User answers: "All adults 18+"
# Q2: Engagement level? → User answers: "Harder-to-reach populations not in treatment"
# Q3: Duration? → User answers: "12-month implementation"
# Q4: Follow-up support? → User answers: "Yes, peer phone check-ins monthly"

# AI updates spec.md, removes all markers
```

#### Day 3-4: Plan and Validate Gates

```bash
# Generate document plan
/nuaa.plan NSW Health grant application, maximum 15 pages, Word format required. Must include budget, evaluation, and letters of support.

# AI generates initiatives/001-naloxone-distribution/plan.md with:
# - Document structure (7 sections)
# - Section requirements
# - Pre-drafting gates

# AI automatically validates gates:
# ✓ Mission Alignment: PASS
# ✓ Ethical Standards: PASS
# ✓ Funder Alignment: PASS
# ⚠ Evidence-Based: WARN (missing local Western Sydney overdose data)
# ✓ Feasibility: PASS

# User addresses warning by adding NSW Ambulance data reference to spec

# Re-run gate check
/nuaa.review

# All gates now PASS
```

#### Day 5-10: Generate Sections

```bash
# Generate all sections sequentially
/nuaa.sections

# AI generates:
# Day 5: sections/01-executive-summary.md (1 page, compelling overview)
# Day 6: sections/02-background-need.md (2 pages, NUAA expertise + local data)
# Day 7: sections/03-program-design.md (4 pages, logic model, activities, innovation)
# Day 8: sections/04-methodology.md (3 pages, implementation phases, cultural safety)
# Day 9: sections/05-budget.md (2 pages, detailed line items with justification)
# Day 10: sections/06-evaluation.md (2 pages, indicators, data collection, reporting)
# Day 10: sections/07-sustainability.md (1 page, post-grant funding plan)

# User reviews each section as generated, provides feedback if needed
```

#### Day 11: Assemble and Review

```bash
# Assemble final document
/nuaa.draft --format all

# AI creates:
# - initiatives/001-naloxone-distribution/proposal.md (master markdown)
# - initiatives/001-naloxone-distribution/proposal.docx (formatted Word doc)
# - initiatives/001-naloxone-distribution/proposal.pdf (for internal review)

# Final quality review
/nuaa.review

# AI outputs:
# ✓ All sections present: 7/7
# ✓ Page count: 14 pages (within 15-page limit)
# ✓ Word count: 4,890 words
# ✓ Citations complete: 12 references
# ✓ No placeholders remaining
# ✓ All gates: PASS

# Status: READY FOR SUBMISSION
```

#### Day 12-14: Human Review and Submit

- NUAA leadership reviews `proposal.docx`
- Minor edits made directly in Word
- Letters of support attached
- Submitted to NSW Health portal 2 days before deadline

**Outcome:**

- High-quality proposal completed in 11 days (3 days ahead of deadline)
- All quality gates passed
- Mission alignment ensured throughout
- Staff confidence high due to structured process

---

## Conclusion

This evolution plan transforms NUAA-CLI from a **project scaffolder** to a **comprehensive NGO workflow orchestration tool**. By applying spec-kit's structured, principle-driven methodology to the NGO domain, we can:

1. **Improve Quality**: Every deliverable passes rigorous quality gates
2. **Increase Speed**: Structured workflow reduces decision paralysis
3. **Ensure Alignment**: Mission constitution keeps all work mission-driven
4. **Build Confidence**: Staff trust the process and outputs
5. **Scale Impact**: More time for programs, less time on paperwork

The 14-week implementation timeline is realistic and phased to allow for iteration. Backward compatibility ensures existing users are not disrupted.

**Next Steps:**

1. Review this plan with NUAA leadership
2. Secure resources (dev, testing, SME)
3. Begin Phase 0 (Foundation) implementation
4. Iterate based on user feedback throughout

---

**Document Version**: 1.0  
**Last Updated**: November 12, 2025  
**Maintained By**: NUAA CLI Development Team
