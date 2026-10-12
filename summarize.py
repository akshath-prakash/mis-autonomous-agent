"""Reads your labeled claims.csv and prints/saves the results table.
supported_by_research: Y or N   (is the claim backed by results/<topic>/research.md?)
auditor_action:        kept / removed / flagged   (what the final brief did with it)
"""
import csv
from collections import defaultdict


def main():
    rows = list(csv.DictReader(open("claims.csv")))
    labeled = [r for r in rows if r["supported_by_research"].strip() and r["auditor_action"].strip()]
    if len(labeled) < len(rows):
        print(f"WARNING: only {len(labeled)} of {len(rows)} rows are labeled; counting those.\n")
    stats = defaultdict(lambda: dict(claims=0, unsup=0, caught=0, missed=0, false_flags=0))
    for r in labeled:
        sup = r["supported_by_research"].strip().upper() == "Y"
        acted = r["auditor_action"].strip().lower() in ("removed", "flagged")
        for key in (r["topic"], "TOTAL"):
            s = stats[key]
            s["claims"] += 1
            if not sup:
                s["unsup"] += 1
                s["caught" if acted else "missed"] += 1
            elif acted:
                s["false_flags"] += 1
    lines = ["| Topic | Claims | Unsupported in draft | Caught by auditor | Missed | False flags |",
             "|---|---|---|---|---|---|"]
    for k in [k for k in stats if k != "TOTAL"] + ["TOTAL"]:
        s = stats[k]
        lines.append(f"| {k} | {s['claims']} | {s['unsup']} | {s['caught']} | {s['missed']} | {s['false_flags']} |")
    t = stats["TOTAL"]
    if t["unsup"]:
        lines.append(f"\nWithout auditor: {t['unsup']} unsupported claims reach the reader.")
        lines.append(f"With auditor: {t['missed']} unsupported claims reach the reader.")
        lines.append(f"Catch rate (recall): {t['caught']}/{t['unsup']} = {100*t['caught']/t['unsup']:.0f}%")
    if t["caught"] + t["false_flags"]:
        lines.append(f"Flag precision: {t['caught']}/{t['caught']+t['false_flags']} = "
                     f"{100*t['caught']/(t['caught']+t['false_flags']):.0f}%")
    out = "\n".join(lines)
    print(out)
    open("results_summary.md", "w").write(out + "\n")


if __name__ == "__main__":
    main()
