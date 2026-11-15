# Ontario SB-10 Energy Efficiency Path Selector (2024 OBC)

Which SB-10 compliance path applies to your building — and which climate zone and prescriptive table come with it? The selector walks the actual decision structure of Ontario's Supplementary Standard SB-10: Division 5 eligibility for small non-residential Part 9 buildings, the three Division 3 reference standards, the CO2e and peak-demand overlays, and the three different climate-zone frameworks SB-10 uses (which are routinely confused).

**Live web tool:** https://dust2engineering.github.io/ontario-sb10-path-selector/web/

## How it works

- Answer the routing questions: existing building, Part 9 or Part 3, residential or not, electric heat, winter occupancy, glazing and skylight ratios, and your location's HDD18 from SB-1.
- Part 9 residential exits immediately — houses follow OBC 12.2.2 / SB-12, not SB-10. Existing buildings route to Part 10/11.
- Eligible Part 9 non-residential buildings get Division 5 (with its own 2-zone table, reproduced in full) — unless glazing > 40% or skylights > 3% push the envelope back to Division 3.
- Everything else lands in Division 3: pick ASHRAE 90.1-2013 + Ch. 2, NECB 2015 + Ch. 3, or ASHRAE 189.1-2014 §7, then prescriptive or performance inside it — with the CO2e cap and peak-demand cap on every path.

## Data in this repository

- `sb10-data.json` — the path structure, all three climate-zone frameworks, the full Division 5 Table 1.1.1.2, the Division 3 Zone 5 opaque-element table (SB 5.5-5–2017), the CO2e factors and the Division 5 HVAC anchors, as machine-readable JSON.
- Verified from the official SB-10 text on ontario.ca (2024 Building Code Compendium). Zone 6/7 envelope values and NECB-path cell values exist in SB-10 but were not extracted in this pass — the tool names your zone without inventing their numbers.

## Command line

```bash
python3 sb10_selector.py --part9 yes --residential no --electric-heat no --hdd 4500
```

## Worked examples

- [example-small-commercial.txt](examples/example-small-commercial.txt)
- [example-part3-office.txt](examples/example-part3-office.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Building general. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
