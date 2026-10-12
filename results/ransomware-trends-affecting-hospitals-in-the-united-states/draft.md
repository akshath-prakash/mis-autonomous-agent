# Executive Brief: Ransomware Risk to U.S. Hospitals

**Basis:** Synthesized from background research with no live data access. Coverage runs through roughly mid-2025. Figures marked *(verify)* need confirmation against primary sources before external use.

---

## Headline Takeaway

**Ransomware is a persistent, patient-safety-level threat to hospitals, and disrupting individual criminal groups has not reduced it.** The largest losses come from single points of failure, such as vendors and shared platforms, and from basic control gaps like missing multi-factor authentication (MFA).

---

## Key Findings

- **Healthcare remains a top-targeted sector.** The FBI, CISA, and HHS consistently rank it among the most-targeted critical infrastructure sectors.
- **Hacking dominates large breaches.** It accounts for most of the roughly 700+ large breaches reported to HHS annually *(verify)*.
- **Vendor compromise multiplies damage.** The February 2024 Change Healthcare attack disrupted claims nationwide for weeks. Entry was reportedly through a remote-access portal without MFA. Affected individuals were reported at about 190M *(verify)*.
- **Hospital operations are directly hit.** Ascension (May 2024, ~140 hospitals) and Kettering Health (2025) saw EHR downtime, ambulance diversions, canceled procedures, and a return to paper.
- **Extortion has evolved.** Many groups now steal data and threaten to leak it, so restoring from backups does not end an incident.
- **Group churn does not equal progress.** LockBit was disrupted, ALPHV/BlackCat exited, and RansomHub and Black Basta declined, yet Qilin, Interlock, Rhysida, Akira, and others remain active against healthcare.
- **Costs are high.** Healthcare has had the highest average breach cost of any industry for years, about $7.4M in 2025 and $9.8M in 2024 *(verify)*. Research also links attacks to strain on neighboring hospitals' emergency departments.
- **Common entry points are well understood:** stolen credentials, unpatched internet-facing devices, help-desk social engineering, and flat networks with legacy medical devices.

---

## Risks

1. **Patient safety and continuity:** Downtime of days to weeks and delayed care carry clinical consequences.
2. **Concentration risk:** Another Change Healthcare-style vendor failure is plausible.
3. **Regulatory uncertainty:** The proposed HIPAA Security Rule overhaul (MFA, encryption, segmentation, 72-hour system restoration) has no confirmed final status. CIRCIA reporting rules (72-hour incident, 24-hour ransom-payment) are also delayed or unconfirmed.
4. **Resource gaps:** Rural and smaller hospitals have thin margins and little security staff. No dedicated federal funding program is known, and there are reports of reduced federal cyber capacity *(verify)*.
5. **Rising insurance scrutiny:** Underwriting requirements and costs may continue to tighten.

---

## Recommended Actions

1. **Close the basics within 90 days.** Enforce MFA on all remote and privileged access, and prioritize patching internet-facing systems (VPNs, firewalls, file-transfer tools).
2. **Harden the help desk.** Require strong identity verification for password and MFA resets.
3. **Prove recovery, not just backup.** Keep offline, immutable backups and test restoration of critical systems against a 72-hour target.
4. **Rehearse downtime.** Run clinical downtime and diversion exercises with executive and board participation.
5. **Map and tier vendor dependencies.** Identify single points of failure, require MFA and incident notification in contracts, and build workarounds for critical vendors such as claims clearing and EHR hosting.
6. **Segment the network** and inventory medical devices, starting with unpatchable legacy equipment.
7. **Prepare for compliance.** Gap-assess against HHS Cybersecurity Performance Goals and the proposed HIPAA rule, and pre-plan 24/72-hour reporting workflows.
8. **Join Health-ISAC** and confirm the incident-response retainer and cyber insurance terms.

---

**Before external use, verify:** the HHS Breach Portal counts, FBI IC3 data, final affected-individual figures, and the status of HIPAA and CIRCIA rulemaking.