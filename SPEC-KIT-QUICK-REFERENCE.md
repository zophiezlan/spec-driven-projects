# Quick Reference: Spec-Kit Methodology for NUAA-CLI

**Purpose:** Rapid reference for applying spec-kit's structured approach to NGO workflows  
**Audience:** Developers, project managers, NUAA staff  
**Last Updated:** November 12, 2025

---

## 🎯 Core Principle

**Spec-Kit Principle:** Structured, principle-driven software development  
**NUAA-CLI Adaptation:** Structured, mission-driven NGO program documentation

---

## 🔄 Workflow Mapping

### Spec-Kit (6 Phases)

```
Constitution → Specify → Clarify → Plan → Tasks → Implement
```

### NUAA-CLI (7 Phases)

```
Mission → Specify → Clarify → Plan → Sections → Draft → Review
```

---

## 📝 Command Mapping

| Spec-Kit                | NUAA-CLI         | Purpose           | Output                               |
| ----------------------- | ---------------- | ----------------- | ------------------------------------ |
| `/speckit.constitution` | `/nuaa.mission`  | Define principles | `memory/constitution.md`             |
| `/speckit.specify`      | `/nuaa.specify`  | Create spec       | `initiatives/NNN-name/spec.md`       |
| `/speckit.clarify`      | `/nuaa.clarify`  | Ask questions     | Updated `spec.md`                    |
| `/speckit.plan`         | `/nuaa.plan`     | Structure doc     | `initiatives/NNN-name/plan.md`       |
| `/speckit.tasks`        | `/nuaa.sections` | Break down        | `initiatives/NNN-name/sections/*.md` |
| `/speckit.implement`    | `/nuaa.draft`    | Generate          | `initiatives/NNN-name/proposal.docx` |
| `/speckit.analyze`      | `/nuaa.review`   | Quality check     | Review report                        |

---

## 🚪 Gate Translation

### Software Gates → NGO Gates

| Software Gate         | NGO Equivalent        | Key Checks                                    |
| --------------------- | --------------------- | --------------------------------------------- |
| **Simplicity**        | **Mission Alignment** | Peer-led? Harm reduction? Mission-driven?     |
| **Anti-Abstraction**  | **Ethical Standards** | Privacy? Cultural safety? Inclusive language? |
| **Integration-First** | **Funder Alignment**  | Matches priorities? Budget realistic?         |
| _(New)_               | **Evidence-Based**    | Research cited? Outcomes defined?             |
| _(New)_               | **Feasibility**       | Capacity? Partnerships? Risks managed?        |

---

## 📋 File Structure Comparison

### Spec-Kit Structure

```
.specify/
  memory/
    constitution.md
specs/
  001-feature-name/
    spec.md
    plan.md
    tasks.md
    checklists/
```

### NUAA-CLI Structure

```
memory/
  constitution.md
initiatives/
  001-program-name/
    spec.md
    plan.md
    sections/
      01-executive-summary.md
      02-background.md
      ...
    proposal.docx
nuaa-kit/
  checklists/
```

---

## 🎨 Template Comparison

### Spec-Kit Template Purpose

- **spec.md:** What software should do (user stories, requirements)
- **plan.md:** How to build it (architecture, tech stack, components)
- **tasks.md:** Step-by-step coding tasks

### NUAA-CLI Template Purpose

- **spec.md:** What program should achieve (outcomes, activities, beneficiaries)
- **plan.md:** How to document it (proposal structure, section requirements)
- **sections/\*.md:** Step-by-step section drafts

---

## 🔍 Key Differences

| Aspect             | Spec-Kit                      | NUAA-CLI                          |
| ------------------ | ----------------------------- | --------------------------------- |
| **Domain**         | Software development          | NGO program management            |
| **Output**         | Executable code               | Professional documents            |
| **Validation**     | Unit tests, integration tests | Quality gates, peer review        |
| **Stakeholders**   | Developers, users             | NGO staff, funders, communities   |
| **Success Metric** | Working software              | Funded programs                   |
| **Language**       | Technical (APIs, databases)   | Mission-driven (outcomes, impact) |

---

## 💡 Key Innovations NUAA-CLI Adds

### 1. Mission Constitution

**What:** Living document encoding organizational values  
**Why:** Ensures all AI outputs are mission-aligned  
**Spec-Kit Equivalent:** Code quality constitution

### 2. Interactive Clarification

**What:** AI asks targeted questions about ambiguities  
**Why:** Reduces guesswork, increases accuracy  
**Spec-Kit Equivalent:** Direct copy (excellent feature!)

### 3. Pre-Drafting Gates

**What:** 5 quality checkpoints before document generation  
**Why:** Catches issues early, ensures quality  
**Spec-Kit Equivalent:** Pre-implementation gates (adapted for NGO context)

### 4. Section-by-Section Generation

**What:** Break documents into reviewable chunks  
**Why:** Increases control, reduces AI hallucinations  
**Spec-Kit Equivalent:** Task-by-task implementation

### 5. Dual-Mode Operation

**What:** Legacy "quick mode" + new "guided mode"  
**Why:** No disruption, gradual adoption  
**Spec-Kit Equivalent:** Not applicable (spec-kit is one mode)

---

## 📊 Impact Metrics

### Spec-Kit Goals

- ✅ Reduce development time by 40%
- ✅ Improve code quality through gates
- ✅ Ensure architectural consistency
- ✅ Enable AI-assisted development

### NUAA-CLI Goals

- ✅ Reduce proposal writing time by 60%
- ✅ Improve document quality through gates
- ✅ Ensure mission consistency
- ✅ Enable AI-assisted documentation

---

## 🛠️ Implementation Checklist

### Phase 0: Foundation (Weeks 1-2)

- [ ] Create `commands/mission.md`
- [ ] Create default mission constitution template
- [ ] Update agent context scripts to inject constitution
- [ ] Add CLI command: `nuaa mission`

### Phase 1: Specify & Clarify (Weeks 3-4)

- [ ] Create `commands/specify.md`
- [ ] Create `commands/clarify.md`
- [ ] Create `scripts/create-new-initiative.sh`
- [ ] Implement `[NEEDS CLARIFICATION]` marker system

### Phase 2: Planning & Gates (Weeks 5-7)

- [ ] Create `commands/plan.md`
- [ ] Create all 5 gate checklists
- [ ] Create `scripts/setup-plan.sh`
- [ ] Create `scripts/check-gates.sh`

### Phase 3: Section Drafting (Weeks 8-10)

- [ ] Create `commands/sections.md`
- [ ] Create section-specific prompts
- [ ] Create `scripts/generate-sections.sh`

### Phase 4: Assembly & Review (Weeks 11-12)

- [ ] Create `commands/draft.md`
- [ ] Create `commands/review.md`
- [ ] Create `scripts/assemble-document.sh`
- [ ] Create `scripts/review-document.sh`

### Phase 5: Migration (Weeks 13-14)

- [ ] Add deprecation notices to legacy commands
- [ ] Create migration guide
- [ ] Update README with mode comparison
- [ ] Test backward compatibility

---

## 🎓 Learning from Spec-Kit

### What to Adopt Directly

✅ **Constitution concept** - Governing principles document  
✅ **Clarification workflow** - Interactive ambiguity resolution  
✅ **Quality gates** - Pre-work validation checkpoints  
✅ **Phased workflow** - Step-by-step progression  
✅ **JSON output from scripts** - Structured data exchange

### What to Adapt

🔄 **Gate content** - Software → NGO context  
🔄 **Terminology** - Features → Programs, Tasks → Sections  
🔄 **Validation** - Tests → Document review  
🔄 **Output format** - Code → Word/PDF documents

### What NOT to Adopt

❌ **Test-driven development** - Not applicable to documents  
❌ **Code compilation** - Not applicable to documents  
❌ **CI/CD pipelines** - Different workflow for documents  
❌ **Version control of code** - Use version control of markdown instead

---

## 🚨 Common Pitfalls to Avoid

### 1. Over-Engineering

**Risk:** Making workflow too complex  
**Mitigation:** Keep dual mode (quick + guided)

### 2. Rigid Gates

**Risk:** Gates block reasonable work  
**Mitigation:** Allow overrides with justification

### 3. Poor AI Prompts

**Risk:** AI generates poor content despite structure  
**Mitigation:** Invest heavily in prompt engineering

### 4. Ignoring User Feedback

**Risk:** Building wrong features  
**Mitigation:** Continuous testing with NUAA staff

### 5. Breaking Backward Compatibility

**Risk:** Disrupting existing users  
**Mitigation:** Keep all legacy commands working

---

## 📚 Resources

### Primary Documents

- **This Quick Reference:** `SPEC-KIT-QUICK-REFERENCE.md`
- **Detailed Evolution Plan:** `SPEC-KIT-EVOLUTION-PLAN.md`
- **Executive Summary:** `SPEC-KIT-EVOLUTION-SUMMARY.md`

### Spec-Kit Resources

- **GitHub:** https://github.com/github/spec-kit
- **Documentation:** https://github.com/github/spec-kit/tree/main/docs
- **Spec-Driven Methodology:** `spec-driven.md` in spec-kit repo

### NUAA-CLI Resources

- **Agent Guide:** `AGENTS.md`
- **Current Kit:** `nuaa-kit/README.md`
- **Contributing:** `CONTRIBUTING.md`

---

## 🤝 Getting Help

### For Understanding Spec-Kit

- Read spec-kit's `README.md` and `spec-driven.md`
- Review spec-kit's command templates
- Study the constitution concept

### For NUAA-CLI Evolution

- Review the detailed evolution plan
- Contact NUAA CLI development team
- Participate in user testing sessions

---

**Version:** 1.0  
**Status:** Reference Document  
**Next Update:** After Phase 0 completion
