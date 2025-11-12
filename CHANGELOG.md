# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to the NUAA CLI and templates are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2025-11-12

### Added - Phase 3: Section-by-Section Drafting System

#### New Commands

- **`nuaa draft <section> [--initiative INIT] [--resolve]`** - Draft a document section with AI assistance
  - Creates section file structure from template
  - Auto-loads specification, plan, dependencies, and mission constitution
  - Drafts content meeting gate criteria with context awareness
  - Supports placeholder markers for missing information (`[PLACEHOLDER: question]`)
  - Updates plan.md status to "In Progress" automatically
  - Supports placeholder resolution mode (`--resolve`) to fill in missing information
  - Supports both CLI and AI agent usage (`/nuaa.draft`)

- **`nuaa revise <section> [--initiative INIT] [--type TYPE] [--feedback "..."]`** - Revise a drafted section
  - Four revision types: placeholder, feedback, consistency, enhancement
  - Placeholder resolution: Asks for and incorporates missing information
  - Feedback incorporation: Addresses specific gate validation feedback
  - Consistency update: Aligns with changed dependency sections
  - Quality enhancement: Strengthens evidence, clarity, and mission alignment
  - Updates revision history automatically
  - Maintains document structure and preserves working content
  - Supports both CLI and AI agent usage (`/nuaa.revise`)

#### Templates

- **`nuaa-kit/templates/section-template.md`** - Section draft structure template
  - Metadata section (initiative, gate, status, last updated)
  - Section purpose statement
  - Main content area
  - References section for citations
  - Notes for reviewers
  - Revision history tracking

- **`nuaa-kit/commands/draft.md`** - AI agent command template for section drafting
  - Context loading workflow (plan → spec → mission → dependencies → related sections)
  - Content requirements by gate (Gate 1-5 quality standards)
  - Placeholder handling guidelines with documentation format
  - Content guidelines by document type (proposals, designs, reports, impact)
  - Context injection examples with real-world scenarios
  - Placeholder resolution workflow
  - Best practices for good vs. bad placeholders
  - Document type adaptation (tone, focus, evidence, length)

- **`nuaa-kit/commands/revise.md`** - AI agent command template for section revision
  - Four revision types with detailed workflows
  - Type 1: Placeholder resolution (filling in missing information)
  - Type 2: Feedback incorporation (addressing gate validation feedback)
  - Type 3: Consistency update (aligning with changed dependencies)
  - Type 4: Quality enhancement (strengthening evidence and clarity)
  - Revision guidelines (do's and don'ts)
  - Revision history format
  - Integration with overall workflow
  - Examples by revision type
  - Troubleshooting common issues

#### Scripts

- **`scripts/bash/create-section-draft.sh`** - Section creation script for Unix/Linux/macOS
  - Creates `initiatives/NNN-slug/sections/` directory structure
  - Generates section file from template with metadata substitution
  - Extracts gate and purpose from plan.md automatically
  - Updates plan.md status to "In Progress"
  - JSON output mode for programmatic integration with CLI
  - Auto-detects most recent initiative if not specified
  - Validates section exists in plan before creating file

- **`scripts/powershell/create-section-draft.ps1`** - Section creation script for Windows
  - Feature parity with bash version
  - PowerShell-native implementation
  - Same JSON output format for CLI integration

#### Documentation

- Updated workflow documentation showing Draft → Validate → Revise cycle
- Context awareness explanation (specification, mission, dependencies, related sections)
- Placeholder management workflow
- Revision type selection guidance
- Integration with Phase 2 (planning and gate validation)

### Design Decisions

- **Minimal changes**: Only sections being drafted require changes, not the entire document
- **Context awareness**: AI automatically loads all relevant context for consistent drafting
- **Placeholder-driven**: Missing information is explicitly tracked, not left implicit
- **Targeted revisions**: Revisions update only what needs changing, preserving working content
- **Gate integration**: Drafting directly ties to gate validation from Phase 2
- **Revision history**: All changes are tracked for transparency and accountability

## [0.5.0] - 2025-11-12

### Added - Phase 2: Planning & Quality Gates System

#### New Commands

- **`nuaa plan [initiative] [--type TYPE]`** - Create a structured document plan from a program specification
  - Auto-detects document type (proposal, design, evaluation, impact) based on spec content
  - Breaks documents into logical sections with gate assignments
  - Identifies dependencies between sections
  - Provides quality criteria for each gate
  - Supports both CLI and AI agent usage (`/nuaa.plan`)

- **`nuaa gate-check <section> [--initiative INIT]`** - Validate a section against its quality gate criteria
  - Checks dependencies are satisfied before validation
  - Enforces gate progression rules (can't skip gates)
  - Provides pass/fail with specific, actionable feedback
  - Integrates with planning workflow
  - Supports both CLI and AI agent usage (`/nuaa.gate-check`)

- **`nuaa status [initiative]`** - Show initiative progress and section gate status
  - Displays overall completion percentage
  - Shows section-by-section progress with gate status
  - Identifies blocked sections and their dependencies
  - Highlights next available sections to work on
  - Estimates timeline based on average completion rate
  - Supports both CLI and AI agent usage (`/nuaa.status`)

#### Templates

- **`nuaa-kit/templates/document-plan-template.md`** - Structured template for document planning
  - Five quality gates (Initial Structure, Core Content, Evidence & Justification, Integration & Coherence, Review & Polish)
  - Section structure with gate assignments, dependencies, and quality criteria
  - Progress tracking table with status values
  - Gate progression rules and review history
  - Planning metadata for document type, length, audience, and deadlines

- **`nuaa-kit/commands/plan.md`** - AI agent command template for document planning
  - Gate assignment logic based on section purpose
  - Automatic dependency detection between sections
  - Document type detection (proposal vs. design vs. evaluation vs. impact)
  - Section count and length guidelines by document type
  - Gate distribution recommendations (Gate 1: 15-20%, Gate 2: 30-40%, etc.)
  - Validation checks for balanced gates and no circular dependencies

- **`nuaa-kit/commands/gate-check.md`** - AI agent command template for quality gate validation
  - Comprehensive validation criteria for all 5 gates
  - Gate criteria inheritance (higher gates include lower gate criteria)
  - Dependency validation before content review
  - Structured feedback report format with pass/fail results
  - Common failure patterns by gate type
  - Actionable recommendations for addressing issues

- **`nuaa-kit/commands/status.md`** - AI agent command template for progress tracking
  - Section progress table with status symbols (✓ Passed, 🔄 In Progress, ⏸ Blocked, ⭕ Not Started, ❌ Failed)
  - Gate summary showing pass rates by gate level
  - Next actionable sections (ready vs. blocked)
  - Timeline estimation based on completed work
  - Warnings and recommendations (dependency chains, gate imbalances)

#### Scripts

- **`scripts/bash/check-gate-status.sh`** - Gate validation script for Unix/Linux/macOS
  - Parses plan.md to extract section metadata (gate, dependencies, status)
  - Validates all dependencies are satisfied before allowing progression
  - JSON output mode for programmatic integration with CLI
  - Returns exit codes: 0 = dependencies satisfied, 1 = blocked
  - Auto-detects most recent initiative if not specified

- **`scripts/powershell/check-gate-status.ps1`** - Gate validation script for Windows
  - Feature parity with bash version
  - PowerShell best practices and error handling
  - Consistent JSON output format
  - Cross-platform compatibility

#### Documentation

- Phase 2 introduces the "Plan → Draft → Gate-Check → Status" workflow
- Each section is assigned a quality gate (1-5) based on its purpose
- Dependencies ensure logical document construction order
- Quality gates prevent compound errors by catching issues early

### Changed

- Enhanced workflow: Specify → Clarify → **Plan → Draft → Gate-Check → Status** → Review
- CLI now supports full document lifecycle from specification through quality validation

## [0.4.0] - 2025-11-12

### Added - Phase 1: Specify & Clarify Workflow

#### New Commands

- **`nuaa specify <description>`** - Create a new program specification with auto-numbered initiative
  - Automatically creates `initiatives/NNN-slug/spec.md` directory structure
  - Auto-incrementing initiative numbers (001, 002, 003...)
  - Intelligent slug generation from program descriptions
  - Populates specification template with metadata
  - Supports both CLI and AI agent usage (`/nuaa.specify`)

- **`nuaa clarify [initiative]`** - Resolve ambiguities in program specifications interactively
  - Finds all `[NEEDS CLARIFICATION: ...]` markers in specifications
  - Presents structured questions with context
  - Captures user answers and updates specification
  - Removes markers after clarification
  - Auto-detects most recent initiative if not specified
  - Supports both CLI and AI agent usage (`/nuaa.clarify`)

#### Templates

- **`nuaa-kit/commands/specify.md`** - AI agent command template for creating program specifications
  - Comprehensive guidance on specification structure
  - `[NEEDS CLARIFICATION]` marker system (max 5 per spec)
  - Mission constitution integration
  - Quality checks and best practices

- **`nuaa-kit/commands/clarify.md`** - AI agent command template for clarification workflow
  - Interactive question presentation format
  - Suggested answer options with implications
  - Context-aware guidance for each ambiguity
  - Integration with mission constitution

- **`nuaa-kit/templates/program-specification-template.md`** - Structured template for program specs
  - Comprehensive sections: Overview, Target Population, Duration, Evidence, Activities, Outcomes, Alignment
  - `[PLACEHOLDER]` markers for AI to fill
  - Support for `[NEEDS CLARIFICATION]` markers
  - Metadata fields for initiative tracking

#### Scripts

- **`scripts/bash/create-new-initiative.sh`** - Initiative management script for Unix/Linux/macOS
  - Auto-incrementing initiative numbering
  - Smart slug generation with stop word filtering
  - Template copying and population
  - JSON output for programmatic use
  - Environment variable setting (`NUAA_INITIATIVE`)

- **`scripts/powershell/create-new-initiative.ps1`** - Initiative management script for Windows
  - Feature parity with bash version
  - Cross-platform compatibility
  - PowerShell best practices
  - Consistent JSON output format

#### Documentation

- Added comprehensive "Creating Program Specifications" section to `nuaa-kit/README.md`
  - Detailed workflow explanation (Specify → Clarify → Plan)
  - Example usage with code blocks
  - Clarification marker system documentation
  - Best practices and tips
  - Integration with planning phase

#### Testing

- **`tests/test_specify_clarify.py`** - Comprehensive test suite for new commands
  - Test initiative creation with proper numbering
  - Test clarification marker detection and resolution
  - Test edge cases (no markers, auto-increment)
  - Test template copying and script execution
  - All tests passing (7 total tests across all test files)

### Changed

- Updated `.gitignore` to exclude working directories (`initiatives/`, `nuaa/`)
- Enhanced CLI with two new subcommands maintaining consistency with existing patterns

### Security

- CodeQL security scan: **0 alerts** - no vulnerabilities detected
- All scripts use safe parameter handling and proper escaping
- No hardcoded credentials or sensitive data

## [0.3.0] - 2025-11-12

### Added - NUAA Workflows in CLI

- Implemented first-class NUAA workflow subcommands in the CLI:
  - `nuaa design <program> <target> <duration>` → scaffolds `nuaa/NNN-slug/` with `program-design.md`, `logic-model.md`, `impact-framework.md`, and `CHANGELOG.md`
  - `nuaa propose <program> <funder> <amount> <duration>` → creates `proposal.md` from template
  - `nuaa measure <program> <evaluation-period> <budget>` → creates/updates `impact-framework.md`
  - `nuaa document <program>` → creates `existing-program-analysis.md` (brownfield)
  - `nuaa report <program> [--type]` → initializes `report.md` scaffold
  - `nuaa refine <program> [--note]` → appends entry to feature `CHANGELOG.md`
- Added robust helpers for feature numbering, slug generation, template discovery, metadata stamping, and placeholder substitution.
- Comprehensive test coverage for all CLI subcommands (`tests/test_cli_basic.py`).

### Changed

- Bumped package version to 0.3.0 in `pyproject.toml`.
- `version` command continues to report latest template release and local CLI version.

### Fixed

- **Security**: Corrected GitHub Copilot agent folder path from `.github/` to `.github/agents/` in security notice to prevent accidentally ignoring CI workflows.
- **Resource Management**: All httpx HTTP clients now properly managed with context managers to prevent unclosed session warnings.
- **UX**: `check` command now distinguishes IDE-based assistants from CLI tools, avoiding false "install an AI assistant" messaging when Copilot/Windsurf/etc are available.
- Updated all optional parameter type hints to use modern `| None` syntax for Python 3.11+ compatibility.

### Notes

- Initial implementation prioritizes practical scaffolding using markdown templates in `nuaa-kit/templates/`.
- Future releases may integrate direct AI invocation and richer validations.

## [0.2.0] - 2025-11-11

### Changed - NUAA Template Source Migration

- Template downloader now pulls NUAA release assets from this repository (`nuaa-template-<agent>-<script>-<version>.zip`).
- Asset naming migrated from `spec-kit-template-*` to `nuaa-template-*` consistently across CLI and release scripts.
- Version command already pointed at NUAA repo; initialization now aligned with NUAA asset pattern.
- Added internal comments clarifying asset expectations for maintainers.

### Added

- Governance note for forthcoming deprecation of legacy `specify` alias (to be scheduled in a later minor release).
- CHANGELOG entry documenting final phase of rebrand (template source).

### Deprecated (Planned)

- Legacy `specify` command will be deprecated after a grace period (target: >= 0.4.0). Backwards compatibility retained for now.

### Security / Integrity

- Clear error panel when NUAA assets are missing, listing available release asset names to prevent silent initialization failures.

---

## [0.1.0] - 2025-11-11

### Changed - Complete NUAA Project Transformation

This release represents a **complete transformation** from Spec-Kit to NUAA Project. This is now exclusively the NUAA project toolkit, designed specifically for NSW Users and AIDS Association.

#### Breaking Changes

- **BREAKING**: Rebranded project from "Spec Kit" to "NUAA Project"
- **BREAKING**: Renamed package from `specify-cli` to `nuaa-cli`
- **BREAKING**: Renamed Python module from `src/specify_cli` to `src/nuaa_cli`
- **BREAKING**: Changed command prefixes from `/speckit.*` to `/nuaa.*` in CLI output
- **BREAKING**: Updated directory structure from `.specify/` to `.nuaa/`
- **BREAKING**: Renamed agent rules files from `*-specify-rules.md` to `*-nuaa-rules.md`
- **BREAKING**: Environment variable changed from `SPECIFY_FEATURE` to `NUAA_FEATURE` (legacy `SPECIFY_FEATURE` still supported)
- **BREAKING**: Release packages now named `nuaa-template-*` instead of `spec-kit-template-*`

#### Added

- New primary `nuaa` CLI command (legacy `specify` command maintained for backwards compatibility)
- NUAA-specific commands: `/nuaa.design`, `/nuaa.propose`, `/nuaa.measure`, `/nuaa.document`, `/nuaa.refine`, `/nuaa.report`
- Complete NUAA Kit documentation in `/nuaa-kit/` directory
- NUAA-focused examples and templates

#### Updated

- All documentation (README, AGENTS.md, CONTRIBUTING.md, docs/) to reflect NUAA as primary identity
- CLI help text, banners, and output to show NUAA branding
- All scripts (bash and PowerShell) to use NUAA conventions
- GitHub workflows and release scripts for NUAA packaging
- VS Code settings for NUAA command recommendations
- Repository description and links throughout

#### Maintained

- Backwards compatibility with `specify` command alias
- Spec-Driven Development methodology as the underlying framework
- All existing agent support (Claude, Gemini, Copilot, Cursor, etc.)

**Note**: Spec-Driven Development methodology remains as the foundational framework. NUAA Project is a specialized application of SDD principles for community health program management.

## [0.0.22] - 2025-11-07

- Support for VS Code/Copilot agents, and moving away from prompts to proper agents with hand-offs.
- Move to use `AGENTS.md` for Copilot workloads, since it's already supported out-of-the-box.
- Adds support for the version command. ([#486](https://github.com/github/spec-kit/issues/486))
- Fixes potential bug with the `create-new-feature.ps1` script that ignores existing feature branches when determining next feature number ([#975](https://github.com/github/spec-kit/issues/975))
- Add graceful fallback and logging for GitHub API rate-limiting during template fetch ([#970](https://github.com/github/spec-kit/issues/970))

## [0.0.21] - 2025-10-21

- Fixes [#975](https://github.com/github/spec-kit/issues/975) (thank you [@fgalarraga](https://github.com/fgalarraga)).
- Adds support for Amp CLI.
- Adds support for VS Code hand-offs and moves prompts to be full-fledged chat modes.
- Adds support for `version` command (addresses [#811](https://github.com/github/spec-kit/issues/811) and [#486](https://github.com/github/spec-kit/issues/486), thank you [@mcasalaina](https://github.com/mcasalaina) and [@dentity007](https://github.com/dentity007)).
- Adds support for rendering the rate limit errors from the CLI when encountered ([#970](https://github.com/github/spec-kit/issues/970), thank you [@psmman](https://github.com/psmman)).

## [0.0.20] - 2025-10-14

### Added

- **Intelligent Branch Naming**: `create-new-feature` scripts now support `--short-name` parameter for custom branch names
  - When `--short-name` provided: Uses the custom name directly (cleaned and formatted)
  - When omitted: Automatically generates meaningful names using stop word filtering and length-based filtering
  - Filters out common stop words (I, want, to, the, for, etc.)
  - Removes words shorter than 3 characters (unless they're uppercase acronyms)
  - Takes 3-4 most meaningful words from the description
  - **Enforces GitHub's 244-byte branch name limit** with automatic truncation and warnings
  - Examples:
    - "I want to create user authentication" → `001-create-user-authentication`
    - "Implement OAuth2 integration for API" → `001-implement-oauth2-integration-api`
    - "Fix payment processing bug" → `001-fix-payment-processing`
    - Very long descriptions are automatically truncated at word boundaries to stay within limits
  - Designed for AI agents to provide semantic short names while maintaining standalone usability

### Changed

- Enhanced help documentation for `create-new-feature.sh` and `create-new-feature.ps1` scripts with examples
- Branch names now validated against GitHub's 244-byte limit with automatic truncation if needed

## [0.0.19] - 2025-10-10

### Added

- Support for CodeBuddy (thank you to [@lispking](https://github.com/lispking) for the contribution).
- You can now see Git-sourced errors in the Specify CLI.

### Changed

- Fixed the path to the constitution in `plan.md` (thank you to [@lyzno1](https://github.com/lyzno1) for spotting).
- Fixed backslash escapes in generated TOML files for Gemini (thank you to [@hsin19](https://github.com/hsin19) for the contribution).
- Implementation command now ensures that the correct ignore files are added (thank you to [@sigent-amazon](https://github.com/sigent-amazon) for the contribution).

## [0.0.18] - 2025-10-06

### Added

- Support for using `.` as a shorthand for current directory in `specify init .` command, equivalent to `--here` flag but more intuitive for users.
- Use the `/speckit.` command prefix to easily discover Spec Kit-related commands.
- Refactor the prompts and templates to simplify their capabilities and how they are tracked. No more polluting things with tests when they are not needed.
- Ensure that tasks are created per user story (simplifies testing and validation).
- Add support for Visual Studio Code prompt shortcuts and automatic script execution.

### Changed

- All command files now prefixed with `speckit.` (e.g., `speckit.specify.md`, `speckit.plan.md`) for better discoverability and differentiation in IDE/CLI command palettes and file explorers

## [0.0.17] - 2025-09-22

### Added

- New `/clarify` command template to surface up to 5 targeted clarification questions for an existing spec and persist answers into a Clarifications section in the spec.
- New `/analyze` command template providing a non-destructive cross-artifact discrepancy and alignment report (spec, clarifications, plan, tasks, constitution) inserted after `/tasks` and before `/implement`.
  - Note: Constitution rules are explicitly treated as non-negotiable; any conflict is a CRITICAL finding requiring artifact remediation, not weakening of principles.

## [0.0.16] - 2025-09-22

### Added

- `--force` flag for `init` command to bypass confirmation when using `--here` in a non-empty directory and proceed with merging/overwriting files.

## [0.0.15] - 2025-09-21

### Added

- Support for Roo Code.

## [0.0.14] - 2025-09-21

### Changed

- Error messages are now shown consistently.

## [0.0.13] - 2025-09-21

### Added

- Support for Kilo Code. Thank you [@shahrukhkhan489](https://github.com/shahrukhkhan489) with [#394](https://github.com/github/spec-kit/pull/394).
- Support for Auggie CLI. Thank you [@hungthai1401](https://github.com/hungthai1401) with [#137](https://github.com/github/spec-kit/pull/137).
- Agent folder security notice displayed after project provisioning completion, warning users that some agents may store credentials or auth tokens in their agent folders and recommending adding relevant folders to `.gitignore` to prevent accidental credential leakage.

### Changed

- Warning displayed to ensure that folks are aware that they might need to add their agent folder to `.gitignore`.
- Cleaned up the `check` command output.

## [0.0.12] - 2025-09-21

### Changed

- Added additional context for OpenAI Codex users - they need to set an additional environment variable, as described in [#417](https://github.com/github/spec-kit/issues/417).

## [0.0.11] - 2025-09-20

### Added

- Codex CLI support (thank you [@honjo-hiroaki-gtt](https://github.com/honjo-hiroaki-gtt) for the contribution in [#14](https://github.com/github/spec-kit/pull/14))
- Codex-aware context update tooling (Bash and PowerShell) so feature plans refresh `AGENTS.md` alongside existing assistants without manual edits.

## [0.0.10] - 2025-09-20

### Fixed

- Addressed [#378](https://github.com/github/spec-kit/issues/378) where a GitHub token may be attached to the request when it was empty.

## [0.0.9] - 2025-09-19

### Changed

- Improved agent selector UI with cyan highlighting for agent keys and gray parentheses for full names

## [0.0.8] - 2025-09-19

### Added

- Windsurf IDE support as additional AI assistant option (thank you [@raedkit](https://github.com/raedkit) for the work in [#151](https://github.com/github/spec-kit/pull/151))
- GitHub token support for API requests to handle corporate environments and rate limiting (contributed by [@zryfish](https://github.com/@zryfish) in [#243](https://github.com/github/spec-kit/pull/243))

### Changed

- Updated README with Windsurf examples and GitHub token usage
- Enhanced release workflow to include Windsurf templates

## [0.0.7] - 2025-09-18

### Changed

- Updated command instructions in the CLI.
- Cleaned up the code to not render agent-specific information when it's generic.

## [0.0.6] - 2025-09-17

### Added

- opencode support as additional AI assistant option

## [0.0.5] - 2025-09-17

### Added

- Qwen Code support as additional AI assistant option

## [0.0.4] - 2025-09-14

### Added

- SOCKS proxy support for corporate environments via `httpx[socks]` dependency

### Fixed

N/A

### Changed

N/A
