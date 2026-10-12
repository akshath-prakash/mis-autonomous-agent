# Research Summary: Ransomware Trends Affecting U.S. Hospitals

**Method note:** I had no live data access for this task. Everything below comes from my background knowledge, which has a cutoff and may be missing the latest events. Each item is tagged **[High]**, **[Medium]**, or **[Low]** confidence. Figures marked **[VERIFY]** should be checked against the primary source before use. I have avoided inventing numbers where I was unsure.

---

## 1. Big-picture trends

- **Healthcare is a persistent top target. [High]** The FBI, CISA, and HHS have repeatedly named healthcare and public health among the most-targeted critical infrastructure sectors for ransomware. The FBI IC3 annual reports have ranked it at or near the top in ransomware complaints.
  - *Uncertain:* exact IC3 complaint counts for 2023 and 2024. I recall figures in the low-to-mid hundreds per year but won't state a number. **[VERIFY]**
- **Hacking/IT incidents dominate large breach reports. [High]** In the HHS OCR "Wall of Shame" (breaches of 500+ records), hacking/IT incidents are the clear majority of reported breaches, and a large share of affected records.
  - Roughly 700+ large breaches were reported per year in 2023 and 2024. **[Medium] [VERIFY]**
  - Record totals in 2024 were inflated by the Change Healthcare breach. **[High]**
- **Data theft and extortion, with or without encryption, is increasingly common. [Medium]** Many groups steal data first and threaten leaks, so restoring from backups no longer ends the incident.
- **Attacks on third parties and vendors cause outsized damage. [High]** Examples are Change Healthcare (claims clearing), and billing, EHR-hosting, and lab vendors. One vendor compromise can disrupt many hospitals at once.
- **Ransomware-group churn does not reduce overall risk. [Medium]**
  - LockBit was disrupted by law enforcement in Feb 2024 (Operation Cronos). **[High]**
  - ALPHV/BlackCat apparently exit-scammed in March 2024 after the Change Healthcare payout. **[High]**
  - RansomHub rose in 2024. It reportedly went dark around April 2025. **[Medium]**
  - Black Basta suffered an internal chat leak in early 2025 and appeared to decline. **[Medium]**
  - Groups active against healthcare in 2024–2025 include Qilin, Interlock, Rhysida, INC Ransom, Medusa, Play, and Akira. **[Medium]** Attribution for specific incidents should be verified.
- **Ransom payments overall:** Chainalysis reported a record year in 2023 (about $1B+) and a notable drop in 2024 (a decline of roughly a third). **[Medium] [VERIFY exact amounts]** I don't have reliable healthcare-specific payment statistics.
- **Share of healthcare orgs hit:** Sophos surveys suggest roughly two-thirds of surveyed healthcare organizations reported a ransomware attack in a recent year. **[Low–Medium] [VERIFY]** This is a vendor survey, not a census, and it is not U.S.-only.

## 2. Key incidents and timeline

- **Sept 2020:** Universal Health Services (Ryuk) hit across U.S. facilities, with EHR downtime. **[High]**
- **2021:** Scripps Health (San Diego, spring) had weeks of disruption. **[High]**
- **Oct 2022:** CommonSpirit Health had a multi-state outage. About 600K+ individuals were later reported affected. **[Medium] [VERIFY]**
- **2023:**
  - Prospect Medical Holdings (August) suffered a major attack affecting multiple states. **[Medium]**
  - Ardent Health Services (Nov) forced diversions and EHR downtime. **[Medium]**
- **Feb 21, 2024:** Change Healthcare (UnitedHealth Group), attributed to ALPHV/BlackCat.
  - Entry was reportedly via a remote-access portal without MFA. **[High]**
  - Claims and payment disruption lasted weeks to months. **[High]**
  - UnitedHealth reportedly paid a ransom of about $22M. **[Medium–High]**
  - The affected-individuals count was later revised upward. Reports cited about 190 million. **[Medium] [VERIFY]**
- **May 2024:** Ascension (about 140 hospitals) was hit, attributed to Black Basta. **[High]**
  - EHR downtime, diversions, and a return to paper processes followed. **[High]**
  - Later notifications cited roughly 5.6M individuals. **[Medium] [VERIFY]**
- **2025 (my coverage is thinner and less reliable):**
  - Kettering Health (Ohio, ~May) had procedures canceled and systems down, attributed to Interlock. **[Medium]**
  - Covenant Health, Frederick Health, and others were also reported hit. **[Low–Medium]**
  - DaVita (dialysis, not a hospital) was hit in April 2025. **[Medium]**
- **Late 2025 to now:** I lack reliable information. **[Unknown]**

## 3. Attack vectors and risk drivers

- Stolen or weak credentials, especially remote access without MFA. **[High]**
- Unpatched internet-facing devices (VPNs, firewalls, Citrix, Ivanti, Fortinet, file-transfer tools). **[High]**
- Social engineering, including help-desk impersonation, a technique associated with Scattered Spider-style actors. **[Medium]**
- Legacy and unpatchable medical devices and flat networks. **[High]**
- Third-party and supply-chain concentration. **[High]**
- Possible attacker use of AI for phishing and reconnaissance. **[Low]** This is widely discussed, but I have no solid healthcare-specific evidence.

## 4. Patient-safety and operational impacts

- Common effects are EHR downtime, ambulance diversion, canceled procedures, delayed imaging and lab work, and reversion to paper. **[High]**
- Academic research indicates ransomware attacks spill over into neighboring hospitals' emergency departments. **[Medium–High]**
- One University of Minnesota-led study counted about 374 ransomware attacks on U.S. healthcare delivery organizations from 2016 to 2021, exposing tens of millions of patient records. **[Medium] [VERIFY]**
- Studies suggest higher in-hospital mortality among inpatients during attacks. **[Medium]** The magnitude is uncertain and I won't cite a figure. Causation is debated.
- Average breach cost: IBM/Ponemon has ranked healthcare highest among industries for years. The 2024 figure was about $9.8M, and the 2025 figure was lower, about $7.4M. **[Medium] [VERIFY]**
- Financial effects include lost revenue, cash-flow strain, class-action litigation, and regulatory scrutiny. **[High]**

## 5. Current constraints

- **Funding and staffing:** Rural and critical-access hospitals have thin margins and few security staff. **[High]**
  - Security spending as a share of IT budgets is often cited as low, but I am unsure of the percentage. **[Low] [VERIFY]**
- **No broad federal funding program** dedicated to hospital cyber defense exists as far as I know. **[Medium]**
- **Regulatory gap:** The current HIPAA Security Rule dates from 2003, with a 2013 update, and is non-prescriptive. HHS published voluntary Cybersecurity Performance Goals in Jan 2024. **[High]**
- **Federal capacity concerns:** There were 2025 reports of staffing and budget reductions affecting CISA and HHS cyber functions. **[Low–Medium] [VERIFY]** The operational impact is uncertain.
- **Information sharing:** The Cybersecurity Information Sharing Act of 2015 faced lapse and short-term extension in late 2025. **[Low] [VERIFY current status]**
- **Legacy technology:** Devices and systems that can't be easily patched or segmented. **[High]**

## 6. Planned and proposed developments

- **HIPAA Security Rule overhaul (HHS OCR NPRM):** Published around Dec 27, 2024 and in the Federal Register in Jan 2025. **[Medium–High]**
  - Proposed requirements: mandatory MFA, encryption, network segmentation, asset inventory, vulnerability scanning and pen testing, restoring critical systems within 72 hours, and annual compliance audits. **[Medium]**
  - Comment period closed in 2025. **[Medium]**
  - **Final rule status and date: UNKNOWN.** Industry groups, including hospital associations, opposed parts of it on cost. Whether it will be finalized, changed, or withdrawn is uncertain.
- **CIRCIA (CISA incident reporting):** Proposed rule issued April 2024. **[High]**
  - It would require reporting covered incidents within 72 hours and ransom payments within 24 hours. **[High]**
  - The final rule was expected in 2025, but I recall delays into 2026. **[Low–Medium] [VERIFY]**
  - Healthcare entities are expected to be covered. Exact applicability thresholds are uncertain.
- **State action:** New York's hospital cybersecurity regulation was finalized in late 2024, with a roughly one-year compliance window running into late 2025. **[Medium] [VERIFY]** Other states have proposals. **[Low]**
- **Congress:** Several bills have been proposed (for example, healthcare cybersecurity and resiliency acts, and proposals for minimum standards or funding).
  - Enactment status: **UNKNOWN**. I am not aware of any enacted.
- **Medical devices:** FDA's Section 524B cyber requirements for new device submissions have applied since 2023. **[High]**
- **Industry initiatives:** Health-ISAC sharing, the HSCC and 405(d) guidance, and increased cyber insurance underwriting requirements. **[Medium]**

## 7. Risks and outlook (my assessment, not established fact)

- Continued high likelihood of attacks. **[Medium–High]** Strong profit motive, sensitive data, and operational urgency make hospitals attractive.
- A repeat of a Change Healthcare-style single-point-of-failure event is plausible. **[Medium]**
- Law-enforcement disruptions cause only short-term dips as affiliates move to other groups. **[Medium]**
- Possible policy shifts, such as ransom-payment restrictions or mandatory reporting, could change attacker and victim behavior. **[Low]** Speculative.
- Cyber insurance costs and requirements may continue to tighten. **[Low–Medium]**
- Regulatory costs may burden small and rural hospitals if mandates arrive without funding. **[Medium]**

## 8. Summary of uncertainties

- Exact 2024–2025 healthcare ransomware counts (IC3, HHS, Comparitech, Sophos): **not confirmed**.
- Final affected-individual counts for Change Healthcare (about 190M) and Ascension (about 5.6M): **verify**.
- Final-rule timing for the HIPAA Security Rule update and CIRCIA: **unknown or uncertain**.
- Status of federal legislation and the Cybersecurity Information Sharing Act extension: **unknown**.
- Healthcare-specific ransom payment amounts and payment rate: **no reliable figure**.
- Attribution of specific 2025 incidents, and anything after roughly mid/late 2025: **low confidence**.

## 9. Recommended primary sources to verify

- HHS OCR Breach Portal
- FBI IC3 Annual Reports
- CISA/FBI/HHS advisories (#StopRansomware)
- Federal Register (HIPAA NPRM, CIRCIA)
- Health-ISAC
- Chainalysis Crypto Crime Report
- IBM Cost of a Data Breach
- Sophos State of Ransomware in Healthcare
- Company 8-K filings and notification letters