---
status: draft
version: 0.1.0
purpose: "Stub budget calculator template (planned)"
---

# Budget Calculator Template (PLANNED)

This is a stub placeholder. Full calculator will include:

## Planned Sections

1. Overview & Usage Instructions
2. Input Parameters
   - Participant counts
   - Session counts
   - Peer remuneration standard ($300/session)
   - Staff FTE allocations
3. Cost Categories Table
4. Automatic Totals & Percentages
5. Sensitivity Scenarios (Reduced / Expanded Funding)
6. Export Guidance (Excel / CSV)
7. Version & Change Log Block

## Roadmap

- Integrate with future `specify nuaa budget` subcommand.
- Provide PowerShell and bash scripts to auto-fill line items.

## Placeholder Table (Structure Only)

| Category            | Line Item           | Unit           | Qty     | Rate | Subtotal |
| ------------------- | ------------------- | -------------- | ------- | ---- | -------- |
| Personnel           | Program Coordinator | FTE-Month      | 0.6 x 6 | $X   | $Y       |
| Personnel           | Peer Workers        | Session        | N       | $300 | $N\*300  |
| Operations          | Venue               | Session        | N       | $X   | $Y       |
| Participant Support | Transport           | Person-Session | N       | $X   | $Y       |
| Evaluation          | Survey Tools        | License-Month  | M       | $X   | $Y       |
| Administration      | Overhead            | Percent        | %       | Base | Calc     |

> Replace placeholders once implemented.
