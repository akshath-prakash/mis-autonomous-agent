# Executive Brief: Ransomware Risk to U.S. Hospitals

**Basis:** This brief is synthesized from background research with no live data access. Coverage runs through roughly mid-2025, and 2025 coverage is thinner and less reliable. Nothing after mid/late 2025 is covered. Items marked *(verify)* need confirmation against primary sources before external use. Items marked *(assessment)* are analytical judgment, not established fact.

---

## Headline Takeaway

**Ransomware is a persistent, patient-safety-level threat to hospitals. Disrupting individual criminal groups has not demonstrably reduced the overall risk.** The most damaging incidents have come from single points of failure, such as vendors and shared platforms. Basic control gaps, such as missing multi-factor authentication (MFA), have also played a role.

---

## Key Findings

- **Healthcare remains a top-targeted sector.** The FBI, CISA, and HHS have repeatedly named healthcare and public health among the most-targeted critical infrastructure sectors for ransomware.
- **Hacking dominates large breaches.** Hacking/IT incidents are the clear majority of large breaches (500+ records) reported to HHS. Roughly 700+ such breaches were reported per year in 2023 and 2024 *(verify)*. Change Healthcare inflated the 2024 record totals.
- **Vendor compromise multiplies damage.** The February 2024 Change Healthcare attack (attributed to ALPHV/BlackCat) disrupted claims and payments for weeks to months. Entry was reportedly through a remote-access portal without MFA. Affected individuals were reported at about 190M *(verify)*.
- **Hospital operations are directly hit.**
  - Ascension (May 2024, about 140 hospitals) experienced EHR downtime, ambulance diversions, and a return to paper processes.
  - Kettering Health (Ohio, about May 2025) had procedures canceled and systems down. The attack was attributed to Interlock *(verify)*.
- **Extortion has evolved.** Many groups now steal data first and threaten to leak it, so restoring from backups does not end an incident.
- **Group churn does not equal progress.**
  - LockBit was disrupted by law enforcement in February 2024.
  - ALPHV/BlackCat apparently exit-scammed in March 2024.
  - RansomHub reportedly went dark around April 2025, and Black Basta appeared to decline after a 2025 chat leak.
  - Qilin, Interlock, Rhysida, Akira, and others were active against healthcare in 2024–2025. Attribution of specific incidents should be verified.
- **Costs are high.** IBM/Ponemon has ranked healthcare highest among industries for average breach cost for years. The figure was about $9.8M in 2024 and about $7.4M in 2025 *(verify)*. Research also indicates attacks spill over into neighboring hospitals' emergency departments.
- **Common entry points are well understood.** These are stolen or weak credentials, unpatched internet-facing devices, help-desk social engineering, and flat networks with legacy medical devices.

---

## Risks

1. **Patient safety and continuity:** Downtime and delayed care are common effects of attacks. Studies suggest higher in-hospital mortality during attacks, but the magnitude is uncertain and causation is debated.
2. **Concentration risk:** Another Change Healthcare-style vendor failure is plausible *(assessment)*.
3. **Regulatory uncertainty:**
   - The proposed HIPAA Security Rule overhaul (published around Dec 2024/Jan 2025) would require MFA, encryption, segmentation, and restoration of critical systems within 72 hours. Its final status is unknown.
   - The proposed CIRCIA rule would require incident reports within 72 hours and ransom-payment reports within 24 hours. The final rule has reportedly been delayed *(verify)*.
4. **Resource gaps:** Rural and smaller hospitals have thin margins and little security staff. No dedicated federal hospital cyber-funding program is known to exist. There are 2025 reports of reduced federal cyber capacity, with uncertain operational impact *(verify)*.
5. **Insurance pressure:** Cyber insurance costs and underwriting requirements may continue to tighten *(assessment, low–medium confidence)*.

---

## Recommended Actions

*These actions are advisory. The timelines and targets come from the proposed rules or from judgment, not from the research findings.*

1. **Close the basics within 90 days.** Enforce MFA on all remote and privileged access, and prioritize patching internet-facing systems (VPNs, firewalls, file-transfer tools).
2. **Harden the help desk.** Require strong identity verification for password and MFA resets.
3. **Prove recovery, not just backup.** Keep offline, immutable backups. Test restoration of critical systems against the 72-hour benchmark in the proposed HIPAA rule.
4. **Rehearse downtime.** Run clinical downtime and diversion exercises with executive and board participation.
5. **Map and tier vendor dependencies.** Identify single points of failure, require MFA and incident notification in contracts, and build workarounds for critical vendors such as claims clearing and EHR hosting.
6. **Segment the network** and inventory medical devices, starting with unpatchable legacy equipment.
7. **Prepare for compliance.** Gap-assess against HHS voluntary Cybersecurity Performance Goals (January 2024) and the proposed HIPAA rule. Pre-plan reporting workflows for the proposed CIRCIA 24/72-hour windows.
8. **Join Health-ISAC** and confirm the incident-response retainer and cyber insurance terms.

---

**Before external use, verify:**
- HHS Breach Portal counts
- FBI IC3 data
- Final affected-individual figures (Change Healthcare, Ascension)
- IBM cost figures
- 2025 incident attributions
- Status of HIPAA and CIRCIA rulemaking
- Status of federal funding and CISA/HHS capacity

---

### Compliance Review Log

- **Softened "largest losses come from…"** to "most damaging incidents," because the research does not quantify losses.
- **Changed "consistently rank" to "repeatedly named,"** to match the research wording.
- **Corrected the Change Healthcare duration** from "weeks nationwide" to "weeks to months." The research does not support "nationwide."
- **Separated the Ascension and Kettering impacts.** The original attributed diversions and paper processes to both, but the research supports those details only for Ascension.
- **Changed "remain active" to "were active in 2024–2025,"** because nothing after mid-2025 is known. Added attribution and decline caveats for RansomHub, Black Basta, and ALPHV.
- **Softened "has not reduced it"** to "has not demonstrably reduced it." The research rates this Medium confidence.
- **Qualified the patient-safety claim,** because the mortality causation is debated.
- **Added a verify flag to CIRCIA delay claims** (Low–Medium confidence).
- **Labeled the Concentration risk and Insurance pressure items as assessments.**
- **Labeled the 72-hour restoration target as a proposed-rule benchmark** and the 90-day timeline as advisory.
- **Added the coverage-limits statement** (thin 2025 data, nothing after mid/late 2025).