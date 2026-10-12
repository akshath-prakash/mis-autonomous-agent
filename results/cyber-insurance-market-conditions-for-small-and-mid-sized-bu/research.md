# Research Summary: Cyber Insurance Market Conditions for Small and Mid-Sized Businesses (SMBs)

**Method note and limits**
- This summary comes from my training knowledge. I had no live data access in this session, so nothing was checked against current sources.
- My knowledge thins out in late 2025, so anything after that is absent or unreliable.
- Confidence tags: **[High]** = well documented and stable. **[Medium]** = I recall it but exact figures or dates may be off. **[Low/Unverified]** = treat as a lead to check, not a fact.
- I have deliberately left out precise numbers I can't stand behind. Where a figure appears, it is approximate.

---

## 1. Market Cycle and Pricing

- **Hard market, 2020–2022 [High].** Ransomware losses drove sharp rate increases, tighter underwriting, lower limits, and some carriers withdrawing. Marsh's global index showed cyber rate increases above 100% in some 2021 quarters. *Exact quarterly figures: [Medium/uncertain].*
- **Stabilization in 2023, softening in 2024–2025 [Medium-High].** New capacity, better security controls among insureds, and lower ransomware severity at some carriers pushed rates flat to down. Reported decreases were typically single digits to low double digits. *Exact percentages by quarter and region: [uncertain].*
- **Premium volume [Medium].**
  - Global cyber premiums were roughly mid-teens of billions USD in 2024 (Munich Re estimate, about $15B). *Exact figure and forecasts: [uncertain].*
  - Industry forecasts expect continued growth, with some projecting a doubling by around 2030. *Treat as a forecast, not a fact.*
  - US NAIC data puts annual direct premiums in the high single-digit billions. *Year-by-year numbers: [uncertain].*
- **SMB-specific pricing [Low/Unverified].** I lack reliable SMB-only rate data. SMB pricing generally follows the overall market, but it is more driven by automated and scan-based underwriting. Check broker and MGA reports (Marsh, Aon, WTW, Coalition, Cowbell, At-Bay) for SMB segments.

## 2. Current Constraints for SMBs

**Underwriting and eligibility [High unless noted]**
- Baseline security controls are now commonly required or heavily weighted:
  - Multi-factor authentication (email, remote access, privileged accounts)
  - Endpoint detection and response (EDR)
  - Tested, offline or immutable backups
  - Patch management
  - Email filtering
  - Incident response planning and employee training
- Without MFA, applicants may be declined, face large premium loads, or receive ransomware sublimits.
- Many carriers and MGAs use outside-in scanning (open ports, exposed RDP, vulnerable software) as part of quoting. Findings can change price or eligibility.
- Industry exposure matters. Healthcare, education, municipal, manufacturing, and financial services are often scrutinized more. *Specific appetite changes: [uncertain].*

**Coverage limitations [High unless noted]**
- Ransomware sublimits and coinsurance clauses are common, especially for weaker risk profiles.
- Social engineering and funds-transfer-fraud coverage is often sublimited.
- Exclusions and restrictions that have appeared in many forms:
  - War and state-backed attack exclusions. Lloyd's required them in new and renewing policies from 31 March 2023 (market bulletins and LMA clauses 5564–5567). *Exact wording varies by insurer.*
  - Widespread or systemic event and infrastructure exclusions or sublimits.
  - "Failure to maintain" security standards conditions.
  - Limited coverage for bricking and betterment, and for contingent business interruption.
- **Legal uncertainty on war exclusions [Medium].** In Merck v. ACE (NotPetya), courts in New Jersey ruled against applying the war exclusion to a cyberattack. *Details and appeal status: [verify].* Mondelez v. Zurich settled in 2022.

**Awareness and affordability [Medium]**
- SMB take-up remains well below that of large enterprises. Many SMBs wrongly believe they are not targets, or assume general liability or property policies cover cyber losses. *Specific penetration percentages vary widely by survey: [uncertain].*
- Cost, complexity of applications, and uncertainty over what policies actually cover are the commonly cited barriers.

## 3. Market Structure and Capacity

- **MGAs and insurtechs dominate SMB distribution [Medium-High].** Examples: Coalition, At-Bay, Cowbell, Corvus (acquired by Travelers in 2024; *deal value about $435M: [Medium]*), Resilience. Large carriers (Chubb, Beazley, Hiscox, AXA XL, Tokio Marine HCC, Travelers) are also active. *Current market shares: [uncertain].*
- **Distribution trends [Medium].** Bundling with managed service providers (MSPs), embedding in software and security vendor offerings, and premium incentives for adopting security tools are growing.
- **Reinsurance and alternative capital [Medium].** Cyber cat bonds began in 2023 (Beazley was among the first, about $45M, *figure uncertain*). More issuances followed. Reinsurance terms softened in 2024–2025. *Details: [uncertain].*

## 4. Planned and Emerging Developments

**Regulatory and policy** *(check status of each; these change frequently)*
- **NYDFS Part 500 amendments [High].** Phased through 1 Nov 2025, including MFA and asset inventory requirements. These affect NY-regulated financial entities and indirectly their vendors and SMB suppliers.
- **CIRCIA (US critical-infrastructure incident reporting) [Medium].**
  - CISA issued a proposed rule in April 2024. It would require 72-hour incident reports and 24-hour ransom payment reports.
  - The final rule was expected in 2025 but I recall delays toward 2026. *Final timing and scope: [uncertain].*
- **HIPAA Security Rule update [Medium].** An NPRM was published in Jan 2025. *Finalization status: [unknown].*
- **EU [Medium-High].**
  - NIS2: transposition deadline Oct 2024, uneven member-state implementation.
  - DORA: applied from 17 Jan 2025.
  - Cyber Resilience Act: in force Dec 2024, with reporting obligations from about Sept 2026 and full application about Dec 2027. *Dates should be verified.*
- **UK [Low-Medium].** The government consulted in 2025 on ransomware measures (public-sector and critical-infrastructure payment bans, payment notification, mandatory reporting). A Cyber Security and Resilience Bill was announced. *Final outcomes and timing: [uncertain].*
- **US federal backstop for catastrophic cyber [Medium].** Treasury and GAO have studied the issue. No enacted cyber-specific backstop that I know of. TRIA expires 31 Dec 2027, and whether it covers cyber is ambiguous. *Any legislative movement since my cutoff: [unknown].*

**Product and underwriting trends [Medium; direction is clearer than timing]**
- Continuous monitoring and scanning, with pricing tied to security posture.
- Clearer language on systemic events and war, and possibly AI-related exclusions or affirmative coverage. *Prevalence: [uncertain].*
- Parametric and event-triggered cyber products, mostly niche for now.
- Expansion of packaged SMB products with embedded incident response services.

## 5. Risks and Threat Environment

- **Ransomware remains the dominant loss driver [High].**
  - Chainalysis estimated reported ransom payments fell in 2024 (about $814M vs about $1.25B in 2023; *[Medium]*). Reported payments may understate attack frequency, and payment declines don't equal fewer attacks or lower business-interruption costs.
  - Verizon's 2025 DBIR indicated ransomware appears in a very large share of SMB breaches (I recall about 88%, *[Medium-Low, verify]*).
- **Third-party and supply-chain risk [Medium-High].** Incidents such as MOVEit (2023), Change Healthcare (2024), and others show SMBs can be hit through vendors. SMB policies may have limited dependent-business coverage.
- **Systemic or aggregation events [High on existence, uncertain on size].**
  - The CrowdStrike outage (July 2024) was a non-malicious event with large insured loss estimates. *Estimates varied widely, from hundreds of millions to low billions USD: [uncertain].*
  - A cloud or software provider failure or widespread zero-day could trigger correlated losses and a market reversal.
- **AI-enabled threats [Medium].** Deepfake-driven social engineering, more convincing phishing, and faster vulnerability exploitation. The impact on loss frequency is not yet quantified. *[Uncertain.]*
- **Soft-market risk [Medium; my analytical judgment].** Falling rates while threat activity persists could produce under-pricing. A major event could cause a sharp correction, with SMB buyers possibly facing higher rates, narrower coverage, or reduced appetite. *Likelihood and timing: [unknown]. This is a risk scenario, not a prediction.*
- **Claims and litigation [Medium].** Disputes over exclusions (war, failure to maintain controls) and misrepresentation on applications (rescission risk) are a risk for SMBs that answer security questionnaires inaccurately.
- **Regulatory and privacy liability [Medium].** Growth in US state privacy laws, wiretapping and pixel-tracking litigation, and biometric claims (BIPA) can create coverage disputes. *Specifics: [verify].*

## 6. Timeline Snapshot

| Period | Event | Confidence |
|---|---|---|
| 2020–2022 | Hard market; ransomware surge; steep rate rises | High |
| 2022 | Mondelez v. Zurich settled; Lloyd's announces state-backed attack exclusion requirements | Medium-High |
| Mar 2023 | Lloyd's state-backed exclusion requirement takes effect | Medium-High |
| 2023 | Rates stabilize; first cyber cat bonds; Merck v. ACE ruling | Medium |
| Nov 2023 | NYDFS Part 500 amendments begin phase-in | High |
| 2024 | Rates soften; Travelers–Corvus deal; CrowdStrike outage (July); Change Healthcare attack; CIRCIA NPRM (Apr) | Medium-High |
| Jan 2025 | DORA applies; HIPAA Security Rule NPRM | Medium-High |
| Nov 2025 | NYDFS final phase-in milestones | High |
| ~2026 | CIRCIA final rule (expected, delayed); EU CRA reporting obligations (~Sept 2026) | Medium-Low |
| Dec 2027 | TRIA sunset | Medium-High |

## 7. Key Uncertainties and Gaps

- Current (2025–2026) SMB-specific rate trends, loss ratios, and take-up rates: **not known to me**.
- Exact premium volumes, market shares, and forecast numbers: **approximate only**.
- Whether a soft market continues or reverses: **unknown**.
- Final status and dates of CIRCIA, HIPAA update, and UK ransomware and cyber legislation: **verify**.
- Prevalence of AI-related exclusions or endorsements: **unverified**.
- Impact of major 2025 incidents on carrier appetite: **I'm unsure**.

## 8. Recommended Verification Sources

- Marsh Global Insurance Market Index; Aon, WTW, and Howden cyber reports
- NAIC cyber insurance market reports; Munich Re Cyber Insurance report
- Verizon DBIR, Sophos State of Ransomware, Chainalysis Crypto Crime report, Coalition and At-Bay claims reports
- CISA, NYDFS, HHS, EU Commission, and UK government pages for regulatory status
- Lloyd's market bulletins; A.M. Best, Fitch, and Swiss Re Institute commentary