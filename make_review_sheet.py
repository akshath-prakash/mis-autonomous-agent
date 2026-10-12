"""Builds claims.csv: one row per sentence/bullet in each writer draft, for you to label by hand.
Won't overwrite an existing claims.csv (so your labels are safe)."""
import csv
import re
from pathlib import Path

RESULTS = Path("results")
OUT = Path("claims.csv")


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def claims_from(text):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("---"):
            continue
        line = re.sub(r"^[-*\d.\s]+", "", line).replace("**", "")
        for s in re.split(r"(?<=[.!?])\s+", line):
            if len(s) >= 30:
                out.append(s.strip())
    return out


def main():
    if OUT.exists():
        print("claims.csv already exists - not overwriting your labels.")
        return
    rows = []
    for folder in sorted(p for p in RESULTS.iterdir() if p.is_dir()):
        draft = (folder / "draft.md").read_text()
        final_n = norm((folder / "final.md").read_text())
        for c in claims_from(draft):
            rows.append({"topic": folder.name, "claim": c,
                         "appears_unchanged_in_final": "yes" if norm(c) in final_n else "no",
                         "supported_by_research": "", "auditor_action": "", "notes": ""})
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} claims to {OUT}. Fill in the last 3 columns.")


if __name__ == "__main__":
    main()
