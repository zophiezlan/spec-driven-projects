# NUAA Kit Changelog

All notable changes to the NUAA adaptation of Spec Kit are documented here. This changelog tracks kit‑specific content (commands, templates, guidance) separate from the core Specify CLI (`pyproject.toml` + `CHANGELOG.md`).

Format: YYYY-MM-DD Semantic grouping (Added / Changed / Removed / Deprecated / Fixed / Security)

## [Unreleased]

### Added

- Initial glossary (`glossary.md`) covering evaluation and harm reduction terminology.
- Accessibility & Inclusive Content Guidelines (`accessibility-guidelines.md`).
- Command flags schema (`commands/schema.json`).
- Placeholder lint scripts (PowerShell + Bash).
- Evaluation data dictionary and indicator CSV example.
- Stubs: `report.md`, `refine.md`, `budget-calculator.md` (PLANNED).

### Changed

- Normalized ordered list spacing in `commands/design.md`.
- Updated `nuaa-kit/README.md` directory tree and added pre‑submission checks section.

### Fixed

- Markdown heading/list spacing issues in newly added documents.

### Deprecated

- None.

### Removed

- None.

### Security

- None.

## 2025-11-11 Initial Draft Baseline

### Added

- Core NUAA command documents: `design.md`, `measure.md`, `propose.md`.
- Supporting templates: `program-design.md`, `logic-model.md`, `impact-framework.md`, `proposal.md`.
- `STATUS.md` tracking implemented vs planned artifacts.
- Microsoft365 scaffolding directories.

### Changed

- Adjusted schema draft to 07 for compatibility.

### Fixed

- Initial markdown lint errors (code fence languages, blank lines around headings, tables).

### Deprecated / Removed / Security

- None.

---

Release process:

1. Update documents and run placeholder + markdown lint checks.
2. Increment [Unreleased] entries into dated section upon tagging.
3. Peer review significant content changes (glossary, evaluation frameworks) prior to release.
4. Keep entries concise; cross‑reference detailed diffs in version control as needed.
