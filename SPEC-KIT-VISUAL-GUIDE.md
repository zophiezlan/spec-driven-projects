# NUAA-CLI Evolution: Visual Guide

**Purpose:** Visual representations of the spec-kit methodology adaptation  
**Audience:** All stakeholders  
**Last Updated:** November 12, 2025

---

## 📐 Architecture Evolution

### Current Architecture (Simple)

```
┌─────────────────────────────────────────────────────────┐
│                      NUAA-CLI                           │
│                                                         │
│  User → Single Command → Full Document                  │
│                                                         │
│  /nuaa.design ──────────────→ program-design.md         │
│  /nuaa.propose ─────────────→ proposal.md               │
│  /nuaa.measure ─────────────→ impact-framework.md       │
│                                                         │
│  No intermediate steps                                  │
│  No quality gates                                       │
│  Limited control                                        │
└─────────────────────────────────────────────────────────┘
```

### Target Architecture (Structured)

```
┌─────────────────────────────────────────────────────────────────────┐
│                         NUAA-CLI Enhanced                           │
│                                                                     │
│  Step 1: Mission          ┌──────────────────┐                      │
│  /nuaa.mission ──────────→│ Constitution     │                      │
│                           │ (Values & Ethics)│                      │
│                           └────────┬─────────┘                      │
│                                    │                                │
│  Step 2: Specify          ┌────────▼─────────┐                      │
│  /nuaa.specify ──────────→│ Program Spec     │                      │
│                           │ [NEEDS           │                      │
│                           │  CLARIFICATION]  │                      │
│                           └────────┬─────────┘                      │
│                                    │                                │
│  Step 3: Clarify          ┌────────▼─────────┐                      │
│  /nuaa.clarify ──────────→│ Updated Spec     │                      │
│                           │ (No ambiguities) │                      │
│                           └────────┬─────────┘                      │
│                                    │                                │
│  Step 4: Plan             ┌────────▼─────────┐                      │
│  /nuaa.plan ─────────────→│ Document Plan    │                      │
│                           │ (Structure)      │                      │
│                           └────────┬─────────┘                      │
│                                    │                                │
│  Gate Validation          ┌────────▼─────────┐                      │
│  (Automatic) ────────────→│ Quality Gates    │                      │
│                           │ ✓ Mission        │                     │
│                           │ ✓ Ethical        │                     │
│                           │ ✓ Funder         │                     │
│                           │ ✓ Evidence       │                     │
│                           │ ✓ Feasibility    │                     │
│                           └────────┬─────────┘                      │
│                                    │                                │
│  Step 5: Sections         ┌────────▼─────────┐                      │
│  /nuaa.sections ─────────→│ Section 1        │                      │
│                           │ Section 2        │                      │
│                           │ Section 3        │                      │
│                           │ ... (Review each)│                      │
│                           └────────┬─────────┘                      │
│                                    │                                │
│  Step 6: Draft            ┌────────▼─────────┐                      │
│  /nuaa.draft ────────────→│ Final Document   │                      │
│                           │ (.md, .docx,     │                      │
│                           │  .pdf)           │                      │
│                           └────────┬─────────┘                      │
│                                    │                                │
│  Step 7: Review           ┌────────▼─────────┐                      │
│  /nuaa.review ───────────→│ Quality Report   │                      │
│                           │ READY FOR        │                      │
│                           │ SUBMISSION       │                      │
│                           └──────────────────┘                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Workflow Comparison

### Spec-Kit: Software Development

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Constitution │────→│   Feature    │────→│  Clarify     │
│   (Tech      │     │     Spec     │     │ Ambiguities  │
│  Principles) │     │ (User Stories)│    │              │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                   │
        ┌──────────────────────────────────────────┘
        │
        ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Implementation│────→│   Generate   │────→│  Executable  │
│     Plan      │     │    Tasks     │     │     Code     │
│ (Architecture)│     │ (Step-by-step)│    │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

### NUAA-CLI: NGO Program Development

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Mission    │────→│   Program    │────→│  Clarify     │
│ Constitution │     │     Spec     │     │ Ambiguities  │
│(Values/Ethics)│     │ (Outcomes)   │     │              │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                   │
        ┌──────────────────────────────────────────┘
        │
        ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Document    │────→│   Generate   │────→│Professional  │
│    Plan      │     │   Sections   │     │  Document    │
│ (Structure)  │     │ (Step-by-step)│    │ (.docx/.pdf) │
└──────────────┘     └──────────────┘     └──────────────┘
        │                                          │
        ▼                                          ▼
┌──────────────┐                          ┌──────────────┐
│ Quality Gates│                          │    Review    │
│ (Validation) │                          │   & Submit   │
└──────────────┘                          └──────────────┘
```

---

## 🚪 Quality Gates Deep Dive

### Gate Flow

```
                    ┌──────────────────────┐
                    │   Document Plan      │
                    │      Generated       │
                    └──────────┬───────────┘
                               │
                               ▼
        ┌──────────────────────────────────────┐
        │       GATE 1: Mission Alignment      │
        │  ✓ Peer-led approach?                │
        │  ✓ Harm reduction embedded?          │
        │  ✓ Advances organizational mission?  │
        └──────────────┬───────────────────────┘
                       │ PASS
                       ▼
        ┌──────────────────────────────────────┐
        │       GATE 2: Ethical Standards      │
        │  ✓ Data privacy addressed?           │
        │  ✓ Cultural safety ensured?          │
        │  ✓ Inclusive language used?          │
        │  ✓ Informed consent planned?         │
        └──────────────┬───────────────────────┘
                       │ PASS
                       ▼
        ┌──────────────────────────────────────┐
        │       GATE 3: Funder Alignment       │
        │  ✓ Matches funder priorities?        │
        │  ✓ Budget within range?              │
        │  ✓ All sections included?            │
        │  ✓ Timeline realistic?               │
        └──────────────┬───────────────────────┘
                       │ PASS
                       ▼
        ┌──────────────────────────────────────┐
        │    GATE 4: Evidence-Based Practice   │
        │  ✓ Research cited?                   │
        │  ✓ Outcome measures defined?         │
        │  ✓ Evaluation rigorous?              │
        │  ✓ Assumptions explicit?             │
        └──────────────┬───────────────────────┘
                       │ WARN (add local data)
                       ▼
        ┌──────────────────────────────────────┐
        │       GATE 5: Feasibility            │
        │  ✓ NUAA has capacity?                │
        │  ✓ Partnerships confirmed?           │
        │  ✓ Budget justified?                 │
        │  ✓ Risks identified?                 │
        └──────────────┬───────────────────────┘
                       │ PASS
                       ▼
            ┌───────────────────────┐
            │  All Gates Passed     │
            │  (1 warning addressed)│
            │                       │
            │  PROCEED TO DRAFTING  │
            └───────────────────────┘
```

### Gate Result Scenarios

```
┌─────────────────────────────────────────────────────────────┐
│                       SCENARIO A                            │
│                                                             │
│  All Gates: ✓ PASS                                          │
│  ────────────────────────────────────────────────           │
│  Result: Proceed to drafting automatically                  │
│  User Action: None required                                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                       SCENARIO B                            │
│                                                             │
│  4 Gates: ✓ PASS                                            │
│  1 Gate:  ⚠ WARN                                            │
│  ────────────────────────────────────────────────           │
│  Result: Warning displayed, can proceed with acknowledgment │
│  User Action: "I acknowledge warning and choose to proceed" │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                       SCENARIO C                            │
│                                                             │
│  3 Gates: ✓ PASS                                            │
│  2 Gates: ✗ FAIL                                            │
│  ────────────────────────────────────────────────           │
│  Result: Drafting blocked, remediation required             │
│  User Action: Address failed gates, re-run validation       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 User Journey Comparison

### Current: Quick Mode (Legacy)

```
Day 1
├── User: Launch AI agent in nuaa-kit directory
├── User: Type /nuaa.propose "Peer naloxone program" "NSW Health" "$50k" "12 months"
├── AI: Generate 15-page proposal in 10 minutes
└── User: Review full document
    ├── Find gaps (no cultural safety section)
    ├── Find errors (budget doesn't match narrative)
    └── Manually fix issues (2-3 hours)

Day 2
├── User: Submit proposal (nervous about quality)
└── Wait for funder response
```

**Total Time:** ~3-4 hours  
**Quality Confidence:** Medium  
**User Control:** Low

### Target: Guided Mode (New)

```
Day 1: Foundation (30 minutes)
├── User: /nuaa.mission --set "NUAA's mission is..."
└── AI: Generate mission constitution

Day 2: Specification (45 minutes)
├── User: /nuaa.specify "Peer naloxone distribution program..."
├── AI: Generate spec with 4 [NEEDS CLARIFICATION] markers
├── User: /nuaa.clarify
├── AI: Ask 4 targeted questions
├── User: Answer questions
└── AI: Update spec

Day 3: Planning (1 hour)
├── User: /nuaa.plan "NSW Health grant, 15 pages, Word format"
├── AI: Generate document plan
├── AI: Run quality gates automatically
│   ├── ✓ Mission Alignment: PASS
│   ├── ✓ Ethical Standards: PASS
│   ├── ✓ Funder Alignment: PASS
│   ├── ⚠ Evidence-Based: WARN (add local data)
│   └── ✓ Feasibility: PASS
├── User: Add NSW Ambulance data reference
└── AI: Re-validate → All PASS

Days 4-8: Section Generation (4 hours spread over 5 days)
├── User: /nuaa.sections
├── AI: Generate Section 1 (Executive Summary)
├── User: Review & approve
├── AI: Generate Section 2 (Background)
├── User: Review & approve
├── ... (continues for all 7 sections)
└── User: High confidence (reviewed each section)

Day 9: Assembly (15 minutes)
├── User: /nuaa.draft
└── AI: Assemble sections → proposal.docx, proposal.pdf

Day 10: Review (10 minutes)
├── User: /nuaa.review
├── AI: Final quality check
│   ├── ✓ All sections present: 7/7
│   ├── ✓ Page count: 14/15
│   ├── ✓ Citations complete: 12
│   ├── ✓ No placeholders
│   └── ✓ All gates: PASS
└── Status: READY FOR SUBMISSION

Day 11: Submit (5 minutes)
├── User: Leadership review (minor edits only)
└── User: Submit with confidence
```

**Total Time:** ~7 hours (spread over 11 days)  
**Quality Confidence:** High  
**User Control:** Very High

---

## 🎯 Impact Visualization

### Time Distribution

```
LEGACY MODE (Quick)
┌────────────────────────────────────────────────────┐
│ Generation: 10 min ████                            │
│ Review & Fix: 3 hours ████████████████████████████ │
│ Total: ~3.5 hours                                  │
└────────────────────────────────────────────────────┘

GUIDED MODE (New)
┌────────────────────────────────────────────────────┐
│ Mission (one-time): 30 min ███████                 │
│ Specify & Clarify: 45 min ██████████               │
│ Plan & Gates: 1 hour ██████████████                │
│ Section Generation: 4 hours ███████████████████████│
│ Assembly & Review: 25 min ██████                   │
│ Total: ~7 hours (but spread over days)             │
└────────────────────────────────────────────────────┘
```

### Quality Improvement

```
            Low                    Medium                    High
             │                       │                       │
Legacy Mode: └───────────────────────┼───────────────────────┤
                                     ▲                       │
                                   Quality                   │
                                 Confidence                  │
                                                             │
Guided Mode: ────────────────────────────────────────────────┘
                                                             ▲
                                                       High Quality
                                                        Confidence
```

### Proposal Success Rate (Hypothetical)

```
Before NUAA-CLI (Manual):
Success Rate: 40% ████████████████████

With Legacy Mode:
Success Rate: 60% ██████████████████████████████

With Guided Mode:
Success Rate: 85% ██████████████████████████████████████████
```

---

## 🏗️ Directory Structure Evolution

### Before

```
nuaa-projects/
├── program-designs/
│   └── various-files.md (unstructured)
├── proposals/
│   └── various-files.docx (unstructured)
└── memory/
    └── constitution.md (unused template)
```

### After (Target)

```
nuaa-projects/
├── memory/
│   └── constitution.md (ACTIVE - referenced by all commands)
│
├── initiatives/
│   ├── 001-naloxone-distribution/
│   │   ├── spec.md (program specification)
│   │   ├── plan.md (document structure)
│   │   ├── sections/
│   │   │   ├── 01-executive-summary.md
│   │   │   ├── 02-background-need.md
│   │   │   ├── 03-program-design.md
│   │   │   ├── 04-methodology.md
│   │   │   ├── 05-budget.md
│   │   │   ├── 06-evaluation.md
│   │   │   └── 07-sustainability.md
│   │   ├── proposal.md (assembled markdown)
│   │   ├── proposal.docx (final document)
│   │   └── proposal.pdf (for review)
│   │
│   ├── 002-stigma-workshops/
│   │   └── [similar structure]
│   │
│   └── 003-lgbtiq-support/
│       └── [similar structure]
│
└── nuaa-kit/
    ├── commands/ (enhanced with new commands)
    ├── templates/ (section-specific prompts added)
    ├── checklists/ (NEW - quality gates)
    └── docs/ (migration guides added)
```

---

## 🔄 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    GUIDED MODE DATA FLOW                    │
└─────────────────────────────────────────────────────────────┘

USER INPUT                 AI PROCESSING              OUTPUT
───────────                ─────────────              ──────

Mission statement    ──→   Load template        ──→   constitution.md
                           + populate                 (stored in memory/)
                                    │
                                    ├──────────────────────┐
                                    │                      │
Program description  ──→   Read constitution        ──→   spec.md
                           + generate spec               (with [NEEDS
                           + mark ambiguities             CLARIFICATION])
                                    │
                                    │
User answers Q&A     ──→   Update spec          ──→   spec.md (updated,
                           + remove markers              no ambiguities)
                                    │
                                    │
Funder requirements  ──→   Read spec                ──→   plan.md
                           + Read constitution           (document
                           + generate structure          structure)
                                    │
                                    │
[Automatic]          ──→   Read plan                ──→   Gate validation
                           + check against gates         report (JSON)
                                    │                         │
                                    │                         │
                                    ├─── PASS ────────────────┘
                                    │
[Sections command]   ──→   For each section:        ──→   sections/*.md
                           - Read plan                   (01-summary.md,
                           - Read constitution            02-background.md,
                           - Read spec                    etc.)
                           - Load section prompt
                           - Generate content
                                    │
                                    │
[Draft command]      ──→   Read all sections        ──→   proposal.md
                           + assemble in order           proposal.docx
                           + add TOC                     proposal.pdf
                           + format for funder
                                    │
                                    │
[Review command]     ──→   Re-run gates            ──→   Review report
                           + check formatting            (JSON + console)
                           + validate citations
                           + check placeholders
```

---

## 📈 Adoption Strategy

### Rollout Phases

```
PHASE 0: INTERNAL TESTING (Weeks 1-4)
┌──────────────────────────────────────────┐
│ Development Team                         │
│ ↓                                        │
│ Build mission constitution system        │
│ ↓                                        │
│ Internal testing with sample programs    │
│ ↓                                        │
│ Refine based on feedback                 │
└──────────────────────────────────────────┘

PHASE 1: PILOT GROUP (Weeks 5-8)
┌──────────────────────────────────────────┐
│ 3-5 NUAA Staff Members                   │
│ ↓                                        │
│ Training sessions (2 hours)              │
│ ↓                                        │
│ Use guided mode for real proposals       │
│ ↓                                        │
│ Weekly feedback sessions                 │
└──────────────────────────────────────────┘

PHASE 2: EXPANDED ROLLOUT (Weeks 9-12)
┌──────────────────────────────────────────┐
│ All NUAA Staff                           │
│ ↓                                        │
│ Organization-wide training               │
│ ↓                                        │
│ Both modes available (quick + guided)    │
│ ↓                                        │
│ Ongoing support & iteration              │
└──────────────────────────────────────────┘

PHASE 3: OPTIMIZATION (Week 13+)
┌──────────────────────────────────────────┐
│ Continuous Improvement                   │
│ ↓                                        │
│ Analyze usage patterns                   │
│ ↓                                        │
│ Refine prompts & gates                   │
│ ↓                                        │
│ Add new features based on needs          │
└──────────────────────────────────────────┘
```

---

## 📝 Key Takeaways

### For Leadership

```
✓ Investment: 14 weeks development time
✓ ROI: 60% time savings on proposals
✓ Risk: Mitigated by keeping legacy mode
✓ Impact: Higher quality, more funded programs
```

### For Staff

```
✓ Learning Curve: Moderate (2-hour training)
✓ Control: Much higher than current
✓ Quality: Built-in quality assurance
✓ Choice: Use quick or guided mode
```

### For Development

```
✓ Complexity: Manageable (phased approach)
✓ Tech Stack: Python, typer, rich (existing)
✓ Testing: User acceptance with NUAA staff
✓ Maintenance: Iterative improvement
```

---

**Document Version:** 1.0  
**Visual Style:** ASCII diagrams for maximum compatibility  
**Next Update:** After Phase 0 completion
