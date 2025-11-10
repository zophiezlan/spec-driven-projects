---
status: draft
version: 0.1.0
mode: planned
---

# /nuaa.refine (PLANNED)

Iteratively improve existing NUAA documents (program design, proposal, impact framework) using targeted feedback and version history.

## Purpose

- Apply focused revisions (language, indicators, scope)
- Preserve version history & rationale
- Support peer / consumer advisory feedback cycles

## Inputs (planned)

- Source document path
- Revision focus (--focus=logic-model|budget|evaluation|narrative)
- Feedback summary text or file
- Output mode (--mode=inline|diff|summary)

## Outputs (planned)

- Updated document (inline or new version file)
- Diff summary section
- Changelog entry suggestion

## Roadmap

- Add structured feedback ingestion
- Implement diff rendering for AI output
- Integrate placeholder lint pre-commit
