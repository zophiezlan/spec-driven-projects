<div align="center">
    <h1>🌱 NUAA Project</h1>
    <h3><em>AI-Assisted Project Management for NSW Users and AIDS Association</em></h3>
</div>

<p align="center">
    <strong>An open source project transforming program design, proposal writing, and impact measurement into systematic, AI-assisted workflows for NUAA.</strong>
</p>

<p align="center">
    <a href="https://github.com/zophiezlan/spec-driven-projects/actions/workflows/release.yml"><img src="https://github.com/zophiezlan/spec-driven-projects/actions/workflows/release.yml/badge.svg" alt="Release"/></a>
    <a href="https://github.com/zophiezlan/spec-driven-projects/stargazers"><img src="https://img.shields.io/github/stars/zophiezlan/spec-driven-projects?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/zophiezlan/spec-driven-projects/blob/main/LICENSE"><img src="https://img.shields.io/github/license/zophiezlan/spec-driven-projects" alt="License"/></a>
</p>

---

## Table of Contents

- [🤔 What is NUAA Kit?](#-what-is-nuaa-kit)
- [⚡ Get Started](#-get-started)
- [🎯 Core Features](#-core-features)
- [📋 Quick Start Guide](#-quick-start-guide)
- [🔧 Prerequisites](#-prerequisites)
- [📖 Learn More](#-learn-more)
- [👥 Maintainers](#-maintainers)
- [💬 Support](#-support)
- [📄 License](#-license)

## 🤔 What is NUAA Kit?

NUAA Kit is a specialized adaptation of Spec-Driven Development methodology designed specifically for **NSW Users and AIDS Association (NUAA)**. It transforms program design, proposal writing, and impact measurement into systematic, AI-assisted workflows integrated with Microsoft 365.

### Key Benefits

- **Program Design Made Easy**: Generate comprehensive program designs with logic models, stakeholder journeys, and risk assessments
- **Faster Proposal Writing**: Automatically create funding proposals with budget tables, methodologies, and timelines
- **Better Impact Measurement**: Define clear evaluation frameworks with indicators and data collection templates
- **Built-in NUAA Principles**: Every output incorporates peer-led approaches, harm reduction philosophy, and ethical practices

## ⚡ Get Started

### Quick Installation

NUAA Kit is available in the `/nuaa-kit` directory of this repository. To start using it:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zophiezlan/spec-driven-projects.git
   cd spec-driven-projects/nuaa-kit
   ```

2. **Review the Quick Start Guide:**
   ```bash
   cat QUICKSTART.md
   ```

3. **Try your first command:**
   Launch your AI assistant in the `nuaa-kit` directory and use:
   ```bash
   /nuaa.design Design a peer-led workshop series on stigma reduction in healthcare settings
   ```

### System Requirements

- **Linux/macOS/Windows**
- [Supported AI coding agent](#-supported-ai-agents) (Claude Code, GitHub Copilot, etc.)
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## 🎯 Core Features

### 1. Program Design & Logic Models (`/nuaa.design`)

Generate comprehensive program designs with:
- Automatic logic model creation (Inputs → Activities → Outputs → Outcomes → Impact)
- Stakeholder journey mapping
- Risk assessment integration
- Built-in NUAA principles and ethics

### 2. Proposal & Grant Writing (`/nuaa.propose`)

Create professional funding proposals with:
- Automatic budget table generation
- Methodology breakdown from program design
- Timeline chart creation
- NUAA capability statement integration
- Export to Word with professional formatting

### 3. Impact Measurement & Evaluation (`/nuaa.measure`)

Define clear impact frameworks with:
- Indicator development (process, output, outcome, impact)
- Evaluation planning
- Data collection template generation
- Export to Excel for tracking

## 📋 Quick Start Guide

### Deploy in Weeks

#### Phase 1: Core Setup (Week 1)
1. Install dependencies
2. Configure Microsoft 365 integration
3. Import NUAA-specific templates
4. Train staff on first command: `/nuaa.design`

#### Phase 2: Initial Use (Week 2-3)
- Create first program design using logic model generator
- Generate proposal for upcoming funding opportunity
- Test impact measurement framework

#### Phase 3: Iteration (Week 4+)
- Refine based on staff feedback
- Expand to additional commands
- Full Microsoft 365 automation deployment

## 🤖 Supported AI Agents

NUAA Kit works with all major AI coding assistants:

| Agent                                                     | Support | Notes                                             |
|-----------------------------------------------------------|---------|---------------------------------------------------|
| [Claude Code](https://www.anthropic.com/claude-code)      | ✅ |                                                   |
| [GitHub Copilot](https://code.visualstudio.com/)          | ✅ |                                                   |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ✅ |                                                   |
| [Cursor](https://cursor.sh/)                              | ✅ |                                                   |
| [Qwen Code](https://github.com/QwenLM/qwen-code)          | ✅ |                                                   |
| [opencode](https://opencode.ai/)                          | ✅ |                                                   |
| [Windsurf](https://windsurf.com/)                         | ✅ |                                                   |

For a complete list of supported agents, see the [NUAA Kit README](./nuaa-kit/README.md).

## 🔧 Prerequisites

### Required
- **Linux/macOS/Windows** operating system
- **[Git](https://git-scm.com/downloads)** for version control
- **[Python 3.11+](https://www.python.org/downloads/)** for CLI tools
- **[uv](https://docs.astral.sh/uv/)** for package management
- **AI coding agent** (see supported list above)

### Optional
- **Microsoft 365** for full integration features (Word, Excel, SharePoint)
- **Microsoft Teams** for collaboration features
- **Power Automate** for workflow automation

## 📖 Learn More

### NUAA Kit Documentation
- **[NUAA Kit README](./nuaa-kit/README.md)** - Complete guide to NUAA Kit features
- **[Quick Start Guide](./nuaa-kit/QUICKSTART.md)** - Week-by-week onboarding for staff
- **[Status & Roadmap](./nuaa-kit/STATUS.md)** - Current implementation status
- **[Workflow Diagram](./nuaa-kit/docs/workflow-diagram.md)** - Visual guide to program lifecycle
- **[Evolution Guide](./nuaa-kit/docs/evolution-guide.md)** - Maintaining program designs over time

### NUAA Examples
- **[NUAA Examples](./NUAA-examples/)** - Real NUAA program documents and examples
- Strategic plans, constitutions, and reporting examples

### Technical References
- **[Accessibility Guidelines](./nuaa-kit/accessibility-guidelines.md)** - Making outputs accessible
- **[Evaluation Data Dictionary](./nuaa-kit/evaluation-data-dictionary.md)** - Standard indicators
- **[Glossary](./nuaa-kit/glossary.md)** - NUAA-specific terminology

## 🌟 NUAA-Specific Principles

Every command and template incorporates:

- **Peer-led approach** - Lived experience at center
- **Harm reduction philosophy** - Non-judgmental, evidence-based
- **Consumer remuneration** - Fair payment for contributions ($300/session standard)
- **Cultural safety** - Respectful of diverse communities
- **Transparency** - Open processes and decision-making
- **Impact focus** - Outcomes over outputs
- **Ethical practice** - Do no harm, informed consent

## 📽️ Learn About Spec-Driven Development

NUAA Kit is built on Spec-Driven Development methodology. Watch our [video overview](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv) to understand the foundation:

[![Spec Kit video header](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

For a complete guide to Spec-Driven Development, see [spec-driven.md](./spec-driven.md).

## 🔍 Troubleshooting

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## 👥 Maintainers

- Den Delimarsky ([@localden](https://github.com/localden))
- John Lam ([@jflam](https://github.com/jflam))

## 💬 Support

For support, please open a [GitHub issue](https://github.com/zophiezlan/spec-driven-projects/issues/new). We welcome bug reports, feature requests, and questions about using NUAA Kit.

## 🙏 Acknowledgements

This project is heavily influenced by and based on the work and research of [John Lam](https://github.com/jflam) and the Spec-Driven Development methodology.

## 📄 License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) file for the full terms.

---

**Built for NUAA by NUAA principles** 🌱
