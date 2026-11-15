#!/usr/bin/env python3
"""Ontario SB-10 energy-efficiency path selector (2024 OBC).
Usage:
  python3 sb10_selector.py --part9 yes --residential no --electric-heat no --winter-occupied yes --hdd 4500
  python3 sb10_selector.py --part9 no --hdd 3800
"""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(__file__), "sb10-data.json")))
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--existing", action="store_true")
    ap.add_argument("--part9", choices=["yes", "no"], default="no")
    ap.add_argument("--residential", choices=["yes", "no"], default="no")
    ap.add_argument("--electric-heat", choices=["yes", "no"], default="no")
    ap.add_argument("--winter-occupied", choices=["yes", "no"], default="yes")
    ap.add_argument("--glazing-pct", type=float, default=0, help="fenestration as % of wall area")
    ap.add_argument("--skylight-pct", type=float, default=0, help="skylights as % of ceiling area")
    ap.add_argument("--hdd", type=float, default=4500, help="heating degree-days below 18 C (SB-1 Table 2)")
    a = ap.parse_args()
    if a.existing:
        print("Existing building: route through OBC Part 10 (change of use) or Part 11 (renovation) - outside the SB-10 new-building paths.")
        return
    if a.part9 == "yes" and a.residential == "yes":
        print("Part 9 residential: SB-10 does not apply. Energy efficiency is OBC Subsection 12.2.2 / SB-12.")
        return
    z3 = 5 if a.hdd < 4000 else (6 if a.hdd < 5000 else 7)
    print(f"Division 3 climate zone (Table 1.3.1.1): Zone {z3} at HDD18 {a.hdd:g}")
    if a.part9 == "yes" and a.electric_heat == "no" and a.winter_occupied == "yes":
        z5 = 1 if a.hdd < 5000 else 2
        print(f"Division 5 (simplified prescriptive) is AVAILABLE: Part 9, non-residential, no electric space heating, winter-occupied. Division 5 zone: Zone {z5} (Table 1.1.1.2).")
        if a.glazing_pct > 40 or a.skylight_pct > 3:
            print("  BUT: fenestration > 40% of wall or skylights > 3% of ceiling - the ENVELOPE must comply with Division 3.")
        print("Division 3 also remains available as an alternative.")
    print("Division 3: choose ONE - (a) ASHRAE 90.1-2013 + SB-10 Ch. 2 (prescriptive Sections 5-10 or Section 11 Energy Cost Budget); (b) NECB 2015 + SB-10 Ch. 3 (prescriptive/trade-off or Part 8 performance); (c) ASHRAE 189.1-2014 Section 7 only.")
    print("Overlays on every Division 3 path: CO2e cap (Art. 1.1.2.2) and peak electric demand cap (Art. 1.1.2.3).")
    if a.electric_heat == "yes":
        print("Electric space heating: on the 90.1 path the envelope must meet the Zone 7 table (SB 5.5-7) regardless of location.")
if __name__ == "__main__":
    main()
